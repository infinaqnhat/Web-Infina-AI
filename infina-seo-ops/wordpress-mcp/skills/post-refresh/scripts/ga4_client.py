#!/usr/bin/env python3
"""
Client goi Google Analytics 4 Data API (analyticsdata.googleapis.com) bang chinh
service account key da dung cho GSC (`gsc-service-account.json`). Service account
nay PHAI duoc them thu cong vao GA4 property cua site (GA4 Admin > Account Access
Management > them dung email service account, quyen Viewer la du), Google Cloud
cap quyen GSC va GA4 rieng biet nen 1 key co quyen GSC khong tu dong co quyen GA4.

Yeu cau bien moi truong SEO_GSC_SA_JSON chua NGUYEN VAN noi dung JSON cua
service account key (dung chung voi gsc_client.py, khong phai key rieng).

Bat buoc set bien moi truong SEO_GA4_PROPERTY_ID (xem trong GA4 Admin > Property
Settings, la day so, KHONG phai Measurement ID dang G-XXXXXXX). Khong co gia tri
mac dinh that, script se bao loi ro neu chua set.

Khac voi Clarity (chi lay duoc 1-3 ngay), GA4 Data API KHONG bi gioi han thoi gian
nhu vay, co the lay bat ky khoang ngay nao (7 ngay, 28 ngay, ca nam).

Cach dung (CLI):
    python3 ga4_client.py traffic --start 7daysAgo --end today
    python3 ga4_client.py pages --start 28daysAgo --end today --limit 20
    python3 ga4_client.py sources --start 28daysAgo --end today --limit 20

--start/--end nhan ca dinh dang tuyet doi (YYYY-MM-DD) lan tuong doi kieu GA4
(vd "7daysAgo", "28daysAgo", "today", "yesterday").
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


class GA4Client:
    def __init__(self, sa_json=None, property_id=None):
        raw = sa_json or os.environ.get("SEO_GSC_SA_JSON")
        if not raw:
            raise RuntimeError(
                "Thieu bien moi truong SEO_GSC_SA_JSON (noi dung JSON cua service "
                "account key, dung chung voi gsc_client.py). Xem docstring dau file."
            )
        self.sa = json.loads(raw)
        self.property_id = property_id or os.environ.get("SEO_GA4_PROPERTY_ID", "YOUR_GA4_PROPERTY_ID")
        self._token = None
        self._token_exp = 0

    def _get_token(self):
        if self._token and time.time() < self._token_exp - 60:
            return self._token

        now = int(time.time())
        payload = {
            "iss": self.sa["client_email"],
            "scope": "https://www.googleapis.com/auth/analytics.readonly",
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

    def _run_report(self, dimensions, metrics, start, end, limit=25, order_by_metric=None,
                     page_path_filter=None):
        token = self._get_token()
        body = {
            "dateRanges": [{"startDate": start, "endDate": end}],
            "dimensions": [{"name": d} for d in dimensions],
            "metrics": [{"name": m} for m in metrics],
            "limit": limit,
        }
        if order_by_metric:
            body["orderBys"] = [{"metric": {"metricName": order_by_metric}, "desc": True}]
        if page_path_filter:
            body["dimensionFilter"] = {
                "filter": {
                    "fieldName": "pagePath",
                    "stringFilter": {"matchType": "EXACT", "value": page_path_filter},
                }
            }

        req = urllib.request.Request(
            f"https://analyticsdata.googleapis.com/v1beta/properties/{self.property_id}:runReport",
            data=json.dumps(body).encode(),
            headers={"Authorization": f"Bearer {token}", "Content-Type": "application/json"},
            method="POST",
        )
        try:
            with urllib.request.urlopen(req, timeout=30) as resp:
                return json.loads(resp.read().decode())
        except urllib.error.HTTPError as e:
            raise RuntimeError(f"GA4 API loi {e.code}: {e.read().decode()}") from e

    def traffic_by_date(self, start, end):
        return self._run_report(
            dimensions=["date"],
            metrics=["sessions", "activeUsers", "screenPageViews"],
            start=start, end=end, limit=1000,
        )

    def top_pages(self, start, end, limit=25):
        return self._run_report(
            dimensions=["pagePath", "pageTitle"],
            metrics=["screenPageViews", "sessions", "averageSessionDuration"],
            start=start, end=end, limit=limit, order_by_metric="screenPageViews",
        )

    def traffic_sources(self, start, end, limit=25):
        return self._run_report(
            dimensions=["sessionSource", "sessionMedium"],
            metrics=["sessions", "activeUsers"],
            start=start, end=end, limit=limit, order_by_metric="sessions",
        )

    def page_sources(self, page_path, start, end, limit=25):
        """Breakdown nguon/kenh cho DUNG 1 trang cu the (pagePath phai khop chinh xac,
        vd '/shop/tay-cam-ps4-dualshock4-rep/'). Dung khi nghi ngo 1 trang tang/giam
        traffic do 1 nguon cu the (Facebook, direct, referral...) chu khong phai do SEO."""
        return self._run_report(
            dimensions=["sessionSource", "sessionMedium"],
            metrics=["sessions", "screenPageViews"],
            start=start, end=end, limit=limit, order_by_metric="sessions",
            page_path_filter=page_path,
        )


def _print_report(report):
    dim_names = [h["name"] for h in report.get("dimensionHeaders", [])]
    metric_names = [h["name"] for h in report.get("metricHeaders", [])]
    rows = report.get("rows", [])
    if not rows:
        print("(khong co du lieu)")
        return
    for row in rows:
        dims = " / ".join(dv["value"] for dv in row.get("dimensionValues", []))
        metrics = "  ".join(
            f"{name}={mv['value']}" for name, mv in zip(metric_names, row.get("metricValues", []))
        )
        print(f"{dims}\t{metrics}")


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = parser.add_subparsers(dest="cmd", required=True)

    p_traffic = sub.add_parser("traffic", help="Sessions/users/pageviews theo ngay")
    p_traffic.add_argument("--start", required=True)
    p_traffic.add_argument("--end", required=True)

    p_pages = sub.add_parser("pages", help="Top trang theo pageviews")
    p_pages.add_argument("--start", required=True)
    p_pages.add_argument("--end", required=True)
    p_pages.add_argument("--limit", type=int, default=25)

    p_sources = sub.add_parser("sources", help="Traffic theo nguon/kenh (source/medium)")
    p_sources.add_argument("--start", required=True)
    p_sources.add_argument("--end", required=True)
    p_sources.add_argument("--limit", type=int, default=25)

    p_page_sources = sub.add_parser("page-sources", help="Breakdown nguon/kenh cho 1 trang cu the")
    p_page_sources.add_argument("--page", required=True, help="pagePath chinh xac, vd /ayn-thor-review/")
    p_page_sources.add_argument("--start", required=True)
    p_page_sources.add_argument("--end", required=True)
    p_page_sources.add_argument("--limit", type=int, default=25)

    args = parser.parse_args()
    client = GA4Client()

    if args.cmd == "traffic":
        _print_report(client.traffic_by_date(args.start, args.end))
    elif args.cmd == "pages":
        _print_report(client.top_pages(args.start, args.end, args.limit))
    elif args.cmd == "sources":
        _print_report(client.traffic_sources(args.start, args.end, args.limit))
    elif args.cmd == "page-sources":
        _print_report(client.page_sources(args.page, args.start, args.end, args.limit))


if __name__ == "__main__":
    main()
