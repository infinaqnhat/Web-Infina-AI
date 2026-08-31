---
name: "news-to-cluster-article"
description: "Crawl tin tức mới theo 10 mảng, đối chiếu keyword trong Excel và Google Sheet tracker, check bài đã có trên WordPress (published/scheduled/draft), chọn tin phù hợp và viết cluster article đạt Rank Math ≥80/100. Dùng khi muốn viết bài cluster từ tin tức mới nhất."
---

# SKILL: Daily News → Cluster Article (Rank Math SEO)

## Mô tả
Crawl tin tức mới theo 10 mảng → đối chiếu Google Sheet tracker (nguồn pillar/dedup chính thức) + WordPress → đối chiếu keyword trong Excel → chọn tin phù hợp → viết và đăng cluster article lên WordPress đạt Rank Math ≥80/100. Toàn bộ chạy qua API, không cần browser.

**Nguyên tắc cốt lõi:** bài viết từ tin tức (cluster/spoke) luôn target một keyword long-tail RIÊNG của nó (`FOCUS_KW`), khác với keyword của pillar page (`PILLAR_KW`) mà nó link về. Không bao giờ để 2 bài trong site cùng target 1 keyword — pillar page giữ vị trí rank cho keyword đầu (head term), cluster article chỉ mượn góc tin tức để nhắm long-tail và đẩy internal link/topical authority về pillar. Nguồn xác định keyword nào đã "có chủ" (Plan = pillar, News = cluster đã viết) là Google Sheet tracker ở Bước 2b — đọc lại sheet này mỗi lần chạy, và append 1 dòng mới vào đó sau khi publish (Bước 7).

**Lịch sử:** skill này có 2 nhánh phát triển từng tồn tại song song trên account (một nhánh tập trung compliance/tracker/anti-cannibalization, một nhánh tập trung chất lượng ảnh/category/rate-limit) — bản này là merge của cả hai, giữ lại phần tốt của từng bên.

---

## Category IDs

| ID | Tên | Dùng cho |
|----|-----|---------|
| 19 | AI Chatbot | Bài về chatbot, AI assistant, conversational AI, ISA |
| 85 | CRM Software | Bài về CRM, sales automation, lead management |
| 1  | News | Bài tin tức thời sự chung (không phải cluster real estate) |

Truyền category **bằng tên** vào param `categories` (KHÔNG phải ID số — WP MCP tự resolve tên category thành term, tạo mới nếu tên chưa tồn tại):
```python
"categories": ["CRM Software"]
"categories": ["AI Chatbot"]
```
Chọn category theo chủ đề bài: CRM/sales automation → "CRM Software", chatbot/AI assistant/ISA/compliance → "AI Chatbot".

---

## Publishing Rules (kiểm tra TRƯỚC KHI PUBLISH)

### Rule 1 — Chỉ 1 bài mỗi lần chạy, tối đa 3 bài/ngày
Skill này chỉ viết **đúng 1 bài** mỗi lần được gọi. Ngoài ra, trước khi publish, đếm số bài đã publish trong cùng ngày (giờ site) qua `list_posts` (JSON-RPC, KHÔNG dùng REST API `/wp-json/wp/v2/posts` không xác thực — REST API công khai không thấy được bài `draft`, dễ đếm thiếu):
```python
def count_posts_on_date(all_posts, target_date):
    """target_date: 'YYYY-MM-DD'. all_posts: list từ get_all_posts() ở Bước 2."""
    return sum(1 for p in all_posts if p["status"] == "publish" and p["date"].startswith(target_date))

count = count_posts_on_date(posts, "2026-08-11")
if count >= 3:
    print("STOP: Ngày này đã đủ 3 bài, dừng lại không publish thêm.")
```

### Rule 2 — Không trùng focus keyword / slug / pillar keyword
Xem Bước 2 (dedup WordPress) + Bước 2b (tracker sheet) + Bước 4 (pillar vs cluster).

### Rule 3 — Slug phải chứa từng chữ của FOCUS_KW
Xem Slug rules cuối file.

---

## WordPress Connection

**Endpoint:** `https://infina.ai/news/wp-json/infina-mcp/v1/blog?key=<WP_MCP_KEY>` (key thật lưu ở account-level skill / secret store, KHÔNG commit vào repo)

**Protocol:** JSON-RPC 2.0 qua HTTPS POST

**Cần set trước khi chạy** (không hard-code key vào file này để tránh lộ secret khi commit): `WP_MCP_KEY`, `GROK_API_KEY`, `FREEIMAGE_API_KEY`, `GEMINI_API_KEY` (tuỳ chọn, xem Image Pipeline). Bản skill cài trong account Claude giữ giá trị thật.

```python
import os, requests, base64, re, json

WP_URL = f"https://infina.ai/news/wp-json/infina-mcp/v1/blog?key={os.environ['WP_MCP_KEY']}"
GROK_KEY = os.environ.get("GROK_API_KEY")
FREEIMAGE_KEY = os.environ.get("FREEIMAGE_API_KEY")
GEMINI_KEY = os.environ.get("GEMINI_API_KEY")  # optional, xem Image Pipeline phương án B

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

**Các method dùng được — đối chiếu trực tiếp với source code server tại `wordpress-mcp/infina-wp-mcp-server-snippet.php` trong repo `infinaqnhat/web-infina-ai` (ground truth, ưu tiên hơn cả test API vì đọc thẳng code PHP xử lý request — các bảng tham số ở các bản skill cũ như `edit_date`, `filename`/`alt_text` là SAI, không tồn tại trên server thật):**

| Method | Params chính | Ghi chú |
|--------|-------------|---------|
| `list_posts` | `status` (array, optional — bỏ trống = lấy tất cả 5 trạng thái draft/publish/future/pending/private), `number` (int, mặc định 20 — **không có pagination, truyền số lớn như 500 để lấy hết**), `search` (string, optional) | Liệt kê bài viết. Đây là cách DUY NHẤT thấy được bài `draft` — REST API công khai không xác thực sẽ không thấy draft |
| `create_post` | `title`*, `content`* (*bắt buộc), `status` (draft\|publish\|future\|pending\|private, mặc định draft), `date` (chỉ dùng khi status=future, format `"YYYY-MM-DD HH:MM:SS"` — **không phải ISO có chữ T**, và phải là thời điểm tương lai so với giờ server, nếu không server trả lỗi `past_date`), `excerpt`, `slug`, `categories` (array tên danh mục dạng string — WP tự tạo term mới nếu tên chưa tồn tại), `tags` (array string), `seo_title`, `seo_description`, `seo_focus_keyword`, `image_url`, `image_alt` | Tạo bài. **Không có tool xoá post** — cân nhắc kỹ trước khi tạo, kể cả status=draft |
| `update_post` | `post_id`* (bắt buộc) + tất cả field như `create_post` (chỉ truyền field muốn đổi, field không truyền giữ nguyên) | Sửa bài đã tồn tại (kể cả đổi status/date/category/content). **Không có param `edit_date`** — chỉ cần truyền `date` là đủ |
| `upload_media` | `image_url`* (bắt buộc, phải là https), `alt`, `title` | Tải ảnh về Media Library qua `media_sideload_image`, có chặn SSRF (server tự HEAD-check content-type phải là image/*, từ chối URL nội bộ). **Không có param `filename`/`alt_text`** |
| `delete_media` | `media_id`* (bắt buộc) | Xoá vĩnh viễn 1 media/attachment (bỏ qua Trash). Không xoá được post |

**Response format chính xác của từng method** (lấy thẳng từ code PHP, dùng để viết regex parse post_id/media_id):

| Method | Response text (thành công) |
|--------|------|
| `list_posts` | mỗi bài 1 dòng: `#{id} [{status}] {title} ({date}) - {edit_url} \| {link}` — **không có field slug/focus_keyword riêng**, slug phải tự suy ra từ đoạn cuối `{link}`; bài `future` link dạng `?p={id}` (chưa có slug thật) |
| `create_post` | `Da tao bai ID {id} [status: {status}].{image_note} Sua: {edit_url} \| Xem: {link}` |
| `update_post` | `Da cap nhat bai ID {id} [status: {status}].{image_note} Sua: {edit_url} \| Xem: {link}` |
| `upload_media` | `Da tai anh. media_id: {id} \| source_url: {url}` |
| `delete_media` | `Da xoa han media ID {id} (ca file goc + cac ban resize).` |

`{image_note}` (chỉ xuất hiện khi có truyền `image_url`): `" Da gan anh dai dien."` nếu thành công, hoặc `" Luu y: tai anh dai dien that bai (<lý do>)."` nếu lỗi — **luôn check chuỗi này trong response `create_post`/`update_post`** vì lỗi ảnh không làm fail cả request.

Khi lỗi (status/date sai, thiếu field bắt buộc...), server trả `isError: true` kèm message tiếng Việt không dấu — hàm `call()` ở trên đã tự raise Exception khi gặp `isError`.

---

## Image Pipeline

**Phương án A (dùng mặc định, BẮT BUỘC) — Gemini `nano-banana` (`gemini-3.1-flash-lite-image`), $0.034/ảnh, native 1408×768, tự crop 16:9 bằng PIL:**
```python
import io
from PIL import Image

def nano_banana(prompt, model="gemini-3.1-flash-lite-image", retries=2):
    last_err = None
    for attempt in range(retries):
        try:
            r = requests.post(
                f"https://generativelanguage.googleapis.com/v1beta/models/{model}:generateContent?key={GEMINI_KEY}",
                json={"contents": [{"parts": [{"text": prompt}]}],
                      "generationConfig": {"responseModalities": ["IMAGE"]}},
                timeout=120,
            )
            r.raise_for_status()
            parts = r.json()["candidates"][0]["content"]["parts"]
            for p in parts:
                if "inlineData" in p:
                    img = Image.open(io.BytesIO(base64.b64decode(p["inlineData"]["data"])))
                    w, h = img.size
                    target = 16 / 9
                    if w / h < target - 0.05:
                        new_h = int(w / target); top = (h - new_h) // 2
                        img = img.crop((0, top, w, top + new_h))
                    elif w / h > target + 0.05:
                        new_w = int(h * target); left = (w - new_w) // 2
                        img = img.crop((left, 0, left + new_w, h))
                    buf = io.BytesIO(); img.save(buf, format="JPEG", quality=92)
                    return buf.getvalue()
            raise Exception(f"No image: {r.json()}")
        except Exception as e:
            last_err = e
    raise last_err

def stage_and_upload(img_bytes, alt, title):
    # nano_banana() trả về bytes ảnh — cần 1 URL public tạm trước khi WP media_sideload_image tải về.
    # Bước trung gian ưu tiên: freeimage.host. Nếu freeimage.host lỗi (400 "Internal upload error" —
    # đã gặp thực tế nhiều lần, có lần lỗi kéo dài cả 1 lần chạy chứ không chỉ transient), tự động
    # fallback sang litterbox.catbox.moe (không cần key, trả về URL image/jpeg trực tiếp, file tự xoá
    # sau 1h — đủ dùng vì WP tải về ngay lập tức). KHÔNG bỏ qua bước upload ảnh, KHÔNG báo lỗi cho user
    # nếu fallback thành công — chỉ báo nếu CẢ HAI đều lỗi.
    try:
        b64 = base64.b64encode(img_bytes).decode()
        r = requests.post("https://freeimage.host/api/1/upload",
            data={"key": FREEIMAGE_KEY, "action": "upload", "source": b64, "format": "json"},
            timeout=30)
        if r.status_code != 200:
            raise Exception(f"freeimage upload failed: {r.status_code} {r.text[:200]}")
        tmp_url = r.json()["image"]["url"]
    except Exception:
        r = requests.post("https://litterbox.catbox.moe/resources/internals/api.php",
            data={"reqtype": "fileupload", "time": "1h"},
            files={"fileToUpload": ("img.jpg", img_bytes, "image/jpeg")},
            timeout=30)
        if r.status_code != 200 or not r.text.strip().startswith("http"):
            raise Exception(f"Ca freeimage.host lan litterbox.catbox.moe deu loi: {r.status_code} {r.text[:200]}")
        tmp_url = r.text.strip()
    resp = call("upload_media", {"image_url": tmp_url, "alt": alt, "title": title})
    for part in resp.split("|"):
        part = part.strip()
        if part.startswith("source_url:"):
            return part.replace("source_url:", "").strip()
    raise Exception(f"Cannot parse upload_media response: {resp}")

wp_url = stage_and_upload(nano_banana(prompt), alt_text, title_text)
```

**Lưu ý các host tạm khác đã thử và KHÔNG dùng được** (qua agent proxy của môi trường này): `0x0.st` (connection reset ở tầng proxy), `catbox.moe` file-upload thường (412 "Invalid uploader"), `tmpfiles.org` (trả về trang HTML preview chứ không phải URL ảnh trực tiếp, fail HEAD content-type check của WP). Chỉ `litterbox.catbox.moe` (biến thể "temp file" của catbox) đã verify hoạt động — dùng đúng endpoint `https://litterbox.catbox.moe/resources/internals/api.php` như code trên, không phải endpoint catbox.moe thường.

**Nếu Gemini lỗi liên tục (kể cả sau retry trong hàm trên):** thử lại thêm 1 lần thủ công (gọi lại `nano_banana()`), nếu vẫn lỗi thì **báo cho user trong tóm tắt**, KHÔNG tự ý fallback sang Grok — Grok đã bị loại khỏi pipeline vì cho ra ảnh illustration/style không đồng nhất với chuẩn photorealistic + glossy/gradient hiện tại của site.

**Phương án B (đã ngừng dùng, chỉ còn giá trị lịch sử) — Grok API:** từng là default ban đầu (`grok-imagine-image` qua `api.x.ai`), đã bị thay thế hoàn toàn bằng Gemini nano-banana. Không dùng lại trừ khi có chỉ đạo mới rõ ràng từ user.

Mỗi bài cần **4 ảnh**: HERO, STATS/DATA, DEMO, COMPARISON. Ảnh HERO vẫn tạo và chèn vào content như bình thường; riêng **featured image/thumbnail dùng STATS** (xem Bước 6 — lý do: tránh lặp lại HERO photo giống nhau trên trang chủ).

---

## Image Prompt System — viết prompt sao cho ảnh không bị lỗi

Áp dụng cho cả phương án A và B — đây là kinh nghiệm thực tế để tránh lỗi tay thừa ngón, ánh mắt sai hướng, tỉ lệ khung sai, chữ bị vỡ trên màn hình trong ảnh AI-generated.

**4 nguyên tắc khi mô tả người trong ảnh (HERO/DEMO):**
1. **Camera angle trước tiên** — neo logic không gian trước khi mô tả chủ thể (vd: "over-the-shoulder shot, camera behind and slightly left of the subject")
2. **Gaze rõ ràng theo cấu trúc "ai → nhìn vào đâu → vật gì"** — xác nhận màn hình/vật hướng về phía chủ thể (vd: "eyes directed at laptop screen which faces her")
3. **Khoá vị trí tay cụ thể**, không mơ hồ (vd: "right hand resting on trackpad, left hand on keyboard home row" — không viết chung chung "using laptop")
4. **Luôn thêm negative guard ở cuối prompt**: `"no extra fingers, no floating objects, no readable text on screen, no garbled letters, no mirrored text, no screen facing away from user"`

**Lens cho ảnh 16:9:**
- HERO: dùng lens góc rộng `35mm` hoặc `24mm` — tránh `85mm f/1.4` (lens chân dung dễ ra khung dọc dù có crop PIL)
- Ảnh cận cảnh chi tiết (không phải HERO): `50mm`/`85mm` được

**Nội dung trên màn hình trong ảnh — KHÔNG bao giờ yêu cầu chữ cụ thể** (AI generate chữ trên màn hình luôn bị vỡ/sai):
```
✅ "CRM dashboard with colored bar charts and contact card grid"
✅ "warning UI with large yellow caution triangle icon"
❌ "screen showing text: Speed-to-Lead Report 2026"
```

**Ảnh diagram/infographic (STATS, COMPARISON)** — style đơn giản hơn, không cần rule người:
```
"{chủ đề}, clean flat infographic style, blue and white color palette, professional design, clear labels, high contrast, no people, no photorealistic elements"
```

**Bảng chọn role → cách viết prompt:**

| Role | Kiểu prompt | Lens (nếu có người) |
|------|------------|------|
| HERO | Có người + môi trường | 35mm wide, luôn dùng cho HERO |
| DEMO | Có người hoặc diagram tuỳ ngữ cảnh | 24-50mm |
| STATS | Diagram/infographic | — |
| COMPARISON | Diagram/infographic | — |

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

Top 3–5 tin mỗi mảng. Ưu tiên tin thực sự mới (trong tuần), có số liệu/dữ liệu cụ thể để làm hook, và **chưa trùng góc đã viết** (xem Bước 2/2b trước khi chốt). **Output:** Bảng markdown — Mảng | Tiêu đề | URL | Ngày | Tóm tắt 1 câu.

---

## Bước 2 — Kiểm tra bài đã tồn tại trên WordPress

Pull toàn bộ bài đang có (published + scheduled/future + draft/...) trước khi chọn keyword, để tránh viết trùng. `list_posts` không phân trang — gọi 1 lần với `number` đủ lớn là lấy hết.

```python
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

**Dedup logic — skip keyword nếu:** (KHÔNG có field `focus_keyword` trong response của `list_posts`, nên chỉ dedup được theo title/slug qua đây — kết hợp thêm Bước 2b để dedup theo focus keyword thật)

```python
def is_duplicate(candidate_slug, candidate_title, existing_posts):
    candidate_words = set(candidate_slug.replace("-", " ").split())
    candidate_title_words = set(candidate_title.lower().split())

    for p in existing_posts:
        existing_slug_words = set(p["slug"].replace("-", " ").split()) if p["slug"] else set()
        existing_title_words = set(p["title"].lower().split())

        if existing_slug_words:
            overlap = len(candidate_words & existing_slug_words)
            if overlap / max(len(candidate_words), 1) > 0.6:
                return True, f"Slug overlap với [{p['status']}] #{p['id']} {p['title']}"

        title_overlap = len(candidate_title_words & existing_title_words)
        if title_overlap / max(len(candidate_title_words), 1) > 0.6:
            return True, f"Title overlap với [{p['status']}] #{p['id']} {p['title']}"

    return False, None
```

**Output Bước 2:** Danh sách keyword bị loại + lý do. Chỉ keyword pass dedup mới vào Bước 3.

---

## Bước 2b — Đọc Tracker Sheet (nguồn PILLAR_KW chính thức, ưu tiên hơn Excel)

Google Sheet **"Infina News — Published Articles Tracker"** (`fileId: 1uVI1tPQxhTUk4qj8NWZSi-EReEwe2ZKIyIt_eQGeFOs`) là **nguồn sự thật sống** (live source of truth) về việc keyword nào đã "có chủ" — ưu tiên hơn Excel `Content Pillars (AIDA)` vì Excel chỉ là kế hoạch tĩnh, còn sheet này phản ánh đúng những gì đã thực sự publish. Đọc bằng `mcp__Google_Drive__read_file_content` (fileId ở trên) trước mỗi lần chọn keyword mới.

Cấu trúc cột: `#, Date, Title, URL, Focus Keyword, Type` — `Type` chỉ có 2 giá trị:

- **`Plan`** = bài pillar/cornerstone (thường là dạng "Best X for Real Estate", "What Is X?"...). Focus Keyword của các bài này là **PILLAR_KW đã bị chiếm** — tuyệt đối không dùng lại làm FOCUS_KW cho bài mới.
- **`News`** = bài cluster viết từ tin tức (chính là loại bài skill này tạo ra). Các bài News trước đó cũng đã dùng FOCUS_KW riêng của chúng rồi — cũng phải tránh trùng, y hệt như Plan.

**Lưu ý quan trọng:** tracker sheet có thể bị trễ so với thực tế trên WordPress nếu có automation khác cũng publish bài không log vào đây (đã từng xảy ra với các bài category "CRM Software" từ nhánh skill khác). Luôn coi Bước 2 (list_posts trực tiếp trên WP) là lớp dedup bắt buộc song song, KHÔNG chỉ dựa vào tracker sheet.

```python
def get_tracker_rows():
    text = read_file_content("1uVI1tPQxhTUk4qj8NWZSi-EReEwe2ZKIyIt_eQGeFOs")  # mcp__Google_Drive__read_file_content
    rows = []
    for line in text.split("\n"):
        cells = [c.strip() for c in line.strip("| \n").split("|")]
        if len(cells) != 6 or not cells[0].isdigit():
            continue  # bỏ header/separator markdown
        rows.append({
            "num": cells[0], "date": cells[1], "title": cells[2],
            "url": cells[3], "focus_keyword": cells[4].lower(), "type": cells[5],
        })
    return rows

tracker = get_tracker_rows()
used_keywords = {r["focus_keyword"] for r in tracker}          # TOÀN BỘ keyword đã dùng (Plan + News) — FOCUS_KW mới không được trùng bất kỳ cái nào
plan_rows = [r for r in tracker if r["type"].lower() == "plan"]  # nguồn PILLAR_KW + PILLAR_URL để link về
```

---

## Bước 3 — Đọc keyword groups từ Excel

Đọc file `AI_SalesX_Customer_Segments_Content_Pillars - Copy.xlsx` (trong repo: `wordpress-mcp/skills/news-to-cluster-article/keywords/AI_SalesX_Customer_Segments_Content_Pillars.xlsx`), dùng làm **nguồn tham khảo ý tưởng/chiến lược pillar** (7 Content Pillar theo AIDA), KHÔNG còn là nguồn PILLAR_KW độc quyền — Bước 2b (tracker sheet) mới là nguồn quyết định pillar nào thực sự đã tồn tại + URL thật của nó. Excel hữu ích khi tin tức khớp với 1 pillar theo kế hoạch AIDA nhưng pillar đó **chưa có bài Plan nào trên tracker** — lúc đó coi target keyword trong Excel như một PILLAR_KW "dự kiến" (chưa có URL thật để link, cân nhắc chọn pillar khác đã có bài Plan thật để link thay vào).

Lấy 2 loại dữ liệu tách biệt từ Excel:

1. **Pillar keyword dự kiến** (sheet `Content Pillars (AIDA)`) — mỗi Content Pillar có 1 "Target keyword" gắn với 1 trang pillar tương lai. Đối chiếu với `plan_rows` ở Bước 2b: nếu đã có bài Plan dùng đúng keyword này → dùng URL bài đó làm PILLAR_URL; nếu chưa có → không có PILLAR_URL thật.
2. **Cluster keyword candidates** (sheet `✅ Customer Response AI Chatbot` và các sheet main keyword khác) — hàng trăm sub-keyword long-tail nằm dưới mỗi Main Keyword group. Đây là nguồn keyword thật sự để bài viết từ tin tức nhắm tới (FOCUS_KW).

**Chưa bị loại ở Bước 2 (WordPress) và không nằm trong `used_keywords` ở Bước 2b (Tracker Sheet)** áp dụng cho cluster keyword candidates trước khi chọn làm FOCUS_KW.

---

## Bước 4 — Map tin → pillar (để link) + chọn cluster keyword riêng (để viết) + chọn category

*(Chỉ xét cluster keyword đã pass dedup check ở Bước 2 và Bước 2b)*

**Quy tắc quan trọng — tránh cannibalization:** Bài cluster viết từ tin tức **không được dùng chính keyword của pillar page làm focus keyword của nó**. Pillar page đã (hoặc sẽ) target keyword đó rồi — nếu cluster article cũng target y hệt, 2 bài cùng site sẽ cạnh tranh nhau trên cùng 1 từ khóa. Thay vào đó:

- Cluster article target một **long-tail keyword khác, hẹp hơn**, bám sát góc tin tức.
- Bài chỉ **dẫn link nội bộ (internal link) về pillar page**, dùng anchor text tự nhiên có chứa pillar keyword.

Với mỗi tin, đánh giá:

1. **Pillar target:** Tin này liên quan đến pillar nào trong `plan_rows` (Bước 2b)? Ưu tiên chọn pillar đã có bài Plan **thật** trên tracker (có URL thật). Để đa dạng internal-link equity, ưu tiên pillar **chưa được dùng làm PILLAR_URL** trong các bài News gần đây (xem tracker) trước khi tái sử dụng cùng 1 pillar liên tục.
2. **Cluster keyword:** Chọn 1 keyword long-tail — **không được trùng bất kỳ giá trị nào trong `used_keywords`** (Bước 2b) và pass `is_duplicate()` ở Bước 2 (WordPress). Kiểm tra thêm slug-overlap thủ công (>0.6 là trùng) với các slug hiện có, kể cả slug của chính các bài News trước đó (không chỉ Plan) — dễ bị bỏ sót vì nhiều bài đều có đuôi `-real-estate-agents` khiến overlap dễ vượt ngưỡng.
3. **Category:** CRM/sales automation topic → `"CRM Software"`, Chatbot/AI assistant/ISA/compliance topic → `"AI Chatbot"`.
4. **Angle:** Tin cung cấp dữ liệu/case study/xu hướng gì để làm hook cho đúng cluster keyword đó?

Chọn **top 1 bộ** (tin + cluster keyword + pillar target + category) có relevance cao nhất và angle rõ ràng nhất để viết. Output rõ các giá trị: `FOCUS_KW`, `PILLAR_KW`/`PILLAR_URL`, `CATEGORY_NAME`.

---

## Bước 5 — Viết cluster article

**Cấu trúc HTML bài viết:**

```
Intro paragraph — có FOCUS_KW (cluster keyword, KHÔNG phải pillar keyword) trong 100 từ đầu, context từ tin tức
[HERO image]
H2: Dữ liệu/tin tức mới — hook từ news, cite URL nguồn làm external link
[STATS image]
H2: Tại sao điều này quan trọng với real estate agents
H2: Giải pháp — [FOCUS_KW] trong thực tế  ← MỘT H2 PHẢI CHỨA FOCUS_KW NGUYÊN VĂN
[DEMO image]
H2: Top platforms/tools — external dofollow links tới tool websites
[COMPARISON image]
H2: Related reading — internal link về PILLAR_URL, anchor text tự nhiên chứa PILLAR_KW (không phải FOCUS_KW) + 1 bài liên quan khác
H2: Final Thoughts
```

**Lưu ý khi viết đoạn "Related reading":** anchor text trỏ về pillar page nên đọc tự nhiên và chứa PILLAR_KW, vì đây chính là cách truyền tín hiệu từ khóa cho pillar page. FOCUS_KW mới là keyword bài này cần rank, PILLAR_KW chỉ xuất hiện trong anchor text/link.

**Rank Math SEO checklist — tự verify trước khi publish:** (đã sửa sau khi phát hiện thực tế Rank Math chấm 43/100 dù `check_seo()` cũ báo "ok" — hàm cũ THIẾU 2 check quan trọng: keyword trong SEO title, keyword trong subheading. Luôn dùng bản đầy đủ dưới đây, không dùng bản rút gọn của các skill cũ hơn):

```python
def check_seo(content, keyword, seo_title=None, pillar_keyword=None, pillar_url=None):
    raw = re.sub(r'<[^>]+>', ' ', content)
    words = raw.split()
    kw_count = len(re.findall(re.escape(keyword), raw.lower()))
    density = (kw_count / len(words)) * 100
    ext_links = len(re.findall(r'href="https?://(?!infina\.ai)[^"]*"', content))
    int_links = len(re.findall(r'href="https?://infina\.ai[^"]*"', content))
    img_alts_with_kw = len([m for m in re.findall(r'alt="[^"]*"', content.lower())
                             if keyword in m])
    h2_texts = re.findall(r'<h2>(.*?)</h2>', content, re.IGNORECASE)
    kw_in_h2 = any(keyword in h2.lower() for h2 in h2_texts)

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
    if not kw_in_h2:
        issues.append("FOCUS_KW không xuất hiện nguyên văn trong bất kỳ H2 nào — Rank Math trừ điểm mục 'keyword in subheading'")
    if seo_title is not None and keyword not in seo_title.lower():
        issues.append("FOCUS_KW không xuất hiện nguyên văn trong SEO_TITLE — Rank Math báo lỗi 'Focus Keyword does not appear in the SEO title', kéo điểm xuống rất thấp (từng gặp 43/100 chỉ vì lỗi này)")

    # Chống cannibalization: FOCUS_KW (cluster) không được trùng PILLAR_KW
    if pillar_keyword and keyword.strip().lower() == pillar_keyword.strip().lower():
        issues.append(f"FOCUS_KW trùng hệt PILLAR_KW ('{pillar_keyword}') — đổi sang long-tail keyword khác, pillar keyword chỉ dùng làm anchor text")
    if pillar_url and pillar_url not in content:
        issues.append(f"Thiếu internal link trỏ về pillar page ({pillar_url}) trong đoạn Related reading")

    return {
        "words": len(words),
        "kw_count": kw_count,
        "density": f"{density:.2f}%",
        "ext_links": ext_links,
        "int_links": int_links,
        "img_alts_with_kw": img_alts_with_kw,
        "kw_in_h2": kw_in_h2,
        "ok": len(issues) == 0,
        "issues": issues
    }

# Dùng trước khi publish — LUÔN truyền seo_title, không chỉ content:
seo = check_seo(CONTENT, FOCUS_KW, SEO_TITLE, PILLAR_KW, PILLAR_URL)
if not seo["ok"]:
    print("SEO issues:", seo["issues"])
    # Sửa CONTENT/SEO_TITLE trước khi gọi create_post — vd: thêm FOCUS_KW nguyên văn vào 1 H2 và vào SEO_TITLE
```

**Cách viết SEO_TITLE và H2 chứa FOCUS_KW mà vẫn tự nhiên:** vì FOCUS_KW nhiều khi là cụm dài (vd `"tcpa compliance for real estate agents"`), khi diễn giải lại bằng từ đồng nghĩa hoặc chèn thêm từ ở giữa (vd viết thành `"tcpa compliance among real estate agents"`) sẽ làm mất match chính xác — Rank Math và hàm check ở trên đều tìm **substring y hệt**, không hiểu đồng nghĩa. Luôn giữ FOCUS_KW làm 1 cụm liền mạch trong ít nhất 1 câu của SEO_TITLE và 1 H2, phần diễn giải tự nhiên đặt trước/sau cụm đó chứ không chen vào giữa.

**Nếu density thấp:** thêm các đoạn tự nhiên sử dụng FOCUS_KW (cụm liền mạch, không chèn từ ở giữa) vào body sections.
**Nếu thiếu internal link:** thêm đoạn "Related reading" trước Final Thoughts với ≥2 link đến bài trong infina.ai/news, trong đó có 1 link chính xác trỏ về `PILLAR_URL` với anchor text chứa `PILLAR_KW`.
**Nếu thiếu external link:** đảm bảo link tới URL nguồn tin và website các tool đề cập trong bài không có `rel="nofollow"` với nguồn tin (được phép nofollow với tool/vendor link).
**Nếu FOCUS_KW trùng PILLAR_KW:** đây là lỗi cannibalization — quay lại Bước 4 chọn cluster keyword khác, không sửa bằng cách đổi PILLAR_KW.

---

## Bước 6 — Xác định thời điểm publish + Publish lên WordPress

Lấy giờ bài `status=publish` gần nhất trên WordPress (từ `posts` ở Bước 2), tính `target = giờ_bài_gần_nhất + 1 tiếng`:
- Nếu `target` đã ở quá khứ so với giờ hiện tại → `create_post` với `status: "publish"` (publish ngay).
- Nếu `target` còn ở tương lai → `create_post` với `status: "future"` và `date = target` (format `"YYYY-MM-DD HH:MM:SS"`, KHÔNG phải ISO có chữ T) để lên lịch thay vì publish ngay.

⚠️ **Featured image = `IMG["STATS"]`, KHÔNG phải `IMG["HERO"]`.** Xem `THUMBNAIL_BEST_PRACTICES.md` (cùng thư mục skill) — ảnh HERO (photorealistic người ngồi laptop) lặp lại gần như y hệt qua các bài khiến trang chủ nhìn "toàn ảnh giống nhau", đây chính là vấn đề đợt audit toàn site trước đó đã sửa cho các bài cũ. Ảnh HERO vẫn tạo và chèn trong content như bình thường (đầu bài), chỉ riêng featured image/thumbnail dùng STATS.

```python
resp = call("create_post", {
    "title": TITLE,
    "content": CONTENT,
    "status": STATUS,  # "publish" hoặc "future" theo logic trên
    # "date": TARGET_DATETIME_STR,  # chỉ set khi status="future"
    "slug": SLUG,
    "seo_title": SEO_TITLE,
    "seo_description": SEO_DESC,
    "seo_focus_keyword": FOCUS_KW,
    "categories": [CATEGORY_NAME],  # "AI Chatbot" hoặc "CRM Software" — tên string, KHÔNG phải ID số
    "tags": TAGS,
    "image_url": IMG["STATS"],  # KHÔNG dùng IMG["HERO"] — xem lý do bên dưới
    "image_alt": f"{FOCUS_KW} statistics infographic",
})

post_id_match = re.search(r'ID (\d+)', resp)  # khớp "Da tao bai ID {id} [status: ...]" từ source code server
if post_id_match:
    post_id = post_id_match.group(1)
    print(f"Post ID {post_id} — status {STATUS}")
    print(f"URL: https://infina.ai/news/{SLUG}/")
if "that bai" in resp:  # image_note báo lỗi gắn ảnh đại diện dù post vẫn tạo thành công
    print("CANH BAO:", resp)
```

**Sửa bài sau khi publish** (đổi date/category/status/content...) dùng `update_post` trực tiếp qua cùng endpoint JSON-RPC:

```python
resp = call("update_post", {"post_id": post_id, "seo_title": NEW_SEO_TITLE})
```

**Verify sau publish** (khuyến nghị, đặc biệt sau khi từng gặp Rank Math score thấp dù `check_seo()` báo pass): dùng `list_posts` với `search` param hoặc mở link edit để người dùng tự confirm điểm Rank Math thật, vì không có tool nào đọc trực tiếp điểm Rank Math qua API MCP hiện tại.

---

## Bước 7 — Log kết quả vào Tracker Sheet

Sau khi publish thành công, phải **append 1 dòng mới** vào chính Google Sheet tracker ở Bước 2b (`1uVI1tPQxhTUk4qj8NWZSi-EReEwe2ZKIyIt_eQGeFOs`).

**QUAN TRỌNG — đưa dòng dưới dạng tab-separated, KHÔNG dùng bảng markdown `| ... |`:** nếu đưa format `| 16 | 07/08/2026 | ... |` cho người dùng copy-paste, Google Sheets sẽ dán nguyên chuỗi đó vào 1 ô duy nhất thay vì tự tách cột (Sheets chỉ tự tách cột khi dán dữ liệu có ký tự **tab** giữa các trường, không nhận diện dấu `|`). Luôn in dòng cần thêm bằng tab thật giữa 6 trường, ví dụ (mỗi khoảng trắng dưới đây là 1 tab, không phải dấu `|`):

```
16	07/08/2026	Compliance-First AI: What Every Brokerage Should Demand	https://infina.ai/news/compliance-first-ai-brokerage/	tcpa compliance ai texting real estate	News
```

Thứ tự cột đúng bằng thứ tự header hiện có: `#, Date, Title, URL, Focus Keyword, Type`.

**Giới hạn công cụ hiện tại — chưa tự động hoá được bước này:** các tool Google Drive hiện có (`create_file`, `read_file_content`, `download_file_content`, `search_files`, `copy_file`, `get_file_metadata`) **không có tool nào ghi/sửa nội dung 1 Google Sheet đã tồn tại**. Vì vậy sau khi publish:

1. In ra đúng dòng cần thêm (dạng tab-separated ở trên) trong 1 code block để giữ nguyên ký tự tab khi người dùng copy.
2. Nói rõ với người dùng: "Đã publish xong, đây là dòng cần thêm vào tracker sheet — copy nguyên khối code rồi paste vào ô đầu dòng trống cuối sheet giúp mình nhé" (kèm link sheet).
3. Nếu người dùng lỡ paste sai (dính hết vào 1 ô) — hướng dẫn sửa nhanh bằng **Data → Split text to columns → Custom separator** thay vì bắt họ xoá paste lại từ đầu.
4. Nếu về sau có kết nối Google Sheets API/connector hỗ trợ ghi, dùng nó để tự append thay vì làm thủ công — kiểm tra qua `ListConnectors`/`SearchMcpRegistry` trước khi báo là "không làm được".

---

## Bước 8 (Optional) — Kiểm tra traffic Google Search Console + Google Analytics

Không chạy mỗi ngày trong pipeline chính — chỉ dùng khi user hỏi về traffic/ranking/impressions/users của site hoặc các bài đã đăng.

**Credential:** dùng chung 1 service account cho cả 2 API — key thật **không nằm trong repo này** (tránh commit secret vào git history). Key thật lưu ở account-level skill copy tại `credentials/gsc_service_account.json` (cùng thư mục skill, ngoài GitHub). Service account email: `search-console-api@tidy-set-492904-b1.iam.gserviceaccount.com`.

- **Search Console:** đã cấp quyền `Full` trên 2 property: `https://infina.ai/` và `https://infina.ai/news/`.
- **Google Analytics (GA4):** đã được add vào GA4 với quyền đọc, property cần dùng là **"Infina AI" — `properties/505677884`** (thuộc account GA "RealStake", account ID `140795077`). Xác nhận truy cập được ngày 2026-08-24 — timeZone của property là `Asia/Saigon`, currencyCode `VND`.
- **Lưu ý dựng lại từ đầu (container mới không còn `credentials/gsc_service_account.json`):** nếu file key không tồn tại ở đường dẫn trên, tìm bản gốc đã upload trong `/root/.claude/uploads/{session_id}/*infina_ai_search_console_api*.json` hoặc hỏi user upload lại. Nếu Admin API/Data API của GA trả lỗi `SERVICE_DISABLED`, đó là do 2 API `analyticsadmin.googleapis.com` và `analyticsdata.googleapis.com` chưa được bật trên GCP project `tidy-set-492904-b1` — báo user vào link `activationUrl` trong response lỗi để bấm Enable (không tự làm được qua API).

Không có sẵn `google-auth`/`google-api-python-client` trong môi trường — tự build JWT bằng `pyjwt` + `cryptography` rồi đổi lấy access token qua `token_uri`. Nếu `cryptography`/`cffi` bị lỗi native binding (`ModuleNotFoundError: cffi` hoặc rust panic), chạy `pip3 install --user --force-reinstall cffi cryptography` trước. Access token GA và GSC dùng chung code JWT, chỉ khác `SCOPE`.

```python
import json, time, jwt, requests
import os

KEY_PATH = os.environ.get("GSC_SERVICE_ACCOUNT_KEY_PATH", "credentials/gsc_service_account.json")  # relative to skill dir

def get_access_token(scope):
    creds = json.load(open(KEY_PATH))
    now = int(time.time())
    payload = {"iss": creds["client_email"], "scope": scope, "aud": creds["token_uri"],
               "iat": now, "exp": now + 3600}
    assertion = jwt.encode(payload, creds["private_key"], algorithm="RS256")
    resp = requests.post(creds["token_uri"], data={
        "grant_type": "urn:ietf:params:oauth:grant-type:jwt-bearer",
        "assertion": assertion,
    }, timeout=30)
    return resp.json()["access_token"]

# --- Search Console ---
def query_search_analytics(site_url, start_date, end_date, dimensions=None, row_limit=25):
    token = get_access_token("https://www.googleapis.com/auth/webmasters.readonly")
    headers = {"Authorization": f"Bearer {token}", "Content-Type": "application/json"}
    url = f"https://www.googleapis.com/webmasters/v3/sites/{requests.utils.quote(site_url, safe='')}/searchAnalytics/query"
    body = {"startDate": start_date, "endDate": end_date, "rowLimit": row_limit}
    if dimensions:
        body["dimensions"] = dimensions
    return requests.post(url, headers=headers, json=body, timeout=30).json()

# Vi du: top pages theo impressions trong 28 ngay gan nhat
# query_search_analytics("https://infina.ai/news/", "2026-07-22", "2026-08-19", dimensions=["page"], row_limit=30)

# --- Google Analytics (GA4) ---
GA_PROPERTY_ID = "505677884"  # "Infina AI" property

def query_ga4_report(metrics, dimensions=None, start_date="7daysAgo", end_date="today", property_id=GA_PROPERTY_ID):
    token = get_access_token("https://www.googleapis.com/auth/analytics.readonly")
    headers = {"Authorization": f"Bearer {token}"}
    body = {
        "dateRanges": [{"startDate": start_date, "endDate": end_date}],
        "metrics": [{"name": m} for m in metrics],
    }
    if dimensions:
        body["dimensions"] = [{"name": d} for d in dimensions]
        body["orderBys"] = [{"dimension": {"dimensionName": dimensions[0]}}]
    url = f"https://analyticsdata.googleapis.com/v1beta/properties/{property_id}:runReport"
    return requests.post(url, headers=headers, json=body, timeout=30).json()

# Vi du: users/sessions/pageviews theo ngay, 7 ngay gan nhat
# query_ga4_report(["activeUsers", "sessions", "screenPageViews"], dimensions=["date"])
# Vi du: traffic theo landing page
# query_ga4_report(["activeUsers", "sessions"], dimensions=["landingPage"], start_date="28daysAgo")
```

GSC data có độ trễ report ~2-3 ngày, nên `endDate` gần "hôm nay" thường trả về 0 cho vài ngày cuối. GA4 gần real-time hơn nhưng ngày hiện tại thường chưa đầy đủ (đang chạy dở). Dùng dimensions GSC `["date"]`, `["page"]`, `["query"]`; dimensions GA4 phổ biến `["date"]`, `["landingPage"]`, `["sessionDefaultChannelGroup"]`, `["deviceCategory"]` tuỳ nhu cầu. **Không bao giờ commit file key JSON thật hoặc `private_key` vào repo này** — key thật chỉ tồn tại ở account-level skill copy, ngoài GitHub.

**--- Microsoft Clarity (heatmap/engagement, khác hệ thống với Google) ---**

User đã cấp 1 API token riêng (JWT, scope `Data.Export`, do Clarity tự phát hành trong project settings, không liên quan gì tới service account Google ở trên). Token thật lưu tại `credentials/clarity_api_token.txt` (account-level skill copy, ngoài GitHub, cùng thư mục với `gsc_service_account.json`). Token dùng trực tiếp làm Bearer, không cần build JWT/đổi access token như Google.

```python
import os, requests

CLARITY_TOKEN_PATH = os.environ.get("CLARITY_TOKEN_PATH", "credentials/clarity_api_token.txt")

def query_clarity(num_of_days=1, dimension1=None, dimension2=None, dimension3=None):
    token = open(CLARITY_TOKEN_PATH).read().strip()
    params = {"numOfDays": num_of_days}
    if dimension1: params["dimension1"] = dimension1  # vd: "Browser", "Country", "Device", "PopularPages"...
    if dimension2: params["dimension2"] = dimension2
    if dimension3: params["dimension3"] = dimension3
    r = requests.get(
        "https://www.clarity.ms/export-data/api/v1/project-live-insights",
        headers={"Authorization": f"Bearer {token}"},
        params=params, timeout=30,
    )
    return r.json()

# Vi du: data mac dinh 1 ngay gan nhat (tra ve toan bo cac metric: Traffic, EngagementTime,
# ScrollDepth, DeadClickCount, RageClickCount, Browser, Device, OS, Country, PageTitle,
# ReferrerUrl, PopularPages, v.v. — moi metric 1 object trong list ket qua)
# query_clarity(num_of_days=1)
```

**Giới hạn quan trọng — KHÔNG được bỏ qua:** API Clarity giới hạn **tối đa 10 request/ngày/project** (tính theo project, không phải theo key). Chỉ gọi khi user thực sự hỏi về Clarity/heatmap/engagement, không gọi tuỳ tiện hoặc gọi lặp lại nhiều lần trong 1 lần kiểm tra. `numOfDays` tối đa hỗ trợ là 3 (API chỉ cho xem 1-3 ngày gần nhất, không có range dài hơn — muốn xu hướng dài hạn phải tự lưu lại kết quả qua nhiều lần gọi cách ngày). Project Clarity "Infina AI" track chung cả app (`ai.infina.vn`) lẫn blog (`infina.ai/news`) — phần lớn session sẽ là traffic app, không phải blog, cần lọc qua `PopularPages`/`ReferrerUrl` nếu chỉ quan tâm blog.

**Nếu file token không tồn tại** (container mới, thư mục `credentials/` trống): tìm bản gốc user đã upload dạng `.txt` trong `/root/.claude/uploads/{session_id}/*Clarity*` hoặc hỏi user upload lại — không tự bịa token.

---

## Slug rules (critical)

- Slug bám theo `FOCUS_KW` (cluster keyword của chính bài này), KHÔNG bám theo `PILLAR_KW`
- Mỗi từ trong FOCUS_KW phải xuất hiện trong slug
- Ví dụ: keyword `crm for real estate agents` → slug `crm-for-real-estate-agents` (phải có `for`)
- Singular ≠ plural: `agent` ≠ `agents`
- Tách keyword ra từng từ, check từng từ có trong slug không trước khi publish
- Trước khi chốt slug, so overlap thủ công với TOÀN BỘ slug hiện có trên site (không chỉ pillar) — nhiều slug trong niche này đều có đuôi `-real-estate-agents` nên dễ vượt ngưỡng overlap >60% nếu không cẩn thận chọn phần đầu slug đủ khác biệt

---

## Output script file

Mỗi lần chạy tạo file: `article_cluster{N}_{slug}.py` lưu vào cùng folder với các script khác.

---

## Inputs cần thiết

| Input | Bắt buộc | Ghi chú |
|-------|----------|---------|
| Excel keyword file | Có | Đường dẫn tuyệt đối đến file xlsx |
| Tracker Sheet (Google Sheets) | Có | `fileId: 1uVI1tPQxhTUk4qj8NWZSi-EReEwe2ZKIyIt_eQGeFOs` — cần quyền đọc qua Google Drive connector (`mcp__Google_Drive__read_file_content`). Đây là nguồn PILLAR_KW/dedup chính thức, đọc lại mỗi lần chạy vì nó thay đổi liên tục |
| Category | Có | `"AI Chatbot"` hoặc `"CRM Software"` tuỳ chủ đề bài (xem Bước 4) |

