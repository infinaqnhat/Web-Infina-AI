# Infina AI Blog (WordPress)

Tài liệu tổng quan về blog/tin tức của Infina AI chạy trên **WordPress**, dùng theme
block **`infina-ai-news`** (thư mục `infina-ai-news/`).

---

## 1. Mục tiêu & vị trí
- Blog/newsroom của Infina AI, đặt tại **`https://infina.ai/news`** (subdirectory —
  giữ được SEO/authority cho domain chính, thay vì subdomain).
- Giao diện đồng bộ site marketing chính: font **Be Vietnam Pro**, màu **navy `#001F5C`**
  / **blue `#1863DC`**, header + footer Infina.

## 2. Theme: `infina-ai-news`
Block theme (Full Site Editing), cần **WordPress 6.4+**.

| Template | Vai trò |
|---|---|
| `templates/home.html` | Trang blog: **featured 4 bài** (1 lớn + 3 list) + **bảng News** (Date · Category · Title) + sidebar (Search + promo) |
| `templates/single.html` | Trang bài viết + author card |
| `templates/page.html` | Trang tĩnh |
| `templates/archive.html` | Lưu trữ theo category/tag/author (dạng bảng) |
| `templates/search.html` | Kết quả tìm kiếm |
| `templates/404.html` | Không tìm thấy |
| `parts/header.html`, `parts/footer.html` | Nav + footer Infina |

Đặc điểm:
- **Featured hiện trên mọi trang** (4 bài mới nhất), bảng News bên dưới **phân trang**.
- **Pagination AJAX**: bấm Previous/Next thay bảng tại chỗ, **giữ viewport** (không nhảy
  lên đầu); có fallback nếu tắt JS.
- **Search**: dùng core Search block.

## 3. Cài đặt theme
1. Nén thư mục `infina-ai-news/` thành `infina-ai-news.zip`.
2. WP Admin → **Appearance → Themes → Add New → Upload Theme** → **Activate**.
3. Tạo vài **Post** có **Featured image** + gán **Category** để trang newsroom hiển thị đủ.

> Bản zip build không được commit vào git (xem `.gitignore`); build lại từ source khi cần.

## 4. Cấu hình chạy ở `infina.ai/news` (subdirectory)
Đây là cấu hình **WordPress + server**, không phải theme:
1. Cài WordPress ở subdirectory `/news` (hoặc map về đó), đặt
   **Settings → General → Site Address (URL)** = `https://infina.ai/news`.
2. Reverse proxy (ví dụ nginx): route `/news` về WordPress, phần còn lại của
   `infina.ai` vẫn phục vụ site tĩnh:
   ```nginx
   location /news/ {
       try_files $uri $uri/ /news/index.php?$args;
   }
   ```
3. **Settings → Permalinks → Post name** → URL bài viết dạng `infina.ai/news/ten-bai/`.

## 5. Mô hình nội dung
- **Post** = bài viết tin tức.
- **Category** = nhãn hiển thị ở cột "Category" trong bảng News (dùng *primary category*).
- **Featured image** = ảnh lớn ở khối featured / ảnh cover trang bài.
- **Author** = hiển thị ở meta (Category · Author · Date).
- **Ghim bài lên featured**: WordPress dùng **sticky post** ("Stick to the top of the
  blog"). *Hiện tại* khối featured lấy 4 bài mới nhất theo ngày; nếu muốn ưu tiên bài
  sticky lên đầu (giống "Feature this post" của Ghost), cần thêm custom query trong
  `functions.php`.

## 6. Quan hệ với theme Ghost
Repo còn có một bản theme **Ghost** tương đương ở `../ghost-theme/infina/` (cùng layout
newsroom). Theme WordPress này được port từ theme Ghost đó để giữ giao diện đồng nhất.
Nếu chỉnh giao diện, nên đồng bộ cả hai để nhất quán.

## 7. Kiểm thử
- Block theme nhạy với cú pháp block-markup — nên cài lên **WP staging** kiểm tra trong
  Site Editor trước khi lên production. Nếu template nào báo lỗi block, kiểm tra lại
  file `.html` tương ứng trong `templates/`.
