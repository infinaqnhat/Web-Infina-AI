#!/usr/bin/env python3
"""Teardown cụm pillar của 1 site: lấy URL, dựng internal link graph, xếp hạng pillar.

Xem wordpress-mcp/references/competitor-pillar-teardown.md cho phương pháp đầy đủ.
Chỉ dùng thư viện chuẩn của Python 3, không cần pip install gì.

    python3 competitor_teardown.py www.example.com
    python3 competitor_teardown.py www.example.com --path /blog/ --workers 6
    python3 competitor_teardown.py example.com --crawl            # site khong co sitemap tu te
    python3 competitor_teardown.py example.com --urls seed.txt    # nap them URL tu file

Chạy xong có graph.json. Gửi file đó đi là phân tích tiếp được, không cần crawl lại.

Script LUÔN tôn trọng Disallow trong robots.txt. Dùng --ignore-robots để bỏ qua chỉ khi
site đó là của chính bạn.
"""
import argparse
import gzip
import json
import re
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from collections import defaultdict, deque
from concurrent.futures import ThreadPoolExecutor

UA = ("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36")
HEADERS = {
    "User-Agent": UA,
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.9",
}
SKIP_EXT = re.compile(r"\.(jpg|jpeg|png|gif|webp|svg|pdf|zip|mp4|mp3|css|js|ico)$", re.I)
GUESSES = ("sitemap_index.xml", "sitemap.xml", "wp-sitemap.xml",
           "post-sitemap.xml", "sitemap-index.xml")


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


# ---------------------------------------------------------------- robots.txt

def load_robots(domain):
    """Trả về (danh sách path bị Disallow cho User-agent *, danh sách sitemap khai báo)."""
    disallow, sitemaps, applies = [], [], False
    try:
        _, body = fetch_raw(f"https://{domain}/robots.txt")
        text = body.decode("utf-8", "ignore")
    except Exception:
        return disallow, sitemaps
    if text.lstrip().lower().startswith("<!doctype"):
        return disallow, sitemaps          # bi chan, tra ve trang HTML chu khong phai robots
    for line in text.splitlines():
        line = line.split("#", 1)[0].strip()
        if not line or ":" not in line:
            continue
        key, _, val = line.partition(":")
        key, val = key.strip().lower(), val.strip()
        if key == "user-agent":
            applies = val == "*"
        elif key == "sitemap":
            sitemaps.append(val)
        elif key == "disallow" and applies and val:
            disallow.append(val)
    return disallow, sitemaps


def blocked(url, disallow):
    path = urllib.parse.urlsplit(url).path or "/"
    return any(path.startswith(d) for d in disallow)


# ---------------------------------------------------------------- sitemap

def collect_sitemap_urls(domain, path_filter, limit, explicit, declared):
    queue = ([explicit] if explicit else []) + list(declared)
    prefixes = [""] + ([path_filter.strip("/") + "/"] if path_filter else [])
    for pre in prefixes:
        queue += [f"https://{domain}/{pre}{g}" for g in GUESSES]
    seen_sm, urls = set(), []
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
            if SKIP_EXT.search(loc) or (path_filter and path_filter not in loc):
                continue
            urls.append(loc)
        if limit and len(urls) >= limit:
            break
    return urls


# ---------------------------------------------------------------- crawl

def make_fetcher(domain, delay):
    link_re = re.compile(rf'href="(https?://{re.escape(domain)}/[^"#?]*)"')
    rel_re = re.compile(r'href="(/[^"#?][^"#?]*)"')

    def fetch(url, want_all_links=False):
        try:
            final, body = fetch_raw(url)
            html = body.decode("utf-8", "ignore")
        except urllib.error.HTTPError as e:
            return url, None, set(), f"HTTP {e.code}"
        except Exception as e:
            return url, None, set(), type(e).__name__
        scope = html if want_all_links else None
        if scope is None:
            # bo header/nav/footer, neu khong moi link menu se dem vao moi trang
            parts = re.split(r"<main\b|<article\b", html, 1)
            scope = parts[-1] if len(parts) > 1 else html
            scope = re.split(r"<footer\b", scope, 1)[0]
        links = {l.rstrip("/") for l in link_re.findall(scope)}
        links |= {f"https://{domain}{l}".rstrip("/") for l in rel_re.findall(scope)}
        links = {l for l in links if not SKIP_EXT.search(l)}
        if delay:
            time.sleep(delay)
        return url, final, links - {url.rstrip("/")}, None

    return fetch


def bfs_discover(domain, fetch, disallow, limit, path_filter, seeds):
    """Đi theo link từ trang chủ, dùng khi sitemap không bao phủ hết site."""
    start = seeds or [f"https://{domain}/"]
    seen, queue, found = set(), deque(start), []
    while queue and (not limit or len(found) < limit):
        batch = [queue.popleft() for _ in range(min(20, len(queue)))]
        batch = [u for u in batch if u.rstrip("/") not in seen]
        for u in batch:
            seen.add(u.rstrip("/"))
        if not batch:
            continue
        with ThreadPoolExecutor(max_workers=10) as ex:
            for u, final, links, err in ex.map(lambda x: fetch(x, True), batch):
                if err:
                    continue
                found.append(u)
                for l in links:
                    if l.rstrip("/") in seen or blocked(l, disallow):
                        continue
                    if path_filter and path_filter not in l:
                        continue
                    queue.append(l)
        print(f"  ...đã thấy {len(found)} trang, còn {len(queue)} trong hàng đợi")
    return found


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("domain", help="vd www.example.com, không có https://")
    ap.add_argument("--workers", type=int, default=12)
    ap.add_argument("--delay", type=float, default=0.0, help="nghỉ giữa request, giây")
    ap.add_argument("--limit", type=int, default=0, help="giới hạn số URL, 0 là không giới hạn")
    ap.add_argument("--path", default="", help="chỉ lấy URL chứa chuỗi này, vd /blog/")
    ap.add_argument("--sitemap", default="", help="URL sitemap cụ thể")
    ap.add_argument("--urls", default="", help="file chứa danh sách URL, mỗi dòng 1 URL")
    ap.add_argument("--crawl", action="store_true", help="đi theo link thay vì chỉ dựa sitemap")
    ap.add_argument("--ignore-robots", action="store_true")
    ap.add_argument("--out", default="graph.json")
    a = ap.parse_args()
    domain = a.domain.replace("https://", "").replace("http://", "").strip("/")

    disallow, declared = load_robots(domain)
    if a.ignore_robots:
        disallow = []
    print(f"[1/3] robots.txt: {len(disallow)} luật Disallow, {len(declared)} sitemap khai báo")

    seeds = []
    if a.urls:
        seeds = [l.strip() for l in open(a.urls) if l.strip().startswith("http")]
        print(f"      nạp {len(seeds)} URL từ {a.urls}")

    fetch = make_fetcher(domain, a.delay)
    urls = collect_sitemap_urls(domain, a.path, a.limit, a.sitemap, declared)
    print(f"      sitemap cho {len(urls)} URL")
    if a.crawl:
        print("      đi theo link để tìm thêm ...")
        urls += bfs_discover(domain, fetch, disallow, a.limit, a.path, seeds or urls[:50])
    urls += seeds

    out, seen = [], set()
    for u in urls:
        k = u.rstrip("/")
        if k in seen or blocked(u, disallow) or SKIP_EXT.search(u):
            continue
        seen.add(k)
        out.append(u)
    urls = out[:a.limit] if a.limit else out
    if not urls:
        print("  không tìm được URL nào. Site có thể chặn bot, hoặc không có sitemap.")
        print(f"  thử mở https://{domain}/robots.txt trên trình duyệt xem site khai sitemap ở đâu.")
        sys.exit(1)
    print(f"      tổng {len(urls)} URL sau khi lọc robots và trùng lặp")

    print(f"[2/3] crawl với {a.workers} luồng ...")
    graph, redirected, failed = {}, [], defaultdict(int)
    t0 = time.time()
    with ThreadPoolExecutor(max_workers=a.workers) as ex:
        for i, (u, final, links, err) in enumerate(ex.map(fetch, urls), 1):
            if err:
                failed[err] += 1
            elif final.rstrip("/") != u.rstrip("/"):
                redirected.append(u)            # stub 301, loại khỏi phân tích
            else:
                graph[u.rstrip("/")] = links
            if i % 100 == 0 or i == len(urls):
                el = time.time() - t0
                print(f"  {i}/{len(urls)}  {el:.0f}s  ({el/i:.2f}s/URL)")
    if failed:
        print("  lỗi:", dict(failed))
    print(f"  {len(redirected)} stub 301 đã loại, {len(graph)} trang thật")
    if not graph:
        print("  không trang nào đọc được, nhiều khả năng site chặn crawl. Dừng.")
        sys.exit(1)

    print("[3/3] xếp hạng ...")
    pages = set(graph)
    inb = defaultdict(set)
    for s, ds in graph.items():
        for t in ds:
            if t in pages:
                inb[t].add(s)
    N = len(pages)
    rows = sorted(((len(inb[u]), len(graph[u]), u) for u in graph), reverse=True)
    print(f"\n{'IN':>5} {'%':>5} {'OUT':>5}  PATH   (trên {N} trang)")
    for r in rows[:30]:
        flag = "  <= co ve la link template" if r[0] > 0.3 * N else ""
        print(f"{r[0]:>5} {100*r[0]/N:>4.0f}% {r[1]:>5}  {r[2].replace('https://'+domain,'')}{flag}")

    orph = [r for r in rows if r[0] == 0]
    print(f"\n{len(orph)} trang không có inbound nội bộ ({100*len(orph)/N:.0f}%), 15 ví dụ:")
    for r in orph[:15]:
        print(f"  OUT={r[1]:<4} {r[2].replace('https://'+domain,'')}")

    json.dump({
        "domain": domain,
        "crawled_at": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        "sitemap_urls": len(urls),
        "pages": len(graph),
        "robots_disallow": disallow,
        "redirect_stubs": redirected,
        "errors": dict(failed),
        "graph": {k: sorted(v) for k, v in graph.items()},
    }, open(a.out, "w"), indent=1)
    print(f"\nđã lưu {a.out} ({len(graph)} trang). Gửi file này đi là phân tích tiếp được.")


if __name__ == "__main__":
    main()
