---
name: "news-to-cluster-article"
description: "Crawl tin tức mới theo 10 mảng, đối chiếu keyword trong Excel, check bài đã có trên WordPress (published/scheduled/draft), chọn tin phù hợp và viết cluster article đạt Rank Math ≥80/100. Dùng khi muốn viết bài cluster từ tin tức mới nhất."
---

# SKILL: Daily News → Cluster Article (Rank Math SEO)

## Mô tả
Crawl tin tức mới theo 10 mảng → kiểm tra bài đã có trên WordPress → đối chiếu keyword trong Excel → chọn tin phù hợp → viết và đăng cluster article lên WordPress đạt Rank Math ≥80/100. Toàn bộ chạy qua API, không cần browser.

---

## WordPress Connection

**Endpoint:** `https://infina.ai/news/wp-json/infina-mcp/v1/blog?key=<WP_MCP_KEY>` (key thật lưu ở account-level skill / secret store, KHÔNG commit vào repo)

**Protocol:** JSON-RPC 2.0 qua HTTPS POST

**Cần set trước khi chạy** (không hard-code key vào file này để tránh lộ secret khi commit): `WP_MCP_KEY`, `GROK_API_KEY`, `FREEIMAGE_API_KEY`. Bản skill cài trong account Claude (`~/.claude/skills/news-to-cluster-article/`) giữ giá trị thật.

```python
import os, requests, base64, re, json

WP_URL = f"https://infina.ai/news/wp-json/infina-mcp/v1/blog?key={os.environ['WP_MCP_KEY']}"
GROK_KEY = os.environ["GROK_API_KEY"]
FREEIMAGE_KEY = os.environ["FREEIMAGE_API_KEY"]

def call(method, params):
    r = requests.post(WP_URL, json={
        "jsonrpc": "2.0",
        "id": 1,
        "method": "tools/call",
        "params": {"name": method, "arguments": params}
    }, timeout=60)
    result = r.json().get("result", {})
    content = result.get("content", [])
    text = content[0]["text"] if content else str(r.json())
    if result.get("isError"):
        raise Exception(f"{method} failed: {text}")
    return text
```

**Các method dùng được — đối chiếu trực tiếp với source code server tại `wordpress-mcp/infina-wp-mcp-server-snippet.php` trong repo `infinaqnhat/web-infina-ai` (ground truth, ưu tiên hơn cả test API vì đọc thẳng code PHP xử lý request):**

| Method | Params chính | Ghi chú |
|--------|-------------|---------|
| `list_posts` | `status` (array, optional — bỏ trống = lấy tất cả 5 trạng thái draft/publish/future/pending/private), `number` (int, mặc định 20 — **không có pagination, truyền số lớn như 200 để lấy hết**), `search` (string, optional) | Liệt kê bài viết |
| `create_post` | `title`*, `content`* (*bắt buộc), `status` (draft\|publish\|future\|pending\|private, mặc định draft), `date` (chỉ dùng khi status=future, format `"YYYY-MM-DD HH:MM:SS"` — **không phải ISO có chữ T**, và phải là thời điểm tương lai so với giờ server, nếu không server trả lỗi `past_date`), `excerpt`, `slug`, `categories` (array tên danh mục dạng string — WP tự tạo term mới nếu tên chưa tồn tại), `tags` (array string), `seo_title`, `seo_description`, `seo_focus_keyword`, `image_url`, `image_alt` | Tạo bài. **Không có tool xoá post** — cân nhắc kỹ trước khi tạo, kể cả status=draft |
| `update_post` | `post_id`* (bắt buộc) + tất cả field như `create_post` (chỉ truyền field muốn đổi, field không truyền giữ nguyên) | Sửa bài đã tồn tại (kể cả đổi status/date/category) — dùng thay vì workaround REST API/Application Password |
| `upload_media` | `image_url`* (bắt buộc, phải là https), `alt`, `title` | Tải ảnh về Media Library qua `media_sideload_image`, có chặn SSRF (server tự HEAD-check content-type phải là image/*, từ chối URL nội bộ) |
| `delete_media` | `media_id`* (bắt buộc) | Xoá vĩnh viễn 1 media/attachment (bỏ qua Trash). Không xoá được post |

**Response format chính xác của từng method** (lấy thẳng từ code PHP, dùng để viết regex parse post_id/media_id):

| Method | Response text (thành công) |
|--------|------|
| `list_posts` | mỗi bài 1 dòng: `#{id} [{status}] {title} ({date}) - {edit_url} \| {link}` — **không có field slug/focus_keyword riêng**, slug phải tự suy ra từ đoạn cuối `{link}`; bài `future` link dạng `?p={id}` (chưa có slug thật) |
| `create_post` | `Da tao bai ID {id} [status: {status}].{image_note} Sua: {edit_url} \| Xem: {link}` |
| `update_post` | `Da cap nhat bai ID {id} [status: {status}].{image_note} Sua: {edit_url} \| Xem: {link}` |
| `upload_media` | `Da tai anh. media_id: {id} \| source_url: {url}` |
| `delete_media` | `Da xoa han media ID {id} (ca file goc + cac ban resize).` |

`{image_note}` (chỉ xuất hiện khi có truyền `image_url`): `" Da gan anh dai dien."` nếu thành công, hoặc `" Luu y: tai anh dai dien that bai (<lý do>)."` nếu lỗi — **luôn check chuỗi này trong response `create_post`/`update_post` vì lỗi ảnh không làm fail cả request**, dễ bị bỏ sót nếu chỉ regex lấy post_id rồi coi là xong.

Khi lỗi (status/date sai, thiếu field bắt buộc...), server trả `isError: true` kèm message tiếng Việt không dấu (vd: `"status 'future' can 'date'..."`, `"'date' phai o tuong lai de len lich."`) — hàm `call()` ở trên đã tự raise Exception khi gặp `isError`, không cần tự check lại.

---

## Image Pipeline

**Grok API → freeimage.host → WP Media**

```python
def grok_image(prompt):
    r = requests.post(
        "https://api.x.ai/v1/images/generations",
        headers={"Authorization": f"Bearer {GROK_KEY}", "Content-Type": "application/json"},
        json={"model": "grok-imagine-image", "prompt": prompt, "n": 1},
        timeout=90
    )
    return r.json()["data"][0]["url"]

def upload_to_freeimage(url):
    img_data = requests.get(url, timeout=30).content
    b64 = base64.b64encode(img_data).decode()
    r = requests.post("https://freeimage.host/api/1/upload",
        data={"key": FREEIMAGE_KEY, "action": "upload", "source": b64, "format": "json"},
        timeout=30)
    return r.json()["image"]["url"]
```

Luồng: `grok_image(prompt)` → URL tạm → `upload_to_freeimage()` → public URL → `upload_to_wp()` → WP media URL.

Mỗi bài cần **4 ảnh**: HERO, STATS/DATA, DEMO, COMPARISON.

---

## Bước 1 — Crawl tin tức 7 ngày gần nhất

Dùng `WebSearch` tool để tìm tin mới cho từng mảng. Thay `YYYY-MM-DD` bằng ngày 7 ngày trước ngày chạy.

| # | Mảng | Search query |
|---|------|-------------|
| 1 | Real estate market trends | `real estate market news 2026 after:YYYY-MM-DD` |
| 2 | Mortgage & interest rates | `mortgage rates update 2026 after:YYYY-MM-DD` |
| 3 | PropTech / real estate tech | `proptech real estate technology news 2026 after:YYYY-MM-DD` |
| 4 | AI in real estate | `AI tools real estate agents 2026 after:YYYY-MM-DD` |
| 5 | CRM & sales automation | `CRM real estate automation 2026 after:YYYY-MM-DD` |
| 6 | Lead generation | `real estate lead generation news 2026 after:YYYY-MM-DD` |
| 7 | Agent business tips | `real estate agent business strategy 2026 after:YYYY-MM-DD` |
| 8 | Economic indicators | `housing market economic data 2026 after:YYYY-MM-DD` |
| 9 | New construction & housing supply | `new home construction housing supply 2026 after:YYYY-MM-DD` |
| 10 | Rental market | `rental market trends 2026 after:YYYY-MM-DD` |

Top 3–5 tin mỗi mảng. **Output:** Bảng markdown — Mảng | Tiêu đề | URL | Ngày | Tóm tắt 1 câu.

---

## Bước 2 — Kiểm tra bài đã tồn tại trên WordPress

Pull toàn bộ bài đang có (published + scheduled/future + draft/...) trước khi chọn keyword, để tránh viết trùng. `list_posts` không phân trang — gọi 1 lần với `number` đủ lớn là lấy hết (tổng số bài hiện tại ~26, nhưng cứ để dư).

```python
import re

def get_all_posts():
    resp = call("list_posts", {"number": 500})  # bỏ trống "status" = lấy tất cả trạng thái
    posts = []
    line_re = re.compile(
        r'^#(\d+)\s+\[(\w+)\]\s+(.*?)\s+\(([\d-]+ [\d:]+)\)\s+-\s+(\S+)\s+\|\s+(\S+)$'
    )
    for line in resp.strip().split("\n"):
        m = line_re.match(line.strip())
        if not m:
            continue
        post_id, status, title, date, edit_url, public_url = m.groups()
        slug = public_url.rstrip("/").split("/")[-1]
        if slug.startswith("?p="):  # bài future/chưa có slug thật, dùng title thay
            slug = ""
        posts.append({
            "id": post_id, "status": status, "title": title,
            "date": date, "slug": slug, "public_url": public_url,
        })
    return posts

posts = get_all_posts()
```

**Dedup logic — skip keyword nếu:** (KHÔNG có field `focus_keyword` trong response của `list_posts`, nên chỉ dedup được theo title/slug — không dựa vào focus keyword của bài cũ)

```python
def is_duplicate(candidate_slug, candidate_title, existing_posts):
    candidate_words = set(candidate_slug.replace("-", " ").split())
    candidate_title_words = set(candidate_title.lower().split())

    for p in existing_posts:
        existing_slug_words = set(p["slug"].replace("-", " ").split()) if p["slug"] else set()
        existing_title_words = set(p["title"].lower().split())

        # Slug overlap >60%
        if existing_slug_words:
            overlap = len(candidate_words & existing_slug_words)
            if overlap / max(len(candidate_words), 1) > 0.6:
                return True, f"Slug overlap với [{p['status']}] #{p['id']} {p['title']}"

        # Title overlap cao (đề phòng bài future chưa có slug thật)
        title_overlap = len(candidate_title_words & existing_title_words)
        if title_overlap / max(len(candidate_title_words), 1) > 0.6:
            return True, f"Title overlap với [{p['status']}] #{p['id']} {p['title']}"

    return False, None
```

**Output Bước 2:** Danh sách keyword bị loại + lý do. Chỉ keyword pass dedup mới vào Bước 3.

---

## Bước 3 — Đọc keyword groups từ Excel

Đọc file `AI_SalesX_Customer_Segments_Content_Pillars - Copy.xlsx`, lấy các focus keyword **chưa bị loại ở Bước 2**.

Từ file Excel extract:
- Focus keyword của từng bài chưa publish
- Pillar page tương ứng (để xác định internal link target)

---

## Bước 4 — Map tin → keyword

*(Chỉ xét keyword đã pass dedup check)*

Với mỗi tin, đánh giá:

1. **Relevance (1–5):** Tin liên quan đến focus keyword nào?
2. **Angle:** Tin cung cấp dữ liệu/case study/xu hướng gì để làm hook?
3. **Pillar target:** Bài cluster sẽ link về pillar page nào?

Chọn **top 1 cặp** (tin + keyword) có relevance cao nhất và angle rõ ràng nhất để viết.

---

## Bước 5 — Viết cluster article

**Cấu trúc HTML bài viết:**

```
Intro paragraph — có focus keyword trong 100 từ đầu, context từ tin tức
[HERO image]
H2: Dữ liệu/tin tức mới — hook từ news, cite URL nguồn làm external link
[STATS image]
H2: Tại sao điều này quan trọng với real estate agents
H2: Giải pháp — [focus keyword] trong thực tế
[DEMO image]
H2: Top platforms/tools — external dofollow links tới tool websites
[COMPARISON image]
H2: Related reading — internal links (pillar page + 1 bài liên quan)
H2: Final Thoughts
```

**Rank Math SEO checklist — tự verify trước khi publish:**

```python
def check_seo(content, keyword):
    raw = re.sub(r'<[^>]+>', ' ', content)
    words = raw.split()
    kw_count = len(re.findall(re.escape(keyword), raw.lower()))
    density = (kw_count / len(words)) * 100
    ext_links = len(re.findall(r'href="https?://(?!infina\.ai)[^"]*"', content))
    int_links = len(re.findall(r'href="https?://infina\.ai[^"]*"', content))
    img_alts_with_kw = len([m for m in re.findall(r'alt="[^"]*"', content.lower())
                             if keyword in m])
    issues = []
    if density < 0.5:
        issues.append(f"Density too low: {density:.2f}% (need ≥0.5%)")
    if density > 2.5:
        issues.append(f"Density too high: {density:.2f}% (max 2.5%)")
    if ext_links < 1:
        issues.append("No external dofollow links")
    if int_links < 2:
        issues.append(f"Only {int_links} internal link(s) (need ≥2)")
    if img_alts_with_kw < 1:
        issues.append("No img alt contains focus keyword")
    return {
        "words": len(words),
        "kw_count": kw_count,
        "density": f"{density:.2f}%",
        "ext_links": ext_links,
        "int_links": int_links,
        "img_alts_with_kw": img_alts_with_kw,
        "ok": len(issues) == 0,
        "issues": issues
    }

# Dùng trước khi publish:
seo = check_seo(CONTENT, FOCUS_KW)
if not seo["ok"]:
    print("SEO issues:", seo["issues"])
    # Sửa CONTENT trước khi gọi create_post
```

**Nếu density thấp:** thêm các đoạn tự nhiên sử dụng focus keyword vào body sections.
**Nếu thiếu internal link:** thêm đoạn "Related reading" trước Final Thoughts với ≥2 link đến bài trong infina.ai/news.
**Nếu thiếu external link:** đảm bảo link tới URL nguồn tin và website các tool đề cập trong bài không có `rel="nofollow"`.

---

## Bước 6 — Publish lên WordPress

```python
resp = call("create_post", {
    "title": TITLE,
    "content": CONTENT,
    "status": "publish",  # dùng "draft" trước nếu muốn người duyệt xem lại trước khi publish thật
    "slug": SLUG,
    "seo_title": SEO_TITLE,
    "seo_description": SEO_DESC,
    "seo_focus_keyword": FOCUS_KW,
    "categories": ["AI Chatbot"],  # tên danh mục dạng string, KHÔNG phải ID số
    "tags": TAGS,
    "image_url": IMG["HERO"],
    "image_alt": f"{FOCUS_KW} 2026",
    # "date": "2026-08-10 12:00:00",  # CHỈ set khi status="future". Format "YYYY-MM-DD HH:MM:SS", KHÔNG phải ISO có chữ T
})

post_id_match = re.search(r'ID (\d+)', resp)  # khớp "Da tao bai ID {id} [status: ...]" từ source code server
if post_id_match:
    post_id = post_id_match.group(1)
    print(f"Published: Post ID {post_id}")
    print(f"URL: https://infina.ai/news/{SLUG}/")
if "that bai" in resp:  # image_note báo lỗi gắn ảnh đại diện dù post vẫn tạo thành công
    print("CANH BAO:", resp)
```

**Sửa bài sau khi publish** (đổi date/category/status...) dùng `update_post` trực tiếp qua cùng endpoint JSON-RPC — không cần WP Application Password hay REST API riêng:

```python
resp = call("update_post", {"post_id": 223, "date": "2026-08-10 12:00:00", "status": "future"})
```

---

## Bước 7 — Log kết quả

Append vào file `cluster_articles_log.md` sau mỗi lần chạy:

```markdown
| Date run | News source | Focus keyword | Post ID | Slug | SEO check | Status |
|----------|-------------|---------------|---------|------|-----------|--------|
| 2026-08-07 | [Title](URL) | real estate agent crm | 223 | real-estate-agent-crm-speed-to-lead | ✅ passed | Published |
```

---

## Slug rules (critical)

- Mỗi từ trong focus keyword phải xuất hiện trong slug
- Ví dụ: keyword `crm for real estate agents` → slug `crm-for-real-estate-agents` (phải có `for`)
- Singular ≠ plural: `agent` ≠ `agents`
- Tách keyword ra từng từ, check từng từ có trong slug không trước khi publish

---

## Output script file

Mỗi lần chạy tạo file: `article_cluster{N}_{slug}.py` lưu vào cùng folder với các script khác.

---

## Inputs cần thiết

| Input | Bắt buộc | Ghi chú |
|-------|----------|---------|
| Excel keyword file | Có | Đường dẫn tuyệt đối đến file xlsx |
| Publish date | Có | Theo schedule hiện tại |

