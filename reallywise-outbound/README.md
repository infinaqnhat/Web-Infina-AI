# ReallyWise outbound email (listing agents, US)

Everything produced in one working session (2026-11-10 to 2026-11-18): email sequences, Brevo templates,
research, previews, the demo GIF and the scripts used to build them. Status: **drafts, nothing has been sent to anyone.**

- **Sender persona:** Eric, Growth Manager, ReallyWise (`Eric RWise <eric@reallywise.ai>`)
- **Audience:** US listing agents
- **Style:** personal plain-text-looking emails (see `previews/`), brand colors only as accents
- **Language:** email copy in English, planning docs in Vietnamese

## 1. What is in the box

```
reallywise-outbound/
  README.md                         this file
  docs/
    reallywise-outbound-sequence-summary.md      MASTER PLAN: all emails, schedule, open items (start here)
    reallywise-outbound-option-b-pay-per-closing.md   option B: 4 emails incl. pay-per-closing, fee research, legal risk
    outbound-email-best-practices.md             cold email research with sources and confidence labels
    realtor-email-crawl-summary.md               what was crawled for realtor emails, which Apify actors, results
    history/                                     earlier plan versions (v1 branded, v2, v3), kept for reference
  email-templates/
    option-a/   01-product-intro.html, 02-free-3-months.html, 03-close-the-loop.html, 01b-product-intro-with-listing.html
    option-b/   03-pay-per-closing.html
    archive/    older designs: branded-v1 (navy header + logo), branded-v2, personal-v3 (earlier copy direction)
  previews/     PNG renders of every template (sample data: "Alex", "1428 Maple Ave")
  assets/       demo GIF, two product screenshots, reversed logo
  scripts/      template generators, GIF/tour helpers, DRE CSV downloader
  data/         git-ignored on purpose (personal data), see data/README.md
  build/        git-ignored output of the generators
```

## 2. The sequences

**Option A, 3 emails (templates are on Brevo):**

| # | Day | Name | Goal | Media |
|---|---|---|---|---|
| 1 | 0 | Product intro | Eric introduces himself and Property Expert, sends the reader into the guided tour | Demo GIF linked to the tour |
| 2 | 3 | Incentive | Free first 3 months if they open an account by the end of Q1 2027 and try it | Agent dashboard screenshot linked to the app |
| 3 | 10 | Close the loop | Not a fit? Invite them to describe another need, interview and build around it | none |

Variant **1B** (not on Brevo): same as email 1 for agents whose newly listed home is known, with a per-listing
tour link. Needs two Brevo contact attributes (Text): `LISTING_STREET`, `TOUR_LINK`.

**Option B, 4 emails:** 1, 2, **pay-per-closing**, close the loop (days 0, 3, 8, 14). The new email offers
"7% of your listing-side commission, only when the listing closes, no cap" instead of a subscription.
**Do not send it before a lawyer has reviewed it** (RESPA Section 8 and state licensing rules, see option-b doc).

Suggested schedule: gaps of 3 then 7 days, land on weekdays, avoid Thanksgiving week (Thu 2026-11-26).

## 3. Brevo state (account "Infina GPT", sender id 2 = Eric RWise)

| Template ID | Name | Use |
|---|---|---|
| 1 | RW outbound 1 \| Product intro | Option A email 1 |
| 2 | RW outbound 2 \| Free for your first 3 months | Option A email 2 (and option B email 2) |
| 3 | RW outbound 3 \| Close the loop | Option A email 3 (option B email 4) |
| 15 | RW outbound B3 \| Pay per closing | Option B email 3 |
| 4, 10, 11 | old drafts | **unused, delete by hand** (the Brevo connector cannot delete) |

All are inactive HTML templates. Brevo automations cannot be created through the connector; build the
workflow in the Brevo UI (trigger: contact added to a list, waits as above, exit on reply/unsubscribe).
Brevo cannot detect replies, so remove contacts who reply from the list manually.

## 4. External links the emails depend on

| What | URL | Note |
|---|---|---|
| Guided tour (opens the 7-step tour via `#tour=1`, ends on the agent dashboard) | `https://infinaqnhat.github.io/Web-Infina-AI/property-expert-demo-tour.html?agent=dashboard#tour=1` | Served by GitHub Pages of the **old** repo |
| Create account / app | `https://reallywise-app.infina.dev` | Page is still branded INFINA AI |
| Demo GIF | `https://raw.githubusercontent.com/infinaqnhat/Web-Infina-AI/claude/epic-ride-msgpbj/reallywise/email/rw-demo-buyer.gif` | **Tied to a branch name of the old repo** |
| Dashboard / buyer screenshots | `https://infinaqnhat.github.io/Web-Infina-AI/reallywise/uploads/pp-pdf-agent.jpg` (and `pp-pdf-buyer.jpg`) | GitHub Pages of the old repo |

**After moving this folder to another repo**, those URLs keep pointing at the old repo. Host
`assets/rw-demo-buyer.gif` and the two screenshots somewhere stable (new repo's Pages/CDN or Brevo's media library),
then replace the URLs in `email-templates/**` and in Brevo templates 1 and 2 (and 1B). A quick way for the files:

```bash
grep -rl "raw.githubusercontent.com/infinaqnhat" email-templates | xargs sed -i 's#https://raw.githubusercontent.com/infinaqnhat/Web-Infina-AI/claude/epic-ride-msgpbj/reallywise/email/rw-demo-buyer.gif#NEW_GIF_URL#g'
```

Brevo HTML templates were saved from these files; after editing a file, paste the HTML into the Brevo template
(or ask Claude to update it through the connector). Keep the original GIF in the old repo until the emails are updated.

## 5. How to rebuild the templates

```bash
mkdir -p build/out build/preview
python3 -I scripts/build_templates/build4.py     # option A emails 1-3  -> build/out/
python3 -I scripts/build_templates/build1b.py    # variant 1B           -> build/out/
python3 -I scripts/build_templates/buildppc.py   # option B pay-per-closing -> build/out/
```

The outputs are byte-identical to `email-templates/option-a` and `option-b` (checked). Edit the copy in
`build4.py` / `build1b.py` / `buildppc.py`, rerun, then update Brevo. `scripts/record_demo_frames.js` (Playwright) records
the demo, `scripts/make_demo_gif.py` assembles the GIF, `scripts/check_tour_url.js` and `check_tour_end.js` verify that
`#tour=1` opens the tour and where it ends. They need Node + Playwright, and Python + Pillow.

## 6. Realtor email data: current status

See `docs/realtor-email-crawl-summary.md`. Short version: **no usable email list exists yet.** The only dataset is the
free DRE new-licensees file (names and addresses, no emails). A few small Apify test runs (Google Maps based
`get-leads/real-estate-agent-scraper`, `nexgendata/person-business-email-finder`, `j0401/ca-dre`) found no verified
emails for the target agents. Nothing was crawled from Facebook groups or Reddit. Apify used about $0.1 in total.

## 7. Open items before sending anything

1. Terms of "free first 3 months" (start, what happens after, card needed?), and confirm the account flow on `reallywise-app.infina.dev`.
2. Scope of "build around what you need" in email 3 (who runs the interviews).
3. Option B: lawyer review of commission sharing, then fix the fee basis, collection time and who pays.
4. Send a test of every email to yourself: check the tour opens through Brevo link tracking, and click **Reply** (templates 1 and 3 had no reply-to set).
5. Move the GIF/screenshots to stable hosting (section 4), delete unused Brevo templates (4, 10, 11), build the automation.
6. Get a real, compliant email source (list provenance, Brevo's anti-spam policy forbids scraped/purchased lists, CAN-SPAM footer already included).
7. SMS: do not send cold marketing SMS to phone numbers taken from listings (TCPA risk); see docs.

## 8. Security notes

- No API keys are stored in this folder. A Brevo API key was pasted into the Claude chat during the session: **revoke it in Brevo and re-enable IP blocking for API keys** if it was turned off.
- Apify access in the session came from an environment variable (`Apify_key`), never written to files.
- `data/` and raw crawl results stay out of git because they contain other people's personal data.

## 9. Moving this branch to another repo

Branch: `claude/epic-ride-msgpbj` (repo `infinaqnhat/Web-Infina-AI`). The folder is self-contained, so the cleanest way is to copy it:

```bash
# in the old repo, on this branch
cp -r reallywise-outbound /path/to/new-repo/
cd /path/to/new-repo && git add reallywise-outbound && git commit -m "Add ReallyWise outbound email package"
```

Alternatively, push the whole branch (this brings the old repo's history with it):

```bash
git remote add newrepo <NEW_REPO_URL>
git push newrepo claude/epic-ride-msgpbj
```

The old repo's branch also holds `reallywise/email/rw-demo-buyer.gif`, which the live emails currently link to (section 4).
