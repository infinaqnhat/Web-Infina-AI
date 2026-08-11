# Infina AI News — WordPress block theme

A Full-Site-Editing (block) theme for the Infina AI blog, matching the marketing
site's brand (Be Vietnam Pro, navy `#001F5C` / blue `#1863DC`). Newsroom-style home
(featured post + side list + news table + search/promo aside), plus single post,
page, archive, search and 404.

## Structure
| Path | Purpose |
|------|---------|
| `style.css` | Theme header + all brand styles |
| `theme.json` | Colors, fonts, layout (contentSize 720 / wideSize 1100) |
| `functions.php` | Enqueues Be Vietnam Pro (Google Fonts), stylesheet, mobile-nav JS; theme supports |
| `templates/home.html` | **Blog home** — featured + side list + news table + aside |
| `templates/index.html` | Fallback (same as home) |
| `templates/single.html` | Single post + author card |
| `templates/page.html` | Static page |
| `templates/archive.html` | Category/tag/author archive (news table) |
| `templates/search.html` | Search results (news table) |
| `templates/404.html` | Not found |
| `parts/header.html` | Nav (logo + links to main site + News + CTA + mobile) |
| `parts/footer.html` | Footer |
| `assets/` | Logo, mobile-nav JS |

## Navigation
The header/footer links are static (block markup via a Custom-HTML block), pointing
to the main marketing site (`https://infina.ai/…`) plus the `News` link (`/news/`).
Edit `parts/header.html` / `parts/footer.html` (or the Site Editor → Patterns/Template
Parts) to change them.

## Running the blog under `infina.ai/news` (subdirectory — SEO on main domain)
This is **WordPress + server config, not theme code**:

1. Install WordPress in a `/news` subdirectory (or map it there), and set
   **Settings → General → Site Address (URL)** to `https://infina.ai/news`.
2. Reverse-proxy (nginx example): route `/news` to WordPress; the rest of `infina.ai`
   keeps serving the static marketing site.
   ```nginx
   location /news/ {
       try_files $uri $uri/ /news/index.php?$args;
   }
   ```
3. Permalinks: **Settings → Permalinks → Post name** (recommended) so URLs are
   `infina.ai/news/post-slug/`.

## Install
1. Zip the `infina-ai-news/` folder → `infina-ai-news.zip`.
2. WP Admin → **Appearance → Themes → Add New → Upload Theme** → activate.
3. Create a few posts (with Featured image + a Category) to populate the newsroom.
4. Optional: add a `screenshot.png` (1200×900) in the theme root for the theme card.

## Notes
- Featured + side list always show the latest **4** posts (highlights), on every page;
  the News table below paginates through all posts.
- **AJAX pagination**: clicking the News table's Previous/Next fetches the target page
  and swaps only the table in place, keeping the viewport (falls back to normal
  navigation if JS is off). See `assets/js/main.js`.
- WordPress analog of Ghost's "Feature this post" is a **sticky post** ("Stick to the
  top of the blog" in the post's visibility settings). The featured queries currently
  show the latest posts by date; to prioritise sticky/featured posts, a custom query
  via `functions.php` can be added.
- Search uses the core Search block. The promo card is a static Custom-HTML block —
  edit its text/link in `templates/home.html`.
