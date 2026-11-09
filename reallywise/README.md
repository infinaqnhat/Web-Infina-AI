# ReallyWise workspace

Working copies of every page that belongs to the ReallyWise product (formerly Infina AI property US),
kept here so the rebrand can happen without touching the Infina AI company site at the repo root.
Everything in this folder is a plain duplicate of the root files at the time of copying and has not been
rebranded yet. The brand source of truth is `brand/`.

## Layout
| Path | What it is | Copied from |
|---|---|---|
| `brand/ReallyWise-Brand-Guideline.html` | Brand guideline v1.0 (11/2026) | uploaded by the team |
| `brand/Really_Wise_Logo.svg` | Primary logo | uploaded by the team |
| `realsalex-v2.html` | Product landing page | `realsalex-v2.html` |
| `nav.js`, `footer.js` | Shared nav and footer web components | `nav.js`, `footer.js` |
| `property-expert-demo*.html`, `property-expert-admin-demo*.html` | Six demo pages: notification flow, long Hob tour, short tour, each with its admin page | same names at the root |
| `dashboard/` | Static export of the agent dashboard (62 pages) | `dashboard/` |
| `investor-overview.html`, `product-presentation.html` | Pitch pages | same names at the root |
| `scripts/build-presentation-pdf.mjs` | Builds `uploads/AI-Property-Product-Presentation.pdf` from the presentation | `scripts/` |
| `realsalex-mockups/` | Dashboard, deal room and email mockups | `realsalex-mockups/` |
| `wordpress-theme/infina-ai-news/` | News blog block theme | `wordpress-theme/infina-ai-news/` |
| `uploads/` | Only the images, video and PDF these pages reference | `uploads/` |

## Notes
- Paths stay relative, so each page opens from this folder the same way it does from the root.
- `nav.js` links to company pages (`home.html`, `work.html`, `personal.html`, `inside.html`) that are not duplicated
  here, so those links do not resolve inside this folder until the nav is rewired.
- The WordPress theme keeps its original folder name and `style.css` header for now. Rename both before installing
  it next to the original theme, or the two will conflict.
- Rebuild the PDF from this folder with `node scripts/build-presentation-pdf.mjs` (Playwright with Chromium required).
