# Danh mục cảnh mockup có sẵn

Mỗi cảnh là một hàm/biến trong `scripts/scenes/s_<nhóm>.py`, render ra `m_<tên>.jpg` 1600x900. Chạy `python3 s_<nhóm>.py <tên>`.

| Cảnh | File | Bài đã dùng | Chèn ở mục | Nội dung |
|---|---|---|---|---|
| `fly_layouts` | s_fly | #1967 flyers | cuối "Layout Examples" | 4 bố cục flyer (photo trên, trái-phải, headline lớn, lưới 4 ảnh) |
| `fly_anno` | s_fly | #1967 | thay ảnh DEMO sau "What to Put" | flyer listing có 6 chú thích số khớp danh sách của bài |
| `fly_vs` | s_fly | #1967 | thay ảnh COMPARISON | flyer rối (5 phông, 6 ảnh) vs flyer sạch |
| `testi_cards` | s_testi | #1949 testimonials | sau bảng yếu/mạnh | thẻ yếu vs thẻ mạnh, tô màu situation, result, person |
| `testi_ask` | s_testi | #1949 | sau 3 câu hỏi | khung tin nhắn xin review + 3 bước |
| `testi_site` | s_testi | #1949 | sau "Where to Use" | trang web mẫu, 3 quote cạnh form liên hệ |
| `lp_price` | s_lp | #1955 listing presentation | cuối mục Pricing | slide pricing: 3 comps, thanh khoảng giá |
| `lp_plan` | s_lp | #1955 | sau đoạn đầu mục Marketing Plan | slide kế hoạch 3 cột có mốc ngày |
| `lp_outline` | s_lp | #1955 | sau danh sách 12 slide | lưới 12 slide thumbnail |
| `card_layouts` | s_card | #1883 business cards | sau bảng Layouts | 4 mặt trước thẻ + chú thích mặt sau |
| `card_back` | s_card | #1883 | sau "Lines for the Back" | mặt trước, mặt sau QR, mặt sau referral |
| `card_proof` | s_card | #1883 | thay ảnh DEMO "Proofread" | thẻ lớn có 5 chấm kiểm + checklist |
| `logo_types` | s_logo | #1889 logos | sau "Examples in Words" | 5 loại logo, mỗi loại một ví dụ |
| `logo_small` | s_logo | #1889 | thay ảnh DEMO "Files and Technical Checks" | logo ở 4 cỡ, một màu, đảo màu |
| `logo_cliche` | s_logo | #1889 | thay ảnh COMPARISON, trước "Color and Type" | logo sáo mòn vs logo riêng |
| `post_just_sold` | s_post | #1877 postcards | sau bảng "by Goal" | postcard just sold, mặt trước và sau |
| `post_anno` | s_post | #1877 | sau mục Design | postcard có 5 chú thích số |
| `post_qr` | s_post | #1877 | thay ảnh DEMO "Track Responses" | market update card + bảng đo mỗi mailing |
| `bio_profile` | s_bio | #1895 bio | thay ảnh DEMO sau template | trang hồ sơ, tô màu who, proof, next step |
| `bio_beforeafter` | s_bio | #1895 | sau mục "Before and After" | 4 cặp dòng yếu, dòng mạnh |
| `bio_gallery` | s_bio | #1895 | sau "Examples" | 3 thẻ hồ sơ theo đối tượng |
| `gbp_fields` | s_gbp | #1937 Google Business Profile | sau bảng "What to Enter in Each Field" | hồ sơ doanh nghiệp mẫu có 7 chú thích số khớp bảng (không dùng logo Google) |
| `gbp_review` | s_gbp | #1937 | thay ảnh COMPARISON cuối mục Reviews | 1 review + phản hồi của chủ, 3 quy tắc, ví dụ cấm tặng quà |
| `gbp_name` | s_gbp | #1937 | trước "Measure" | tên thật vs tên nhồi từ khóa |
| `plan_budget` | s_plan | #1843 Marketing Plan | cuối mục Budget | 2 thanh xếp chồng: agent mới $500, agent đang lớn $1,500, số % lấy từ bảng của bài |
| `plan_template` | s_plan | #1843 | sau mục Template | sheet "3 Plan" của file xlsx thật (dựng lại bằng HTML từ dữ liệu file, vì LibreOffice không mở được ở môi trường này) |
| `plan_tracker` | s_plan | #1843 | thay ảnh DEMO mục Review | sheet "4 Quarterly Review" với số mẫu, spend per closing tự tính |
| `seo_results` | s_seo | #1871 SEO | trước "What Google Says Drives Local Rankings" | trang tìm kiếm mẫu (không dùng giao diện Google): local pack + organic, 2 chú thích |
| `seo_profile` | s_seo | #1871 | thay ảnh DEMO mục Profile | checklist 6 mục của hồ sơ |
| `seo_plan` | s_seo | #1871 | trước "Should You Hire Someone" | kế hoạch 90 ngày, 3 cột tháng, mỗi tháng 4 đến 6 giờ |
| `name_uses` | s_name | #1979 Name Ideas | thay ảnh COMPARISON mục Online | một tên trên biển, thẻ, email, social, website |
| `name_formulas` | s_name | #1979 | sau danh sách công thức | 5 công thức đặt tên + ví dụ lấy từ bài |
| `name_test` | s_name | #1979 | thay ảnh DEMO mục Test | 5 bước kiểm tên |
| `soc_calendar` | s_soc | #1865 Social | sau bảng lịch 4 tuần | lịch 4 tuần x 3 bài, gắn nhãn loại bài (màu) |
| `soc_week` | s_soc | #1865 | thay ảnh DEMO sau bảng routine | routine thứ Hai đến thứ Sáu, tổng 140 phút |
| `soc_caption` | s_soc | #1865 | trước "Batch Your Content" | một bài đăng với caption mẫu, 3 chú thích |
| `adv_examples` | s_adv | #1859 Advertising | trước "Fair Housing Rules" | 4 quảng cáo mẫu (search, social x3) |
| `adv_metrics` | s_adv | #1859 | trước "How to Test" | phễu mẫu $900, 30 lead, 6 hẹn, 2 khách, 1 closing |
| `adv_test` | s_adv | #1859 | thay ảnh DEMO mục Test | 5 bước test 30 ngày + thanh tiến độ |
| `pillar_channels` | s_pillar | #1825 pillar | sau bảng "Strategies Compared" | 6 kênh đặt theo chi phí và thời gian ra kết quả, lấy từ bảng của bài |
| `pillar_stage` | s_pillar | #1825 | sau bảng "by Career Stage" | 3 giai đoạn: ưu tiên và lý do (nguyên văn bảng) |
| `pillar_leadsource` | s_pillar | #1825 | thay ảnh DEMO mục Measure | form liên hệ có trường Lead source + 3 câu hỏi |
| `brand_sheet` | s_brand | #1832 hub branding | trước "A 20-Minute Brand Audit" | brand sheet một trang đủ 6 mục theo bài |
| `brand_looks` | s_brand | #1832 | thay ảnh DEMO mục Teams and Premium | một thương hiệu trên thẻ, web, biển, bài đăng, email |
| `brand_mixed` | s_brand | #1832 | thay ảnh COMPARISON cuối mục Audit | look lẫn lộn vs look nhất quán |
| `ideas_matrix` | s_ideas | #1853 marketing ideas | sau bảng Ten Quick Wins | 10 ý tưởng đặt theo chi phí và công sức (từ bảng) |
| `ideas_notes` | s_ideas | #1853 | trước "Social Media Ideas" | thư ghi chú kỷ niệm nhà + bản tin thị trường quý |
| `referral_ask` | s_ref | #1961 referral | thay ảnh DEMO sau 5 bước | tin nhắn xin giới thiệu + 5 bước |
| `referral_agreement` | s_ref | #1961 | cuối mục Referral Fee | dàn ý hợp đồng giới thiệu giữa 2 brokerage (ô phí để trống) |
| `referral_tracker` | s_ref | #1961 | cuối mục Track | bảng theo dõi người giới thiệu |
| `gift_note` | s_gift | #1977 closing gifts | thay ảnh COMPARISON mục Personalize | thiệp in sẵn vs ghi chú viết tay |
| `gift_timeline` | s_gift | #1977 | thay ảnh DEMO mục When to Give | 3 lần chạm: ngày đóng, 1 tuần sau, kỷ niệm |
| `gift_log` | s_gift | #1977 | trước "Final Thoughts" | sổ ghi quà tặng |
| `gads_targeting` | s_gads | #1943 Google Ads | thay ảnh COMPARISON sau bảng targeting | bản đồ: bán kính/thành phố được, ZIP không được |
| `gads_search` | s_gads | #1943 | sau bảng "What to Bid On" | tìm kiếm của người bán, quảng cáo, trang đích khớp |
| `gads_weeks` | s_gads | #1943 | thay ảnh DEMO mục Test | test 4 tuần, nguyên văn các bước |
| `soft_connect` | s_soft | #1901 software | trước "How to Trial" | CRM ở giữa, 5 công cụ kết nối (từ bảng) |
| `soft_trial` | s_soft | #1901 | trước "Questions to Ask Before You Buy" | 6 bước dùng thử |
| `soft_sprawl` | s_soft | #1901 | trước "Common Mistakes" | nhiều thuê bao chồng chéo vs bộ công cụ gọn, giá mẫu |


## Cảnh nên làm tiếp (chưa có)

Wave 3: hộp kịch bản door knocking và cold calling, checklist open house, bảng chọn farm, lịch 12 tháng, khung video (kịch bản và thiết lập điện thoại).
Các bài còn lại của Cụm 9 chưa có mockup: #1859 và #1865 (đã dựng, chờ publish), #1871 (đã dựng, chờ publish).
