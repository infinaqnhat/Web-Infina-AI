# Bộ vai trò bài trong cụm (9 họ)

Chốt ngày 2026-10-12. Mỗi bài trong bảng cụm của `content-plan.md` phải mang đúng **một** trong 9 họ
dưới đây, ghi ở đầu ô "Vai trò" dưới dạng mã trong dấu huyền, ví dụ `review`. Nhãn cũ vẫn được giữ
phía sau mã làm ghi chú (niche, brand, HUB...), nên không mất thông tin.

**Vì sao 9 họ:** trước đó cột này có 67 giá trị khác nhau, không máy nào đọc được, trong khi guide chỉ
nêu 4 kiểu cluster chuẩn. 9 họ gom từ chính các nhãn đang dùng, đủ hẹp để phân biệt cách link của
từng loại bài, đủ rộng để bài mới luôn gán được.

⚠️ **Đây là bộ do tôi gom từ dữ liệu, bạn đã chốt "9 họ" nhưng chưa duyệt từng nhãn.** Nếu thấy một
nhãn xếp sai họ, sửa mã trong `content-plan.md` rồi cập nhật bảng ánh xạ ở cuối file này.

## Chín họ

| Mã | Tên | Định nghĩa | Funnel hay gặp | Cách link | Số bài hiện có |
|---|---|---|---|---|---|
| `pillar` | Pillar / hub | Trang tổng quan của cả cụm, hoặc sub-hub nhận link từ nhiều bài cùng chủ đề (IDX hub, roundup hub). | Discovery/TOF | Nhận link từ mọi bài cluster. Đích của link lên pillar. Anchor đa dạng >= 70%. | 13 |
| `review` | Review / roundup | Bài đánh giá, xếp hạng, liệt kê, ví dụ: review brand, review niche, listicle, examples/inspiration. | Evaluation/MOF | Link lên pillar 1 lần, ngang 2-3 bài cùng cụm. Đích thường xuyên của link từ News. | 17 |
| `compare` | So sánh / quyết định | So sánh 2 phương án, thay thế, hoặc quyết định build vs buy. | Evaluation/MOF, Decision/BOF | Link lên pillar 1 lần. Không lặp keyword với bài review cùng chủ đề. | 8 |
| `buying-guide` | Buying guide | Hướng dẫn chọn mua, thang tiêu chí, checklist trước khi mua. | Decision/BOF | Link lên pillar 1 lần. Hợp để đặt link tới money page. | 5 |
| `explainer` | Định nghĩa / giải thích | Bài 'X là gì', định nghĩa chung hoặc theo ngách, giải thích pain-point. | Discovery/TOF | Đích tốt cho link từ bài News cần dẫn người đọc về nền tảng khái niệm. | 7 |
| `how-to` | How-to / thiết lập | Hướng dẫn làm, thiết lập kỹ thuật, kênh cụ thể, support có bước. | Post-purchase/how-to, Decision/BOF | Link lên pillar 1 lần, ngang tới bài review/compare liên quan. | 4 |
| `niche` | Sub-topic / ngách | Chủ đề con hoặc ngách đối tượng của cụm (pipeline, marketing, open house, home valuation...). | Evaluation/MOF, Post-purchase | Có pillar riêng nhỏ hơn khi cụm lớn. Cần giữ góc riêng, không trùng keyword. | 7 |
| `news-support` | News hỗ trợ | Bài viết từ tin tức, có FOCUS_KW long-tail riêng, hỗ trợ pillar bằng góc thời sự. | Post-purchase/support | Link lên pillar 1 lần, ngang 2-3 bài cùng cụm. Bước 6.5 phải gắn link ngược từ 1 bài cùng cụm. | 23 |
| `bridge` | Bridge / cross-link | Bài nối hai cụm, trỏ sang cụm khác theo thiết kế. | Evaluation/MOF | Là ngoại lệ có chủ đích của quy tắc 'trỏ pillar nhà >= 50%'. Ghi rõ cụm đích. | 3 |

Tổng **87** dòng có URL trong `content-plan.md` đã được gán họ, không còn dòng nào thiếu.

## Quy tắc dùng

1. **Bài mới phải khai họ** ở Bước 4 của skill, cùng lúc chọn pillar và FOCUS_KW. Bài News luôn là
   `news-support`.
2. **Một bài, một họ.** Bài vừa là review vừa là niche thì chọn họ quyết định cách link của nó, ghi
   phần còn lại vào nhãn cũ phía sau mã.
3. **Họ không phải căn cứ SEO.** Google không đọc nhãn này. Nó chỉ để biên tập và để script phân loại
   khi đo (ví dụ đếm số cluster của một cụm, chọn donor).
4. **Thành viên cụm vẫn lấy từ bảng cụm**, không suy ra từ link graph (xem guide mục 2).

## Bảng ánh xạ nhãn cũ sang họ

### `pillar`

- Pillar
- Pillar (HUB)
- Pillar (nhẹ)
- Pillar = refresh #147
- Pillar A
- Pillar B
- Pillar chính (ĐÃ ĐỔI 01/10)
- Pillar nhẹ  Infina AI
- Review/list (HUB)
- Review/list (roundup, HUB)
- Định nghĩa (HUB)

### `review`

- Evaluation/MOF (cluster hợp lệ)
- Examples/inspiration
- Listicle chiến lược (TOF)  Infina AI
- Review (brand cụ thể)  Infina AI
- Review (niche: broker)
- Review (niche: free)
- Review (niche: investor)
- Review (niche: luxury)
- Review (niche: realtor)
- Review (niche: solo agent)
- Review/list
- Review/list (niche: broker)
- Review/list (niche: free)
- Review/list (niche: teams)
- Review/list (phát hiện thêm 01/10)

### `compare`

- Decision (build vs buy)
- So sánh
- So sánh (MOF)  Infina AI
- So sánh/thay thế

### `buying-guide`

- Buying guide
- Buying guide (BOF)
- Buying guide (agency)
- Buying guide/how-to

### `explainer`

- Giải thích/pain-point = refresh #223
- Định nghĩa
- Định nghĩa (beginner)
- Định nghĩa (broker)
- Định nghĩa (chung)
- Định nghĩa (khác góc)
- Định nghĩa (niche RE)

### `how-to`

- How-to (kỹ thuật)
- Kênh cụ thể
- Support/how-to → bắc cầu Cụm 7

### `niche`

- Niche: agent chung
- Niche: home valuation
- Niche: open house
- Niche: seller chung
- Sub-topic: marketing (strategy)
- Sub-topic: marketing (định nghĩa)
- Sub-topic: pipeline

### `news-support`

- Hỗ trợ
- Hỗ trợ (News)

### `bridge`

- Bridge → Cụm 3
- Cross-link → Cụm 7  Infina AI

