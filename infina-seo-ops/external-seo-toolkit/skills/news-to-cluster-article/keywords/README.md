# Thư mục `keywords/`: dữ liệu keyword của site bạn (TEMPLATE)

Skill `news-to-cluster-article` (Bước 3) đọc 2 loại dữ liệu từ thư mục này. Toolkit **không kèm dữ liệu
thật của Infina** (file gốc là xlsx 2,6MB và csv 2,7MB, nằm trong repo `infinaqnhat/web-infina-ai`
tại `wordpress-mcp/skills/news-to-cluster-article/keywords/`). Bạn tạo 2 file thay thế theo mẫu bên dưới.

| File của bạn | Mẫu | Dùng để |
|---|---|---|
| `[ĐIỀN: tên site]_content_pillars.csv` | `content-pillars-template.csv` | Danh sách pillar dự kiến và keyword mục tiêu của từng pillar |
| `[ĐIỀN: tên site]_keyword_stats_YYYY-MM-DD.csv` | `keyword-stats-template.csv` | Volume, cạnh tranh, YoY của từng keyword, làm nguồn chọn FOCUS_KW |

## Cách có dữ liệu

1. **Volume**: xuất từ Google Keyword Planner (Tools > Keyword Planner > Get search volume and forecasts > Download).
   File xuất ra thường là **UTF-16 tab-separated**, đổi sang UTF-8 trước khi đọc bằng Python:
   `iconv -f UTF-16 -t UTF-8 export.csv > keyword-stats.csv`. Giữ lại các cột trong mẫu, bỏ các cột quảng cáo.
2. **Pillar**: lập từ chính plan cụm của bạn (xem `pillar-cluster-writer/SKILL.md` Bước 4 và
   `content-plan-template.md`). Mỗi pillar một dòng, có `Target keyword` và `URL` (để trống nếu chưa viết).
3. **Cập nhật**: xuất lại volume mỗi quý, đặt ngày trong tên file để biết dữ liệu mới đến đâu.

## Ví dụ file thật (Infina AI)

Bản gốc có 2 phần (chỉ nêu cấu trúc, không kèm dữ liệu):
- File xlsx 7 sheet: `Content Pillars (AIDA)` (7 pillar theo AIDA), 1 sheet mỗi nhóm main keyword (Chatbot, CRM, Website Builder...
  mỗi sheet gồm Main keyword, Keyword, Avg Monthly Searches, Competition, Top 10 SERP, Search intent, Suggested SEO titles, Notes),
  và sheet `Customer Segments` (6 cột: phân khúc, nhân khẩu, lý do dùng, hành vi, rào cản, pain point).
- File csv xuất thẳng từ Keyword Planner, khoảng 28 cột gồm 12 tháng volume.

Bạn không cần đúng cấu trúc đó. Chỉ cần mỗi keyword có: **từ khóa, volume trung bình tháng, mức cạnh tranh, nhóm/pillar nó thuộc về**.
