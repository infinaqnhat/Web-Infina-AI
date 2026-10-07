# Teardown cụm pillar của đối thủ: đọc cấu trúc content từ chính site họ

**Ngày soạn: 2026-10-07.** File này trả lời đúng 1 câu hỏi: *cho 1 domain đối thủ, làm sao dựng lại
bản đồ pillar + cluster của họ mà không cần tool trả phí.*

Bổ sung cho `content-strategy-framework.md` (đi từ data keyword đến content plan cho site MÌNH).
File này đi hướng ngược lại: đọc cấu trúc đã có sẵn của NGƯỜI KHÁC, rồi dùng nó để tìm gap.

**Lưu ý về nguồn**: phần khung phương pháp (Bước 0-6) ổn định theo thời gian. Riêng các con số
benchmark ở Bước 4 là tổng hợp ngành tại 10/2026, không phải ranking factor Google công bố, nên
dùng để so sánh tương đối giữa các đối thủ chứ đừng coi là ngưỡng pass/fail. Xem mục Nguồn cuối file.

---

## Nguyên tắc cốt lõi

**Đừng đọc menu, tiêu đề hay breadcrumb của đối thủ để đoán cụm. Đọc internal link graph của họ.**

Navigation phản ánh cách phòng marketing muốn kể chuyện. Internal link phản ánh cách họ thật sự dồn
link equity. Hai thứ này lệch nhau thường xuyên, và cái thứ hai mới là thứ Google đọc.

Hệ quả thực tế: trang pillar thật của 1 site nhiều khi **không nằm trên menu**, và trang nằm chễm
chệ trên menu nhiều khi chỉ là landing page không ai link tới.

---

## Bước 0: Chọn đúng đối thủ trước khi crawl

Lọc còn 3-5 đối thủ tìm kiếm thật, theo công thức: 1 market leader + 2 ngang cơ + 1 mới nổi.

**Loại khỏi danh sách**: Wikipedia, site tin tức tổng hợp, aggregator (Capterra, G2, Clutch...).
Chúng rank bằng domain authority chứ không bằng cấu trúc cụm, nên teardown không học được gì.

Dấu hiệu chọn đúng: đối thủ đó xuất hiện lặp lại ở top 10 của **nhiều** keyword trong cụm mình nhắm,
không phải chỉ 1 keyword.

---

## Bước 1: Lấy toàn bộ bản đồ URL

Thử theo thứ tự, dừng ở cái nào chạy được:

```bash
# 1. Sitemap index (hay gặp nhất)
curl -sS https://<domain>/sitemap_index.xml
curl -sS https://<domain>/post-sitemap.xml
curl -sS https://<domain>/sitemap.xml

# 2. Nếu robots.txt khai chỗ khác
curl -sS https://<domain>/robots.txt | grep -i sitemap
```

Nếu đối thủ chạy WordPress, **ưu tiên REST API** vì nó trả về category và ngày đăng luôn, đỡ phải
crawl từng trang để biết phân loại:

```bash
curl -sS "https://<domain>/wp-json/wp/v2/posts?per_page=100&page=1&_fields=id,slug,link,title,categories,date"
curl -sS "https://<domain>/wp-json/wp/v2/categories?per_page=100&_fields=id,name,count"
```

**Tách theo folder trước khi làm gì khác.** `/blog/`, `/guides/`, `/resources/`, `/learn/` thường đã
là ranh giới cụm do chính đối thủ tự vạch. Nếu site có folder rõ ràng, một nửa công việc gom cụm đã
xong miễn phí.

---

## Bước 2: Dựng internal link graph và nhận diện pillar

Đây là bước quan trọng nhất, và là bước không có tool miễn phí nào làm thay.

**Pillar = trang có nhiều inbound internal link nhất, nằm nông trong cây URL, và link ra nhiều trang
con nhất.** Ba tín hiệu này phải cùng xuất hiện. Chỉ 1 trong 3 thì chưa đủ kết luận.

```python
# teardown.py, chạy: python3 teardown.py <domain>
import re, sys, time, urllib.request
from collections import defaultdict

DOMAIN = sys.argv[1]
UA = {"User-Agent": "Mozilla/5.0"}

def get(url):
    return urllib.request.urlopen(
        urllib.request.Request(url, headers=UA), timeout=30
    ).read().decode("utf-8", "ignore")

# 1. URL list từ sitemap
xml = get(f"https://{DOMAIN}/post-sitemap.xml")
urls = re.findall(r"<loc>([^<]+)</loc>", xml)
print(f"{len(urls)} URL")

# 2. Fetch từng trang, lấy internal link
outbound = {}
for i, u in enumerate(urls):
    try:
        html = get(u)
    except Exception:
        continue
    body = re.split(r"<main|<article", html, 1)[-1]          # bỏ bớt header/nav
    body = re.split(r"<footer", body, 1)[0]
    links = set(re.findall(rf'href="(https?://{re.escape(DOMAIN)}/[^"#?]*)"', body))
    outbound[u] = {l.rstrip("/") for l in links} - {u.rstrip("/")}
    time.sleep(0.4)                                           # lịch sự, tránh bị chặn

# 3. Đếm ngược
inbound = defaultdict(set)
for src, dsts in outbound.items():
    for d in dsts:
        inbound[d].add(src)

rows = []
for u in urls:
    k = u.rstrip("/")
    depth = k.replace(f"https://{DOMAIN}", "").strip("/").count("/")
    rows.append((len(inbound[k]), len(outbound.get(u, [])), depth, k))

print(f"\n{'IN':>4} {'OUT':>4} {'DEPTH':>5}  URL")
for r in sorted(rows, reverse=True)[:40]:
    print(f"{r[0]:>4} {r[1]:>4} {r[2]:>5}  {r[3]}")
```

**Đọc kết quả:**

| Hình dạng | Nghĩa là gì |
|---|---|
| IN cao, OUT cao, DEPTH thấp | Pillar thật |
| IN cao, OUT thấp | Trang rank tốt nhưng không phân phối link equity, cụm chưa khép |
| IN thấp, OUT cao | Trang index/listing, không phải pillar |
| IN = 0 | **Trang mồ côi.** Đây là điểm yếu lớn nhất của đối thủ, xem Bước 6 |

### Sáu cái bẫy khi đọc con số này

**1. Phải cắt header/nav/footer trước khi đếm.** Nếu không, mọi trang trong menu sẽ có inbound bằng
đúng tổng số trang và con số mất hết ý nghĩa. Đoạn `re.split` ở trên là bản tối giản, site nào không
dùng `<main>`/`<article>` thì phải tự tìm selector khác.

**2. Sitemap thường vẫn liệt kê URL đã 301.** Đây là bẫy nguy hiểm nhất vì nó tạo ra mồ côi giả.
URL đã redirect sẽ cho `IN=0` (không ai link tới nó nữa, đúng) nhưng `OUT` lại **bằng đúng OUT của
trang đích**, vì crawler đi theo redirect rồi đọc nội dung trang đích. Dấu hiệu nhận ra: một nhóm
URL cùng có `IN=0` và `OUT` trùng khít với `OUT` của một trang pillar nào đó trong danh sách.
Cách xử lý: so URL cuối sau redirect với URL gốc, lệch thì loại khỏi phân tích.

```python
req = urllib.request.Request(u, headers=UA)
with urllib.request.urlopen(req, timeout=30) as r:
    final = r.geturl()
if final.rstrip("/") != u.rstrip("/"):
    continue        # stub 301, bỏ qua
```

**3. Cột DEPTH chỉ có nghĩa khi site dùng folder.** Blog phẳng kiểu `/<slug>/` sẽ cho DEPTH = 0 ở
mọi dòng, lúc đó chỉ đọc IN và OUT.

**5. Link template trong sidebar và CTA sẽ chiếm hết top bảng.** Cắt header/nav/footer là chưa đủ,
vì nhiều theme nhét block CTA ngay trong vùng `<main>`. Chạy thật trên `tuscanaproperties.com`
(1.466 trang), 6 vị trí dẫn đầu đều là loại này: `/contact` xuất hiện trên 97% số trang,
`/sellers/our-books` và `/sellers/move-for-free` trên 61%.

Cách nhận ra: tính **tỷ lệ số trang có link tới nó**. Trên 50% thì chắc chắn là sitewide. Nhưng
**đừng dùng một ngưỡng cố định**, đã kiểm chứng là không có con số nào đúng cho mọi site:

| Ngưỡng | Trên site 1.466 trang | Trên site 130 trang |
|---|---|---|
| 20% | Lọc đúng cả 6 CTA | **Loại nhầm pillar thật** (47/130 = 36%) |
| 50% | **Để lọt** CTA ở mức 27% | Giữ đúng pillar |

Site càng nhỏ thì pillar thật càng dễ vượt ngưỡng %. Cách làm đúng: tính tỷ lệ, sắp xếp giảm dần,
rồi **nhìn 10 dòng đầu và tự loại bằng mắt** những trang rõ ràng là CTA, liên hệ, hoặc pháp lý
(`/contact`, `/privacy-policy`, `/terms`, trang đăng ký, trang tải ebook). Mất 30 giây và không sai.

**6. Đếm link là chưa đủ, phải xem link nằm Ở ĐÂU trong trang.** Theo patent reasonable surfer của
Google (US8117209B1), trọng số mỗi link tính theo xác suất người đọc bấm vào, dựa trên vị trí link
trong tài liệu, vị trí trong danh sách link, anchor text và mức liên quan. Nghĩa là 20 link nằm
giữa các đoạn văn mạnh hơn hẳn 20 link dồn vào box cuối bài, dù script đếm ra cùng con số.

Ba mức, đừng gộp mức 2 với mức 3:

| Mức | Vị trí | Giá trị |
|---|---|---|
| 1 | Giữa đoạn văn, ngay chỗ nhắc chủ đề con | Cao nhất |
| 2 | Box "Related Reading" cuối bài, anchor mô tả | Trung bình |
| 3 | Nav, sidebar, footer, boilerplate lặp mọi trang | Thấp nhất |

Cách đo tỷ lệ này cho 1 site bất kỳ, chạy trên nội dung đã fetch:

```python
import re
TAIL = re.compile(r"<h2[^>]*>\s*(Related Reading|Final Thoughts|You might also)", re.I)
def split_links(html, domain):
    m = TAIL.search(html)
    cut = m.start() if m else len(html)
    pat = rf'href="https?://{re.escape(domain)}/[^"]*"'
    return len(re.findall(pat, html[:cut])), len(re.findall(pat, html[cut:]))
```

**Ngưỡng tham chiếu: tối thiểu 50% link nội bộ nằm trong thân bài.** Đo trên 113 bài của
`infina.ai/news` ngày 07/10/2026: chỉ 41% nằm trong thân bài, 59% dồn vào Related Reading và Final
Thoughts. Khi soi đối thủ, một site có nhiều link nhưng toàn nằm ở boilerplate thì yếu hơn con số
thô gợi ý, và ngược lại.

Lưu ý mục lục (TOC) không thuộc nhóm này. Nó thường là anchor nhảy trong cùng trang nên không
truyền equity sang trang khác, trừ khi link thẳng tới trang cluster.

**4. Trang category và tag archive sẽ leo lên đầu bảng.** Mọi bài đều link về category của nó, nên
archive luôn có inbound cao nhất site mà không phải pillar nội dung. Đo thật trên `infina.ai/news`:
nếu không lọc, 3 vị trí dẫn đầu là `/crm-software/`, `/ai-chatbot/`, `/real-estate-websites/`, toàn
archive. **Cách lọc: chỉ xếp hạng những URL có mặt trong sitemap bài viết**, bỏ mọi URL không nằm
trong tập đó.

---

## Bước 2b: Khi site đối thủ lớn

### Script chạy lâu bao lâu

Đo thật trên môi trường này, 24 URL mẫu:

| Cách chạy | Tốc độ | So với tuần tự |
|---|---|---|
| Tuần tự + `sleep(0.4)` (script ở trên) | 2,09 s/URL | 1x |
| 8 luồng | 0,25 s/URL | 6,7x |
| 16 luồng | 0,18 s/URL | 9,2x |

Quy ra thời gian chạy:

| Số URL | Script tuần tự | 12 luồng |
|---|---|---|
| 150 | ~5 phút | ~25 giây |
| 1.000 | ~35 phút | ~3,5 phút |
| 5.000 | ~3 giờ | ~17 phút |
| 20.000 | ~12 giờ | ~1 giờ |
| 100.000 | ~2,5 ngày | ~6 giờ |

Mốc thực tế: **dưới 2.000 URL thì script tuần tự vẫn dùng được. Trên mức đó phải chạy song song.
Trên 20.000 URL thì đừng crawl hết, xem phần lấy mẫu bên dưới.**

### Bản song song, có lọc redirect và cache

**Bản dùng thật nằm ở `wordpress-mcp/scripts/competitor_teardown.py`** (chỉ thư viện chuẩn, không
cần cài gì), đã gộp đủ cả 4 bẫy ở trên, tự dò sitemap qua `robots.txt`, đi đệ quy sitemap index, và
xử lý được cả WordPress cài trong subfolder:

```bash
python3 competitor_teardown.py www.example.com
python3 competitor_teardown.py www.example.com --path /blog/ --workers 6
python3 competitor_teardown.py www.example.com --sitemap https://www.example.com/custom-sitemap.xml
```

Bản rút gọn dưới đây giữ lại để hiểu logic:

```python
# fast.py, chay: python3 fast.py <domain>
import json, re, sys, time, urllib.request
from concurrent.futures import ThreadPoolExecutor

DOMAIN, WORKERS, CACHE = sys.argv[1], 12, "graph.json"
UA = {"User-Agent": "Mozilla/5.0"}
LINK = re.compile(rf'href="(https?://{re.escape(DOMAIN)}/[^"#?]*)"')

def fetch(u):
    try:
        req = urllib.request.Request(u, headers=UA)
        with urllib.request.urlopen(req, timeout=30) as r:
            final, html = r.geturl(), r.read().decode("utf-8", "ignore")
    except Exception:
        return u, None, set()
    body = re.split(r"<main|<article", html, 1)[-1]
    body = re.split(r"<footer", body, 1)[0]
    return u, final, {l.rstrip("/") for l in LINK.findall(body)}

xml = urllib.request.urlopen(
    urllib.request.Request(f"https://{DOMAIN}/post-sitemap.xml", headers=UA)).read().decode()
urls = re.findall(r"<loc>([^<]+)</loc>", xml)

t = time.time()
out, redirected = {}, []
with ThreadPoolExecutor(max_workers=WORKERS) as ex:
    for u, final, links in ex.map(fetch, urls):
        if final is None:
            continue
        if final.rstrip("/") != u.rstrip("/"):
            redirected.append(u)          # stub 301, loai khoi phan tich
            continue
        out[u.rstrip("/")] = links - {u.rstrip("/")}
el = time.time() - t
print(f"{len(urls)} URL trong {el:.1f}s, {len(redirected)} stub 301 da loai, {len(out)} trang that")
json.dump({k: sorted(v) for k, v in out.items()}, open(CACHE, "w"))
```

Ba thứ bản này thêm so với bản tối giản: **song song 12 luồng**, **tự loại stub 301** (bẫy số 2), và
**cache ra `graph.json`** để mọi phân tích sau đó chạy offline trong vài giây, không phải crawl lại.

Giữ `WORKERS` ở mức 8-16. Cao hơn dễ bị rate-limit hoặc chặn IP, mà cũng không nhanh thêm bao nhiêu.
Nếu đối thủ có Cloudflare, hạ xuống 4-6 và thêm `time.sleep` nhỏ.

### Site quá lớn thì lấy mẫu, đừng crawl hết

Mấu chốt: **để nhận diện pillar, ta chỉ cần THỨ HẠNG tương đối, không cần con số tuyệt đối.** Crawl
20% số trang thì mọi inbound count chỉ còn ~20%, nhưng trang nào đứng đầu thì vẫn đứng đầu.

Đo thật trên 129 trang của `infina.ai/news`, mỗi tỷ lệ chạy 60 lần lấy mẫu ngẫu nhiên:

| Tỷ lệ mẫu | Đoán đúng pillar số 1 | Trùng top 10 | Trùng top 5 |
|---|---|---|---|
| 50% | 100% | 7,5/10 | 3,5/5 |
| 30% | 100% | 6,8/10 | 3,2/5 |
| 20% | 98% | 6,4/10 | 3,0/5 |
| 10% | 83% | 5,0/10 | 2,5/5 |

Kết luận dùng được ngay: **mẫu 20-30% là đủ để chỉ ra pillar chính gần như chắc chắn**, nhưng không
đủ để xếp hạng chính xác nhóm giữa. Với teardown đối thủ thì vậy là đủ, vì ta cần biết trang nào là
pillar chứ không cần biết trang xếp thứ 4 hay thứ 6.

Hai cách thu hẹp khác, ưu tiên dùng trước khi lấy mẫu ngẫu nhiên:

1. **Crawl đúng 1 folder.** Nếu chỉ quan tâm cụm CRM của đối thủ thì crawl `/blog/crm/` thay vì cả
   site. Chính xác tuyệt đối trong phạm vi đó, và thường nhanh hơn lấy mẫu toàn site.
2. **Lọc sitemap theo ngày.** Hầu hết sitemap có `<lastmod>`. Bài từ 3 năm trước hiếm khi là pillar
   đang được nuôi, bỏ bớt cho nhẹ.

---

## Bước 3: Gom cụm theo hub

Mỗi URL thuộc về pillar mà nó **link lên**. Gom xong sẽ ra 1 trong 3 hình:

1. **Cụm khép kín**: pillar ↔ cluster link 2 chiều đầy đủ. Khó đánh trực diện.
2. **Cụm 1 chiều**: cluster link lên pillar nhưng pillar không link xuống. Rất phổ biến. Nghĩa là
   cụm được xây dần chứ không có kế hoạch, và link equity chảy 1 hướng.
3. **Chùm rời rạc**: nhiều trang cùng chủ đề nhưng không trang nào link nhau. Đây không phải cụm,
   chỉ là 1 đống bài. Đối thủ dạng này dễ vượt nhất.

Nếu 2 trang cùng chủ đề mà cả hai đều có IN cao và không link nhau, khả năng cao **đối thủ đang tự
cannibalize**. Ghi lại, đó là cơ hội.

---

## Bước 4: Chấm chất lượng cụm theo benchmark

| Tín hiệu | Ngưỡng tham chiếu (10/2026) |
|---|---|
| **Link nội bộ, tính theo tỷ lệ** | **3–5 mỗi 1.000 chữ**, nới tới 8 cho bài dài |
| Pillar 3.000–5.000 chữ quy ra | 20–40 link |
| Số cluster trên 1 pillar | 5–15, khởi động 5–7, mở rộng tới 8–15 |
| **Mỗi bài cluster link ra** | **pillar + 2–3 bài cluster khác** |
| Độ dài pillar | 3.000–5.000 từ |
| Mỗi subtopic trong pillar | 100–200 từ tóm tắt rồi link ra bài sâu |
| Anchor text cluster → pillar | chứa keyword mục tiêu của pillar |
| Link 2 chiều | bắt buộc chiều cluster → pillar |
| Ngưỡng AI citation | 5+ trang liên kết nhau trong cùng 1 chủ đề |

⚠️ **Luôn chia số link cho số chữ trước khi đánh giá.** Con số tuyệt đối 20-40 chỉ đúng cho pillar
dài 3.000-5.000 chữ. Pillar 1.800 chữ mà có 20 link là **nhiều**, không phải vừa. Đã mắc lỗi này
thật ngày 07/10/2026 khi soi chính site mình.

**Google không có giới hạn số link trên 1 trang.** Quy tắc "100 link mỗi trang" bị trích rất nhiều
nhưng đã bỏ từ 2008, vốn là giới hạn kỹ thuật thời Googlebot chỉ tải khoảng 100KB đầu trang. Nên khi
thấy pillar của đối thủ có 30-40 link nội bộ **trên một bài 4.000 chữ**, đó là dấu hiệu hub khoẻ,
không phải spam.

Hai dòng in đậm là hai chỉ số phân biệt nhanh nhất giữa cụm có kiến trúc và một đống bài rời rạc.
Đo thật: `wiseagent.com` có **0 link cluster sang cluster** trên 250 bài blog, và 86% site mồ côi.

Dùng bảng này để **so sánh giữa các đối thủ**, không phải để chấm đỗ/trượt. Một đối thủ có 4 cụm đạt
chuẩn nguy hiểm hơn hẳn đối thủ có 12 cụm rời rạc.

**Cũng dùng bảng này để tự soi site mình.** Đo ngày 07/10/2026 trên `infina.ai/news` theo đúng tỷ
lệ: `best-crm-for-real-estate` 1.832 chữ với 20 link ra 10,9/1.000 (nhiều), `crm-pipeline-management`
1.682 chữ với 5 link ra 3,0/1.000 (thiếu). Nhưng kết luận quan trọng hơn con số link: chỉ 1 trong 8
pillar đạt 3.000 chữ, phần còn lại 1.200-1.800 chữ nên **đang là bài cluster dài chứ chưa phải
pillar**. Link ngang trung bình 1,23/bài so với chuẩn 2-3, chỉ 31% số bài đạt.

---

## Bước 5: Phân loại đối thủ trước khi quyết đánh hay né

Bước hay bị bỏ qua nhất, và là bước quyết định tốn bao nhiêu nguồn lực.

**Loại A, rank nhờ 1 asset outlier**: traffic dồn vào 1-2 URL, phần còn lại im lặng. Thường là 1 bài
cũ ăn backlink tốt. Cấu trúc cụm phía sau yếu hoặc không có.
→ Đánh được bằng 1 cụm chuyên sâu hẹp, không cần xây cả hệ thống.

**Loại B, rank nhờ mạng topical**: traffic trải đều trên 10-30 URL liên kết chặt.
→ Không có đường tắt. Phải xây cụm đối ứng, hoặc chọn nhánh con mà họ bỏ trống.

Cách phân biệt nhanh mà không cần tool traffic: nhìn phân bố IN ở Bước 2. Nếu 1 URL có IN gấp 5-10
lần trung bình và phần còn lại gần như bằng nhau ở mức thấp, đó là loại A.

---

## Bước 6: Tìm gap ở mức structural node, không phải keyword lẻ

Gap đáng khai thác **không phải** "thiếu từ khóa X" mà là "thiếu hẳn 1 nhánh subtopic".

Ba nguồn gap theo thứ tự giá trị:

1. **Nhánh vắng mặt hoàn toàn.** So cây cụm của họ với cây cụm của mình, tìm node không ai có. Giá
   trị cao nhất, cạnh tranh gần bằng 0.
2. **Pillar quá rộng.** Trang rank cho hàng trăm từ nhưng không trả lời sâu câu nào. Chen vào bằng
   bài hẹp và sâu hơn hẳn phần tương ứng trong pillar của họ.
3. **Trang mồ côi của họ** (IN = 0 ở Bước 2). Chủ đề họ đã xác nhận là đáng viết, nhưng chính họ
   không chống lưng bằng internal link. Viết lại tử tế kèm cụm đầy đủ là vượt được.

**Ưu tiên bằng ma trận volume × độ yếu đối thủ**, lấy high-value low-effort trước, nhắm intent hẹp
mà đối thủ vắng mặt hoàn toàn. Đừng bắt đầu từ node có volume cao nhất nếu đó cũng là node họ mạnh nhất.

---

## Hai cạm bẫy

**1. Đừng copy cấu trúc cụm của đối thủ 1:1.** Cụm của họ phục vụ ICP của họ. Bê nguyên về thường
chồng lên nội dung sẵn có của mình rồi tự cannibalize. Dùng teardown để tìm *chỗ trống*, không phải
để *sao chép bản đồ*.

**2. Thin cluster hại hơn không viết.** Nếu bài cluster không sâu hơn chính đoạn tóm tắt 100-200 từ
trong pillar, nó là cannibalization chứ không phải topical authority. Áp rule này cho cả việc đọc
đối thủ: đối thủ có 15 bài cluster mỏng yếu hơn đối thủ có 6 bài dày.

---

## Case thật trên site này

**Lần 1, audit 01/10/2026, Cụm 2 (CRM Software).** content-plan lúc đó ghi `#384` là pillar chính,
thuần tuý vì tiêu đề nghe "pillar hơn". Link graph cho thấy ngược lại:

- `#207` best-crm-for-real-estate: **15 inbound link sitewide**
- `#384` best-crm-software-real-estate-agents: **2 inbound link**

Đã đổi vai trò pillar sang `#207`, trỏ lại toàn bộ cluster, rồi merge `#384` vào `#207` kèm 301.

**Lần 2, chạy chính script trong file này ngày 07/10/2026 trên 142 URL.** Kết quả xác nhận cấu trúc
đã lành:

| Trang | IN | OUT |
|---|---|---|
| best-crm-for-real-estate (#207) | 51 | 21 |
| real-estate-website-builder (#546) | 27 | 15 |
| ai-crm-real-estate | 20 | 5 |

`#207` giờ có inbound gấp gần 2 lần pillar đứng thứ hai, đúng hình dạng pillar mong đợi.

**Và bẫy số 2 ở Bước 2 lộ ra ngay trong lần chạy này.** Script báo 8 URL có `IN=0`. Soát lại thì 7
trong số đó là **stub 301 đã merge** chứ không phải mồ côi thật, nhận ra được vì `OUT` của chúng
trùng khít với `OUT` của trang đích (ví dụ `best-crm-software-real-estate-agents` có OUT=21, bằng
đúng OUT của `#207`). Cái còn lại là trang index `/news` của blog. Tức là site hiện **không có mồ côi
thật nào**, nhưng nếu đọc vội con số thì sẽ kết luận ngược.

Bài học: **cùng 1 phương pháp dùng được cho cả site mình lẫn site đối thủ**, và chạy trên site mình
trước là cách rẻ nhất để phát hiện script đang đếm sai ở đâu, vì mình biết đáp án đúng.

---

## Nguồn

- [rankdots, 5-step framework to reverse-engineer competitor pages](https://rankdots.com/blog/competitor-reverse-engineering). Khung 5 bước, khái niệm Visibility Index và phân biệt outlier asset vs topical network
- [rankdots, analyze competitor topic coverage to find content gaps](https://rankdots.com/blog/competitive-analysis). Gom URL theo hub page, gap matrix ở mức structural node
- [digitalapplied, SEO content clusters 2026 topic authority guide](https://www.digitalapplied.com/blog/seo-content-clusters-2026-topic-authority-guide). Benchmark số cluster, độ dài pillar, ngưỡng AI citation
- [HubSpot, topic clusters the next evolution of SEO](https://blog.hubspot.com/marketing/topic-clusters-seo). Mô hình pillar-cluster gốc, quy tắc anchor text và link 2 chiều
- [Search Engine Land, Messy SEO Part 6: pillar pages and topic clusters](https://searchengineland.com/messy-seo-part-6-pillar-pages-and-topic-clusters-379169). Ghi chép triển khai thật, các lỗi hay gặp
