# Project Roadmap

Status as of **2026-05-28**. The site exists, all six pages are live in main, the shared nav/footer are stable. Remaining work is launch readiness, content polish, and infrastructure hardening.

## Phase 1 — Site Foundation ✅ Complete

- [x] Shared top navigation (`nav.js` / `<infina-nav>`).
- [x] Shared footer (`footer.js` / `<infina-footer>`).
- [x] Mobile-responsive nav with hamburger panel.
- [x] AI Work dropdown with sub-page (`focus-alignment.html`).
- [x] Six core pages drafted: `home`, `work`, `inside`, `personal`, `focus-alignment`, `about`.
- [x] Canonical brand tokens established (navy `#001F5C`, Be Vietnam Pro, radius 22px).
- [x] Brand partner logos integrated on `inside.html`.

## Phase 2 — Content Polish 🔄 In Progress

Recent activity (`git log`) shows the team iterating on hero copy, spacing, and demo widgets:
- [x] Standardize hero eyebrow style across pages (commit `dacbf42`).
- [x] Redesign AI Personal panel to card-grid style (commit `4e1a55f`).
- [x] Auto-scroll prompt bar to center active button in the Personal chat demo (commit `f2f7dd4`).
- [x] Lock right-column height on tab switch in Personal demo (commit `41b77c0`).
- [x] Trim "financial" from hero subtext (commit `33378bc`).
- [ ] Final copy review across all six pages with stakeholder sign-off.
- [ ] Open Graph + Twitter card meta tags on every page.
- [ ] Audit alt text on every brand logo and lifestyle image.

## Phase 3 — Launch Readiness ⏳ Next

- [ ] Wire `#demo` CTA to a real destination (form / Calendly / HubSpot).
- [ ] Add `index.html` (or host-level rewrite) so `/` resolves to home.
- [ ] Add `404.html`.
- [ ] Add `robots.txt` and `sitemap.xml`.
- [ ] Add structured data (`Organization`, `WebSite`) JSON-LD to `home.html` and `about.html`.
- [ ] Pick and configure a production host (Vercel / Netlify / Cloudflare Pages). See `deployment-guide.md`.
- [ ] DNS + HTTPS + apex/www redirect.
- [ ] Privacy-friendly analytics (Plausible or Umami) added globally.

## Phase 4 — Performance & QA ⏳ Next

- [ ] Lighthouse pass on all pages (target ≥ 90 each category).
- [ ] Inline image audit — replace any oversized PNG with optimized formats (`webp`/`avif`).
- [ ] Decide whether to inline `nav.js` and `footer.js` into each page or keep external (current).
- [ ] Cross-browser smoke test (Chrome / Safari / Edge / Firefox; iOS Safari; Chrome Android).
- [ ] Keyboard-only navigation pass.

## Phase 5 — Architecture Evolution 📅 Later

Decisions to revisit when the site is stable and content additions slow down:

- [ ] **Migrate to a static-site generator** (Astro or 11ty) to deduplicate the inline CSS that currently lives in all six pages. Each HTML file is ≥ 700 lines and `inside.html` is > 6,700 lines; a templating layer would let copy edits stop touching CSS.
- [ ] **Lift shared CSS** to one or two CSS files (`base.css`, `components.css`). Tokens move to `:root` in `base.css`.
- [ ] **Vietnamese-language variants** for all six pages.
- [ ] **CMS integration** — Sanity / Contentful / Notion-based — once marketing wants to ship copy without engineering.

## Phase 6 — Optional Enhancements 📅 Later

- [ ] Animated hero illustrations (respecting `prefers-reduced-motion`).
- [ ] Personal page chat-demo upgrade — connect to real product API.
- [ ] Customer-story pages with case studies.
- [ ] Pricing / packaging page (if commercial model permits).
- [ ] Resources / blog area.

## Decision Log (Open)

| Decision | Owner | Due |
|----------|-------|-----|
| Choose production host (Vercel / Netlify / Cloudflare Pages) | Eng | Before launch |
| Where the `#demo` CTA lands | Marketing | Before launch |
| Analytics vendor and what to track | Marketing + Eng | Before launch |
| Static-site generator migration — yes/no, and when | Eng | After Phase 4 |

## Milestones (Aspirational)

| Milestone | Target |
|-----------|--------|
| Public launch on production domain | TBD |
| Vietnamese localization shipped | Q3 2026 |
| First customer-story page live | Q3 2026 |
| Site generator migration complete | Q4 2026 |

## How to Update This Roadmap

- After every meaningful feature merge, check the item off and add a one-line note (commit SHA or PR link).
- Move items between phases as priorities shift; don't delete unless explicitly dropped.
- Keep the Open Decision Log honest — close items the moment a decision is made.

## Related Docs

- `project-overview-pdr.md` — what we're building and why.
- `codebase-summary.md` — current state of the code.
- `code-standards.md` — how to make changes safely.
- `system-architecture.md` — how the runtime is wired.
- `design-guidelines.md` — visual language and tokens.
- `deployment-guide.md` — how to ship.
