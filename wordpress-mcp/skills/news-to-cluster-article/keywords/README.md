# keywords/: file keyword tổng của Infina AI

`Infina_AI_RealSale_Keyword_Stats_2026-09-15.csv` là file tổng, **UTF-16 tab-separated**, 26 cột, đúng định dạng xuất từ Google Keyword Planner.
Tên file giữ nguyên ngày seed đầu tiên dù đã merge thêm nhiều đợt. Cột tháng (`Searches: ...`) trống ở toàn bộ dòng, nên chỉ dùng cột `Avg. monthly searches`.

## Cách đọc volume cho đúng

- **Volume là bucket thô** (50, 500, 5.000, 50.000), cột `Currency` toàn VND, nên chỉ dùng để xếp hạng tương đối, không dùng làm số tuyệt đối.
- **Cột `Segmentation`**: để trống = các đợt export lấy volume Mỹ hoặc không khai geo (18.985 dòng đầu). `Vietnam` = dòng từ đợt 23/10/2026, **volume của thị trường Việt Nam**, không đại diện cho Mỹ. Các dòng này nằm ở cuối file, không xếp lẫn theo volume.
- Khi chọn FOCUS_KW cho thị trường Mỹ, chỉ tin volume ở dòng có `Segmentation` trống. Dòng `Vietnam` chỉ nên coi là gợi ý biến thể từ khóa.

## Lịch sử merge (dòng cũ luôn giữ nguyên, chỉ thêm keyword chưa có)

| Ngày | Nguồn | Thêm | Ghi chú |
|---|---|---|---|
| 15/09/2026 | Seed ban đầu | 11.552 | |
| đầu 10/2026 | Chatbot/conversational AI, real estate CRM (US-geo), CEP | vài trăm đến 1.486 | xem `content-plan.md` mục Cụm 1, 2 |
| 12/10/2026 | `Keyword_Stats_2026-10-12` (geo Hoa Kỳ) | 7.433 | 175 dòng trùng giá trị giống hệt; bỏ 2 dòng tổng ở đầu export |
| 23/10/2026 | `Keyword_Stats_2026-10-23` (lead generation, **geo Vietnam**, kỳ 10/2025 đến 09/2026) | 3.396 | 884 keyword đã có (565 giá trị khác, giữ nguyên dòng cũ); gắn `Segmentation = Vietnam`, xếp ở cuối file |

## Quy trình merge lần sau

1. Xuất từ Keyword Planner với **vị trí Hoa Kỳ** (dòng 4 của file xuất phải là `Hoa Kỳ` hoặc `United States`). Nếu là quốc gia khác, vẫn merge được nhưng phải gắn `Segmentation`.
2. Bỏ 2 dòng tiêu đề và 2 dòng tổng ở đầu, giữ header của file tổng.
3. So khóa theo `keyword.strip().lower()`. Chỉ thêm khóa chưa có, không sửa dòng cũ.
4. Ghi lại UTF-16 có BOM, CRLF. Kiểm tra dòng cũ không đổi (so sánh danh sách dòng trước và sau).
