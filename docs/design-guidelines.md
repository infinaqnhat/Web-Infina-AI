# Design Guidelines

Brand and visual language for the Infina AI marketing site. Keep these tokens consistent across all pages.

## 1. Brand Palette

| Token | Hex | Use |
|-------|-----|-----|
| `--accent` | `#001F5C` | Brand navy — CTAs, active states, key headings, brand mark |
| Highlight gradient stop | `#1863DC` | Used in inline SVG gradients (hero illustrations) |
| `--accent-light` | `rgba(0, 31, 92, 0.08)` | Hover backgrounds, soft highlight panels, tag chips |
| `--bg` | `#ffffff` | Page background |
| `--surface` | `#fafafa` | Card / section surface |
| `--fg` | `#000000` | Primary text |
| `--fg-secondary` | `#212121` | Body text on light backgrounds |
| `--muted` | `#6b6b76` | Captions, footer copy, eyebrow text |
| `--border` | `#e5e7eb` | Cards, dividers |
| `--border-light` | `#f2f2f2` | Subtle separators (nav bottom border, mobile panel) |

White-on-navy is the canonical CTA pairing. Avoid using the navy as body text on light backgrounds (insufficient contrast for paragraph runs); reserve it for headings and pill buttons.

## 2. Typography

- **Family:** [Be Vietnam Pro](https://fonts.google.com/specimen/Be+Vietnam+Pro) (Google Fonts), weights `400 / 500 / 600 / 700`.
- **Fallback:** `-apple-system, system-ui, sans-serif`.
- **Tokens:** `--font-display` and `--font-body` resolve to the same family today; keep them separate so we can diverge later.

### Scale (rules of thumb from existing pages)
- Hero `<h1>`: ~`clamp(40px, 6vw, 72px)`, weight 700, tight tracking (`letter-spacing: -0.03em`).
- Section `<h2>`: ~`clamp(32px, 4vw, 48px)`, weight 600.
- Card / sub-section `<h3>`: ~`24–28px`, weight 600.
- Body: `16–17px`, weight 400–500, `--fg-secondary`.
- Eyebrow / label: `12–13px`, uppercase, weight 600, `--muted` or `--accent`.

Standardize new eyebrow labels to the style codified by commit `dacbf42` ("Standardize hero eyebrow style across all pages") — small caps, navy or muted.

## 3. Layout

- **Max content width:** `1200px`.
- **Horizontal padding:** `32px` on desktop, `16px` on mobile (≤ 768px).
- **Section rhythm:** `var(--section-gap)` = `clamp(48px, 6vw, 72px)` between major blocks.
- **Card radius:** `var(--radius)` = `22px`. Use `9999px` only for pill buttons / chips.
- **Grid columns:** prefer 2 / 3 / 4-up CSS Grid (`grid-template-columns: repeat(auto-fit, minmax(280px, 1fr))`). No flexbox-only multi-column layouts.

## 4. Components

### Pill CTA ("Book a demo")
```
padding: 11px 22px
border-radius: 9999px
background: var(--accent)
color: #fff
font-size: 14px
font-weight: 500
transition: all .3s
hover: translateY(-2px); box-shadow: 0 8px 20px rgba(0,0,0,.2)
```

### Top Navigation (`<infina-nav>`)
- Fixed top, height `72px`.
- Background `rgba(255,255,255,.9)` with `backdrop-filter: blur(20px)`.
- Bottom border `1px solid --border-light`.
- Link underline animation: `2px` navy bar grows from `0` to full width on hover/active.
- Dropdown menu: white card, `border-radius: 12px`, `box-shadow: 0 12px 40px rgba(0,0,0,.1)`, fades in on hover with a `4px` vertical lift.

### Footer (`<infina-footer>`)
- White surface, `48px` vertical padding.
- Top border `1px solid --border-light`.
- Logo (23px tall) on the left, link group center, copyright right.
- Collapses to vertical centered stack ≤ 640px.

### Mobile Nav Panel
- Slides down from `top: 72px`.
- Background `rgba(255,255,255,.98)` with `backdrop-filter: blur(20px)`.
- Link rows: `14px` vertical padding, `16px` text, `--fg-secondary`, divider lines via `--border-light`.
- Mobile CTA reuses the pill CTA color but stretches full-width.
- Locks background scroll via `body.nav-open { overflow: hidden; }`.

### Cards (product / agent tiles)
- White or `--surface` background.
- `border-radius: 22px`, `border: 1px solid --border`.
- `padding: 24–32px`.
- Hover: subtle `translateY(-4px)` and shadow lift; use only on interactive cards.

## 5. Imagery

- Brand logos in `uploads/` are rendered at small sizes; preserve their aspect ratio and crisp edges. Avoid stretching.
- Lifestyle imagery (`assets/travel-*.png`, `uploads/grocery-shopping.png`, `uploads/house-interior-clean.jpg`, `uploads/luxury-resort.png`) belongs on Personal and Inside pages and should be displayed at `border-radius: 22px`.
- The master logo (`uploads/infina-ai-logo-web-329e3857.png`) is the single source of truth for the brand mark. Reference it from `nav.js` and `footer.js`; do not embed alternative versions inline.

## 6. Motion

- Transitions default to `0.2–0.3s` ease.
- Hover lifts: `translateY(-2px to -4px)`.
- Mobile panel open: `0.25s ease` on `transform` + `opacity`.
- Future animations should respect `@media (prefers-reduced-motion: reduce)` — disable lifts and transitions in that branch.

## 7. Iconography

- Inline SVG only. No icon font.
- Stroke width `2.5`, `stroke-linecap: round`, `stroke-linejoin: round`.
- Use `currentColor` so icons inherit the parent text color (matches `nav.js` chevron + hamburger).

## 8. Voice & Copy Patterns

- Punchy, two-line headlines (e.g., "State your problem. Watch it get done.").
- Sentence case for headlines; Title Case is OK for nav items and section labels.
- Verbs over nouns ("Watch it get done" > "Easy task completion").
- Reuse "AI specialist" and "specialist agent" language consistently — it is the brand positioning.
- "Book a demo" is the canonical CTA label everywhere.

## 9. Accessibility Checklist

- All interactive elements reachable by keyboard (Tab, Shift+Tab).
- Focus styles visible — never `outline: none` without a replacement.
- `aria-expanded` / `aria-hidden` on the mobile panel toggle and panel.
- `aria-label` on icon-only controls.
- Alt text on every brand logo using the canonical brand name (`alt="BIDV"`, `alt="Prudential"`).
- Body copy ≥ 16px.
- Color is never the only signal — pair color with text/icon for state.

## 10. When to Break the Rules

Hero illustrations, demo widgets, and one-off marketing modules may break the grid/typography rules to land a visual idea. But they must:
- Still use the canonical palette and font.
- Pass keyboard navigation.
- Remain responsive down to 360px width.

## 11. Source of Truth

If this document and the inline page CSS disagree:
- Tokens (`:root`) — this document wins. Fix the page.
- Layout / motion specifics — the page wins; update this doc with the new rule.
