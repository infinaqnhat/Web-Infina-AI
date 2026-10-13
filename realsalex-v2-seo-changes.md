# realsalex-v2.html: on-page SEO changes (review note)

- **File:** `realsalex-v2.html` (on `main`, commit `6baad6b`)
- **Target keyword:** AI assistant for real estate agents
- **Scope:** this file only. The live `infina.ai` page is a React port, so the tags below reach the live site only once they are applied in that codebase (see "Still open").

## 1. Changes made

### Head
| Item | Before | After |
|---|---|---|
| `<title>` | Send a 24/7 Home Concierge (26 chars) | AI Assistant for Real Estate Agents \| Real Sale X by Infina (59 chars) |
| Meta description | about 215 chars (gets truncated), no keyword | 154 chars: "Real Sale X is an AI assistant for real estate agents. Turn any listing into a 24/7 expert that answers buyer questions and shows you who is ready to act." |
| Robots | none | `index, follow, max-image-preview:large` |
| Canonical | none | `https://infina.ai/` |
| hreflang | none | `en-US` -> `/`, `vi` -> `/vn`, `x-default` -> `/` |
| Open Graph | none | type, site_name, locale, url, title, description, image, image:alt |
| Twitter card | none | `summary_large_image` with title, description, image |
| JSON-LD | none | `Organization`, `WebSite`, `SoftwareApplication` (Real Sale X), `FAQPage` |

### Body
| Item | Before | After |
|---|---|---|
| H1 | 2 H1s (one per hero slide) | 1 H1 on the default slide (Listing Agent): "AI assistant for real estate agents: turn every brochure and yard sign into a 24/7 Property Expert." |
| Buyer-slide heading | H1 | H2 with class `hero-title`, same look (CSS selectors extended) |
| Hero copy | no keyword | Buyer sub-copy starts with "Real Sale X gives every buyer..."; listing sub-copy says "an AI assistant that knows everything about the property" |
| Alt text | "Real Sale X, watch the film"; hero photo alt generic | Poster alt "Real Sale X, the AI assistant for real estate agents: watch the film"; hero photo alt reworded |
| FAQ section (new, `#faq`) | none | H2 "AI assistant for real estate agents: common questions" + 6 `<details>` items, placed before testimonials. Text is identical to the `FAQPage` JSON-LD, so edit both together |
| Guides section (new) | no links to `/news` | "Guides for agents" with 3 links: `/news/real-estate-marketing/`, `/news/real-estate-marketing-plan/`, `/news/real-estate-lead-follow-up-automation-guide/` (all returned 200 when checked) |
| CSS | n/a | New `.faq-*` and `.guide-*` styles, using the existing design tokens |

### FAQ questions added
1. What is an AI assistant for real estate agents?
2. How does Real Sale X work?
3. Does the AI assistant replace the agent?
4. Does it make up answers?
5. Do I need a CRM or a long setup?
6. Do buyers need to log in?

Answers use only claims already on the page (MLS, disclosures, inspection report, public records, sources shown, no CRM, no login). No pricing, ratings or numbers were added.

## 2. How it was checked
- Rendered in Chromium at 1366px and 390px: no JS errors, no horizontal scroll, hero headline fits on both.
- All four JSON-LD blocks parse; the page has exactly one `<h1>`.
- The FAQ opens and closes; the guide cards display as a 3-column grid on desktop and 1 column on mobile.

## 3. Review checklist
- [ ] Confirm the title and meta description wording.
- [ ] Confirm the H1 wording. It is long (about 5 lines on desktop); shorten it if the design team prefers.
- [ ] Check the FAQ answers against what the product really does, especially "no login" and "no CRM".
- [ ] Replace `og:image` (currently `hero-boss-gen.webp`, not 1200x630) with a dedicated share image.
- [ ] Confirm that hreflang `vi` -> `/vn` is correct.

## 4. Still open (not done)
1. **Live site:** the server still returns an empty 1.8 KB shell, and title, meta and OG are injected by JS. Apply the tags above in the React codebase and prerender or SSR `/` and `/vn`.
2. **Soft 404s:** unknown paths and missing assets (for example `realsalex-tvc-poster.webp`) return 200 with the shell. They should return 404. Same for `/sitemap_index.xml` and `/llms.txt` if they are not used.
3. **Redirect:** `http://infina.ai` redirects to `https://infina.ai:443/`; it should go to `https://infina.ai/`.
4. **Sitemap:** no `lastmod`; some listed URLs (`/inside`, `/work`, `/personal`) serve the same empty shell.
5. **Footer:** `footer.js` has no Privacy or Terms links, and ignores the `links` attribute in this repo.
6. **Testimonials** (Dana Whitfield, Marcus Ellery, Priya Raman): the spec marks them TBD ("need real quote"). Not touched. Replace with real quotes or remove them before running ads.
7. **Naming:** the page still uses two product names ("Home Concierge" and "Property Expert"). Both are now framed as an "AI assistant"; unifying them means changing buttons, JS and demo pages.
8. **Performance:** compress the large webp images (about 200-370 KB each) and code-split the 3.7 MB JS bundle on the live app.
