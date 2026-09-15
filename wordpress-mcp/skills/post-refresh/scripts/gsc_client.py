#!/usr/bin/env python3
"""
Client gọi Google Search Console API (webmasters v3 + searchconsole v1) bằng service
account, dùng cho skill post-refresh (generic SEO toolkit).

Yeu cau bien moi truong SEO_GSC_SA_JSON chua NGUYEN VAN BAN JSON cua service
account key (khong phai duong dan file), vi container chay skill la ephemeral, khong
the dua vao 1 file co dinh con ton tai giua cac lan chay.

Cach lay noi dung dung cho bien nay: doc file JSON key bang 1 dong (khong xuong dong),
hoac dung `python3 -c "import json;print(json.dumps(json.load(open('key.json'))))"` roi
set lam gia tri bien moi truong SEO_GSC_SA_JSON trong cau hinh environment/session.

Site mac dinh: https://example.com/ (co the doi qua bien SEO_GSC_SITE_URL).

Cach dung (CLI):
    python3 gsc_client.py pages --start 2026-07-14 --end 2026-08-12 --limit 25
    python3 gsc_client.py queries --start 2026-07-14 --end 2026-08-12 --limit 25 --page "https://example.com/ten-bai-viet-mau/"
    python3 gsc_client.py inspect --url "https://example.com/ten-bai-viet-mau/"

Cach dung (import):
    from gsc_client import GSCClient
    client = GSCClient()
    rows = client.query_pages(start="2026-07-14", end="2026-08-12", limit=25)
"""

import argparse
import json
import os
import sys
import time
import urllib.error
import urllib.parse
import urllib.request

try:
    import jwt  # PyJWT
except ImportError:
    print("Thieu thu vien PyJWT. Cai bang: pip3 install PyJWT cryptography", file=sys.stderr)
    sys.exit(1)


class GSCClient:
    def __init__(self, sa_json=None, site_url=None):
        raw = sa_json or os.environ.get("SEO_GSC_SA_JSON")
        if not raw:
            raise RuntimeError(
                "Thieu bien moi truong SEO_GSC_SA_JSON (noi dung JSON cua service "
                "account key). Xem docstring dau file de biet cach lay gia tri nay."
            )
        self.sa = json.loads(raw)
        self.site_url = site_url or os.environ.get(
            "SEO_GSC_SITE_URL", "https://example.com/"
        )
        self._token = None
        self._token_exp = 0

    def _get_token(self):
        if self._token and time.time() < self._token_exp - 60:
            return self._token

        now = int(time.time())
        payload = {
            "iss": self.sa["client_email"],
            "scope": "https://www.googleapis.com/auth/webmasters.readonly",
            "aud": self.sa["token_uri"],
            "iat": now,
            "exp": now + 3600,
        }
        assertion = jwt.encode(payload, self.sa["private_key"], algorithm="RS256")
        data = urllib.parse.urlencode(
            {
                "grant_type": "urn:ietf:params:oauth:grant-type:jwt-bearer",
                "assertion": assertion,
            }
        ).encode()
        req = urllib.request.Request(self.sa["token_uri"], data=data, method="POST")
        with urllib.request.urlopen(req, timeout=30) as resp:
            tok = json.loads(resp.read().decode())
        self._token = tok["access_token"]
        self._token_exp = now + int(tok.get("expires_in", 3600))
        return self._token

    def _post(self, url, body):
        token = self._get_token()
        req = urllib.request.Request(
            url,
            data=json.dumps(body).encode(),
            headers={
                "Authorization": f"Bearer {token}",
                "Content-Type": "application/json",
            },
            method="POST",
        )
        try:
            with urllib.request.urlopen(req, timeout=30) as resp:
                return json.loads(resp.read().decode())
        except urllib.error.HTTPError as e:
            raise RuntimeError(f"GSC API loi {e.code}: {e.read().decode()}") from e

    def _get(self, url):
        token = self._get_token()
        req = urllib.request.Request(url, headers={"Authorization": f"Bearer {token}"})
        try:
            with urllib.request.urlopen(req, timeout=30) as resp:
                return json.loads(resp.read().decode())
        except urllib.error.HTTPError as e:
            raise RuntimeError(f"GSC API loi {e.code}: {e.read().decode()}") from e

    def query_pages(self, start, end, limit=25, order_by="clicks"):
        site_enc = urllib.parse.quote(self.site_url, safe="")
        body = {
            "startDate": start,
            "endDate": end,
            "dimensions": ["page"],
            "rowLimit": limit,
            "orderBy": [{"fieldName": order_by, "sortOrder": "DESCENDING"}],
        }
        result = self._post(
            f"https://www.googleapis.com/webmasters/v3/sites/{site_enc}/searchAnalytics/query",
            body,
        )
        return result.get("rows", [])

    def query_queries_for_page(self, page_url, start, end, limit=25):
        site_enc = urllib.parse.quote(self.site_url, safe="")
        body = {
            "startDate": start,
            "endDate": end,
            "dimensions": ["query"],
            "rowLimit": limit,
            "orderBy": [{"fieldName": "impressions", "sortOrder": "DESCENDING"}],
            "dimensionFilterGroups": [
                {
                    "filters": [
                        {"dimension": "page", "operator": "equals", "expression": page_url}
                    ]
                }
            ],
        }
        result = self._post(
            f"https://www.googleapis.com/webmasters/v3/sites/{site_enc}/searchAnalytics/query",
            body,
        )
        return result.get("rows", [])

    def inspect_url(self, url):
        body = {"inspectionUrl": url, "siteUrl": self.site_url}
        result = self._post(
            "https://searchconsole.googleapis.com/v1/urlInspection/index:inspect", body
        )
        return result.get("inspectionResult", {})


# Benchmark CTR theo vi tri trung binh, tu references/post-refresh-playbook.md
# (rut ra tu case that tren example.com, khong phai so ly thuyet)
_CTR_BENCHMARK = [
    (1, 29), (2, 15), (3, 11), (4, 8), (5, 7),
    (6, 5), (7, 4), (8, 3.5), (9, 3), (10, 2.5),
]


def benchmark_ctr(position):
    for max_pos, ctr in _CTR_BENCHMARK:
        if position <= max_pos:
            return ctr
    return 1.5  # trang 2 (vi tri 11-20)


def find_striking_distance(rows, min_position=8, max_position=20, min_impressions=10):
    """Loc trang o vung 'striking distance' (vi tri 8-20), impressions du lon, va CTR
    thap hon benchmark theo vi tri (co hoi that, khong chi la vi tri kem binh thuong).
    Tra ve list da sort giam dan theo impressions, kem ca nhung trang CTR dung/tren benchmark
    (danh dau rieng) de tien doi chieu."""
    out = []
    for r in rows:
        position = r.get("position", 0)
        impressions = r.get("impressions", 0)
        if not (min_position <= position <= max_position):
            continue
        if impressions < min_impressions:
            continue
        clicks = r.get("clicks", 0)
        ctr = r.get("ctr", 0) * 100
        bench = benchmark_ctr(position)
        gap = ctr - bench
        out.append({
            "page": " / ".join(r.get("keys", [])),
            "clicks": clicks, "impressions": impressions,
            "ctr": ctr, "position": position, "benchmark_ctr": bench, "gap": gap,
        })
    out.sort(key=lambda x: -x["impressions"])
    return out


def _print_rows(rows, key_label):
    for r in rows:
        keys = " / ".join(r.get("keys", []))
        clicks = r.get("clicks", 0)
        impressions = r.get("impressions", 0)
        ctr = r.get("ctr", 0) * 100
        position = r.get("position", 0)
        print(
            f"{keys}\tclicks={clicks}\timpressions={impressions}\tctr={ctr:.2f}%\tposition={position:.1f}"
        )


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = parser.add_subparsers(dest="cmd", required=True)

    p_pages = sub.add_parser("pages", help="Liet ke trang co traffic, sort theo clicks")
    p_pages.add_argument("--start", required=True)
    p_pages.add_argument("--end", required=True)
    p_pages.add_argument("--limit", type=int, default=25)
    p_pages.add_argument("--order-by", default="clicks", choices=["clicks", "impressions", "ctr", "position"])

    p_queries = sub.add_parser("queries", help="Liet ke query dan traffic ve 1 trang cu the")
    p_queries.add_argument("--page", required=True)
    p_queries.add_argument("--start", required=True)
    p_queries.add_argument("--end", required=True)
    p_queries.add_argument("--limit", type=int, default=25)

    p_inspect = sub.add_parser("inspect", help="Kiem tra index status cho 1 URL cu the")
    p_inspect.add_argument("--url", required=True)

    p_striking = sub.add_parser(
        "striking-distance",
        help="Loc trang vi tri 8-20 co CTR duoi benchmark theo vi tri (co hoi cai thien nhanh)"
    )
    p_striking.add_argument("--start", required=True)
    p_striking.add_argument("--end", required=True)
    p_striking.add_argument("--min-position", type=float, default=8)
    p_striking.add_argument("--max-position", type=float, default=20)
    p_striking.add_argument("--min-impressions", type=int, default=10)
    p_striking.add_argument("--only-below-benchmark", action="store_true",
                             help="Chi in trang co CTR thap hon benchmark (co hoi that)")

    args = parser.parse_args()
    client = GSCClient()

    if args.cmd == "pages":
        rows = client.query_pages(args.start, args.end, args.limit, args.order_by)
        _print_rows(rows, "page")
    elif args.cmd == "queries":
        rows = client.query_queries_for_page(args.page, args.start, args.end, args.limit)
        _print_rows(rows, "query")
    elif args.cmd == "inspect":
        result = client.inspect_url(args.url)
        print(json.dumps(result, indent=2, ensure_ascii=False))
    elif args.cmd == "striking-distance":
        rows = client.query_pages(args.start, args.end, limit=1000, order_by="impressions")
        results = find_striking_distance(rows, args.min_position, args.max_position, args.min_impressions)
        if args.only_below_benchmark:
            results = [r for r in results if r["gap"] < 0]
        if not results:
            print("(khong tim thay trang nao trong vung striking distance voi dieu kien da cho)")
        for r in results:
            flag = "  <-- CTR duoi benchmark (co hoi that)" if r["gap"] < -1 else ""
            print(
                f"{r['page']}\tclicks={r['clicks']}\timpressions={r['impressions']}\t"
                f"ctr={r['ctr']:.2f}%\tposition={r['position']:.1f}\t"
                f"benchmark={r['benchmark_ctr']:.1f}%\tgap={r['gap']:+.1f}pp{flag}"
            )


if __name__ == "__main__":
    main()
