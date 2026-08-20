<?php
/**
 * Infina AI News — block theme functions.
 *
 * @package InfinaAINews
 */

if ( ! defined( 'ABSPATH' ) ) {
	exit;
}

if ( ! function_exists( 'infina_ai_news_setup' ) ) {
	function infina_ai_news_setup() {
		add_theme_support( 'wp-block-styles' );
		add_theme_support( 'responsive-embeds' );
		add_theme_support( 'editor-styles' );
		add_theme_support( 'html5', array( 'search-form', 'comment-form', 'comment-list', 'gallery', 'caption', 'style', 'script' ) );
		add_editor_style( 'style.css' );
	}
}
add_action( 'after_setup_theme', 'infina_ai_news_setup' );

if ( ! function_exists( 'infina_ai_news_assets' ) ) {
	function infina_ai_news_assets() {
		// Brand font — Be Vietnam Pro.
		wp_enqueue_style(
			'infina-ai-news-fonts',
			'https://fonts.googleapis.com/css2?family=Be+Vietnam+Pro:wght@400;500;600;700;800&display=swap',
			array(),
			null
		);

		// Theme stylesheet.
		wp_enqueue_style(
			'infina-ai-news-style',
			get_stylesheet_uri(),
			array(),
			wp_get_theme()->get( 'Version' )
		);

		// Mobile nav toggle.
		wp_enqueue_script(
			'infina-ai-news-nav',
			get_theme_file_uri( 'assets/js/main.js' ),
			array(),
			wp_get_theme()->get( 'Version' ),
			true
		);
	}
}
add_action( 'wp_enqueue_scripts', 'infina_ai_news_assets' );

/**
 * Home "News" list starts after the 4 posts already shown in the featured area
 * (1 lead + 3 side). Recompute the offset per paginated page so pagination stays
 * correct regardless of core's offset handling. Scoped to the home query (queryId 12).
 */
if ( ! function_exists( 'infina_ai_news_offset_home_query' ) ) {
	function infina_ai_news_offset_home_query( $query, $block ) {
		if ( is_admin() ) {
			return $query;
		}
		if ( 12 !== (int) ( $block->context['queryId'] ?? 0 ) ) {
			return $query;
		}
		$skip     = 4; // posts shown in the featured block above.
		$per_page = (int) ( $query['posts_per_page'] ?? 8 );
		if ( $per_page < 1 ) {
			$per_page = 8;
		}
		$page_key = 'query-' . (int) $block->context['queryId'] . '-page';
		$page     = isset( $_GET[ $page_key ] ) ? max( 1, (int) $_GET[ $page_key ] ) : 1; // phpcs:ignore WordPress.Security.NonceVerification.Recommended
		$query['offset'] = $skip + ( ( $page - 1 ) * $per_page );
		return $query;
	}
}
add_filter( 'query_loop_block_query_vars', 'infina_ai_news_offset_home_query', 10, 2 );

/**
 * Branded placeholder when a post has no featured image, so image-based layouts
 * (side list, news rows, lead) don't collapse. Only fires when there is no thumbnail.
 */
if ( ! function_exists( 'infina_ai_news_thumb_placeholder' ) ) {
	function infina_ai_news_thumb_placeholder( $html, $post_id ) {
		if ( is_admin() || '' !== $html ) {
			return $html;
		}
		$title  = wp_strip_all_tags( (string) get_the_title( $post_id ) );
		$letter = strtoupper( mb_substr( trim( $title ), 0, 1 ) );
		if ( '' === $letter ) {
			$letter = 'I';
		}
		return '<span class="nr-thumb-ph" aria-hidden="true">' . esc_html( $letter ) . '</span>';
	}
}
add_filter( 'post_thumbnail_html', 'infina_ai_news_thumb_placeholder', 10, 2 );
