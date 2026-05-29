# Infina AI — Marketing Website

Static marketing site for **Infina AI** — specialist AI agents for companies, products, and individuals (Vietnam-focused fintech / wealth / insurance verticals).

Six standalone HTML pages share a single navigation bar and footer via two Web Component scripts. No build step, no framework, no bundler. Open any `*.html` in a browser and it works.

## Pages

| File | Route Intent | What It Sells |
|------|--------------|---------------|
| `home.html` | `/` | Umbrella story — three product lines (Work / Inside / Personal) |
| `work.html` | `/work` | **Infina AI Work** — specialist agents for company functions (CRM/Sales, Focus, Expense, KB, Custom) |
| `inside.html` | `/inside` | **Infina AI Inside** — embeddable AI specialists for partner products (SDK / white-label) |
| `personal.html` | `/personal` | **Infina AI Personal** — consumer-facing AI specialists for everyday decisions |
| `focus-alignment.html` | `/work/focus-alignment` | Deep-dive on the Focus & Alignment agent |
| `about.html` | `/about` | Company story, timeline, differentiators |

## Shared Modules

- `nav.js` — defines `<infina-nav active="...">` Web Component. Renders the fixed top bar, dropdown for AI Work sub-pages, and the mobile hamburger panel.
- `footer.js` — defines `<infina-footer>` Web Component. Renders the bottom strip with logo, secondary links, copyright.

Each page embeds the components by tag and includes the two scripts at the bottom of `<body>`. The `active` attribute on `<infina-nav>` highlights the current section.

## Assets

- `assets/` — illustrative travel imagery used by the Personal lifestyle cards.
- `uploads/` — brand logos (BIDV, MBB, VCB, Prudential, AIA, Bao Viet, PVI, MWG, HPG, VIC, Petrolimex) plus the master Infina AI logo and lifestyle photography used on Personal and Inside.

## Run Locally

Any static file server works. Easiest:

```bash
python3 -m http.server 8080
# then open http://localhost:8080/home.html
```

Or open `home.html` directly in a browser (Web Components load fine from `file://`).

## Project Docs

- `docs/project-overview-pdr.md` — Product Development Requirements
- `docs/codebase-summary.md` — Module-by-module summary
- `docs/code-standards.md` — Conventions for HTML/CSS/JS in this repo
- `docs/system-architecture.md` — Page composition, shared components, asset flow
- `docs/design-guidelines.md` — Brand tokens, typography, layout patterns
- `docs/deployment-guide.md` — How to ship
- `docs/project-roadmap.md` — Phase status and next milestones

## Repository Layout

```
.
├── home.html
├── work.html
├── inside.html
├── personal.html
├── focus-alignment.html
├── about.html
├── nav.js                  # shared top navigation Web Component
├── footer.js               # shared footer Web Component
├── assets/                 # decorative imagery
├── uploads/                # brand logos + photography
├── docs/                   # project documentation (this site)
└── plans/                  # implementation plans & reports
```

## Brand & Tech Snapshot

- **Brand color:** `#001F5C` (deep navy) with `#1863DC` highlight.
- **Type:** Be Vietnam Pro (Google Fonts), 400/500/600/700.
- **No build:** plain HTML + inline `<style>` + vanilla JS Custom Elements.
- **No analytics / no tracking** at the moment; static pages only.

## Conventions

- Page-level styles live inline in each HTML file's `<head><style>` block.
- Shared chrome (nav, footer) styles live inside the corresponding JS Custom Element.
- File and asset names use kebab-case.
- Commit messages follow conventional commits (`feat:`, `fix:`, `refactor:`, etc.) — no AI references.

See `docs/code-standards.md` for the full set of rules.
