# Deployment Guide

The site is a flat directory of HTML/JS/image files. No build step, no environment variables, no server runtime. Any static host will serve it.

## 1. Pre-deploy Checklist

- [ ] `home.html` opens in a browser with no console errors.
- [ ] Nav highlights the right item on every page (`home.html`, `work.html`, `inside.html`, `personal.html`, `focus-alignment.html`, `about.html`).
- [ ] Mobile hamburger opens, closes via Esc / outside click / link click / resize past 768px.
- [ ] All `#demo` CTAs point at the production destination (form / Calendly URL). Today they are in-page anchors only — wire them before launch.
- [ ] All `<title>` strings are correct.
- [ ] Brand logos load from `uploads/`; lifestyle images load from `assets/` and `uploads/`.
- [ ] No console 404s on font preconnect (Google Fonts).

## 2. Local Smoke Test

Run a static server from the repo root:

```bash
python3 -m http.server 8080
# visit http://localhost:8080/home.html
```

Or:

```bash
npx serve .
```

`file://` also works for quick checks (Custom Elements run from disk), but image paths in some browsers behave oddly under `file://` — prefer the local server.

## 3. Recommended Hosts

Any of these are appropriate. Pick one and stick with it.

### Vercel
```bash
npm i -g vercel
vercel --prod
```
Drop the repo as a "static" project. Set the output directory to the repo root. No build command needed.

### Netlify
```bash
npx netlify-cli deploy --dir . --prod
```
Or drag-and-drop the repo folder into the Netlify UI. Set publish directory to `.`.

### Cloudflare Pages
- Connect the repo in the Pages dashboard.
- Build command: *(none)*.
- Output directory: `/`.
- Production branch: `main`.

### GitHub Pages
- Settings → Pages → Source = `main` branch, folder `/ (root)`.
- Site will publish to `https://<user>.github.io/Web-Infina-AI/`.
- Internal links work because they are relative (`href="work.html"`).

### Generic S3 / nginx
- Upload the repo contents preserving directory structure.
- Configure your host to serve `home.html` as the index for `/`, **or** rename `home.html` → `index.html` at deploy time.

## 4. Optional Renames on Deploy

To make `/` resolve to the homepage on hosts that expect `index.html`:

```bash
# Option A: deploy-time copy (don't commit)
cp home.html index.html
```

Or configure host-level rewrites:
- Vercel: `vercel.json` with `"rewrites": [{ "source": "/", "destination": "/home.html" }]`.
- Netlify: `_redirects` file with `/  /home.html  200`.
- Cloudflare Pages: `_redirects` file with the same syntax.

## 5. Caching & Headers

For a marketing site, the defaults are fine, but tighten when you have a real CDN:

| Asset class | Recommended `Cache-Control` |
|-------------|-----------------------------|
| `*.html` | `public, max-age=300, must-revalidate` (5 min) |
| `nav.js` / `footer.js` | `public, max-age=300` (or fingerprint and use `immutable`) |
| `assets/*`, `uploads/*` | `public, max-age=31536000, immutable` (1 year) |

Add `Strict-Transport-Security`, `X-Content-Type-Options: nosniff`, and a sane `Content-Security-Policy` once the host is chosen.

## 6. Domain & DNS

- Point the apex (`infina.ai` or chosen domain) at the static host.
- Add a `www` redirect.
- Enforce HTTPS.

## 7. Post-deploy Verification

- Visit each of the six pages on production.
- Run Lighthouse on `home.html` and `inside.html` — target ≥ 90 across all four categories.
- Verify Google Fonts loads (no FOUT issue).
- Confirm the demo CTA destination works end-to-end (form submission, calendar link, etc.).

## 8. Rollback

Because deploys are static, rollback is trivial:
- Vercel / Netlify / Cloudflare Pages — promote a previous deployment from the dashboard.
- GitHub Pages — `git revert` the offending commit on `main`, push.
- S3 — re-upload the previous snapshot.

## 9. Things That Don't Exist Yet (Add Before Launch)

- `index.html` → `home.html` rewrite (or rename).
- Real destination on `#demo` (form / Calendly / HubSpot).
- Analytics (Plausible / Umami / GA4) if marketing wants the data.
- Open Graph + Twitter card meta on every page for share previews.
- `sitemap.xml` and `robots.txt`.
- 404 page (`404.html`) — most hosts wire it automatically when the file exists.

## 10. CI/CD

No pipelines today. When you add one:
- Run an HTML validator (`html-validate` or `vnu`) on `*.html` to catch broken markup.
- Run Lighthouse CI on push to `main`.
- Auto-deploy to the chosen host on `main` push (Vercel/Netlify/CF Pages do this out of the box).
