<?php
// Infina AI - WordPress MCP server snippet (JSON-RPC 2.0, khong dung SSE)
// Dan doan nay vao WPCode -> PHP Snippet, Insert Method: Auto Insert, Location: Run Everywhere.
//
// KHONG dan secret that vao file nay, file nay nam trong git repo nen ai doc duoc
// repo se doc duoc secret. Set secret that bang 1 trong 2 cach sau (chon 1):
//
// Cach 1 (khuyen dung, can FTP/File Manager toi wp-config.php): mo wp-config.php,
// them dong duoi day o phia TREN dong "/* That's all, stop editing! */":
//   define( 'INFINA_MCP_SECRET', 'dan-secret-that-vao-day' );
//
// Cach 2 (khong dong wp-config.php): chay 1 lan qua WP-CLI hoac 1 snippet "Run Once":
//   update_option( 'infina_mcp_secret', 'dan-secret-that-vao-day', false );
//
// Sinh secret: php -r "echo bin2hex(random_bytes(24));"
//
// ============================ CAC TOOL ============================
//   list_posts     - liet ke bai theo trang thai (draft/publish/future/pending/private)
//   create_post    - tao bai: status = draft | publish | future (scheduled, kem 'date')
//   update_post    - sua bai bat ky + doi trang thai (draft/publish/future)
//   upload_media   - tai ANH tu URL https ve Media Library (chong SSRF)
//   delete_media   - xoa han 1 media (bo qua thung rac, xoa ca file goc)
// SEO: Rank Math. Media: chi anh. Khong ho tro xoa post (chi xoa media).
// =================================================================

function infina_mcp_get_secret() {
    if ( defined( 'INFINA_MCP_SECRET' ) && INFINA_MCP_SECRET !== '' ) {
        return INFINA_MCP_SECRET;
    }
    $option_secret = get_option( 'infina_mcp_secret', '' );
    return is_string( $option_secret ) ? $option_secret : '';
}

add_action( 'rest_api_init', function () {
    register_rest_route( 'infina-mcp/v1', '/blog', [
        'methods'             => 'POST',
        'callback'            => 'infina_mcp_handle_request',
        'permission_callback' => 'infina_mcp_check_permission',
    ] );
} );

function infina_mcp_check_permission( WP_REST_Request $request ) {
    $configured_secret = infina_mcp_get_secret();
    if ( $configured_secret === '' ) {
        return false; // chua cau hinh secret -> tu choi het
    }
    $key = (string) $request->get_param( 'key' );
    return hash_equals( $configured_secret, $key );
}

// ------------------------- Helpers -------------------------

function infina_mcp_url_is_safe_for_sideload( $url ) {
    $parsed = wp_parse_url( $url );
    if ( empty( $parsed['scheme'] ) || strtolower( $parsed['scheme'] ) !== 'https' || empty( $parsed['host'] ) ) {
        return false;
    }
    $host = $parsed['host'];
    if ( in_array( strtolower( $host ), [ 'localhost' ], true ) ) {
        return false;
    }
    $ip = filter_var( $host, FILTER_VALIDATE_IP ) ? $host : gethostbyname( $host );
    if ( $ip === $host && ! filter_var( $host, FILTER_VALIDATE_IP ) ) {
        return false; // khong resolve duoc hostname
    }
    if ( ! filter_var( $ip, FILTER_VALIDATE_IP, FILTER_FLAG_NO_PRIV_RANGE | FILTER_FLAG_NO_RES_RANGE ) ) {
        return false; // chan IP noi bo/private/reserved (SSRF)
    }
    return true;
}

// Tai 1 ANH tu URL ve Media Library, tra ve attachment_id (hoac WP_Error).
function infina_mcp_sideload_image( $url, $alt_text = '', $post_id = 0 ) {
    if ( ! infina_mcp_url_is_safe_for_sideload( $url ) ) {
        return new WP_Error( 'unsafe_url', 'URL anh khong hop le (phai la https) hoac tro toi dia chi noi bo, tu choi tai ve.' );
    }

    $head = wp_remote_head( $url, [ 'timeout' => 10 ] );
    if ( is_wp_error( $head ) ) {
        return $head;
    }
    $content_type = wp_remote_retrieve_header( $head, 'content-type' );
    if ( ! is_string( $content_type ) || strpos( $content_type, 'image/' ) !== 0 ) {
        return new WP_Error( 'not_image', 'URL khong tra ve content-type dang anh (image/*), tu choi tai ve.' );
    }

    require_once ABSPATH . 'wp-admin/includes/media.php';
    require_once ABSPATH . 'wp-admin/includes/file.php';
    require_once ABSPATH . 'wp-admin/includes/image.php';

    $attachment_id = media_sideload_image( $url, $post_id, $alt_text, 'id' );
    if ( is_wp_error( $attachment_id ) ) {
        return $attachment_id;
    }
    if ( ! empty( $alt_text ) ) {
        update_post_meta( $attachment_id, '_wp_attachment_image_alt', $alt_text );
    }
    return $attachment_id;
}

function infina_mcp_text_result( $text, $is_error = false ) {
    return [ 'isError' => (bool) $is_error, 'content' => [ [ 'type' => 'text', 'text' => $text ] ] ];
}

// category la taxonomy HIERARCHICAL -> wp_set_post_terms can TERM ID, khong nhan ten.
// Ham nay doi ten (hoac ID) thanh term_id: tim theo name (case-insensitive), roi slug,
// neu chua co thi tao moi. Tra ve mang term_id.
function infina_mcp_resolve_category_ids( $names ) {
    $ids = [];
    foreach ( (array) $names as $name ) {
        $name = trim( (string) $name );
        if ( $name === '' ) {
            continue;
        }
        if ( is_numeric( $name ) ) {
            $ids[] = (int) $name;
            continue;
        }
        $term = get_term_by( 'name', $name, 'category' );
        if ( ! $term ) {
            $term = get_term_by( 'slug', sanitize_title( $name ), 'category' );
        }
        if ( $term && ! is_wp_error( $term ) ) {
            $ids[] = (int) $term->term_id;
        } else {
            $new = wp_insert_term( $name, 'category' );
            if ( ! is_wp_error( $new ) && ! empty( $new['term_id'] ) ) {
                $ids[] = (int) $new['term_id'];
            }
        }
    }
    return array_values( array_unique( array_filter( $ids ) ) );
}

// Ap dung danh muc/tag/SEO/anh dai dien cho 1 post. Tra ve ghi chu ve anh (string).
function infina_mcp_apply_post_meta( $post_id, $args, $on_create = true ) {
    $isset = function ( $k ) use ( $args, $on_create ) {
        return $on_create ? ! empty( $args[ $k ] ) : array_key_exists( $k, $args );
    };

    if ( $isset( 'categories' ) ) {
        $cat_ids = infina_mcp_resolve_category_ids( $args['categories'] ); // ten -> term_id (tao neu chua co)
        wp_set_post_terms( $post_id, $cat_ids, 'category', false );
    }
    if ( $isset( 'tags' ) ) {
        // post_tag la non-hierarchical -> nhan ten truc tiep (tu tao neu chua co).
        wp_set_post_terms( $post_id, $args['tags'], 'post_tag', false );
    }
    if ( $isset( 'seo_title' ) ) {
        update_post_meta( $post_id, 'rank_math_title', $args['seo_title'] );
    }
    if ( $isset( 'seo_description' ) ) {
        update_post_meta( $post_id, 'rank_math_description', $args['seo_description'] );
    }
    if ( $isset( 'seo_focus_keyword' ) ) {
        update_post_meta( $post_id, 'rank_math_focus_keyword', $args['seo_focus_keyword'] );
    }

    $image_note = '';
    if ( ! empty( $args['image_url'] ) ) {
        $attachment_id = infina_mcp_sideload_image( $args['image_url'], $args['image_alt'] ?? '', $post_id );
        if ( is_wp_error( $attachment_id ) ) {
            $image_note = ' Luu y: tai anh dai dien that bai (' . $attachment_id->get_error_message() . ').';
        } else {
            set_post_thumbnail( $post_id, $attachment_id );
            $image_note = ' Da gan anh dai dien.';
        }
    }
    return $image_note;
}

// Chuan hoa & xac thuc status + date (cho create/update). Tra ve mang postarr-extra hoac WP_Error.
//   - status 'future'   : bat buoc 'date' o TUONG LAI  -> len lich (scheduled)
//   - status khac + date: dat post_date theo 'date', cho phep QUA KHU -> backdate publish
//   - khong co date      : de WP tu lay gio hien tai
function infina_mcp_resolve_status( $status, $date ) {
    $allowed = [ 'draft', 'publish', 'future', 'pending', 'private' ];
    $status  = strtolower( (string) $status );
    if ( ! in_array( $status, $allowed, true ) ) {
        return new WP_Error( 'bad_status', "status khong hop le. Cho phep: " . implode( ', ', $allowed ) );
    }
    $extra = [ 'post_status' => $status ];
    $date  = trim( (string) $date );

    if ( $status === 'future' ) {
        if ( $date === '' ) {
            return new WP_Error( 'need_date', "status 'future' can 'date' (gio dia phuong site, dinh dang 'YYYY-MM-DD HH:MM:SS')." );
        }
        $ts = strtotime( $date );
        if ( ! $ts ) {
            return new WP_Error( 'bad_date', "khong doc duoc 'date'. Dung 'YYYY-MM-DD HH:MM:SS'." );
        }
        if ( $ts <= strtotime( current_time( 'mysql' ) ) ) {
            return new WP_Error( 'past_date', "'date' phai o tuong lai de len lich (future)." );
        }
        $extra['post_date']     = date( 'Y-m-d H:i:s', $ts );
        $extra['post_date_gmt'] = get_gmt_from_date( $extra['post_date'] );
        $extra['edit_date']     = true;
    } elseif ( $date !== '' ) {
        // Backdate / dat ngay tuy y cho draft/publish/pending/private (cho phep qua khu).
        $ts = strtotime( $date );
        if ( ! $ts ) {
            return new WP_Error( 'bad_date', "khong doc duoc 'date'. Dung 'YYYY-MM-DD HH:MM:SS'." );
        }
        $extra['post_date']     = date( 'Y-m-d H:i:s', $ts );
        $extra['post_date_gmt'] = get_gmt_from_date( $extra['post_date'] );
        $extra['edit_date']     = true; // bat buoc de wp_update_post thuc su doi ngay
    }
    return $extra;
}

// ------------------------- Tool schema -------------------------

function infina_mcp_post_props( $for_update ) {
    $props = [
        'title'             => [ 'type' => 'string', 'description' => 'Tieu de bai viet' ],
        'content'           => [ 'type' => 'string', 'description' => 'Noi dung day du dang HTML' ],
        'status'            => [ 'type' => 'string', 'enum' => [ 'draft', 'publish', 'future', 'pending', 'private' ], 'description' => "Trang thai. 'future' = len lich (kem 'date')." ],
        'date'              => [ 'type' => 'string', 'description' => "Ngay dang (gio dia phuong site, 'YYYY-MM-DD HH:MM:SS'). status='future' -> phai TUONG LAI (len lich). status khac (publish/draft...) -> ngay bat ky, ke ca QUA KHU (backdate)." ],
        'excerpt'           => [ 'type' => 'string', 'description' => 'Tom tat, tuy chon' ],
        'slug'              => [ 'type' => 'string', 'description' => 'Duong dan URL, de trong se tu tao' ],
        'categories'        => [ 'type' => 'array', 'items' => [ 'type' => 'string' ], 'description' => 'Ten danh muc' ],
        'tags'              => [ 'type' => 'array', 'items' => [ 'type' => 'string' ], 'description' => 'Ten tag' ],
        'seo_title'         => [ 'type' => 'string', 'description' => 'Rank Math meta title' ],
        'seo_description'   => [ 'type' => 'string', 'description' => 'Rank Math meta description' ],
        'seo_focus_keyword' => [ 'type' => 'string', 'description' => 'Rank Math focus keyword' ],
        'image_url'         => [ 'type' => 'string', 'description' => 'URL anh https lam anh dai dien (featured image), tuy chon' ],
        'image_alt'         => [ 'type' => 'string', 'description' => 'Alt text cho anh dai dien, tuy chon' ],
    ];
    if ( $for_update ) {
        $props = [ 'post_id' => [ 'type' => 'integer', 'description' => 'ID bai can sua' ] ] + $props;
    }
    return $props;
}

function infina_mcp_tools_schema() {
    return [
        [
            'name'        => 'list_posts',
            'description' => 'Liet ke bai viet theo trang thai (draft, publish, future/scheduled, pending, private).',
            'inputSchema' => [
                'type'       => 'object',
                'properties' => [
                    'status' => [ 'type' => 'array', 'items' => [ 'type' => 'string', 'enum' => [ 'draft', 'publish', 'future', 'pending', 'private' ] ], 'description' => "Loc theo trang thai. De trong = tat ca cac trang thai tren." ],
                    'number' => [ 'type' => 'integer', 'description' => 'So bai can lay, mac dinh 20' ],
                    'search' => [ 'type' => 'string', 'description' => 'Tu khoa tim trong tieu de/noi dung, tuy chon' ],
                ],
            ],
        ],
        [
            'name'        => 'create_post',
            'description' => 'Tao bai viet moi. status = draft | publish | future (len lich, kem date) | pending | private. Kem danh muc, tag, SEO Rank Math, anh dai dien tuy chon.',
            'inputSchema' => [
                'type'       => 'object',
                'required'   => [ 'title', 'content' ],
                'properties' => infina_mcp_post_props( false ),
            ],
        ],
        [
            'name'        => 'update_post',
            'description' => 'Cap nhat 1 bai viet bat ky (draft/publish/scheduled): noi dung, danh muc, tag, SEO, anh dai dien, va co the DOI trang thai (draft/publish/future).',
            'inputSchema' => [
                'type'       => 'object',
                'required'   => [ 'post_id' ],
                'properties' => infina_mcp_post_props( true ),
            ],
        ],
        [
            'name'        => 'upload_media',
            'description' => 'Tai mot ANH tu URL https ve Media Library (chong SSRF, chi nhan content-type image/*). Tra ve media_id va source_url.',
            'inputSchema' => [
                'type'       => 'object',
                'required'   => [ 'image_url' ],
                'properties' => [
                    'image_url' => [ 'type' => 'string', 'description' => 'URL anh https' ],
                    'alt'       => [ 'type' => 'string', 'description' => 'Alt text, tuy chon' ],
                    'title'     => [ 'type' => 'string', 'description' => 'Tieu de media, tuy chon' ],
                ],
            ],
        ],
        [
            'name'        => 'delete_media',
            'description' => 'Xoa HAN mot media (attachment): bo qua thung rac, xoa ca file goc + cac ban resize. Khong the hoan tac. Chi xoa attachment, khong xoa post.',
            'inputSchema' => [
                'type'       => 'object',
                'required'   => [ 'media_id' ],
                'properties' => [
                    'media_id' => [ 'type' => 'integer', 'description' => 'ID cua media/attachment can xoa' ],
                ],
            ],
        ],
    ];
}

// ------------------------- Tool dispatch -------------------------

function infina_mcp_call_tool( $name, $args ) {

    if ( $name === 'list_posts' ) {
        $statuses = ! empty( $args['status'] ) && is_array( $args['status'] )
            ? $args['status']
            : [ 'draft', 'publish', 'future', 'pending', 'private' ];
        $q = [
            'post_type'   => 'post',
            'post_status' => $statuses,
            'numberposts' => isset( $args['number'] ) ? (int) $args['number'] : 20,
            'orderby'     => 'date',
            'order'       => 'DESC',
        ];
        if ( ! empty( $args['search'] ) ) {
            $q['s'] = (string) $args['search'];
        }
        $posts = get_posts( $q );
        if ( empty( $posts ) ) {
            return infina_mcp_text_result( 'Khong co bai nao khop.' );
        }
        $lines = array_map( function ( $p ) {
            $edit = admin_url( 'post.php?post=' . $p->ID . '&action=edit' );
            $link = get_permalink( $p );
            return "#{$p->ID} [{$p->post_status}] {$p->post_title} ({$p->post_date}) - {$edit}" . ( $link ? " | {$link}" : '' );
        }, $posts );
        return infina_mcp_text_result( implode( "\n", $lines ) );
    }

    if ( $name === 'create_post' ) {
        $resolved = infina_mcp_resolve_status( $args['status'] ?? 'draft', $args['date'] ?? '' );
        if ( is_wp_error( $resolved ) ) {
            return infina_mcp_text_result( 'Loi: ' . $resolved->get_error_message(), true );
        }

        $postarr = array_merge( [
            'post_title'   => $args['title'] ?? '',
            'post_content' => $args['content'] ?? '',
            'post_excerpt' => $args['excerpt'] ?? '',
            'post_name'    => $args['slug'] ?? '',
            'post_type'    => 'post',
            'post_author'  => 1,
        ], $resolved );

        $post_id = wp_insert_post( $postarr, true );
        if ( is_wp_error( $post_id ) ) {
            return infina_mcp_text_result( 'Loi: ' . $post_id->get_error_message(), true );
        }

        $image_note = infina_mcp_apply_post_meta( $post_id, $args, true );
        $edit_url   = admin_url( 'post.php?post=' . $post_id . '&action=edit' );
        $status     = get_post_status( $post_id );
        $link       = get_permalink( $post_id );
        return infina_mcp_text_result( "Da tao bai ID {$post_id} [status: {$status}].{$image_note} Sua: {$edit_url}" . ( $link ? " | Xem: {$link}" : '' ) );
    }

    if ( $name === 'update_post' ) {
        $post_id = isset( $args['post_id'] ) ? (int) $args['post_id'] : 0;
        if ( ! $post_id ) {
            return infina_mcp_text_result( 'Thieu post_id.', true );
        }
        $existing = get_post( $post_id );
        if ( ! $existing || $existing->post_type !== 'post' ) {
            return infina_mcp_text_result( "Khong tim thay bai post ID {$post_id}.", true );
        }

        $update = [ 'ID' => $post_id ];
        if ( isset( $args['title'] ) )   $update['post_title']   = $args['title'];
        if ( isset( $args['content'] ) ) $update['post_content'] = $args['content'];
        if ( isset( $args['excerpt'] ) ) $update['post_excerpt'] = $args['excerpt'];
        if ( isset( $args['slug'] ) )    $update['post_name']    = $args['slug'];

        if ( isset( $args['status'] ) ) {
            $resolved = infina_mcp_resolve_status( $args['status'], $args['date'] ?? '' );
            if ( is_wp_error( $resolved ) ) {
                return infina_mcp_text_result( 'Loi: ' . $resolved->get_error_message(), true );
            }
            $update = array_merge( $update, $resolved );
        }

        if ( count( $update ) > 1 ) {
            $result = wp_update_post( $update, true );
            if ( is_wp_error( $result ) ) {
                return infina_mcp_text_result( 'Loi: ' . $result->get_error_message(), true );
            }
        }

        $image_note = infina_mcp_apply_post_meta( $post_id, $args, false );
        $edit_url   = admin_url( 'post.php?post=' . $post_id . '&action=edit' );
        $status     = get_post_status( $post_id );
        $link       = get_permalink( $post_id );
        return infina_mcp_text_result( "Da cap nhat bai ID {$post_id} [status: {$status}].{$image_note} Sua: {$edit_url}" . ( $link ? " | Xem: {$link}" : '' ) );
    }

    if ( $name === 'upload_media' ) {
        $url = (string) ( $args['image_url'] ?? '' );
        if ( $url === '' ) {
            return infina_mcp_text_result( 'Thieu image_url.', true );
        }
        $attachment_id = infina_mcp_sideload_image( $url, $args['alt'] ?? '' );
        if ( is_wp_error( $attachment_id ) ) {
            return infina_mcp_text_result( 'Loi: ' . $attachment_id->get_error_message(), true );
        }
        if ( ! empty( $args['title'] ) ) {
            wp_update_post( [ 'ID' => $attachment_id, 'post_title' => $args['title'] ] );
        }
        $src = wp_get_attachment_url( $attachment_id );
        return infina_mcp_text_result( "Da tai anh. media_id: {$attachment_id} | source_url: {$src}" );
    }

    if ( $name === 'delete_media' ) {
        $media_id = isset( $args['media_id'] ) ? (int) $args['media_id'] : 0;
        if ( ! $media_id ) {
            return infina_mcp_text_result( 'Thieu media_id.', true );
        }
        if ( get_post_type( $media_id ) !== 'attachment' ) {
            return infina_mcp_text_result( "ID {$media_id} khong phai la media/attachment, tu choi xoa.", true );
        }
        $deleted = wp_delete_attachment( $media_id, true ); // true = xoa han, khong vao Trash
        if ( ! $deleted ) {
            return infina_mcp_text_result( "Xoa media ID {$media_id} that bai.", true );
        }
        return infina_mcp_text_result( "Da xoa han media ID {$media_id} (ca file goc + cac ban resize)." );
    }

    return infina_mcp_text_result( "Khong biet tool: {$name}", true );
}

// ------------------------- JSON-RPC handler -------------------------

function infina_mcp_handle_request( WP_REST_Request $request ) {
    $body = json_decode( $request->get_body(), true );

    if ( ! is_array( $body ) ) {
        return new WP_REST_Response( [
            'jsonrpc' => '2.0', 'id' => null,
            'error'   => [ 'code' => -32700, 'message' => 'Parse error' ],
        ], 200 );
    }

    $id     = $body['id'] ?? null;
    $method = $body['method'] ?? '';
    $params = $body['params'] ?? [];

    if ( strpos( $method, 'notifications/' ) === 0 ) {
        return new WP_REST_Response( null, 202 );
    }

    if ( $method === 'initialize' ) {
        return new WP_REST_Response( [
            'jsonrpc' => '2.0', 'id' => $id,
            'result'  => [
                'protocolVersion' => '2025-06-18',
                'capabilities'    => [ 'tools' => new stdClass() ],
                'serverInfo'      => [ 'name' => 'infina-blog', 'version' => '2.1.1' ],
            ],
        ], 200 );
    }

    if ( $method === 'ping' ) {
        return new WP_REST_Response( [ 'jsonrpc' => '2.0', 'id' => $id, 'result' => new stdClass() ], 200 );
    }

    if ( $method === 'tools/list' ) {
        return new WP_REST_Response( [
            'jsonrpc' => '2.0', 'id' => $id,
            'result'  => [ 'tools' => infina_mcp_tools_schema() ],
        ], 200 );
    }

    if ( $method === 'tools/call' ) {
        $name   = $params['name'] ?? '';
        $args   = $params['arguments'] ?? [];
        $result = infina_mcp_call_tool( $name, $args );
        return new WP_REST_Response( [ 'jsonrpc' => '2.0', 'id' => $id, 'result' => $result ], 200 );
    }

    return new WP_REST_Response( [
        'jsonrpc' => '2.0', 'id' => $id,
        'error'   => [ 'code' => -32601, 'message' => 'Method not found: ' . $method ],
    ], 200 );
}
