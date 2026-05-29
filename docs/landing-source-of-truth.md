# Landing React — Source of Truth & One-Way Sync

**Web-Infina-AI is the source of truth for the landing React bundle.** It flows
**one-way** into `infina-pfa-80389` (the production runtime that builds/deploys
landing). PFA's landing dirs are **read-only downstream**.

## The canonical bundle (3 path-sets)

| Path | What |
|------|------|
| `src/components/landing-v2/**` | All landing React components |
| `src/pages/landing/**` | The 6 route pages + `LandingLayout` |
| `src/styles/landing*.css` | 7 global CSS files imported by the pages |

Assets: components reference **absolute** `/landing-html/uploads/<file>` (served
from PFA `public/landing-html/`). The Web harness mirrors `uploads/` there via
`scripts/setup-harness-assets.mjs` (`predev`/`prebuild`). Use absolute paths only.

## Workflow (steady state)

```
Marketing edits HTML (*.html)  →  dev hand-ports HTML → React in Web src/
   →  verify in Web harness (npm run dev / build / typecheck)
   →  scripts/sync-landing-to-pfa.sh <pfa-checkout>   (copies 3 path-sets + manifest)
   →  review PFA diff, commit on a branch, open PFA PR
   →  PFA CI "Landing Drift Check" must be green
```

- **Author landing only in Web.** Never hand-edit the bundle in PFA — the drift
  check will fail the PFA PR.
- The sync script **does not commit or push** — it leaves PFA changes for a human PR.
- HTML→React conversion stays manual (creative step). The harness only verifies it.

## Drift guard

`scripts/sync-landing-to-pfa.sh` writes `src/landing-sync-manifest.json` into PFA:
the Web source commit + a sha256 per path-set. PFA's CI job
(`.github/workflows/landing-drift-check.yml` → `scripts/check-landing-drift.sh`)
recomputes those hashes and fails if they don't match — catching accidental
PFA-side edits or an incomplete sync. Fix drift by editing in Web and re-syncing.

## Not in scope

- Automating HTML→React conversion (manual).
- Packaging landing as an npm module / monorepo (rejected — YAGNI).
- Retiring the HTML site.
