# SEO Update Changelog

Lịch sử các lần update/optimize lại bài đã publish (theo quy trình ở `CONTENT_REFRESH_GUIDELINE.md`). Đây là log riêng cho việc **sửa bài cũ**, khác với tracker sheet Google Sheets (chỉ log bài **mới** viết ra ở Bước 7 trong `SKILL.md`).

**Quy tắc:** mỗi lần refresh/optimize 1 bài đã publish, append 1 dòng mới vào bảng dưới — không sửa/xoá dòng cũ.

---

## Log

| Date | Post ID | URL | Loại thay đổi | Chi tiết | Lý do / trigger |
|------|---------|-----|---------------|----------|------------------|
| 2026-08-20 | 123 | [chatbot-vs-conversational-ai-real-estate](https://infina.ai/news/chatbot-vs-conversational-ai-real-estate/) | Regenerate ảnh | Thay 6 ảnh (1 featured/HERO + 5 ảnh trong bài) từ Grok Imagine sang Gemini nano-banana, giữ nguyên alt text/vị trí | User yêu cầu — bài đang dùng ảnh Grok (illustration style) thay vì photorealistic Gemini là style chuẩn của site |
| 2026-08-20 | 189 | [zendesk-sunshine-conversations-alternative-real-estate](https://infina.ai/news/zendesk-sunshine-conversations-alternative-real-estate/) | Trim meta description | 188 → 141 ký tự | GSC audit: position 9.1, 20 impressions, 0 click — meta quá dài (>155) bị Google cắt cụt trong SERP |
| 2026-08-20 | 277 | [crm-pipeline-management](https://infina.ai/news/crm-pipeline-management/) | Trim meta description | 211 → 143 ký tự | GSC audit: meta vượt xa ngưỡng 155 ký tự, chắc chắn bị cắt |
| 2026-08-20 | 58 | [best-ai-chatbot-for-real-estate-lead-capture](https://infina.ai/news/best-ai-chatbot-for-real-estate-lead-capture/) | Trim meta description | 173 → 143 ký tự | GSC audit: meta vượt ngưỡng 155 ký tự |
| 2026-08-20 | 521, 513, 528 | [real-estate-contact-form-conversion-rate](https://infina.ai/news/real-estate-contact-form-conversion-rate/), [ai-job-substitution-risk-real-estate-agents](https://infina.ai/news/ai-job-substitution-risk-real-estate-agents/), [embedded-ai-real-estate-brokerage-platforms](https://infina.ai/news/embedded-ai-real-estate-brokerage-platforms/) | Thêm internal link | Thêm 1 câu vào cuối đoạn "Related Reading" mỗi bài, trỏ về `best-ai-chat-platform-real-estate` (post #99) | GSC audit: pillar #99 có impressions cao nhất site (35) nhưng position kém (34.2) — cần thêm internal link authority theo Bước 6 guideline |
| 2026-08-20 | 561, 553, 546, 528, 521, 655, 649, 513, 643, 637, 504, 631 | best-website-builder-for-realtors, best-real-estate-website-builder, real-estate-website-builder, embedded-ai-real-estate-brokerage-platforms, real-estate-contact-form-conversion-rate, real-estate-agent-websites-with-idx, best-idx-website-for-realtors, ai-job-substitution-risk-real-estate-agents, real-estate-crm-with-idx, real-estate-website-builder-with-idx, ai-data-readiness-for-real-estate-brokerages, idx-feed-real-estate-setup | Đổi thumbnail (featured image) | Thay featured image từ ảnh HERO (người ngồi laptop, na ná nhau trên trang chủ) sang ảnh STATS hoặc COMPARISON đã có sẵn trong từng bài — không sinh ảnh mới, không đổi ảnh trong content | User nhận thấy toàn bộ thumbnail trên trang chủ blog quá giống nhau; chọn ảnh thể hiện đúng "key info"/con số nổi bật của từng bài để tăng CTR khi lướt feed |
| 2026-08-20 | 561, 553, 546, 649, 643, 637, 631, 655 | best-website-builder-for-realtors, best-real-estate-website-builder, real-estate-website-builder, best-idx-website-for-realtors, real-estate-crm-with-idx, real-estate-website-builder-with-idx, idx-feed-real-estate-setup, real-estate-agent-websites-with-idx | Regenerate thumbnail (lần 2) | Ảnh COMPARISON/STATS đổi ở lượt trước (từ automation khác) hoá ra là bảng dữ liệu chi tiết 5-6 cột hoặc checklist nhiều câu văn — fail nặng theo `THUMBNAIL_BEST_PRACTICES.md`. Tạo mới 8 ảnh single-message sạch (1 icon/1 badge/1 flow 2 bước, chữ to, không table) bằng Gemini nano-banana, thay lại featured image | User yêu cầu tạo lại ảnh thumbnail cho các bài này sau khi xem checklist best practice — ảnh cũ không đọc được khi thu nhỏ |

---

## Template dòng mới

```
| {YYYY-MM-DD} | {post_id(s)} | [{slug}](https://infina.ai/news/{slug}/) | {loại: Trim meta / Regenerate ảnh / Thêm internal link / Update content / Update title/H1 / Khác} | {chi tiết cụ thể, before → after nếu có số liệu} | {lý do: GSC audit / user request / content decay / khác} |
```
