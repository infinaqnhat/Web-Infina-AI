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

```python
import os, requests, base64, re, json

WP_URL = f"https://infina.ai/news/wp-json/infina-mcp/v1/blog?key={os.environ['WP_MCP_KEY']}"
GEMINI_KEY = os.environ["GEMINI_API_KEY"]
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

**Các method dùng được:**

| Method | Params chính | Ghi chú |
|--------|-------------|---------|
| `list_posts` | `status` (array, optional — bỏ trống = lấy tất cả 5 trạng thái), `number` (int, mặc định 20 — **truyền 500 để lấy hết**), `search` (string, optional) | Liệt kê bài viết. Cách DUY NHẤT thấy được bài `draft` |
| `create_post` | `title`*, `content`* (*bắt buộc), `status` (draft\|publish\|future), `date` (chỉ khi future, format `"YYYY-MM-DD HH:MM:SS"`), `slug`, `categories` (array tên string), `tags`, `seo_title`, `seo_description`, `seo_focus_keyword`, `image_url`, `image_alt` | Tạo bài |
| `update_post` | `post_id`* + bất kỳ field nào của create_post | Sửa bài đã tồn tại |
| `upload_media` | `image_url`* (phải là https), `alt`, `title` | Tải ảnh vào Media Library. **Không có param `filename`/`alt_text`** |
| `delete_media` | `media_id`* | Xoá vĩnh viễn 1 media |

**Response format:**

| Method | Response text (thành công) |
|--------|------|
| `list_posts` | mỗi bài 1 dòng: `#{id} [{status}] {title} ({date}) - {edit_url} \| {link}` |
| `create_post` | `Da tao bai ID {id} [status: {status}].{image_note} Sua: {edit_url} \| Xem: {link}` |
| `update_post` | `Da cap nhat bai ID {id} [status: {status}].{image_note} Sua: {edit_url} \| Xem: {link}` |
| `upload_media` | `Da tai anh. media_id: {id} \| source_url: {url}` |

---

## Image Pipeline

**Model mặc định:** `gemini-3.1-flash-lite-image` — $0.034/ảnh, native 1408×768 (~16:9)

```python
import io
from PIL import Image

IMAGE_MODEL = "gemini-3.1-flash-lite-image"

def nano_banana(prompt, model=IMAGE_MODEL):
    """Generate image, return JPEG bytes cropped to 16:9."""
    r = requests.post(
        f"https://generativelanguage.googleapis.com/v1beta/models/{model}:generateContent?key={GEMINI_KEY}",
        json={"contents": [{"parts": [{"text": prompt}]}],
              "generationConfig": {"responseModalities": ["IMAGE"]}},
        timeout=120,
    )
    parts = r.json()["candidates"][0]["content"]["parts"]
    for p in parts:
        if "inlineData" in p:
            img_bytes = base64.b64decode(p["inlineData"]["data"])
            img = Image.open(io.BytesIO(img_bytes))
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

def upload_to_freeimage(img_bytes):
    b64 = base64.b64encode(img_bytes).decode()
    r = requests.post("https://freeimage.host/api/1/upload",
        data={"key": FREEIMAGE_KEY, "action": "upload", "source": b64, "format": "json"},
        timeout=30)
    return r.json()["image"]["url"]

def upload_to_wp(img_url, alt, title):
    resp = call("upload_media", {"image_url": img_url, "alt": alt, "title": title})
    for part in resp.split("|"):
        part = part.strip()
        if part.startswith("source_url:"):
            return part.replace("source_url:", "").strip()
    raise Exception(f"Cannot parse: {resp}")
```

**Luồng:** `nano_banana(prompt)` → JPEG bytes → `upload_to_freeimage()` → URL → `upload_to_wp()` → WP media URL

Nếu freeimage.host lỗi 400 → upload thẳng URL tạm của Gemini vào `upload_to_wp()`, WP tự sideload.

Mỗi bài cần **4 ảnh**: HERO (human), STATS (diagram), DEMO (human/diagram), COMPARISON (diagram)

---

## Image Prompt System — Logic-Safe Rules

### 4 Rules

**Rule 1 — Camera angle first** — anchors spatial logic before model fills scene

**Rule 2 — Explicit gaze triplet** — who → looking at → what (confirm object faces subject)
> ✅ "eyes directed at laptop screen which faces her"

**Rule 3 — Lock hands** — specific position, not vague
> ✅ "right hand resting on trackpad, left hand on keyboard home row"

**Rule 4 — Negative guards at end** — always append NEGATIVE_GUARDS

### ⚠️ Lens Rule for 16:9
- **HERO images**: always use `35mm` or `24mm` wide-angle lens → landscape framing
- **AVOID `85mm f/1.4` for HERO** — portrait lens causes tall/portrait output even with PIL crop

### ⚠️ Screen Content — NO TEXT
```
✅ "CRM dashboard with colored bar charts and contact card grid"
✅ "warning UI with large yellow caution triangle icon on white background"
❌ "screen showing text: Speed-to-Lead Report 2026"
```

### build_human_prompt()

```python
CAMERA = {
    "over_shoulder_left":  "over-the-shoulder shot, camera positioned behind and slightly to the left of the subject",
    "over_shoulder_right": "over-the-shoulder shot, camera positioned behind and slightly to the right of the subject",
    "side_profile":        "side profile shot, camera at desk level to the subject's right",
    "three_quarter":       "3/4 front angle, camera slightly elevated, subject faces slightly left",
    "group_at_screen":     "wide shot, all subjects gathered on the viewer-facing side of the screen, camera faces the group from the front",
    "wall_display":        "camera faces the wall display from behind the group, subjects visible from the back and sides",
}
HANDS = {
    "laptop_typing":   "right hand resting on trackpad, left hand on keyboard home row, fingers naturally curved downward",
    "laptop_reading":  "both hands resting in lap or on desk edge, leaning slightly forward",
    "pointing_screen": "right index finger pointing toward the screen which faces the subject, arm extended naturally",
    "holding_phone":   "phone held vertically in right hand at chest height, screen facing subject",
    "pen_writing":     "pen held naturally between thumb and first two fingers of right hand, tip touching notepad",
    "mouse_click":     "right hand resting on mouse, index finger lightly on left button",
}
LENS = {
    "hero_wide":     "Shot on Sony alpha7R V, 35mm f/2.0 lens, wide environmental framing, moderate depth of field",
    "group_wide":    "Shot on Nikon Z9, 24mm f/2.8 lens, wide environmental shot, all subjects sharp",
    "portrait_hero": "Shot on Canon EOS R5, 85mm f/1.4 prime lens, shallow depth of field",  # ⚠️ avoid for HERO
    "detail_close":  "Shot on Canon EOS R5, 50mm f/1.8 macro-style, close crop on hands and screen",
}
QUALITY = (
    "wide 16:9 landscape composition, horizontal framing, "
    "warm natural office lighting, ultra-realistic DSLR photography, "
    "editorial quality, 8K resolution"
)
NEGATIVE_GUARDS = (
    "no screen facing away from user, no person looking the wrong direction, "
    "no extra fingers, no floating objects, "
    "no readable text on screen, no garbled letters, no mirrored text, "
    "no tablet facing camera instead of person holding it, "
    "no illustration, no cartoon, no vector art, no 3D render, no anime"
)

def build_human_prompt(camera, subject, gaze, hands, screen_content, environment, lens="hero_wide"):
    cam  = CAMERA.get(camera, camera)
    hand = HANDS.get(hands, hands)
    gl   = LENS.get(lens, lens)
    return (
        f"{cam}, {subject}, eyes directed at {gaze}, {hand}, "
        f"screen/display faces subject with {screen_content} partially visible to viewer from camera angle, "
        f"{environment}. {gl}, {QUALITY}. {NEGATIVE_GUARDS}."
    )
```

### build_diagram_prompt()

```python
def build_diagram_prompt(subject, style="clean flat infographic", palette="blue and white", extra=""):
    base = (f"{subject}, {style}, {palette} color palette, "
            "professional design, clear labels, high contrast, no people, no photorealistic elements, "
            "wide 16:9 landscape composition")
    if extra:
        base += f", {extra}"
    return base
```

### Decision table

| Role | Function | Lens |
|------|----------|------|
| HERO | `build_human_prompt()` | `hero_wide` (35mm) ← always |
| Team/group | `build_human_prompt()` | `group_wide` (24mm) |
| Device close-up | `build_human_prompt()` | `detail_close` (50mm) |
| Diagram/chart | `build_diagram_prompt()` | — |

---

## Bước 1 — Crawl tin tức 7 ngày gần nhất

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

---

## Bước 2 — Kiểm tra bài đã tồn tại trên WordPress

```python
def get_all_posts():
    resp = call("list_posts", {"number": 500})
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
        if slug.startswith("?p="):
            slug = ""
        posts.append({
            "id": post_id, "status": status, "title": title,
            "date": date, "slug": slug, "public_url": public_url,
        })
    return posts

def count_posts_on_date(all_posts, target_date):
    return sum(1 for p in all_posts if p["status"] == "publish" and p["date"].startswith(target_date))

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

---

## Bước 2b — Đọc Tracker Sheet

Google Sheet **"Infina News — Published Articles Tracker"** (`fileId: 1uVI1tPQxhTUk4qj8NWZSi-EReEwe2ZKIyIt_eQGeFOs`) — đọc bằng `mcp__Google_Drive__read_file_content`.

Cột: `#, Date, Title, URL, Focus Keyword, Type` — Type: `Plan` (pillar) hoặc `News` (cluster đã viết).

```python
def get_tracker_rows(text):
    rows = []
    for line in text.split("\n"):
        cells = [c.strip() for c in line.strip("| \n").split("|")]
        if len(cells) != 6 or not cells[0].isdigit():
            continue
        rows.append({
            "num": cells[0], "date": cells[1], "title": cells[2],
            "url": cells[3], "focus_keyword": cells[4].lower(), "type": cells[5],
        })
    return rows

tracker = get_tracker_rows(tracker_text)
used_keywords = {r["focus_keyword"] for r in tracker}
plan_rows = [r for r in tracker if r["type"].lower() == "plan"]
```

**Lưu ý:** tracker có thể trễ so với WP thực tế — luôn kết hợp cả Bước 2 (list_posts) lẫn Bước 2b để dedup.

---

## Bước 3 — Đọc keyword groups từ Excel

File: `AI_SalesX_Customer_Segments_Content_Pillars - Copy.xlsx`. Dùng làm nguồn tham khảo ý tưởng pillar + cluster keyword candidates. PILLAR_KW/URL thật lấy từ tracker sheet (Bước 2b) — Excel chỉ là kế hoạch tĩnh.

---

## Bước 4 — Map tin → pillar (link) + cluster keyword (viết) + category

**Quy tắc chống cannibalization:** FOCUS_KW (bài cluster) ≠ PILLAR_KW (pillar page). Cluster article chỉ link về pillar, không cạnh tranh keyword với pillar.

1. **Pillar target:** Chọn pillar từ `plan_rows` có URL thật, ưu tiên pillar chưa được link gần đây
2. **Cluster keyword:** Long-tail keyword, không trùng `used_keywords`, pass `is_duplicate()`
3. **Category:** CRM/automation → `"CRM Software"`, Chatbot/AI/ISA → `"AI Chatbot"`
4. **Angle:** Data/case study từ tin làm hook cho cluster keyword

Output: `FOCUS_KW`, `PILLAR_KW`, `PILLAR_URL`, `CATEGORY_NAME`

---

## Bước 5 — Viết cluster article

**Văn phong — KHÔNG dùng em dash (—):** không dùng em dash ở bất kỳ đâu trong TITLE, content, SEO_TITLE, hay SEO_DESC. Khi cần ngắt ý, dùng dấu chấm câu mới, dấu phẩy, hoặc dấu hai chấm thay vì em dash. Đây là yêu cầu cố định từ user, áp dụng cho mọi bài.

```
Intro — FOCUS_KW trong 100 từ đầu, context từ tin tức
[HERO — build_human_prompt(), lens=hero_wide]
H2: Dữ liệu/tin tức mới — external link tới nguồn
[STATS — build_diagram_prompt()]
H2: Tại sao quan trọng với real estate agents
H2: Giải pháp — [FOCUS_KW nguyên văn trong H2 này]
[DEMO — human hoặc diagram]
H2: Top platforms — external dofollow links
[COMPARISON — build_diagram_prompt()]
H2: Related reading — link về PILLAR_URL (anchor=PILLAR_KW) + 1 bài liên quan khác
H2: Final Thoughts
```

**SEO check đầy đủ (bắt buộc dùng bản này — bản cũ thiếu check kw_in_h2 và kw_in_seo_title dẫn đến Rank Math score thấp):**

```python
def check_seo(content, keyword, seo_title=None, seo_desc=None, title=None, pillar_keyword=None, pillar_url=None):
    raw = re.sub(r'<[^>]+>', ' ', content)
    words = raw.split()
    kw_count = len(re.findall(re.escape(keyword), raw.lower()))
    density = (kw_count / len(words)) * 100
    ext_links = len(re.findall(r'href="https?://(?!infina\.ai)[^"]*"', content))
    int_links = len(re.findall(r'href="https?://infina\.ai[^"]*"', content))
    img_alts_with_kw = len([m for m in re.findall(r'alt="[^"]*"', content.lower()) if keyword in m])
    h2_texts = re.findall(r'<h2>(.*?)</h2>', content, re.IGNORECASE)
    kw_in_h2 = any(keyword in h2.lower() for h2 in h2_texts)
    issues = []
    if density < 0.5: issues.append(f"Density {density:.2f}% < 0.5%")
    if density > 2.5: issues.append(f"Density {density:.2f}% > 2.5%")
    if ext_links < 1: issues.append("No external dofollow links")
    if int_links < 2: issues.append(f"Only {int_links} internal links (need ≥2)")
    if img_alts_with_kw < 1: issues.append("No img alt contains focus keyword")
    if not kw_in_h2: issues.append("FOCUS_KW không có trong bất kỳ H2 nào — Rank Math trừ điểm")
    if seo_title and keyword not in seo_title.lower():
        issues.append("FOCUS_KW không có trong SEO_TITLE — gây Rank Math score rất thấp (đã gặp 43/100)")
    if pillar_keyword and keyword.strip().lower() == pillar_keyword.strip().lower():
        issues.append(f"FOCUS_KW trùng PILLAR_KW — cannibalization, đổi sang long-tail khác")
    if pillar_url and pillar_url not in content:
        issues.append(f"Thiếu internal link về pillar page ({pillar_url})")
    for field_name, field_val in [("content", content), ("TITLE", title), ("seo_title", seo_title), ("seo_desc", seo_desc)]:
        if field_val and "—" in field_val:
            issues.append(f"Có em dash (—) trong {field_name} — thay bằng dấu chấm/phẩy/hai chấm")
    return {"words": len(words), "density": f"{density:.2f}%", "ok": len(issues)==0, "issues": issues}

# Gọi với đầy đủ field để check hết, không chỉ content:
# seo = check_seo(CONTENT, FOCUS_KW, seo_title=SEO_TITLE, seo_desc=SEO_DESC, title=TITLE, pillar_keyword=PILLAR_KW, pillar_url=PILLAR_URL)
```

---

## Bước 6 — Publish

Tính thời điểm publish: lấy giờ bài publish gần nhất + 1 tiếng. Nếu đã qua → `status: "publish"`. Nếu chưa → `status: "future"`, `date: "YYYY-MM-DD HH:MM:SS"`.

```python
resp = call("create_post", {
    "title": TITLE, "content": CONTENT, "status": STATUS,
    "slug": SLUG, "seo_title": SEO_TITLE, "seo_description": SEO_DESC,
    "seo_focus_keyword": FOCUS_KW, "categories": [CATEGORY_NAME],
    "tags": TAGS, "image_url": IMG["HERO"],
    "image_alt": f"{FOCUS_KW} hero illustration",
})
post_id = re.search(r'ID (\d+)', resp).group(1)
print(f"Post ID {post_id} — https://infina.ai/news/{SLUG}/")
if "that bai" in resp:
    print("CANH BAO anh dai dien:", resp)
```

---

## Bước 7 — Log vào Tracker Sheet

Sau publish, in dòng tab-separated để người dùng paste vào sheet (Google Drive connector hiện tại chỉ đọc, không ghi được vào Sheets):

```
{num}	{date DD/MM/YYYY}	{TITLE}	https://infina.ai/news/{SLUG}/	{FOCUS_KW}	News
```

**Quan trọng:** dùng tab thật (không phải `|`) — Google Sheets tự tách cột khi paste dữ liệu tab-separated. Nếu dán sai vào 1 ô: **Data → Split text to columns → Custom separator → Tab**.

Link sheet: `https://docs.google.com/spreadsheets/d/1uVI1tPQxhTUk4qj8NWZSi-EReEwe2ZKIyIt_eQGeFOs`

---

## Bước 8 (Optional) — Kiểm tra traffic Google Search Console

Không chạy mỗi ngày trong pipeline chính — chỉ dùng khi user hỏi về traffic/ranking/impressions của các bài đã đăng.

**Credential:** service account key **không nằm trong repo này** (tránh commit secret vào git history). Key thật được lưu ở account-level skill copy tại `credentials/gsc_service_account.json` (cùng thư mục skill, ngoài GitHub). Service account email: `search-console-api@tidy-set-492904-b1.iam.gserviceaccount.com`, đã được cấp quyền `Full` trên 2 property: `https://infina.ai/` và `https://infina.ai/news/`.

Không có sẵn `google-auth`/`google-api-python-client` trong môi trường — tự build JWT bằng `pyjwt` + `cryptography` rồi đổi lấy access token qua `token_uri`. Nếu `cryptography`/`cffi` bị lỗi native binding (`ModuleNotFoundError: cffi` hoặc rust panic), chạy `pip3 install --user --force-reinstall cffi cryptography` trước.

```python
import json, time, jwt, requests
import os

KEY_PATH = os.environ.get("GSC_SERVICE_ACCOUNT_KEY_PATH", "credentials/gsc_service_account.json")  # relative to skill dir
SCOPE = "https://www.googleapis.com/auth/webmasters.readonly"

def get_access_token():
    creds = json.load(open(KEY_PATH))
    now = int(time.time())
    payload = {"iss": creds["client_email"], "scope": SCOPE, "aud": creds["token_uri"],
               "iat": now, "exp": now + 3600}
    assertion = jwt.encode(payload, creds["private_key"], algorithm="RS256")
    resp = requests.post(creds["token_uri"], data={
        "grant_type": "urn:ietf:params:oauth:grant-type:jwt-bearer",
        "assertion": assertion,
    }, timeout=30)
    return resp.json()["access_token"]

def query_search_analytics(site_url, start_date, end_date, dimensions=None, row_limit=25):
    token = get_access_token()
    headers = {"Authorization": f"Bearer {token}", "Content-Type": "application/json"}
    url = f"https://www.googleapis.com/webmasters/v3/sites/{requests.utils.quote(site_url, safe='')}/searchAnalytics/query"
    body = {"startDate": start_date, "endDate": end_date, "rowLimit": row_limit}
    if dimensions:
        body["dimensions"] = dimensions
    return requests.post(url, headers=headers, json=body, timeout=30).json()

# Ví dụ: top pages theo impressions trong 28 ngày gần nhất
# query_search_analytics("https://infina.ai/news/", "2026-07-22", "2026-08-19", dimensions=["page"], row_limit=30)
```

GSC data có độ trễ report ~2-3 ngày, nên `endDate` gần "hôm nay" thường trả về 0 cho vài ngày cuối. Dùng dimensions `["date"]`, `["page"]`, `["query"]` tuỳ nhu cầu. **Không bao giờ commit file key JSON thật hoặc `private_key` vào repo này** — key thật chỉ tồn tại ở account-level skill copy, ngoài GitHub.

---

## Slug rules

- Slug theo `FOCUS_KW` (cluster keyword), không theo `PILLAR_KW`
- Mỗi từ trong FOCUS_KW phải có trong slug
- Singular ≠ plural: `agent` ≠ `agents`
- Preposition bắt buộc: keyword `for real estate` → slug phải có `for`
- Check overlap thủ công với toàn bộ slug hiện có — nhiều slug có đuôi `-real-estate-agents` dễ overlap >60%

---

## Output script file

Mỗi lần chạy tạo: `article_cluster{N}_{slug}.py`

---

## Inputs cần thiết

| Input | Bắt buộc | Ghi chú |
|-------|----------|---------|
| Excel keyword file | Có | `AI_SalesX_Customer_Segments_Content_Pillars - Copy.xlsx` |
| Tracker Sheet | Có | fileId: `1uVI1tPQxhTUk4qj8NWZSi-EReEwe2ZKIyIt_eQGeFOs` — đọc qua Google Drive connector |
| Category | Có | `"AI Chatbot"` hoặc `"CRM Software"` |

