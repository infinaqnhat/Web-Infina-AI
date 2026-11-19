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
| `brand/Really_Wise_Logo.svg`, `brand/Really_Wise_Logo_white.svg` | Primary logo and its white version (chat-house mark with "reallyWise", Nov 11) | uploaded by the team |
| `brand/Really_Wise_Logo_balanced.svg`, `brand/Really_Wise_Logo_balanced_white.svg` | Balanced version of the primary logo, matched to the reference image from the team: wordmark lowered to sit on the icon's base, "really" x-height equal to "Wise", tighter spacing in "ise", dots lowered to the middle of the icon. Used by the lead capture video; the landing page still uses `Really_Wise_Logo.svg` | adjusted from `Really_Wise_Logo.svg` |
| `brand/reallywise-app-icon.svg`, `brand/reallywise-app-icon-color.svg`, `brand/reallywise-favicon.svg` | Chat-bubble app icon: white-background version (primary), navy-background version, and the favicon (the same artwork as the app icon). Extracted from the guideline v2; the favicon and apple-touch icon on the landing page use these | guideline v2 |
| `brand/reallywise-logo-primary.png`, `-reversed.png`, `-mono.png` | Logo PNGs rendered from the logo SVGs. Reversed comes from the white SVG; mono is derived by recoloring | rendered from `Really_Wise_Logo.svg` |
| `reallywise.html` | Product landing page | `realsalex-v2.html` (renamed) |
| `nav.js`, `footer.js` | Shared nav and footer web components | `nav.js`, `footer.js` |
| `property-expert-demo*.html`, `property-expert-admin-demo*.html` | Six demo pages: notification flow, long Hob tour, short tour, each with its admin page | same names at the root |
| `dashboard/` | Static export of the agent dashboard (62 pages) | `dashboard/` |
| `investor-overview.html`, `product-presentation.html` | Pitch pages | same names at the root |
| `scripts/build-presentation-pdf.mjs` | Builds `uploads/AI-Property-Product-Presentation.pdf` from the presentation | `scripts/` |
| `realsalex-mockups/` | Dashboard, deal room and email mockups | `realsalex-mockups/` |
| `wordpress-theme/infina-ai-news/` | News blog block theme | `wordpress-theme/infina-ai-news/` |
| `video/lead-capture-video.html`, `video/render-video.mjs`, `video/voiceover.json`, `video/voiceover.py` | Lead capture explainer video (about 71 s, 1920x1080, English voice-over and burned-in subtitles): share kit, six channels (yard sign, open house, social, text and email, postcards, website), buyer chat with Realisa, lead in the dashboard. The voice-over script, timings and voice settings live in `voiceover.json`. `GEMINI_API_KEY=... python video/voiceover.py gemini` builds it with Google Gemini TTS (model `gemini-3.8-flash-tts`, voice `Laomedeia`, director's notes for an excited but clear Bay Area SaaS-intro read; each clip is transcribed back and regenerated if it does not match the script); `python video/voiceover.py kokoro <model dir>` uses the offline Kokoro voice instead. Either way it writes `voiceover.m4a`, `subtitles.srt` and `subtitles.js`, caches clips in `video/.vo-cache/` (git-ignored) and never stores the API key. Lines keep their natural pace: when a line runs long, the picture waits for it (`TIMEWARP` in `subtitles.js`), so the video length follows the voice-over. A cue can carry `{"rate": 1.3}` to play that line, and the picture leading to it, faster. The HTML plays in a browser (click to play with sound, `?t=30` jumps to a time, `?nosubs` hides subtitles); `node video/render-video.mjs` renders it frame by frame and muxes the voice-over into `uploads/property-expert-lead-capture.mp4` (`--nosubs`, `--silent` for other cuts; Playwright and ffmpeg required). The QR code encodes `https://reallywise.ai/l/123-main` | new |
| `video/promo/` (`promo.html`, `voiceover.json`, `capture-ui.cjs`, `shots/`) | Promo video for email and the website (about 1:24 after a 1.3x speed-up of the 1:49 render, benefit-led, with Realisa the agent assistant, Gemini voice-over and subtitles), built on screenshots of the real product UI: the buyer demo, the admin demo, the landing page create flow and the dashboard export. `node capture-ui.cjs` retakes the screenshots and records the boxes of the UI elements the video zooms to and highlights (`shots/regions.js`). The published files are the render sped up 1.3x (`setpts=PTS/1.3` and `atempo=1.3`), with the thumbnail as a 0.1 s first frame and as embedded cover art, and `uploads/property-expert-promo-1.3x.srt` as the matching subtitles. The thumbnail `uploads/property-expert-promo-thumbnail.jpg` comes from `promo/thumbnail.html` (`node promo/render-thumbnail.cjs`). Screens stay still; each feature is circled on the screen and shown enlarged in a card beside it. Outputs `uploads/property-expert-promo.mp4` (1080p) and `uploads/property-expert-promo-720p.mp4` (about 6.5 MB, for email and web). Dashboard numbers come from the demo account and are labelled as such. This replaces the product tour video, which used drawn mockups instead of the real UI | new |
| `video/product-tour/` (`product-tour.html`, `voiceover.json`), `video/video-engine.js` | Full product tour video (about 3 min, 1920x1080, Gemini voice-over and subtitles) covering every Property Expert feature in nine chapters: set up, what it knows, share, buyers, inbox, open questions, showings and offers, pipeline and insights, sellers. One listing (123 Main Street) and one agent (Alex Rivera) throughout; dashboard numbers are marked sample data. Build: `python video/voiceover.py gemini --dir product-tour`, then `node video/render-video.mjs --page product-tour/product-tour.html --out ../uploads/property-expert-product-tour.mp4`. `video-engine.js` is the shared player (timeline, time warp, subtitles, cursor targets) | new |
| `uploads/` | Only the images, video and PDF these pages reference | `uploads/` |

## Notes
- Paths stay relative, so each page opens from this folder the same way it does from the root.
- The WordPress theme keeps its original folder name and `style.css` header for now. Rename both before installing
  it next to the original theme, or the two will conflict.
- Rebuild the PDF from this folder with `node scripts/build-presentation-pdf.mjs` (Playwright with Chromium required).
