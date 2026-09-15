# Keyword Content Planning Framework

Đúc kết từ research best practice (2026) về keyword content plan. Mục tiêu: có cách trả lời rõ
ràng cho 2 câu hỏi "keyword nào nên viết" và "nên viết bao nhiêu bài cho 1 chủ đề", dựa trên
data thật (GSC, GA4, file keyword research riêng của site) thay vì cảm tính.

**Ghi chú khi setup cho site mới**: file này giữ nguyên phần khung phương pháp/best practice
(generic, áp dụng được cho mọi site). Phần áp dụng cụ thể dựa trên data thật của site (mục 5,
tự thêm sau khi có đủ data GSC/GA4 vài tháng) nên viết riêng theo từng site, không copy nguyên
data từ site khác sang.

## 0. Cách nghiên cứu từ khóa cho 1 page (Keyword Research)

### Quy trình chuẩn: Tìm → Phân tích → Dùng

1. **Xác định seed keyword**: 5-10 từ khóa gốc theo chủ đề chính của site
2. **Mở rộng** qua các nguồn miễn phí bên dưới
3. **Check search intent TRƯỚC khi viết** (quan trọng hơn cả mật độ từ khóa theo xu hướng
   2026): search thử keyword thật trên Google, xem top 3-5 kết quả đang là dạng gì (listicle,
   guide, trang sản phẩm...). Nếu top toàn trang bán hàng mà viết blog thì khó rank, đổi sang
   biến thể khác khớp đúng intent hơn.

### Nguồn miễn phí (áp dụng được ngay, không cần tool trả phí)

- **Google Autocomplete**: gõ chủ đề vào ô search, đọc gợi ý tự động, phản ánh đúng cách người
  thật tìm kiếm
- **People Also Ask**: xuất hiện ở ~43% kết quả search, mỗi câu hỏi trong đó là 1 ý tưởng
  heading/FAQ cho bài
- **Related Searches** (cuối trang kết quả Google): thường có thêm ~8 biến thể từ khóa
- **Google Ads Keyword Planner**: nguồn volume chính xác nhất vì lấy thẳng từ Google. **Lưu ý 2
  hạn chế**: (1) nếu tài khoản Google Ads không chạy ads đang active, chỉ trả về khoảng ước
  lượng rộng (vd "1K-10K") thay vì số chính xác, cần tài khoản có chạy ads mới lấy được số cụ
  thể; (2) chỉ số "Competition" trong tool này là độ cạnh tranh **đấu giá quảng cáo trả phí**,
  KHÔNG phải độ khó SEO ranking tự nhiên, 2 khái niệm khác nhau, không dùng thay thế cho việc
  research SERP thật. Có tính năng "Discover new keywords" hữu ích để tìm từ khóa mới khi ra
  sản phẩm/chủ đề mới, nên chạy lại định kỳ (gợi ý mỗi quý, hoặc khi có dòng sản phẩm/chủ đề
  mới) nếu có quyền truy cập tài khoản Google Ads đang active.
- **Google Search Console (dùng qua `gsc_client.py` trong skill `post-refresh`)**: nguồn mạnh
  nhất vì là data thật của chính site, không cần tool ngoài. Xem kỹ thuật "Striking Distance
  Keywords" ngay dưới.

### Striking Distance Keywords: kỹ thuật GSC mạnh nhất cho site đã có traffic

Lọc trong data GSC (`gsc_client.py pages`/`queries`): **vị trí 8-20 + impressions cao + CTR
thấp** = cơ hội tốt nhất, vì:
- Cải thiện 1 bài đã có sẵn thường NHANH và RẺ hơn viết bài mới hoàn toàn (không cần content
  gap, chỉ cần sửa title/nội dung để đẩy từ vị trí ~8 lên top 3, CTR có thể tăng gấp 3-5 lần
  theo benchmark CTR-theo-vị-trí trong `post-refresh-playbook.md`)
- Đây chính là cơ chế skill `post-refresh` đang làm thủ công (Bước 1-2), giờ có tên gọi và
  ngưỡng cụ thể để lọc nhanh hơn: ưu tiên trang có vị trí 8-20 VÀ impressions cao hơn hẳn CTR
  thực tế so với benchmark
- Ngoài ra, **query nào có impressions trong GSC nhưng KHÔNG trang nào target rõ ràng** (không
  match title/heading bài nào) chính là gợi ý content gap tự nhiên từ chính data thật của site,
  đáng cân nhắc viết bài mới

### 4 loại search intent, mỗi loại cần định dạng bài khác nhau

| Loại intent | Tỷ trọng volume trung bình | Định dạng bài phù hợp |
|---|---|---|
| Informational (muốn học/hiểu) | ~53% | Guide, hướng dẫn, "X là gì" |
| Navigational (tìm 1 trang cụ thể) | ~21% | Không áp dụng cho content mới (người tìm brand/site cụ thể) |
| Transactional (sẵn sàng mua) | ~16% | Trang sản phẩm, review có CTA mua hàng |
| Commercial (đang so sánh) | ~8.5% | Bảng so sánh, "nên mua X hay Y" |

Xác định intent bằng cách search thật rồi xem SERP đang trả về dạng gì (đáng tin hơn suy đoán
từ cách viết của keyword).

## 1. Cách xác định keyword nào NÊN viết bài

### Công thức chấm điểm (0-12 điểm, ưu tiên viết nếu ≥8)

| Yếu tố | 3 điểm | 1 điểm |
|---|---|---|
| Search volume | Cao (trong khoảng sweet spot, xem dưới) | Thấp/không có data |
| Độ khó (Keyword Difficulty, nếu có tool đo) | Thấp | Cao |
| Search intent khớp mục tiêu | Có ý định mua/tìm hiểu sâu, đúng đối tượng site | Chỉ tò mò lướt qua |
| Đối thủ đang cover yếu | Bài đối thủ mỏng/thiếu thông tin mới | Đối thủ đã cover rất kỹ |

### Ngưỡng volume hợp lý cho site nhỏ/mới

- **Sweet spot: 100-1.000 lượt tìm/tháng.** Đủ ý nghĩa nhưng chưa cạnh tranh khốc liệt với site
  lớn có backlink mạnh.
- Site độ uy tín thấp/mới nên ưu tiên **Keyword Difficulty thấp** (tương đối, nếu chưa có tool
  đo KD trực tiếp, có thể ước lượng qua độ mạnh của các trang đang đứng top 10 khi research SERP
  thủ công).
- **Long-tail luôn là chiến lược đúng cho site nhỏ**: cụ thể hơn, cạnh tranh thấp hơn, tỷ lệ
  khớp đúng ý định người tìm cao hơn (khớp với nguyên tắc "content-accurate keyword" trong skill
  `seo-blog-writer`: chọn từ khóa mô tả đúng chủ thể chính của bài, không ép theo volume cao
  nhưng sai ngữ cảnh).
- Nếu keyword không có data volume (quá mới/quá ngách): vẫn viết được nếu tin đủ nóng trên
  cộng đồng (nhiều thảo luận/lượt xem), miễn khớp đúng chủ thể bài.

## 2. Cách xác định viết BAO NHIÊU bài cho 1 chủ đề

### Nguyên tắc gộp/tách bài: SERP Overlap Method

Trước khi quyết định viết 1 bài riêng cho 1 keyword mới, kiểm tra top 10 kết quả Google cho
keyword đó và cho keyword gần nghĩa đã có bài:
- Nếu **≥3-4 URL trùng nhau** trong top 10 → Google coi 2 keyword cùng 1 search intent →
  **gộp vào 1 bài** (mở rộng bài cũ), không tách bài mới để tránh cannibalize.
- Nếu top 10 khác biệt rõ (ít URL trùng) → search intent khác nhau thật → tách bài riêng là hợp
  lý.

Đây chính là cơ chế đang làm thủ công qua `used-keywords.md` (đối chiếu keyword dự định dùng
với bảng đã có), có thể làm bài bản hơn bằng cách chủ động search SERP thật trước khi chốt viết
bài mới cho 1 chủ đề nghi ngờ trùng, không chỉ so tên keyword.

### Chiều sâu quan trọng hơn chiều rộng

- Nghiên cứu 2026 chỉ ra: brand có **3-7 topic cluster được đầu tư sâu (30-50 bài/cluster)**
  luôn thắng brand có 15-20 cluster nhưng mỗi cái chỉ 10 bài hời hợt, trên mọi metric SEO.
- **Bài cluster mỏng còn tệ hơn không có bài** — nếu 1 bài không cover chủ đề con sâu hơn hẳn
  phần liên quan trong bài pillar, nó gây cannibalization thay vì tín hiệu chuyên môn (topical
  authority).
- Kiến trúc chuẩn: 1 **pillar page** (bài tổng quan bao quát cả chủ đề lớn) + nhiều **cluster
  page** (mỗi bài đào sâu 1 khía cạnh con, link ngược về pillar).

### Quy mô cho site affiliate/thương mại nhỏ

- Cần khoảng **100-500 bài xuất bản** mới đủ sức cạnh tranh ở nhóm từ khóa thương mại.
- Xuất bản đều đặn **8-15 bài/tháng** trong 12-24 tháng là ngưỡng thực tế để cạnh tranh dần.
- Site nhỏ nên ưu tiên keyword **high-intent, low-competition** (mang về người mua thật, không
  chỉ người lướt xem) hơn là chạy theo volume tuyệt đối.

## 3. Đánh giá evergreen vs tin tức (tự đo lại theo data thật của từng site)

Trước khi đầu tư mạnh vào 1 trong 2 hướng (bài evergreen như review/so sánh/hướng dẫn mua, hay
bài tin tức thời sự), nên tự đo bằng data GSC thật của site (không giả định kết quả từ site
khác áp dụng đúng cho site mình):

1. Lấy danh sách URL có traffic organic 60-90 ngày qua (`gsc_client.py pages`)
2. Tự phân loại thủ công: bài nào là evergreen (review, so sánh, hướng dẫn mua, "X là gì"), bài
   nào là tin tức (giá tăng, ra mắt, preorder, sự kiện thời hạn), loại bỏ trang chức năng
   (shop/cart/category/trang chủ)
3. Tính tổng clicks/impressions/CTR trung bình cho mỗi nhóm, so sánh clicks trung bình/bài giữa
   2 nhóm

Ghi lại kết quả và ngày đo vào đây (hoặc file riêng theo site) sau khi có đủ data, làm căn cứ
quyết định tỷ trọng đầu tư giữa 2 hướng nội dung cho đúng site đó.

## 4. Độ dài bài phù hợp

**Quan trọng: word count KHÔNG phải ranking factor nhân quả.** Semrush 2024 Ranking Factors Study
đo correlation giữa độ dài nội dung và vị trí xếp hạng chỉ **0.02** (gần như bằng 0, dựa trên data
thật, không phải suy đoán). Google (John Mueller, phát ngôn chính thức nhiều lần) cũng khẳng định
word count không phải yếu tố chất lượng hay xếp hạng. Các con số "1.500-2.500 từ" hay gặp trên
mạng chỉ là **trung bình của các trang ĐANG rank top** (quan sát, không phải mục tiêu cần đạt để
được rank). Dùng độ dài như 1 cách tự kiểm tra đã viết đủ sâu chưa, không coi là KPI phải đạt.

### Theo search intent (độ tin cậy YẾU, chỉ có nguồn thứ cấp/practitioner, không có study gốc đo trực tiếp)

| Intent | Range hay được trích |
|---|---|
| Navigational | 50-500 từ |
| Transactional | 300-1.000 từ |
| Informational | 800-2.500 từ |
| Commercial | 1.200-3.000 từ |

### Theo loại bài (cũng chỉ là quy ước ngành lặp lại nhiều nơi, không truy được về 1 study gốc cụ thể)

| Loại bài | Range hay được trích |
|---|---|
| Tin tức | 300-800 từ |
| Review 1 sản phẩm | 1.500-2.500 từ |
| So sánh 2+ sản phẩm | 2.500-4.000 từ |
| Guide/hướng dẫn mua | 1.500-2.500 từ (tới 4.000 nếu rất chi tiết) |
| "X là gì" (định nghĩa) | Không có study riêng, gần tương đương informational (800-1.500 từ), ưu tiên trả lời trực tiếp 40-60 từ đầu đoạn (khớp answer capsule đã có) |

### Tin tức có nên ngắn hơn evergreen không?

Có lý do hợp lý (query tin tức cần fact nhanh, không cần đào sâu, Google News/Discover ưu tiên
tính thời sự hơn độ sâu cho loại query này) và được đồng thuận rộng rãi trong ngành, nhưng
**không có study nào đo trực tiếp** "tin ngắn rank tốt hơn tin dài" hay ngược lại. Đây là logic
khớp-đúng-intent, không phải data thực nghiệm.

## Nguồn tham khảo

- Độ dài bài theo intent/loại bài: Backlinko (search-engine-ranking, content-study), Semrush 2024
  Ranking Factors Study, Ahrefs (content-length blog series), HubSpot (qua tổng hợp của Search
  Engine Journal), phát ngôn chính thức John Mueller/Google (qua Search Engine Roundtable, Search
  Engine Journal), Yoast (blog-post-word-count-seo)
- Topic cluster & pillar-cluster: Brafton, Topic Intelligence, SEOsolved, DigitalApplied
- Keyword volume/difficulty threshold: TopContent, Keyword.com, Semrush, Victorious
- Content gap analysis & scoring formula: Respona, RankSper, ClusteA, Up North Media
- SERP overlap / keyword clustering: Thruuu, Plerdy, SEOcluster.ai, WriteIntent
- Content volume cho niche/affiliate site: NicheSiteProject, GetLasso, various affiliate SEO
  guides
- Quy trình keyword research & search intent: Mangools, Brafton, Prism-me, Web Tonic, Incremys
- Phương pháp miễn phí (Autocomplete/PAA/Related Searches): 20MinuteMarketing, Lilach Bullock,
  BrandWell, Okara
- Google Ads Keyword Planner cho SEO: SEO.com, ResultFirst, Surfside PPC, The Marketing Agency
- Striking Distance Keywords: Vazoola, Clutch.co, GSCdaddy, Content Raptor, Ricketyroo, Citewins
