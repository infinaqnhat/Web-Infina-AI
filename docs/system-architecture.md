# System Architecture

## 1. One-Line Summary

A static, build-free, multi-page marketing site. Each HTML page is self-contained except for two shared Web Components (`<infina-nav>`, `<infina-footer>`) loaded at runtime from `nav.js` and `footer.js`.

## 2. Topology

```
┌───────────────────────────────────────────────────────────────────────┐
│                      Visitor Browser (evergreen)                      │
│                                                                       │
│   ┌──── any *.html page ────────────────────────────────────────┐     │
│   │   inline <style> (page-scoped CSS, design tokens)           │     │
│   │   <body>                                                    │     │
│   │     <infina-nav active="..."></infina-nav>  ◄── nav.js      │     │
│   │       └── injects <style id="infina-nav-styles"> once       │     │
│   │       └── injects rendered <nav class="infina-nav">         │     │
│   │       └── self-removes host element                         │     │
│   │     <!-- page content sections -->                          │     │
│   │     <infina-footer></infina-footer>         ◄── footer.js   │     │
│   │       └── injects <style id="infina-footer-styles"> once    │     │
│   │       └── injects rendered <footer class="infina-footer">   │     │
│   │       └── self-removes host element                         │     │
│   │   <script src="nav.js">                                     │     │
│   │   <script src="footer.js">                                  │     │
│   └─────────────────────────────────────────────────────────────┘     │
│                                                                       │
│   External:                                                           │
│     • fonts.googleapis.com  (Be Vietnam Pro)                          │
│     • fonts.gstatic.com     (font binaries)                           │
└───────────────────────────────────────────────────────────────────────┘
              ▲
              │  HTTP (static file server / CDN)
              │
        ┌─────┴───────────────────────────────────────┐
        │  Static hosting (Vercel/Netlify/CF Pages)   │
        │  Serves: *.html, nav.js, footer.js,         │
        │          assets/*, uploads/*                │
        └─────────────────────────────────────────────┘
```

## 3. Component Inventory

### Pages (the routes)
| Page | URL intent | Active nav state |
|------|-----------|------------------|
| `home.html` | `/` | (none) |
| `work.html` | `/work` | `work` |
| `inside.html` | `/inside` | `inside` |
| `personal.html` | `/personal` | `personal` |
| `focus-alignment.html` | `/work/focus-alignment` | `focus-alignment` (lights up "AI Work") |
| `about.html` | `/about` | `about` |

### Shared Web Components
| Element | Module | Responsibility |
|---------|--------|----------------|
| `<infina-nav active="...">` | `nav.js` | Desktop + mobile navigation, active highlight, dropdown for AI Work, "Book a demo" CTA |
| `<infina-footer>` | `footer.js` | Brand logo, secondary nav links, copyright |

Both Custom Elements:
1. Self-register via `customElements.define(...)` guarded by `customElements.get(...)`.
2. Inject styles into `document.head` exactly once (id-guarded `<style>`).
3. Insert the real DOM next to the host node, then remove the host.
4. Are framework-free and stateless except for the mobile-panel open/closed flag on `<body>` (`body.nav-open`).

### Asset Buckets
- `assets/` — decorative lifestyle photography for Personal cards.
- `uploads/` — brand logos (banks, insurers, retail) + the master Infina logo + lifestyle photography used across Inside and Personal.

## 4. Rendering Lifecycle (per page load)

1. Browser fetches `*.html`.
2. Browser parses inline `<style>` and renders the page DOM, *including* the literal `<infina-nav>` / `<infina-footer>` placeholders (display: contents).
3. `<script src="nav.js">` and `<script src="footer.js">` load and execute synchronously at the end of `<body>`.
4. Each Custom Element's `connectedCallback`:
   - Injects its `<style>` block into `<head>` (one-time, id-guarded).
   - Builds the real `<nav>` / `<footer>` DOM node.
   - `insertBefore(...)`s it adjacent to the host element.
   - Removes the host element from the DOM.
5. Nav wires global event listeners for mobile-panel close (Esc, outside click, resize).
6. Page becomes interactive. No further script runs unless the visitor triggers a hover/click.

## 5. Data Flow

There is no application state, no network requests at runtime beyond Google Fonts, no API calls, no analytics, no cookies, no local storage.

```
visitor click on link → browser navigates to new HTML page → full reload → repeat lifecycle
```

The `#demo` anchor is the only conversion edge. Today it scrolls in-page (anchor only); the production destination must be wired (Calendly, HubSpot form, in-house form) — see `project-roadmap.md`.

## 6. Cross-Cutting Concerns

### Design Tokens
All pages declare the same `:root` custom-property set (brand color `#001F5C`, Be Vietnam Pro, radius 22px, section gap clamp(48px, 6vw, 72px)). The shared nav/footer rely on those tokens via `var(--accent, #001F5C)` fallbacks so they degrade gracefully even when embedded in pages that lack the tokens.

### Active Navigation Highlight
`<infina-nav>` reads its `active` attribute on connection:
- `inside` / `work` / `personal` / `focus-alignment` / `about` → highlights the corresponding top-level item.
- `focus-alignment` is treated as a member of the "AI Work" group; the dropdown toggle stays highlighted plus the submenu item gains the `active` class.
- `home.html` passes `active=""` — nothing highlights.

### Responsive Behavior
- Desktop ≥ 769px: full horizontal nav, hover-to-open AI Work dropdown.
- Mobile ≤ 768px: hamburger button reveals a slide-down panel; opening it toggles `body.nav-open` to lock background scroll.
- Footer collapses to vertical stack ≤ 640px.

## 7. Failure Modes & Resilience

| Failure | Effect | Mitigation |
|---------|--------|------------|
| `nav.js` fails to load | Pages render without a top nav, but content is intact (host `<infina-nav>` collapses via `display: contents`) | Keep `nav.js` versioned with the site; consider inlining the script if hosting reliability becomes an issue |
| `footer.js` fails to load | Footer missing; content unaffected | Same |
| Google Fonts unavailable | Falls back to `-apple-system, system-ui` | Already handled in the CSS variable |
| User has JS disabled | Site renders without nav/footer; page content (which is pure HTML+CSS) is fully usable | Acceptable for a marketing site |
| Custom Elements unsupported (legacy browser) | Site loses nav/footer | Out of scope (modern browsers only) |

## 8. Sequence: First Paint to Interactive

```
[t=0]  Browser receives HTML, starts parsing
[t=Δ1] Inline <style> parsed; layout begins
[t=Δ2] DOM tree complete (including <infina-nav>/<infina-footer> placeholders)
[t=Δ3] nav.js executes:
        - styles injected into <head>
        - <nav> built and inserted
        - <infina-nav> host removed
[t=Δ4] footer.js executes (same pattern)
[t=Δ5] Google Fonts arrive; font swap; layout reflow on text
[t=Δ6] Interactive — hover/click listeners armed
```

## 9. Notable Implementation Choices

- **Custom Elements over server includes / iframes** — keeps the project a flat directory of HTML pages while sharing chrome. No bundler required.
- **Inline page CSS over a shared stylesheet** — each page is fully shippable on its own (e.g., for partner microsite reuse), at the cost of style drift risk.
- **No router** — every nav link is a hard `<a href="*.html">` reload. Simpler, SEO-friendly, no client-side state to manage.
- **No analytics yet** — easy to layer in (Plausible / Umami) by appending a script tag to each page when needed.
- **Landing React = canonical, synced one-way to PFA** — the React port under `src/` is the source of truth for `infina-pfa-80389`'s landing; a minimal Vite harness verifies it locally and `scripts/sync-landing-to-pfa.sh` + a PFA CI drift check keep PFA read-only downstream. See `docs/landing-source-of-truth.md`.

## 10. Diagram Style Reminder

If future architecture diagrams are added to this doc, follow `/ck:tech-graph` `references/svg-layout-best-practices.md` (component spacing, arrow routing, label placement, z-index ordering). Pair with `/ck:preview --diagram` for visual self-review.
