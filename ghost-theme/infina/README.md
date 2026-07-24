# Infina AI — Ghost blog theme

A minimal Ghost theme for the Infina AI blog, matching the marketing site's brand
(Be Vietnam Pro, navy `#001F5C` / blue `#1863DC`). Ships a blog home (featured post
+ card grid), single post, static page, tag/author archives, and a 404.

## Templates
| File | Purpose |
|------|---------|
| `default.hbs` | Base layout (head, header, footer, scripts) |
| `index.hbs` | Blog home — 1 featured post + grid + pagination |
| `post.hbs` | Single blog post + author card + related posts |
| `page.hbs` | Static page |
| `tag.hbs` / `author.hbs` | Archive listings |
| `error.hbs` | 404 / error |
| `partials/header.hbs` | Nav (logo + Ghost `{{navigation}}` + CTA + mobile) |
| `partials/footer.hbs` | Footer |
| `partials/navigation.hbs` | Menu item markup (driven by Ghost Admin → Settings → Navigation) |
| `partials/post-card.hbs` | Reusable post card |
| `partials/pagination.hbs` | Pagination controls |

## Navigation
Menu is managed in **Ghost Admin → Settings → Navigation**. Add the marketing-site
links there (e.g. `AI Inside` → `https://infina.ai/inside.html`, `AI Work` →
`https://infina.ai/work.html`, `AI Personal` → `https://infina.ai/personal.html`,
`News` → `https://infina.ai/news/`). The logo and footer links point to the main site.

## Running the blog under `infina.ai/news` (subdirectory — SEO on main domain)
This is **server config, not theme code**:

1. In Ghost's `config.production.json`, set:
   ```json
   { "url": "https://infina.ai/news" }
   ```
2. Reverse-proxy (nginx example): route `/news` to the Ghost instance while the rest
   of `infina.ai` continues serving the static marketing site.
   ```nginx
   location /news/ {
       proxy_pass http://127.0.0.1:2368;
       proxy_set_header Host $host;
       proxy_set_header X-Forwarded-Proto $scheme;
   }
   ```
All internal links use Ghost helpers (`{{url}}`, `{{asset}}`, `{{@site.url}}`), so they
are automatically prefixed with `/news`. `{{ghost_head}}` emits canonical/OG/JSON-LD
under `infina.ai/news/...` for SEO.

## Install
1. Zip the `infina/` folder → `infina.zip`.
2. Ghost Admin → **Settings → Design → Change theme → Upload theme**.
3. Recommended: validate first with [GScan](https://gscan.ghost.org/) or
   `npx gscan .` from inside the theme folder.
