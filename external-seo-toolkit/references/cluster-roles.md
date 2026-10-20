# Bộ vai trò bài trong cụm (9 họ)

Rút ra từ site gốc ngày 2026-10-12 sau khi cột "Vai trò" trong bảng cụm có tới 67 giá trị khác nhau, không script nào đọc được.
Gom về 9 họ: đủ hẹp để phân biệt cách link của từng loại bài, đủ rộng để bài mới luôn gán được.

⚠️ **Bộ này gom từ dữ liệu của một site cụ thể.** Dùng làm điểm xuất phát, đổi tên hoặc bỏ họ nào site bạn không có
(ví dụ `buying-guide` nếu không bán gì). Điều quan trọng là **mỗi bài đúng một mã**, không phải 9 mã này.

| Mã | Tên | Định nghĩa | Funnel hay gặp | Cách link |
| --- | --- | --- | --- | --- |
| `pillar` | Pillar / hub | Trang tổng quan của cả cụm, hoặc sub-hub nhận link từ nhiều bài cùng chủ đề (IDX hub, roundup hub). | Discovery/TOF | Nhận link từ mọi bài cluster. Đích của link lên pillar. Anchor đa dạng >= 70%. |
| `review` | Review / roundup | Bài đánh giá, xếp hạng, liệt kê, ví dụ: review brand, review niche, listicle, examples/inspiration. | Evaluation/MOF | Link lên pillar 1 lần, ngang 2-3 bài cùng cụm. Đích thường xuyên của link từ News. |
| `compare` | So sánh / quyết định | So sánh 2 phương án, thay thế, hoặc quyết định build vs buy. | Evaluation/MOF, Decision/BOF | Link lên pillar 1 lần. Không lặp keyword với bài review cùng chủ đề. |
| `buying-guide` | Buying guide | Hướng dẫn chọn mua, thang tiêu chí, checklist trước khi mua. | Decision/BOF | Link lên pillar 1 lần. Hợp để đặt link tới money page. |
| `explainer` | Định nghĩa / giải thích | Bài 'X là gì', định nghĩa chung hoặc theo ngách, giải thích pain-point. | Discovery/TOF | Đích tốt cho link từ bài News cần dẫn người đọc về nền tảng khái niệm. |
| `how-to` | How-to / thiết lập | Hướng dẫn làm, thiết lập kỹ thuật, kênh cụ thể, support có bước. | Post-purchase/how-to, Decision/BOF | Link lên pillar 1 lần, ngang tới bài review/compare liên quan. |
| `niche` | Sub-topic / ngách | Chủ đề con hoặc ngách đối tượng của cụm (pipeline, marketing, open house, home valuation...). | Evaluation/MOF, Post-purchase | Có pillar riêng nhỏ hơn khi cụm lớn. Cần giữ góc riêng, không trùng keyword. |
| `news-support` | News hỗ trợ | Bài viết từ tin tức, có FOCUS_KW long-tail riêng, hỗ trợ pillar bằng góc thời sự. | Post-purchase/support | Link lên pillar 1 lần, ngang 2-3 bài cùng cụm. Bước 6.5 phải gắn link ngược từ 1 bài cùng cụm. |
| `bridge` | Bridge / cross-link | Bài nối hai cụm, trỏ sang cụm khác theo thiết kế. | Evaluation/MOF | Là ngoại lệ có chủ đích của quy tắc 'trỏ pillar nhà >= 50%'. Ghi rõ cụm đích. |

## Quy tắc dùng

1. **Bài mới khai họ** ở bước chọn pillar và keyword chính (Bước 4 của `pillar-cluster-writer`). Bài lấy từ tin tức luôn là `news-support`.
2. **Một bài, một họ.** Bài vừa là review vừa là niche thì chọn họ quyết định cách link của nó, ghi phần còn lại thành nhãn phụ sau mã.
3. **Họ không phải căn cứ SEO.** Google không đọc nhãn này. Nó chỉ để biên tập, và để script phân loại khi đo (đếm số cluster của một cụm, chọn donor).
4. **Thành viên cụm lấy từ bảng cụm do người quyết định**, không suy ra từ link graph (xem `internal-linking-guide.md` mục 2).
5. Ghi mã ở đầu ô "Vai trò" trong content plan dưới dạng mã trong dấu huyền, ví dụ `how-to`, nhãn cũ để phía sau làm ghi chú.
