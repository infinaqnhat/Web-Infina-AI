# SEO Update Changelog (TEMPLATE)

Lịch sử các lần update/optimize lại bài đã publish (theo quy trình ở `CONTENT_REFRESH_GUIDELINE.md`). Đây là log riêng cho việc **sửa bài cũ**,
khác với tracker sheet Google Sheets (chỉ log bài **mới** viết ra ở Bước 7 trong `SKILL.md`).

**Quy tắc:** mỗi lần refresh/optimize 1 bài đã publish, thêm 1 dòng mới vào bảng dưới. Không sửa hoặc xoá dòng cũ.
Ở site có `skills/post-refresh/`, log chi tiết hơn nằm ở `skills/post-refresh/references/refresh-log.md`; file này dùng cho các sửa nhỏ
(trim meta, đổi thumbnail, thêm link) ngoài vòng GSC của skill đó.

---

## Log

Xóa 3 dòng "Ví dụ" khi bắt đầu ghi log thật. Các dòng này mô phỏng đúng loại thay đổi hay gặp ở site gốc.

| Date | Post ID | URL | Loại thay đổi | Chi tiết | Lý do / trigger |
|------|---------|-----|---------------|----------|------------------|
| 2026-08-20 | 189 | [ví dụ-bai-a](https://example.com/blog/vi-du-bai-a/) | Trim meta description | 188 → 141 ký tự | GSC audit: position 9.1, 20 impressions, 0 click; meta vượt ngưỡng 155 ký tự nên bị cắt |
| 2026-08-20 | 123 | [ví dụ-bai-b](https://example.com/blog/vi-du-bai-b/) | Regenerate ảnh | Thay 6 ảnh (1 featured + 5 trong bài) sang bộ ảnh mới, giữ nguyên alt và vị trí | Audit thumbnail: ảnh cũ không đạt checklist (có chữ lỗi) |
| 2026-08-24 | 237 (target), 492 (sửa) | [ví dụ-bai-c](https://example.com/blog/vi-du-bai-c/) | Thêm internal link | Bài 492 thêm 1 link tới 237 với anchor mô tả (≤8 từ) | Bài 237 chưa có inbound biên tập (xem Bước 6.5) |

---

## Template dòng mới

```
| {YYYY-MM-DD} | {post_id(s)} | [{slug}]({BASE}/{slug}/) | {loại: Trim meta / Regenerate ảnh / Thêm internal link / Update content / Update title/H1 / Khác} | {chi tiết cụ thể, before → after nếu có số liệu} | {lý do: GSC audit, user báo lỗi, đồng bộ guideline...} |
```
