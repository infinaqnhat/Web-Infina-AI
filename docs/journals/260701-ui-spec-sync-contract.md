# Living UI/UX Spec with Extractor — Sync Contract Shipping

**Date**: 2026-07-01 15:00  
**Severity**: Medium (design decision + data flow)  
**Component**: `scripts/extract-ui-spec.mjs`, `docs/ui-spec/`, spec regenerator  
**Status**: Shipped (commit 9493c0d); follow-up deferred  

## What Happened

Built a living spec system so this static HTML marketing site (source of truth) stays in sync with production Nx app (`apps/infina-ai`). When marketing edits HTML, `npm run spec` regenerates canonical specs. Nx team reads mapping, edits components. Shipped 7 page specs + 3 extraction scripts.

## The Brutal Truth

This felt high-stakes because it's a sync boundary — if the marker-splice invariant breaks, Nx team ships outdated UI. Code review caught a latent bug that would've silently corrupted specs in production, turning what felt like a "solved problem" into a live mine.

## Technical Details

**C1 (Critical, latent)**: `String.replace(SPLICE_RE, zone)` treats `$` in HTML copy as replacement patterns. If a future price is "$50/mo", it replaces `$&` with the last matched substring, mangling the MANUAL zone. This breaks idempotency — next `npm run spec` would overwrite hand-written Nx mappings.

```javascript
// BAD (shipped initially)
auto.replace(SPLICE_RE, manualZone)  // $ in manualZone triggers replacement pattern

// FIXED
auto.replace(SPLICE_RE, () => manualZone)  // Replacer function ignores special chars
```

**H1/H2**: `spec:check` exited 0 when spec files or markers were missing — green while broken. CI gate was blind.

```javascript
// Now counts errors, exit(1) if any missing/stale markers
if (errors) process.exit(1)
```

**M1/M2**: Baseline CSS token parser was fragile — failed on empty `:root` or missing final `;`. Fixed to pick first NON-empty block + tolerate trailing semicolon.

## What We Tried

Marker-splice hybrid felt like the right invariant: AUTO zone (tokens, section inventory, headings/CTAs, assets — regenerated from HTML source), MANUAL zone (hand-written Nx component/route mapping + design intent). Generator rewrites only AUTO, leaving MANUAL untouched.

Works when the generator is correct. Code review exposed that "correct" required more care than initially assumed — string replacement is not safe for untrusted/dynamic content, even in the context of HTML.

## Root Cause Analysis

Didn't think through the threat model for `String.replace`. Assumed the replacement string was "safe" because it's internal HTML structure. Mistake: "internal" ≠ "immutable". Once you wire this to marketing copy, a single `$50/mo` price tag becomes a vector for accidental data loss.

Should have audited the spec format for any character sequences that could break replace semantics. The fact that this was caught in code review, not in test, meant no edge case was written first.

## Lessons Learned

1. **String.replace with dynamic content is a footgun.** Always use a replacer function when the replacement string isn't a literal. Even "safe looking" strings (HTML structure) break once they contain user data (prices, quotes, etc.). Cost: 10 chars. Value: saved a production bug.

2. **CI gates that exit 0 on empty data are silent failures.** `--check` should fail fast on missing markers — a green CI with stale specs is worse than a broken build. Needed explicit error counting.

3. **Idempotency isn't free.** The marker-splice design assumes the generator is idempotent. That's only true if the generation logic doesn't have subtle state dependencies (here: string replacement semantics). Every regen is a potential corruption vector.

4. **Fragile token parsing is a liability.** CSS baseline parser should tolerate missing semicolons and empty blocks — defensively assume the source HTML might be slightly malformed. Spec should not crash on borderline-valid input.

## Notable Findings (Not Bugs, Design Gaps)

Nx render diverges from HTML on 3 pages:
- `personal`: hero-only (Jobs/Usecases/CTA commented out; missing lead form entirely)
- `inside`: hides 3 sections dynamically
- `work`: hides Coworkers section

Flagged per-row in specs so sync agent won't wrongly re-add hidden sections. This revealed a gap: source of truth (HTML) has all sections, but production Nx selectively hides them. Spec mapping must capture that intent, otherwise sync is lossy.

`salesx` has a granularity mismatch: HTML = 5 top-level sections; Nx = 7 components (some Nx sections are nested divs in HTML). Mapping is 1:many. Spec notes this — Nx agent must be aware.

## Next Steps

**Open follow-up (YAGNI-deferred, not in scope)**

Pre-commit/CI hook running `npm run spec:check` to catch HTML edited without regenerating the spec. Would prevent: developer commits HTML + forgets spec regen, sync agent sees stale spec, ships outdated UI.

Currently: manual discipline. If we get a "oops we shipped the old UI" incident, prioritize this hook. For now: spec docs document the workflow; Nx sync process includes a review step that should catch stale specs.

## Verified

- Idempotent regen: `npm run spec` → `npm run spec` produces byte-identical output
- MANUAL-zone byte-preservation: hand-written Nx mappings survive generator rewrites
- C1 regression: `$50/mo` in copy stays intact, MANUAL zone untouched
- Exit codes: `--check` exits 1 on missing/stale, 0 on healthy specs

---

**Files Involved**
- `/scripts/extract-ui-spec.mjs` (Node ESM, node-html-parser, zero native deps)
- `/scripts/ui-spec-parse.mjs` (CSS token extraction)
- `/docs/ui-spec/README.md` (sync workflow, `Last synced to Nx` marker)
- `/docs/ui-spec/_tokens.md` (13-token baseline)
- `/docs/ui-spec/{home,work,inside,personal,about,focus-alignment,salesx}.md` (7 page specs)
