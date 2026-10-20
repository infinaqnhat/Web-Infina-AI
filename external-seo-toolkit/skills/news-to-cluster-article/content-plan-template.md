# Content Plan (TEMPLATE)

Copy file này thành `content-plan.md` ở gốc repo và điền. Skill `news-to-cluster-article` (Bước 4, 6.5) và
`pillar-cluster-writer` (Bước 8.5) **đọc và ghi** file này. Đây là **nguồn đúng duy nhất về "bài nào thuộc cụm nào"**:
đừng suy ra từ link graph (xem `references/internal-linking-guide.md`, mục 2).

Phần ví dụ lấy từ site gốc (Infina AI) để bạn thấy mức chi tiết; xóa các dòng "Ví dụ" khi điền dữ liệu thật.

---

## 1. Tổng quan site

- **Site/blog:** `[ĐIỀN: tên, BASE]`. Ví dụ: "Infina AI News, `https://infina.ai/news`".
- **Money page:** `[ĐIỀN: URL]`. Ví dụ: `https://infina.ai/` (SaaS cho agent bất động sản Mỹ).
- **Số cụm:** `[ĐIỀN]`. Ví dụ: 9 cụm (CRM, chatbot, website builder, voice AI, landing page, lead gen, compliance, marketing...).
- **Cụm ưu tiên (gắn với sản phẩm):** `[ĐIỀN: cụm nào đang chủ động viết bài mới]`. Ví dụ: Cụm 2 CRM, Cụm 4 AI Voice, Cụm 7 Lead Gen.
- **Trần bài/ngày và khung giờ:** `[ĐIỀN]`. Ví dụ: tối đa 3 bài/ngày, 10:00, 14:00, 18:00 giờ site.

## 2. Bộ vai trò bài (họ)

Dùng 9 họ ở `references/cluster-roles.md` (hoặc bản đã chỉnh của bạn). Mỗi bài đúng một mã, ghi ở đầu ô "Vai trò" trong dấu huyền.

## 3. Bảng cụm (mỗi cụm một mục)

### Cụm `[ĐIỀN: số]`: `[ĐIỀN: tên cụm]`, `[ĐIỀN: N]` bài

- **Pillar:** `[ĐIỀN: slug]` (`#[ĐIỀN: post id]`), `[ĐIỀN: số chữ]` chữ.
- **Hub phụ (nếu có):** `[ĐIỀN]`.
- **Ưu tiên:** `[ĐIỀN: có/không gắn sản phẩm]`.

| Vai trò | Bài | Focus keyword | Funnel | Trạng thái |
|---|---|---|---|---|
| `pillar` **Pillar** | [`[ĐIỀN: tiêu đề]`](`[ĐIỀN: URL]`) | `[ĐIỀN: keyword]` | Discovery/TOF | `[ĐIỀN: ✅ Published ngày = #id, số chữ, density, số bảng, số ảnh, category. Link lên/ra những bài nào. Inbound: đã thêm từ ...]` |
| `how-to` | `[ĐIỀN]` | `[ĐIỀN]` | Consideration/MOF | `[ĐIỀN: ⏰ Scheduled ngày giờ = #id ...]` |
| `news-support` | `[ĐIỀN]` | `[ĐIỀN]` | Post-purchase/support | `[ĐIỀN]` |

**Ví dụ (một dòng thật, rút gọn):**

| Vai trò | Bài | Focus keyword | Funnel | Trạng thái |
|---|---|---|---|---|
| `how-to` Wave 1 | [Real Estate Marketing Plan: Template and Budget](https://infina.ai/news/real-estate-marketing-plan/) | `real estate marketing plan` | Consideration/MOF | ✅ Published 12/10 = #1843, 1.784 từ, density 0,56%, 4 bảng + 4 ảnh AI, category Real Estate Marketing (392). Link lên pillar #1825, sang #1853. Inbound: đã thêm từ pillar #1825 (15/10) |

Quy ước cột Trạng thái (giữ cho script và người đọc nhất quán): `✅ Published <ngày giờ> = #<id>` hoặc `⏰ Scheduled <ngày giờ> = #<id>`,
tiếp theo là số chữ, density, số bảng, số ảnh, category, **link đi** (lên pillar, sang bài nào) và **inbound** (đã/chưa có). Bài nào chưa có
inbound thì ghi rõ `Chưa có inbound` để ngày sau không quên làm bước 6.5.

## 4. Cannibalization: lịch sử audit

| Ngày | Cặp bài nghi trùng | Quyết định | Kết quả |
|---|---|---|---|
| `[ĐIỀN]` | `[ĐIỀN: bài A vs bài B]` | `[merge / internal-link / giữ nguyên]` | `[ĐIỀN]` |

## 5. Bị loại khỏi plan (không dùng)

| Chủ đề | Lý do loại |
|---|---|
| `[ĐIỀN]` | `[ĐIỀN: trùng cụm khác, rủi ro bản quyền, volume quá thấp...]` |

## 6. Việc còn lại

1. `[ĐIỀN: việc đang chờ, ví dụ: inbound pass cho wave 3 sau ngày publish]`
