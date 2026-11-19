# ReallyWise workspace

Working copies of every page that belongs to the ReallyWise product (formerly Infina AI property US),
kept here so the rebrand can happen without touching the Infina AI company site at the repo root.
Files marked done in the status table below are rebranded to the ReallyWise guideline (v1.0). Everything else is still a plain
duplicate of the root files. The brand source of truth is `brand/`.

## Rebrand status
| File | Status |
|---|---|
| `reallywise.html`, `nav.js`, `footer.js` | Done. One page with three views: the homepage (no hash), the listing agents tab (`#listing-agent`) and the buyer agents tab (`#buyer-agent`). The logo and `#home` go to the homepage; `#mission`, `#fight`, `#tools` and `#endings` are homepage anchors (reachable by link, not from the menu). `nav.js` and `footer.js` are the `rw-nav` and `rw-footer` components and only serve ReallyWise pages |
| `property-expert-demo-tour.html`, `property-expert-admin-demo-tour.html` | Done (assistant name Realisa kept) |
| `property-expert-presentation.html` | Done. MVP pitch deck: Property Expert and Realisa only (no Home Concierge), built around the ReallyWise mission: capture every lead and turn it into a hot lead (a booked viewing), deepen every relationship, multiply your capacity, close more deals. Light hero with `uploads/home-hero-agent.jpg`. One Capture and convert slide (from a conversation to a hot lead) and a Realisa slide with its intro video. 13 slides on the web, 10 PDF pages (`uploads/ReallyWise-Property-Expert-Presentation.pdf`). Plays the Property Expert promo and lead capture videos and the Realisa intro |
| `property-expert-presentation-v1.html` | Saved v1 of the MVP deck (Nov 19, 2026), frozen; its PDF is `uploads/ReallyWise-Property-Expert-Presentation-v1.pdf` and the git tag is `reallywise-mvp-deck-v1`. Edit `property-expert-presentation.html` for new versions |
| `property-expert-short.html` | Short version of the MVP deck: hero, Your AI team, Property Expert, Realisa, How it works, thank you. 6 slides and a 6-page PDF (`uploads/ReallyWise-Property-Expert-Short.pdf`). Cut from the full deck by `deck-src/build-property-expert-short.py`; buttons for the demos link to the full deck |
| everything else | Not started |

Navy on the landing page follows guideline v2: Navy 900 `#012976`, Navy 700 `#013A9E`, Navy 500 `#33599F`, Navy 100 `#E4E9F3` (hover navy `#011F59` is derived).

Landing page follows guideline v2: Inter for headings and UI (Montserrat only for large numbers), DM Sans for text and buttons, DM Mono for data, logo at least 140px wide, soft corners, surface `#F4F6FB` and line `#DBE1EE`.

The homepage hero is full-bleed like the two tabs and reads its photo from `uploads/home-hero.jpg`. The photo was generated with Gemini (gemini-3-pro-image): an agent shaking hands with a couple in front of a craftsman home, white clouds at the top left like the two tab heroes. Swap the file to change it; nothing else needs to change. Overlay, brightness and clear area defaults are the same as the tabs.

`property-expert-demo-tour.html` is also rebranded to guideline v2 (fonts, navy and green, ReallyWise logo and favicon, chat-bubble avatar, sentence-case labels, factual school line, estimate disclaimer). The assistant is still called Realisa. `property-expert-admin-demo-tour.html` is rebranded the same way (logo in the left nav, claim buttons in Insight Green). The other four demo pages are not rebranded yet.

Defaults used for the landing page, change them in one place if the answer differs:
- Text name is "ReallyWise" (no ".ai"); `reallywise.ai` is used only as the domain in canonical, Open Graph and JSON-LD.
- "Property Expert" and "Home Concierge" stay as feature names.
- No Vietnamese `hreflang` alternate, since the brand copy is US English.
- The Open Graph image and JSON-LD logo point at `https://reallywise.ai/...`, which does not exist until the site is deployed there.

## Layout
| Path | What it is | Copied from |
|---|---|---|
| `brand/ReallyWise-Brand-Guideline.html` | Brand guideline v2 (replaces v1; App icon is now the white-background version, the navy one is "Bản nền màu") | uploaded by the team |
| `brand/Really_Wise_Logo.svg`, `brand/Really_Wise_Logo_white.svg` | Primary logo and its white version (chat-house mark with "reallyWise"; rebalanced version, Nov 17, 3479x698, ratio 4.98:1) | uploaded by the team |
| `brand/reallywise-app-icon.svg`, `brand/reallywise-app-icon-color.svg`, `brand/reallywise-favicon.svg` | Chat-bubble app icon: white-background version (primary), navy-background version, and the favicon (the same artwork as the app icon). Extracted from the guideline v2; the favicon and apple-touch icon on the landing page use these | guideline v2 |
| `brand/reallywise-logo-primary.png`, `-reversed.png`, `-mono.png` | Logo PNGs rendered from the logo SVGs. Reversed comes from the white SVG; mono is derived by recoloring | rendered from `Really_Wise_Logo.svg` |
| `reallywise.html` | Product landing page | `realsalex-v2.html` (renamed) |
| `nav.js`, `footer.js` | Shared nav and footer web components | `nav.js`, `footer.js` |
| `property-expert-demo*.html`, `property-expert-admin-demo*.html` | Six demo pages: notification flow, long Hob tour, short tour, each with its admin page | same names at the root |
| `dashboard/` | Static export of the agent dashboard (62 pages) | `dashboard/` |
| `investor-overview.html`, `product-presentation.html` | Pitch pages | same names at the root |
| `scripts/build-presentation-pdf.mjs` | Builds a PDF from a presentation page: `node scripts/build-presentation-pdf.mjs [page] [pdf name]`, defaults to `product-presentation.html` and `AI-Property-Product-Presentation.pdf` | `scripts/` |
| `uploads/property-expert-promo.mp4`, `-lead-capture.mp4` and their posters | The Property Expert videos (1:12 promo, 1:11 lead capture) | the video artifacts |
| `uploads/realisa-intro.mp4`, `realisa-intro-poster.jpg`, `realisa-intro-card.jpg` | Realisa intro video (1:08) and stills | branch `claude/stoic-mayer-d2yx6f` |
| `realsalex-mockups/` | Dashboard, deal room and email mockups | `realsalex-mockups/` |
| `wordpress-theme/infina-ai-news/` | News blog block theme | `wordpress-theme/infina-ai-news/` |
| `uploads/` | Only the images, video and PDF these pages reference | `uploads/` |

## Notes
- The MVP deck is generated: edit `deck-src/property-expert-slides.html` (slides) or `deck-src/build-property-expert-presentation.py` (brand styles, scripts), then run `python3 reallywise/deck-src/build-property-expert-presentation.py` and rebuild its PDF. For the short version, then run `python3 reallywise/deck-src/build-property-expert-short.py` and `node scripts/build-presentation-pdf.mjs property-expert-short.html ReallyWise-Property-Expert-Short.pdf` from `reallywise/`. The build reuses the root `product-presentation.html` for the slide engine and the live demo slides.
- Paths stay relative, so each page opens from this folder the same way it does from the root.
- The WordPress theme keeps its original folder name and `style.css` header for now. Rename both before installing
  it next to the original theme, or the two will conflict.
- Rebuild the PDFs from this folder with `node scripts/build-presentation-pdf.mjs` and `node scripts/build-presentation-pdf.mjs property-expert-presentation.html ReallyWise-Property-Expert-Presentation.pdf` (Playwright with Chromium required).
