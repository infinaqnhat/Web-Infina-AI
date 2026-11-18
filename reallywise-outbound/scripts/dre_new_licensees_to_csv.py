"""Download DRE's free weekly new-licensees file and write a clean CSV.

Usage (from the reallywise-outbound folder):
    pip install xlrd
    python3 -I scripts/dre_new_licensees_to_csv.py data/dre_new_licensees.csv

Source: https://secure.dre.ca.gov/datafile/new_licensees.xls (updated by DRE every Monday).
The file has NO email addresses. It contains names and mailing addresses of licensees (many are
home addresses), so keep the output out of git (data/ is git-ignored) and check the DRE notice
that addresses are "not intended for mass mailing purposes" before using it.
"""
import csv, sys, tempfile, urllib.request
import xlrd

URL = "https://secure.dre.ca.gov/datafile/new_licensees.xls"
out = sys.argv[1] if len(sys.argv) > 1 else "data/dre_new_licensees.csv"

def d(s):
    return f"{s[:4]}-{s[4:6]}-{s[6:]}" if len(s) == 8 and s.isdigit() else s

with tempfile.NamedTemporaryFile(suffix=".xls") as tmp:
    urllib.request.urlretrieve(URL, tmp.name)
    sh = xlrd.open_workbook(tmp.name).sheet_by_index(0)
    head = [c.strip("\x00") for c in sh.row_values(0)]
    rows = [dict(zip(head, [str(v).strip("\x00").strip() for v in sh.row_values(i)])) for i in range(1, sh.nrows)]

recs = []
for r in rows:
    recs.append({
        "license_number": r["license_number"], "license_type": r["license_type"], "license_status": r["license_status"],
        "first_name": r["licensee_first_secondary_name"], "last_name": r["licensee_last_primary_name"],
        "name_suffix": r["licensee_name_suffix_code"],
        "original_date_of_license": d(r["original_date_of_license"]), "effective_date": d(r["license_effective_date"]),
        "expiration_date": d(r["license_expiration_date"]),
        "address_1": r["address_1"], "address_2": r["address_2"], "city": r["city"], "state": r["state"],
        "zip_code": r["zip_code"], "county": r["county_name"],
        "related_license_number": r["related_license_number"],
        "related_name": (r["related_first_name"] + " " + r["related_last_name"]).strip(),
        "related_license_type": r["related_license_type"],
        "restricted": r["restricted_flag"], "multiple_license": r["multiple_license_ind"], "email": "",
    })
recs.sort(key=lambda x: (x["original_date_of_license"], x["license_number"]), reverse=True)
with open(out, "w", newline="", encoding="utf-8-sig") as f:
    w = csv.DictWriter(f, fieldnames=list(recs[0])); w.writeheader(); w.writerows(recs)
print(f"wrote {len(recs)} rows to {out}")
