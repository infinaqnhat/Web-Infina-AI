---
name: pillar-cluster-writer
description: >
  Lên plan và viết trọn bộ bài blog SEO affiliate theo mô hình pillar +
  cluster cho 1 trang sản phẩm/dịch vụ cầu nối trên site WordPress (có nút
  mua hàng/affiliate ra ngoài). Gồm: tra volume từ khóa thật, kiểm tra
  cannibalize qua log + sitemap, lên plan pillar+cluster cho người dùng
  duyệt, viết từng bài theo chuẩn Rank Math (dùng skill `seo-blog-writer`),
  chèn video YouTube/ảnh AI minh họa đúng chỗ, internal link 2 chiều
  pillar-cluster-money page, lên lịch đăng theo trần bài/ngày, và log
  keyword vào Git. Dùng khi người dùng nói "làm SEO affiliate cho sản phẩm
  X", "lên plan pillar cluster cho trang sản phẩm", "viết bộ bài blog hỗ
  trợ cho sản phẩm đang bán", hoặc sau khi đã tạo 1 trang sản phẩm/dịch vụ
  mới và muốn viết nội dung blog đi kèm để tránh rủi ro thin affiliate/
  doorway page.
---

# Pillar + Cluster Writer

Skill đúc kết từ quy trình đã chạy thật khi xây bộ pillar + cluster cho 1 sản phẩm affiliate trên 1
site production, sau đó generic hoá cho site này. Nếu site có 1 file guideline riêng về on-page SEO
(meta, schema, internal link, `rel="sponsored nofollow"`, EEAT...), đọc lại file đó song song với
skill này — skill này tập trung *quy trình*, không thay thế phần quy tắc kỹ thuật chi tiết.

**Trước khi dùng skill này cho site mới**: điền vào các mục `[ĐIỀN: ...]` bên dưới cho khớp với
site/brand thật. Xem `README.md` ở thư mục gốc toolkit này để biết cách setup đầy đủ.

## Bối cảnh site (điền khi setup cho site mới)

- Tên site/brand: `[ĐIỀN: tên site]`
- Domain: `[ĐIỀN: https://vidu.com/]`
- Nền tảng bán hàng: `[ĐIỀN: WooCommerce/Shopify/khác, có bán trực tiếp hay chỉ affiliate ra sàn
  khác kiểu Shopee/Amazon]`
- File guideline on-page riêng (nếu có): `[ĐIỀN: tên file, hoặc "chưa có"]`
- File content plan chung: `[ĐIỀN: tên file, ví dụ content-plan.md]`
- File log keyword đã dùng: `[ĐIỀN: tên file, ví dụ content-logs/used-keywords.md]`

## Vì sao skill này tồn tại

1 trang sản phẩm/dịch vụ cầu nối (chỉ có ảnh + mô tả + nút mua/affiliate) đứng đơn lẻ rất dễ bị
Google xếp vào diện **"thin affiliate site"/"doorway page"**. Cách phòng tránh là gắn trang sản
phẩm đó vào 1 cụm chủ đề (pillar + cluster), link 2 chiều giữa các bài.

## Điều kiện cần trước khi chạy

- File keyword nghiên cứu của site (CSV/Excel), dùng để tra volume từ khóa thật.
- File log keyword đã dùng (xem "Bối cảnh site" ở trên), dùng để check cannibalize.
- Kết nối MCP WordPress (`wp-mcp-server-snippet.php` ở thư mục gốc toolkit này) để dùng
  `create_draft_post`/`update_post`/`list_posts`, đọc biến môi trường `SEO_MCP_KEY` (xem
  `secrets/README.md`).
- **Nếu cần đụng tới trang sản phẩm (money page)** — thêm mục "Xem thêm", tạo redirect cloak
  affiliate, set FAQ schema cho trang sản phẩm — `wp-mcp-server-snippet.php` đi kèm toolkit này
  (từ 2026-09-15) đã có đủ tool quản lý sản phẩm WooCommerce (`create_product`/`update_product`/
  `delete_product`/`get_product`/`list_products`, `create_product_variation`/
  `update_product_variation`/`list_product_variations`, `set_affiliate_redirect`/
  `delete_affiliate_redirect`/`list_affiliate_redirects`, `set_product_faq`/`delete_product_faq`)
  bên cạnh tool bài viết. Yêu cầu site đích chạy WooCommerce; nền tảng bán hàng khác (Shopify,
  custom cart...) vẫn cần tự viết route REST tương ứng, snippet hiện tại chỉ hỗ trợ WooCommerce.
- Nếu muốn generate ảnh AI minh họa: biến môi trường `GEMINI_API_KEY` (xem Bước 5.2).

## Quy trình

### Bước 1: Xác định sản phẩm/money page và chủ đề

Xác nhận rõ với người dùng: sản phẩm/dịch vụ nào (ID, slug, tên), và chủ đề cụm sẽ xoay quanh
(thường là chính tên sản phẩm hoặc dòng sản phẩm đó).

**Trước khi đi tiếp, mở file content plan chung của site** — tra xem đã có cụm/nhánh pillar+cluster
nào cùng chủ đề/dòng sản phẩm chưa. Nếu có, ưu tiên **thêm money page mới vào nhánh đã có** (thêm
vào bài so sánh, cập nhật pillar link tới) thay vì tự tạo pillar+cluster mới từ đầu — tránh trùng
lặp nội dung. Chỉ tạo nhánh/cụm hoàn toàn mới nếu chủ đề thực sự khác biệt, không có nhánh nào
phù hợp.

**Lưu ý:** file content plan chỉ để quyết định "nhập nhánh cũ hay tạo nhánh mới", KHÔNG thay thế
bước check cannibalize keyword thật ở Bước 3 — bảng trong file có thể lỗi thời, vẫn phải check đủ
cả file log keyword lẫn sitemap thật trên site trước khi chốt bất kỳ focus keyword nào.

### Bước 2: Tra volume từ khóa thật

Xem chi tiết cách đọc 2 loại nguồn (bucket-tier vs số chính xác) trong
`../../references/content-strategy-framework.md` Bước 1. Tóm tắt: dùng nguồn export mới nhất làm
chính, nguồn cũ (nếu có số chính xác) chỉ dùng phá thế hòa khi 2 keyword rơi cùng bucket.

Ghi lại volume (kèm ghi rõ là "tier" hay "số chính xác") và % thay đổi cho từng ứng viên keyword,
dùng làm dữ liệu chọn keyword ở bước sau — không tự đoán volume. **Nếu nguồn keyword là dạng
Explorer Access (chưa chạy Ads đủ lâu), không tin cột % thay đổi (3-month/YoY)** — đã kiểm chứng
thực tế trên 1 site các giá trị này gần như luôn là bội số tròn của 900%, chỉ là artifact của việc
nhảy bucket, không phải xu hướng tìm kiếm thật. Kiểm tra lại hiện tượng này trên site mới trước khi
tin theo.

### Bước 3: Kiểm tra cannibalize (bắt buộc đủ nguồn, không chỉ log)

Với mỗi keyword ứng viên:
1. Grep file log keyword đã dùng, tìm keyword đó và các biến thể gần (không chỉ khớp chính xác).
2. **Đối chiếu thêm qua sitemap thật trên site** (`curl https://<domain>/post-sitemap.xml`, lọc
   `<loc>` có chứa từ khóa/slug liên quan) — không chỉ tin riêng log, vì log ghi thủ công có thể
   thiếu sót hoặc từng bị mất dữ liệu.
3. **Check thêm file content plan chung, vì đây là keyword đã "có chủ" dù có thể CHƯA đăng nên
   chưa vào log:** nhánh/cụm khác trong file có thể đã lên plan trùng keyword.
   Lý do bắt buộc thêm 2 nguồn này: file log chỉ ghi nhận **sau khi đăng thành công**, nên 1
   keyword đã "đặt chỗ" trong plan nhưng chưa viết sẽ không xuất hiện ở đó — nếu chỉ check log +
   sitemap sẽ không phát hiện được, dẫn tới 2 kế hoạch cùng nhắm 1 keyword mà không ai biết cho
   tới khi cả 2 cùng viết xong.
4. Loại các keyword đã trùng bài/plan khác chủ đề. Giữ lại/note các bài/plan đã có sẵn liên quan để
   cân nhắc link chéo thay vì viết đè.

### Bước 4: Lên plan pillar + cluster, trình bày cho người dùng duyệt trước khi viết

Thiết kế theo khung chuẩn:
- **1 bài pillar**: bao quát chủ đề lớn, dùng keyword có volume cao nhất và rộng nhất trong nhóm.
- **2-4 bài cluster**, mỗi bài 1 vai trò khác nhau theo funnel (xem
  `../../references/content-strategy-framework.md` Bước 2):
  - So sánh (Evaluation/MOF) — ví dụ "X chính hãng vs rep"
  - Review chuyên sâu (Evaluation/MOF)
  - Buying guide (Decision/BOF)
  - Support/how-to, ví dụ hướng dẫn kết nối/sử dụng (Discovery/Post-purchase) — loại bài này
    thường có nhiều long-tail volume nhỏ gộp lại, đáng làm 1 bài riêng thay vì bỏ qua
- Mỗi bài: vai trò, tiêu đề dự kiến, keyword chính + volume/YoY, funnel stage.
- Vẽ rõ luồng internal link dự kiến (pillar ↔ từng cluster, cluster ↔ money page, money page →
  pillar/cluster liên quan nhất).

**Check rủi ro bản quyền/nội dung cấm nếu chủ đề đụng phần mềm/công cụ nhạy cảm** (emulator, mod,
bẻ khóa/jailbreak, ROM/firmware, tải file, "hack" thiết bị, hoặc bất kỳ công cụ/dịch vụ nào có tiền
lệ bị kiện/DMCA) — xem chi tiết quy trình 4 bước trong `../../references/content-strategy-framework.md`
Bước 1.5. Tóm tắt: web search tình trạng pháp lý hiện tại của công cụ trước khi chốt keyword, không
chỉ tin vào volume/tên nghe hợp pháp. Nếu công cụ đã bị chủ sở hữu bản quyền gốc ép đóng cửa/kiện
thắng, KHÔNG lên plan bài dạng "hướng dẫn cài đặt/sử dụng" cho công cụ đó — đổi góc tin tức/giải
thích hoặc bỏ khỏi plan.

**Trình bày bảng plan này cho người dùng duyệt trước khi viết bài thật** — đây là bước tốn công
viết nhiều bài, không tự ý viết hết rồi mới hỏi.

### Bước 5: Viết từng bài theo chuẩn skill `seo-blog-writer`

Áp dụng đúng cấu trúc và checklist Rank Math của skill `seo-blog-writer` (H1 chứa keyword đầu câu,
meta description, H2 rải keyword/biến thể, đoạn <120 từ, ít nhất 1 external link dofollow tới
nguồn uy tín thật đã verify, bảng so sánh nếu hợp lý, 600+ từ). Chốt slug tường minh cho từng bài
(không để tool tự sinh) để kiểm soát được internal link ngay từ đầu, vì các bài trong cùng cụm sẽ
link chéo nhau.

Thứ tự viết: pillar trước (nội dung link tới cluster có thể để placeholder rồi bổ sung ở Bước 6),
rồi từng cluster (link về pillar ngay vì pillar đã tồn tại).

### Bước 5.1: Chèn video YouTube minh họa — đánh giá từng đoạn nội dung, không chèn tràn lan

Với MỌI bài trong cụm (không riêng bài support/how-to), khi viết xong từng đoạn/H2, tự hỏi: đoạn
này có phải dạng nội dung **video minh họa sẽ giúp người đọc hiểu nhanh hơn text** không (thao tác
từng bước, demo sản phẩm, so sánh trực quan)? Nếu có:

1. Web search tìm video YouTube thật, khớp đúng nội dung đoạn đó (không phải khớp chung chung cả
   bài — ví dụ bài có cả đoạn "kết nối với thiết bị A", "kết nối với thiết bị B", "kết nối với
   thiết bị C" thì tìm **video riêng biệt cho từng đoạn**, không dùng 1 video chung cho tất cả —
   đã có 1 case thật dùng nhầm 1 video chung, phải sửa lại sau khi bị phát hiện).
2. **Verify video tồn tại thật và đúng nội dung** qua YouTube oEmbed API trước khi chèn, không tự
   đoán video ID:
   ```bash
   curl -sS "https://www.youtube.com/oembed?url=https://www.youtube.com/watch?v=<VIDEO_ID>&format=json"
   ```
   Đọc `title` trả về, đối chiếu có khớp đúng nội dung đoạn đang viết không. Nếu API trả "Not
   Found", video không tồn tại/đã gỡ, đổi video khác.
3. Chèn bằng cách dán URL YouTube trần (`https://www.youtube.com/watch?v=<ID>`) trên 1 dòng/đoạn
   `<p>` riêng, đặt **ngay sau đoạn/H2 nội dung liên quan** (không dồn hết video lên đầu bài).
   WordPress tự nhận diện qua oEmbed. Không dùng thẻ `<iframe>` viết tay — đã kiểm chứng thực tế bị
   `wp_kses` strip mất khi lưu qua REST API, khiến khung video hiện trống dù tool báo thành công.
4. Nếu không tìm được video nào thật sự khớp đúng nội dung đoạn đó, bỏ qua, không chèn video gượng
   ép chỉ để có video.
5. **Sau khi bài publish thật** (không phải lúc còn draft/future), luôn `curl` lại trang live tìm
   `youtube.com/embed/` để xác nhận từng video đã render đúng, đúng số lượng — không chỉ tin tool
   báo cập nhật thành công.

### Bước 5.2: Generate ảnh AI minh họa — chỉ khi không có video/ảnh thật phù hợp

Nếu 1 đoạn nội dung cần minh họa trực quan nhưng KHÔNG phải dạng hướng dẫn thao tác (không hợp
video) và không có ảnh thật/ảnh sản phẩm sẵn có phù hợp, generate ảnh AI. Đúc kết từ 1 đợt viết
cụm thật, luôn đi theo thứ tự ưu tiên sau, KHÔNG generate thẳng bằng text prompt thuần trừ khi đã
thử hết các lựa chọn có ảnh tham chiếu.

**1. Ảnh minh họa cho chính sản phẩm site đang bán (bài về money page đó)**

Dùng ảnh thật của sản phẩm (từ gallery money page) làm ảnh tham chiếu (reference), KHÔNG generate
ảnh chay từ text. Gemini image model hỗ trợ nhận nhiều ảnh input (image-to-image), độ chính xác
cao hơn hẳn so với chỉ mô tả bằng chữ:

```bash
python3 scripts/generate_image_ref.py output.png "<prompt tiếng Anh, mô tả chi tiết bối cảnh muốn tạo, không chữ trong ảnh, luôn ghi rõ 'matching the reference image exactly' để model bám sát>" ref-san-pham-1.jpg [ref-san-pham-2.jpg ...]
```

Có thể truyền nhiều ảnh reference cùng lúc (ví dụ bài so sánh 2 sản phẩm, truyền cả 2 ảnh sản phẩm
vào 1 lần gọi để ra ảnh có cả 2 trong cùng khung hình).

**Khi truyền 2+ ảnh reference của 2 sản phẩm khác nhau (bài so sánh), phải gọi rõ tên từng ảnh
trong prompt và mô tả đặc điểm riêng biệt của mỗi cái** (ví dụ "reference image 1 is Product A, a
solid black item... reference image 2 is Product B, a white item... the two products must look
clearly different from each other, matching their own reference image"). Đã kiểm chứng thực tế: nếu
chỉ ghi chung chung "using the two products in the reference images", model có xu hướng làm 2 sản
phẩm nhìn giống hệt nhau (cùng 1 màu/dáng), mất luôn điểm khác biệt chính mà bài so sánh cần thể
hiện. Luôn kiểm tra lại ảnh ra có phân biệt đúng 2 sản phẩm không trước khi gửi duyệt.

**2. Ảnh minh họa khái niệm chung/loại sản phẩm mà site KHÔNG bán** (ví dụ 1 loại sản phẩm khác
được nhắc tới để so sánh/bối cảnh, không phải sản phẩm đang bán)

**Bắt buộc web search tìm 1 ảnh thật của loại sản phẩm đó trước, tải về làm reference, rồi mới
generate** — tuyệt đối không generate thẳng bằng text prompt thuần cho trường hợp này. Lý do: đã
kiểm chứng thực tế rằng generate chỉ bằng text mô tả có thể ra kết quả **sai cấu trúc thật của sản
phẩm** (ví dụ 1 thiết bị gồm 2 nửa tách rời bị vẽ dính liền thành 1 khối) dù mô tả bằng lời nghe có
vẻ đúng. Ảnh sai cấu trúc này nhìn "giả"/"AI" rất rõ và có thể khiến người đọc hiểu sai về cách sản
phẩm đó hoạt động.

Quy trình: web search tìm ảnh sản phẩm/bài review thật của loại sản phẩm đó → lấy URL ảnh → tải về
bằng `curl` → dùng làm reference cho `generate_image_ref.py` giống bước 1 ở trên, chỉ khác là ghi
rõ trong prompt đây là minh họa khái niệm chung ("generic/conceptual illustration of this product
type, not a specific real branded product, no visible brand names or logos") để không vô tình tái
tạo đúng logo/thương hiệu của ảnh reference.

**3. Chỉ dùng `scripts/generate_image.py` (text prompt thuần, không có ảnh reference) khi đã thử
web search ở bước 2 mà không tìm được ảnh thật nào phù hợp.** Đây là phương án cuối, chấp nhận rủi
ro sai cấu trúc cao hơn.

**Chuẩn phong cách ảnh (điều chỉnh theo brand/ngách của từng site):** ví dụ gợi ý — ảnh chụp cận
cảnh góc nhìn thứ nhất, bối cảnh đời thường hơi bừa làm mờ nhòe phía sau, ánh sáng tự nhiên, khung
hình hơi lệch tự nhiên (không bố cục hoàn hảo kiểu ảnh stock/cinematic), tránh ánh sáng studio hoàn
hảo quá mức vì dễ bị nhận xét "nhìn AI lắm". Luôn generate 1 ảnh thử, gửi cho người dùng duyệt
trước khi generate hàng loạt cho nhiều bài, vì đây là khoản tốn công/API call.

Dùng biến môi trường `GEMINI_API_KEY`, model `gemini-3.1-flash-lite-image` (đổi tên model nếu bản
mới hơn đã ra mắt). Sau khi generate và được duyệt, upload qua `upload_media` rồi chèn `<img>` vào
đúng vị trí đoạn nội dung liên quan trong `content` khi gọi `update_post`. Ảnh đại diện (featured
image) của bài cũng nên generate theo đúng quy trình và chuẩn phong cách này (dùng `image_url` của
`update_post`/`create_draft_post` trỏ về ảnh vừa upload) thay vì để trống hoặc dùng ảnh og:image
không liên quan.

**Nếu bài đang viết cần ảnh minh họa cho 1 tin/nguồn cụ thể** (không phải sản phẩm site đang bán)
và nguồn gốc không có `og:image`/`twitter:image` dùng được: đừng bỏ cuộc ngay, web search tìm 1
ảnh thật khác phù hợp (trang sản phẩm/thông cáo chính hãng của thứ đang nói tới, hoặc nguồn uy tín
khác đưa cùng tin có ảnh rõ ràng hơn) trước khi coi là "không tìm được ảnh". Chỉ khi đã thử cả
nguồn gốc lẫn web search mà vẫn không ra ảnh phù hợp mới giữ bài ở draft chờ người dùng tự thêm.

**Nguyên tắc bắt buộc khi dùng ảnh AI:**
- Không dùng để tạo ảnh trông giống ảnh thật của 1 sản phẩm/thiết bị cụ thể theo cách đánh lừa
  người đọc — nhưng khi ảnh reference CHÍNH LÀ ảnh sản phẩm site đang bán (trường hợp 1), việc bám
  sát hình dáng thật là mục tiêu đúng, không phải rủi ro.
- Luôn nêu rõ trong báo cáo cuối đây là ảnh AI-generated, không phải ảnh thật.
- Nếu bài đang viết là về chính sản phẩm site đang bán, ưu tiên dùng ảnh THẬT của sản phẩm đó làm
  reference (trường hợp 1 ở trên) thay vì generate chay, để ảnh minh họa vẫn đúng đúng model đang
  bán dù là ảnh dàn dựng.

### Bước 5.3: Convert HTML trước khi gọi tool đăng bài (bắt buộc, không được bỏ qua)

`create_draft_post`/`update_post` nhận nội dung ở field `content` dưới dạng HTML thô, không tự
render markdown. Trước khi gọi tool cho mỗi bài (pillar lẫn từng cluster), convert bản markdown
vừa viết ở Bước 5 sang HTML thật:

- `# Tiêu đề` không đưa vào content, dùng làm giá trị `title` của tool
- `## Heading` thành `<h2>Heading</h2>` **thật** (không phải `<p><strong>Heading</strong></p>`)
- Đoạn văn thường thành `<p>...</p>`
- `[chữ](/slug/)` thành `<a href="https://<domain>/slug/">chữ</a>` (đã verify tồn tại thật ở Bước
  6), tự thêm domain đầy đủ vì content đăng qua API cần link tuyệt đối
- Bảng markdown thành `<table><tr><th>...</th></tr>...</table>`
- Gạch đầu dòng thành `<ul><li>...</li></ul>`
- Phần "Meta description" ở đầu bài không đưa vào content, dùng làm giá trị `seo_description`

**Tuyệt đối không copy nguyên văn bản markdown/text đã viết ở Bước 5 rồi dán thẳng vào field
`content`, và càng không bao giờ lấy nội dung từ vùng hiển thị đã render của cửa sổ chat (copy
đoạn text đang hiển thị đẹp mắt).** Đã kiểm chứng thực tế trên 1 site production: làm vậy khiến
mọi heading biến thành `<strong>` in đậm giả trong `<p>` kèm class CSS rác của giao diện chat (dạng
`font-claude-response-body break-words whitespace-normal leading-[1.7]`), Rank Math/Google không
nhận diện được heading nào cả — lỗi này từng tồn tại nhiều tháng trên cả bài top traffic của site
mà không ai phát hiện vì trang hiển thị vẫn trông bình thường (xem chi tiết trong
`post-refresh-playbook.md`). Sau khi convert xong, tự rà lại 1 lượt: đếm số `<h2>` thật trong
content có đúng số heading dự kiến không, trước khi gọi tool.

### Bước 6: Hoàn thiện internal link 2 chiều

1. Sau khi tất cả cluster đã tạo (có slug thật), quay lại bài pillar (`update_post`), bổ sung link
   tới tất cả cluster nếu lúc viết đầu chưa đủ.
2. Mỗi cluster nên link về pillar + 1-2 cluster liên quan nhất (không cần mesh đầy đủ tất cả với
   tất cả).
3. Cập nhật money page (trang sản phẩm): lấy nội dung mô tả đầy đủ hiện tại qua REST API công khai
   (với WooCommerce, KHÔNG dùng field rút gọn nếu tool chỉ trả `short_description`, phải lấy đủ
   `content`/`description` đầy đủ trước):
   ```bash
   curl -sS "https://<domain>/wp-json/wp/v2/product/<ID>?_fields=content"
   ```
   Lấy nội dung đầy đủ, nối thêm 1 đoạn "Xem thêm" trỏ về pillar (+ 1 cluster liên quan nhất, ví
   dụ bài so sánh), rồi gọi tool update sản phẩm với field mô tả = nội dung cũ + đoạn mới (không
   được chỉ gửi đoạn mới, nếu tool ghi đè toàn bộ mô tả chứ không tự append).
4. Verify lại bằng `curl` trang live tìm đúng đoạn "Xem thêm" và các link mới.

### Bước 6.1: CTA mua hàng trong bài cluster (nếu có) nên dùng link cloak, không link affiliate trực tiếp

Bài trong cụm (đặc biệt buying guide, review — nhóm Decision/BOF) đôi khi hợp lý để chèn thêm 1
câu CTA dẫn thẳng tới hành động mua, không chỉ dẫn về money page bằng link nội bộ WordPress. Nếu
làm vậy:

1. **Không bao giờ chèn link affiliate trực tiếp** (ví dụ link rút gọn của sàn thương mại điện
   tử) vào nội dung bài blog nếu site có sẵn cơ chế cloak riêng (redirect 301 nội bộ dạng
   `<domain>/go/<slug>`) — giữ link equity, dễ quản lý hàng loạt khi link đổi.
2. Nếu redirect cloak cho sản phẩm đó chưa tồn tại, tạo trước bằng tool quản lý redirect (nếu site
   đã có, xem "Điều kiện cần trước khi chạy") rồi mới dùng trong bài, không tự chèn link affiliate
   tạm.
3. Ưu tiên mặc định vẫn là **link nội bộ về money page** (ví dụ `/shop/<slug-san-pham>/`) thay vì
   link cloak thẳng ra sàn ngay trong bài cluster — cluster là support/evaluation content nuôi
   money page bằng link nội bộ, không nên tự ý biến mọi cluster thành nơi bán hàng trực tiếp. Chỉ
   dùng link cloak khi có lý do rõ ràng (ví dụ buying guide muốn CTA nhanh ngay dưới bảng giá) và
   cân nhắc kỹ, không mặc định làm ở mọi bài.

### Bước 6.2: Nếu money page có phần FAQ trong mô tả, đảm bảo có FAQ schema thật (không chỉ text)

Khi rà lại money page, nếu mô tả sản phẩm đã có/được bổ sung phần "Câu hỏi thường gặp" nhưng chưa
có `FAQPage` schema đi kèm:

1. Nhiều plugin SEO bản free (ví dụ Rank Math) không hỗ trợ mẫu FAQ trong Schema Generator (khoá
   PRO) — nếu site dùng plugin loại này, không mất công vào wp-admin tìm cách bật.
2. Dùng tool quản lý FAQ schema riêng nếu site đã có (xem "Điều kiện cần trước khi chạy"). Lưu ý
   kỹ thuật đã gặp thật ở 1 site: `update_post_meta()` của WordPress tự gọi `wp_unslash()` trước
   khi lưu vào DB, có thể làm hỏng ký tự escape unicode nếu code lưu JSON không dùng
   `JSON_UNESCAPED_UNICODE` — kiểm tra lại nếu thấy ký tự có dấu bị lưu sai thành mã unicode rác.
3. Dùng đúng nguyên văn câu hỏi/đáp đã hiển thị thật trong mô tả sản phẩm, verify lại bằng cách
   tìm `"@type":"FAQPage"` trên trang live sau khi set.

### Bước 7: Lên lịch đăng theo trần bài/ngày

1. Gọi `list_posts` với `status: ["future","publish"]` để biết ngày nào đã kín theo trần hiện tại
   (điền số trần bài/ngày đang áp dụng của site vào file quy tắc riêng nếu có, đừng hardcode số
   trong skill này).
2. Xếp các bài trong cụm vào những ngày còn trống đầu tiên, tối đa theo trần, không cần xếp liền
   kề (đây là nội dung evergreen, không có ngoại lệ tin nóng như bài tin tức).
3. Set `slug` tường minh khi tạo bài (không để tool tự sinh) để chủ động kiểm soát internal link.
4. Gọi `update_post` với `status: "future"` và `publish_date` tương ứng cho từng bài.

### Bước 8: Log keyword và commit

Thêm 1 dòng mới đầu bảng file log keyword đã dùng cho MỖI bài (pillar lẫn cluster), theo đúng
format `| ID | keyword | chắc chắn | tiêu đề | future/draft/publish | ngày giờ |` (xem
`../../references/used-keywords-template.md` nếu site chưa có file log riêng). Commit + push ngay
trong cùng phiên, không dồn lại — tránh rủi ro mất dữ liệu nếu môi trường làm việc bị cấp lại giữa
chừng.

### Bước 8.5: Cập nhật file tracking content plan chung

Ngay sau Bước 8 (log keyword), cập nhật luôn file content plan chung của site trong cùng lần
commit:
- Nếu vừa tạo nhánh/cụm hoàn toàn mới: thêm 1 mục "Nhánh"/"Cụm" mới vào đúng vị trí trong cây chủ
  đề (không thêm rời rạc không rõ quan hệ với các cụm đã có), đúng format các nhánh đã có (Money
  page / Pillar / Cluster..., kèm ID, tiêu đề, focus keyword, status).
- Nếu vừa thêm money page mới vào nhánh đã có (theo gợi ý ở Bước 1): thêm 1 dòng "Money page" mới
  vào đúng bảng nhánh đó, không tạo mục mới.
- Commit + push cùng lúc với Bước 8 (không tách riêng lần commit khác).

### Bước 9: Báo cáo kết quả

Tổng hợp cho người dùng: bảng plan đã duyệt, danh sách bài đã tạo (ID, vai trò, keyword, lịch
đăng), danh sách video/ảnh đã chèn kèm vị trí, các link "Xem thêm" đã thêm vào money page, và nhắc
việc còn cần làm thủ công (preview nội dung trong wp-admin, verify embed sau khi publish thật).

## Phạm vi KHÔNG thuộc skill này

- Tạo/sửa sản phẩm trên nền tảng bán hàng (dùng skill tạo sản phẩm riêng của site, nếu có).
- Rà tin tức hàng ngày (nếu site có skill riêng cho việc đó).
- Viết 1 bài blog đơn lẻ không thuộc mô hình pillar+cluster (dùng thẳng skill `seo-blog-writer`).
