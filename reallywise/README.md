# ReallyWise workspace

Working copies of every page that belongs to the ReallyWise product (formerly Infina AI property US),
kept here so the rebrand can happen without touching the Infina AI company site at the repo root.
Files marked done in the status table below are rebranded to the ReallyWise guideline (v1.0). Everything else is still a plain
duplicate of the root files. The brand source of truth is `brand/`.

## Rebrand status
| File | Status |
|---|---|
| `reallywise.html`, `nav.js`, `footer.js` | Done. Name, logo, fonts, colors, hero, copy, metadata. `nav.js` and `footer.js` are now the `rw-nav` and `rw-footer` components and only serve ReallyWise pages |
| everything else | Not started |

Defaults used for the landing page, change them in one place if the answer differs:
- Text name is "ReallyWise" (no ".ai"); `reallywise.ai` is used only as the domain in canonical, Open Graph and JSON-LD.
- "Property Expert" and "Home Concierge" stay as feature names.
- No Vietnamese `hreflang` alternate, since the brand copy is US English.
- The Open Graph image and JSON-LD logo point at `https://reallywise.ai/...`, which does not exist until the site is deployed there.

## Layout
| Path | What it is | Copied from |
|---|---|---|
| `brand/ReallyWise-Brand-Guideline.html` | Brand guideline v1.0 (11/2026) | uploaded by the team |
| `brand/Really_Wise_Logo.svg` | Primary logo | uploaded by the team |
| `brand/reallywise-app-icon.svg`, `brand/reallywise-favicon.svg` | App icon and favicon, copied from the guideline | extracted from the guideline |
| `brand/reallywise-logo-primary.png`, `-reversed.png`, `-mono.png` | Official logo PNGs, copied from the guideline downloads. The landing page uses the primary SVG only | extracted from the guideline |
| `reallywise.html` | Product landing page | `realsalex-v2.html` (renamed) |
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
- The WordPress theme keeps its original folder name and `style.css` header for now. Rename both before installing
  it next to the original theme, or the two will conflict.
- Rebuild the PDF from this folder with `node scripts/build-presentation-pdf.mjs` (Playwright with Chromium required).
