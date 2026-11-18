# Used SEO Focus Keywords Log

Dùng để tránh cannibalize (2 bài khác nhau cùng nhắm 1 focus keyword) khi chọn từ khóa chính
cho bài mới trong skill `seo-blog-writer`.

**Khi setup cho site mới**: đổi tên file này thành `used-keywords.md`, xóa dòng ví dụ mẫu bên
dưới, seed lại bảng từ danh sách bài đã có sẵn trên site (qua `post-sitemap.xml` hoặc tool
`list_posts` của WordPress MCP) nếu site đã có bài từ trước khi bắt đầu dùng skill này.

## Cách dùng

1. **Trước khi chốt** focus keyword ở Bước 1 (skill `seo-blog-writer`), tìm trong bảng dưới xem
   keyword dự định dùng (hoặc biến thể rất gần, cùng thực thể chính) đã xuất hiện chưa.
2. Nếu đã trùng với 1 bài **khác chủ đề**, đổi sang biến thể long-tail hơn (thêm năm, thêm chi
   tiết cụ thể của bài đang viết) thay vì dùng nguyên keyword gốc.
3. Nếu bài đang viết là góc khai thác mới của **đúng chủ đề cũ** (người dùng yêu cầu rõ ràng
   viết lại), giữ nguyên keyword là chấp nhận được, không tính là cannibalize ngoài ý muốn, ghi
   chú rõ trong báo cáo bàn giao.
4. **Sau khi đăng bài mới thành công**, thêm ngay 1 dòng mới vào đầu bảng dưới (ID, keyword,
   nguồn, tiêu đề, status, ngày) để log luôn cập nhật cho lần chạy sau.
5. File này chỉ nên giữ khoảng **150-200 bài gần nhất**. Khi vượt ngưỡng, xóa bớt các dòng cũ
   nhất ở cuối bảng để tránh phình file tốn context khi đọc.

Cột **Nguồn**: `chắc chắn` = lấy trực tiếp từ payload lúc đăng bài. `suy đoán` = backfill bằng
cách đọc SEO title public trên trang và suy ra theo rule keyword-đầu-tiêu-đề, có thể lệch nhẹ so
với keyword thật đã set trong Rank Math.

| ID | Focus keyword | Nguồn | Tiêu đề | Status | Ngày đăng |
|---|---|---|---|---|---|
