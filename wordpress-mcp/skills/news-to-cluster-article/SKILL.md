---
name: "news-to-cluster-article"
description: "Crawl tin tức mới theo 10 mảng, đối chiếu keyword trong Excel và Google Sheet tracker, check bài đã có trên WordPress (published/scheduled/draft), chọn tin phù hợp và viết cluster article đạt Rank Math ≥80/100. Dùng khi muốn viết bài cluster từ tin tức mới nhất."
---

# SKILL: Daily News → Cluster Article (Rank Math SEO)

## Mô tả
Crawl tin tức mới theo 10 mảng → đối chiếu Google Sheet tracker (nguồn pillar/dedup chính thức) + WordPress → đối chiếu keyword trong Excel → chọn tin phù hợp → viết và đăng cluster article lên WordPress đạt Rank Math ≥80/100. Toàn bộ chạy qua API, không cần browser.

**Nguyên tắc cốt lõi:** bài viết từ tin tức (cluster/spoke) luôn target một keyword long-tail RIÊNG của nó (`FOCUS_KW`), khác với keyword của pillar page (`PILLAR_KW`) mà nó link về. Không bao giờ để 2 bài trong site cùng target 1 keyword — pillar page giữ vị trí rank cho keyword đầu (head term), cluster article chỉ mượn góc tin tức để nhắm long-tail và đẩy internal link/topical authority về pillar. Nguồn xác định keyword nào đã "có chủ" (Plan = pillar, News = cluster đã viết) là Google Sheet tracker ở Bước 2b — đọc lại sheet này mỗi lần chạy, và append 1 dòng mới vào đó sau khi publish (Bước 7). **Bài mới phải có ít nhất 1 inbound link biên tập**: Bước 5 lo chiều đi (cluster lên pillar, cluster sang 2-3 bài cùng cụm), Bước 6.5 lo chiều về bằng cách sửa 1 bài cluster cùng cụm trỏ sang bài mới. Bỏ Bước 6.5 là bài vừa publish không có trang nào trỏ tới.

**Lịch sử:** skill này có 2 nhánh phát triển từng tồn tại song song trên account (một nhánh tập trung compliance/tracker/anti-cannibalization, một nhánh tập trung chất lượng ảnh/category/rate-limit) — bản này là merge của cả hai, giữ lại phần tốt của từng bên.

---

## Category IDs

| ID | Tên | Dùng cho |
|----|-----|---------|
| 19 | AI Chatbot | Bài về chatbot, AI assistant, conversational AI, ISA, AI voice |
| 85 | CRM Software | Bài về CRM, sales automation, lead management |
| 153 | Real Estate Websites | Bài về website builder, IDX, MLS feed, landing page, web design |
| 289 | Real Estate Chatbots | (đã tồn tại trên site, ít dùng — ưu tiên 19) |
| 13 | Thought Leadership | (đã tồn tại trên site, ít dùng) |
| 1  | News | Bài tin tức thời sự chung (không phải cluster real estate) |

**Bảng trên đã bổ sung 03/10/2026** sau khi phát hiện bản cũ chỉ liệt kê 19/85/1 trong khi site thực tế có 6 category — bài IDX/website dùng **153**, không phải 19 hay 85 (verify bằng `GET /wp-json/wp/v2/posts?slug=idx-website-for-realtors&_fields=categories`). Luôn tra lại danh sách thật qua `GET https://infina.ai/news/wp-json/wp/v2/categories?per_page=100&_fields=id,name` nếu chủ đề bài không khớp 3 dòng đầu.

Truyền category **bằng tên** vào param `categories` (WP MCP tự resolve tên category thành term qua `wp_set_post_terms`, tạo mới nếu tên chưa tồn tại):
```python
"categories": ["CRM Software"]
"categories": ["AI Chatbot"]
```
Chọn category theo chủ đề bài: CRM/sales automation → "CRM Software", chatbot/AI assistant/ISA/compliance → "AI Chatbot".

**Đã gặp thực tế (01/10/2026, bài #1415):** truyền `"categories": ["CRM Software"]` cả ở `create_post` lẫn `update_post` sau đó đều không gán được category (REST API trả về `"categories": []"` dù response báo thành công và `tags` bằng tên trong CÙNG lúc gán đúng bình thường) — không rõ nguyên nhân (không phải lỗi proxy/cache, đã kiểm tra nhiều lần). Workaround verify hoạt động: truyền **ID dạng string** thay vì tên, vd `"categories": ["85"]` cho "CRM Software" (tra ID qua `GET https://infina.ai/news/wp-json/wp/v2/categories?per_page=100&_fields=id,name` — "AI Chatbot"=19, "CRM Software"=85). Nếu gặp lại category rỗng sau khi publish, luôn `curl` REST API verify `categories` field rồi fix bằng ID ngay, đừng chỉ tin message "Da cap nhat" là đã thành công.

---

## Publishing Rules (kiểm tra TRƯỚC KHI PUBLISH)

### Rule 1: Chỉ 1 bài mỗi lần chạy, tối đa 3 bài/ngày
Skill này chỉ viết **đúng 1 bài** mỗi lần được gọi. Ngoài ra, trước khi publish, đếm số bài đã publish trong cùng ngày (giờ site) qua `list_posts` (JSON-RPC, KHÔNG dùng REST API `/wp-json/wp/v2/posts` không xác thực — REST API công khai không thấy được bài `draft`, dễ đếm thiếu):
```python
def count_posts_on_date(all_posts, target_date):
    """target_date: 'YYYY-MM-DD'. all_posts: list từ get_all_posts() ở Bước 2."""
    return sum(1 for p in all_posts if p["status"] == "publish" and p["date"].startswith(target_date))

count = count_posts_on_date(posts, "2026-08-11")
if count >= 3:
    print("STOP: Ngày này đã đủ 3 bài, dừng lại không publish thêm.")
```

### Rule 2: Không trùng focus keyword / slug / pillar keyword
Xem Bước 2 (dedup WordPress) + Bước 2b (tracker sheet) + Bước 4 (pillar vs cluster).

### Rule 3: Slug phải chứa từng chữ của FOCUS_KW
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

**Lưu ý các host tạm khác đã thử và KHÔNG dùng được** (qua agent proxy của môi trường này): `0x0.st` (connection reset ở tầng proxy), `catbox.moe` file-upload thường (412 "Invalid uploader"), `tmpfiles.org` (trả về trang HTML preview chứ không phải URL ảnh trực tiếp, fail HEAD content-type check của WP). `litterbox.catbox.moe` từng hoạt động tốt nhưng đã gặp lỗi 500 "Internal Server Error" liên tục (01/10/2026, không phải lỗi proxy — đã xác nhận qua `__agentproxy/status` không có relay failure) — khi gặp, fallback ngay sang `uguu.se`:

```python
def upload_uguu(img_bytes):
    r = requests.post("https://uguu.se/upload",
        files={"files[]": ("img.jpg", img_bytes, "image/jpeg")}, timeout=30)
    r.raise_for_status()
    data = r.json()
    if not data.get("success"):
        raise Exception(f"uguu failed: {data}")
    return data["files"][0]["url"]  # vd: https://h.uguu.se/xxxxx.jpg
```
Đã verify hoạt động tốt (không cần key, trả JSON có `files[0].url`, URL serve đúng `content-type: image/jpeg`). Thử theo thứ tự: freeimage.host → litterbox.catbox.moe → uguu.se.

⚠️ **`requests` không có sẵn trong container mới (07/10/2026).** Và `python3 -I` bỏ qua user
site-packages, nên `pip install requests` cũng không cứu được: import vẫn fail. Mọi đoạn code dùng
`requests` ở trên chỉ chạy khi môi trường tình cờ đã có nó. Dùng bản stdlib đã đóng gói sẵn thay vì
ngồi sửa import:

```bash
python3 -I wordpress-mcp/scripts/gen_article_images.py spec.json
```

`spec.json` là `[{"name": "...", "alt": "...", "prompt": "..."}, ...]`. Script tự gắn negative
guards, crop 16:9, upload uguu, in ra URL cho từng ảnh. Key đọc từ file `gkey` cạnh script.

**Nếu Gemini lỗi liên tục (kể cả sau retry trong hàm trên):** thử lại thêm 1 lần thủ công (gọi lại `nano_banana()`), nếu vẫn lỗi thì **báo cho user trong tóm tắt**, KHÔNG tự ý fallback sang Grok — Grok đã bị loại khỏi pipeline vì cho ra ảnh illustration/style không đồng nhất với chuẩn photorealistic + glossy/gradient hiện tại của site.

**Phương án B (đã ngừng dùng, chỉ còn giá trị lịch sử) — Grok API:** từng là default ban đầu (`grok-imagine-image` qua `api.x.ai`), đã bị thay thế hoàn toàn bằng Gemini nano-banana. Không dùng lại trừ khi có chỉ đạo mới rõ ràng từ user.

Mỗi bài cần **4 ảnh**: HERO, STATS/DATA, DEMO, COMPARISON. Ảnh HERO vẫn tạo và chèn vào content như bình thường; riêng **featured image/thumbnail dùng STATS** (xem Bước 6 — lý do: tránh lặp lại HERO photo giống nhau trên trang chủ).

---

## Image Prompt System: viết prompt sao cho ảnh không bị lỗi

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

**Bảng so sánh/số liệu chi tiết nhiều hàng-cột (≥3 cột hoặc ≥4 hàng) — dùng `<table>` HTML thật trong thân bài, KHÔNG generate ảnh AI.** Lý do: ảnh AI dựng bảng hay bịa tên sản phẩm/số liệu không khớp nội dung bài (đã xảy ra thực tế ở bài `best-free-crm-for-real-estate-agents`, #438 — ảnh so sánh bịa 3 tên CRM giả, ảnh thống kê bịa % adoption kèm dòng disclaimer "hypothetical" nhỏ xíu không ai đọc được), và vi phạm luôn checklist thumbnail (`THUMBNAIL_BEST_PRACTICES.md`: "không dùng bảng dữ liệu nhiều hàng/cột làm ảnh"). Ảnh AI (STATS/COMPARISON Template A-E) chỉ dùng cho 1 con số/1 so sánh 2 phe đơn giản; bảng dữ liệu thật phải là markup, không phải ảnh.

Theme đang chạy (`infina-ai-news` v1.0.9) **đã tự style sẵn mọi `<table>` trong `.post-content`**:
border, padding, nền và màu chữ của header, zebra-stripe hàng chẵn, **và đã tự lo luôn cuộn ngang
trên mobile**. Rule thật, đọc từ `https://infina.ai/news/wp-content/themes/infina-ai-news/style.css`:

```css
.post-content .wp-block-table { margin: 1.8em 0; overflow-x: auto }
.post-content table           { width: 100%; border-collapse: collapse; font-size: 15px }
.post-content th,
.post-content td              { border: 1px solid var(--border); padding: 12px 16px; text-align: left }
.post-content thead th        { background: var(--blue-soft) /* #EEF3FF */;
                                color: var(--navy) /* #001F5C */; font-weight: 700 }
.post-content tbody tr:nth-child(even) { background: #fafbfc }
```

Nên markup chuẩn chỉ cần đúng một thứ: **bọc `<table>` trong `<figure class="wp-block-table">`**.
Chính cái class đó kích hoạt `overflow-x: auto` của theme. Không cần style nội tuyến gì cả:

```html
<figure class="wp-block-table">
<table>
<thead><tr>
<th>Cột 1</th><th>Cột 2</th><th>Cột 3</th>
</tr></thead>
<tbody>
<tr><td>...</td><td>...</td><td>...</td></tr>
<tr><td>...</td><td>...</td><td>...</td></tr>
</tbody>
</table>
</figure>
```

⚠️ **`<table>` trần, không bọc `<figure class="wp-block-table">`, là thứ gây vỡ layout mobile.** Rule
của theme nhắm vào `.wp-block-table`, nên bảng trần không có container cuộn nào. Đo 08/10 ở viewport
375px: `#546` (6 cột) cần 565px, tràn 190px; `#89` 468px; `#1462` 438px. Đã bọc lại 20 bảng ở 16 bài.

⚠️ **KHÔNG set `style="background:...;color:...;"` lên `<tr>`/`<th>`/`<td>`.** Theme đã set nền
`#EEF3FF` + chữ `#001F5C` thẳng trên `th`, nên nền đặt ở `tr` không bao giờ hiện ra, còn `color` đặt
inline thì THẮNG theme. Đây là cái bẫy đã bắt hụt dự án **hai lần** ở `#438`:

| Lần | `tr` | `th` | Nền thật sự thấy | Tương phản |
|---|---|---|---|---|
| Ban đầu | `background:#1a2b4c` | `color:#001F5C` | `#EEF3FF` (của theme) | **1,11:1** |
| Tôi "sửa" 08/10 | `background:#1a2b4c` | `color:#ffffff` | `#EEF3FF` (của theme) | **1,10:1**, tệ hơn |
| Đúng | bỏ hết style | bỏ hết style | `#EEF3FF` | **13,99:1** |

Cách sửa đúng là **xoá sạch `style` trên `tr`/`th`/`td`**, để theme lo. Chuẩn WCAG AA là 4,5:1.

⚠️ **Nếu buộc phải dùng style nội tuyến cho overflow, viết `overflow:auto` chứ không phải
`overflow-x:auto`.** WordPress lọc `style` qua `safecss_filter_attr()` và `overflow-x` không nằm
trong danh sách property được phép nên bị xoá sạch; `overflow`, `display`, `max-width` thì sống. Đã
kiểm chứng bằng cách ghi thử cả hai lên `#1415` rồi đọc lại qua REST. Nhưng trong hầu hết trường hợp
bạn **không cần** nó: cứ bọc `<figure class="wp-block-table">` là theme lo rồi.

### ⚠️ Cách đọc CSS của site cho đúng, và một lỗi phương pháp đã xảy ra thật

Ngày 08/10 tôi kết luận "theme không có rule nào cho table" và viết nhầm vào chính file này. Toàn bộ
kết luận đó sai, và nó bắt nguồn từ **một regex thiếu**:

```python
re.findall(r'<link[^>]+href="([^"]+\.css[^"]*)"', html)          # SAI, chỉ bắt nháy kép
re.findall(r"""<link[^>]+href=["']([^"']+\.css[^"']*)["']""", h)  # ĐÚNG, bắt cả nháy đơn
```

WordPress xuất `<link rel='stylesheet' href='...'>` bằng **nháy đơn**. Regex cũ trả về 0 stylesheet,
từ đó tôi tưởng site chỉ có CSS inline, rồi render local thiếu hẳn CSS của theme, rồi đo ra những con
số không có thật, rồi "sửa" `#438` thành chữ trắng trên nền sáng.

Quy tắc rút ra: khi render local để đo, **phải nạp cả stylesheet ngoài vào snapshot**, và kiểm tra
số stylesheet nạp được có khác 0 không trước khi tin bất cứ phép đo nào. Script
`wordpress-mcp/skills/post-refresh/scripts/render_snapshot.py` làm đúng việc đó (nó ném lỗi nếu
nạp được 0 stylesheet).

⚠️ **Theme trong repo đã cũ, đừng dùng làm nguồn tra cứu.** `wordpress-theme/infina-ai-news/style.css`
là **v1.0.5**, bản đang chạy là **v1.0.9**, lệch 64 dòng. Toàn bộ rule `.post-content thead th` và
`.post-content .wp-block-table` **chỉ có ở bản live**, chưa có trong repo. Muốn biết theme style gì,
tải thẳng file CSS từ site chứ đừng đọc file trong repo.
- `<tbody>` không cần `style` cho hàng chẵn/lẻ — theme tự zebra-stripe hàng chẵn `#fafbfc`.

---

## Bước 1: Crawl tin tức 7 ngày gần nhất

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

## Bước 2: Kiểm tra bài đã tồn tại trên WordPress

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

## Bước 2b: Đọc Tracker Sheet (nguồn PILLAR_KW chính thức, ưu tiên hơn Excel)

Google Sheet **"Infina News — Published Articles Tracker"** (`fileId: 1uVI1tPQxhTUk4qj8NWZSi-EReEwe2ZKIyIt_eQGeFOs`) là **nguồn sự thật sống** (live source of truth) về việc keyword nào đã "có chủ" — ưu tiên hơn Excel `Content Pillars (AIDA)` vì Excel chỉ là kế hoạch tĩnh, còn sheet này phản ánh đúng những gì đã thực sự publish.

⚠️ **Dùng `mcp__Google_Drive__download_file_content` với `exportMimeType: "text/csv"`, KHÔNG dùng `read_file_content`** (đã gặp thực tế 02/10/2026): `read_file_content` trả về bản tóm tắt dạng "Table Sample Data" chỉ gồm header + **đúng 1 dòng mẫu**, không phải toàn bộ 120+ dòng — nếu dedup dựa vào đó sẽ bỏ sót gần như toàn bộ keyword đã dùng mà không có cảnh báo nào. `download_file_content` trả base64 của CSV đầy đủ (chỉ sheet đầu tiên "Published article", đúng sheet cần), decode rồi parse bằng `csv.reader`.

```python
import base64, csv, io
raw = base64.b64decode(download_file_content(FILE_ID, exportMimeType="text/csv")["content"]).decode()
rows = list(csv.DictReader(io.StringIO(raw)))   # cột: #, Date, Title, URL, Focus Keyword, Type
used_keywords = {r["Focus Keyword"].strip().lower() for r in rows if r.get("Focus Keyword")}
plan_rows = [r for r in rows if r["Type"].strip().lower() == "plan"]
```

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

## Bước 3: Đọc keyword groups từ Excel

Đọc file `AI_SalesX_Customer_Segments_Content_Pillars - Copy.xlsx` (trong repo: `wordpress-mcp/skills/news-to-cluster-article/keywords/AI_SalesX_Customer_Segments_Content_Pillars.xlsx`), dùng làm **nguồn tham khảo ý tưởng/chiến lược pillar** (7 Content Pillar theo AIDA), KHÔNG còn là nguồn PILLAR_KW độc quyền — Bước 2b (tracker sheet) mới là nguồn quyết định pillar nào thực sự đã tồn tại + URL thật của nó. Excel hữu ích khi tin tức khớp với 1 pillar theo kế hoạch AIDA nhưng pillar đó **chưa có bài Plan nào trên tracker** — lúc đó coi target keyword trong Excel như một PILLAR_KW "dự kiến" (chưa có URL thật để link, cân nhắc chọn pillar khác đã có bài Plan thật để link thay vào).

Lấy 2 loại dữ liệu tách biệt từ Excel:

1. **Pillar keyword dự kiến** (sheet `Content Pillars (AIDA)`) — mỗi Content Pillar có 1 "Target keyword" gắn với 1 trang pillar tương lai. Đối chiếu với `plan_rows` ở Bước 2b: nếu đã có bài Plan dùng đúng keyword này → dùng URL bài đó làm PILLAR_URL; nếu chưa có → không có PILLAR_URL thật.
2. **Cluster keyword candidates** (sheet `✅ Customer Response AI Chatbot` và các sheet main keyword khác) — hàng trăm sub-keyword long-tail nằm dưới mỗi Main Keyword group. Đây là nguồn keyword thật sự để bài viết từ tin tức nhắm tới (FOCUS_KW).

**Chưa bị loại ở Bước 2 (WordPress) và không nằm trong `used_keywords` ở Bước 2b (Tracker Sheet)** áp dụng cho cluster keyword candidates trước khi chọn làm FOCUS_KW.

---

## Bước 4: Map tin → pillar (để link) + chọn cluster keyword riêng (để viết) + chọn category

*(Chỉ xét cluster keyword đã pass dedup check ở Bước 2 và Bước 2b)*

**Quy tắc quan trọng — tránh cannibalization:** Bài cluster viết từ tin tức **không được dùng chính keyword của pillar page làm focus keyword của nó**. Pillar page đã (hoặc sẽ) target keyword đó rồi — nếu cluster article cũng target y hệt, 2 bài cùng site sẽ cạnh tranh nhau trên cùng 1 từ khóa. Thay vào đó:

- Cluster article target một **long-tail keyword khác, hẹp hơn**, bám sát góc tin tức.
- Bài chỉ **dẫn link nội bộ (internal link) về pillar page**. Anchor text phải mô tả đúng trang đích và **khác với anchor các bài trước đã dùng cho cùng pillar đó** (xem mục Anchor text bên dưới).

Với mỗi tin, đánh giá:

1. **Pillar target:** Tin này liên quan đến pillar nào trong `plan_rows` (Bước 2b)? Ưu tiên chọn pillar đã có bài Plan **thật** trên tracker (có URL thật). Để không dồn mọi bài News lên cùng 1 pillar (xem ràng buộc cấu trúc site ở Bước 6.5), ưu tiên pillar **chưa được dùng làm PILLAR_URL** trong các bài News gần đây (xem tracker) trước khi tái sử dụng cùng 1 pillar liên tục.
2. **Cluster keyword:** Chọn 1 keyword long-tail — **không được trùng bất kỳ giá trị nào trong `used_keywords`** (Bước 2b) và pass `is_duplicate()` ở Bước 2 (WordPress). Kiểm tra thêm slug-overlap thủ công (>0.6 là trùng) với các slug hiện có, kể cả slug của chính các bài News trước đó (không chỉ Plan) — dễ bị bỏ sót vì nhiều bài đều có đuôi `-real-estate-agents` khiến overlap dễ vượt ngưỡng.
3. **Category:** CRM/sales automation topic → `"CRM Software"`, Chatbot/AI assistant/ISA/compliance topic → `"AI Chatbot"`.
4. **Angle:** Tin cung cấp dữ liệu/case study/xu hướng gì để làm hook cho đúng cluster keyword đó?

Chọn **top 1 bộ** (tin + cluster keyword + pillar target + category) có relevance cao nhất và angle rõ ràng nhất để viết. Output rõ các giá trị: `FOCUS_KW`, `PILLAR_KW`/`PILLAR_URL`, `CATEGORY_NAME`.

---

## Bước 5: Viết cluster article

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
H2: Related reading — internal link về PILLAR_URL, anchor mô tả trang đích và chưa bài nào dùng + 1 bài liên quan khác
H2: Final Thoughts
```

**Lưu ý khi viết đoạn "Related reading":** FOCUS_KW là keyword bài này cần rank, nên FOCUS_KW không được dùng làm anchor trỏ sang pillar. Anchor trỏ pillar phải mô tả đúng pillar, nhưng **không bắt buộc chứa PILLAR_KW nguyên văn**, xem mục ngay dưới đây.

### Anchor text: mô tả được, và không trùng nhau

⚠️ **Tới 2026-10-08 skill này bắt buộc anchor trỏ pillar phải chứa `PILLAR_KW`.** Vì `PILLAR_KW` cố
định cho mỗi pillar, mọi bài đổ dồn về cùng một anchor. Đo ngày 08/10 trên 145 bài:

| Pillar | Link trỏ tới | Anchor khác nhau | |
|---|---|---|---|
| `best-crm-for-real-estate` | 53 | 12 (23%) | **35 link dùng y hệt** `best crm for real estate agents` |
| `tcpa-compliance-for-real-estate-agents` | 14 | 2 (14%) | 12 link trùng |
| `real-estate-website-builder` | 28 | 6 (21%) | |
| `ai-crm-real-estate` | 23 | 9 (39%) | |
| `crm-pipeline-management` | 12 | 5 (42%) | |
| `real-estate-lead-follow-up-automation-guide` | 15 | 6 (40%) | |
| `real-estate-agent-crm-speed-to-lead` | 13 | 10 (77%) | đạt |
| `best-ai-virtual-assistant-real-estate` | 9 | 7 (78%) | đạt |

**Quy tắc:**

1. 🟢 **Anchor phải hiểu được khi đọc tách khỏi câu.** Che câu đi, chỉ còn anchor, vẫn đoán được
   trang đích nói gì. Google nêu đúng phép thử này trong tài liệu chính thức.
2. 🟢 **Không dùng** `click here`, `read more`, `this post`, `here` làm anchor.
3. 🟢 **Không nhồi keyword, không dài lê thê.** Khoảng 3-8 từ.
4. ✏️ **`PILLAR_KW` KHÔNG bắt buộc xuất hiện nguyên văn.** Anchor chỉ cần mô tả đúng pillar. Đây là
   thay đổi so với bản trước và là nguyên nhân gốc của bảng trên.
5. ✏️ **Đọc anchor đã dùng trước khi viết**, chọn biến thể chưa ai dùng. Script ngay dưới.
6. ✏️ **Mỗi bài chỉ 1 anchor trỏ pillar**, không lặp anchor đó trong cùng bài.
7. 📊 **Mục tiêu: anchor khác nhau / tổng link tới 1 pillar >= 70%.** Con số lấy từ 2 pillar đã tự
   nhiên đạt (77% và 78%), nên là mốc chạm được chứ không phải ngưỡng ngành đi mượn.

**Đọc anchor đã dùng, chạy TRƯỚC khi viết đoạn Related reading:**

```python
import json, urllib.request, re, html, collections

def anchors_to(slug):
    """Moi anchor text dang tro toi slug nay, tu toan bo bai tren site."""
    out, page = [], 1
    while True:
        b = json.load(urllib.request.urlopen(
            "https://infina.ai/news/wp-json/wp/v2/posts"
            "?per_page=100&page=%d&_fields=id,content" % page))
        if not b:
            break
        for p in b:
            for sl, t in re.findall(
                    r'<a[^>]+href="https://infina\.ai/news/([a-z0-9-]+)/?"[^>]*>(.*?)</a>',
                    p["content"]["rendered"], re.S | re.I):
                if sl == slug:
                    out.append(html.unescape(re.sub("<[^>]+>", "", t)).strip())
        if len(b) < 100:
            break
        page += 1
    return out

a = anchors_to(PILLAR_SLUG)
uniq = set(x.lower() for x in a)
print("%d link, %d anchor khac nhau (%.0f%%)" % (len(a), len(uniq), len(uniq)/max(len(a),1)*100))
for t, n in collections.Counter(x.lower() for x in a).most_common(10):
    print("  %2dx  %s" % (n, t))
# Chon anchor KHONG nam trong danh sach tren.
```

**Bốn hướng tạo biến thể**, để không phải nghĩ lại từ đầu mỗi lần. Ví dụ với pillar CRM:

| Hướng | Ví dụ anchor |
|---|---|
| Theo vai trò người đọc | `CRM platforms built for brokerage teams` |
| Theo vấn đề bài đích giải quyết | `how to pick a CRM when leads go cold` |
| Theo định dạng bài đích | `our side-by-side CRM comparison` |
| Theo đúng phần trong bài đích | `the automation scoring breakdown` |

Cả bốn đều mô tả đúng trang đích mà không trùng nhau, và không cái nào cần chứa `PILLAR_KW` nguyên văn.

**Nguồn:** [Google Search Central, Make your links crawlable](https://developers.google.com/search/docs/crawling-indexing/links-crawlable) cho quy tắc 1-3. [Zyppy, 23 Million Internal Links](https://zyppy.com/seo/internal-links-study/) cho việc đa dạng anchor tương quan mạnh với clicks, lưu ý đó là nghiên cứu tương quan. Mốc 70% là quyết định biên tập.


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

# Dùng trước khi publish: LUÔN truyền seo_title, không chỉ content:
seo = check_seo(CONTENT, FOCUS_KW, SEO_TITLE, PILLAR_KW, PILLAR_URL)
if not seo["ok"]:
    print("SEO issues:", seo["issues"])
    # Sửa CONTENT/SEO_TITLE trước khi gọi create_post — vd: thêm FOCUS_KW nguyên văn vào 1 H2 và vào SEO_TITLE
```

**Cách viết SEO_TITLE và H2 chứa FOCUS_KW mà vẫn tự nhiên:** vì FOCUS_KW nhiều khi là cụm dài (vd `"tcpa compliance for real estate agents"`), khi diễn giải lại bằng từ đồng nghĩa hoặc chèn thêm từ ở giữa (vd viết thành `"tcpa compliance among real estate agents"`) sẽ làm mất match chính xác — Rank Math và hàm check ở trên đều tìm **substring y hệt**, không hiểu đồng nghĩa. Luôn giữ FOCUS_KW làm 1 cụm liền mạch trong ít nhất 1 câu của SEO_TITLE và 1 H2, phần diễn giải tự nhiên đặt trước/sau cụm đó chứ không chen vào giữa.

**Nếu density thấp:** thêm các đoạn tự nhiên sử dụng FOCUS_KW (cụm liền mạch, không chèn từ ở giữa) vào body sections.
**Nếu thiếu internal link:** thêm đoạn "Related reading" trước Final Thoughts với ≥2 link đến bài trong infina.ai/news, trong đó có 1 link chính xác trỏ về `PILLAR_URL`, anchor mô tả đúng pillar và chưa trùng anchor bài khác.
**Nếu thiếu external link:** đảm bảo link tới URL nguồn tin và website các tool đề cập trong bài không có `rel="nofollow"` với nguồn tin (được phép nofollow với tool/vendor link).
**Nếu FOCUS_KW trùng PILLAR_KW:** đây là lỗi cannibalization — quay lại Bước 4 chọn cluster keyword khác, không sửa bằng cách đổi PILLAR_KW.

---

## Bước 6: Xác định thời điểm publish + Publish lên WordPress

Lấy giờ bài `status=publish` gần nhất trên WordPress (từ `posts` ở Bước 2), tính `target = giờ_bài_gần_nhất + 1 tiếng`:
- Nếu `target` đã ở quá khứ so với giờ hiện tại → `create_post` với `status: "publish"` (publish ngay).
- Nếu `target` còn ở tương lai → `create_post` với `status: "future"` và `date = target` (format `"YYYY-MM-DD HH:MM:SS"`, KHÔNG phải ISO có chữ T) để lên lịch thay vì publish ngay.

⚠️ **Featured image = `IMG["STATS"]`, KHÔNG phải `IMG["HERO"]`.** Xem `THUMBNAIL_BEST_PRACTICES.md` (cùng thư mục skill) — ảnh HERO (photorealistic người ngồi laptop) lặp lại gần như y hệt qua các bài khiến trang chủ nhìn "toàn ảnh giống nhau", đây chính là vấn đề đợt audit toàn site trước đó đã sửa cho các bài cũ. Ảnh HERO vẫn tạo và chèn trong content như bình thường (đầu bài), chỉ riêng featured image/thumbnail dùng STATS.

⚠️ **GATE trước khi publish: mọi link nội bộ phải trỏ tới URL trả 200.** Chạy trên `CONTENT`
lúc nó còn là chuỗi, **trước** `create_post`. Fail ở đây không tốn gì vì chưa có gì lên site, khác hẳn
một `assert` hậu publish.

```python
import re, urllib.request, urllib.error

class _NoRedirect(urllib.request.HTTPRedirectHandler):
    def redirect_request(self, *a, **k): return None
_opener = urllib.request.build_opener(_NoRedirect)

def _probe(sl):
    r = _opener.open(urllib.request.Request(
        "https://infina.ai/news/%s/" % sl,
        headers={"User-Agent": "Mozilla/5.0"}), timeout=40)
    return r.status, ""

def check_targets(html_str, allow=()):
    """{slug: (ma_http, slug_dich_CUOI_CUNG)} cho moi link noi bo KHONG tra 200.

    allow: cac slug duoc phep 404 vi bai do dang status=future, se tu lanh.
    """
    bad = {}
    for sl in sorted(set(re.findall(
            r'href="https://infina\.ai/news/([a-z0-9-]+)/?"', html_str))):
        cur, code, first, hops = sl, None, None, 0
        while hops < 5:
            try:
                code, _ = _probe(cur)
                break
            except urllib.error.HTTPError as e:
                code = e.code
                first = first if first is not None else e.code  # ma cua chang DAU
                loc = e.headers.get("Location", "")
                nxt = loc.replace("https://infina.ai/news/", "").strip("/")
                # go het chuoi redirect de in ra DICH CUOI, khong phai hau dau tien
                if e.code in (301, 302, 307, 308) and nxt and nxt != cur:
                    cur, hops = nxt, hops + 1
                    continue
                break
        if code == 200 and cur == sl:
            continue
        if code == 404 and sl in allow:
            continue
        bad[sl] = (first if first is not None else code, cur if cur != sl else "")
    return bad

# SCHEDULED_OK: slug cua bai da len lich ma ta co y link sang (xem ghi chu duoi)
bad = check_targets(CONTENT, allow=SCHEDULED_OK)
assert not bad, "link tro vao URL khong tra 200: %s" % bad
```

⚠️ **Phải đo bằng HTTP, đừng đối chiếu với danh sách bài đã merge trong `content-plan.md`.** Cách
đọc tài liệu đã sai thật ngày 08/10: nó báo 10 link hỏng trong khi con số thật là **26**, và còn kê oan
một trang đang sống thành stub. Tài liệu luôn trễ hơn site; mã HTTP trả về thì không.

`check_targets` **gỡ hết chuỗi redirect rồi mới in đích**. Phải thế vì có stub 2 hầu thật trên site
(`top-crm-tools-real-estate-teams` → `top-crm-tools-for-real-estate-teams` → `best-crm-for-real-estate`);
bản đầu chỉ in hầu đầu tiên, sửa theo nó là rơi vào một stub khác.

`SCHEDULED_OK` là danh sách slug được phép 404: bài đã `status=future` mà ta **cố ý** link sang, nó tự
lành đúng giờ publish. Tiền lệ là cặp #1487/#1488: hai bài viết cùng lúc, lên lịch cách nhau 1 ngày,
#1487 link sang #1488 ngay từ đầu. Để rỗng `SCHEDULED_OK = []` khi không có trường hợp đó, đừng
dùng nó để làm ngơ một slug gõ sai. Chiều ngược lại (bài khác trỏ **vào** bài chưa live) vẫn phải
chờ, xem Bước 6.5.

Khi `check_targets` báo một slug `301`, sửa `href` sang slug đích mà nó in ra, **rồi đọc lại anchor**:
nếu anchor là tên nguyên văn của trang cũ (kiểu `Best AI Chatbot for Real Estate Lead Capture`) thì
phải viết lại cho mô tả đúng trang đích, vì trang mang tên đó không còn tồn tại. Đã phải sửa 5 anchor
kiểu này ngày 08/10.

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

## Bước 6.5: Bảo đảm bài mới có inbound link biên tập (BẮT BUỘC, không được bỏ)

Bước 5 đã cho bài mới link LÊN pillar và link ngang sang 2-3 bài cùng cụm. Chiều còn thiếu là **có
trang nào đó trỏ TỚI bài mới**, và nó không tự xảy ra: mọi bài khác trên site đều viết trước nó.

**Đây không phải lo xa.** Audit 2026-10-07 bằng `scripts/competitor_teardown.py` chạy trên chính
`infina.ai/news`: 35/130 trang không có inbound biên tập nào, 23 trong đó là bài bất động sản thật.
Nguyên nhân duy nhất là skill này trước đây kết thúc ở Bước 7 mà không có bước này.

### Số link: không có ngưỡng nào đến từ Google

⚠️ **Mục này trước 2026-10-08 có bảng ngưỡng "3-5 link mỗi 1.000 chữ, nới tới 8" kèm bảng quy đổi
theo độ dài. Đã gỡ.** Nguồn của nó là blog AirOps và Wellows, không phải Google. Đừng dựng lại.

**Thứ Google thật sự nói:**

- Không có giới hạn số link trên 1 trang. Quy tắc "100 link mỗi trang" bỏ từ 2008, vốn là giới hạn
  kỹ thuật thời Googlebot chỉ tải khoảng 100KB đầu trang.
- Quá nhiều internal link làm loãng **cấu trúc site**, không làm yếu từng link. Mueller nói điều này
  ở hangout 02/07/2021 và **không kèm con số nào**.

Mốc vận hành của riêng site này nằm ở bảng "Mốc vận hành đi kèm" bên dưới. Đó là quyết định biên tập,
sửa được, không phải thứ Google đo.

⚠️ **Dù vậy, đừng áp con số tuyệt đối lên bài ngắn.** Lỗi này xảy ra thật ngày 2026-10-07: lấy
"20-40 link cho pillar" áp lên pillar 1.832 chữ rồi kết luận nhầm là "đang thiếu link". Sai hai tầng:
sai vì dùng số tuyệt đối thay vì chia cho độ dài, và sai vì bản thân con số đó không có cơ sở. Khi
so sánh thì chia cho số chữ, và so với **chính các bài khác trên site**.

**Độ dài pillar: suy ra từ SỐ CLUSTER, đừng đặt mục tiêu số chữ.**

⚠️ **Word count không phải ranking factor.** John Mueller: "Word count is not a ranking factor, save
yourself the trouble." Danny Sullivan (2023): "The best word count needed to succeed in Google
Search is not a thing, it doesn't exist." Mọi con số dưới đây là **mốc vận hành để tự soi**, không
phải thứ Google đo. Bài dài rank tốt vì phủ chủ đề đủ và hút backlink, không phải vì dài.

Logic đúng: pillar cần đủ section để tóm tắt **mọi subtopic trong cụm của nó, không hơn**. Pillar
phủ 8 cluster đương nhiên ngắn hơn pillar phủ 30. Kết hợp với chuẩn "mỗi subtopic 100-200 chữ tóm
tắt rồi link ra bài sâu":

```
do_dai_pillar ~= 400 (mo bai) + 150 x so_cluster + 200 (ket)
```

| Số cluster | Độ dài suy ra |
|---|---|
| 8 | ~1.800 chữ |
| 15 | ~2.950 chữ |
| 25 | ~4.350 chữ |
| 30 | ~5.100 chữ |

Khoảng tham khảo của ngành là **2.000-5.000 chữ, sweet spot quanh 3.000**, và nó chính là hệ quả
của công thức trên khi cụm có 10-30 bài. Nếu pillar của bạn rơi ngoài khoảng đó, kiểm tra số cluster
trước khi kết luận bài quá ngắn hay quá dài.

**Pillar quá tải cụm thì tách, đừng viết dài vô hạn.** Chuẩn ngành là 8-15 cluster mỗi pillar. Vượt
xa mức đó (ví dụ 40+) thì công thức sẽ đòi 6.000-7.000 chữ, lúc đó bài thành không đọc nổi. Giải
pháp đúng là tách thành nhiều sub-hub, mỗi hub 10-15 cluster.

**Mốc vận hành đi kèm** (quyết định biên tập của site này, không phải ngưỡng Google):

| Chỉ số | Mốc |
|---|---|
| Độ dài bài cluster | 1.200-2.000 chữ |
| Số bài cluster trên 1 pillar | 8-15, vượt 20 thì cân nhắc tách sub-hub |
| Bài cluster link lên pillar | đúng 1 lần, không lặp |
| Bài cluster link ngang cùng cụm | 2-3, chọn theo độ gần chủ đề |
| Tổng link nội bộ, bài ~1.000 chữ | 4-6 |
| Pillar link tới cluster | mỗi cluster đúng 1 lần, không lặp |
| Link tới money page | 1-3 lần, đặt ở chỗ intent mua cao nhất (sau phần so sánh, đánh giá, kết luận) |
| Money page nhận inbound | 10-20 link từ các trang liên quan |

**Google không có giới hạn số link trên 1 trang.** Quy tắc "100 link mỗi trang" đã bỏ từ 2008, vốn
là giới hạn kỹ thuật thời Googlebot chỉ tải khoảng 100KB đầu trang. John Mueller khẳng định nhiều
lần không có con số cứng. Mọi ngưỡng trên là mốc tham chiếu để tự soi, không phải luật.

**Hiện trạng site tại 2026-10-07**, đo bằng link nội bộ unique chia cho số chữ thân bài:

| Pillar | Chữ | Link | /1.000 chữ | |
|---|---|---|---|---|
| `best-crm-for-real-estate` | 4.253 | 21 | 4,9 | vừa, sau khi mở rộng 07/10 |
| `real-estate-lead-follow-up-automation-guide` | 2.460 | 11 | 4,5 | vừa, sau khi mở rộng 07/10 |
| `tcpa-compliance-for-real-estate-agents` | 1.180 | 8 | 6,8 | vừa |
| `ai-crm-real-estate` | 1.656 | 10 | 6,0 | vừa |
| `real-estate-agent-crm-speed-to-lead` | 1.498 | 7 | 4,7 | vừa |
| `real-estate-website-builder` | 3.016 | 14 | 4,6 | vừa |
| `crm-pipeline-management` | 1.682 | 5 | 3,0 | thiếu |
| `best-ai-virtual-assistant-real-estate` | 1.794 | 5 | 2,8 | thiếu |

Đọc bảng này cho đúng: vấn đề không nằm ở số link mà ở **tỷ lệ giữa độ dài pillar và số cluster nó
thật sự gánh**.

⚠️ **Đếm số cluster bằng số inbound link là SAI.** Thử ngày 07/10/2026: `#207` nhận 47 inbound, nếu
coi đó là 47 cluster thì công thức đòi 7.650 chữ và kết luận "pillar quá tải, phải tách". Soi kỹ thì
**28 trong 47 bài đó còn link lên pillar của cụm khác**, tức chúng là link chéo cụm (bài IDX, landing
page, web design tham chiếu sang CRM), không phải thành viên Cụm 2. Đổi sang đếm "chỉ link lên đúng
1 pillar" lại hụt ngược, vì bài cluster hợp lệ mà có link chéo sẽ bị loại oan.

**Kết luận phương pháp: không suy ra thành viên cụm từ link graph.** Nguồn đúng duy nhất là bảng
phân cụm trong `content-plan.md`, nơi mỗi bài được gán cụm bằng quyết định biên tập. Link graph
dùng để đo sức khoẻ link (inbound, outbound, mồ côi), không dùng để định nghĩa cụm.

Số liệu đúng lấy từ `content-plan.md` ngày 07/10/2026:

| Cụm | Cluster (KHÔNG tính pillar) | Pillar | Chữ pillar | Cần có | Chênh |
|---|---|---|---|---|---|
| Cụm 2 CRM Software | 25 | `best-crm-for-real-estate` | 4.253 | 4.350 | **-97 đạt** |
| Cụm 1 Chatbot | 13 trên **2 pillar** | A `best-conversational-ai-chatbot-for-real-estate` 3.030, B `best-chatbot-customer-service-real-estate` 3.991 | | 1.500 mỗi pillar | **đạt cả hai** |
| Cụm 3 Website Builder / IDX | 13 | `real-estate-website-builder` | 3.016 | 2.550 | **+466 đạt** |
| Cụm 7 Lead Generation | 9 | `real-estate-lead-follow-up-automation-guide` | 2.460 | 1.950 | **+510 đạt** |
| Cụm 4 AI Voice | 6 | `best-ai-voice-assistants-for-real-estate` | 2.251 | 1.500 | **+751 đạt** |
| Cụm 5 Website / Web Design | 6 | `website-design-for-real-estate-agents` | 1.812 | 1.500 | **+312 đạt** |
| Cụm 6 Landing Pages | 5 | `real-estate-landing-page-guide` | 1.889 | 1.350 | **+539 đạt** |
| Cụm 8 Compliance | 5 | `tcpa-compliance-for-real-estate-agents` | 1.919 | 1.350 | **+569 đạt** |

⚠️ Cột thứ 2 là **số cluster đã trừ pillar**. Vài dòng trong bảng này được lập trước khi làm rõ
điểm đó nên có thể còn lệch 1 cluster, tức lệch 150 chữ ở cột "Cần có". Đích là sàn chứ không phải
con số chính xác, và mọi pillar đã sửa đều vượt sàn có biên, nên không đáng đi tính lại cả bảng.
Khi dùng cho 1 cụm cụ thể thì đếm lại từ `content-plan.md`.

Năm cụm đã đạt. Hai pillar yếu nhất đều được mở rộng ngày 07/10, xem `content-plan.md` mục Cụm 2
và Cụm 7 cho bảng từng bước: Cụm 2 từ 1.832 lên 4.253 chữ qua 4 lần `update_post`, Cụm 7 từ 722 lên
2.460 chữ qua 3 lần. Cả 8 cụm giờ đều đạt sàn độ dài pillar.

⚠️ **Đếm cluster cho đúng: "N bài sống" trong `content-plan.md` đã GỒM pillar.** Cụm 6 từng bị
ghi là cần 1.500 chữ vì lấy thẳng "6 bài" làm số cluster, trong khi thật ra là 1 pillar + 5
cluster nên đích đúng là 1.350. Trừ pillar ra trước khi nhân 150.

⚠️ **Cụm có 2 pillar thì phải chia số cluster ra trước khi áp công thức.** Cụm 1 từng bị ghi là hụt
269 chữ vì dồn cả 13 cluster lên 1 pillar. Thực tế cụm này có 2 pillar song song, mỗi pillar gánh ~6
cluster nên chỉ cần 1.500 chữ, và cả hai đều đã vượt từ trước. Kiểm tra số pillar trong
`content-plan.md` trước khi kết luận một cụm thiếu độ dài.

⚠️ **Độ dài đạt không có nghĩa pillar khoẻ.** Audit Cụm 1 ngày 07/10 cho thấy cả 2 pillar đều thừa
chữ nhưng Pillar A có **0 link ngoài** (fail Rank Math) và **7/8 link nội bộ dồn trong
`<h3>Related Reading</h3>`**, Pillar B chỉ 1,9 link/1.000 chữ. Đo đủ bộ: độ dài, link/1.000 chữ, tỷ
lệ link trong thân bài, số link ngoài, density, dash.

⚠️ **Bài tư vấn pháp lý thì verify claim TRƯỚC khi viết thêm, không phải sau.** Ngày 07/10, lúc
chuẩn bị mở rộng pillar Cụm 8, phát hiện claim nổi bật nhất của bài là sai: nó mô tả quy tắc FCC
one-to-one consent như đang có hiệu lực, trong khi quy tắc đó **đã bị Toà Phúc thẩm Khu vực 11 huỷ
tháng 01/2025, vài ngày trước ngày có hiệu lực**. Bài đã sống như vậy nhiều tháng. Nếu lúc đó chỉ lo
thêm chữ cho đủ sàn thì sẽ viết thêm 700 chữ xây trên nền sai.

Quy tắc rút ra: với bài compliance/legal/tax/medical, **mỗi claim quy phạm phải verify bằng WebFetch
tới nguồn thật trước khi đụng vào bài**, và riêng nhóm này thì đọc trang nguồn chứ không tin bản tóm
tắt của WebSearch. Chi tiết vụ việc trong `content-plan.md` mục Cụm 8.

⚠️ **Mở link ra đọc, đừng chỉ tin câu văn quanh nó.** Rà 5 bài cluster Cụm 8 ngày 07/10 cho thấy
loại lỗi phổ biến nhất ở cluster không phải sai luật mà là **sai trích dẫn**, và nó vô hình khi đọc
lướt vì câu văn nghe hợp lý: #1481 có câu "NAR đang đẩy tài liệu chống gian lận cho hội viên" nhưng
link lại trỏ tới trang NAR về pre-marketing/coming-soon listings, chẳng liên quan gì; #1260 gọi sai
tên nghiên cứu của ALTA. Khi rà, mở từng link ngoài và hỏi: trang này có thật sự nói điều mà câu văn
đang gán cho nó không?

⚠️ **Kiểm tra link có trỏ vào stub 301 không, bằng `check_targets()` ở Bước 6.** Mỗi lần sửa bài
cũ cũng chạy hàm đó trên nội dung mới trước khi ghi. Link qua redirect vẫn chạy nhưng loãng tín hiệu
và sẽ chết khi dọn redirect.

Đợt rà 08/10 tìm ra **26 link đi qua 301** trên 20 bài, trong đó 1 link đi qua **2 hầu**
(`top-crm-tools-real-estate-teams` → `top-crm-tools-for-real-estate-teams` → `best-crm-for-real-estate`).
Đã sửa hết, xem `post-refresh/references/refresh-log.md`.

⚠️ **Regex đếm heading phải cho phép attribute.** `<h2>(.*?)</h2>` bỏ sót `<h2 id="...">`, khiến
lần đo đầu tiên của Pillar B báo nhầm "chỉ có 1 H2" trong khi thật sự có 8. Luôn dùng
`<h2[^>]*>(.*?)</h2>`.

⚠️ **Độ dài pillar đạt không có nghĩa cả cụm đã khoẻ.** Audit Cụm 7 sau khi vá pillar cho thấy 7
trong 8 bài cluster chỉ dài 536-766 chữ, so với chuẩn cluster 1.200-2.000. Đo pillar xong thì đo
luôn phân bố độ dài của cluster, đừng dừng ở con số pillar.

Không cụm nào vượt 25 bài, nên **chưa cụm nào cần tách sub-hub**. Việc cần làm là viết dài pillar
cho đủ vai trò, không phải chia nhỏ cụm.

Cách tự đo nhanh:

```python
import re, json, urllib.request
c = json.load(urllib.request.urlopen(
    f"https://infina.ai/news/wp-json/wp/v2/posts/{POST_ID}?_fields=content"
))["content"]["rendered"]
t = re.sub("&[a-z#0-9]+;", " ", re.sub("<[^>]+>", " ", c))
words = len(re.findall(r"[A-Za-z0-9,.%$-]+", t))
links = len(set(re.findall(r'href="https://infina\.ai/news/([a-z0-9-]+)/"', c)))
print(f"{words} chu, {links} link, {links/words*1000:.1f}/1000 chu")
```

### Đặt link ở đâu: ưu tiên biên tập, không phải quy tắc SEO

⚠️ **Mục này trước 2026-10-08 nói ngược.** Nó dựng bảng 3 mức giá trị theo vị trí link (thân bài >
Related Reading > footer) và chống lưng bằng patent reasonable surfer. Mueller bác thẳng:

> "We don't really differentiate there."
>
> John Mueller, [SEJ 03/2022](https://www.searchenginejournal.com/are-internal-links-in-header-and-footer-treated-differently/441993/), về link ở header, footer, sidebar so với thân bài.

**Vậy còn lý do gì để ưu tiên link thân bài?** Hai lý do, đều là biên tập chứ không phải SEO:

1. **Anchor text bám ngữ cảnh.** Link giữa đoạn được viết thành câu có lý do, nên anchor mô tả đúng
   thứ nằm ở đầu kia. Link trong danh sách cuối bài hay bị rút thành tiêu đề trần.
2. **Người đọc đang ở đúng chỗ.** Link đặt ngay lúc nhắc tới chủ đề thì gặp người đang quan tâm chủ
   đề đó, khác với một danh sách đọc thêm sau khi họ đã đọc xong.

Nên đây là **ưu tiên lúc viết**, không phải điều kiện pass/fail. Đừng dựng lại ngưỡng phần trăm
quanh nó.

**Thứ Google có nói, và là ràng buộc thật:** quá nhiều internal link làm loãng **cấu trúc site**.

> "If every page links to every other page, then there's no real structure there."
>
> John Mueller, hangout 02/07/2021, [SEJ](https://www.searchenginejournal.com/google-cautions-against-using-too-many-internal-links/412553/).

Ông **không đưa ra con số nào**. Ràng buộc này nhắm vào **phân bố link trên toàn site**, không nhắm
vào từng bài, và nó chính là lý do Bước 6.5 chọn sibling thay vì dồn mọi bài news vào pillar.

**Số đo hiện trạng, giữ lại làm quan sát chứ không phải đích:** ngày 07/10/2026 trên 113 bài của
`infina.ai/news`, 41% link nội bộ nằm trong thân bài, 59% dồn vào Related Reading và Final Thoughts.

**TOC không thuộc nhóm này.** Mục lục thường là anchor nhảy trong cùng trang (`#heading`), phục vụ
UX và featured snippet, không phải internal linking, trừ khi nó link thẳng sang các trang cluster.

### Ba việc bắt buộc, theo thứ tự rẻ tiền trước

**1. Link ngang sang 2-3 bài cùng cụm, ĐẶT TRONG THÂN BÀI, làm ngay lúc viết (Bước 5).** Rẻ nhất vì
không phải sửa bài nào khác, và mạnh nhất vì nằm trong ngữ cảnh. Chọn bài cùng cụm có chủ đề gần
nhất, chèn vào đúng đoạn đang nói về chủ đề đó, viết thành câu có lý do để người đọc bấm chứ không
liệt kê tiêu đề. Đây là việc quan trọng nhất trong cả Bước 6.5.

**2. Link lên pillar.** Bước 5 đã làm, chỉ cần verify lại.

**3. Cho bài mới một inbound link biên tập.** Đây là việc duy nhất ở Bước 6.5 mà bài mới không tự
làm được, và là lý do bước này tồn tại: mọi bài khác trên site đều viết trước nó.

⚠️ **Nguồn ưu tiên là một bài cluster cùng cụm, KHÔNG phải pillar.** Trước 2026-10-08 bước này luôn
nối thêm một câu vào pillar. Cách đó sai ở hai chỗ:

- Lý do cũ là "link từ pillar mạnh hơn vì pillar có authority". Mueller 03/2022 bác thẳng: vị trí và
  trang nguồn không làm Google đánh giá link khác đi.
- Nó cộng dồn vĩnh viễn. Mỗi bài news lại thêm 1 link vào cùng 1 pillar, nên `#207` lên tới 22 link
  nội bộ. Đúng cái Mueller cảnh báo: site mà trang nào cũng link tới trang nào thì không còn cấu
  trúc thật. Chọn sibling thì tải phân tán ra cả cụm và pillar đứng yên.

**Tiêu chí chọn bài donor, theo thứ tự:**

1. Cùng cụm theo `content-plan.md`. Không suy ra từ link graph, xem cảnh báo ở trên.
2. **Có sẵn một đoạn đang nói đúng chủ đề của bài mới**, chèn vào đó thành câu có lý do để bấm.
   Không có đoạn nào như vậy thì loại bài đó ra, đừng ép. Đây là tiêu chí quyết định.
3. Chưa link sang bài mới.
4. Ưu tiên bài đã có traffic (Bước 8), vì link ở đó có người đọc thật đi qua.

**Đường lui:** không bài cluster nào trong cụm đạt tiêu chí 2 thì mới dùng pillar, theo đúng cách cũ.
Hay gặp với cụm mới hoặc chủ đề lần đầu xuất hiện. Lui về pillar là hợp lệ, không phải thất bại.

Dù chọn bài nào, `update_post` ghi đè toàn bộ field `content` nên phải fetch full content trước:

```python
import urllib.request, json
did = DONOR_POST_ID          # bai cluster cung cum, hoac PILLAR_POST_ID neu phai lui
cur = json.load(urllib.request.urlopen(
    f"https://infina.ai/news/wp-json/wp/v2/posts/{did}?_fields=id,slug,content"
))["content"]["rendered"]

# ANCHOR la nua cau cuoi cua doan muon chen vao, COPY NGUYEN VAN tu cur.
ANCHOR = "...thay bang doan that trong bai donor..."
ADD = (f' Goc tin moi nhat o <a href="https://infina.ai/news/{SLUG}/">{FOCUS_KW}</a>.')
assert cur.count(ANCHOR) == 1, "ANCHOR khong duy nhat, chon doan cu the hon"
call("update_post", {"post_id": did, "content": cur.replace(ANCHOR, ANCHOR + ADD)})
```

⚠️ `ANCHOR` phải **duy nhất** trong bài donor. Đừng dùng `"</p>"` hay `"<h2>"`: chúng xuất hiện hàng
chục lần và `replace` sẽ chèn link vào mọi đoạn. Copy nguyên văn nửa câu cuối của đoạn muốn chèn.

Nếu phải lui về pillar mà pillar chưa có section "Related Reading" thì tạo mới ngay trước "Final
Thoughts". Audit 07/10 cho thấy 4 trên 5 pillar lớn vốn **không có section này**, và đó là lý do
chúng không bao giờ link xuống bài con.

### Verify bằng REST, không tin tool báo thành công

Tách làm 2 làn. **GATE** là thứ hỏng thật và script tự sửa được, `assert` chặn. **WARN** là phán đoán
biên tập, chỉ in ra rồi ghi kèm vào dòng tracker ở Bước 7.

⚠️ **Sau khi đã publish, không `assert` nào được phép abort.** Bài đã lên mà script chết giữa chừng
thì Bước 7 không chạy và lần sau không ai biết. Mọi check hậu publish gom vào `warnings`. Session
2026-10-07 đã bị đúng lỗi này 2 lần: `assert` fail chặn script trước khi kịp ghi file.

```python
import re, json, urllib.request

def content(pid):
    return json.load(urllib.request.urlopen(
        f"https://infina.ai/news/wp-json/wp/v2/posts/{pid}?_fields=content"
    ))["content"]["rendered"]

def linked(from_id, to_slug):
    return f"/{to_slug}/" in content(from_id)

# --- GATE: fail la hong that, phai sua roi chay lai ---
assert linked(new_post_id, PILLAR_SLUG), "bai moi chua link len pillar"
assert sum(linked(new_post_id, s) for s in SIBLING_SLUGS) >= 2, "thieu link ngang"
assert linked(did, SLUG), "bai donor chua link sang bai moi, bai moi dang mo coi"

# --- WARN: chi ghi nhan, khong chan ---
warnings = []
c = content(new_post_id)
t = re.sub("&[a-z#0-9]+;", " ", re.sub("<[^>]+>", " ", c))
words = len(re.findall(r"[A-Za-z0-9,.%$-]+", t))
pat = r'href="https://infina\.ai/news/[a-z0-9-]+/"'
links = len(set(re.findall(r'href="https://infina\.ai/news/([a-z0-9-]+)/"', c)))
per_k = links / words * 1000

if c.count(f'href="https://infina.ai/news/{PILLAR_SLUG}/"') > 1:
    warnings.append("link len pillar lap lai, chi can 1 lan")

# anchor tro pillar co trung voi bai khac khong (anchors_to() o Buoc 5)
import html
ma = re.search(r'<a[^>]+href="https://infina\.ai/news/%s/?"[^>]*>(.*?)</a>' % PILLAR_SLUG,
               c, re.S | re.I)
if ma:
    mine = html.unescape(re.sub("<[^>]+>", "", ma.group(1))).strip().lower()
    dup = [x.lower() for x in anchors_to(PILLAR_SLUG)].count(mine) - 1
    if dup > 0:
        warnings.append(f"anchor '{mine}' da duoc {dup} bai khac dung, doi sang bien the khac")

# anchor cua CA cac link ngang, khong chi pillar
for sl in SIBLING_SLUGS:
    mb = re.search(r'<a[^>]+href="https://infina\.ai/news/%s/?"[^>]*>(.*?)</a>' % sl,
                   c, re.S | re.I)
    if not mb:
        continue
    a = html.unescape(re.sub("<[^>]+>", "", mb.group(1))).strip().lower()
    d = [x.lower() for x in anchors_to(sl)].count(a) - 1
    if d > 0:
        warnings.append(f"anchor '{a}' tro toi {sl} da duoc {d} bai khac dung")

m = re.search(r"<h2[^>]*>\s*(Related Reading|Final Thoughts)", c, re.I)
cut = m.start() if m else len(c)
body, tail = len(re.findall(pat, c[:cut])), len(re.findall(pat, c[cut:]))
print(f"{words} chu, {links} link, {per_k:.1f}/1000 chu, than bai {body} / cuoi bai {tail}")

if body < tail:
    warnings.append(f"qua nua link don o cuoi bai ({body} than / {tail} cuoi)")
if per_k > 9:
    warnings.append(f"mat do {per_k:.1f}/1000 chu, lech han so voi phan con lai cua site")

for w in warnings:
    print("WARN:", w)
```

**Hai ngưỡng trong khối WARN, và vì sao chúng chỉ là WARN:**

- `body < tail` là **sở thích biên tập**, không phải chuẩn SEO. Link thân bài có anchor bám ngữ cảnh
  cụ thể hơn và nằm đúng chỗ người đọc đang quan tâm, nhưng Google **không** đánh giá nó cao hơn.
  Tới 2026-10-08 đây còn là một `assert` chặn script, dựa trên bảng 3 mức giá trị đã bị gỡ ở trên.
  Chính nó khiến `#214` (45% thân bài) từng bị gọi nhầm là lỗi SEO.
- `9/1.000` **không phải ngưỡng SEO**, mà là mốc so với chính site này: 8 pillar đo ngày 07/10 nằm
  trong khoảng 2,8-6,8/1.000. Vượt 9 nghĩa là bài lệch hẳn khỏi phần còn lại nên đáng nhìn lại, chứ
  không đáng chặn. Đo lại phân bố site rồi chỉnh mốc này mỗi khi chạy teardown định kỳ.

### Ba lưu ý

- **Bài đang `status: future` thì hoãn chiều inbound.** Slug chưa live, trỏ bài khác vào URL còn
  404 là hại. Đặt lịch quay lại sau giờ publish, và ghi `⏳ còn thiếu link ngược` vào
  `content-plan.md` để không quên. Riêng link ngang thì làm được ngay vì nó nằm trong bài mới.
- **Density của bài donor đổi sau khi nối thêm câu.** Tính lại focus keyword của chính bài donor,
  dưới 0,5% thì chèn thêm 1 lần tự nhiên ngay trong đoạn vừa sửa.
- **Mồ côi ở đây nghĩa là thiếu inbound BIÊN TẬP, không phải Google không thấy bài.** Mọi bài đều
  nằm trong category archive `/news/category/<slug>/`, và archive đó là `index, follow` nên vẫn tạo
  đường crawl. Vá link vẫn đáng làm vì nó là tín hiệu topical relevance và dòng PageRank thật,
  nhưng đừng báo cáo nhầm thành "bài bị rớt khỏi index".

### Kiểm tra định kỳ

Mỗi 10-15 bài publish, chạy lại script teardown trên chính site mình:

```bash
python3 wordpress-mcp/scripts/competitor_teardown.py infina.ai --path /news/
```

Số trang `IN=0` phải đi ngang hoặc giảm. Nếu nó tăng theo số bài publish thì Bước 6.5 đang bị bỏ.

### Nguồn

**Đã xác minh, từ phát ngôn của Google:**

- [SEJ, Are Internal Links In Header And Footer Treated Differently?](https://www.searchenginejournal.com/are-internal-links-in-header-and-footer-treated-differently/441993/) (03/2022). John Mueller: *"We don't really differentiate there."* Vị trí link trên trang (header, footer, sidebar, thân bài) **không** làm Google đánh giá link khác đi.
- [SEJ, Google Cautions Against Using Too Many Internal Links](https://www.searchenginejournal.com/google-cautions-against-using-too-many-internal-links/412553/) (hangout 02/07/2021). Quá nhiều internal link làm loãng **cấu trúc site**, không làm yếu từng link. Mueller **không đưa ra con số nào**; con số "20 link" trong bài đó là của tác giả.
- [Search Engine Roundtable, There Is No Limit To The Number Of Links Per Page](https://www.seroundtable.com/google-link-unlimited-18468.html). Quy tắc 100 link bỏ từ 2008.
- [Search Engine Roundtable, Google Says Word Count Is Not A Ranking Factor](https://www.seroundtable.com/google-word-count-is-not-a-ranking-factor-27994.html). Mueller và Sullivan.
- [SEJ, Content Length: Is It a Google Ranking Factor?](https://www.searchenginejournal.com/ranking-factors/content-length/). Tương quan không phải nhân quả.

**KHÔNG được dùng làm căn cứ ngưỡng.** Liệt kê ở đây để lần sau không ai vô tình trích lại:

- LinkWhisper "20-40 link cho pillar", Wellows "1 link mỗi 200-300 chữ", AirOps "3-5 link mỗi 1.000 chữ", eesel "2-3 link ngang mỗi cluster". Cả bốn là blog vendor, không có nguồn Google chống lưng, và cả bốn từng được dùng làm ngưỡng cứng trong chính file này cho tới 2026-10-08. Đây đúng loại nguồn mà quy trình vẫn gỡ khỏi bài publish, nên không được dùng để gác script.
- [Reasonable surfer patent US8117209B1](https://patents.google.com/patent/US8117209B1/en). Nộp 2004, Google **chưa bao giờ xác nhận** đang chạy theo nó. Không dùng để biện minh cho việc xếp hạng giá trị link theo vị trí.
- Headline SEJ 2020 "Links in Primary Content Hold More Value" là **suy diễn của tác giả**. Mueller chỉ nói Google tập trung vào primary content, không nhắc link, ranking hay PageRank.

---

## Bước 7: Log kết quả vào Tracker Sheet

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

## Bước 8 (Optional): Kiểm tra traffic Google Search Console + Google Analytics

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
# ReferrerUrl, PopularPages, v.v.: moi metric 1 object trong list ket qua)
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

