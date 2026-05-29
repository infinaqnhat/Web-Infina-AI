# Codebase Summary

A flat, build-free static marketing site. Six HTML pages plus two shared JS Custom Elements (nav + footer). All page-specific CSS lives inline in each HTML file's `<head><style>` block.

## Directory Map

```
.
├── home.html                  Marketing homepage — three product lines pitch
├── work.html                  AI Work — agents for company functions
├── inside.html                AI Inside — embeddable specialists for partners
├── personal.html              AI Personal — consumer AI specialists
├── focus-alignment.html       Deep-dive: Focus & Alignment agent
├── about.html                 Company story, timeline, differentiators
├── nav.js                     <infina-nav> Web Component (shared top nav)
├── footer.js                  <infina-footer> Web Component (shared footer)
├── assets/                    Lifestyle imagery (travel-*.png)
├── uploads/                   Brand logos + photography
├── docs/                      Project documentation
├── plans/                     Implementation plans & reports
├── release-manifest.json      Asset/release inventory (large; tooling-generated)
├── .gitignore                 Standard ignore rules
└── .repomixignore             Repomix packing rules
```

## File Sizes (LOC)

| File | Lines | Note |
|------|------:|------|
| `inside.html` | 6,753 | Largest. All inline CSS + extensive sections |
| `home.html` | 5,980 | Inline CSS heavy |
| `about.html` | 1,415 | |
| `work.html` | 2,272 | |
| `personal.html` | 2,112 | |
| `focus-alignment.html` | 718 | Smallest content page |
| `nav.js` | 164 | Shared Web Component |
| `footer.js` | 50 | Shared Web Component |

## Module Notes

### `nav.js` — `<infina-nav>` Custom Element

- Defines a Web Component named `infina-nav`.
- Reads an `active` attribute (`inside`, `work`, `personal`, `focus-alignment`, `about`) to highlight the current section.
- Injects a `<style>` block (id `infina-nav-styles`) into `document.head` exactly once.
- Builds a desktop nav with logo, three top-level links, an "AI Work" dropdown that hovers to expose `focus-alignment.html`, and a "Book a demo" CTA pointing at `#demo`.
- Builds a mobile hamburger panel that mirrors the desktop links and adds a CTA-styled mobile button.
- Wires `Escape`, outside-click, and resize handlers to close the mobile panel.
- After mounting the rendered `<nav>` before itself, the host `<infina-nav>` removes itself from the DOM.

### `footer.js` — `<infina-footer>` Custom Element

- Defines `infina-footer`.
- Injects its own `<style>` (id `infina-footer-styles`) once.
- Renders the Infina AI logo, four secondary links (Inside / Work / Personal / About), and the © line.
- Removes the host element after mount.

### Page Files (`*.html`)

Every page follows the same skeleton:

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>...</title>
  <!-- preconnect to Google Fonts; Be Vietnam Pro -->
  <style>:root { --bg/-fg/--accent/... } /* large inline stylesheet */</style>
</head>
<body>
  <infina-nav active="..."></infina-nav>
  <!-- page sections -->
  <infina-footer></infina-footer>
  <script src="nav.js"></script>
  <script src="footer.js"></script>
</body>
</html>
```

Differences per page are content + section-specific CSS only.

### `home.html`
Sections (selection of `<h2>`): "State your problem. Watch it get done.", "Precision built for your exact need", three product-line panels (Work / Inside / Personal), Specialist agent grid (Stock, Wealth Management, Personal Finance, Insurance), platform pillars (Agent Orchestration, Tools & Connectors, Knowledge & Data, Evaluation & Safety), final demo CTA.

### `work.html`
Eyebrow → hero → "Works inside your setup. Acts the moment you ask." → "AI Specialists for Every Company Function" grid (Focus & Alignment, Expense Management, Knowledge Base, Custom Workflow) → CRM/Sales pipeline deep dive → integration + multi-channel + automation + verticalization pillars → demo CTA. Inline video toggle on the Sales section.

### `inside.html`
Largest page. Embeddable AI specialists pitch. Sections include "AI in every screen", "Smarter with your data", "A fraction of in-house cost", "Fully white-labeled", "Regulation-compliant by design", four specialist tiles, mobile SDK integration story, testing/monitoring story (Single-Turn / Multi-Turn / Production Monitoring), data-handling section ("De-identified. Regulation-compliant. Zero PII."), demo CTA.

### `personal.html`
Tab-style category UI across Finance / Wealth / Insurance / Lifestyle. "Top AI Specialist Agents" carousel: Stock Analyst, Investment Advisor, Budget Planner, Market Analyst, Compare Insurance Plans, Travel Planner. "Popular Use Cases" grid. Chat-like demo panel ("Start a conversation with your specialist"). Demo CTA.

### `focus-alignment.html`
Single-product deep dive for the Focus & Alignment agent. Hero ("The AI chief of staff for teams under 50."), "Built for the whole team, not just the manager.", "Works with the tools your team already uses.", closing CTA ("Ready to get your team aligned?").

### `about.html`
"We Built the AI First. Then We Made It Available to You." Story timeline (web launch, mobile launch, AI Inside launch, securities firm intro, first embedded prod deployment). Differentiator grid (Proven in Production, Multi-Agent Architecture, Country-Specific Expertise, Fastest Path to Live AI). Demo CTA.

## Asset Inventory

### `assets/` — 5 lifestyle images
- `travel-culture-sm.png`, `travel-evening-sm.png`, `travel-food-sm.png`, `travel-place-sm.png`, `travel-weather-sm.png`

### `uploads/` — brand logos + photography
- Brand logos: `aia.png`, `baoviet.png`, `bidv-logo.png`, `hpg-logo.png`, `mbb-logo.png`, `mwg-logo.png`, `petrolimex.png`, `prudential.png`, `pvi-insurance.png`, `vcb-logo.png`, `vic-logo.png`
- Imagery: `grocery-shopping.png`, `house-interior-clean.jpg`, `luxury-resort.png`, `image (109).png`
- Master logo: `infina-ai-logo-web-329e3857.png` (referenced by both `nav.js` and `footer.js`)

## Cross-File Conventions

- All pages link the same two scripts at the end of `<body>`: `<script src="nav.js"></script>` and `<script src="footer.js"></script>`.
- The `active` attribute on `<infina-nav>` is empty on `home.html` (no highlight) and one of `inside | work | personal | focus-alignment | about` elsewhere.
- All `#demo` links target a future demo-booking destination — currently anchor-only.

## Landing React Source of Truth

This repo is also the **source of truth for the landing React bundle** synced
one-way into `infina-pfa-80389` (read-only downstream). A minimal Vite harness
(`package.json`, `vite.config.ts`, `tsconfig*`, `index.html`, `src/main.tsx`,
`src/App.tsx`) makes `src/components/landing-v2/**`, `src/pages/landing/**`, and
`src/styles/landing*.css` compile/render for verification. Sync via
`scripts/sync-landing-to-pfa.sh`; PFA CI guards drift.
See `docs/landing-source-of-truth.md` for the full contract.

## Things That Are NOT in This Repo

- No backend code, API specs, or database schemas.
- No tests for the HTML marketing pages.
- The HTML site itself has no bundler — it ships as flat `*.html` + `nav.js`/`footer.js`.
  (The Vite tooling that now exists is the landing-React verification harness only,
  not a build step for the HTML site.)
