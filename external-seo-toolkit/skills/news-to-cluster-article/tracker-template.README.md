# Tracker sheet (TEMPLATE)

Tạo một Google Sheet với **đúng 6 cột theo thứ tự**: `# | Date | Title | URL | Focus Keyword | Type`, dán nội dung
`tracker-template.tsv` vào ô A1 (dán dạng tab-separated để Sheets tự tách cột). Điền fileId của sheet vào
`TRACKER_FILE_ID` ở mục Cấu hình site của `SKILL.md`, và cấp quyền đọc cho Google Drive connector.

- `Type = Plan`: bài pillar/cornerstone. Focus Keyword của nó là **PILLAR_KW đã bị chiếm**, không dùng lại cho bài khác.
- `Type = News`: bài cluster viết từ tin tức (loại bài skill này tạo ra). FOCUS_KW riêng của nó cũng đã bị chiếm.
- Skill đọc toàn bộ sheet bằng `download_file_content` với `exportMimeType: "text/csv"`, không dùng `read_file_content` (xem Bước 2b).
- Ghi dòng mới bằng cách dán dòng **tab-separated** (không dùng bảng markdown `|`), xem Bước 7.

Ví dụ một dòng đã điền (Infina AI):

```
16	07/08/2026	Compliance-First AI: What Every Brokerage Should Demand	https://infina.ai/news/compliance-first-ai-brokerage/	tcpa compliance ai texting real estate	News
```
