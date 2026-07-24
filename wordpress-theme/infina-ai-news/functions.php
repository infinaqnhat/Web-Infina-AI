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
