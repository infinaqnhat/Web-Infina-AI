# Mockup ảnh minh họa cho Cụm 9 (13/10/2026)

59 ảnh 1600x900 (21 ưu tiên cao + 18 trung bình + 20 thấp) dựng bằng HTML + Playwright (không dùng AI vẽ chữ), chụp thành JPG. Gồm 7 bài: cards (#1883), logos (#1889),
postcards (#1877), bio (#1895), testimonials (#1949), listing presentation (#1955), flyers (#1967).

- `src/s_*.py`: mỗi file dựng một nhóm ảnh. Chạy trong thư mục `src` kèm `common.py` và ảnh nền `../photos/ph_*.jpg`
  (copy ảnh vào cùng thư mục với file html khi render). `python3 s_fly.py [tên_cảnh]`.
- `final/*.jpg`: ảnh đã dựng. `photos/`: 5 ảnh nhà sinh bằng Gemini (không có chữ, không có người).
- `spec.json`: URL media đã upload lên WordPress + alt, và quy tắc chèn/thay/xóa ảnh cho từng bài.
- `apply_mockups.py <post_id> <in.html> <out.html>`: áp quy tắc lên nội dung hiện tại của bài, kiểm tra chữ và link không đổi.

Tình trạng: #1949, #1955, #1967 đã cập nhật ngày 13/10. #1877, #1883, #1889, #1895 chờ bài publish rồi mới chèn
(bài future không đọc được nội dung qua REST, tránh ghi đè bằng bản local cũ).

Quy ước: tên và số liệu trong mockup đều hư cấu và được ghi chú ngay trên ảnh. Cần `pip install segno` để vẽ QR (trỏ về example.com).

Lưu ý: mã dựng ảnh và script chèn bản chuẩn, dùng lại cho bài khác, nằm ở skill `skills/mockup-images/`. Thư mục này chỉ giữ kết quả đợt Cụm 9
và bản `apply_mockups.py` mà các trigger 14/10 và 15/10 đang gọi.

Nhóm trung bình (13/10): #1937 GBP, #1979 Name Ideas, #1843 Marketing Plan đã cập nhật ngay (#1843 từ bản live). #1859 và #1865 chèn sau khi publish
(trigger 13/10 19:45 UTC), #1871 (trigger 14/10 11:00 UTC). `spec.json` có đủ 13 bài.

Nhóm thấp (13/10): #1825 pillar, #1832 hub (đã live, lấy bản live), #1961, #1977, #1943 (wave 2 future) đã cập nhật. #1853 chờ publish (trigger 13/10 10:30 UTC), #1901 (trigger 15/10 18:30 UTC).
Bài #1825 giữ ảnh COMPARISON vì có câu "Notice the contrast in the image above".

## Vòng thử mobile-first (13/10/2026)
Làm lại 2 bài #1843 (real-estate-marketing-plan) và #1832 (real-estate-branding) với 6 ảnh canvas 1000px (`*_m.jpg`, media 2051–2056, scenes `s_m_plan.py`, `s_m_brand.py`). Chạy: `python3 apply_mockups.py <id> <in> <out> --mobile` (đọc `spec['mobile_round']`). Chữ/link bài giữ nguyên (đã kiểm). Chờ user xem trên điện thoại rồi quyết định làm lại cả 59 ảnh.

## Làm lại toàn bộ 59 ảnh mobile-first (13/10/2026)
- 53 cảnh `_m` còn lại do 5 agent dựng (`s_m_*.py`), media WordPress 2059–2111; `spec.json` có đủ 59 ảnh `_m`.
- Đã áp dụng (thay ảnh gen-1): #1825 (live), #1853 (live, áp dụng trực tiếp ảnh `_m`), #1937 #1943 #1949 #1955 #1961 #1967 #1977 #1979 (future, nội dung gốc ở `bases/<id>.html`, đã là bản mới), #1843 #1832 (đợt thử).
- `spec['posts']` của #1859 #1865 #1871 #1877 #1883 #1889 #1895 #1901 đã đổi sang khóa `_m`; các trigger chèn ảnh sau khi bài publish sẽ dùng bản mới.
- `fig()` escape `"` trong alt thành `&quot;` (alt của gads_search_m có dấu nháy).

- 13/10 19:45 UTC: trigger chèn ảnh `_m` vào #1859 (adv_examples_m, adv_metrics_m, adv_test_m) và #1865 (soc_week_m, soc_calendar_m, soc_caption_m): xong, 4 figure thành 5, chữ và link không đổi.

## Thay ảnh cho bài đang có traffic SEO (14/10/2026)
GSC 28 ngày (14/09 đến 12/10) cho thấy các bài cũ Cụm CRM/website/IDX có ảnh Gemini chữ nhỏ, có số bịa và tên hãng. 10 ảnh `_m` mới (media 2125–2134, scenes `s_m_webdesign.py`, `s_m_crm_builder.py`, `s_m_idx.py`) đã thay tại chỗ: #981 (1), #1011 (1), #207 (2), #546 (2), #610 (2), #616 (2). Bỏ #1056 theo ý user (ảnh chụp màn hình trang hãng, giữ nguyên). `spec.json` có mục `traffic_round`.
