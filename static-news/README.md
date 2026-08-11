# Infina AI News — static export (blog + articles)

Bản HTML tĩnh của trang News (blog listing + article pages) — để **host tĩnh** hoặc
**Super Import vào Instatic**.

## Cấu trúc
```
static-news/
├── index.html                         # TRANG BLOG (featured + bảng News)
├── articles/
│   ├── the-model-was-never-the-prize.html
│   ├── cut-crm-busywork-to-zero.html
│   ├── genai-first-real-revenue-number.html
│   └── ai-moved-into-your-slack.html  # mỗi bài = 1 file
└── assets/
    ├── css/screen.css                 # style brand Infina (dùng chung)
    ├── js/main.js                     # mobile nav toggle
    └── images/infina-logo.png
```

## 2 template
- **`index.html`** — blog listing: 1 bài featured lớn + 3 bài list + bảng News (Date · Category · Title), mỗi hàng link tới file article.
- **`articles/*.html`** — trang bài viết: tiêu đề, meta (Category · Author · Date), ảnh feature (placeholder gradient), nội dung, author card.

## Host tĩnh
Upload cả thư mục `static-news/` lên bất kỳ static host nào (Netlify, GitHub Pages, S3,
Cloudflare Pages…). Trang chủ là `index.html`. Để đặt tại `infina.ai/news`, deploy nội
dung này dưới đường dẫn `/news/`.

- Ảnh feature hiện là **placeholder gradient** — thay bằng `<img>` thật khi có ảnh.
- Ô Search chỉ là trang trí (static không có backend tìm kiếm).

## Super Import vào Instatic
Zip thư mục này rồi dùng **Super Import** của Instatic:
- Instatic sẽ nhận diện **2 layout** (blog + article) thành **template tái dùng**.
- `:root` biến thành **design tokens** (màu/font) trong Core Framework.
- Sau import, dùng **Content/Collection** của Instatic để tự liệt kê bài (thay bảng News
  tĩnh) và tạo bài mới từ template article — không cần sửa HTML tay.

## Nguồn thiết kế
Layout/CSS được port từ theme Ghost `../ghost-theme/infina/` (cùng phong cách newsroom)
để giữ giao diện đồng nhất với blog Ghost/WordPress.
