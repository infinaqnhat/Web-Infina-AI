# Infina AI — Automate đăng bài WordPress qua custom MCP

Tài liệu mô tả cơ chế **tự động đăng bài lên blog WordPress của Infina AI**
(`infina.ai/news`) thông qua một **custom MCP connector** của Claude.ai / Claude Desktop.

File kèm theo: [`infina-wp-mcp-server-snippet.php`](./infina-wp-mcp-server-snippet.php)
— snippet PHP dán vào WordPress để tạo MCP server.

---

## 1. Cơ chế tổng quan

```
Claude (claude.ai / Desktop)
   │  gọi tool (JSON-RPC 2.0 qua HTTPS POST)
   ▼
https://infina.ai/news/wp-json/infina-mcp/v1/blog?key=<secret>
   │  REST route tự viết (register_rest_route)
   ▼
WordPress  →  wp_insert_post()/wp_update_post()  →  bài viết ở trạng thái DRAFT
```

- Claude kết nối tới WordPress như một **MCP server** qua HTTP POST, mỗi request là một
  gói **JSON-RPC 2.0** (`initialize`, `tools/list`, `tools/call`…). **Không dùng SSE**.
- WordPress trả về JSON đồng bộ (request/response) — đơn giản, không cần server chủ động
  đẩy tin nhắn, nên không vướng phần SSE chưa hoàn thiện của plugin chính thức.

### Vì sao KHÔNG dùng plugin `WordPress/mcp-adapter`
Plugin chính thức (bản ~0.5.0) cài được, đăng ký route được, nhưng HTTP transport báo
`Internal error: SSE streaming not yet implemented` khi Claude kết nối — tính năng SSE
trong plugin chưa xong. → Tự viết REST route trả JSON-RPC thuần là cách chắc chắn hoạt
động. Sau này khi `mcp-adapter` vá xong SSE có thể cân nhắc chuyển lại.

### Vì sao xác thực bằng secret key trong URL (không OAuth/Basic Auth)
Giao diện "Add custom connector" của Claude.ai chỉ có ô OAuth Client ID/Secret, **không
cho gắn custom header** (vd `Authorization`). Vì vậy không dùng được Application Password
qua header như REST API chuẩn. → Nhét một **secret token ngẫu nhiên dài** vào query string
của URL connector; route kiểm tra bằng `hash_equals()`. Không mạnh bằng OAuth thật nhưng
đủ cho một endpoint nội bộ ít người biết.

> Bảo mật này chỉ áp dụng khi gọi qua custom connector từ claude.ai/Claude Desktop.
> Không liên quan CORS (MCP chạy từ server Anthropic, không phải trình duyệt).

---

## 2. Các tool được cung cấp

| Tool | Chức năng |
|---|---|
| `create_draft_post` | Tạo bài **draft** mới: `title`, `content` (HTML), `excerpt`, `slug`, `categories[]`, `tags[]`, SEO Rank Math (`seo_title`/`seo_description`/`seo_focus_keyword`), ảnh đại diện (`image_url` + `image_alt`) |
| `list_draft_posts` | Liệt kê các bài đang ở trạng thái draft (`number`, mặc định 5) |
| `update_draft_post` | Sửa 1 bài **draft** (`post_id` bắt buộc). **Từ chối nếu bài đã publish** để tránh sửa nhầm bài live |

**An toàn theo thiết kế:**
- Bài luôn tạo ở trạng thái **`draft`** — Claude không tự publish; con người review rồi mới đăng.
- `update_draft_post` chặn thao tác lên bài đã publish.
- Sideload ảnh có chống **SSRF**: chỉ nhận URL `https`, chặn `localhost`/IP nội bộ/private,
  kiểm tra `content-type: image/*` trước khi tải.

---

## 3. Cài đặt

### Bước 1 — Đặt secret (chọn 1 cách; KHÔNG hardcode vào file trong repo)
Sinh secret ngẫu nhiên (chạy trên máy cá nhân):
```bash
php -r "echo bin2hex(random_bytes(24));"
```
- **Cách 1 (khuyên dùng):** mở `wp-config.php`, thêm phía trên dòng `/* That's all, stop editing! */`:
  ```php
  define( 'INFINA_MCP_SECRET', 'dan-secret-that-vao-day' );
  ```
- **Cách 2 (không có FTP):** WP-CLI `wp option update infina_mcp_secret "..."`, hoặc một
  snippet WPCode chế độ **Run Once** gọi `update_option( 'infina_mcp_secret', '...', false );`
  rồi xoá snippet đó ngay sau khi lưu.

### Bước 2 — Dán snippet PHP
- Vào **WPCode → Add Snippet → PHP Snippet**, dán nội dung
  `infina-wp-mcp-server-snippet.php`.
- Insert Method: **Auto Insert**, Location: **Run Everywhere**. Lưu & Active.

### Bước 3 — Thêm connector trong Claude
- Claude.ai → Settings → Connectors → **Add custom connector**.
- URL:
  ```
  https://infina.ai/news/wp-json/infina-mcp/v1/blog?key=<secret>
  ```
  (thay `<secret>` bằng giá trị đã set ở Bước 1; đây là REST endpoint của WordPress đặt
  tại subdirectory `/news`).
- Sau khi kết nối, Claude sẽ thấy 3 tool ở trên và có thể tạo/sửa/liệt kê bài draft.

### Kiểm thử nhanh (không cần Claude)
```bash
curl -s -X POST "https://infina.ai/news/wp-json/infina-mcp/v1/blog?key=<secret>" \
  -H "Content-Type: application/json" \
  -d '{"jsonrpc":"2.0","id":1,"method":"tools/list"}'
```
Trả về danh sách tool = route hoạt động.

---

## 4. Bảo mật — bắt buộc đọc
- **Không bao giờ** dán secret thật vào `infina-wp-mcp-server-snippet.php` hay bất kỳ file
  nào trong git repo. File chỉ định nghĩa hàm đọc secret từ `wp-config.php`/option.
- Nếu secret lỡ bị commit hoặc để lộ → **đổi ngay** (đổi `INFINA_MCP_SECRET` hoặc option
  `infina_mcp_secret`) và cập nhật lại URL connector trong Claude.
- Nên đặt secret dài (>= 32 hex chars) và chỉ chia sẻ trong nội bộ.

---

## 5. Ghi chú kỹ thuật
- **Naming đã đổi cho Infina** (so với bản ToyHunter gốc):
  - Prefix hàm `toyhunter_mcp_*` → `infina_mcp_*`
  - Constant `TOYHUNTER_MCP_SECRET` → `INFINA_MCP_SECRET`
  - Option `toyhunter_mcp_secret` → `infina_mcp_secret`
  - Route namespace `toyhunter-mcp/v1` → `infina-mcp/v1`
  - `serverInfo.name` → `infina-blog`
- **SEO plugin:** snippet đang ghi meta cho **Rank Math** (`rank_math_title`,
  `rank_math_description`, `rank_math_focus_keyword`). Nếu blog Infina dùng **Yoast**, đổi
  các key sang `_yoast_wpseo_title`, `_yoast_wpseo_metadesc`, `_yoast_wpseo_focuskw`.
- **Tác giả:** bài tạo với `post_author = 1`. Đổi nếu muốn gán tác giả khác.
- Endpoint phụ thuộc WordPress cài ở `infina.ai/news`; nếu đổi vị trí cài đặt thì đổi URL
  connector tương ứng.
