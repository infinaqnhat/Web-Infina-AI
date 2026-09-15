---
name: post-refresh
description: >
  Rà soát và tối ưu lại các bài đã publish trên site dựa trên dữ liệu Google Search
  Console thật (vị trí, CTR, impressions theo trang/theo query), chẩn đoán đúng nguyên nhân
  (nội dung thiếu thông tin mới, title/meta kém CTR, hay vấn đề kỹ thuật như index/internal
  link) theo playbook đã đúc kết từ các case thật, rồi đề xuất và áp dụng update qua WordPress
  MCP. Dùng skill này khi người dùng nói "check bài nào cần update", "tối ưu lại bài cũ",
  "xem trang nào có traffic/lỗi trên search console", "sửa title cho tăng CTR", hoặc muốn biết
  bài nào đang mất traffic tiềm năng cần refresh. Khác với skill viết bài mới, skill này chỉ
  làm việc với bài ĐÃ publish.
---

# Post Refresh

Skill nối 3 việc: kéo dữ liệu GSC thật cho site, chẩn đoán trang nào đáng refresh
và vì sao (theo `references/post-refresh-playbook.md`), rồi áp dụng update qua WordPress MCP
sau khi đã thống nhất với người dùng. Không tự ý sửa hàng loạt bài mà không có dữ liệu GSC hỗ
trợ, mọi đề xuất phải bắt nguồn từ số liệu thật, không suy đoán cảm tính.

## Điều kiện cần trước khi chạy

- Biến môi trường `SEO_GSC_SA_JSON`: chứa nguyên văn nội dung JSON của Google service
  account key có quyền đọc Search Console cho site (permission `Full` hoặc `Restricted` đều đọc
  được performance data). Nếu thiếu biến này trong session hiện tại, đọc trực tiếp file key đã
  lưu sẵn trong repo tại `secrets/gsc-service-account.json` (chỉ nếu repo là private và người
  dùng đã đồng ý lưu file này trong repo làm nguồn dự phòng) rồi export vào biến môi trường:
  ```bash
  export SEO_GSC_SA_JSON="$(python3 -c "import json;print(json.dumps(json.load(open('secrets/gsc-service-account.json'))))")"
  ```
  Chỉ khi file này cũng không có mới dừng lại và báo người dùng cách lấy key mới: tạo service
  account trên Google Cloud Console, cấp quyền cho email service account đó trong Search Console
  (Settings > Users and permissions > Add user), rồi đọc file JSON key gốc, nén thành 1 dòng
  bằng `python3 -c "import json;print(json.dumps(json.load(open('key.json'))))"`, set làm giá
  trị biến môi trường này trong cấu hình environment/session, hoặc gửi file key để lưu lại vào
  `secrets/gsc-service-account.json` trong repo.
- Biến môi trường `SEO_MCP_KEY`: secret key đã cấu hình trong `wp-mcp-server-snippet.php` trên
  site WordPress đích, dùng để gọi `update_post` khi áp dụng thay đổi.
- Site mặc định lấy qua biến `SEO_GSC_SITE_URL` (bắt buộc set, không có domain mặc định thật
  trong script này, vì mỗi lần setup cho site mới đều cần domain khác nhau).
- Script `scripts/gsc_client.py` cần thư viện `PyJWT` và `cryptography` (thường có sẵn trong
  môi trường Python chuẩn, kiểm tra nhanh bằng `python3 -c "import jwt, cryptography"` nếu
  không chắc).
- Biến môi trường `SEO_CLARITY_TOKEN` (tùy chọn, chỉ cần khi muốn xem thêm data hành vi
  người dùng từ Microsoft Clarity, bổ sung cho GSC chứ không thay thế): token dạng JWT của
  Clarity Data Export API cho site đích. Nếu thiếu biến này, script `clarity_client.py` tự
  đọc từ `secrets/clarity-token.txt` (đường dẫn tương đối, tìm từ thư mục làm việc hiện tại).
- Google Analytics 4 (bổ sung, không thay thế GSC): có thể dùng **chung key** `SEO_GSC_SA_JSON`
  ở trên nếu cùng 1 service account đã được add thủ công vào GA4 property của site (GA4 Admin >
  Account Access Management > thêm email service account, quyền Viewer trở lên), hoặc dùng key
  GA4 riêng nếu muốn tách quyền. Bắt buộc set biến `SEO_GA4_PROPERTY_ID` (số property GA4, xem
  trong GA4 Admin > Property Settings, không phải Measurement ID dạng G-XXXXXXX). Khác với
  Clarity (chỉ 1-3 ngày), GA4 Data API **không giới hạn khoảng thời gian**, dùng
  `scripts/ga4_client.py` khi cần traffic/pages/nguồn traffic theo bất kỳ khoảng ngày nào (không
  chỉ 28 ngày như GSC mặc định).

## Quy trình

### Bước 1: Kéo dữ liệu trang có traffic gần đây

```bash
python3 scripts/gsc_client.py pages --start <YYYY-MM-DD> --end <YYYY-MM-DD> --limit 25
```

Mặc định lấy 28-30 ngày gần nhất nếu người dùng không chỉ định khoảng thời gian khác, sort
theo `clicks` giảm dần. Nếu người dùng chỉ hỏi tổng quan ("xem trang nào có traffic gần đây"),
dừng ở đây và trình bày bảng kết quả, chưa cần chẩn đoán sâu.

Nếu người dùng muốn so sánh xu hướng (dao động vị trí), chạy thêm 1 lần nữa với khoảng thời
gian trước đó liền kề (vd 30 ngày trước khoảng đầu) để đối chiếu.

**Tìm nhanh "Striking Distance Keywords"** (trang vị trí 8-20, CTR thấp hơn benchmark theo vị
trí, xem `references/content-planning-framework.md` mục 0) thay vì tự tính tay từ kết quả
`pages`:
```bash
python3 scripts/gsc_client.py striking-distance --start <YYYY-MM-DD> --end <YYYY-MM-DD> --only-below-benchmark
```
Trả về danh sách đã sort giảm dần theo impressions, kèm `gap` (chênh lệch CTR thật so với
benchmark theo vị trí, âm nghĩa là dưới kỳ vọng). Đây thường là cách nhanh nhất để tìm ứng viên
refresh ở Bước 2, ưu tiên trang impressions cao nhất trong danh sách trả về mà **chưa có trong
`references/refresh-log.md` trong 2-3 tuần gần nhất** (xem quy tắc bỏ qua trang vừa sửa ở cuối
Bước 6).

**Bổ sung (tùy chọn) từ Google Analytics 4:** khi cần traffic/pageviews/nguồn traffic theo
khoảng thời gian bất kỳ (không giới hạn như GSC/Clarity), chạy:
```bash
python3 scripts/ga4_client.py traffic --start 7daysAgo --end today
python3 scripts/ga4_client.py pages --start 28daysAgo --end today --limit 20
python3 scripts/ga4_client.py sources --start 28daysAgo --end today --limit 20
python3 scripts/ga4_client.py page-sources --page "/duong-dan-bai/" --start 7daysAgo --end today
```
`--start`/`--end` nhận cả định dạng tuyệt đối (`YYYY-MM-DD`) lẫn tương đối kiểu GA4
(`7daysAgo`, `28daysAgo`, `today`, `yesterday`). Dữ liệu GA4 (pageviews, session, nguồn
traffic thật) khác về bản chất so với GSC (chỉ đo hành vi tìm kiếm/impressions trên Google) và
Clarity (hành vi UX như dead click/scroll), nên dùng bổ sung khi cần góc nhìn traffic tổng thể
hoặc theo nguồn (Facebook, direct, referral...), không dùng thay thế GSC khi đang chẩn đoán vấn
đề SEO/thứ hạng tìm kiếm.

**Bắt buộc chạy `page-sources` (không chỉ `sources` tổng) khi kết luận 1 trang cụ thể tăng/giảm
traffic vì nguồn nào.** `sources` tổng site dễ gây kết luận sai (trộn lẫn traffic của nhiều
trang khác nhau). Luôn so 2 khoảng thời gian liền kề (tuần này vs tuần trước) bằng
`page-sources` trước khi kết luận nguyên nhân tăng/giảm traffic của 1 trang cụ thể, `pagePath`
truyền vào phải khớp CHÍNH XÁC (bắt đầu và kết thúc bằng `/`, không phải domain đầy đủ).

**Bổ sung (tùy chọn) từ Microsoft Clarity:** nếu người dùng muốn xem thêm hành vi người dùng
thật (dead click, rage click, scroll depth, thiết bị/OS, trang phổ biến theo lượt xem thực tế,
tỷ lệ session bot) bên cạnh số liệu tìm kiếm từ GSC, chạy:
```bash
python3 scripts/clarity_client.py insights --days 3
```
**Giới hạn thật của Clarity Data Export API** (không phải lỗi script): tham số `--days` CHỈ
nhận 1, 2, hoặc 3, không có cách nào lấy xa hơn 3 ngày gần nhất qua API này. Nếu người dùng hỏi
số liệu dài hơn 3 ngày, báo rõ giới hạn này thay vì cố lấy hoặc suy diễn số liệu. Luôn để ý field
`totalBotSessionCount` trong response, tỷ lệ bot có thể khá cao, cần trừ hao khi diễn giải số
liệu traffic từ Clarity, khác với GSC vốn đã lọc bot.

### Bước 2: Chẩn đoán trang cần refresh

Đọc `references/post-refresh-playbook.md` TRƯỚC khi chẩn đoán. Với mỗi trang được chọn để
xem xét (theo yêu cầu người dùng, hoặc tự đề xuất 2-3 trang có dấu hiệu rõ nhất từ bảng kéo ở
Bước 1), tra bảng "rẽ nhánh theo triệu chứng" trong playbook để xác định vấn đề khả năng cao
nhất (nội dung thiếu chiều sâu, title/meta kém CTR, hay vấn đề kỹ thuật), không chạy đủ 5 bước
cho mọi trang.

Nếu nghi ngờ vấn đề kỹ thuật (impressions thấp bất thường dù bài không mới), chạy:

```bash
python3 scripts/gsc_client.py inspect --url "<URL bài>"
```

để kiểm tra index status trước khi đụng vào nội dung.

Nếu cần xem query nào đang dẫn traffic về trang đó (phục vụ Bước 1 của playbook, xem SERP
thật cho đúng query):

```bash
python3 scripts/gsc_client.py queries --page "<URL bài>" --start <YYYY-MM-DD> --end <YYYY-MM-DD>
```

### Bước 3: Đối chiếu SERP thật và nội dung hiện có

Với top query lấy được ở trên, search trực tiếp trên Google (không tự bịa kết quả SERP), đọc
lại nội dung bài hiện tại (fetch trực tiếp URL bài trên site), rồi làm theo đúng thứ tự bước
trong playbook đã chọn ở Bước 2. Xác định rõ gap cụ thể trước khi viết lại bất kỳ nội dung nào,
không tự chế số liệu (giá, ngày, thông số) không kiểm chứng được, tra nguồn thật nếu cần bổ sung
thông tin mới.

### Bước 4: Trình bày đề xuất trước khi áp dụng

Báo lại người dùng: trang nào, chẩn đoán gì, đề xuất sửa cụ thể ra sao (nội dung mới sẽ thêm/
sửa, title/meta mới nếu có). Chỉ gọi `update_post` sau khi người dùng xác nhận đồng ý, trừ khi
người dùng đã nói rõ từ đầu muốn tự động áp dụng luôn không cần duyệt từng bài.

### Bước 5: Áp dụng update

Gọi tool `update_post` của kết nối WordPress MCP đang dùng cho site này với `post_id` của bài,
kèm `content`/`seo_title`/`seo_description`/`tags` đã sửa. Giữ nguyên các phần không liên quan
đến gap đã xác định, không viết lại toàn bộ bài nếu chỉ cần sửa 1-2 đoạn.

Nếu phần vừa sửa/thêm cần kèm ảnh minh họa, xem thứ tự ưu tiên nguồn ảnh ở mục "Nguồn ảnh minh
họa khi update bài" ngay dưới đây trước khi chèn.

## Nguồn ảnh minh họa khi update bài

**Luôn kiểm tra trùng ảnh trước khi chèn**, nếu bài đã có sẵn ít nhất 1 ảnh (ảnh đại diện hoặc
ảnh khác trong nội dung): nhiều bài báo cùng đưa tin 1 sự kiện hay dùng chung đúng 1 tấm key
art/press photo từ nhà phát hành, nên rất dễ vô tình chọn phải ảnh trùng ảnh đã có sẵn trong
bài dù lấy từ 2 nguồn khác nhau. Trước khi tải ảnh mới lên Media Library, so sánh với ảnh đã có
bằng:
```bash
python3 scripts/check_image_similarity.py <anh_da_co_san> <anh_ung_vien_moi>
```
Hamming distance ≤5/64 nghĩa là gần như chắc chắn cùng 1 ảnh (chỉ khác crop/resize/nén), đổi
sang ảnh khác, không dùng. 6-15 là khá giống, cân nhắc đổi nếu muốn đa dạng hình ảnh trong bài.
>15 mới đủ khác biệt để dùng song song.

**Vị trí chèn ảnh cũng cần cân nhắc, không chỉ nội dung ảnh:** theme của nhiều site tự hiển thị
ảnh đại diện (featured image) ngay đầu bài, phía trên nội dung. Nếu chèn thêm 1 ảnh khác ngay
sau đoạn mở bài, 2 ảnh sẽ nằm sát nhau nhìn dồn cục, mất cân đối. Ưu tiên chèn ảnh minh họa mới
vào **giữa bài**, gần đúng đoạn nội dung nó minh họa (ví dụ ngay trước/sau section vừa thêm),
không đặt sát ngay sau đoạn mở bài khi bài đã có ảnh đại diện.

**Lỗi hay gặp khi gọi tool tạo/sửa bài kèm cả `image_url` và ảnh trong `content`**: luôn so sánh
URL ảnh đầu tiên trong content với `image_url` (ảnh đại diện) trước khi gọi tool, tránh vô tình
để ảnh đại diện xuất hiện lại y hệt ngay đầu content.

Ưu tiên theo thứ tự:

1. **Ảnh gốc từ nguồn tin/nguồn sản phẩm thật** (cách làm mặc định, xem Bước 3): lấy `og:image`
   từ bài báo nguồn đã trích dẫn, hoặc ảnh chính hãng. Luôn kiểm tra `content-type` trước khi
   tải (`curl -I`), luôn dùng cho mọi trường hợp ảnh cần thể hiện ĐÚNG 1 sản phẩm/thiết bị/sự
   kiện cụ thể, không được thay bằng ảnh AI hay ảnh không liên quan trong các trường hợp này vì
   có thể gây hiểu nhầm cho người đọc.
2. **Tái sử dụng ảnh có sẵn trong Media Library từ bài khác trên site**: chỉ dùng khi ý cần
   minh họa là khái niệm chung/trừu tượng (không đại diện 1 sản phẩm cụ thể), và ảnh đó thật sự
   tồn tại (kiểm tra qua `wp-json/wp/v2/media` hoặc bài liên quan đã biết chắc có ảnh phù hợp),
   không tự đoán URL.
3. **Generate ảnh AI qua Gemini** (chỉ khi 2 nguồn trên đều không có, và ý minh họa KHÔNG đòi
   hỏi độ chính xác):
   ```bash
   python3 scripts/generate_image.py "<prompt tiếng Anh, mô tả chi tiết, không chữ trong ảnh>" output.png
   ```
   Dùng biến môi trường `GEMINI_API_KEY`, model `gemini-3.1-flash-lite-image`. Sau khi generate,
   upload qua `upload_media` như ảnh thường. **Luôn nêu rõ trong báo cáo với người dùng đây là
   ảnh AI-generated minh họa, không phải ảnh thật của sản phẩm/sự kiện**. Tuyệt đối không dùng
   AI để tạo ảnh trông giống ảnh thật của 1 sản phẩm/thiết bị cụ thể vì có thể đánh lừa người đọc
   về hình dáng/thông số thật.

### Bước 6: Cập nhật log

Thêm 1 dòng mới vào **đầu bảng** trong `references/refresh-log.md`: ngày check, URL, chẩn
đoán, đã sửa gì, kết quả (`đã sửa`/`giữ nguyên`/`theo dõi`), số liệu trước khi sửa (vị trí/
CTR/impressions từ Bước 1). Nếu bảng vượt khoảng 100-150 dòng, xóa bớt dòng cũ nhất ở cuối.

Trước khi chọn trang để check ở Bước 2, xem nhanh log này, nếu 1 trang vừa được `đã sửa`
trong vòng 2-3 tuần gần nhất, ưu tiên bỏ qua (chưa đủ thời gian để Google phản ánh thay đổi
vào dữ liệu), trừ khi người dùng chỉ định rõ muốn xem lại đúng trang đó.

## Khi người dùng chỉ hỏi xem dữ liệu, không yêu cầu update

Nếu ý định người dùng chỉ là xem báo cáo ("trang nào có traffic", "có lỗi index không"), dừng
ở Bước 1-2, trình bày dữ liệu và chẩn đoán ngắn gọn, không tự ý nhảy sang đề xuất sửa/áp dụng
nếu không được hỏi. Chỉ chủ động gợi ý "có muốn tối ưu tiếp không" ở cuối câu trả lời.

## Files

- `references/post-refresh-playbook.md` — khung chẩn đoán rẽ nhánh theo triệu chứng GSC, 5
  bước check gốc, và lưu ý viết title/meta tăng CTR.
- `references/refresh-log.md` — log các lần đã check/sửa, dùng để tránh check lại quá dày và
  theo dõi hiệu quả các lần sửa trước.
- `references/content-planning-framework.md` — best practice keyword research, độ dài bài,
  pillar-cluster (dùng chung với skill viết bài).
- `scripts/gsc_client.py` — client gọi Google Search Console API bằng service account, hỗ trợ
  4 lệnh CLI: `pages` (trang có traffic), `queries` (query dẫn traffic về 1 trang), `inspect`
  (index status 1 URL), `striking-distance` (lọc trang vị trí 8-20 có CTR dưới benchmark).
  Có thể import trực tiếp class `GSCClient` nếu cần dùng trong script Python khác.
- `scripts/generate_image.py` — generate 1 ảnh minh họa qua Gemini (`GEMINI_API_KEY`), dùng khi
  không có ảnh gốc/ảnh tái sử dụng phù hợp.
- `scripts/check_image_similarity.py` — so sánh 2 ảnh bằng average hash (Pillow, không cần
  cài thêm gì), phát hiện ảnh trùng/gần trùng trước khi chèn thêm 1 ảnh vào bài đã có ảnh.
- `scripts/clarity_client.py` — client gọi Microsoft Clarity Data Export API bằng
  `SEO_CLARITY_TOKEN`, lệnh `insights --days 1|2|3` (giới hạn thật của API, không lấy
  được xa hơn 3 ngày). Dùng để bổ sung số liệu hành vi người dùng bên cạnh GSC.
- `scripts/ga4_client.py` — client gọi Google Analytics 4 Data API, dùng chung hoặc riêng key
  với GSC (`SEO_GSC_SA_JSON`), property ID bắt buộc set qua `SEO_GA4_PROPERTY_ID`. 4 lệnh CLI:
  `traffic` (sessions/users/pageviews theo ngày), `pages` (top trang theo pageviews), `sources`
  (traffic theo nguồn/kênh toàn site), `page-sources --page <pagePath>` (traffic theo nguồn/kênh
  cho ĐÚNG 1 trang cụ thể, bắt buộc dùng thay vì chỉ `sources` khi cần kết luận nguyên nhân
  tăng/giảm traffic của 1 trang). Không giới hạn khoảng thời gian như Clarity.
