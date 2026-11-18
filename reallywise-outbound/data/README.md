# data/ (git-ignored)

Files here are **not committed** because they contain personal data of other people
(names and mailing addresses of California real estate licensees, raw crawl results).

To recreate the DRE new-licensees CSV (free, public file, no emails inside):

```bash
pip install xlrd
python3 -I scripts/dre_new_licensees_to_csv.py data/dre_new_licensees.csv
```

DRE updates the source file every Monday. Its own notice says addresses are "provided for reference only and
are not intended for mass mailing purposes", so get legal sign-off before using it for outreach.
