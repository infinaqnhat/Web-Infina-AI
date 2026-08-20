# Guideline: Update & Optimize Existing SEO Article (Content Refresh)

Quy trình tham khảo khi cần audit và refresh lại 1 bài đã publish (khác với viết bài mới ở `SKILL.md`). Dựa trên best practice 2026 từ Ahrefs, Animalz, SEOptimer, Semrush, và các nguồn liệt kê ở cuối file.

---

## Bước 1 — Xác định bài nào cần refresh (data-driven)

Dùng Google Search Console (xem `SKILL.md` → Bước 8 để lấy traffic data) để lọc ra các bài có ít nhất 1 trong các dấu hiệu sau:

- Traffic giảm >20% trong 90 ngày so với kỳ trước
- Rank tụt >5 bậc so với trước
- CTR giảm nhưng impressions vẫn ổn định (vẫn hiện ra nhưng không ai click — thường do title/meta không hấp dẫn)
- Không có backlink mới trong 6+ tháng

**Xếp tier ưu tiên:**

| Tier | Điều kiện | Hành động |
|------|-----------|-----------|
| Tier 1 | Traffic/impression cao, đang decay | Full refresh (toàn bộ các bước dưới) |
| Tier 2 | Traffic trung bình | Refresh nhanh: intro, kết luận, số liệu |
| Tier 3 | Traffic quá thấp, không cứu được | Merge vào bài khác hoặc bỏ (không refresh) |

---

## Bước 2 — Check lại search intent hiện tại

SERP có thể đã đổi format kể từ lúc viết bài (ví dụ top 10 giờ toàn listicle thay vì bài hướng dẫn dài, hoặc ngược lại). Search lại focus keyword, xem top 10 hiện tại đang trả lời intent gì — nếu bài cũ lệch intent, cần viết lại theo format phù hợp chứ không chỉ sửa câu chữ.

---

## Bước 3 — Content gap & depth check

So bài hiện tại với top-ranking competitors:

- Thiếu section nào đối thủ có?
- Bài có ngắn hơn đáng kể không?
- Thiếu số liệu/ví dụ/data nào đối thủ đang dùng?

Thêm depth là cách hiệu quả nhất để chữa content decay — hiệu quả hơn hầu hết các thay đổi on-page khác.

---

## Bước 4 — Update nội dung

- Thay số liệu/thống kê cũ bằng data mới nhất (kèm nguồn)
- Xóa phần lỗi thời (tool/luật/feature không còn đúng)
- Thêm section mới nếu thiếu depth (Bước 3)
- Update ảnh nếu screenshot/UI cũ

---

## Bước 5 — On-page re-optimize

- **Title tag:** 50–60 ký tự, FOCUS_KW gần đầu
- **Meta description:** 140–155 ký tự, có CTA rõ ràng
- **H1** khớp title; **H2/H3** đúng thứ tự phân cấp (không nhảy cóc H1 → H4)
- Đảm bảo FOCUS_KW vẫn còn đúng chỗ: xuất hiện trong title, ít nhất 1 H2, mật độ 0.5–2.5% — dùng lại `check_seo()` trong `SKILL.md` để verify
- Không có em dash (—), tuân theo văn phong đã set trong `SKILL.md`

---

## Bước 6 — Internal linking

- Thêm link từ 3–5 bài mới hơn trỏ ngược về bài đang refresh (một bài mới publish là cơ hội tự nhiên để làm việc này)
- Review lại internal link cũ trong bài — có link nào trỏ tới trang không còn tồn tại không
- Vẫn tuân theo nguyên tắc anti-cannibalization: không đổi FOCUS_KW của bài thành trùng PILLAR_KW

---

## Bước 7 — Technical / schema check

- Fix broken link (cả nội bộ và external)
- Kiểm tra Article schema hợp lệ (Search Console → Enhancements report)
- Core Web Vitals nếu có ảnh hưởng tới trang này

---

## Bước 8 — E-E-A-T signals

Các Core Update gần đây phạt mạnh content AI mỏng, thiếu E-E-A-T. Cần đảm bảo:

- Tác giả/nguồn rõ ràng
- Trích dẫn nguồn xác thực (external dofollow link tới nguồn uy tín — đã áp dụng trong `check_seo()`)
- Ngày cập nhật hiển thị trên bài

---

## Bước 9 — Update ngày, KHÔNG đổi URL

Đổi "last modified date" (qua `update_post` với param `date`) là tín hiệu freshness mạnh với Google.

**Tuyệt đối không đổi slug/URL** — sẽ mất hết backlink đã trỏ về và mất lịch sử index đã có.

---

## Bước 10 — Re-submit index + monitor

- Google Search Console → URL Inspection → Request Indexing, để Google crawl lại ngay thay vì chờ crawl tự nhiên
- Theo dõi lại sau 2–4 tuần qua GSC (so sánh period trước/sau) xem impressions/position/clicks có cải thiện không
- Nếu sau 4–6 tuần vẫn không cải thiện, xem lại Bước 2 (search intent) — có thể bài đã lệch intent hoàn toàn, cần viết lại từ đầu thay vì refresh

---

## Kỳ vọng kết quả (theo data ngành)

- Refresh theo quý (quarterly) hiệu quả hơn refresh hàng năm khoảng 42%
- Chỉ cần update ~20% nội dung của 1 bài đang decay đã có thể phục hồi >50% traffic trong vài tuần

---

## Nguồn tham khảo

- [The Complete Content Refresh SEO Checklist for 2026 — TopicalMap.ai](https://topicalmap.ai/blog/auto/content-refresh-seo-checklist-2026)
- [Content Refresh Prioritization: 2026 SEO Decision Matrix — Digital Applied](https://www.digitalapplied.com/blog/content-refresh-prioritization-2026-seo-decision-matrix)
- [When to Update Content for Better SEO Results (2026 Guide) — Wellows](https://wellows.com/blog/update-strategy/)
- [Content Refresh for SEO & AI Visibility: A 2026 Playbook — Growth Lessons](https://growthlessons.vercel.app/blog/content-refresh-seo-ai-visibility)
- [How to Refresh Old Content for SEO and the Age of AI — SEOptimer](https://www.seoptimer.com/blog/republishing-content/)
- [Content Refresh Strategy: How to Update Old Content for SEO and AI Search — Animalz](https://www.animalz.co/blog/content-refresh)
- [Content Decay: How to Refresh Outdated Statistics for SEO — WordPattern](https://wordpattern.org/blogs/how-to-refresh-outdated-statistics-stats-for-better-rankings/)
- [What Is Content Decay? (And How to Fix It Before It Tanks Your Traffic) — Ahrefs](https://ahrefs.com/blog/content-decay/)
- [How to Improve Old Blog Posts That Stopped Ranking — Click Laboratory](https://www.clicklaboratory.com/content-analytics/improve-old-blog-posts-stopped-ranking/)
- [On-page SEO checklist: The complete task list for 2026 — Semrush](https://www.semrush.com/blog/on-page-seo-checklist/)
- [On-Page SEO Checklist (2026) — Titles, Headings, Schema & Core Web Vitals — Prateeksha](https://prateeksha.com/blog/on-page-seo-checklist-2026-titles-headings-schema-core-web-vitals)
- [SEO Audit Checklist: A Practical 2026 Framework — Vibe Marketing](https://vibe-marketing.org/blog/seo-audit-checklist)
