# Infina AI money page (https://infina.ai/): SEO changes for production

- **Target keyword:** AI assistant for real estate agents
- **Product name:** Infina AI (do not use "Real Sale X" in any visible text, tag or schema)
- **Reference implementation:** `realsalex-v2.html` on `main` (static HTML). The production page is the React app, so these changes have to be ported there. Everything below is copied from that file, so it can be pasted as is.
- **Do NOT change:** hero headings and hero sub-copy, testimonials, footer. These were reviewed and left as they are.

## 0. Read this first: the page must be readable without JavaScript

Right now the server sends the same 1.8 KB empty shell for every URL (`<title>Infina AI</title>`, an empty `<div id="root">`). Title, meta tags and all content appear only after JS runs. Tags added with Helmet/JS are not seen by many crawlers, link previews (Slack, Zalo, Facebook, LinkedIn) or AI search bots.

**Required:** `/` and `/vn` must return the title, meta tags, JSON-LD, the H1 and the FAQ text in the first HTML response. Options: build-time prerender (for example `vite-plugin-prerender` or `react-snap`) or SSR.

Check after deploy (must show the new values without running JS):
```
curl -s https://infina.ai/ | grep -E "<title>|rel=\"canonical\"|application/ld\+json|<h1"
curl -s -A "Googlebot" https://infina.ai/ | grep -c "common questions"   # must be 1 or more
```

## 1. Head tags for `/` (replace the current head tags of the page)

```html
<title>AI Assistant for Real Estate Agents | Infina AI</title>
<meta name="description" content="Infina AI is an AI assistant for real estate agents. Turn any listing into a 24/7 expert that answers buyer questions and shows you who is ready to act.">
<meta name="robots" content="index, follow, max-image-preview:large">
<link rel="canonical" href="https://infina.ai/">
<link rel="alternate" hreflang="en-US" href="https://infina.ai/">
<link rel="alternate" hreflang="vi" href="https://infina.ai/vn">
<link rel="alternate" hreflang="x-default" href="https://infina.ai/">
<meta property="og:type" content="website">
<meta property="og:site_name" content="Infina AI">
<meta property="og:locale" content="en_US">
<meta property="og:url" content="https://infina.ai/">
<meta property="og:title" content="AI Assistant for Real Estate Agents | Infina AI">
<meta property="og:description" content="Infina AI is an AI assistant for real estate agents. Turn any listing into a 24/7 expert that answers buyer questions and shows you who is ready to act.">
<meta property="og:image" content="https://infina.ai/landing-html/uploads/hero-boss-gen.webp">
<meta property="og:image:alt" content="Buyers holding the keys in front of their new home">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="AI Assistant for Real Estate Agents | Infina AI">
<meta name="twitter:description" content="Infina AI is an AI assistant for real estate agents. Turn any listing into a 24/7 expert that answers buyer questions and shows you who is ready to act.">
<meta name="twitter:image" content="https://infina.ai/landing-html/uploads/hero-boss-gen.webp">
```

Notes:
- Title is 47 characters, description is 152 characters. Do not make them longer.
- The page must have **one** canonical, one title and one description (remove duplicates from `index.html` or Helmet).
- `og:image` is a temporary image. Replace it with a dedicated 1200x630 share image when design has one.
- hreflang: `/vn` must carry the same three alternate tags, its own canonical `https://infina.ai/vn`, and its own Vietnamese title and description. Only keep the `vi` tag if `/vn` is a real Vietnamese version of the same page.
- Do not redirect crawlers by IP or by the `infina_region` cookie: `/` must always return the same page to Googlebot.

## 2. Structured data (JSON-LD)

Add four blocks in the head of `/` (`/vn` gets its own set in Vietnamese or none).

```html
<script type="application/ld+json">
{"@context":"https://schema.org","@type":"Organization","@id":"https://infina.ai/#org","name":"Infina AI","url":"https://infina.ai/","logo":"https://infina.ai/landing-html/uploads/infina-ai-logo-web.webp"}
</script>
<script type="application/ld+json">
{"@context":"https://schema.org","@type":"WebSite","@id":"https://infina.ai/#website","url":"https://infina.ai/","name":"Infina AI","publisher":{"@id":"https://infina.ai/#org"},"inLanguage":"en-US"}
</script>
<script type="application/ld+json">
{"@context":"https://schema.org","@type":"SoftwareApplication","@id":"https://infina.ai/#software","name":"Infina AI","alternateName":"Infina AI assistant for real estate agents","description":"Infina AI is an AI assistant for real estate agents. Turn any listing into a 24/7 expert that answers buyer questions and shows you who is ready to act.","url":"https://infina.ai/","applicationCategory":"BusinessApplication","operatingSystem":"Web","audience":{"@type":"Audience","audienceType":"Real estate agents"},"publisher":{"@id":"https://infina.ai/#org"}}
</script>
<script type="application/ld+json">
{"@context":"https://schema.org","@type":"FAQPage","mainEntity":[
{"@type":"Question","name":"What is an AI assistant for real estate agents?","acceptedAnswer":{"@type":"Answer","text":"It is software that answers buyers' questions about a listing at any hour, using the listing's own data such as the MLS record, seller disclosure, inspection report and public records. Infina AI is built so the agent stays at the center of the relationship: it answers the routine questions and tells you when a buyer is ready for a conversation."}},
{"@type":"Question","name":"How does Infina AI work?","acceptedAnswer":{"@type":"Answer","text":"Paste a link to your listing and Infina AI creates a private page with an AI Property Expert for that home. Buyers open it from a link or a QR code on a yard sign or brochure, ask questions, and get answers that show their sources. You see what they asked and where your attention can help."}},
{"@type":"Question","name":"Does the AI assistant replace the agent?","acceptedAnswer":{"@type":"Answer","text":"No. Property Expert does not replace you, it extends you. The agent sees every question and can join the conversation at any point."}},
{"@type":"Question","name":"Does it make up answers?","acceptedAnswer":{"@type":"Answer","text":"It is grounded in your listing data and shows the source for each answer. If the answer is not in the data, it says so."}},
{"@type":"Question","name":"Do I need a CRM or a long setup?","acceptedAnswer":{"@type":"Answer","text":"No. There is no CRM connection and no complicated setup. You can start with one listing and create your first advisor in under a minute."}},
{"@type":"Question","name":"Do buyers need to log in?","acceptedAnswer":{"@type":"Answer","text":"No. Buyers get answers instantly with no login, and every buyer gets a private conversation."}}
]}
</script>
```

Rules:
- No price, rating or review fields: none of these exist on the page, and invented values can cause a manual action.
- The FAQPage text must match the visible FAQ on the page (section 3) word for word. If one changes, change both.
- Organization: confirm the official company name and add `sameAs` with the real social profile URLs if wanted.
- Validate in Google's Rich Results Test and the Schema Markup Validator after deploy.

## 3. FAQ block (visible on the page)

- **Placement:** after the "Turn curiosity into intent" section and before the testimonials, `id="faq"`.
- **H2:** AI assistant for real estate agents: common questions (the words "common questions" use the existing accent style).
- **Behavior:** native `<details>`/`<summary>`, closed by default. The answer text must be in the HTML (not loaded after a click), so crawlers can read it.

| # | Question | Answer |
|---|---|---|
| 1 | What is an AI assistant for real estate agents? | It is software that answers buyers' questions about a listing at any hour, using the listing's own data such as the MLS record, seller disclosure, inspection report and public records. Infina AI is built so the agent stays at the center of the relationship: it answers the routine questions and tells you when a buyer is ready for a conversation. |
| 2 | How does Infina AI work? | Paste a link to your listing and Infina AI creates a private page with an AI Property Expert for that home. Buyers open it from a link or a QR code on a yard sign or brochure, ask questions, and get answers that show their sources. You see what they asked and where your attention can help. |
| 3 | Does the AI assistant replace the agent? | No. Property Expert does not replace you, it extends you. The agent sees every question and can join the conversation at any point. |
| 4 | Does it make up answers? | It is grounded in your listing data and shows the source for each answer. If the answer is not in the data, it says so. |
| 5 | Do I need a CRM or a long setup? | No. There is no CRM connection and no complicated setup. You can start with one listing and create your first advisor in under a minute. |
| 6 | Do buyers need to log in? | No. Buyers get answers instantly with no login, and every buyer gets a private conversation. |

HTML (one item shown, repeat for the six):
```html
<section class="section faq-section" id="faq">
  <div class="container">
    <div class="section-head reveal">
      <h2>AI assistant for real estate agents: <span class="accent">common questions</span></h2>
    </div>
    <div class="faq-list">
      <details class="faq-item">
        <summary>What is an AI assistant for real estate agents?</summary>
        <p>It is software that answers buyers' questions ...</p>
      </details>
      <!-- ...5 more -->
    </div>
  </div>
</section>
```

CSS (uses the page's existing variables; adapt to the Tailwind/CSS setup of the app):
```css
.faq-list { max-width:780px; margin:0 auto; display:flex; flex-direction:column; gap:12px; }
.faq-item { border:1.5px solid var(--border); border-radius:16px; background:var(--bg); }
.faq-item summary { cursor:pointer; list-style:none; padding:18px 22px; font-size:17px; font-weight:700; color:var(--accent); display:flex; justify-content:space-between; align-items:center; gap:16px; }
.faq-item summary::-webkit-details-marker { display:none; }
.faq-item summary::after { content:"+"; font-size:22px; font-weight:600; color:var(--muted); flex-shrink:0; }
.faq-item[open] summary::after { content:"\2212"; }
.faq-item p { padding:0 22px 20px; font-size:16px; color:var(--fg-secondary); line-height:1.7; }
```
For `/vn`: the FAQ needs a Vietnamese translation (visible text and JSON-LD together), or leave it out of `/vn`.

## 4. Smaller on-page changes

| # | Where | Current | Change to |
|---|---|---|---|
| 1 | Heading in the "For Buyer Agent" hero slide | `<h1>` "Don't just send a listing. Send a Concierge." | Same words, tag changed to `<h2>`. The page must have exactly **one** `<h1>`: the Listing Agent hero ("Turn every brochure and yard sign into a 24/7 Property Expert."), which is the slide shown by default |
| 2 | Style of that heading | n/a | If the app has a generic rule such as `h2 .accent` (gradient text), override it for the hero so the word "Concierge." keeps the light-blue hero color `#9cc2ff`: `background:none; -webkit-text-fill-color:#9cc2ff; animation:none;`. Without this the word turns dark navy and is hard to read |
| 3 | Label above the video | See how it works | See how the AI assistant works |
| 4 | Last line of the final CTA (Buyer tab) | Give them an advisor they can talk to. | Give them an AI assistant they can talk to. |
| 5 | Alt text, Listing hero image (`hero-listing-new`) | A For Sale yard sign with a QR code sticker in front of a home | A For Sale yard sign with a QR code that opens an AI assistant for the listing |
| 6 | Alt text, Buyer hero image (`hero-boss-gen`) | A happy couple holding keys in front of their new home | Buyers holding the keys in front of their new home |
| 7 | Alt text, video poster (`realsalex-tvc-poster`) | Real Sale X, watch the film | Infina AI, the AI assistant for real estate agents: watch the film |
| 8 | Play button `aria-label` and fallback link text | "Play the Real Sale X film" / "Watch the Real Sale X film" | "Play the Infina AI film" / "Watch the Infina AI film" |

## 5. Technical items for the server and app (priority order)

| # | Priority | Item | Current | What to do |
|---|---|---|---|---|
| 1 | P0 | Prerender / SSR | Empty shell for every URL | See section 0 |
| 2 | P0 | Soft 404 | Unknown paths and missing files return `200` with the shell. Examples: `/this-page-does-not-exist`, `/sitemap_index.xml`, `/llms.txt`, `/landing-html/uploads/realsalex-tvc-poster.webp` | Return a real `404` for paths that are not routes and files that do not exist. Remove them or create real files |
| 3 | P0 | Redirect | `http://infina.ai` goes to `https://infina.ai:443/` | Redirect to `https://infina.ai/` (no port). Same for `www` |
| 4 | P1 | Video poster | The poster URL returns an HTML page, not an image | Fix the path or upload the file; the code expects `uploads/realsalex-tvc-poster.jpg` (check the production path and extension) |
| 5 | P2 | Sitemap | 7 URLs, no `lastmod`. `/inside`, `/work`, `/personal` return the same empty shell | Add `lastmod`, keep only URLs that have their own content, and add the `/news` sitemap (`https://infina.ai/news/wp-sitemap.xml`) |
| 6 | P2 | Images | webp files about 200-370 KB, most without `width`/`height` | Compress to about 120 KB or less, add `width` and `height`, preload only the hero image |
| 7 | P2 | JS bundle | One 3.7 MB bundle (`index-*.js`) | Code-split the app and deal-room parts so the landing page loads less |

## 6. Acceptance checklist (for the dev to tick)

- [ ] `curl https://infina.ai/` shows the new `<title>`, meta description, canonical, hreflang, OG and the four JSON-LD blocks in the raw HTML.
- [ ] Raw HTML contains exactly one `<h1>`, and the FAQ questions and answers are in the HTML.
- [ ] `curl -I https://infina.ai/xyz-not-real` returns `404`.
- [ ] `http://infina.ai/` redirects once to `https://infina.ai/`.
- [ ] Rich Results Test shows `FAQPage` and `SoftwareApplication` as valid with no errors.
- [ ] Hero "Concierge." is light blue (not dark navy) on the Buyer slide, on desktop and mobile.
- [ ] Search the page source for "Real Sale X": no results.
- [ ] Request indexing for `https://infina.ai/` in Google Search Console after deploy.
