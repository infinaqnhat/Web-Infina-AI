# keywords/: file keyword tổng của Infina AI

`Infina_AI_RealSale_Keyword_Stats_2026-09-15.csv` là file tổng, **UTF-16 tab-separated**, 26 cột, đúng định dạng xuất từ Google Keyword Planner.
Tên file giữ nguyên ngày seed đầu tiên dù đã merge thêm nhiều đợt (hiện 23.040 dòng). Cột tháng (`Searches: ...`) trống ở toàn bộ dòng, nên chỉ dùng cột `Avg. monthly searches`.

## Cách đọc volume cho đúng

- **Volume là bucket thô** (50, 500, 5.000, 50.000), cột `Currency` toàn VND, nên chỉ dùng để xếp hạng tương đối, không dùng làm số tuyệt đối.
- **Cột `Segmentation`** để trống ở mọi dòng, nên geo của từng dòng không đọc được từ file. Các đợt merge từ 12/10 là geo Hoa Kỳ, và đợt 23/10 cũng đã xác nhận `United States`.
- **Không merge export có geo khác Mỹ** vào file này. Ngày 23/10/2026 một export lead gen geo Vietnam đã được merge nhầm rồi gỡ ra ngay (volume Việt Nam thấp hơn nhiều và không đại diện cho thị trường Mỹ).
- Cột `Competition` của dòng thuộc đợt 23/10 đã đổi từ Low/Medium/High sang Thấp/Trung bình/Cao cho khớp các dòng cũ. Cột này là mức cạnh tranh quảng cáo, không phải độ khó SERP.

## Lịch sử merge (dòng cũ luôn giữ nguyên, chỉ thêm keyword chưa có)

| Ngày | Nguồn | Thêm | Ghi chú |
|---|---|---|---|
| 15/09/2026 | Seed ban đầu | 11.552 | |
| đầu 10/2026 | Chatbot/conversational AI, real estate CRM (US-geo), CEP | vài trăm đến 1.486 | xem `content-plan.md` mục Cụm 1, 2 |
| 12/10/2026 | `Keyword_Stats_2026-10-12` (geo Hoa Kỳ) | 7.433 | 175 dòng trùng giá trị giống hệt; bỏ 2 dòng tổng ở đầu export |
| 23/10/2026 | `Keyword_Stats_2026-10-23 at 13_06_17` (lead generation, **geo Hoa Kỳ**, kỳ 10/2025 đến 09/2026) | 3.396 | 884 keyword đã có (giữ nguyên dòng cũ; sau khi chuẩn hóa số, 534 dòng khác ở cột phụ như bid, nhãn, nhưng chỉ 11 dòng khác volume); sắp lại theo volume giảm dần, dòng cũ giữ nguyên thứ tự tương đối. Bản export geo Vietnam (13:01) đã loại |
| 23/10/2026 | `Keyword_Stats_2026-10-23 at 16_13_09` (lead management, **geo Hoa Kỳ**, kỳ 10/2025 đến 09/2026) | 659 | 841 dòng dữ liệu, 182 keyword đã có (giữ nguyên dòng cũ; 52 dòng có volume khác, không cập nhật). Chỉ 205 trong 659 keyword mới có volume (454 dòng trống), và gần như toàn nhiễu do Keyword Planner mở rộng từ khóa chung (`value`, `led`, `follow up`, `lead conversion`): chỉ khoảng 5 keyword mới ≥ 500 liên quan lead management (xem `references/` hoặc lịch sử commit). Header tháng lệch 1 tháng so với file tổng (Oct 2025 đến Sep 2026), nhưng cột tháng trống nên bỏ qua |
| 26/10/2026 | `Keyword_Stats_2026-10-26 at 14_27_06` (sphere of influence + referral, **geo Hoa Kỳ**, kỳ 10/2025 đến 09/2026) | 1.703 | 1.825 dòng dữ liệu, 122 keyword đã có (giữ nguyên dòng cũ, 0 dòng khác volume). 880 keyword mới có volume, phần lớn nhiễu (`thank you note`, `sphere of influence` nghĩa lịch sử/chính trị). Dùng được cho BĐS: `real estate agent referral` (5.000), `real estate referral program(s)`, `realtor referral program`, `real estate referral companies` (500). Tổng file 24.743 dòng. |

## Quy trình merge lần sau

1. Xuất từ Keyword Planner với **vị trí Hoa Kỳ**. Kiểm tra dòng 5 của file xuất: phải là `Hoa Kỳ` hoặc `United States`. Nếu là quốc gia khác thì **dừng và báo lại**, đừng merge.
2. Bỏ 2 dòng tiêu đề và 2 dòng tổng ở đầu, giữ header của file tổng.
3. So khóa theo `keyword.strip().lower()`. Chỉ thêm khóa chưa có, không sửa dòng cũ.
4. Ghi lại UTF-16 có BOM, CRLF. Kiểm tra dòng cũ không đổi (so sánh danh sách dòng trước và sau).
