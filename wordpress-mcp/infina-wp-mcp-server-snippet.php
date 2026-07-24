<?php
// Infina AI - WordPress MCP server snippet (JSON-RPC 2.0, khong dung SSE)
// Dan doan nay vao WPCode -> PHP Snippet, Insert Method: Auto Insert, Location: Run Everywhere.
// (Neu truoc do co dan snippet cua plugin "MCP Adapter" thi xoa/di tat, khong can dung nua.)
//
// KHONG dan secret that vao file nay, file nay nam trong git repo nen ai doc duoc
// repo se doc duoc secret. Set secret that bang 1 trong 2 cach sau (chon 1):
//
// Cach 1 (khuyen dung, can FTP/File Manager toi wp-config.php): mo wp-config.php,
// them dong duoi day o phia TREN dong "/* That's all, stop editing! */":
//   define( 'INFINA_MCP_SECRET', 'dan-secret-that-vao-day' );
//
// Cach 2 (khong dong wp-config.php, dung khi khong co FTP): chay 1 lan qua WP-CLI
// neu host ho tro:
//   wp option update infina_mcp_secret "dan-secret-that-vao-day"
// hoac tao 1 snippet PHP KHAC trong WPCode, che do "Run Once", noi dung:
//   update_option( 'infina_mcp_secret', 'dan-secret-that-vao-day', false );
// roi xoa snippet "Run Once" do ngay sau khi da luu xong, khong de lai.
//
// Sinh secret ngau nhien an toan (chay tren may ca nhan, khong chay tren o web):
//   php -r "echo bin2hex(random_bytes(24));"

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
    // Chua cau hinh secret that thi tu choi tat ca, khong bao gio cho qua khi rong
    if ( $configured_secret === '' ) {
        return false;
    }
    $key = (string) $request->get_param( 'key' );
    return hash_equals( $configured_secret, $key );
}

function infina_mcp_url_is_safe_for_sideload( $url ) {
    $parsed = wp_parse_url( $url );
    if ( empty( $parsed['scheme'] ) || strtolower( $parsed['scheme'] ) !== 'https' || empty( $parsed['host'] ) ) {
        return false;
    }
    $host = $parsed['host'];
    // Chan thang cac dia chi IP hoac hostname noi bo pho bien, khong can resolve DNS
    if ( in_array( strtolower( $host ), [ 'localhost' ], true ) ) {
        return false;
    }
    $ip = filter_var( $host, FILTER_VALIDATE_IP ) ? $host : gethostbyname( $host );
    if ( $ip === $host && ! filter_var( $host, FILTER_VALIDATE_IP ) ) {
        return false; // khong resolve duoc hostname
    }
    // Chan IP noi bo/private/reserved de tranh SSRF vao mang noi bo cua host
    if ( ! filter_var( $ip, FILTER_VALIDATE_IP, FILTER_FLAG_NO_PRIV_RANGE | FILTER_FLAG_NO_RES_RANGE ) ) {
        return false;
    }
    return true;
}

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

function infina_mcp_tools_schema() {
    return [
        [
            'name'        => 'create_draft_post',
            'description' => 'Tao bai viet moi o trang thai draft cho blog Infina AI (infina.ai/news), kem danh muc, tag va SEO Rank Math tuy chon.',
            'inputSchema' => [
                'type'       => 'object',
                'required'   => [ 'title', 'content' ],
                'properties' => [
                    'title'             => [ 'type' => 'string', 'description' => 'Tieu de bai viet' ],
                    'content'           => [ 'type' => 'string', 'description' => 'Noi dung day du dang HTML' ],
                    'excerpt'           => [ 'type' => 'string', 'description' => 'Tom tat, tuy chon' ],
                    'slug'              => [ 'type' => 'string', 'description' => 'Duong dan URL, de trong se tu tao' ],
                    'categories'        => [ 'type' => 'array', 'items' => [ 'type' => 'string' ], 'description' => 'Ten danh muc' ],
                    'tags'              => [ 'type' => 'array', 'items' => [ 'type' => 'string' ], 'description' => 'Ten tag' ],
                    'seo_title'         => [ 'type' => 'string', 'description' => 'Rank Math meta title' ],
                    'seo_description'   => [ 'type' => 'string', 'description' => 'Rank Math meta description' ],
                    'seo_focus_keyword' => [ 'type' => 'string', 'description' => 'Rank Math focus keyword' ],
                    'image_url'         => [ 'type' => 'string', 'description' => 'URL anh https de tai ve va gan lam anh dai dien (featured image), tuy chon' ],
                    'image_alt'         => [ 'type' => 'string', 'description' => 'Alt text cho anh dai dien, nen chua tu khoa chinh, tuy chon' ],
                ],
            ],
        ],
        [
            'name'        => 'list_draft_posts',
            'description' => 'Liet ke cac bai viet dang o trang thai draft tren blog Infina AI.',
            'inputSchema' => [
                'type'       => 'object',
                'properties' => [
                    'number' => [ 'type' => 'integer', 'description' => 'So luong bai can lay, mac dinh 5' ],
                ],
            ],
        ],
        [
            'name'        => 'update_draft_post',
            'description' => 'Sua mot bai dang o trang thai draft: noi dung, danh muc, tag, SEO Rank Math, hoac gan/doi anh dai dien. Tu choi neu bai khong con la draft (da publish) de tranh chinh nham bai da len live.',
            'inputSchema' => [
                'type'       => 'object',
                'required'   => [ 'post_id' ],
                'properties' => [
                    'post_id'           => [ 'type' => 'integer', 'description' => 'ID bai draft can sua' ],
                    'title'             => [ 'type' => 'string', 'description' => 'Tieu de moi, tuy chon' ],
                    'content'           => [ 'type' => 'string', 'description' => 'Noi dung HTML moi, tuy chon' ],
                    'excerpt'           => [ 'type' => 'string', 'description' => 'Tom tat moi, tuy chon' ],
                    'slug'              => [ 'type' => 'string', 'description' => 'Slug moi, tuy chon' ],
                    'categories'        => [ 'type' => 'array', 'items' => [ 'type' => 'string' ], 'description' => 'Danh muc moi, tuy chon' ],
                    'tags'              => [ 'type' => 'array', 'items' => [ 'type' => 'string' ], 'description' => 'Tag moi, tuy chon' ],
                    'seo_title'         => [ 'type' => 'string', 'description' => 'Rank Math meta title moi, tuy chon' ],
                    'seo_description'   => [ 'type' => 'string', 'description' => 'Rank Math meta description moi, tuy chon' ],
                    'seo_focus_keyword' => [ 'type' => 'string', 'description' => 'Rank Math focus keyword moi, tuy chon' ],
                    'image_url'         => [ 'type' => 'string', 'description' => 'URL anh https de tai ve va gan/doi lam anh dai dien, tuy chon' ],
                    'image_alt'         => [ 'type' => 'string', 'description' => 'Alt text cho anh dai dien, tuy chon' ],
                ],
            ],
        ],
    ];
}

function infina_mcp_call_tool( $name, $args ) {
    if ( $name === 'create_draft_post' ) {
        $post_id = wp_insert_post( [
            'post_title'   => $args['title'] ?? '',
            'post_content' => $args['content'] ?? '',
            'post_excerpt' => $args['excerpt'] ?? '',
            'post_name'    => $args['slug'] ?? '',
            'post_status'  => 'draft',
            'post_type'    => 'post',
            'post_author'  => 1,
        ], true );

        if ( is_wp_error( $post_id ) ) {
            return [ 'isError' => true, 'content' => [ [ 'type' => 'text', 'text' => 'Loi: ' . $post_id->get_error_message() ] ] ];
        }

        if ( ! empty( $args['categories'] ) ) {
            wp_set_post_terms( $post_id, $args['categories'], 'category' );
        }
        if ( ! empty( $args['tags'] ) ) {
            wp_set_post_terms( $post_id, $args['tags'], 'post_tag' );
        }
        if ( ! empty( $args['seo_title'] ) ) {
            update_post_meta( $post_id, 'rank_math_title', $args['seo_title'] );
        }
        if ( ! empty( $args['seo_description'] ) ) {
            update_post_meta( $post_id, 'rank_math_description', $args['seo_description'] );
        }
        if ( ! empty( $args['seo_focus_keyword'] ) ) {
            update_post_meta( $post_id, 'rank_math_focus_keyword', $args['seo_focus_keyword'] );
        }

        $image_note = '';
        if ( ! empty( $args['image_url'] ) ) {
            $attachment_id = infina_mcp_sideload_image( $args['image_url'], $args['image_alt'] ?? '', $post_id );
            if ( is_wp_error( $attachment_id ) ) {
                $image_note = ' Luu y: tai anh dai dien that bai (' . $attachment_id->get_error_message() . '), can tu them anh thu cong.';
            } else {
                set_post_thumbnail( $post_id, $attachment_id );
                $image_note = ' Da tai va gan anh dai dien tu image_url.';
            }
        }

        $edit_url = admin_url( 'post.php?post=' . $post_id . '&action=edit' );
        return [
            'isError' => false,
            'content' => [ [ 'type' => 'text', 'text' => "Da tao bai draft ID {$post_id}.{$image_note} Mo tai: {$edit_url}" ] ],
        ];
    }

    if ( $name === 'update_draft_post' ) {
        $post_id = isset( $args['post_id'] ) ? (int) $args['post_id'] : 0;
        if ( ! $post_id ) {
            return [ 'isError' => true, 'content' => [ [ 'type' => 'text', 'text' => 'Thieu post_id.' ] ] ];
        }

        $existing = get_post( $post_id );
        if ( ! $existing ) {
            return [ 'isError' => true, 'content' => [ [ 'type' => 'text', 'text' => "Khong tim thay bai ID {$post_id}." ] ] ];
        }
        if ( $existing->post_status !== 'draft' ) {
            return [ 'isError' => true, 'content' => [ [ 'type' => 'text', 'text' => "Bai ID {$post_id} khong con o trang thai draft (dang la '{$existing->post_status}'), tu choi sua de tranh dung nham vao bai da publish." ] ] ];
        }

        $update = [ 'ID' => $post_id ];
        if ( isset( $args['title'] ) )   $update['post_title']   = $args['title'];
        if ( isset( $args['content'] ) ) $update['post_content'] = $args['content'];
        if ( isset( $args['excerpt'] ) ) $update['post_excerpt'] = $args['excerpt'];
        if ( isset( $args['slug'] ) )    $update['post_name']    = $args['slug'];

        if ( count( $update ) > 1 ) {
            $result = wp_update_post( $update, true );
            if ( is_wp_error( $result ) ) {
                return [ 'isError' => true, 'content' => [ [ 'type' => 'text', 'text' => 'Loi: ' . $result->get_error_message() ] ] ];
            }
        }

        if ( isset( $args['categories'] ) ) {
            wp_set_post_terms( $post_id, $args['categories'], 'category' );
        }
        if ( isset( $args['tags'] ) ) {
            wp_set_post_terms( $post_id, $args['tags'], 'post_tag' );
        }
        if ( isset( $args['seo_title'] ) ) {
            update_post_meta( $post_id, 'rank_math_title', $args['seo_title'] );
        }
        if ( isset( $args['seo_description'] ) ) {
            update_post_meta( $post_id, 'rank_math_description', $args['seo_description'] );
        }
        if ( isset( $args['seo_focus_keyword'] ) ) {
            update_post_meta( $post_id, 'rank_math_focus_keyword', $args['seo_focus_keyword'] );
        }

        $image_note = '';
        if ( ! empty( $args['image_url'] ) ) {
            $attachment_id = infina_mcp_sideload_image( $args['image_url'], $args['image_alt'] ?? '', $post_id );
            if ( is_wp_error( $attachment_id ) ) {
                $image_note = ' Luu y: tai anh dai dien that bai (' . $attachment_id->get_error_message() . ').';
            } else {
                set_post_thumbnail( $post_id, $attachment_id );
                $image_note = ' Da cap nhat anh dai dien.';
            }
        }

        $edit_url = admin_url( 'post.php?post=' . $post_id . '&action=edit' );
        return [
            'isError' => false,
            'content' => [ [ 'type' => 'text', 'text' => "Da cap nhat bai draft ID {$post_id}.{$image_note} Mo tai: {$edit_url}" ] ],
        ];
    }

    if ( $name === 'list_draft_posts' ) {
        $posts = get_posts( [
            'post_status' => 'draft',
            'numberposts' => $args['number'] ?? 5,
            'orderby'     => 'date',
            'order'       => 'DESC',
        ] );

        if ( empty( $posts ) ) {
            return [ 'isError' => false, 'content' => [ [ 'type' => 'text', 'text' => 'Chua co bai draft nao.' ] ] ];
        }

        $lines = array_map( function ( $p ) {
            $edit_url = admin_url( 'post.php?post=' . $p->ID . '&action=edit' );
            return "#{$p->ID} - {$p->post_title} ({$p->post_date}) - {$edit_url}";
        }, $posts );

        return [ 'isError' => false, 'content' => [ [ 'type' => 'text', 'text' => implode( "\n", $lines ) ] ] ];
    }

    return [ 'isError' => true, 'content' => [ [ 'type' => 'text', 'text' => "Khong biet tool: {$name}" ] ] ];
}

function infina_mcp_handle_request( WP_REST_Request $request ) {
    $body = json_decode( $request->get_body(), true );

    if ( ! is_array( $body ) ) {
        return new WP_REST_Response( [
            'jsonrpc' => '2.0',
            'id'      => null,
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
            'jsonrpc' => '2.0',
            'id'      => $id,
            'result'  => [
                'protocolVersion' => '2025-06-18',
                'capabilities'    => [ 'tools' => new stdClass() ],
                'serverInfo'      => [ 'name' => 'infina-blog', 'version' => '1.0.0' ],
            ],
        ], 200 );
    }

    if ( $method === 'ping' ) {
        return new WP_REST_Response( [ 'jsonrpc' => '2.0', 'id' => $id, 'result' => new stdClass() ], 200 );
    }

    if ( $method === 'tools/list' ) {
        return new WP_REST_Response( [
            'jsonrpc' => '2.0',
            'id'      => $id,
            'result'  => [ 'tools' => infina_mcp_tools_schema() ],
        ], 200 );
    }

    if ( $method === 'tools/call' ) {
        $name   = $params['name'] ?? '';
        $args   = $params['arguments'] ?? [];
        $result = infina_mcp_call_tool( $name, $args );
        return new WP_REST_Response( [
            'jsonrpc' => '2.0',
            'id'      => $id,
            'result'  => $result,
        ], 200 );
    }

    return new WP_REST_Response( [
        'jsonrpc' => '2.0',
        'id'      => $id,
        'error'   => [ 'code' => -32601, 'message' => 'Method not found: ' . $method ],
    ], 200 );
}
