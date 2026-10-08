"""Tai 1 trang tren infina.ai/news ve va render LOCAL, nhung CO nap day du CSS ngoai.

Ly do ton tai: agent proxy khong cho Chromium mo truc tiep site that
(ERR_CERT_AUTHORITY_INVALID), nen phai luu HTML ra file roi mo bang file://.
Neu luu HTML tho thi moi <link rel=stylesheet> deu chet, va moi phep do
(tuong phan mau, tran ngang, computed style) deu sai.

Bay da sap mot lan, 08/10: regex bat <link> cu chi bat nhay kep, trong khi
WordPress xuat href='...' bang NHAY DON. Ket qua la 0 stylesheet duoc nap,
tu do suy ra "theme khong style table", roi sua mot bai thanh chu trang tren
nen sang. Luon kiem tra so stylesheet nap duoc != 0 truoc khi tin phep do.

Dung:
    from render_snapshot import snapshot
    p = snapshot("https://infina.ai/news/best-free-crm-for-real-estate-agents/")
    # roi mo file://{p} bang Chromium o viewport 375px
"""
import urllib.request, gzip, re, os, sys, hashlib

SITE = "https://infina.ai"


def fetch(u, ua="Mozilla/5.0"):
    rq = urllib.request.Request(u, headers={"User-Agent": ua, "Accept-Encoding": "gzip"})
    r = urllib.request.urlopen(rq, timeout=45)
    d = r.read()
    if r.headers.get("Content-Encoding") == "gzip":
        d = gzip.decompress(d)
    return d.decode("utf-8", "replace")


def snapshot(url, outdir="snap", strict=True):
    """Luu 1 ban chup co day du CSS ra file, tra ve duong dan tuyet doi."""
    os.makedirs(outdir, exist_ok=True)
    h = fetch(url)

    # BAT CA NHAY DON LAN NHAY KEP. Day la cho tung sai.
    links = re.findall(r"""<link[^>]+href=["']([^"']+\.css[^"']*)["']""", h)
    if strict and not links:
        raise RuntimeError("0 stylesheet tim duoc, regex hong hoac trang doi markup. "
                           "Dung tin bat ky phep do nao tren ban chup nay.")

    inline = ""
    for u in links:
        if u.startswith("//"):
            u = "https:" + u
        elif u.startswith("/"):
            u = SITE + u
        try:
            inline += "\n/* %s */\n" % u + fetch(u)
        except Exception as e:
            print("  BO QUA css %s: %s" % (u[:70], e), file=sys.stderr)

    # Nhung CSS vao <style> de khong phu thuoc mang khi render file://
    h = re.sub(r"""<link[^>]+href=["'][^"']+\.css[^"']*["'][^>]*>""", "", h)

    # Anh giu cho: giu ty le 16:9 de bo cuc gan that. PHAI chan be ngang,
    # neu khong chinh placeholder lam trang tran ngang va bi doc nham la loi cua site.
    PH = ("data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='1600' "
          "height='900'><rect width='1600' height='900' fill='%23ddd'/></svg>")
    h = re.sub(r'(<img[^>]+?)src="[^"]*"', r'\1src="%s"' % PH, h)
    h = re.sub(r'\ssrcset="[^"]*"', "", h)
    h = re.sub(r'<script[^>]*src="[^"]*"[^>]*></script>', "", h)

    guard = "\nimg,svg{max-width:100%;height:auto}\n"
    h = h.replace("</head>", "<style>%s%s</style></head>" % (inline, guard), 1)

    p = os.path.abspath(os.path.join(outdir, hashlib.md5(url.encode()).hexdigest()[:10] + ".html"))
    with open(p, "w", encoding="utf-8") as f:
        f.write(h)
    print("  nap %d stylesheet, %.1f KB CSS -> %s" % (len(links), len(inline) / 1024, p))
    return p


if __name__ == "__main__":
    for a in sys.argv[1:]:
        snapshot(a)
