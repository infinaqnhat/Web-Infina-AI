#!/usr/bin/env python3
"""Teardown cụm pillar của 1 site: crawl sitemap, dựng internal link graph, xếp hạng pillar.

Xem wordpress-mcp/references/competitor-pillar-teardown.md cho phương pháp đầy đủ.

Chỉ dùng thư viện chuẩn của Python 3, không cần pip install gì.

    python3 competitor_teardown.py www.example.com
    python3 competitor_teardown.py www.example.com --workers 6 --limit 2000
    python3 competitor_teardown.py www.example.com --path /blog/      # chỉ 1 folder

Chạy xong sẽ có graph.json trong thư mục hiện tại. Gửi file đó đi là phân tích được tiếp,
không cần crawl lại.
"""
import argparse
import gzip
import json
import re
import sys
import time
import urllib.error
import urllib.request
from collections import defaultdict
from concurrent.futures import ThreadPoolExecutor

UA = ("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36")
HEADERS = {
    "User-Agent": UA,
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.9",
}
SKIP_EXT = re.compile(r"\.(jpg|jpeg|png|gif|webp|svg|pdf|zip|mp4|mp3|css|js|ico)$", re.I)


def fetch_raw(url, timeout=30):
    req = urllib.request.Request(url, headers=HEADERS)
    with urllib.request.urlopen(req, timeout=timeout) as r:
        data = r.read()
        if r.headers.get("Content-Encoding") == "gzip" or url.endswith(".gz"):
            try:
                data = gzip.decompress(data)
            except OSError:
                pass
        return r.geturl(), data


# ---------------------------------------------------------------- sitemap

GUESSES = ("sitemap_index.xml", "sitemap.xml", "wp-sitemap.xml",
           "post-sitemap.xml", "sitemap-index.xml")


def discover_sitemaps(domain, path_filter="", explicit=""):
    """Tìm sitemap qua robots.txt rồi tới các đường dẫn quen thuộc.

    path_filter cũng được thử như 1 prefix, vì WordPress hay được cài trong
    subfolder (vd blog ở /news/ thì sitemap nằm ở /news/post-sitemap.xml chứ
    không phải ở gốc domain).
    """
    found = []
    if explicit:
        found.append(explicit)
    try:
        _, body = fetch_raw(f"https://{domain}/robots.txt")
        found += re.findall(r"(?im)^\s*sitemap:\s*(\S+)", body.decode("utf-8", "ignore"))
    except Exception:
        pass
    prefixes = [""]
    if path_filter:
        prefixes.append(path_filter.strip("/") + "/")
    for pre in prefixes:
        for guess in GUESSES:
            found.append(f"https://{domain}/{pre}{guess}")
    seen, out = set(), []
    for u in found:
        if u not in seen:
            seen.add(u)
            out.append(u)
    return out


def collect_urls(domain, path_filter, limit, explicit=""):
    """Đi đệ quy qua sitemap index, trả về danh sách URL trang."""
    queue, seen_sm, urls = discover_sitemaps(domain, path_filter, explicit), set(), []
    while queue:
        sm = queue.pop(0)
        if sm in seen_sm:
            continue
        seen_sm.add(sm)
        try:
            _, body = fetch_raw(sm)
        except Exception:
            continue
        xml = body.decode("utf-8", "ignore")
        if "<sitemapindex" in xml:
            queue += re.findall(r"<loc>\s*([^<\s]+)\s*</loc>", xml)
            continue
        for loc in re.findall(r"<loc>\s*([^<\s]+)\s*</loc>", xml):
            if SKIP_EXT.search(loc):
                continue
            if path_filter and path_filter not in loc:
                continue
            urls.append(loc)
        if limit and len(urls) >= limit:
            break
    out, seen = [], set()
    for u in urls:
        k = u.rstrip("/")
        if k not in seen:
            seen.add(k)
            out.append(u)
    return out[:limit] if limit else out


# ---------------------------------------------------------------- crawl

def make_fetcher(domain, delay):
    link_re = re.compile(rf'href="(https?://{re.escape(domain)}/[^"#?]*)"')

    def fetch(url):
        try:
            final, body = fetch_raw(url)
            html = body.decode("utf-8", "ignore")
        except urllib.error.HTTPError as e:
            return url, None, set(), f"HTTP {e.code}"
        except Exception as e:
            return url, None, set(), type(e).__name__
        # bỏ header/nav/footer, nếu không mọi link menu sẽ đếm vào mọi trang
        main = re.split(r"<main\b|<article\b", html, 1)
        body_html = main[-1] if len(main) > 1 else html
        body_html = re.split(r"<footer\b", body_html, 1)[0]
        links = {l.rstrip("/") for l in link_re.findall(body_html)
                 if not SKIP_EXT.search(l)}
        if delay:
            time.sleep(delay)
        return url, final, links - {url.rstrip("/")}, None

    return fetch


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("domain", help="vd www.example.com, không có https://")
    ap.add_argument("--workers", type=int, default=12, help="số luồng, mặc định 12")
    ap.add_argument("--delay", type=float, default=0.0, help="nghỉ giữa request, giây")
    ap.add_argument("--limit", type=int, default=0, help="giới hạn số URL, 0 là không giới hạn")
    ap.add_argument("--path", default="", help="chỉ crawl URL chứa chuỗi này, vd /blog/")
    ap.add_argument("--sitemap", default="", help="URL sitemap cụ thể, dùng khi tự dò không ra")
    ap.add_argument("--out", default="graph.json")
    a = ap.parse_args()
    domain = a.domain.replace("https://", "").replace("http://", "").strip("/")

    print(f"[1/3] tìm sitemap cho {domain} ...")
    urls = collect_urls(domain, a.path, a.limit, a.sitemap)
    if not urls:
        print("  không đọc được sitemap nào. Site có thể chặn bot, hoặc không có sitemap.")
        print("  thử mở https://%s/robots.txt trên trình duyệt để xem site khai sitemap ở đâu." % domain)
        sys.exit(1)
    print(f"  {len(urls)} URL")

    print(f"[2/3] crawl với {a.workers} luồng ...")
    fetch = make_fetcher(domain, a.delay)
    out, redirected, failed = {}, [], defaultdict(int)
    t0 = time.time()
    with ThreadPoolExecutor(max_workers=a.workers) as ex:
        for i, (u, final, links, err) in enumerate(ex.map(fetch, urls), 1):
            if err:
                failed[err] += 1
            elif final.rstrip("/") != u.rstrip("/"):
                redirected.append(u)            # stub 301, loại khỏi phân tích
            else:
                out[u.rstrip("/")] = links
            if i % 100 == 0 or i == len(urls):
                el = time.time() - t0
                print(f"  {i}/{len(urls)}  {el:.0f}s  ({el/i:.2f}s/URL)")
    if failed:
        print("  lỗi:", dict(failed))
    print(f"  {len(redirected)} stub 301 đã loại, {len(out)} trang thật")
    if not out:
        print("  không trang nào đọc được. Nhiều khả năng site chặn crawl, dừng ở đây.")
        sys.exit(1)

    print("[3/3] xếp hạng ...")
    pages = set(out)                            # chỉ xếp hạng trang có trong sitemap,
    inbound = defaultdict(int)                  # nếu không category archive sẽ leo lên đầu
    for src, dsts in out.items():
        for d in dsts:
            if d in pages:
                inbound[d] += 1

    rows = sorted(
        ((inbound[u], len(out[u]), u.replace(f"https://{domain}", "").strip("/").count("/"), u)
         for u in out), reverse=True)
    print(f"\n{'IN':>4} {'OUT':>4} {'DEPTH':>5}  URL")
    for r in rows[:30]:
        print(f"{r[0]:>4} {r[1]:>4} {r[2]:>5}  {r[3]}")

    orphans = [r for r in rows if r[0] == 0]
    print(f"\n{len(orphans)} trang không có inbound nội bộ nào:")
    for r in orphans[:20]:
        print(f"  OUT={r[1]:<4} {r[3]}")

    json.dump({
        "domain": domain,
        "crawled_at": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        "sitemap_urls": len(urls),
        "pages": len(out),
        "redirect_stubs": redirected,
        "errors": dict(failed),
        "graph": {k: sorted(v) for k, v in out.items()},
    }, open(a.out, "w"), indent=1)
    print(f"\nđã lưu {a.out} ({len(out)} trang). Gửi file này đi là phân tích tiếp được.")


if __name__ == "__main__":
    main()
