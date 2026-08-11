// Pure parsing helpers for the UI-spec extractor.
// No file I/O here — takes HTML strings / parsed nodes, returns plain data.
// Coupled to the marketing pages' conventions: a `:root {}` token block and
// top-level <section class id> blocks with headings + CTAs.

const MAX_TEXT = 200; // cap extracted copy so specs stay skimmable & diffs small

/** Collapse whitespace, strip zero-width chars, trim, and cap length. */
export function cleanText(raw) {
  if (!raw) return '';
  const t = raw.replace(/\s+/g, ' ').replace(/​/g, '').trim();
  return t.length > MAX_TEXT ? t.slice(0, MAX_TEXT - 1).trimEnd() + '…' : t;
}

/**
 * Parse the FIRST `:root { ... }` block's custom properties from raw HTML.
 * Returns ordered [{ name, value }] in document order (stable diffs).
 */
export function parseRootTokens(html) {
  // First :root block that actually declares a custom property — skips an empty
  // or reset `:root {}` that may sit above the real token block.
  const tokens = [];
  const blockRe = /:root\s*\{([\s\S]*?)\}/g;
  let block;
  while ((block = blockRe.exec(html)) !== null) {
    // Tolerate a missing final `;` before `}` (value runs to `;` or end-of-block).
    const re = /(--[\w-]+)\s*:\s*([^;}]+)(?:;|$)/g;
    let m;
    while ((m = re.exec(block[1])) !== null) {
      tokens.push({ name: m[1].trim(), value: cleanText(m[2]) });
    }
    if (tokens.length) break; // found the real token block
  }
  return tokens;
}

/** True if `el` has any ancestor <section> (i.e. it is a nested section). */
function hasSectionAncestor(el) {
  let p = el.parentNode;
  while (p) {
    if (p.rawTagName && p.rawTagName.toLowerCase() === 'section') return true;
    p = p.parentNode;
  }
  return false;
}

/** First heading (h1→h3) text inside a section, flattened. */
function firstHeading(section) {
  const h = section.querySelector('h1, h2, h3');
  return h ? cleanText(h.structuredText || h.textContent) : '';
}

/**
 * Primary CTA text: prefer a cta-classed anchor/button, else first anchor
 * that isn't a bare in-copy link. Returns '' when nothing button-like found.
 */
function primaryCta(section) {
  const cta =
    section.querySelector('a[class*="cta"], button[class*="cta"], .btn, [class*="button"]');
  if (cta) return cleanText(cta.structuredText || cta.textContent);
  return '';
}

/** Collect asset references: <img src>, and url(...) / assets|uploads paths in markup. */
function collectAssets(section) {
  const found = new Set();
  for (const img of section.querySelectorAll('img[src]')) {
    found.add(img.getAttribute('src'));
  }
  const html = section.innerHTML || '';
  const urlRe = /url\(\s*['"]?([^'")]+)['"]?\s*\)/g;
  let m;
  while ((m = urlRe.exec(html)) !== null) found.add(m[1]);
  const pathRe = /(?:assets|uploads)\/[^\s'")]+/g;
  while ((m = pathRe.exec(html)) !== null) found.add(m[0]);
  return [...found].filter(Boolean);
}

/**
 * Ordered inventory of TOP-LEVEL sections (nested sections excluded).
 * Each entry: { index, class, id, heading, cta, assets[] }.
 */
export function parseSections(root) {
  const all = root.querySelectorAll('section');
  const top = all.filter((s) => !hasSectionAncestor(s));
  return top.map((s, i) => ({
    index: i + 1,
    class: s.getAttribute('class') || '',
    id: s.getAttribute('id') || '',
    heading: firstHeading(s),
    cta: primaryCta(s),
    assets: collectAssets(s),
  }));
}
