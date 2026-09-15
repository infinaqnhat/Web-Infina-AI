#!/usr/bin/env python3
"""Client goi Microsoft Clarity Data Export API cho site cua ban.

Dung bien moi truong SEO_CLARITY_TOKEN (khong hardcode token vao file nay).
Neu bien nay khong co, thu doc tu file "secrets/clarity-token.txt" tim theo
duong dan tuong doi tu thu muc lam viec hien tai (khong hardcode duong dan
tuyet doi, vi repo co the nam o bat ky dau khi tai lai o may khac).

GIOI HAN THAT CUA API (khong phai loi script): endpoint project-live-insights CHI
nhan numOfDays = 1, 2, hoac 3. Khong co startDate/endDate, khong lay duoc data xa
hon 3 ngay gan nhat qua API nay (da test thuc te: numOfDays=7 tra ve HTTP 400 rong).

Usage:
    python3 clarity_client.py insights --days 3
"""
import argparse
import json
import os
import sys
import urllib.request
import urllib.error

API_URL = "https://www.clarity.ms/export-data/api/v1/project-live-insights"


def get_token() -> str:
    token = os.environ.get("SEO_CLARITY_TOKEN")
    if token:
        return token.strip()
    for fallback in ("secrets/clarity-token.txt", os.path.join(os.getcwd(), "secrets", "clarity-token.txt")):
        if os.path.exists(fallback):
            with open(fallback, "r", encoding="utf-8") as f:
                return f.read().strip()
    raise RuntimeError(
        "Thieu bien moi truong SEO_CLARITY_TOKEN va khong tim thay "
        "secrets/clarity-token.txt trong thu muc lam viec hien tai. Xem docstring dau file."
    )


def fetch_insights(num_of_days: int) -> list:
    if num_of_days not in (1, 2, 3):
        raise ValueError("numOfDays chi duoc phep la 1, 2 hoac 3 (gioi han that cua Clarity API).")

    token = get_token()
    url = f"{API_URL}?numOfDays={num_of_days}"
    req = urllib.request.Request(url, headers={"Authorization": f"Bearer {token}"})
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            return json.load(resp)
    except urllib.error.HTTPError as e:
        body = e.read().decode("utf-8", errors="replace")
        raise RuntimeError(f"Clarity API loi HTTP {e.code}: {body}") from e


def main():
    parser = argparse.ArgumentParser(description="Client cho Microsoft Clarity Data Export API")
    sub = parser.add_subparsers(dest="command", required=True)

    p_insights = sub.add_parser("insights", help="Lay live insights (traffic, UX metrics, top pages...)")
    p_insights.add_argument("--days", type=int, default=3, choices=[1, 2, 3],
                             help="So ngay gan nhat, chi duoc 1/2/3 (mac dinh 3)")

    args = parser.parse_args()

    if args.command == "insights":
        data = fetch_insights(args.days)
        print(json.dumps(data, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
