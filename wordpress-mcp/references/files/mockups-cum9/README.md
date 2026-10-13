# Mockup ảnh minh họa cho Cụm 9 (13/10/2026)

21 ảnh 1600x900 dựng bằng HTML + Playwright (không dùng AI vẽ chữ), chụp thành JPG. Gồm 7 bài: cards (#1883), logos (#1889),
postcards (#1877), bio (#1895), testimonials (#1949), listing presentation (#1955), flyers (#1967).

- `src/s_*.py`: mỗi file dựng một nhóm ảnh. Chạy trong thư mục `src` kèm `common.py` và ảnh nền `../photos/ph_*.jpg`
  (copy ảnh vào cùng thư mục với file html khi render). `python3 s_fly.py [tên_cảnh]`.
- `final/*.jpg`: ảnh đã dựng. `photos/`: 5 ảnh nhà sinh bằng Gemini (không có chữ, không có người).
- `spec.json`: URL media đã upload lên WordPress + alt, và quy tắc chèn/thay/xóa ảnh cho từng bài.
- `apply_mockups.py <post_id> <in.html> <out.html>`: áp quy tắc lên nội dung hiện tại của bài, kiểm tra chữ và link không đổi.

Tình trạng: #1949, #1955, #1967 đã cập nhật ngày 13/10. #1877, #1883, #1889, #1895 chờ bài publish rồi mới chèn
(bài future không đọc được nội dung qua REST, tránh ghi đè bằng bản local cũ).

Quy ước: tên và số liệu trong mockup đều hư cấu và được ghi chú ngay trên ảnh. Cần `pip install segno` để vẽ QR (trỏ về example.com).
