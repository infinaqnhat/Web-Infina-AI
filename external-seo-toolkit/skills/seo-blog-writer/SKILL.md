---
name: seo-blog-writer
description: Viết bài blog chuẩn Rank Math SEO cho site WordPress, đăng qua kết nối WordPress
  MCP. Dùng skill này bất cứ khi nào người dùng yêu cầu viết bài blog, bài tin tức, bài review,
  bài so sánh sản phẩm, hoặc bất kỳ nội dung nào sẽ đăng lên blog site, kể cả khi họ chỉ nói
  "viết bài" hoặc "viết tin" mà không nhắc rõ SEO. Cũng dùng khi người dùng hỏi cách tối ưu Rank
  Math, sửa lỗi SEO cơ bản/bổ sung/khả năng đọc, hoặc cách cấu trúc bài để đạt điểm Rank Math cao.
---

# SEO Blog Writer

Skill viết bài blog, tối ưu sẵn theo checklist thật của Rank Math SEO (rút ra từ testing thực
tế trên 1 site production cụ thể trước đó, không phải suy đoán lý thuyết).

**Trước khi dùng skill này cho site mới**: điền vào các mục `[ĐIỀN: ...]` bên dưới cho khớp với
site/brand thật, đặc biệt phần "Bối cảnh site" và tông giọng viết. Xem `README.md` ở thư mục gốc
để biết cách setup đầy đủ.

## Bối cảnh site (điền khi setup cho site mới)

- Tên site/brand: `[ĐIỀN: tên site]`
- Domain: `[ĐIỀN: https://vidu.com/]`
- Ngách sản phẩm/nội dung: `[ĐIỀN: ví dụ "đồ chơi mô hình, hobby"]`
- Blog nằm ở subfolder hay subdomain: `[ĐIỀN, ảnh hưởng cách viết internal link]`
- Tông giọng: `[ĐIỀN: ví dụ trang trọng/thân thiện/hài hước..., mặc định dùng văn phong tự
  nhiên trung tính nếu chưa xác định rõ]`

## Quy tắc bất di bất dịch

- **Không dùng dấu gạch ngang dài (—)** trong bất kỳ đâu của bài viết. Thay bằng dấu phẩy, ngoặc
  đơn, hoặc tách thành 2 câu.
- Văn phong tự nhiên, không nhồi nhét từ khóa gượng ép.
- **Ưu tiên heading dạng câu hỏi khi hợp lý với nội dung** (vd "X có đáng mua không", "X là gì",
  "Vì sao X..."), phản ánh đúng cách người đọc thật gõ tìm kiếm hoặc hỏi AI (ChatGPT, Google AI
  Overview), thay vì heading "sáng tạo" mơ hồ. Không ép mọi heading thành câu hỏi nếu nghe
  gượng, chỉ áp dụng khi tự nhiên.
- Nếu blog nằm ở **subfolder** (`domain.com/blog/...`), mọi internal link nội bộ dùng đường dẫn
  tương đối kiểu `/ten-bai-viet/`. Nếu là subdomain riêng, dùng URL đầy đủ.
- **Không tự chế internal link.** Chỉ chèn internal link trỏ về bài khác trên site nếu đã xác
  minh URL đó tồn tại thật, ví dụ do người dùng cung cấp trực tiếp, hoặc Claude tự kiểm tra bằng
  web_fetch và thấy trang tồn tại (không phải trang 404). Tuyệt đối không đoán slug rồi viết
  link như thể nó có thật, kể cả khi đường dẫn nghe hợp lý. Nếu không xác minh được, bỏ qua phần
  internal link trong bài, hoặc ghi chú bằng chữ thường dạng gợi ý chủ đề liên quan (không phải
  link bấm được) để người dùng tự thêm link thật sau.
- **Canh ảnh cân đối trong bài, không dồn cục.** Nhiều theme WordPress tự hiển thị ảnh đại diện
  (featured image) ngay đầu bài, phía trên toàn bộ nội dung. Vì vậy:
  - Không chèn ảnh đầu tiên trong nội dung ngay sau đoạn mở bài, vì sẽ nằm sát ngay dưới ảnh đại
    diện, nhìn dồn cục 2 ảnh liền nhau. Đặt ảnh đầu tiên trong content xuống dưới 1 chút, gần 1
    heading/đoạn nội dung cụ thể mà nó minh họa.
  - Nếu bài có từ 2 ảnh trở lên trong content, dàn đều theo chiều dài bài (mỗi ảnh cách nhau ít
    nhất 1-2 section/heading), không đặt 2 ảnh liền kề nhau trong cùng 1 đoạn hoặc 2 đoạn sát
    nhau.
  - Trước khi chèn ảnh thứ 2 trở đi vào 1 bài đã có sẵn ảnh khác (đại diện hoặc trong content),
    kiểm tra trùng ảnh bằng `check_image_similarity.py` (trong skill `post-refresh`) trước khi
    upload, vì nhiều nguồn báo hay dùng chung đúng 1 tấm key art/press photo.
  - **Lỗi hay lặp lại, luôn tự kiểm tra**: khi gọi tool tạo/sửa bài với cả `image_url` (ảnh đại
    diện) VÀ có ảnh trong `content`, PHẢI so sánh URL ảnh đầu tiên trong content với `image_url`
    trước khi gọi tool. Nếu trùng URL hoặc nghi ngờ cùng 1 ảnh, chạy `check_image_similarity.py`
    để xác nhận, không được để ảnh đại diện xuất hiện lại y hệt ngay đầu content.

## Bước 1: Xác định từ khóa chính

Trước khi viết, chốt **1 từ khóa chính** duy nhất:
- 2-4 từ, khớp đúng search intent của bài (không quá dài để nhồi tự nhiên vào câu được)
- Nếu người dùng chưa cho từ khóa, tự đề xuất 1 cụm dựa trên chủ đề bài, giải thích ngắn gọn lý
  do chọn

## Bước 1.5: Check SERP thật trước khi viết (bắt buộc)

Sau khi chốt từ khóa chính, web_search đúng cụm từ khóa đó, đọc top 5-10 kết quả Google. 1 lần
search này trả lời cả 2 câu hỏi dưới, không tách thành 2 bước riêng:

1. **Search intent thật là gì** (đối chiếu bảng dưới, đáng tin hơn suy đoán từ cách viết
   keyword):

| Loại intent | Định dạng đang rank trên SERP | Hướng viết phù hợp |
|---|---|---|
| Informational | Guide, "X là gì", bài giải thích | Guide/hướng dẫn, answer capsule trả lời trực tiếp |
| Transactional | Trang sản phẩm, review có giá/mua ở đâu | Review có CTA, thông số + giá cụ thể |
| Commercial | Bảng so sánh, "nên mua X hay Y" | Bảng so sánh là phần bắt buộc, không chỉ "nếu phù hợp" |
| Navigational | Trang chính thức 1 brand/site cụ thể | Không viết bài mới nhắm keyword này, đổi biến thể khác |

   Nếu top SERP toàn dạng khác hẳn hướng định viết ban đầu (vd định viết guide nhưng top toàn
   trang bán hàng), đổi hướng bài hoặc đổi biến thể keyword cho khớp, không viết ngược lại SERP.
   Lưu ý: nếu từ khóa dự định dùng là 1 từ chung chung có nhiều nghĩa khác nhau (tên trùng với
   khái niệm/sản phẩm/thuật ngữ khác không liên quan), kiểm tra kỹ SERP có thực sự nói về đúng
   chủ đề bài không, nếu bị lấn át bởi nghĩa khác, đổi sang biến thể cụ thể hơn (thêm tên
   brand/loại sản phẩm) để khớp đúng intent.

2. **Có bị trùng (cannibalize) với bài đã có trên site không**: so top 10 SERP của từ khóa mới
   với từ khóa của bài gần nghĩa đã có trong `used-keywords.md` (nếu nghi ngờ trùng chủ đề). Nếu
   **≥3-4 URL trùng nhau** giữa 2 kết quả tìm kiếm, đó là tín hiệu Google coi 2 keyword cùng 1
   intent, nên **mở rộng bài cũ** (qua skill `post-refresh`) thay vì viết bài mới, tránh
   cannibalize. Nếu không đủ 3-4 URL trùng, viết bài mới là hợp lý.

Bỏ qua bước này CHỈ khi từ khóa quá mới/quá ngách để có SERP ý nghĩa (vd tin cộng đồng vừa xảy
ra, chưa ai viết), ghi rõ lý do bỏ qua trong phần bàn giao ở Bước 4.

## Bước 2: Viết theo cấu trúc chuẩn

```
# [Tiêu đề chứa từ khóa chính NGUYÊN CỤM, LIỀN NHAU, ở đầu câu. Có số (năm/con số) và 1 power word nếu hợp lý. Độ dài 50-60 ký tự]

*Meta description: [chứa từ khóa chính nguyên cụm trong câu đầu tiên, dưới 160 ký tự]*

---

[Mở bài 2-3 câu ngắn, chèn nguyên cụm từ khóa chính trong 1-2 câu đầu]

## [Heading 2 dạng câu hỏi, phản ánh đúng cách người đọc thật sự gõ tìm kiếm, chứa từ khóa chính hoặc biến thể gần đúng]
[Đoạn "answer capsule": 40-60 từ đầu tiên trả lời TRỰC TIẾP câu hỏi ở heading, có số liệu/tên riêng cụ thể, không mở đầu vòng vo. Đây là đoạn dễ được AI Overview/ChatGPT trích dẫn nhất khi người đọc tìm qua AI thay vì search truyền thống. Sau đó mới viết tiếp phần còn lại của đoạn (không quá 120 từ tổng). Có ít nhất 1 external link (dofollow) trỏ ra nguồn uy tín]

## [Heading 2 khác — phân tích/bối cảnh]
[Đoạn ngắn, dùng từ nối chuyển ý tự nhiên. Không để 2 câu liên tiếp bắt đầu cùng 1 từ]

## [Heading 2 — bảng so sánh nếu phù hợp với chủ đề, BẮT BUỘC nếu Bước 1.5 xác định intent là Commercial]
| Tiêu chí | A | B |
|---|---|---|

## [Heading 2 — ý nghĩa/tác động với người đọc]
- Gạch đầu dòng để dễ scan
- Đoạn ngắn

## [Heading 2 kết bài — nhắc lại từ khóa chính]
[CTA theo dõi blog / để lại bình luận / xem thêm bài liên quan]

---

*Nguồn tham khảo: [external link]. [Chỉ thêm "Xem thêm: [internal link]" nếu đã xác minh link đó tồn tại thật, không tự chế]*
```

**Độ dài tối thiểu 600 từ** (ngưỡng "Content Length" thật của Rank Math). Ngoài mức sàn này,
chọn độ dài mục tiêu theo loại bài (xem `references/content-planning-framework.md` mục 4 để
biết nguồn và giới hạn độ tin cậy của các con số dưới, chỉ là range tham khảo từ tổng hợp ngành,
KHÔNG phải target bắt buộc, word count không phải ranking factor):

| Loại bài | Độ dài mục tiêu |
|---|---|
| Tin tức | 700-900 từ |
| "X là gì" / định nghĩa | 800-1.500 từ |
| Review 1 sản phẩm | 1.500-2.000 từ |
| So sánh 2+ sản phẩm / guide mua hàng | 2.000-3.000 từ |

Coi độ dài là kết quả của việc viết đủ sâu cho đúng loại bài và intent (xác định ở Bước 1.5),
không phải mục tiêu ép đạt cho đủ số từ.

## Bước 3: Tự kiểm tra trước khi giao bài (checklist Rank Math)

Chạy qua toàn bộ danh sách này trước khi coi bài là hoàn chỉnh. Đây là checklist thật từ Rank
Math, chia làm 4 nhóm:

### Nhóm SEO cơ bản (bắt buộc đạt cả 5)
- [ ] Từ khóa chính xuất hiện trong tiêu đề SEO, nguyên cụm liền nhau
- [ ] Từ khóa chính xuất hiện trong meta description
- [ ] Từ khóa chính xuất hiện trong URL/slug (đề xuất slug ngắn, chỉ chứa từ khóa, bỏ hết từ nối)
- [ ] Từ khóa chính xuất hiện trong 10% nội dung đầu tiên (câu đầu/câu thứ 2 của bài)
- [ ] Nội dung tối thiểu 600 từ

### Nhóm Bổ sung
- [ ] Từ khóa chính xuất hiện trong ít nhất 1 heading phụ (H2/H3)
- [ ] Có ít nhất 1 ảnh, và nhắc người dùng cần điền alt text chứa từ khóa chính cho ảnh khi
  upload (Claude không tự set alt text được nếu chỉ tạo file markdown, phải nhắc người dùng làm
  thủ công trong WordPress nếu không đi qua tool tự động)
- [ ] Mật độ từ khóa nằm trong khoảng 0.5%-2.5% (không quá thưa, không nhồi nhét)
- [ ] Có ít nhất 1 external link (dofollow) trỏ ra nguồn uy tín, nhắc người dùng kiểm tra link
  không bị tự động gắn nofollow khi dán vào WordPress
- [ ] Nếu có internal link trỏ về bài khác trên site, link đó phải đã được xác minh tồn tại thật
  (không tự chế slug). Nếu không xác minh được link nào, được phép bỏ qua mục này, không được
  tự bịa link cho đủ checklist

### Nhóm Khả năng đọc tiêu đề
- [ ] Từ khóa chính nằm ở đầu tiêu đề SEO
- [ ] Tiêu đề chứa 1 con số (năm, thứ hạng, số lượng...) nếu hợp lý với chủ đề
- [ ] Tiêu đề có ít nhất 1 power word

### Nhóm Khả năng đọc nội dung (bổ sung GEO, không thuộc Rank Math nhưng nên giữ)
- [ ] Có ít nhất 1 "answer capsule" (40-60 từ trả lời trực tiếp 1 câu hỏi ngay đầu 1 đoạn, có
  số liệu/tên riêng cụ thể), tăng khả năng được AI Overview/ChatGPT trích dẫn
- [ ] Ít nhất 1-2 heading phụ dạng câu hỏi nếu hợp lý với nội dung
- [ ] Có ít nhất 1 ảnh hoặc video trong bài (nhắc người dùng tự chèn nếu Claude không tìm được
  ảnh phù hợp)
- [ ] Nếu có từ 1 ảnh trở lên trong content (chưa tính ảnh đại diện), ảnh không đặt ngay sau đoạn
  mở bài và không dồn cục gần nhau, xem quy tắc "Canh ảnh cân đối trong bài" ở trên
- [ ] Đoạn văn ngắn, không quá 120 từ/đoạn
- [ ] Không có 2 câu liên tiếp bắt đầu bằng cùng 1 từ
- [ ] Dùng từ nối/chuyển ý đều đặn giữa các đoạn
- [ ] Heading phân bố đều, không để 1 khối văn bản dài không chia nhỏ

## Bước 4: Bàn giao

Sau khi viết xong, LUÔN kèm theo phần tóm tắt ngắn gọn:
1. Từ khóa chính đã chọn (và lý do nếu Claude tự đề xuất)
2. Slug đề xuất cho URL
3. Danh sách các việc người dùng cần tự làm thủ công trong WordPress (alt text ảnh, kiểm tra
   dofollow link, thêm internal link thật nếu bài chưa có link nào được xác minh) nếu không đi
   qua tool đăng bài tự động

**Cảnh báo bắt buộc nếu người dùng sẽ tự copy-paste bài này vào WordPress (không qua tool đăng
bài tự động):** luôn dặn rõ dán đúng **bản markdown thô** ở trên, KHÔNG bao giờ copy trực tiếp từ
vùng hiển thị đã render của cửa sổ chat (bôi đen đoạn text đang hiển thị đẹp rồi dán). Đã kiểm
chứng thực tế nhiều lần trên 1 site production: copy kiểu đó mang theo `class` CSS riêng của giao
diện chat (dạng `font-claude-response-body break-words whitespace-normal leading-[1.7]`), biến mọi
heading thành `<strong>` in đậm giả bên trong `<p>` thay vì `<h2>` thật — Rank Math/Google không
nhận diện được là heading, lỗi này từng tồn tại nhiều tháng trên cả bài top traffic mà không ai
phát hiện vì trang hiển thị vẫn trông bình thường (xem thêm trong `post-refresh-playbook.md`). Nếu
tự Claude gọi tool đăng bài, phải tự convert markdown sang HTML sạch trước khi gọi (`## Heading` →
`<h2>Heading</h2>` thật, không có class thừa) — không bao giờ truyền thẳng bản markdown hay bản
HTML có dính class lạ vào field content của tool.

## Khi người dùng gửi ảnh chụp màn hình Rank Math báo lỗi

Đọc đúng tên lỗi trong ảnh, đối chiếu với checklist ở Bước 3 để xác định thuộc nhóm nào, rồi sửa
trực tiếp phần nội dung tương ứng. Không đoán mò lỗi ngoài những gì thấy trong ảnh.

## Ghi nhớ

Skill này được đúc kết từ việc test thực tế trên 1 site production khác trước đó, dựa trên ảnh
chụp checklist Rank Math thật, không phải tài liệu chính thức của Rank Math nên có thể không bao
quát 100% mọi trường hợp. Nếu người dùng gửi ảnh checklist mới có mục chưa được liệt kê ở đây,
học thêm mục đó và áp dụng, có thể đề xuất cập nhật lại skill này sau.

**Lưu ý về mật độ từ khóa 0.5-2.5%**: đây là chỉ số riêng của plugin Rank Math (kiểm tra literal
trên UI), không phải tín hiệu xếp hạng thật của thuật toán Google (Google hiện đánh giá theo
semantic relevance/entity salience nhiều hơn tần suất từ). Vẫn giữ nguyên rule này vì mục tiêu
là đạt điểm Rank Math cao, chỉ cần biết đây là 2 khái niệm khác nhau khi giải thích cho người
dùng.

**Về độ dài bài theo loại**: rule cũ kiểu "700-900 tin tức, dài hơn cho review/so sánh" nếu
không có căn cứ thì chỉ là ước lượng nội bộ, chưa verify bằng research thật. Bảng độ dài ở Bước 2
đã được verify qua research thật (Backlinko, Semrush 2024 Ranking Factors Study, Ahrefs, HubSpot,
phát ngôn chính thức Google/John Mueller), xem chi tiết và giới hạn độ tin cậy ở
`references/content-planning-framework.md` mục 4: word count KHÔNG phải ranking factor (Semrush
đo correlation chỉ 0.02), các range theo loại bài chỉ là tổng hợp thực tế ngành, dùng để tham
khảo chứ không ép đạt.
