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

---

## Template dòng mới

```
| {YYYY-MM-DD} | {post_id(s)} | [{slug}](https://infina.ai/news/{slug}/) | {loại: Trim meta / Regenerate ảnh / Thêm internal link / Update content / Update title/H1 / Khác} | {chi tiết cụ thể, before → after nếu có số liệu} | {lý do: GSC audit / user request / content decay / khác} |
```
