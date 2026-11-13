#!/usr/bin/env python3
"""Lấy listing agent và email công khai từ danh sách link Zillow listing.

Quy trình:
  1. trakk/zillow-scraper (mode DETAIL): link listing -> listing agent, license, brokerage, profile Zillow.
  2. parsebird/zillow-agent-leads-finder (enrichEmails): profile Zillow -> email do agent tự công khai.
  3. Dự phòng cho agent còn thiếu email (không có profile Zillow, hoặc profile không công khai email):
     apify/google-search-scraper tìm "tên + brokerage + license", lấy email xuất hiện trong kết quả
     (thường là trang agent trên website brokerage). Chỉ nhận email nằm trong kết quả có chứa họ của agent.
     Mỗi lần chạy bước này tốn tối thiểu khoảng $0.5 (Apify), nên chỉ chạy một lần cho cả lô.
     Tắt bằng --no-google. Các dòng có email_source = google_search cần kiểm tra lại kỹ hơn.

Chạy:
  export Apify_key=...
  python3 zillow_agent_emails.py links.txt -o agents.csv
  python3 zillow_agent_emails.py "https://www.zillow.com/homedetails/.../123_zpid/" -o agents.csv

links.txt: mỗi dòng một link listing (dòng trống và dòng bắt đầu bằng # bị bỏ qua).
Chỉ dùng email công khai do agent tự đăng. Cần xác minh email trước khi gửi.
"""
import argparse
import csv
import json
import os
import re
import sys
import urllib.error
import urllib.request

API = "https://api.apify.com/v2/acts/{}/run-sync-get-dataset-items"
DETAIL_ACTOR = "trakk~zillow-scraper"
PROFILE_ACTOR = "parsebird~zillow-agent-leads-finder"
GOOGLE_ACTOR = "apify~google-search-scraper"
GOOGLE_MIN_COST = "0.5"  # Apify không cho đặt trần thấp hơn 0.5 cho actor này
EMAIL_RE = re.compile(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9-]+(?:\.[A-Za-z0-9-]+)+")
GENERIC_LOCAL = {"info", "contact", "support", "hello", "admin", "sales", "office", "help", "noreply", "no-reply"}
FIELDS = ["listing_url", "zpid", "address", "agent_name", "agent_phone", "license",
          "brokerage", "profile_url", "email", "email_source", "status"]


def run_actor(actor, payload, token, max_cost, timeout):
    url = API.format(actor) + "?timeout=%d&maxTotalChargeUsd=%s" % (timeout, max_cost)
    req = urllib.request.Request(
        url, data=json.dumps(payload).encode(),
        headers={"Authorization": "Bearer " + token, "Content-Type": "application/json"})
    try:
        with urllib.request.urlopen(req, timeout=timeout + 60) as r:
            data = json.load(r)
    except urllib.error.HTTPError as e:
        sys.exit("Apify lỗi %s (%s): %s" % (e.code, actor, e.read()[:300].decode(errors="replace")))
    return data if isinstance(data, list) else []


def zpid_of(url):
    m = re.search(r"/(\d+)_zpid", url)
    return m.group(1) if m else None


def screen_name(profile_url):
    m = re.search(r"/profile/([^/?#]+)", profile_url or "")
    return norm(m.group(1)) if m else None


def norm(s):
    return re.sub(r"[^a-z0-9]", "", (s or "").lower())


def pick_google_email(agent_name, results):
    """Chọn email từ kết quả Google. Chỉ nhận kết quả có chứa họ của agent."""
    parts = [x for x in re.split(r"\s+", agent_name.lower().strip()) if len(x) > 1]
    if not parts:
        return "", ""
    last = parts[-1]
    best = ("", "", -1)
    for r in results:
        text = " ".join(str(r.get(k) or "") for k in ("title", "description"))
        if last not in text.lower():
            continue
        for e in EMAIL_RE.findall(text):
            e = e.rstrip(".")
            local = e.split("@")[0].lower()
            if local in GENERIC_LOCAL:
                continue
            score = sum(1 for x in parts if x in local)
            if score > best[2]:
                best = (e, r.get("url") or "", score)
    return best[0], best[1]


def read_links(args):
    links = []
    for a in args:
        if os.path.isfile(a):
            for line in open(a, encoding="utf-8"):
                line = line.strip()
                if line and not line.startswith("#"):
                    links.append(line)
        else:
            links.append(a.strip())
    return [l for l in dict.fromkeys(links) if l]


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("inputs", nargs="+", help="file chứa link, hoặc link trực tiếp")
    ap.add_argument("-o", "--output", default="agents.csv")
    ap.add_argument("--max-cost", default="1.0", help="trần chi phí USD cho mỗi bước (mặc định 1.0)")
    ap.add_argument("--timeout", type=int, default=240)
    ap.add_argument("--no-google", action="store_true", help="bỏ bước dự phòng tìm email bằng Google")
    args = ap.parse_args()

    token = os.environ.get("Apify_key") or os.environ.get("APIFY_TOKEN")
    if not token:
        sys.exit("Thiếu biến môi trường Apify_key")

    links = read_links(args.inputs)
    if not links:
        sys.exit("Không có link nào")
    rows = {}
    for l in links:
        z = zpid_of(l)
        rows[l] = {"listing_url": l, "zpid": z or "", "status": "" if z else "link không có zpid"}
    valid = [l for l in links if rows[l]["zpid"]]

    # Bước 1: listing -> agent + profile
    print("Bước 1: lấy listing agent cho %d link..." % len(valid), file=sys.stderr)
    by_zpid = {}
    if valid:
        items = run_actor(DETAIL_ACTOR, {"mode": "DETAIL", "targets": valid, "maxResults": len(valid)},
                          token, args.max_cost, args.timeout)
        for it in items:
            by_zpid[str(it.get("zpid"))] = it
    for l in valid:
        r, it = rows[l], by_zpid.get(rows[l]["zpid"])
        if not it:
            r["status"] = "không lấy được listing"
            continue
        am = (((it.get("contactFormRenderData") or {}).get("data") or {}).get("agent_module")) or {}
        att = it.get("attributionInfo") or {}
        prof = am.get("profile_url") or ""
        r.update(
            address=it.get("address") if isinstance(it.get("address"), str) else it.get("streetAddress", ""),
            agent_name=att.get("agentName") or am.get("display_name") or "",
            agent_phone=att.get("agentPhoneNumber") or "",
            license=att.get("agentLicenseNumber") or "",
            brokerage=att.get("brokerName") or am.get("business_name") or "",
            profile_url=("https://www.zillow.com" + prof) if prof.startswith("/") else prof,
            status="ok" if prof else "listing không có profile agent")

    # Bước 2: profile -> email (mỗi profile chỉ chạy một lần)
    profiles = list(dict.fromkeys(r["profile_url"] for r in rows.values() if r.get("profile_url")))
    emails = {}
    if profiles:
        print("Bước 2: lấy email cho %d profile..." % len(profiles), file=sys.stderr)
        items = run_actor(PROFILE_ACTOR, {"startUrls": [{"url": p} for p in profiles],
                                          "maxItems": len(profiles), "enrichEmails": True},
                          token, args.max_cost, args.timeout)
        for it in items:
            for key in (screen_name(it.get("url")), norm(it.get("screenName"))):
                if key:
                    emails[key] = it
    for r in rows.values():
        it = emails.get(screen_name(r.get("profile_url")) or "")
        if not it:
            if r.get("profile_url"):
                r["status"] = "không lấy được profile"
            continue
        r["email"] = it.get("email") or it.get("contactEmail") or ""
        r["email_source"] = "zillow_profile" if it.get("email") else ("agent_website" if it.get("contactEmail") else "")
        if not r["email"] and r.get("status") == "ok":
            r["status"] = "profile không công khai email"

    # Bước 3: dự phòng, tìm Google cho agent còn thiếu email
    if not args.no_google:
        missing = [r for r in rows.values() if r.get("agent_name") and not r.get("email")]
        queries = {}
        for r in missing:
            q = " ".join(x for x in [r["agent_name"], r.get("brokerage", ""),
                                     re.sub(r"^DRE\s*#?\s*", "", r.get("license", "")), "email"] if x)
            queries[q] = r
        if queries:
            print("Bước 3: tìm Google cho %d agent còn thiếu email..." % len(queries), file=sys.stderr)
            pages = run_actor(GOOGLE_ACTOR, {"queries": "\n".join(queries), "maxPagesPerQuery": 1,
                                              "resultsPerPage": 10, "countryCode": "us"},
                              token, str(max(float(args.max_cost), float(GOOGLE_MIN_COST))), args.timeout)
            for pg in pages:
                term = (pg.get("searchQuery") or {}).get("term", "")
                r = queries.get(term)
                if not r or r.get("email"):
                    continue
                email, src = pick_google_email(r["agent_name"], pg.get("organicResults") or [])
                if email:
                    r["email"], r["email_source"] = email, "google_search"
                    r["status"] = "email từ Google (%s), cần kiểm tra" % src

    with open(args.output, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=FIELDS)
        w.writeheader()
        for l in links:
            w.writerow({k: rows[l].get(k, "") for k in FIELDS})
    n = sum(1 for r in rows.values() if r.get("email"))
    print("Xong: %d/%d link có email. File: %s" % (n, len(links), args.output), file=sys.stderr)


if __name__ == "__main__":
    main()
