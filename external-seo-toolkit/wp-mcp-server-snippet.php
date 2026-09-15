<?php
// Xoa het cac snippet MCP cu da dan truoc do (ca hai ban lien quan den mcp-adapter)
// Co the tat luon plugin "MCP Adapter" trong Plugins, khong can dung nua
// Dan doan nay vao WPCode, PHP Snippet, Insert Method: Auto Insert, Location: Run Everywhere
//
// KHONG dan secret that vao file nay, file nay nam trong git repo nen ai doc duoc
// repo se doc duoc secret. Set secret that bang 1 trong 2 cach sau (chon 1):
//
// Cach 1 (khuyen dung, can FTP/File Manager toi wp-config.php): mo wp-config.php,
// them dong duoi day o phia TREN dong "/* That's all, stop editing! */":
//   define( 'SEO_MCP_SECRET', 'dan-secret-that-vao-day' );
//
// Cach 2 (khong dong wp-config.php, dung khi khong co FTP): chay 1 lan qua WP-CLI
// neu host ho tro:
//   wp option update seo_mcp_secret "dan-secret-that-vao-day"
// hoac tao 1 snippet PHP KHAC trong WPCode, che do "Run Once", noi dung:
//   update_option( 'seo_mcp_secret', 'dan-secret-that-vao-day', false );
// roi xoa snippet "Run Once" do ngay sau khi da luu xong, khong de lai.
//
// Sinh secret ngau nhien an toan (chay tren may ca nhan, khong chay tren o web):
//   php -r "echo bin2hex(random_bytes(24));"

function seo_mcp_get_secret() {
    if ( defined( 'SEO_MCP_SECRET' ) && SEO_MCP_SECRET !== '' ) {
        return SEO_MCP_SECRET;
    }
    $option_secret = get_option( 'seo_mcp_secret', '' );
    return is_string( $option_secret ) ? $option_secret : '';
}

add_action( 'rest_api_init', function () {
    register_rest_route( 'seo-mcp/v1', '/blog', [
        'methods'             => 'POST',
        'callback'            => 'seo_mcp_handle_request',
        'permission_callback' => 'seo_mcp_check_permission',
    ] );
} );

// ---- Cloak link affiliate qua /go/<slug> ----
// Muc dich: giu link equity khong ro ra ngoai site khi co nhieu san pham cau noi
// tro thang ra site affiliate ngoai, va de quan ly hang loat khi link affiliate doi. Xem
// guideline affiliate cloak link cua ban (neu co).
add_action( 'init', function () {
    add_rewrite_rule( '^go/([^/]+)/?$', 'index.php?seo_go=$matches[1]', 'top' );

    // Flush rewrite rules dung 1 lan sau khi rule tren duoc dang ky, khong flush
    // moi request (ton hieu nang). Tang so version o ten option neu sau nay sua
    // lai pattern rewrite, de buoc flush lai 1 lan nua.
    if ( ! get_option( 'seo_go_rewrite_flushed_v1' ) ) {
        flush_rewrite_rules( false );
        update_option( 'seo_go_rewrite_flushed_v1', 1, false );
    }
} );

add_filter( 'query_vars', function ( $vars ) {
    $vars[] = 'seo_go';
    return $vars;
} );

add_action( 'template_redirect', function () {
    $slug = get_query_var( 'seo_go' );
    if ( empty( $slug ) ) {
        return;
    }
    $redirects = get_option( 'seo_go_redirects', [] );
    if ( ! is_array( $redirects ) || empty( $redirects[ $slug ] ) ) {
        status_header( 404 );
        nocache_headers();
        wp_die( 'Khong tim thay link redirect nay.', 'Khong tim thay', [ 'response' => 404 ] );
    }
    wp_redirect( $redirects[ $slug ], 301 );
    exit;
} );

// ---- In FAQPage schema (JSON-LD) tu code, doc lap voi Rank Math ----
// Dung khi Rank Math ban free khong ho tro mau FAQ (can Pro). Day la khoi
// <script> RIENG, khong dung/sua khoi @graph cua Rank Math (Organization,
// Product, BreadcrumbList...), Google ho tro nhieu khoi JSON-LD tach biet
// tren cung 1 trang. Du lieu FAQ luu qua tool set_product_faq/delete_product_faq.
add_action( 'wp_head', function () {
    if ( ! function_exists( 'is_product' ) || ! is_product() ) {
        return;
    }
    $product_id = get_the_ID();
    if ( ! $product_id ) {
        return;
    }
    $raw = get_post_meta( $product_id, '_seo_faq_schema', true );
    if ( empty( $raw ) ) {
        return;
    }
    $faqs = json_decode( $raw, true );
    if ( ! is_array( $faqs ) || empty( $faqs ) ) {
        return;
    }

    $entities = [];
    foreach ( $faqs as $item ) {
        if ( empty( $item['question'] ) || empty( $item['answer'] ) ) {
            continue;
        }
        $entities[] = [
            '@type'          => 'Question',
            'name'           => $item['question'],
            'acceptedAnswer' => [
                '@type' => 'Answer',
                'text'  => $item['answer'],
            ],
        ];
    }
    if ( empty( $entities ) ) {
        return;
    }

    $schema = [
        '@context'   => 'https://schema.org',
        '@type'      => 'FAQPage',
        'mainEntity' => $entities,
    ];

    echo "\n" . '<script type="application/ld+json">' . wp_json_encode( $schema, JSON_UNESCAPED_UNICODE | JSON_UNESCAPED_SLASHES ) . '</script>' . "\n";
} );

// Chan bot crawl thang vao /go/..., day la buoc quan trong nhat cua ky thuat
// cloak link: Google se thay link noi bo /go/... nhung khong crawl tiep de thay
// dia chi that, nen khong tinh outbound link/rò link equity ra ngoai site.
//
// QUAN TRONG: khong duoc chi ".= " noi vao cuoi $output, vi plugin SEO (Rank Math)
// co the da tu them dong trong + "Sitemap: ..." vao cuoi truoc do (thu tu phu
// thuoc priority filter, khong dam bao). Neu Disallow: /go/ roi xuong duoi dong
// Sitemap/dong trong, no khong con thuoc nhom "User-agent: *" nua, nhieu crawler
// se bo qua dong do (da xac nhan thuc te tren robots.txt live 2026-09-14). Luon
// chen ngay TRUOC dong "Sitemap:" dau tien (hoac truoc dong trong dau tien) de
// chac chan van con trong nhom User-agent: * dung dau file.
add_filter( 'robots_txt', function ( $output, $public ) {
    if ( '1' !== (string) $public ) {
        return $output;
    }
    if ( false !== strpos( $output, "Disallow: /go/" ) ) {
        return $output; // da co roi, tranh chen trung neu filter chay 2 lan
    }

    // Uu tien chen TRUOC dong trong dau tien (ranh gioi ket thuc nhom
    // "User-agent: *"), vi day moi la vi tri con thuoc dung nhom. Chi fallback
    // sang truoc dong "Sitemap:" neu khong tim thay dong trong nao (truong hop
    // hiem, output khong co blank line).
    $line = "Disallow: /go/\n";
    if ( preg_match( '/\n[ \t]*\n/', $output, $m, PREG_OFFSET_CAPTURE ) ) {
        $pos    = $m[0][1] + 1; // ngay sau ky tu \n dau tien cua chuoi dong trong, tuc TRUOC dong trong
        $output = substr( $output, 0, $pos ) . $line . substr( $output, $pos );
    } elseif ( preg_match( '/^Sitemap:/mi', $output, $m, PREG_OFFSET_CAPTURE ) ) {
        $pos    = $m[0][1];
        $output = substr( $output, 0, $pos ) . $line . substr( $output, $pos );
    } else {
        $output = rtrim( $output, "\n" ) . "\n" . $line;
    }

    return $output;
}, 10, 2 );

function seo_mcp_check_permission( WP_REST_Request $request ) {
    $configured_secret = seo_mcp_get_secret();
    // Chua cau hinh secret that thi tu choi tat ca, khong bao gio cho qua khi rong
    if ( $configured_secret === '' ) {
        return false;
    }
    $key = (string) $request->get_param( 'key' );
    return hash_equals( $configured_secret, $key );
}

function seo_mcp_url_is_safe_for_sideload( $url ) {
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

function seo_mcp_sideload_image( $url, $alt_text = '', $post_id = 0 ) {
    if ( ! seo_mcp_url_is_safe_for_sideload( $url ) ) {
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

/**
 * Ap dung status publish/future cho 1 bai viet, tu dong xu ly ngay gio:
 * - status=future nhung khong co publish_date hop le => loi (bat buoc phai co ngay).
 * - status=future voi ngay trong qua khu, hoac status=publish voi ngay trong tuong lai,
 *   se tu dieu chinh lai status cho khop de tranh WordPress tu suy dien sai (vd future
 *   voi ngay qua khu bi WP tu chuyen ve publish ngay lap tuc, gay dang som ngoai y muon).
 * Tra ve status cuoi cung (string) hoac WP_Error.
 */
function seo_mcp_apply_publish_status( $post_id, $requested_status, $publish_date ) {
    $now = current_time( 'timestamp' );

    if ( $requested_status === 'future' ) {
        if ( empty( $publish_date ) ) {
            return new WP_Error( 'missing_date', 'status future can publish_date' );
        }
        $ts = strtotime( $publish_date );
        if ( ! $ts ) {
            return new WP_Error( 'invalid_date', 'publish_date khong hop le' );
        }
        $final_status = $ts > $now ? 'future' : 'publish';
        $update       = [
            'ID'            => $post_id,
            'post_status'   => $final_status,
            'post_date'     => date( 'Y-m-d H:i:s', $ts ),
            'post_date_gmt' => get_gmt_from_date( date( 'Y-m-d H:i:s', $ts ) ),
            'edit_date'     => true,
        ];
    } elseif ( $requested_status === 'publish' ) {
        if ( ! empty( $publish_date ) ) {
            $ts = strtotime( $publish_date );
            if ( $ts && $ts > $now ) {
                $update = [
                    'ID'            => $post_id,
                    'post_status'   => 'future',
                    'post_date'     => date( 'Y-m-d H:i:s', $ts ),
                    'post_date_gmt' => get_gmt_from_date( date( 'Y-m-d H:i:s', $ts ) ),
                    'edit_date'     => true,
                ];
                $final_status = 'future';
            } else {
                $update       = [ 'ID' => $post_id, 'post_status' => 'publish' ];
                $final_status = 'publish';
            }
        } else {
            $update       = [ 'ID' => $post_id, 'post_status' => 'publish' ];
            $final_status = 'publish';
        }
    } else {
        return new WP_Error( 'invalid_status', 'status phai la future hoac publish' );
    }

    $result = wp_update_post( $update, true );
    if ( is_wp_error( $result ) ) {
        return $result;
    }

    return $final_status;
}

function seo_mcp_upload_media_from_base64( $filename, $base64_data, $mime_type = '', $alt_text = '' ) {
    $allowed_mimes = [
        'image/png'  => 'png',
        'image/jpeg' => 'jpg',
        'image/webp' => 'webp',
        'image/gif'  => 'gif',
    ];

    if ( empty( $base64_data ) ) {
        return new WP_Error( 'missing_data', 'Thieu base64_data.' );
    }

    // Cho phep truyen ca dang data URI (data:image/png;base64,....) lan base64 thuan
    if ( preg_match( '#^data:([a-zA-Z0-9/+.-]+);base64,(.+)$#s', $base64_data, $m ) ) {
        if ( empty( $mime_type ) ) {
            $mime_type = $m[1];
        }
        $base64_data = $m[2];
    }

    if ( empty( $mime_type ) || ! isset( $allowed_mimes[ $mime_type ] ) ) {
        return new WP_Error( 'bad_mime', 'mime_type khong hop le, chi cho phep: ' . implode( ', ', array_keys( $allowed_mimes ) ) );
    }

    $decoded = base64_decode( $base64_data, true );
    if ( $decoded === false ) {
        return new WP_Error( 'bad_base64', 'base64_data khong decode duoc, kiem tra lai chuoi base64.' );
    }

    $max_bytes = 20 * 1024 * 1024; // gioi han 20MB moi anh
    if ( strlen( $decoded ) > $max_bytes ) {
        return new WP_Error( 'too_large', 'Anh vuot qua gioi han 20MB.' );
    }

    $ext = $allowed_mimes[ $mime_type ];
    $safe_name = sanitize_file_name( ! empty( $filename ) ? $filename : ( 'blog-upload.' . $ext ) );
    if ( ! preg_match( '/\.' . preg_quote( $ext, '/' ) . '$/i', $safe_name ) ) {
        $safe_name .= '.' . $ext;
    }

    require_once ABSPATH . 'wp-admin/includes/media.php';
    require_once ABSPATH . 'wp-admin/includes/file.php';
    require_once ABSPATH . 'wp-admin/includes/image.php';

    $upload = wp_upload_bits( $safe_name, null, $decoded );
    if ( ! empty( $upload['error'] ) ) {
        return new WP_Error( 'upload_failed', $upload['error'] );
    }

    $attachment = [
        'post_mime_type' => $mime_type,
        'post_title'      => preg_replace( '/\.[^.]+$/', '', $safe_name ),
        'post_content'    => '',
        'post_status'     => 'inherit',
    ];

    $attachment_id = wp_insert_attachment( $attachment, $upload['file'] );
    if ( is_wp_error( $attachment_id ) ) {
        return $attachment_id;
    }

    $attachment_data = wp_generate_attachment_metadata( $attachment_id, $upload['file'] );
    wp_update_attachment_metadata( $attachment_id, $attachment_data );

    if ( ! empty( $alt_text ) ) {
        update_post_meta( $attachment_id, '_wp_attachment_image_alt', $alt_text );
    }

    return [
        'attachment_id' => $attachment_id,
        'url'           => wp_get_attachment_url( $attachment_id ),
    ];
}

function seo_mcp_wc_ready() {
    return function_exists( 'wc_get_product' ) && function_exists( 'wc_create_attribute' );
}

/**
 * Gop image_urls (mang string URL) va image_uploads (mang object base64) thanh 1 danh
 * sach item chuan hoa theo dung thu tu: image_urls truoc, image_uploads sau. Item dau
 * tien trong danh sach tra ve se dung lam anh dai dien, con lai vao gallery.
 */
function seo_mcp_normalize_image_inputs( $image_urls, $image_uploads ) {
    $items = [];
    if ( ! empty( $image_urls ) && is_array( $image_urls ) ) {
        foreach ( $image_urls as $url ) {
            $items[] = [ 'url' => $url ];
        }
    }
    if ( ! empty( $image_uploads ) && is_array( $image_uploads ) ) {
        foreach ( $image_uploads as $upload ) {
            $items[] = $upload; // da co san base64_data/mime_type/filename/alt
        }
    }
    return $items;
}

/**
 * Resolve 1 item anh (tu seo_mcp_normalize_image_inputs) thanh attachment_id,
 * uu tien url (sideload) truoc, khong co url thi thu base64_data (upload truc tiep).
 */
function seo_mcp_resolve_one_image( $item, $post_id = 0 ) {
    if ( ! empty( $item['url'] ) ) {
        return seo_mcp_sideload_image( $item['url'], $item['alt'] ?? '', $post_id );
    }
    if ( ! empty( $item['base64_data'] ) ) {
        $result = seo_mcp_upload_media_from_base64(
            $item['filename'] ?? '',
            $item['base64_data'],
            $item['mime_type'] ?? '',
            $item['alt'] ?? ''
        );
        if ( is_wp_error( $result ) ) {
            return $result;
        }
        if ( $post_id ) {
            wp_update_post( [ 'ID' => $result['attachment_id'], 'post_parent' => $post_id ] );
        }
        return $result['attachment_id'];
    }
    return new WP_Error( 'no_image_source', 'Item anh can co url hoac base64_data.' );
}

/**
 * Resolve tap hop image_urls + image_uploads thanh danh sach attachment_id, gan lam
 * anh dai dien (item dau) + gallery (con lai) cho 1 san pham. Tra ve mang
 * [ 'ids' => [...], 'attempted' => int, 'failed' => int ], khong bao gio tra loi cung
 * (mot vai anh loi khong duoc chan viec tao/sua san pham).
 */
function seo_mcp_apply_product_images( $product, $post_id, $image_urls, $image_uploads, $gallery_mode = 'replace' ) {
    $items = seo_mcp_normalize_image_inputs( $image_urls, $image_uploads );
    if ( empty( $items ) ) {
        return [ 'ids' => [], 'attempted' => 0, 'failed' => 0 ];
    }

    $ids    = [];
    $failed = 0;
    foreach ( $items as $item ) {
        $result = seo_mcp_resolve_one_image( $item, $post_id );
        if ( is_wp_error( $result ) ) {
            $failed++;
            continue;
        }
        $ids[] = (int) $result;
    }

    if ( ! empty( $ids ) ) {
        $product->set_image_id( $ids[0] );
        $rest = array_slice( $ids, 1 );
        if ( 'append' === $gallery_mode ) {
            $rest = array_values( array_unique( array_merge( $product->get_gallery_image_ids(), $rest ) ) );
        }
        $product->set_gallery_image_ids( $rest );
    }

    return [ 'ids' => $ids, 'attempted' => count( $items ), 'failed' => $failed ];
}

/**
 * Dam bao 1 global product attribute (vd "Mau sac") va cac term gia tri (vd "Den",
 * "Trang") da ton tai, tao moi neu chua co. Tra ve [ 'taxonomy' => 'pa_...',
 * 'term_ids' => [...] ] hoac WP_Error.
 */
function seo_mcp_ensure_product_attribute( $name, $options ) {
    if ( empty( $name ) || empty( $options ) || ! is_array( $options ) ) {
        return new WP_Error( 'bad_attribute', 'Attribute can co name va options (mang gia tri).' );
    }

    $slug     = wc_sanitize_taxonomy_name( $name );
    $taxonomy = 'pa_' . $slug;

    if ( ! taxonomy_exists( $taxonomy ) ) {
        $attribute_id = wc_attribute_taxonomy_id_by_name( $slug );
        if ( ! $attribute_id ) {
            $attribute_id = wc_create_attribute( [
                'name'         => $name,
                'slug'         => $slug,
                'type'         => 'select',
                'order_by'     => 'menu_order',
                'has_archives' => false,
            ] );
            if ( is_wp_error( $attribute_id ) ) {
                return $attribute_id;
            }
        }
        // Attribute vua tao chua duoc dang ky taxonomy trong request nay (WooCommerce
        // thuong dang ky luc init), dang ky lai ngay de dung duoc luon khong can doi
        // reload trang.
        delete_transient( 'wc_attribute_taxonomies' );
        foreach ( wc_get_attribute_taxonomies() as $tax ) {
            $tax_name = wc_attribute_taxonomy_name( $tax->attribute_name );
            if ( ! taxonomy_exists( $tax_name ) ) {
                register_taxonomy( $tax_name, 'product', [ 'hierarchical' => false, 'show_ui' => false, 'query_var' => true ] );
            }
        }
    }

    $term_ids = [];
    foreach ( $options as $option_name ) {
        $term = get_term_by( 'name', $option_name, $taxonomy );
        if ( ! $term ) {
            $inserted = wp_insert_term( $option_name, $taxonomy );
            if ( is_wp_error( $inserted ) ) {
                return $inserted;
            }
            $term_ids[] = (int) $inserted['term_id'];
        } else {
            $term_ids[] = (int) $term->term_id;
        }
    }

    return [ 'taxonomy' => $taxonomy, 'term_ids' => $term_ids ];
}

/**
 * Xay dung mang WC_Product_Attribute tu input dang
 * [ [ 'name' => 'Mau sac', 'options' => ['Den','Trang'], 'used_for_variation' => true ] ],
 * tu tao attribute/term global neu chua co. Tra ve mang WC_Product_Attribute hoac WP_Error.
 */
function seo_mcp_build_variable_attributes( $attributes_input ) {
    if ( empty( $attributes_input ) || ! is_array( $attributes_input ) ) {
        return new WP_Error( 'missing_attributes', 'San pham type=variable can attributes.' );
    }

    $attributes = [];
    $position   = 0;
    foreach ( $attributes_input as $attr ) {
        $name    = $attr['name'] ?? '';
        $options = $attr['options'] ?? [];

        $resolved = seo_mcp_ensure_product_attribute( $name, $options );
        if ( is_wp_error( $resolved ) ) {
            return $resolved;
        }

        $attribute_id = wc_attribute_taxonomy_id_by_name( wc_sanitize_taxonomy_name( $name ) );

        $wc_attribute = new WC_Product_Attribute();
        $wc_attribute->set_id( $attribute_id );
        $wc_attribute->set_name( $resolved['taxonomy'] );
        $wc_attribute->set_options( $resolved['term_ids'] );
        $wc_attribute->set_position( $position++ );
        $wc_attribute->set_visible( true );
        $wc_attribute->set_variation( ! isset( $attr['used_for_variation'] ) || $attr['used_for_variation'] );

        $attributes[] = $wc_attribute;
    }

    return $attributes;
}

function seo_mcp_tools_schema() {
    return [
        [
            'name'        => 'upload_media',
            'description' => 'Upload 1 anh (truyen truc tiep du lieu base64, khong can URL co san) vao Media Library, tra ve URL public de dung cho noi khac (vd Buffer).',
            'inputSchema' => [
                'type'       => 'object',
                'required'   => [ 'base64_data' ],
                'properties' => [
                    'filename'    => [ 'type' => 'string', 'description' => 'Ten file mong muon, vd slide1.png, tuy chon' ],
                    'base64_data' => [ 'type' => 'string', 'description' => 'Du lieu anh dang base64 (co the la data URI data:image/png;base64,... hoac chuoi base64 thuan)' ],
                    'mime_type'   => [ 'type' => 'string', 'description' => 'Mime type, vd image/png. Bo qua neu base64_data la data URI da co mime type' ],
                    'alt_text'    => [ 'type' => 'string', 'description' => 'Alt text cho anh, tuy chon' ],
                ],
            ],
        ],
        [
            'name'        => 'create_draft_post',
            'description' => 'Tao bai viet moi o trang thai draft cho site đích (đổi domain thật khi dùng), kem danh muc, tag va SEO Rank Math tuy chon.',
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
                    'status'            => [ 'type' => 'string', 'description' => 'draft (mac dinh), future (len lich) hoac publish (dang ngay). CHI duoc ap dung neu image_url tai anh dai dien thanh cong; neu tai anh that bai hoac khong truyen image_url, bai luon giu draft bat ke gia tri nay.' ],
                    'publish_date'      => [ 'type' => 'string', 'description' => 'Ngay gio dang bai, dinh dang "YYYY-MM-DD HH:MM:SS" theo gio dia phuong cua site. Bat buoc neu status la future. Neu status la publish va publish_date nam trong tuong lai, se tu chuyen thanh future voi ngay gio nay.' ],
                ],
            ],
        ],
        [
            'name'        => 'list_posts',
            'description' => 'Liet ke bai viet tren site đích (đổi domain thật khi dùng) o bat ky trang thai nao (draft, future/schedule, publish, pending, private), mac dinh liet ke tat ca neu khong loc status.',
            'inputSchema' => [
                'type'       => 'object',
                'properties' => [
                    'number' => [ 'type' => 'integer', 'description' => 'So luong bai can lay, mac dinh 10' ],
                    'status' => [ 'type' => 'array', 'items' => [ 'type' => 'string' ], 'description' => 'Loc theo status, vd ["draft"], ["future"], ["publish"]. Bo trong de lay tat ca (tru trash).' ],
                ],
            ],
        ],
        [
            'name'        => 'update_post',
            'description' => 'Sua mot bai viet o BAT KY trang thai nao (draft, future/schedule, hoac da publish): noi dung, danh muc, tag, SEO Rank Math, hoac gan/doi anh dai dien. Khong con gioi han chi sua duoc bai draft, can can nhac ky khi sua bai da publish vi anh huong truc tiep den noi dung dang live.',
            'inputSchema' => [
                'type'       => 'object',
                'required'   => [ 'post_id' ],
                'properties' => [
                    'post_id'           => [ 'type' => 'integer', 'description' => 'ID bai can sua' ],
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
                    'status'            => [ 'type' => 'string', 'description' => 'draft, future (len lich) hoac publish (dang ngay), tuy chon. Neu image_url cung duoc truyen trong cung lan goi va tai anh that bai, status se KHONG duoc ap dung, bai giu nguyen status hien tai.' ],
                    'publish_date'      => [ 'type' => 'string', 'description' => 'Ngay gio dang bai, dinh dang "YYYY-MM-DD HH:MM:SS" theo gio dia phuong cua site, tuy chon. Bat buoc neu status la future.' ],
                ],
            ],
        ],
        [
            'name'        => 'delete_post',
            'description' => 'Xoa mot bai viet o BAT KY trang thai nao (draft, future/schedule, hoac da publish). Mac dinh chi chuyen vao Thung rac (co the khoi phuc lai), truyen force=true de xoa vinh vien luon (KHONG the khoi phuc).',
            'inputSchema' => [
                'type'       => 'object',
                'required'   => [ 'post_id' ],
                'properties' => [
                    'post_id' => [ 'type' => 'integer', 'description' => 'ID bai can xoa' ],
                    'force'   => [ 'type' => 'boolean', 'description' => 'true = xoa vinh vien, khong qua Thung rac, khong the khoi phuc. Mac dinh false (chi chuyen vao Thung rac).' ],
                ],
            ],
        ],
        [
            'name'        => 'delete_media',
            'description' => 'Xoa hoan toan 1 anh/file khoi Media Library (bao gom ca file that tren o dia), khong qua Thung rac, khong the khoi phuc.',
            'inputSchema' => [
                'type'       => 'object',
                'required'   => [ 'attachment_id' ],
                'properties' => [
                    'attachment_id' => [ 'type' => 'integer', 'description' => 'ID cua attachment/anh trong Media Library can xoa' ],
                ],
            ],
        ],
        [
            'name'        => 'create_product',
            'description' => 'Tao san pham WooCommerce moi (simple hoac variable) LUON o trang thai draft, kem anh, danh muc/tag, va attribute (bat buoc neu variable). Dung update_product de chuyen sang publish sau khi kiem tra lai.',
            'inputSchema' => [
                'type'       => 'object',
                'required'   => [ 'name' ],
                'properties' => [
                    'name'              => [ 'type' => 'string', 'description' => 'Ten san pham' ],
                    'type'              => [ 'type' => 'string', 'description' => '"simple" (mac dinh) hoac "variable"' ],
                    'description'       => [ 'type' => 'string', 'description' => 'Mo ta day du dang HTML, tuy chon' ],
                    'short_description' => [ 'type' => 'string', 'description' => 'Mo ta ngan, tuy chon' ],
                    'slug'              => [ 'type' => 'string', 'description' => 'Duong dan URL, de trong se tu tao' ],
                    'sku'               => [ 'type' => 'string', 'description' => 'Ma SKU, tuy chon' ],
                    'regular_price'     => [ 'type' => 'string', 'description' => 'Gia goc, CHI ap dung neu type=simple' ],
                    'sale_price'        => [ 'type' => 'string', 'description' => 'Gia sale, CHI ap dung neu type=simple' ],
                    'manage_stock'      => [ 'type' => 'boolean', 'description' => 'Bat quan ly ton kho theo so luong, CHI ap dung neu type=simple' ],
                    'stock_quantity'    => [ 'type' => 'integer', 'description' => 'So luong ton kho, CHI ap dung neu type=simple va manage_stock=true' ],
                    'stock_status'      => [ 'type' => 'string', 'description' => '"instock", "outofstock", hoac "onbackorder", CHI ap dung neu type=simple' ],
                    'attributes'        => [
                        'type'        => 'array',
                        'description' => 'BAT BUOC neu type=variable. Global attribute dung de tao bien the, vd [{"name":"Mau sac","options":["Den","Trang"],"used_for_variation":true}]. Tu tao attribute/term moi neu chua ton tai.',
                        'items'       => [
                            'type'       => 'object',
                            'properties' => [
                                'name'               => [ 'type' => 'string' ],
                                'options'            => [ 'type' => 'array', 'items' => [ 'type' => 'string' ] ],
                                'used_for_variation' => [ 'type' => 'boolean', 'description' => 'Mac dinh true' ],
                            ],
                        ],
                    ],
                    'categories'        => [ 'type' => 'array', 'items' => [ 'type' => 'string' ], 'description' => 'Ten danh muc san pham' ],
                    'tags'              => [ 'type' => 'array', 'items' => [ 'type' => 'string' ], 'description' => 'Ten tag san pham' ],
                    'image_urls'        => [ 'type' => 'array', 'items' => [ 'type' => 'string' ], 'description' => 'Danh sach URL https anh, anh dau tien = anh dai dien, con lai vao gallery' ],
                    'image_uploads'     => [
                        'type'        => 'array',
                        'description' => 'Anh upload truc tiep base64 (khong can URL co san), noi tiep sau image_urls theo dung thu tu (anh dau tien tren toan bo danh sach = anh dai dien)',
                        'items'       => [
                            'type'       => 'object',
                            'properties' => [
                                'base64_data' => [ 'type' => 'string' ],
                                'mime_type'   => [ 'type' => 'string' ],
                                'filename'    => [ 'type' => 'string' ],
                                'alt'         => [ 'type' => 'string' ],
                            ],
                        ],
                    ],
                    'seo_title'         => [ 'type' => 'string', 'description' => 'Rank Math meta title, tuy chon' ],
                    'seo_description'   => [ 'type' => 'string', 'description' => 'Rank Math meta description, tuy chon. NEN LUON truyen field nay khi short_description co chua shortcode (vd nut [button]), vi neu de trong Rank Math se tu lay nguyen van short_description (bao gom ca shortcode chua render) lam meta description/Open Graph/Twitter card.' ],
                    'seo_focus_keyword' => [ 'type' => 'string', 'description' => 'Rank Math focus keyword, tuy chon' ],
                ],
            ],
        ],
        [
            'name'        => 'update_product',
            'description' => 'Sua san pham WooCommerce da co: thong tin co ban, gia/ton kho (simple), attribute (variable), danh muc/tag, anh, hoac doi status (vd sang publish sau khi tao draft).',
            'inputSchema' => [
                'type'       => 'object',
                'required'   => [ 'product_id' ],
                'properties' => [
                    'product_id'        => [ 'type' => 'integer', 'description' => 'ID san pham can sua' ],
                    'name'              => [ 'type' => 'string', 'description' => 'Ten moi, tuy chon' ],
                    'description'       => [ 'type' => 'string', 'description' => 'Mo ta HTML moi, tuy chon' ],
                    'short_description' => [ 'type' => 'string', 'description' => 'Mo ta ngan moi, tuy chon' ],
                    'slug'              => [ 'type' => 'string', 'description' => 'Slug moi, tuy chon' ],
                    'sku'               => [ 'type' => 'string', 'description' => 'SKU moi, tuy chon' ],
                    'regular_price'     => [ 'type' => 'string', 'description' => 'CHI ap dung neu san pham la type=simple' ],
                    'sale_price'        => [ 'type' => 'string', 'description' => 'CHI ap dung neu san pham la type=simple' ],
                    'manage_stock'      => [ 'type' => 'boolean', 'description' => 'CHI ap dung neu san pham la type=simple' ],
                    'stock_quantity'    => [ 'type' => 'integer', 'description' => 'CHI ap dung neu san pham la type=simple' ],
                    'stock_status'      => [ 'type' => 'string', 'description' => 'CHI ap dung neu san pham la type=simple' ],
                    'attributes'        => [ 'type' => 'array', 'description' => 'CHI ap dung neu san pham la type=variable, cung dinh dang nhu create_product (thay the toan bo danh sach attribute cu)' ],
                    'categories'        => [ 'type' => 'array', 'items' => [ 'type' => 'string' ], 'description' => 'Danh muc moi, tuy chon' ],
                    'tags'              => [ 'type' => 'array', 'items' => [ 'type' => 'string' ], 'description' => 'Tag moi, tuy chon' ],
                    'image_urls'        => [ 'type' => 'array', 'items' => [ 'type' => 'string' ], 'description' => 'Anh moi tu URL https, tuy chon' ],
                    'image_uploads'     => [ 'type' => 'array', 'description' => 'Anh moi upload truc tiep base64, cung dinh dang nhu create_product, tuy chon' ],
                    'image_urls_mode'   => [ 'type' => 'string', 'description' => '"replace" (mac dinh, thay het gallery cu bang anh moi) hoac "append" (giu anh cu, them anh moi vao gallery)' ],
                    'status'            => [ 'type' => 'string', 'description' => '"draft", "pending", hoac "publish"' ],
                    'seo_title'         => [ 'type' => 'string', 'description' => 'Rank Math meta title moi, tuy chon' ],
                    'seo_description'   => [ 'type' => 'string', 'description' => 'Rank Math meta description moi, tuy chon. NEN LUON truyen field nay khi short_description co chua shortcode (vd nut [button]), vi neu de trong Rank Math se tu lay nguyen van short_description (bao gom ca shortcode chua render) lam meta description/Open Graph/Twitter card.' ],
                    'seo_focus_keyword' => [ 'type' => 'string', 'description' => 'Rank Math focus keyword moi, tuy chon' ],
                ],
            ],
        ],
        [
            'name'        => 'delete_product',
            'description' => 'Xoa 1 san pham (ca simple lan variable, xoa san pham cha se xoa luon tat ca bien the con). Mac dinh chi chuyen vao Thung rac, truyen force=true de xoa vinh vien (KHONG the khoi phuc).',
            'inputSchema' => [
                'type'       => 'object',
                'required'   => [ 'product_id' ],
                'properties' => [
                    'product_id' => [ 'type' => 'integer' ],
                    'force'      => [ 'type' => 'boolean' ],
                ],
            ],
        ],
        [
            'name'        => 'get_product',
            'description' => 'Xem chi tiet day du 1 san pham: gia, ton kho, anh, danh muc/tag, attribute va so bien the (neu la variable). Nen goi truoc khi update_product de biet ro trang thai hien tai.',
            'inputSchema' => [
                'type'       => 'object',
                'required'   => [ 'product_id' ],
                'properties' => [
                    'product_id' => [ 'type' => 'integer' ],
                ],
            ],
        ],
        [
            'name'        => 'list_products',
            'description' => 'Liet ke/tim san pham WooCommerce theo tu khoa, slug, danh muc, type, hoac status, dung de lay product_id truoc khi update.',
            'inputSchema' => [
                'type'       => 'object',
                'properties' => [
                    'search'   => [ 'type' => 'string', 'description' => 'Tim theo ten san pham' ],
                    'slug'     => [ 'type' => 'string', 'description' => 'Tim chinh xac theo slug/duong dan URL (vd tu link san pham tren site)' ],
                    'status'   => [ 'type' => 'array', 'items' => [ 'type' => 'string' ], 'description' => 'Loc status, bo trong de lay tat ca (tru trash)' ],
                    'type'     => [ 'type' => 'string', 'description' => '"simple" hoac "variable", tuy chon' ],
                    'category' => [ 'type' => 'string', 'description' => 'Slug danh muc san pham, tuy chon' ],
                    'number'   => [ 'type' => 'integer', 'description' => 'So luong ket qua, mac dinh 10' ],
                ],
            ],
        ],
        [
            'name'        => 'create_product_variation',
            'description' => 'Tao 1 bien the moi cho san pham type=variable da co, voi gia tri attribute cu the (vd mau/size), gia va ton kho rieng.',
            'inputSchema' => [
                'type'       => 'object',
                'required'   => [ 'product_id', 'attributes' ],
                'properties' => [
                    'product_id'      => [ 'type' => 'integer', 'description' => 'ID san pham cha (phai la type=variable)' ],
                    'attributes'      => [ 'type' => 'object', 'description' => 'Gia tri cu the cho tung attribute da khai bao o san pham cha, vd {"Mau sac": "Den"}. Gia tri phai la 1 option da ton tai tren san pham cha.' ],
                    'regular_price'   => [ 'type' => 'string' ],
                    'sale_price'      => [ 'type' => 'string' ],
                    'sku'             => [ 'type' => 'string' ],
                    'manage_stock'    => [ 'type' => 'boolean' ],
                    'stock_quantity'  => [ 'type' => 'integer' ],
                    'stock_status'    => [ 'type' => 'string' ],
                    'image_url'       => [ 'type' => 'string', 'description' => 'Anh rieng cho bien the nay tu URL https, tuy chon (khong truyen se dung anh san pham cha)' ],
                    'image_base64'    => [ 'type' => 'string', 'description' => 'Hoac upload anh truc tiep base64 thay vi image_url, tuy chon' ],
                    'image_mime_type' => [ 'type' => 'string' ],
                    'image_filename'  => [ 'type' => 'string' ],
                ],
            ],
        ],
        [
            'name'        => 'list_product_variations',
            'description' => 'Liet ke toan bo bien the cua 1 san pham type=variable, tra ve variation_id, gia tri attribute, gia, ton kho. Goi truoc khi update_product_variation/delete_product_variation de biet dung ID.',
            'inputSchema' => [
                'type'       => 'object',
                'required'   => [ 'product_id' ],
                'properties' => [
                    'product_id' => [ 'type' => 'integer' ],
                ],
            ],
        ],
        [
            'name'        => 'update_product_variation',
            'description' => 'Sua 1 bien the da co: gia, ton kho, SKU, anh rieng, hoac status.',
            'inputSchema' => [
                'type'       => 'object',
                'required'   => [ 'variation_id' ],
                'properties' => [
                    'variation_id'    => [ 'type' => 'integer' ],
                    'regular_price'   => [ 'type' => 'string' ],
                    'sale_price'      => [ 'type' => 'string' ],
                    'sku'             => [ 'type' => 'string' ],
                    'manage_stock'    => [ 'type' => 'boolean' ],
                    'stock_quantity'  => [ 'type' => 'integer' ],
                    'stock_status'    => [ 'type' => 'string' ],
                    'image_url'       => [ 'type' => 'string', 'description' => 'Anh moi tu URL https, tuy chon' ],
                    'image_base64'    => [ 'type' => 'string', 'description' => 'Hoac upload anh truc tiep base64, tuy chon' ],
                    'image_mime_type' => [ 'type' => 'string' ],
                    'image_filename'  => [ 'type' => 'string' ],
                    'status'          => [ 'type' => 'string', 'description' => '"publish" hoac "private"' ],
                ],
            ],
        ],
        [
            'name'        => 'delete_product_variation',
            'description' => 'Xoa 1 bien the cu the khoi san pham cha, khong anh huong cac bien the khac. Mac dinh chi chuyen vao Thung rac, truyen force=true de xoa vinh vien (KHONG the khoi phuc).',
            'inputSchema' => [
                'type'       => 'object',
                'required'   => [ 'variation_id' ],
                'properties' => [
                    'variation_id' => [ 'type' => 'integer' ],
                    'force'        => [ 'type' => 'boolean' ],
                ],
            ],
        ],
        [
            'name'        => 'list_affiliate_redirects',
            'description' => 'Liet ke toan bo redirect /go/<slug> hien co va link affiliate tuong ung.',
            'inputSchema' => [
                'type'       => 'object',
                'properties' => [],
            ],
        ],
        [
            'name'        => 'set_affiliate_redirect',
            'description' => 'Tao hoac cap nhat 1 redirect 301 dang <domain>/go/<slug> tro toi link affiliate that (affiliate...), dung de cloak link giu link equity va de quan ly hang loat khi link doi. Slug se tu dong bi Disallow trong robots.txt (khong crawl vao duoc). Dung link /go/<slug> nay lam gia tri "link" trong shortcode [button] cua san pham, khong dung link affiliate goc truc tiep nua.',
            'inputSchema' => [
                'type'       => 'object',
                'required'   => [ 'slug', 'url' ],
                'properties' => [
                    'slug' => [ 'type' => 'string', 'description' => 'Phan sau /go/, chi chu thuong/so/gach ngang, vd "tay-cam-ps4"' ],
                    'url'  => [ 'type' => 'string', 'description' => 'Link affiliate that se redirect toi, vd link affiliate that tu mang affiliate ban dung' ],
                ],
            ],
        ],
        [
            'name'        => 'delete_affiliate_redirect',
            'description' => 'Xoa 1 redirect /go/<slug> da tao truoc do.',
            'inputSchema' => [
                'type'       => 'object',
                'required'   => [ 'slug' ],
                'properties' => [
                    'slug' => [ 'type' => 'string' ],
                ],
            ],
        ],
        [
            'name'        => 'set_product_faq',
            'description' => 'Luu danh sach cau hoi/dap cho 1 san pham, tu dong in ra structured data FAQPage (JSON-LD) khi xem trang san pham do, DOC LAP hoan toan voi schema Product cua Rank Math (khong sua/de len schema co san). Dung khi Rank Math ban free khong ho tro mau FAQ (can Pro). Cau hoi/dap nen khop dung noi dung FAQ da hien thi that trong mo ta san pham, khong bia them thong tin ngoai noi dung da viet.',
            'inputSchema' => [
                'type'       => 'object',
                'required'   => [ 'product_id', 'faqs' ],
                'properties' => [
                    'product_id' => [ 'type' => 'integer' ],
                    'faqs'       => [
                        'type'        => 'array',
                        'description' => 'Danh sach cau hoi/dap, vd [{"question":"...","answer":"..."}]. Chi dung text thuan, khong can HTML.',
                        'items'       => [
                            'type'       => 'object',
                            'properties' => [
                                'question' => [ 'type' => 'string' ],
                                'answer'   => [ 'type' => 'string' ],
                            ],
                        ],
                    ],
                ],
            ],
        ],
        [
            'name'        => 'delete_product_faq',
            'description' => 'Xoa FAQ schema da luu cho 1 san pham.',
            'inputSchema' => [
                'type'       => 'object',
                'required'   => [ 'product_id' ],
                'properties' => [
                    'product_id' => [ 'type' => 'integer' ],
                ],
            ],
        ],
    ];
}

function seo_mcp_call_tool( $name, $args ) {
    if ( $name === 'upload_media' ) {
        $result = seo_mcp_upload_media_from_base64(
            $args['filename'] ?? '',
            $args['base64_data'] ?? '',
            $args['mime_type'] ?? '',
            $args['alt_text'] ?? ''
        );

        if ( is_wp_error( $result ) ) {
            return [ 'isError' => true, 'content' => [ [ 'type' => 'text', 'text' => 'Loi: ' . $result->get_error_message() ] ] ];
        }

        return [
            'isError' => false,
            'content' => [ [ 'type' => 'text', 'text' => "Da upload anh. Attachment ID: {$result['attachment_id']}. URL: {$result['url']}" ] ],
        ];
    }

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

        $image_note   = '';
        $image_ok     = false;
        if ( ! empty( $args['image_url'] ) ) {
            $attachment_id = seo_mcp_sideload_image( $args['image_url'], $args['image_alt'] ?? '', $post_id );
            if ( is_wp_error( $attachment_id ) ) {
                $image_note = ' Luu y: tai anh dai dien that bai (' . $attachment_id->get_error_message() . '), can tu them anh thu cong.';
            } else {
                set_post_thumbnail( $post_id, $attachment_id );
                $image_note = ' Da tai va gan anh dai dien tu image_url.';
                $image_ok   = true;
            }
        }

        $status_note = '';
        if ( $image_ok && ! empty( $args['status'] ) && in_array( $args['status'], [ 'future', 'publish' ], true ) ) {
            $status_result = seo_mcp_apply_publish_status( $post_id, $args['status'], $args['publish_date'] ?? '' );
            if ( is_wp_error( $status_result ) ) {
                $status_note = ' Luu y: khong the ap dung status/ngay dang yeu cau (' . $status_result->get_error_message() . '), bai van giu draft.';
            } else {
                $status_note = " Da chuyen bai sang status: {$status_result}.";
            }
        } elseif ( ! $image_ok && ! empty( $args['status'] ) && $args['status'] !== 'draft' ) {
            $status_note = ' Luu y: khong ap dung status yeu cau vi anh dai dien chua co, bai giu draft.';
        }

        $edit_url = admin_url( 'post.php?post=' . $post_id . '&action=edit' );
        return [
            'isError' => false,
            'content' => [ [ 'type' => 'text', 'text' => "Da tao bai draft ID {$post_id}.{$image_note}{$status_note} Mo tai: {$edit_url}" ] ],
        ];
    }

    if ( $name === 'update_post' ) {
        $post_id = isset( $args['post_id'] ) ? (int) $args['post_id'] : 0;
        if ( ! $post_id ) {
            return [ 'isError' => true, 'content' => [ [ 'type' => 'text', 'text' => 'Thieu post_id.' ] ] ];
        }

        $existing = get_post( $post_id );
        if ( ! $existing ) {
            return [ 'isError' => true, 'content' => [ [ 'type' => 'text', 'text' => "Khong tim thay bai ID {$post_id}." ] ] ];
        }

        // Luon giu nguyen status/ngay dang hien tai cua bai, khong de wp_update_post()
        // tu suy dien lai (da xac nhan qua thuc te: chi update content ma khong truyen
        // post_status/post_date ro rang co the khien bai bi rot ve draft ngoai y muon).
        $update = [
            'ID'          => $post_id,
            'post_status' => $existing->post_status,
        ];
        if ( 'future' === $existing->post_status ) {
            $update['post_date']     = $existing->post_date;
            $update['post_date_gmt'] = $existing->post_date_gmt;
            $update['edit_date']     = true;
        }
        if ( isset( $args['title'] ) )   $update['post_title']   = $args['title'];
        if ( isset( $args['content'] ) ) $update['post_content'] = $args['content'];
        if ( isset( $args['excerpt'] ) ) $update['post_excerpt'] = $args['excerpt'];
        if ( isset( $args['slug'] ) )    $update['post_name']    = $args['slug'];

        // Luon goi wp_update_post() de status/ngay dang duoc "khang dinh lai" moi lan,
        // an toan vi $update da chua san status/date hien tai (xem comment o tren),
        // khong chi goi khi co thay doi noi dung, tranh tinh trang rot status ngoai y muon
        // ke ca khi chi sua categories/tags/seo o duoi.
        $result = wp_update_post( $update, true );
        if ( is_wp_error( $result ) ) {
            return [ 'isError' => true, 'content' => [ [ 'type' => 'text', 'text' => 'Loi: ' . $result->get_error_message() ] ] ];
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
        $image_failed_now = false;
        if ( ! empty( $args['image_url'] ) ) {
            $attachment_id = seo_mcp_sideload_image( $args['image_url'], $args['image_alt'] ?? '', $post_id );
            if ( is_wp_error( $attachment_id ) ) {
                $image_note = ' Luu y: tai anh dai dien that bai (' . $attachment_id->get_error_message() . ').';
                $image_failed_now = true;
            } else {
                set_post_thumbnail( $post_id, $attachment_id );
                $image_note = ' Da cap nhat anh dai dien.';
            }
        }

        $status_note = '';
        if ( ! empty( $args['status'] ) && ! $image_failed_now ) {
            $status_result = seo_mcp_apply_publish_status( $post_id, $args['status'], $args['publish_date'] ?? '' );
            if ( is_wp_error( $status_result ) ) {
                $status_note = ' Luu y: khong the ap dung status/ngay dang yeu cau (' . $status_result->get_error_message() . ').';
            } else {
                $status_note = " Da chuyen bai sang status: {$status_result}.";
            }
        } elseif ( ! empty( $args['status'] ) && $image_failed_now ) {
            $status_note = ' Luu y: khong ap dung status yeu cau vi anh dai dien vua tai that bai.';
        }

        $updated_post = get_post( $post_id );
        $edit_url = admin_url( 'post.php?post=' . $post_id . '&action=edit' );
        return [
            'isError' => false,
            'content' => [ [ 'type' => 'text', 'text' => "Da cap nhat bai ID {$post_id} (status: {$updated_post->post_status}).{$image_note}{$status_note} Mo tai: {$edit_url}" ] ],
        ];
    }

    if ( $name === 'list_posts' ) {
        $status = ! empty( $args['status'] ) && is_array( $args['status'] )
            ? array_values( $args['status'] )
            : [ 'draft', 'future', 'publish', 'pending', 'private' ];

        $posts = get_posts( [
            'post_status' => $status,
            'numberposts' => $args['number'] ?? 10,
            'orderby'     => 'date',
            'order'       => 'DESC',
        ] );

        if ( empty( $posts ) ) {
            return [ 'isError' => false, 'content' => [ [ 'type' => 'text', 'text' => 'Khong tim thay bai nao khop dieu kien.' ] ] ];
        }

        $lines = array_map( function ( $p ) {
            $edit_url = admin_url( 'post.php?post=' . $p->ID . '&action=edit' );
            return "#{$p->ID} - {$p->post_title} (status: {$p->post_status}, {$p->post_date}) - {$edit_url}";
        }, $posts );

        return [ 'isError' => false, 'content' => [ [ 'type' => 'text', 'text' => implode( "\n", $lines ) ] ] ];
    }

    if ( $name === 'delete_post' ) {
        $post_id = isset( $args['post_id'] ) ? (int) $args['post_id'] : 0;
        if ( ! $post_id ) {
            return [ 'isError' => true, 'content' => [ [ 'type' => 'text', 'text' => 'Thieu post_id.' ] ] ];
        }

        $existing = get_post( $post_id );
        if ( ! $existing ) {
            return [ 'isError' => true, 'content' => [ [ 'type' => 'text', 'text' => "Khong tim thay bai ID {$post_id}." ] ] ];
        }

        $force  = ! empty( $args['force'] );
        $result = wp_delete_post( $post_id, $force );

        if ( ! $result ) {
            return [ 'isError' => true, 'content' => [ [ 'type' => 'text', 'text' => "Xoa bai ID {$post_id} that bai." ] ] ];
        }

        $mode = $force ? 'xoa vinh vien' : 'chuyen vao Thung rac';
        return [
            'isError' => false,
            'content' => [ [ 'type' => 'text', 'text' => "Da {$mode} bai ID {$post_id} (\"{$existing->post_title}\")." ] ],
        ];
    }

    if ( $name === 'delete_media' ) {
        $attachment_id = isset( $args['attachment_id'] ) ? (int) $args['attachment_id'] : 0;
        if ( ! $attachment_id ) {
            return [ 'isError' => true, 'content' => [ [ 'type' => 'text', 'text' => 'Thieu attachment_id.' ] ] ];
        }

        $existing = get_post( $attachment_id );
        if ( ! $existing || $existing->post_type !== 'attachment' ) {
            return [ 'isError' => true, 'content' => [ [ 'type' => 'text', 'text' => "Khong tim thay attachment ID {$attachment_id}." ] ] ];
        }

        require_once ABSPATH . 'wp-admin/includes/image.php';
        $result = wp_delete_attachment( $attachment_id, true );

        if ( ! $result ) {
            return [ 'isError' => true, 'content' => [ [ 'type' => 'text', 'text' => "Xoa attachment ID {$attachment_id} that bai." ] ] ];
        }

        return [
            'isError' => false,
            'content' => [ [ 'type' => 'text', 'text' => "Da xoa hoan toan attachment ID {$attachment_id} khoi Media Library." ] ],
        ];
    }

if ( $name === 'create_product' ) {
        if ( ! seo_mcp_wc_ready() ) {
            return [ 'isError' => true, 'content' => [ [ 'type' => 'text', 'text' => 'WooCommerce chua san sang tren site nay.' ] ] ];
        }

        $type    = in_array( $args['type'] ?? 'simple', [ 'simple', 'variable' ], true ) ? $args['type'] : 'simple';
        $product = ( 'variable' === $type ) ? new WC_Product_Variable() : new WC_Product_Simple();

        $product->set_name( $args['name'] ?? '' );
        $product->set_status( 'draft' ); // luon tao draft, dung update_product de publish sau
        if ( isset( $args['description'] ) )       $product->set_description( $args['description'] );
        if ( isset( $args['short_description'] ) ) $product->set_short_description( $args['short_description'] );
        if ( ! empty( $args['slug'] ) )             $product->set_slug( $args['slug'] );
        if ( ! empty( $args['sku'] ) )               $product->set_sku( $args['sku'] );

        if ( 'simple' === $type ) {
            if ( isset( $args['regular_price'] ) )  $product->set_regular_price( $args['regular_price'] );
            if ( isset( $args['sale_price'] ) )     $product->set_sale_price( $args['sale_price'] );
            if ( isset( $args['manage_stock'] ) )   $product->set_manage_stock( (bool) $args['manage_stock'] );
            if ( isset( $args['stock_quantity'] ) ) $product->set_stock_quantity( $args['stock_quantity'] );
            if ( isset( $args['stock_status'] ) )   $product->set_stock_status( $args['stock_status'] );
        } else {
            $attributes = seo_mcp_build_variable_attributes( $args['attributes'] ?? [] );
            if ( is_wp_error( $attributes ) ) {
                return [ 'isError' => true, 'content' => [ [ 'type' => 'text', 'text' => 'Loi attribute: ' . $attributes->get_error_message() ] ] ];
            }
            $product->set_attributes( $attributes );
        }

        $product_id = $product->save();
        if ( ! $product_id ) {
            return [ 'isError' => true, 'content' => [ [ 'type' => 'text', 'text' => 'Tao san pham that bai.' ] ] ];
        }

        if ( ! empty( $args['categories'] ) ) {
            wp_set_post_terms( $product_id, $args['categories'], 'product_cat' );
        }
        if ( ! empty( $args['tags'] ) ) {
            wp_set_post_terms( $product_id, $args['tags'], 'product_tag' );
        }

        $image_note = '';
        $image_result = seo_mcp_apply_product_images( $product, $product_id, $args['image_urls'] ?? [], $args['image_uploads'] ?? [] );
        if ( $image_result['attempted'] > 0 ) {
            $product->save();
            $image_note = " Da xu ly {$image_result['attempted']} anh (thanh cong: " . count( $image_result['ids'] ) . ", loi: {$image_result['failed']}).";
        }

        if ( ! empty( $args['seo_title'] ) ) {
            update_post_meta( $product_id, 'rank_math_title', $args['seo_title'] );
        }
        if ( ! empty( $args['seo_description'] ) ) {
            update_post_meta( $product_id, 'rank_math_description', $args['seo_description'] );
        }
        if ( ! empty( $args['seo_focus_keyword'] ) ) {
            update_post_meta( $product_id, 'rank_math_focus_keyword', $args['seo_focus_keyword'] );
        }

        $edit_url = admin_url( 'post.php?post=' . $product_id . '&action=edit' );
        return [
            'isError' => false,
            'content' => [ [ 'type' => 'text', 'text' => "Da tao san pham draft ID {$product_id} (type: {$type}).{$image_note} Mo tai: {$edit_url}" ] ],
        ];
    }

if ( $name === 'update_product' ) {
        if ( ! seo_mcp_wc_ready() ) {
            return [ 'isError' => true, 'content' => [ [ 'type' => 'text', 'text' => 'WooCommerce chua san sang tren site nay.' ] ] ];
        }

        $product_id = isset( $args['product_id'] ) ? (int) $args['product_id'] : 0;
        if ( ! $product_id ) {
            return [ 'isError' => true, 'content' => [ [ 'type' => 'text', 'text' => 'Thieu product_id.' ] ] ];
        }
        $product = wc_get_product( $product_id );
        if ( ! $product ) {
            return [ 'isError' => true, 'content' => [ [ 'type' => 'text', 'text' => "Khong tim thay san pham ID {$product_id}." ] ] ];
        }

        if ( isset( $args['name'] ) )              $product->set_name( $args['name'] );
        if ( isset( $args['description'] ) )       $product->set_description( $args['description'] );
        if ( isset( $args['short_description'] ) ) $product->set_short_description( $args['short_description'] );
        if ( isset( $args['slug'] ) )                $product->set_slug( $args['slug'] );
        if ( isset( $args['sku'] ) )                 $product->set_sku( $args['sku'] );

        if ( $product->is_type( 'simple' ) ) {
            if ( isset( $args['regular_price'] ) )  $product->set_regular_price( $args['regular_price'] );
            if ( isset( $args['sale_price'] ) )     $product->set_sale_price( $args['sale_price'] );
            if ( isset( $args['manage_stock'] ) )   $product->set_manage_stock( (bool) $args['manage_stock'] );
            if ( isset( $args['stock_quantity'] ) ) $product->set_stock_quantity( $args['stock_quantity'] );
            if ( isset( $args['stock_status'] ) )   $product->set_stock_status( $args['stock_status'] );
        }

        if ( isset( $args['attributes'] ) && $product->is_type( 'variable' ) ) {
            $attributes = seo_mcp_build_variable_attributes( $args['attributes'] );
            if ( is_wp_error( $attributes ) ) {
                return [ 'isError' => true, 'content' => [ [ 'type' => 'text', 'text' => 'Loi attribute: ' . $attributes->get_error_message() ] ] ];
            }
            $product->set_attributes( $attributes );
        }

        if ( isset( $args['categories'] ) ) {
            wp_set_post_terms( $product_id, $args['categories'], 'product_cat' );
        }
        if ( isset( $args['tags'] ) ) {
            wp_set_post_terms( $product_id, $args['tags'], 'product_tag' );
        }

        $image_note = '';
        $gallery_mode = in_array( $args['image_urls_mode'] ?? 'replace', [ 'replace', 'append' ], true ) ? ( $args['image_urls_mode'] ?? 'replace' ) : 'replace';
        $image_result = seo_mcp_apply_product_images( $product, $product_id, $args['image_urls'] ?? [], $args['image_uploads'] ?? [], $gallery_mode );
        if ( $image_result['attempted'] > 0 ) {
            $image_note = " Da xu ly {$image_result['attempted']} anh (thanh cong: " . count( $image_result['ids'] ) . ", loi: {$image_result['failed']}).";
        }

        $status_note = '';
        if ( isset( $args['status'] ) && in_array( $args['status'], [ 'draft', 'pending', 'publish' ], true ) ) {
            $product->set_status( $args['status'] );
            $status_note = " Da chuyen status: {$args['status']}.";
        }

        $product->save();

        if ( isset( $args['seo_title'] ) ) {
            update_post_meta( $product_id, 'rank_math_title', $args['seo_title'] );
        }
        if ( isset( $args['seo_description'] ) ) {
            update_post_meta( $product_id, 'rank_math_description', $args['seo_description'] );
        }
        if ( isset( $args['seo_focus_keyword'] ) ) {
            update_post_meta( $product_id, 'rank_math_focus_keyword', $args['seo_focus_keyword'] );
        }

        $edit_url = admin_url( 'post.php?post=' . $product_id . '&action=edit' );
        return [
            'isError' => false,
            'content' => [ [ 'type' => 'text', 'text' => "Da cap nhat san pham ID {$product_id}.{$image_note}{$status_note} Mo tai: {$edit_url}" ] ],
        ];
    }

if ( $name === 'delete_product' || $name === 'delete_product_variation' ) {
        $is_variation = ( $name === 'delete_product_variation' );
        $id_key       = $is_variation ? 'variation_id' : 'product_id';
        $id           = isset( $args[ $id_key ] ) ? (int) $args[ $id_key ] : 0;
        if ( ! $id ) {
            return [ 'isError' => true, 'content' => [ [ 'type' => 'text', 'text' => "Thieu {$id_key}." ] ] ];
        }

        $existing = get_post( $id );
        if ( ! $existing ) {
            return [ 'isError' => true, 'content' => [ [ 'type' => 'text', 'text' => "Khong tim thay ID {$id}." ] ] ];
        }

        $parent_id_for_sync = $is_variation ? (int) $existing->post_parent : 0;

        $force  = ! empty( $args['force'] );
        $result = wp_delete_post( $id, $force );
        if ( ! $result ) {
            return [ 'isError' => true, 'content' => [ [ 'type' => 'text', 'text' => "Xoa ID {$id} that bai." ] ] ];
        }

        if ( $is_variation && $parent_id_for_sync && function_exists( 'wc_get_product' ) ) {
            WC_Product_Variable::sync( $parent_id_for_sync );
        }

        $mode  = $force ? 'xoa vinh vien' : 'chuyen vao Thung rac';
        $label = $is_variation ? 'bien the' : 'san pham';
        return [
            'isError' => false,
            'content' => [ [ 'type' => 'text', 'text' => "Da {$mode} {$label} ID {$id} (\"{$existing->post_title}\")." ] ],
        ];
    }

if ( $name === 'get_product' ) {
        if ( ! seo_mcp_wc_ready() ) {
            return [ 'isError' => true, 'content' => [ [ 'type' => 'text', 'text' => 'WooCommerce chua san sang tren site nay.' ] ] ];
        }

        $product_id = isset( $args['product_id'] ) ? (int) $args['product_id'] : 0;
        $product    = $product_id ? wc_get_product( $product_id ) : null;
        if ( ! $product ) {
            return [ 'isError' => true, 'content' => [ [ 'type' => 'text', 'text' => "Khong tim thay san pham ID {$product_id}." ] ] ];
        }

        $lines   = [];
        $lines[] = "ID: {$product->get_id()}";
        $lines[] = "Ten: {$product->get_name()}";
        $lines[] = "Type: {$product->get_type()}";
        $lines[] = "Status: {$product->get_status()}";
        $lines[] = "Slug: {$product->get_slug()}";
        $lines[] = "SKU: {$product->get_sku()}";
        if ( $product->is_type( 'simple' ) ) {
            $lines[] = "Gia goc: {$product->get_regular_price()}";
            $lines[] = "Gia sale: {$product->get_sale_price()}";
            $lines[] = "Ton kho: {$product->get_stock_quantity()} ({$product->get_stock_status()})";
        }
        $lines[]      = 'Mo ta ngan: ' . wp_strip_all_tags( $product->get_short_description() );
        $cat_names    = wp_list_pluck( wc_get_product_terms( $product->get_id(), 'product_cat' ), 'name' );
        $tag_names    = wp_list_pluck( wc_get_product_terms( $product->get_id(), 'product_tag' ), 'name' );
        $lines[]      = 'Danh muc: ' . ( $cat_names ? implode( ', ', $cat_names ) : '(khong co)' );
        $lines[]      = 'Tag: ' . ( $tag_names ? implode( ', ', $tag_names ) : '(khong co)' );
        $lines[]      = 'Anh dai dien: ' . ( $product->get_image_id() ? wp_get_attachment_url( $product->get_image_id() ) : '(khong co)' );
        $gallery      = $product->get_gallery_image_ids();
        $lines[]      = 'Gallery: ' . ( $gallery ? implode( ', ', array_map( 'wp_get_attachment_url', $gallery ) ) : '(khong co)' );

        if ( $product->is_type( 'variable' ) ) {
            $attr_lines = [];
            foreach ( $product->get_attributes() as $attribute ) {
                $term_names   = wc_get_product_terms( $product->get_id(), $attribute->get_name(), [ 'fields' => 'names' ] );
                $attr_lines[] = str_replace( 'pa_', '', $attribute->get_name() ) . ': ' . implode( ', ', $term_names );
            }
            $lines[] = 'Attributes: ' . ( $attr_lines ? implode( ' | ', $attr_lines ) : '(khong co)' );
            $lines[] = 'So bien the: ' . count( $product->get_children() );
        }

        $lines[] = 'Sua tai: ' . admin_url( 'post.php?post=' . $product->get_id() . '&action=edit' );

        return [ 'isError' => false, 'content' => [ [ 'type' => 'text', 'text' => implode( "\n", $lines ) ] ] ];
    }

if ( $name === 'list_products' ) {
        if ( ! seo_mcp_wc_ready() ) {
            return [ 'isError' => true, 'content' => [ [ 'type' => 'text', 'text' => 'WooCommerce chua san sang tren site nay.' ] ] ];
        }

        if ( ! empty( $args['slug'] ) ) {
            $page = get_page_by_path( $args['slug'], OBJECT, 'product' );
            if ( ! $page ) {
                return [ 'isError' => false, 'content' => [ [ 'type' => 'text', 'text' => "Khong tim thay san pham voi slug '{$args['slug']}'." ] ] ];
            }
            $product  = wc_get_product( $page->ID );
            $edit_url = admin_url( 'post.php?post=' . $product->get_id() . '&action=edit' );
            $price    = $product->is_type( 'variable' ) ? 'xem theo bien the' : $product->get_price();
            $line     = "#{$product->get_id()} - {$product->get_name()} (type: {$product->get_type()}, status: {$product->get_status()}, gia: {$price}) - {$edit_url}";
            return [ 'isError' => false, 'content' => [ [ 'type' => 'text', 'text' => $line ] ] ];
        }

        $query_args = [
            'status'  => ! empty( $args['status'] ) && is_array( $args['status'] ) ? $args['status'] : [ 'draft', 'pending', 'private', 'publish' ],
            'limit'   => $args['number'] ?? 10,
            'orderby' => 'date',
            'order'   => 'DESC',
        ];
        if ( ! empty( $args['search'] ) )   $query_args['s'] = $args['search'];
        if ( ! empty( $args['type'] ) )     $query_args['type'] = $args['type'];
        if ( ! empty( $args['category'] ) ) $query_args['category'] = [ $args['category'] ];

        $products = wc_get_products( $query_args );
        if ( empty( $products ) ) {
            return [ 'isError' => false, 'content' => [ [ 'type' => 'text', 'text' => 'Khong tim thay san pham nao khop dieu kien.' ] ] ];
        }

        $lines = array_map( function ( $p ) {
            $edit_url = admin_url( 'post.php?post=' . $p->get_id() . '&action=edit' );
            $price    = $p->is_type( 'variable' ) ? 'xem theo bien the' : $p->get_price();
            return "#{$p->get_id()} - {$p->get_name()} (type: {$p->get_type()}, status: {$p->get_status()}, gia: {$price}, ton kho: {$p->get_stock_status()}) - {$edit_url}";
        }, $products );

        return [ 'isError' => false, 'content' => [ [ 'type' => 'text', 'text' => implode( "\n", $lines ) ] ] ];
    }

if ( $name === 'create_product_variation' ) {
        if ( ! seo_mcp_wc_ready() ) {
            return [ 'isError' => true, 'content' => [ [ 'type' => 'text', 'text' => 'WooCommerce chua san sang tren site nay.' ] ] ];
        }

        $parent_id = isset( $args['product_id'] ) ? (int) $args['product_id'] : 0;
        $parent    = $parent_id ? wc_get_product( $parent_id ) : null;
        if ( ! $parent || ! $parent->is_type( 'variable' ) ) {
            return [ 'isError' => true, 'content' => [ [ 'type' => 'text', 'text' => "product_id {$parent_id} khong phai san pham type=variable hop le." ] ] ];
        }
        if ( empty( $args['attributes'] ) || ! is_array( $args['attributes'] ) ) {
            return [ 'isError' => true, 'content' => [ [ 'type' => 'text', 'text' => 'Thieu attributes cho bien the, vd {"Mau sac": "Den"}.' ] ] ];
        }

        // Chuyen ten attribute + gia tri sang dang WooCommerce can: taxonomy => term slug
        $variation_attributes = [];
        foreach ( $args['attributes'] as $attr_name => $value ) {
            $taxonomy = 'pa_' . wc_sanitize_taxonomy_name( $attr_name );
            if ( ! taxonomy_exists( $taxonomy ) ) {
                return [ 'isError' => true, 'content' => [ [ 'type' => 'text', 'text' => "Attribute '{$attr_name}' chua ton tai tren san pham cha, tao/update product truoc voi attribute nay." ] ] ];
            }
            $term = get_term_by( 'name', $value, $taxonomy );
            if ( ! $term ) {
                return [ 'isError' => true, 'content' => [ [ 'type' => 'text', 'text' => "Gia tri '{$value}' chua ton tai trong attribute '{$attr_name}'." ] ] ];
            }
            $variation_attributes[ $taxonomy ] = $term->slug;
        }

        $variation = new WC_Product_Variation();
        $variation->set_parent_id( $parent_id );
        $variation->set_attributes( $variation_attributes );
        if ( isset( $args['regular_price'] ) )   $variation->set_regular_price( $args['regular_price'] );
        if ( isset( $args['sale_price'] ) )      $variation->set_sale_price( $args['sale_price'] );
        if ( isset( $args['sku'] ) )              $variation->set_sku( $args['sku'] );
        if ( isset( $args['manage_stock'] ) )    $variation->set_manage_stock( (bool) $args['manage_stock'] );
        if ( isset( $args['stock_quantity'] ) )  $variation->set_stock_quantity( $args['stock_quantity'] );
        if ( isset( $args['stock_status'] ) )    $variation->set_stock_status( $args['stock_status'] );
        $variation->set_status( 'publish' ); // bien the an/hien phu thuoc status cua san pham cha, khong co khai niem draft rieng

        $variation_id = $variation->save();
        if ( ! $variation_id ) {
            return [ 'isError' => true, 'content' => [ [ 'type' => 'text', 'text' => 'Tao bien the that bai.' ] ] ];
        }

        $image_note = '';
        if ( ! empty( $args['image_url'] ) || ! empty( $args['image_base64'] ) ) {
            $item = ! empty( $args['image_url'] )
                ? [ 'url' => $args['image_url'] ]
                : [ 'base64_data' => $args['image_base64'], 'mime_type' => $args['image_mime_type'] ?? '', 'filename' => $args['image_filename'] ?? '' ];
            $result = seo_mcp_resolve_one_image( $item, $variation_id );
            if ( is_wp_error( $result ) ) {
                $image_note = ' Luu y: tai anh bien the that bai (' . $result->get_error_message() . ').';
            } else {
                $variation->set_image_id( (int) $result );
                $variation->save();
                $image_note = ' Da gan anh rieng cho bien the.';
            }
        }

        WC_Product_Variable::sync( $parent_id );

        $edit_url = admin_url( 'post.php?post=' . $parent_id . '&action=edit' );
        return [
            'isError' => false,
            'content' => [ [ 'type' => 'text', 'text' => "Da tao bien the ID {$variation_id} cho san pham cha #{$parent_id}.{$image_note} Xem tai: {$edit_url}" ] ],
        ];
    }

if ( $name === 'list_product_variations' ) {
        if ( ! seo_mcp_wc_ready() ) {
            return [ 'isError' => true, 'content' => [ [ 'type' => 'text', 'text' => 'WooCommerce chua san sang tren site nay.' ] ] ];
        }

        $product_id = isset( $args['product_id'] ) ? (int) $args['product_id'] : 0;
        $product    = $product_id ? wc_get_product( $product_id ) : null;
        if ( ! $product || ! $product->is_type( 'variable' ) ) {
            return [ 'isError' => true, 'content' => [ [ 'type' => 'text', 'text' => "product_id {$product_id} khong phai san pham type=variable hop le." ] ] ];
        }

        $variation_ids = $product->get_children();
        if ( empty( $variation_ids ) ) {
            return [ 'isError' => false, 'content' => [ [ 'type' => 'text', 'text' => 'San pham nay chua co bien the nao.' ] ] ];
        }

        $lines = [];
        foreach ( $variation_ids as $vid ) {
            $variation = wc_get_product( $vid );
            if ( ! $variation ) {
                continue;
            }
            $attr_text = [];
            foreach ( $variation->get_variation_attributes() as $attribute_key => $term_slug ) {
                $taxonomy    = str_replace( 'attribute_', '', $attribute_key );
                $term        = $term_slug ? get_term_by( 'slug', $term_slug, $taxonomy ) : false;
                $attr_text[] = str_replace( 'pa_', '', $taxonomy ) . '=' . ( $term ? $term->name : ( $term_slug ?: 'bat ky' ) );
            }
            $lines[] = "#{$vid} - " . implode( ', ', $attr_text ) . " - gia: {$variation->get_regular_price()}, ton kho: {$variation->get_stock_status()} ({$variation->get_stock_quantity()})";
        }

        return [ 'isError' => false, 'content' => [ [ 'type' => 'text', 'text' => implode( "\n", $lines ) ] ] ];
    }

if ( $name === 'update_product_variation' ) {
        if ( ! seo_mcp_wc_ready() ) {
            return [ 'isError' => true, 'content' => [ [ 'type' => 'text', 'text' => 'WooCommerce chua san sang tren site nay.' ] ] ];
        }

        $variation_id = isset( $args['variation_id'] ) ? (int) $args['variation_id'] : 0;
        $variation    = $variation_id ? wc_get_product( $variation_id ) : null;
        if ( ! $variation || ! $variation->is_type( 'variation' ) ) {
            return [ 'isError' => true, 'content' => [ [ 'type' => 'text', 'text' => "Khong tim thay bien the ID {$variation_id}." ] ] ];
        }

        if ( isset( $args['regular_price'] ) )   $variation->set_regular_price( $args['regular_price'] );
        if ( isset( $args['sale_price'] ) )      $variation->set_sale_price( $args['sale_price'] );
        if ( isset( $args['sku'] ) )              $variation->set_sku( $args['sku'] );
        if ( isset( $args['manage_stock'] ) )    $variation->set_manage_stock( (bool) $args['manage_stock'] );
        if ( isset( $args['stock_quantity'] ) )  $variation->set_stock_quantity( $args['stock_quantity'] );
        if ( isset( $args['stock_status'] ) )    $variation->set_stock_status( $args['stock_status'] );
        if ( isset( $args['status'] ) && in_array( $args['status'], [ 'publish', 'private' ], true ) ) {
            $variation->set_status( $args['status'] );
        }

        $image_note = '';
        if ( ! empty( $args['image_url'] ) || ! empty( $args['image_base64'] ) ) {
            $item = ! empty( $args['image_url'] )
                ? [ 'url' => $args['image_url'] ]
                : [ 'base64_data' => $args['image_base64'], 'mime_type' => $args['image_mime_type'] ?? '', 'filename' => $args['image_filename'] ?? '' ];
            $result = seo_mcp_resolve_one_image( $item, $variation_id );
            if ( is_wp_error( $result ) ) {
                $image_note = ' Luu y: tai anh bien the that bai (' . $result->get_error_message() . ').';
            } else {
                $variation->set_image_id( (int) $result );
                $image_note = ' Da cap nhat anh bien the.';
            }
        }

        $variation->save();
        WC_Product_Variable::sync( $variation->get_parent_id() );

        return [
            'isError' => false,
            'content' => [ [ 'type' => 'text', 'text' => "Da cap nhat bien the ID {$variation_id}.{$image_note}" ] ],
        ];
    }

if ( $name === 'list_affiliate_redirects' ) {
        $redirects = get_option( 'seo_go_redirects', [] );
        $redirects = is_array( $redirects ) ? $redirects : [];
        if ( empty( $redirects ) ) {
            return [ 'isError' => false, 'content' => [ [ 'type' => 'text', 'text' => 'Chua co redirect nao.' ] ] ];
        }
        $lines = [];
        foreach ( $redirects as $slug => $url ) {
            $lines[] = home_url( '/go/' . $slug . '/' ) . ' -> ' . $url;
        }
        return [
            'isError' => false,
            'content' => [ [ 'type' => 'text', 'text' => implode( "\n", $lines ) ] ],
        ];
    }

if ( $name === 'set_affiliate_redirect' ) {
        $slug = sanitize_title( $args['slug'] ?? '' );
        $url  = isset( $args['url'] ) ? esc_url_raw( trim( $args['url'] ) ) : '';
        if ( '' === $slug || '' === $url ) {
            return [ 'isError' => true, 'content' => [ [ 'type' => 'text', 'text' => 'Thieu slug hoac url.' ] ] ];
        }
        $redirects         = get_option( 'seo_go_redirects', [] );
        $redirects         = is_array( $redirects ) ? $redirects : [];
        $redirects[ $slug ] = $url;
        update_option( 'seo_go_redirects', $redirects, false );

        $go_url = home_url( '/go/' . $slug . '/' );
        return [
            'isError' => false,
            'content' => [ [ 'type' => 'text', 'text' => "Da luu redirect {$go_url} -> {$url}. Dung {$go_url} lam link trong shortcode [button] thay cho link affiliate goc truc tiep." ] ],
        ];
    }

if ( $name === 'delete_affiliate_redirect' ) {
        $slug = sanitize_title( $args['slug'] ?? '' );
        if ( '' === $slug ) {
            return [ 'isError' => true, 'content' => [ [ 'type' => 'text', 'text' => 'Thieu slug.' ] ] ];
        }
        $redirects = get_option( 'seo_go_redirects', [] );
        $redirects = is_array( $redirects ) ? $redirects : [];
        if ( ! isset( $redirects[ $slug ] ) ) {
            return [ 'isError' => false, 'content' => [ [ 'type' => 'text', 'text' => "Khong co redirect nao voi slug '{$slug}'." ] ] ];
        }
        unset( $redirects[ $slug ] );
        update_option( 'seo_go_redirects', $redirects, false );
        return [
            'isError' => false,
            'content' => [ [ 'type' => 'text', 'text' => "Da xoa redirect /go/{$slug}." ] ],
        ];
    }

if ( $name === 'set_product_faq' ) {
        $product_id = isset( $args['product_id'] ) ? (int) $args['product_id'] : 0;
        $faqs_input = is_array( $args['faqs'] ?? null ) ? $args['faqs'] : [];
        if ( ! $product_id || empty( $faqs_input ) ) {
            return [ 'isError' => true, 'content' => [ [ 'type' => 'text', 'text' => 'Thieu product_id hoac faqs.' ] ] ];
        }
        $clean = [];
        foreach ( $faqs_input as $item ) {
            $q = trim( wp_strip_all_tags( $item['question'] ?? '' ) );
            $a = trim( wp_strip_all_tags( $item['answer'] ?? '' ) );
            if ( '' !== $q && '' !== $a ) {
                $clean[] = [ 'question' => $q, 'answer' => $a ];
            }
        }
        if ( empty( $clean ) ) {
            return [ 'isError' => true, 'content' => [ [ 'type' => 'text', 'text' => 'Khong co cau hoi/dap hop le nao sau khi loc.' ] ] ];
        }
        // QUAN TRONG: phai dung JSON_UNESCAPED_UNICODE khi luu, khong chi luc in
        // ra. update_post_meta()/update_metadata() cua WordPress tu dong goi
        // wp_unslash() truoc khi luu vao DB, se xoa mat ky tu "\" that trong
        // chuoi "ầ" (escape unicode mac dinh cua json_encode), bien no
        // thanh chuoi rac "u1ea7". Dung UNESCAPED_UNICODE de output la UTF-8
        // tho, khong co dau "\" nao ca nen wp_unslash() khong con gi de xoa
        // sai (da xac nhan thuc te tren live 2026-09-14).
        update_post_meta( $product_id, '_seo_faq_schema', wp_json_encode( $clean, JSON_UNESCAPED_UNICODE | JSON_UNESCAPED_SLASHES ) );
        return [
            'isError' => false,
            'content' => [ [ 'type' => 'text', 'text' => 'Da luu ' . count( $clean ) . ' cau hoi/dap FAQ schema cho san pham ID ' . $product_id . '. Se tu dong in ra structured data FAQPage khi xem trang san pham nay.' ] ],
        ];
    }

    if ( $name === 'delete_product_faq' ) {
        $product_id = isset( $args['product_id'] ) ? (int) $args['product_id'] : 0;
        if ( ! $product_id ) {
            return [ 'isError' => true, 'content' => [ [ 'type' => 'text', 'text' => 'Thieu product_id.' ] ] ];
        }
        delete_post_meta( $product_id, '_seo_faq_schema' );
        return [
            'isError' => false,
            'content' => [ [ 'type' => 'text', 'text' => 'Da xoa FAQ schema cua san pham ID ' . $product_id . '.' ] ],
        ];
    }

    return [ 'isError' => true, 'content' => [ [ 'type' => 'text', 'text' => "Khong biet tool: {$name}" ] ] ];
}

function seo_mcp_handle_request( WP_REST_Request $request ) {
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
                'serverInfo'      => [ 'name' => 'seo-blog-mcp', 'version' => '1.0.0' ],
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
            'result'  => [ 'tools' => seo_mcp_tools_schema() ],
        ], 200 );
    }

    if ( $method === 'tools/call' ) {
        $name   = $params['name'] ?? '';
        $args   = $params['arguments'] ?? [];
        $result = seo_mcp_call_tool( $name, $args );
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
