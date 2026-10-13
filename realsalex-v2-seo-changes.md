# Money page on-page SEO: numbered proposals (nothing applied)

- **Page:** https://infina.ai/ (design source `realsalex-v2.html`). `main` is unchanged: the earlier edits were reverted.
- **Target keyword:** AI assistant for real estate agents
- **Where:** HTML = can be done in `realsalex-v2.html`; React = needs the React codebase; Infra = server/hosting config; Content = needs a decision from the team.
- Priority: P0 = affects indexing, P1 = affects ranking or snippets, P2 = polish.

| # | Area | Current state | Proposed change | Where | Priority | Decision needed |
|---|---|---|---|---|---|---|
| 1 | Rendering | Server returns an empty 1.8 KB shell for every URL. Title, meta and content appear only after JS | Prerender or SSR `/` and `/vn`, or at least put title, description, canonical and OG in the static `index.html` | React / Infra | P0 | Which method (build-time prerender vs SSR)? |
| 2 | Soft 404 | Unknown paths and missing files (for example `realsalex-tvc-poster.webp`) return 200 with the shell. `/sitemap_index.xml` and `/llms.txt` too | Return real 404 for paths not in the router and for missing assets. Remove or create real `llms.txt` and `sitemap_index.xml` | Infra / React | P0 | Do you want an `llms.txt`? |
| 3 | Canonical | No canonical tag. `http://infina.ai` redirects to `https://infina.ai:443/` | Add `<link rel="canonical" href="https://infina.ai/">`. Make the redirect go to `https://infina.ai/` | HTML / Infra | P0 | - |
| 4 | H1 | Two H1s are shown (one per hero slide) | Keep one H1 (on the default Listing Agent slide), turn the other hero heading into an H2 with the same style | HTML / React | P0 | Final H1 wording (see #5) |
| 5 | H1 wording | "Turn every brochure and yard sign into a 24/7 Property Expert." has no searchable keyword | Option A: "AI assistant for real estate agents: turn every brochure and yard sign into a 24/7 Property Expert." (long, about 5 lines). Option B: keep the current headline and put the keyword in an eyebrow line above it. Option C: a shorter H1 such as "The AI assistant for real estate agents" with the current line as sub-heading | HTML / React | P1 | Pick A, B, C or your own |
| 6 | Title tag | "Send a 24/7 Home Concierge" (26 chars), no keyword, no brand | Proposed: "AI Assistant for Real Estate Agents \| Real Sale X by Infina" (59 chars) | HTML / React | P1 | Confirm wording and brand order |
| 7 | Meta description | About 215 chars, gets truncated, no keyword | Proposed (154 chars): "Real Sale X is an AI assistant for real estate agents. Turn any listing into a 24/7 expert that answers buyer questions and shows you who is ready to act." | HTML / React | P1 | Confirm wording |
| 8 | Product naming | Title says "Home Concierge", body says "Property Expert" and "advisor" | Pick one primary name. Option: keep both names but always frame them as "AI assistant" (hero, H2, alt, CTA) | HTML / React | P1 | Which name is primary? Changing it touches buttons, JS and demo pages |
| 9 | Keyword in copy | The phrase "AI assistant" barely appears on the page | Use it naturally in the hero sub-copy, one section H2, the video poster alt and the FAQ. Avoid stuffing | HTML / React | P1 | - |
| 10 | FAQ | No FAQ | Add a visible FAQ (5-6 questions): what it is, how it works, does it replace the agent, does it make up answers, CRM/setup needed, login needed. Use only facts already on the page. Mirror it in `FAQPage` JSON-LD | HTML / React | P1 | Check every answer against the real product. Add pricing question only if you have a public price |
| 11 | Open Graph / Twitter | Only title, description and type (set by JS). No image, no url, no twitter card | Add `og:url`, `og:image` (+ alt), `og:site_name`, `og:locale`, `twitter:card=summary_large_image`, `twitter:title/description/image` | HTML / React | P1 | Need a dedicated 1200x630 share image |
| 12 | Structured data | No JSON-LD on the homepage | Add `Organization`, `WebSite`, `SoftwareApplication` (Real Sale X, no fake price or rating), and `FAQPage` if #10 is done | HTML / React | P1 | Official company name, logo URL and social profile URLs |
| 13 | hreflang | None on the homepage | `en-US` -> `/`, `vi` -> `/vn`, `x-default` -> `/` on both pages | HTML / React | P1 | Is `/vn` a full Vietnamese version of the same page? |
| 14 | Robots meta | None | `index, follow, max-image-preview:large` (optional, default is index) | HTML / React | P2 | - |
| 15 | Internal links (out) | Only `#hash` links and JS buttons. No link to `/news` or other pages | Add a "Guides for agents" block with 3 links: `/news/real-estate-marketing/`, `/news/real-estate-marketing-plan/`, `/news/real-estate-lead-follow-up-automation-guide/`. Add real links (About, Blog) to nav/footer | HTML / React | P2 | Which articles to feature? |
| 16 | Internal links (in) | Articles in the `/news` cluster do not link to the money page | Add contextual links from relevant `/news` articles to `https://infina.ai/` with natural anchors, such as "AI assistant for real estate agents" (one link per article) | Content (WordPress) | P2 | Which articles; limit per article |
| 17 | Footer | Only "(c) 2026" and the geolocation credit. No Privacy, Terms or contact | Add Privacy Policy, Terms and contact email or address | React / shared `footer.js` | P2 | Final URLs of the legal pages |
| 18 | Testimonials | Three named testimonials with brokerage and dollar volume. The spec marks them "TBD, need real quote" | Replace with real, approved quotes, or remove them. Not changed so far | Content | P1 (compliance) | Are these real? Do you have permission? |
| 19 | Images | webp files are large (about 200-370 KB each). Missing `width`/`height` on most | Compress to about 120 KB or less, add `width`/`height`, preload only the hero (LCP) image | HTML / React | P2 | - |
| 20 | JS bundle | One 3.7 MB JS bundle for the whole app | Code-split: load the app and deal-room code only when needed | React | P2 | - |
| 21 | Sitemap | 7 URLs, no `lastmod`. `/inside`, `/work`, `/personal` serve the same empty shell | Add `lastmod`, list only pages with real content, and add the `/news` sitemap | Infra | P2 | Which pages stay indexable? |
| 22 | Video poster | Poster file returns an HTML page with status 200 instead of an image | Check the path and file; fix the missing asset (see #2) | React / Infra | P2 | - |

## Suggested order
1. P0 first: #1, #2, #3, #4. Without #1, the tags in #6, #7, #11-#13 only work if Google runs the JS.
2. Then agree on the wording items (#5, #6, #7, #8, #10) before any edit is made.
3. Then #11-#13, #15-#16, and the content check in #18.
4. Polish and performance last (#14, #17, #19-#22).

## How to reply
Send the numbers and your changes, for example "5 = option C; 6 = ok; 8 = Property Expert is the main name; skip 14". I will apply only what you confirm.
