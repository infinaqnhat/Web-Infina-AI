# Code Standards

Rules for editing this codebase. Optimized for a build-free static site with inline page styles.

## File Naming

- Use **kebab-case** for HTML and JS files: `focus-alignment.html`, `nav.js`, `footer.js`.
- Use **kebab-case** for image and asset filenames: `bidv-logo.png`, `travel-culture-sm.png`.
- Long, descriptive filenames are preferred over short cryptic ones — LLM tools (Grep, Glob) should be able to guess intent from the name.
- Avoid spaces in filenames. Existing `image (109).png` is a legacy exception — rename it next time it is touched.

## HTML

### Skeleton
Each page MUST follow this structure:
```html
<!DOCTYPE html>
<html lang="en">
<head>
  <base target="_top">
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>...</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Be+Vietnam+Pro:wght@400;500;600;700&display=swap" rel="stylesheet">
  <style>/* page-scoped CSS */</style>
</head>
<body>
  <infina-nav active="..."></infina-nav>
  <!-- content -->
  <infina-footer></infina-footer>
  <script src="nav.js"></script>
  <script src="footer.js"></script>
</body>
</html>
```

### Rules
- Set `<title>` and viewport on every page.
- `<infina-nav>` MUST include the `active` attribute (empty string on `home.html`).
- Always load both `nav.js` and `footer.js` at the end of `<body>`.
- Use semantic tags: `<section>`, `<header>`, `<h1>`...`<h3>`, `<nav>`, `<footer>`.
- Wrap brand/partner logos with `alt` text. Decorative imagery may use `alt=""`.

## CSS

### Where it lives
- **Page-scoped CSS** → inline `<style>` in the page's `<head>`. This is intentional — each page is shippable in isolation.
- **Shared component CSS (nav, footer)** → inside the Custom Element JS, appended to `document.head` once via a `<style id="infina-nav-styles">` (or footer equivalent) guard.
- Do NOT create a shared `*.css` file unless you are doing a deliberate cross-page refactor (see roadmap).

### Tokens (CSS Custom Properties)
All pages MUST keep the canonical token set in their `:root`:
```css
:root {
  --bg: #ffffff;
  --surface: #fafafa;
  --fg: #000000;
  --fg-secondary: #212121;
  --muted: #6b6b76;
  --border: #e5e7eb;
  --border-light: #f2f2f2;
  --accent: #001F5C;          /* brand navy */
  --accent-light: rgba(0, 31, 92, 0.08);
  --font-display: 'Be Vietnam Pro', -apple-system, system-ui, sans-serif;
  --font-body:    'Be Vietnam Pro', -apple-system, system-ui, sans-serif;
  --section-gap:  clamp(48px, 6vw, 72px);
  --radius:       22px;
}
```
If you add a token, add it everywhere — drift kills the brand.

### Layout
- Container max width: `1200px`, padding `0 32px` (desktop), `0 16px` (mobile breakpoint).
- Section vertical rhythm: use `var(--section-gap)` between major sections.
- Buttons / pill CTAs: `border-radius: 9999px`, `padding: 11px 22px`, navy background, white text, `transform: translateY(-2px)` and shadow on hover.
- Mobile breakpoint: `@media (max-width: 768px)` for nav, `@media (max-width: 640px)` for footer.

### Naming
- Inline CSS uses descriptive class names: `.nav-inner`, `.nav-dropdown-menu`, `.footer-copy`. No BEM is enforced, but be consistent within a page.
- Reserve `infina-` prefix for Custom-Element-owned classes (`nav.infina-nav`, `footer.infina-footer`).

## JavaScript (Custom Elements)

- Use IIFE-wrapped Custom Element definitions (see `nav.js` / `footer.js`).
- Always `if (customElements.get('infina-...')) return;` guard at module top to allow double-includes.
- Inject styles via a `<style id="infina-...-styles">` element with an `if (!document.getElementById(...))` guard — prevents duplicate stylesheets when components mount multiple times.
- Render the real DOM element next to the host (`this.parentNode.insertBefore(...)`), then `this.remove()` so the custom tag does not pollute the DOM tree.
- Use vanilla DOM APIs only — no jQuery, no framework, no bundler.
- Keep the file under 200 lines. If a Custom Element needs more, split helpers into a separate kebab-case `*.js` companion module and include both scripts on every page.
- Use single-line CSS strings in arrays joined with `'\n'` (current convention) — readable and concatenation-safe.

### Event Handling
- Always clean up listeners that escape page scope (e.g., `document` and `window` listeners) when state demands it. For the nav, the global handlers are intentional and live for the lifetime of the page.
- Use `aria-expanded`, `aria-hidden`, `aria-label` for any interactive control that toggles a panel.

## Accessibility

- All interactive elements MUST be reachable by keyboard.
- `aria-label` on icon-only buttons (e.g., the hamburger toggle has `aria-label="Menu"`).
- Use `alt` on logos (`alt="Infina AI"`). Brand partner logos should use their canonical brand name.
- Maintain contrast ≥ WCAG AA against the navy accent.
- Animations should respect `prefers-reduced-motion` if introduced.

## Comments

- Default: write **no comments**. The HTML and the descriptive class names should be self-explanatory.
- Add a comment only when the WHY is non-obvious: a hidden constraint (e.g., `<base target="_top">` for iframe escapes), a workaround, or a layout invariant.
- Do NOT reference plan files, finding codes, or audit labels inside source files.

## Git Commits

- Conventional commits: `feat:`, `fix:`, `refactor:`, `style:`, `perf:`, `test:`, `build:`, `revert:`.
- **Do not** use `chore:` or `docs:` for `.claude/` directory changes.
- Keep messages focused on actual code/content changes. No AI references.
- Examples from history: `Fix right column jump and lock chat body height on tab switch`, `Reduce white space gap between hero and coworkers section in work.html`.

## Things to Avoid

- ❌ Adding a build step or framework without a migration plan (see roadmap).
- ❌ Inline event handlers (`onclick="..."`) — there is one in `nav.js` (`onclick="location.href=..."`) that is acceptable for the dropdown chrome; do not propagate the pattern.
- ❌ Loading external scripts at runtime (analytics, chat widgets) without explicit approval.
- ❌ Committing files with secrets or credentials. None exist today — keep it that way.
- ❌ Renaming HTML files without grepping for every internal link (`nav.js`, `footer.js`, intra-page anchors, and other pages).

## When to Modularize

The HTML pages already exceed 200 lines because they embed all CSS. That is acceptable for now per the no-build constraint. Modularize when:
- A snippet of inline CSS is copy-pasted across **three or more** pages → lift to a shared style block (introduced as a new `<style>` in `nav.js`/`footer.js` or as a new shared JS module that injects styles).
- A page-specific JS interaction (e.g., the `personal.html` chat demo, the `work.html` video toggle) grows past ~40 lines → extract to a kebab-case `<page>-<feature>.js` file in the repo root and include it on the page that uses it.

## Browser Targets

- Latest two versions of Chrome, Safari, Edge, Firefox.
- Mobile Safari iOS 15+, Chrome Android 100+.
- Custom Elements v1 and `backdrop-filter` are required; both have universal support in those targets.
