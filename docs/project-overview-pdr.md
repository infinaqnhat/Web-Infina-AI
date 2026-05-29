# Project Overview — Product Development Requirements (PDR)

## 1. Product Summary

**Infina AI** marketing website. A six-page static site that positions Infina as a Vietnam-built AI specialist platform with three product lines:

1. **AI Work** — specialist agents inside the company (Focus & Alignment, CRM/Sales, Expense, Knowledge Base, Custom Workflow).
2. **AI Inside** — embeddable AI specialists for partner products (mobile SDK, white-label, regulation-compliant).
3. **AI Personal** — consumer-facing AI specialists across Finance, Insurance, Wealth, Lifestyle.

The site is the top-of-funnel surface. Its only conversion is **"Book a demo"** (anchor `#demo`).

## 2. Goals

- Communicate the "specialist agent" positioning quickly and visually.
- Differentiate between the three product lines without forcing the visitor to read.
- Establish credibility via brand logos (banks, insurers, retail) on `inside.html`.
- Funnel every page to a single CTA: **Book a demo**.

## 3. Non-Goals (Out of Scope)

- No authenticated areas, no dashboard, no in-product surface.
- No CMS, no headless backend, no API.
- No analytics, A/B testing, or marketing automation hooked in yet.
- No multilingual variants (English-only copy today).
- No e-commerce, payment, or pricing pages.

## 4. Target Audience

- **Enterprise buyers** in Vietnam (banks, securities firms, insurers, retail) — primary persona for `work.html` and `inside.html`.
- **Product / engineering leaders** evaluating embed-vs-build for AI features — `inside.html`.
- **End consumers** curious about Infina's app-facing specialists — `personal.html`.
- **Investors / partners** doing diligence — `about.html`.

## 5. Functional Requirements

| ID | Requirement | Status |
|----|-------------|--------|
| FR-1 | Six standalone HTML pages render without a build step | Done |
| FR-2 | Shared top nav across all pages with active-state highlight | Done (`nav.js`) |
| FR-3 | Shared footer with secondary navigation | Done (`footer.js`) |
| FR-4 | Mobile-responsive navigation with hamburger panel | Done |
| FR-5 | AI Work dropdown reveals sub-pages (Focus & Alignment) | Done |
| FR-6 | All pages route the visitor to `#demo` CTA | Done |
| FR-7 | Brand logo strip on `inside.html` showing partner credibility | Done |
| FR-8 | Deep-dive product page for Focus & Alignment | Done |
| FR-9 | Personal page tabs across Finance / Wealth / Insurance / Lifestyle | Done |
| FR-10 | Inline video toggle on selected Work sections | Done |

## 6. Non-Functional Requirements

- **Performance:** No JS framework, no bundling. Largest asset is `inside.html` at ~230 KB (inline styles + markup). Acceptable for marketing.
- **Accessibility:** Semantic headings, alt text on logos, `aria-expanded` on the mobile menu toggle. Color contrast meets WCAG AA against the navy accent.
- **Browser support:** Modern evergreen browsers. Custom Elements + `backdrop-filter` are required.
- **SEO:** `<title>` and viewport meta on every page. No structured data yet.
- **No tracking** by design — easy to swap in later.

## 7. Success Metrics (Aspirational)

- Demo-form submissions per visit (when wired).
- Time-on-page for `home.html` > 30s.
- Bounce rate on `inside.html` < 60%.
- Search visibility for Vietnamese fintech AI keywords.

## 8. Constraints

- **No build pipeline.** Any change must work by editing `*.html` / `nav.js` / `footer.js` and refreshing the browser.
- **Inline styles** are the norm — each page owns its visual language.
- **File-size budget** — keep individual code files reasonable; the HTML pages already trend large because they embed all CSS.
- **English only** for now; copy is the source of truth.

## 9. Risks

| Risk | Impact | Mitigation |
|------|--------|------------|
| Pages drift in look-and-feel (each has its own inline CSS) | Brand inconsistency | Codify tokens in `docs/design-guidelines.md`; lift to shared CSS file when stable |
| HTML pages exceed editor / LLM context windows (`inside.html` already > 6,700 lines) | Hard to edit safely | Split into partials when next major redesign hits |
| `#demo` CTA has no destination | Lost leads | Wire to a form or Calendly before launch |
| No analytics | Can't measure | Add a privacy-friendly analytics layer (Plausible / Umami) when needed |

## 10. Dependencies

- Google Fonts (Be Vietnam Pro).
- Brand logo images in `uploads/` — licensed for marketing use of named partners.
- Photography in `assets/` and `uploads/` — Infina-owned or licensed.

## 11. Open Questions

- Should pages be migrated to a static-site generator (Astro / 11ty) to avoid duplicating inline CSS across the six files? See roadmap.
- What is the production hosting target (Vercel / Netlify / Cloudflare Pages / GitHub Pages)? See `deployment-guide.md`.
- Is multilingual (Vietnamese) on the near-term roadmap?
