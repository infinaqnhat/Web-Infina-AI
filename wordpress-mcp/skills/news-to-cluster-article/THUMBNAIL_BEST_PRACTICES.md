# Checklist: Blog Thumbnail / Featured Image Best Practice

Tổng hợp từ research (Snappa, ThumbnailCreator, Visme, vidIQ, DreamHost — xem nguồn cuối file) + verify thực tế bằng cách tải ảnh thật trên site xuống xem. Dùng để tự chấm 1 ảnh có đủ chuẩn làm featured image/thumbnail hay không, trước khi gán nó cho 1 bài.

---

## Checklist tự chấm cho 1 ảnh thumbnail

- [ ] **Postage-stamp test**: thu ảnh xuống cỡ ~120×68px (bằng icon nhỏ) — chữ chính vẫn đọc được ngay, không cần zoom
- [ ] **Tối đa 1 thông điệp chính** — 1 con số lớn, hoặc 1 icon/so sánh 2 phe, không phải bảng dữ liệu nhiều hàng nhiều cột
- [ ] **Chữ trong ảnh ít hơn ~12 ký tự** cho phần headline/số liệu chính (không tính label phụ nhỏ)
- [ ] **Tương phản cao** giữa chữ và nền (tối thiểu tỷ lệ 4.5:1)
- [ ] **Không nhồi nhét** — còn khoảng trắng (white space) cho mắt nghỉ, không fill kín canvas
- [ ] **Tỉ lệ khung hình nhất quán** giữa các bài (site này đang dùng 16:9) để layout trang chủ không bị lệch
- [ ] Nếu là **ảnh người**: mặt rõ, không bị che, ánh sáng tốt, tương phản cao với nền — công thức CTR đã kiểm chứng
- [ ] Nếu là **infographic/data**: chỉ lấy 1 "snippet" (1 con số/1 so sánh nổi bật nhất), KHÔNG chụp nguyên bảng so sánh chi tiết nhiều platform/nhiều tiêu chí — loại đó để dành cho ảnh trong thân bài, không dùng làm thumbnail
- [ ] Font **đậm, rõ, không dùng font trang trí mảnh** — dễ vỡ nét khi thu nhỏ

---

## Ví dụ đã verify trên chính site

| Loại | Ảnh | Đạt/Không đạt | Vì sao |
|---|---|---|---|
| Ảnh mình tạo (Gemini) | Biểu đồ 2 cột "92% vs 8%" | ✅ Đạt | 1 con số lớn mỗi cột, ít chữ, tương phản tốt |
| Ảnh mình tạo (Gemini) | Đồng hồ đo "64%" | ✅ Đạt (gần đạt) | Trung tâm là 1 số lớn, tuy hơi nhiều icon phụ quanh rìa |
| Ảnh mình tạo (Gemini) | 2 icon "Standalone vs Embedded" | ✅ Đạt | So sánh 2 phe rõ ràng, chữ to, không table |
| Ảnh automation khác | Bảng so sánh 5 platform × 6 cột, sao đánh giá | ❌ Fail nặng | Chữ quá nhỏ, quá nhiều hàng/cột, không đọc được khi thu nhỏ |
| Ảnh automation khác | Checklist 6 mục, mỗi mục 1-2 câu văn đầy đủ | ❌ Fail nặng | Là văn bản dài, không phải hình ảnh — hoàn toàn không hoạt động như thumbnail |

**Kết luận rút ra:** ảnh dạng "1 con số lớn + so sánh 2 phe" (STATS/COMPARISON style hiện dùng cho bài của mình) đã đúng hướng. Vấn đề chỉ nằm ở nhóm ảnh bảng-dữ-liệu-chi-tiết/checklist-văn-bản của 1 automation khác đang publish song song — nhóm đó cần xử lý riêng.

---

## Phong cách hình ảnh (Visual Style) — checklist bổ sung

Research thêm về việc chọn STYLE (không chỉ độ dễ đọc) cho thumbnail.

### So sánh các style

| Style | Ưu điểm | Khi nào dùng |
|---|---|---|
| **Flat illustration/icon** (đang dùng cho STATS/COMPARISON) | Scale tốt ở mọi kích thước, rẻ/nhanh để tạo hàng loạt, rõ ràng ở size nhỏ | Bài so sánh, số liệu, khái niệm trừu tượng (không có "cảnh" cụ thể để chụp) |
| **Photography/photorealistic** (đang dùng cho HERO người) | Mặt người + cảm xúc tăng CTR đã kiểm chứng, tạo cảm giác "con người thật" đứng sau content | Bài news/case study có ngữ cảnh con người cụ thể (agent dùng tool, ai đó ra quyết định) |
| **3D / semi-flat có gradient** | Nổi bật hơn flat thuần, cảm giác "cao cấp" hơn | Landing page/hero section — ít phù hợp cho khối lượng lớn bài blog hàng ngày |

⚠️ Lưu ý quan trọng: **ảnh flat/illustration và ảnh photography phải cùng 1 "mood" màu sắc** (cùng palette, cùng độ tương phản) — nếu 2 style lệch nhau (vd 1 bên màu pastel nhẹ, 1 bên màu neon đậm) sẽ tạo cảm giác thiếu nhất quán, giảm uy tín thương hiệu dù từng ảnh riêng lẻ vẫn đẹp.

### Brand consistency — chọn cố định 2-3 màu

- Chọn **2-3 màu thương hiệu cố định** và dùng xuyên suốt mọi thumbnail (không đổi bảng màu tuỳ hứng mỗi bài) — đây là yếu tố tạo "nhận diện tức thời" khi lướt feed, được ghi nhận giúp CTR tăng tới ~38% ở kênh nhất quán màu sắc.
- Có thể **mã hoá màu theo category** để người đọc phân biệt nhanh loại nội dung ngay từ thumbnail:
  - AI Chatbot → xanh dương/indigo
  - CRM Software → xanh lá/teal
  - Real Estate Websites/IDX → navy/vàng gold
  (đây là gợi ý dựa trên palette đã dùng tự nhiên trong các ảnh vừa tạo — có thể điều chỉnh theo brand guideline thật của Infina AI nếu có)

### Template hoá thay vì tạo prompt tuỳ hứng mỗi bài

Best practice khuyên dùng **3-5 template cố định layout**, chỉ thay nội dung/con số bên trong, thay vì nghĩ prompt mới hoàn toàn mỗi lần — giúp nhất quán mà vẫn đủ linh hoạt theo nội dung. Đề xuất áp dụng cho site này:

| Template | Bố cục cố định | Dùng cho loại bài |
|---|---|---|
| **A — Single Stat** | 1 con số lớn + 1 icon nhỏ + label ngắn | Bài news có 1 con số/thống kê nổi bật (kiểu bài của mình) |
| **B — Two-Way Compare** | 2 icon đối xứng trái-phải + 1 mũi tên/dấu vs ở giữa | Bài "X vs Y", "Standalone vs Embedded", "before/after" |
| **C — Badge/Top Pick** | 1 icon trung tâm (cúp/sao) + headline ngắn phía trên | Bài listicle "Best X", "Top Picks" |
| **D — Flow/Pipeline** | 2-3 icon nối bằng mũi tên theo 1 hướng | Bài giải thích quy trình/tích hợp (vd IDX feed, CRM integration) |
| **E — Checklist ngắn** | 3 icon dấu check xếp NGANG (không xếp dọc — dễ bị crop khi ép 16:9) + headline | Bài buyer's guide/checklist |

Đây gần đúng những gì đã áp dụng thực tế cho 8 bài vừa sửa hôm nay — nên xem như đã hình thành sẵn 5 template ở trên, từ giờ có thể tái sử dụng thay vì generate ngẫu nhiên mỗi lần.

### Nhất quán vs đa dạng — điểm cân bằng

Research chỉ ra không nên chọn cực đoan 1 trong 2:
- **Không nên** dùng đúng 1 ảnh y hệt lặp lại (nhàm, không phân biệt được bài nào với bài nào — đúng vấn đề ban đầu của site này).
- **Không nên** mỗi bài 1 style hoàn toàn khác biệt (mất nhận diện thương hiệu).
- **Nên**: giữ cố định "hệ thống nền" — palette màu, tỉ lệ khung, mức độ chi tiết, bộ template ở trên — nhưng để nội dung cụ thể (icon nào, con số nào) thay đổi theo từng bài.

---

## Nguồn tham khảo

- [WordPress Featured Image Size & Tips — Snappa](https://snappa.com/blog/wordpress-featured-image-size/)
- [What's the Best Size for Blog Post Images in WordPress? — SeaHawk Media](https://seahawkmedia.com/wordpress/best-size-blog-post-images-wordpress/)
- [WordPress Featured Image Size Guide — DreamHost](https://www.dreamhost.com/blog/create-wordpress-featured-image/)
- [Ultimate Guide to Thumbnail Composition — ThumbnailCreator](https://www.thumbnailcreator.com/blog/thumbnail-composition-guide)
- [Text Placement vs. No Text: Thumbnail Impact — ThumbnailCreator](https://www.thumbnailcreator.com/blog/text-placement-vs-no-text-thumbnail-impact)
- [7 Typography Mistakes in Thumbnails — ThumbnailCreator](https://www.thumbnailcreator.com/blog/typography-mistakes-thumbnails)
- [How to Create Clutter-Free Infographics — Visme](https://visme.co/blog/clutter-free-infographics/)
- [YouTube Thumbnail Design Tips: Best Practices for 2026 — vidIQ](https://vidiq.com/blog/post/youtube-thumbnail-design-tips/)
- [How to Improve Your YouTube Thumbnail CTR — vidIQ](https://vidiq.com/blog/post/youtube-custom-thumbnails-ctr/)
- [Best Branding Image Styles for Businesses in 2026 — Its Jeff B](https://www.itsjeffb.com/post/best-branding-image-styles-for-businesses-in-2026)
- [What Is Flat Design? A Complete 2026 Guide — Big Human](https://www.bighuman.com/blog/guide-to-flat-design-style)
- [Flat Vector Illustration: A Complete Guide — Getillustrations](https://getillustrations.com/blog/flat-vector-illustration-guide/)
- [Ultimate Guide To Thumbnail Branding — ThumbnailCreator](https://www.thumbnailcreator.com/blog/ultimate-thumbnail-branding-guide)
- [YouTube Thumbnail Branding Consistency: Secrets to Higher CTR — AIThumbnail](https://www.aithumbnail.so/blog/youtube-thumbnail-branding-consistency)
- [Generate Image Prompts for Blog Thumbnails Fast and Consistent — Our Code World](https://ourcodeworld.com/articles/read/3210/generate-image-prompts-for-blog-thumbnails-fast-and-consistent)
