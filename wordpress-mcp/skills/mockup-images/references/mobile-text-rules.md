# Quy tắc chữ trong ảnh để đọc được trên điện thoại

Phát hiện ngày 13/10/2026: 59 mockup đầu tiên dựng ở canvas 1600x900 với chữ 15 đến 55px. Trên điện thoại ảnh chỉ rộng khoảng 340 CSS px
(hệ số thu 340/1600 = 0,21), nên chữ nhỏ nhất ra khoảng 3px và chữ lớn nhất ra khoảng 11px. Máy kiểm `mobile_report` trong `common.py` báo
**cả 59 ảnh đều không đạt** (100% ký tự dưới 12px trên điện thoại). Dùng `python3 scripts/phone_preview.py out.jpg anh.jpg` để thấy trực quan.

## Số liệu tham khảo (nguồn web, đều là hướng dẫn không phải chuẩn bắt buộc)

- Chữ thân bài trên web: khoảng 16px là mức phổ biến, chữ phụ có thể 14px dùng ít ([10 Mobile Typography Tips, OneNine](https://onenine.com/10-mobile-typography-tips-for-better-readability/)).
- Infographic cho di động: tối thiểu 14pt cho chữ thân và 22pt cho tiêu đề ([Litmus, qua MarketingProfs](https://marketingprofs.com/short-articles/2437/four-tips-for-mobile-email-design)).
- Chữ chú thích tối thiểu 12 đến 15pt trên di động ([Font Size Usage in UI/UX Design](https://medium.com/design-bootcamp/font-size-usage-in-ui-ux-design-web-mobile-tablet-52a9e17c16ce)).
- Apple: cỡ chữ tối thiểu 11pt trên iOS ([bản tóm tắt bảng typography của Apple HIG](https://glama.ai/mcp/servers/@tmaasen/apple-dev-mcp/blob/b82f0efe2115dc4539c83a2374a714a84aeb350a/content/universal/typography.md)).
- Chữ trong ảnh không co giãn: nó hiển thị nhỏ hơn dự định trên điện thoại, nên dùng chữ HTML cho thông tin quan trọng ([Why text on images is inaccessible, St Andrews](https://digitalcommunications.wp.st-andrews.ac.uk/2025/01/22/why-text-on-images-is-inaccessible-and-how-to-fix-it/); WCAG 1.4.5 Images of Text).
- Infographic phức tạp: chia thành các phần nhỏ, tiêu đề và nhãn thật ngắn, có đường mở bản lớn ([Microsoft Writing Style Guide, responsive content](https://learn.microsoft.com/en-us/style-guide/responsive-content)).
- Một blog về ảnh annotated: cỡ chữ theo tỷ lệ cạnh dài của ảnh, tiêu đề khoảng 3%, nhãn khoảng 2%, và kiểm ảnh ở 160 đến 200px ([mujoai](https://mujoai.com/blog/2026/03/annotatedcallout-images-product)). Nguồn đơn lẻ, chỉ là quy tắc ngón tay cái.

## Quy tắc áp dụng cho skill này

1. **Thiết kế theo điện thoại.** Giả định ảnh hiển thị rộng 340 CSS px. Hệ số thu k = 340 / chiều rộng canvas.
2. **Mục tiêu cỡ chữ trên điện thoại:** nhãn và chữ chú thích ≥ 13px, chữ thân ≥ 15px, tiêu đề ≥ 20px. Sàn cứng là 12px (dưới mức đó là lỗi).
3. **Canvas hẹp, không 16:9.** Dùng canvas rộng 1000px, cao 700 đến 1400 tùy nội dung (k = 0,34). Khi đó: nhãn ≥ 38px, thân ≥ 44px, tiêu đề ≥ 60px.
   Canvas 1600 đòi chữ ≥ 60/70/95px nên vô nghĩa; chỉ dùng cho ảnh gần như không có chữ.
4. **Ít chữ.** Tối đa 6 mục chữ mỗi ảnh, mỗi mục tối đa 8 từ. Bảng tối đa 3 cột và 5 hàng. Bỏ cột và chú thích phụ. Một thông điệp mỗi ảnh.
   Muốn thể hiện nhiều dữ liệu thì tách thành 2 ảnh hoặc để bảng HTML trong bài làm việc đó.
5. **Hai tầng chữ.** Tầng 1 (thông điệp: nhãn, số, tiêu đề, chú thích đánh số) phải đạt quy tắc 2. Tầng 2 (chữ "giả" bên trong vật mô phỏng như nội dung tờ flyer, ô bảng) được nhỏ hơn
   nhưng không được chứa thông tin người đọc cần; chuyển thông tin cần đọc ra nhãn ngoài vật mô phỏng hoặc vào thân bài. Có thể thay bằng thanh xám giả chữ.
6. **Ghi chú "sample" và tag** nhỏ trong ảnh được phép nhưng phải lặp lại trong `<figcaption>` HTML để đọc được trên điện thoại.
7. **Alt text và figcaption** mang đủ nội dung chữ chính của ảnh (người dùng đọc màn hình và ai không phóng to được ảnh vẫn nắm ý).
8. **Đường mở bản lớn:** bọc ảnh bằng liên kết tới ảnh gốc hoặc bật lightbox của theme để bấm phóng to.
9. **Kiểm bắt buộc trước khi upload:** `render()` in dòng `phone min ...px ... OK/TOO SMALL`. Không đạt thì sửa. Rồi chạy `phone_preview.py` và nhìn ảnh bằng mắt.

Prototype đạt chuẩn: `scenes/s_mobile_demo.py` (`mobile_budget` canvas 1000x1400: chữ nhỏ nhất 12,9px trên điện thoại; `mobile_flyer`: nhãn 16px, chỉ phần chữ giả của tờ flyer nhỏ hơn).
