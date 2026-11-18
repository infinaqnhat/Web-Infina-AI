# Danh mục cảnh mockup (mobile-first)

Mỗi cảnh là một biến trong `scripts/scenes/s_m_<nhóm>.py`, render ra `m_<tên>.jpg` canvas 1000px rộng (chạy `MOCKUP_OUT=<thư mục> python3 s_m_<nhóm>.py <tên>`). Cả 59 cảnh đã có bản mobile-first, user duyệt ngày 13/10/2026. Bản gen-1 (1600x900, `s_<nhóm>.py` không có `m_`) không đạt chuẩn điện thoại, chỉ giữ để tham khảo nội dung.

| Cảnh | File | Bài | Kích thước | Nội dung (bản mobile-first) |
|---|---|---|---|---|
| `fly_layouts_m` | s_m_fly | #1967 | 1000x1500 | 4 bố cục flyer (photo trên, trái-phải, headline lớn, lưới 4 ảnh) |
| `fly_anno_m` | s_m_fly | #1967 | 1000x1405 | flyer listing có 6 chú thích số khớp danh sách của bài |
| `fly_vs_m` | s_m_fly | #1967 | 1000x898 | flyer rối (5 phông, 6 ảnh) vs flyer sạch |
| `testi_cards_m` | s_m_testi | #1949 | 1000x1190 | thẻ yếu vs thẻ mạnh, tô màu situation, result, person |
| `testi_ask_m` | s_m_testi | #1949 | 1000x1328 | khung tin nhắn xin review + 3 bước |
| `testi_site_m` | s_m_testi | #1949 | 1000x1518 | trang web mẫu, 3 quote cạnh form liên hệ |
| `lp_price_m` | s_m_lp | #1955 | 1000x1252 | slide pricing: 3 comps, thanh khoảng giá |
| `lp_plan_m` | s_m_lp | #1955 | 1000x1305 | slide kế hoạch 3 cột có mốc ngày |
| `lp_outline_m` | s_m_lp | #1955 | 1000x1332 | lưới 12 slide thumbnail |
| `card_layouts_m` | s_m_card | #1883 | 1000x1400 | 4 mặt trước thẻ + chú thích mặt sau |
| `card_back_m` | s_m_card | #1883 | 1000x1220 | mặt trước, mặt sau QR, mặt sau referral |
| `card_proof_m` | s_m_card | #1883 | 1000x1290 | thẻ lớn có 5 chấm kiểm + checklist |
| `logo_types_m` | s_m_logo | #1889 | 1000x1245 | 5 loại logo, mỗi loại một ví dụ |
| `logo_small_m` | s_m_logo | #1889 | 1000x1070 | logo ở 4 cỡ, một màu, đảo màu |
| `logo_cliche_m` | s_m_logo | #1889 | 1000x1150 | logo sáo mòn vs logo riêng |
| `post_just_sold_m` | s_m_post | #1877 | 1000x1422 | postcard just sold, mặt trước và sau |
| `post_anno_m` | s_m_post | #1877 | 1000x1320 | postcard có 5 chú thích số |
| `post_qr_m` | s_m_post | #1877 | 1000x1386 | market update card + bảng đo mỗi mailing |
| `bio_profile_m` | s_m_bio | #1895 | 1000x1320 | trang hồ sơ, tô màu who, proof, next step |
| `bio_beforeafter_m` | s_m_bio | #1895 | 1000x1250 | 4 cặp dòng yếu, dòng mạnh |
| `bio_gallery_m` | s_m_bio | #1895 | 1000x1490 | 3 thẻ hồ sơ theo đối tượng |
| `gbp_fields_m` | s_m_gbp | #1937 | 1000x1450 | hồ sơ doanh nghiệp mẫu có 7 chú thích số khớp bảng (không dùng logo Google) |
| `gbp_review_m` | s_m_gbp | #1937 | 1000x1120 | 1 review + phản hồi của chủ, 3 quy tắc, ví dụ cấm tặng quà |
| `gbp_name_m` | s_m_gbp | #1937 | 1000x1030 | tên thật vs tên nhồi từ khóa |
| `plan_budget_m` | s_m_plan | #1843 | 1000x1431 | 2 thanh xếp chồng: agent mới $500, agent đang lớn $1,500, số % lấy từ bảng của bài |
| `plan_template_m` | s_m_plan | #1843 | 1000x1080 | sheet "3 Plan" của file xlsx thật (dựng lại bằng HTML từ dữ liệu file, vì LibreOffice không mở được ở môi trường này) |
| `plan_tracker_m` | s_m_plan | #1843 | 1000x1305 | sheet "4 Quarterly Review" với số mẫu, spend per closing tự tính |
| `seo_results_m` | s_m_seo | #1871 | 1000x1320 | trang tìm kiếm mẫu (không dùng giao diện Google): local pack + organic, 2 chú thích |
| `seo_profile_m` | s_m_seo | #1871 | 1000x1240 | checklist 6 mục của hồ sơ |
| `seo_plan_m` | s_m_seo | #1871 | 1000x1480 | kế hoạch 90 ngày, 3 cột tháng, mỗi tháng 4 đến 6 giờ |
| `name_uses_m` | s_m_name | #1979 | 1000x1250 | một tên trên biển, thẻ, email, social, website |
| `name_formulas_m` | s_m_name | #1979 | 1000x1380 | 5 công thức đặt tên + ví dụ lấy từ bài |
| `name_test_m` | s_m_name | #1979 | 1000x1160 | 5 bước kiểm tên |
| `soc_calendar_m` | s_m_soc | #1865 | 1000x1127 | lịch 4 tuần x 3 bài, gắn nhãn loại bài (màu) |
| `soc_week_m` | s_m_soc | #1865 | 1000x1046 | routine thứ Hai đến thứ Sáu, tổng 140 phút |
| `soc_caption_m` | s_m_soc | #1865 | 1000x1338 | một bài đăng với caption mẫu, 3 chú thích |
| `adv_examples_m` | s_m_adv | #1859 | 1000x1736 | 4 quảng cáo mẫu (search, social x3) |
| `adv_metrics_m` | s_m_adv | #1859 | 1000x1344 | phễu mẫu $900, 30 lead, 6 hẹn, 2 khách, 1 closing |
| `adv_test_m` | s_m_adv | #1859 | 1000x1225 | 5 bước test 30 ngày + thanh tiến độ |
| `pillar_channels_m` | s_m_pillar | #1825 | 1000x1245 | 6 kênh đặt theo chi phí và thời gian ra kết quả, lấy từ bảng của bài |
| `pillar_stage_m` | s_m_pillar | #1825 | 1000x1268 | 3 giai đoạn: ưu tiên và lý do (nguyên văn bảng) |
| `pillar_leadsource_m` | s_m_pillar | #1825 | 1000x1305 | form liên hệ có trường Lead source + 3 câu hỏi |
| `brand_sheet_m` | s_m_brand | #1832 | 1000x1108 | brand sheet một trang đủ 6 mục theo bài |
| `brand_looks_m` | s_m_brand | #1832 | 1000x1200 | một thương hiệu trên thẻ, web, biển, bài đăng, email |
| `brand_mixed_m` | s_m_brand | #1832 | 1000x1130 | look lẫn lộn vs look nhất quán |
| `ideas_matrix_m` | s_m_ideas | #1853 | 1000x1266 | 10 ý tưởng đặt theo chi phí và công sức (từ bảng) |
| `ideas_notes_m` | s_m_ideas | #1853 | 1000x1290 | thư ghi chú kỷ niệm nhà + bản tin thị trường quý |
| `referral_ask_m` | s_m_ref | #1961 | 1000x1584 | tin nhắn xin giới thiệu + 5 bước |
| `referral_agreement_m` | s_m_ref | #1961 | 1000x1410 | dàn ý hợp đồng giới thiệu giữa 2 brokerage (ô phí để trống) |
| `referral_tracker_m` | s_m_ref | #1961 | 1000x1160 | bảng theo dõi người giới thiệu |
| `gift_note_m` | s_m_gift | #1977 | 1000x1290 | thiệp in sẵn vs ghi chú viết tay |
| `gift_timeline_m` | s_m_gift | #1977 | 1000x1170 | 3 lần chạm: ngày đóng, 1 tuần sau, kỷ niệm |
| `gift_log_m` | s_m_gift | #1977 | 1000x1270 | sổ ghi quà tặng |
| `gads_targeting_m` | s_m_gads | #1943 | 1000x1290 | bản đồ: bán kính/thành phố được, ZIP không được |
| `gads_search_m` | s_m_gads | #1943 | 1000x1500 | tìm kiếm của người bán, quảng cáo, trang đích khớp |
| `gads_weeks_m` | s_m_gads | #1943 | 1000x1246 | test 4 tuần, nguyên văn các bước |
| `soft_connect_m` | s_m_soft | #1901 | 1000x1370 | CRM ở giữa, 5 công cụ kết nối (từ bảng) |
| `soft_trial_m` | s_m_soft | #1901 | 1000x1286 | 6 bước dùng thử |
| `soft_sprawl_m` | s_m_soft | #1901 | 1000x1080 | nhiều thuê bao chồng chéo vs bộ công cụ gọn, giá mẫu |

## Cảnh nên làm tiếp (chưa có)

Wave 3 (dựng ngay theo mobile-first): hộp kịch bản door knocking và cold calling, checklist open house, bảng chọn farm, lịch 12 tháng, khung video (kịch bản và thiết lập điện thoại).
Các bài còn lại của Cụm 9 chưa có mockup: #1859 và #1865 (đã dựng, chờ publish), #1871 (đã dựng, chờ publish).
