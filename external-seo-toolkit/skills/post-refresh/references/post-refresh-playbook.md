# Post Refresh Playbook

Khung chẩn đoán để quyết định 1 bài đã publish trên site cần sửa gì, dựa trên dữ liệu GSC thật,
không phải suy diễn cảm tính. Đây là bản khung phương pháp gốc (đúc kết ban đầu từ 1 site khác),
khi dùng cho site mới nên tự bổ sung case thật của site đó vào cuối file này theo thời gian.

## Nguyên tắc gốc: rẽ nhánh theo triệu chứng, không chạy 5 bước tuần tự cứng

Nhìn 3 chỉ số GSC của trang (vị trí trung bình, CTR, impressions) trước, để biết nên bắt
đầu từ đâu. Chạy đủ 5 bước cho mọi trang là lãng phí thời gian, vấn đề thật thường chỉ nằm
ở 1-2 bước.

| Triệu chứng (đọc từ GSC) | Chẩn đoán khả năng cao nhất | Bắt đầu từ bước nào |
|---|---|---|
| Vị trí kém (>8-10), CTR đúng/gần mức kỳ vọng theo vị trí (xem bảng benchmark bên dưới), impressions thấp-vừa | Nội dung thiếu chiều sâu, thiếu thông tin mới, không đủ khớp search intent so với đối thủ đang đứng trên, HOẶC đơn giản là vị trí chưa đủ cao (cần internal link/backlink, không phải lỗi nội dung) | Bước 1 → 2 (SERP thật + search intent) trước; nếu nội dung đã tốt và đối thủ không có gì hơn, nghi ngờ vấn đề authority/internal link thay vì nội dung |
| CTR **thấp hơn rõ rệt** mức kỳ vọng theo vị trí (không phải chỉ "CTR số nhỏ", số nhỏ có thể là bình thường ở vị trí thấp), impressions cao (>150) | Title/meta description thật sự không đủ hấp dẫn để click, đây mới là dạng lãng phí traffic tiềm năng thật | Bước 3 (on-page title/meta) trước |
| Vị trí tốt, CTR tốt, nhưng impressions rất thấp (<20) dù bài không mới | Có thể không phải vấn đề nội dung, kiểm tra internal link trỏ vào trang, có nằm trong sitemap không, index status (dùng `inspect_url`) | Kiểm tra kỹ thuật (sitemap, internal link, index status) trước khi đụng vào nội dung |
| Vị trí dao động mạnh qua các tuần (so sánh 2 khoảng thời gian) | Google đang "phân vân" xếp hạng, dấu hiệu tốt để can thiệp, 1 update nhỏ có thể đẩy hẳn lên ổn định | Bước 4-5 sau khi đã xử lý xong nhánh chính ở trên |

Một trang có thể rơi vào nhiều hàng cùng lúc, xử lý theo thứ tự trên (từ nội dung → on-page
→ kỹ thuật → theo dõi), không cần làm hết mọi hàng nếu hàng đầu đã giải thích đủ vấn đề.

### Bắt buộc: so CTR với benchmark theo vị trí trước khi kết luận "CTR thấp"

Sai lầm dễ mắc: nhìn 1 con số CTR trông có vẻ thấp rồi vội kết luận "title/meta kém", trong khi
CTR kỳ vọng ở vị trí đó (ví dụ trang 2 Google, vị trí ~10) vốn dĩ chỉ tầm 2-2.5%, tức bài đang
đúng chuẩn, không hề bất thường. Luôn tra bảng benchmark dưới đây trước, chỉ kết luận "title/meta
có vấn đề" khi CTR thực tế **thấp hơn rõ rệt** (dưới khoảng 50-60%) so với mức kỳ vọng của đúng
vị trí đó, không chỉ dựa vào con số CTR tuyệt đối trông có vẻ thấp.

| Vị trí trung bình | CTR kỳ vọng (tham khảo, dao động theo ngành) |
|---|---|
| 1 | ~28-30% |
| 2 | ~15% |
| 3 | ~11% |
| 4 | ~8% |
| 5 | ~7% |
| 6 | ~5% |
| 7 | ~4% |
| 8 | ~3.5% |
| 9 | ~3% |
| 10 | ~2.5% |
| 11-20 (trang 2) | ~1-2% |

CTR **cao hơn hẳn** benchmark là dấu hiệu tốt, không cần sửa gì, thường do có rich snippet
(giá, đánh giá sao) hoặc title/meta đã rất hiệu quả, nên dùng làm mẫu tham khảo khi viết
title/meta cho bài khác cùng site.

## 5 bước check gốc (dùng làm thân bài sau khi đã chọn nhánh ưu tiên ở trên)

### Lưu ý kỹ thuật: fetch trang đối thủ có thể bị chặn ngẫu nhiên theo domain

Một số domain đối thủ có thể bị lớp agent proxy của môi trường chặn ở tầng CONNECT (502 policy
denial), không phải do "Network access" của environment bị tắt hoàn toàn. Đây thường không phải
chặn toàn bộ web, chỉ chặn theo domain cụ thể. Nếu 1 domain bị chặn, thử domain đối thủ khác
trong danh sách kết quả tìm kiếm thay vì báo lỗi và dừng lại. Một số URL lấy từ kết quả tìm kiếm
cũng có thể đã lỗi thời (404) hoặc trỏ tới domain đã hết hạn/parked, kiểm tra `<title>` trang
fetch được có hợp lý không trước khi dùng làm dữ liệu so sánh.

### Lưu ý kỹ thuật: WebSearch không phản ánh đúng SERP theo vùng/quốc gia cụ thể

Nhiều tool WebSearch chỉ hoạt động theo vùng US mặc định, không có tham số geo/region để đổi
sang quốc gia khác một cách chính xác. Nếu site nhắm thị trường ngoài Mỹ (ví dụ Việt Nam), kết
quả trả về có thể là SERP kiểu Mỹ, không phải Google theo domain/vùng thật của thị trường đó,
dù GSC báo trang đang có vị trí tốt cho query liên quan tại thị trường đó. Cách giảm sai lệch:
truyền tham số lọc domain theo quốc gia nếu tool hỗ trợ, nhưng đây vẫn chỉ là lọc domain, KHÔNG
mô phỏng lại đúng thứ hạng/rich snippet/cá nhân hóa theo vùng thật. Khi cần xác nhận vị trí SERP
chính xác cho 1 thị trường cụ thể, cách đáng tin nhất là nhờ người dùng tự search trực tiếp trên
trình duyệt của họ (ẩn danh, từ đúng vùng địa lý) và gửi lại kết quả/ảnh chụp, không tự tin dùng
WebSearch để kết luận thứ hạng theo vùng.

### Bước 1 — Xem lại SERP thật cho đúng query đang ăn traffic

Lấy top query của trang (`gsc_client.py queries --page ...`), search trực tiếp query đó
trên Google (ẩn danh), xem 3-5 kết quả đầu đang đứng trên mình có gì mà bài mình không có,
cấu trúc bài, thông tin họ đề cập (giá, specs, so sánh, review), định dạng (bảng, video,
FAQ). Đây là bước quan trọng nhất khi vấn đề là vị trí kém, vì nó cho biết Google đang thấy
tin gì "đủ tốt" hơn bài mình.

### Bước 2 — Đối chiếu search intent với nội dung hiện có

Đọc lại bài đang có, tự hỏi: người gõ query đó thực sự muốn gì (mua ở đâu/giá bao nhiêu,
review có đáng mua không, so sánh với sản phẩm khác, thông tin kỹ thuật)? Nếu bài hiện tại lệch
hướng hoặc thiếu thông tin mới (thông tin đã có tin chính thức nhưng bài còn ghi "chưa
công bố") thì đó là gap cần bổ sung trước tiên. Không tự bịa thông tin không kiểm chứng được,
nếu cần số liệu mới, tra cứu nguồn thật trước khi viết vào bài.

### Bước 3 — Kiểm tra tín hiệu on-page cơ bản

Title, meta description, URL, heading đầu bài có chứa đúng cụm từ khóa chính tự nhiên
không, mật độ từ khóa trong nội dung có đủ không (theo checklist Rank Math trong skill
`seo-blog-writer`). Khi CTR thấp dù vị trí tốt, đây là bước ưu tiên: so sánh
title/meta hiện tại với các bài cùng site đang có CTR cao để tìm pattern (có số cụ thể, có
câu hỏi trực tiếp kiểu "có đáng mua không", có mốc thời gian/giá trong title).

### Bước 4 — Kiểm tra độ mới của thông tin

Bài viết từ lúc nào, có thông tin nào đã lỗi thời (giá cũ, tình trạng hàng cũ, tin đồn nay đã
có xác nhận chính thức) cần cập nhật không, nội dung "còn sống" thường được Google ưu ái hơn
nội dung đứng yên lâu.

### Bước 5 — Nhìn thêm dữ liệu GSC theo thời gian

So sánh 2 khoảng thời gian gần nhau (vd 30 ngày gần nhất vs 30 ngày trước đó) để biết vị trí
đang ổn định hay dao động mạnh. Dao động mạnh quanh top 5-10 là dấu hiệu Google đang "phân
vân" xếp hạng bài, 1 cú update nhỏ có thể đẩy hẳn lên.

## Lưu ý khi viết title/meta mới để tăng CTR

Khi nghi ngờ 1 trang có vấn đề title/meta thật sự (đã qua bước so benchmark ở trên và xác nhận
CTR thấp hơn rõ rệt), ưu tiên thêm 1 trong các yếu tố: giá/số liệu cụ thể, năm, câu hỏi trực tiếp
đúng intent, hoặc điểm khác biệt nổi bật nhất của sản phẩm/chủ đề, miễn nội dung bài thực sự trả
lời được điều title hứa hẹn, không giật tít sai nội dung. Tìm 1-2 bài trên chính site đang có CTR
cao hơn hẳn benchmark để làm mẫu tham khảo về pattern title/meta hiệu quả, thay vì đoán mò.

**Cảnh báo dễ mắc lỗi**: đừng vội kết luận "title dạng review/dạng câu hỏi là nguyên nhân CTR
thấp" chỉ vì nhìn qua thấy CTR có số nhỏ. Luôn so với benchmark theo đúng vị trí của bài đó
trước (xem bảng ở trên), rất nhiều trường hợp CTR "trông thấp" thực ra khớp đúng benchmark cho
vị trí hiện tại, không phải lỗi title/meta thật.

## Luôn check cấu trúc heading thật (không chỉ đọc text) cho bài cũ

Bài viết cũ (viết trước khi có skill `seo-blog-writer` chuẩn hiện tại, hoặc import từ nguồn
khác) có thể trông đầy đủ nội dung khi đọc qua text đã strip HTML, nhưng thực chất toàn bộ
"heading" chỉ là chữ in đậm (`<strong>`) trong thẻ `<p>`, không có thẻ `<h2>` thật nào,
Rank Math/Google sẽ không nhận diện được đây là heading dù nội dung không thiếu gì. **Luôn fetch
raw `content.rendered` qua `wp-json/wp/v2/posts` và nhìn trực tiếp có thẻ `<h2>` thật không**,
đừng chỉ strip HTML rồi đọc text khi chẩn đoán bài cũ, vì cách đó sẽ bỏ sót lỗi cấu trúc dạng
này. Tương tự, kiểm tra luôn có external link dofollow thật không (không chỉ tin bài "chắc có"
vì nội dung nhắc đến nguồn), và có vi phạm quy tắc viết nào của skill viết bài không (bài cũ hay
dính lỗi vì viết trước khi 1 số quy tắc được thêm vào skill).

### Dấu hiệu nhận diện nguồn gốc lỗi: nội dung dán trực tiếp từ giao diện chat claude.ai

Đã gặp lặp lại nhiều lần trên 1 site (kể cả bài đang là top traffic của toàn site, tồn tại lỗi
suốt nhiều tháng vì không ai đọc raw HTML, chỉ nhìn trang hiển thị bình thường qua mắt thường).
Dấu hiệu nhận diện chắc chắn: các thẻ `<p>`/`<ul>`/`<li>`/`<table>` còn nguyên `class` dạng
`font-claude-response-body break-words whitespace-normal leading-[1.7]` hoặc các class Tailwind
tương tự (`[li_&]:mb-0`, `border-border-300/60`...) — đây là class CSS riêng của giao diện
claude.ai, không phải class do theme WordPress sinh ra. Thường đi kèm 1 loạt thẻ `<hr>` trang trí
ngăn cách giữa các "section" (thay cho heading thật). Khi thấy 2 dấu hiệu này, gần như chắc chắn
nội dung được soạn trực tiếp trong cửa sổ chat rồi copy-paste thẳng vào ô nội dung WordPress, bỏ
qua hẳn bước convert Markdown → HTML sạch.

**Cách sửa (giữ nguyên nội dung, chỉ sửa cấu trúc):**
1. Convert từng đoạn `<p class="..."><strong>Tiêu đề</strong></p>` thành `<h2>Tiêu đề</h2>` thật
   (bỏ số thứ tự "1. 2. 3." nếu có ở đầu, giữ nguyên phần chữ). Với mục dạng câu hỏi/đáp kiểu FAQ
   ở cuối bài, dùng `<h3>` cho từng câu hỏi thay vì `<h2>`.
2. Xóa toàn bộ thẻ `<hr class="...">` trang trí — không còn cần thiết khi đã có heading thật ngăn
   cách.
3. Xóa attribute `class="..."` chứa các class Tailwind trên mọi thẻ còn lại (`<p>`, `<ul>`, `<li>`,
   `<table>`, `<div>`, `<blockquote>`, `<th>`, `<td>`...) — giữ nguyên thẻ, chỉ bỏ class rác.
4. Nhân tiện xóa `srcset`/`sizes` dài không cần thiết trên thẻ `<img>` nếu có (thường cũng đi kèm
   khi ảnh được chèn qua cùng luồng dán từ chat).
5. Verify lại bằng cách `curl` trang live, đếm số `<h2>`/`<h3>` thật xuất hiện, đối chiếu đúng số
   lượng section mong đợi.

## Ghi chú case thật của site này (tự bổ sung theo thời gian)

Thêm vào đây các case thật đã gặp khi refresh bài trên site cụ thể của bạn (tên bài, chẩn đoán
ban đầu, chẩn đoán đúng sau khi kiểm tra kỹ, kết quả sau khi sửa), để tránh lặp lại nhận định sai
đã từng mắc, tương tự cách file gốc của site ToyHunter từng ghi lại 2 case thật giúp phát hiện
lỗi "CTR trông thấp nhưng thực ra đúng benchmark" và lỗi "heading giả dạng `<strong>`".
