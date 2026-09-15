# Refresh Log

Log các lần đã check/sửa bài qua skill `post-refresh`, dùng để tránh check lại 1 trang quá dày
(chờ ít nhất 2-3 tuần sau khi sửa để Google phản ánh thay đổi vào dữ liệu) và theo dõi hiệu quả
các lần sửa trước. Thêm dòng mới vào **đầu bảng**, không phải cuối bảng. Khi bảng vượt khoảng
100-150 dòng, xóa bớt các dòng cũ nhất ở cuối để tránh phình file tốn context khi đọc.

| Ngày check | URL | Chẩn đoán | Đã sửa gì | Kết quả | Số liệu trước khi sửa |
|---|---|---|---|---|---|
