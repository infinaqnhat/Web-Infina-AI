# Internal Linking Guide

Bộ quy tắc liên kết nội bộ dùng lại được cho bất kỳ site blog/content nào, không gắn với một site
cụ thể. Rút ra từ một site production thật sau nhiều đợt audit, nên mỗi quy tắc đều kèm **nguồn**
hoặc **số đo**, và phần nào không có nguồn thì nói thẳng là quyết định biên tập.

**Cách đọc file này:** Phần 1 là thứ Google thật sự nói, gần như không đổi theo thời gian. Phần 4
là mốc vận hành, bạn **phải** đo lại trên site của mình rồi chỉnh. Phần 8 là danh sách cấm, đọc để
không vô tình dựng lại những ngưỡng đã bị gỡ.

---

## 0. Tóm tắt một trang

> **Cụm tự nuôi nhau, pillar đứng yên.**
> Bài mới trỏ **lên** pillar đúng 1 lần và trỏ **ngang** 2-3 bài cùng cụm, đặt trong thân bài.
> Chiều **về** thì nhờ một bài anh em cùng cụm, không nhờ pillar.

Ba việc bắt buộc cho mỗi bài mới, theo thứ tự rẻ tiền trước:

1. **Link ngang sang 2-3 bài cùng cụm, trong thân bài**, làm ngay lúc viết. Rẻ nhất vì không phải
   sửa bài nào khác, tốt nhất vì anchor bám ngữ cảnh.
2. **Link lên pillar, đúng 1 lần.**
3. **Cho bài mới một inbound link biên tập** từ một bài cluster cùng cụm. Đây là việc duy nhất bài
   mới không tự làm được, vì mọi bài khác trên site đều viết trước nó.

Nếu chỉ nhớ được một câu: **bỏ việc số 3 là bài vừa publish không có trang nào trỏ tới.**

---

## 1. Thứ Google thật sự nói, và chỉ có ba điều

| Điều | Nguồn |
|---|---|
| **Không có giới hạn số link trên 1 trang.** Quy tắc "100 link mỗi trang" bỏ từ 2008, vốn là giới hạn kỹ thuật thời Googlebot chỉ tải khoảng 100KB đầu trang | [Search Engine Roundtable](https://www.seroundtable.com/google-link-unlimited-18468.html) |
| **Vị trí link không làm Google đánh giá khác đi.** Header, footer, sidebar hay thân bài đều như nhau: *"We don't really differentiate there."* | John Mueller, [SEJ 03/2022](https://www.searchenginejournal.com/are-internal-links-in-header-and-footer-treated-differently/441993/) |
| **Quá nhiều internal link làm loãng CẤU TRÚC site**, không làm yếu từng link: *"If every page links to every other page, then there's no real structure there."* Mueller **không đưa ra con số nào** | Hangout 02/07/2021, [SEJ](https://www.searchenginejournal.com/google-cautions-against-using-too-many-internal-links/412553/) |

Thêm hai câu từ tài liệu chính thức của Google, đáng nhớ vì chúng định nghĩa sàn và trần:

- **Sàn:** *"Every page you care about should have a link from at least one other page on your site."*
  Đây là lý do một bài mồ côi là vấn đề thật, không phải chuyện làm đẹp.
- **Trần:** *"There's no magical ideal number of links a given page should contain."*
  Đây là lý do mọi ngưỡng số ở Phần 4 chỉ là mốc tự soi.

Ràng buộc thứ ba trong bảng nhắm vào **phân bố link trên toàn site**, không nhắm vào từng bài. Đó là
lý do kỹ thuật cho toàn bộ thiết kế ở Phần 2.

---

## 2. Mô hình pillar-cluster: ai trỏ ai

Một **cụm** gồm 1 pillar (trang hub, nhắm head term) và 8-15 cluster (bài sâu, nhắm long-tail
riêng). Không bao giờ để 2 bài trong site cùng nhắm 1 keyword, nếu không chúng cạnh tranh nhau trên
SERP.

### Bảng chiều link

| Từ ↓ &nbsp;&nbsp; Tới → | **Pillar** | **Cluster cùng cụm** | **Bài vừa publish** |
|---|---|---|---|
| **Pillar** | | mỗi cluster đúng 1 lần | ❌ **không bắt buộc**, chỉ là đường lui |
| **Cluster cũ** | đúng 1 lần | 2-3 bài | ✅ **1 bài phải trỏ sang** |
| **Bài mới** | ✅ đúng **1 lần** | ✅ **2-3 bài**, trong **thân bài** | |

Ô ✅ là bắt buộc, fail thì chặn. Ô ❌ là chỗ nhiều quy trình làm sai.

### Một cluster trỏ lên được MẤY pillar?

Được nhiều. **Không có luật nào của Google cấm**, và quy tắc "1 cluster chỉ trỏ 1 pillar" là quy ước
của khung HubSpot chứ không phải chính sách của Google.

Ba điều đã kiểm:

| Điều | Nguồn |
|---|---|
| Tài liệu chính thức của Google về internal link **không có một chữ nào** về silo, về gom trang thành khu, hay về chuyện một trang được trỏ lên mấy hub | [Google Search Central, Make your links crawlable](https://developers.google.com/search/docs/crawling-indexing/links-crawlable) |
| Mô hình pillar-cluster là khung của **HubSpot, 2017**, dựng từ một **tương quan** họ quan sát được giữa thứ hạng và cách gom internal link. Tương quan không phải ranking factor | [HubSpot](https://blog.hubspot.com/marketing/pillar-cluster-model-transform-blog) |
| Google **chưa bao giờ** xác nhận mô hình này, cũng chưa bao giờ nói link chéo cụm là có hại | không tìm được phát biểu nào, xem cảnh báo bên dưới |

⚠️ **Thứ KHÔNG kiểm được, đừng trích lại.** Có một câu "pyramid structure" gán cho Mueller được các
blog SEO trích đi trích lại để biện minh cho silo. **Không truy được bản gốc.** Đúng loại nguồn mà
Phần 8 đã liệt vào danh sách cấm, nên không dùng nó làm căn cứ theo chiều nào cả.

**Ràng buộc thật duy nhất nhắm vào TOÀN SITE, không nhắm vào từng bài.** Đó là câu Mueller
02/07/2021 ở Phần 1: *"If every page links to every other page, then there’s no real structure
there."* Nó nói về phân bố link trên cả site. Một bài trỏ lên 2 pillar không chạm tới nó.

Đo bằng **mật độ link**: số link nội bộ phân biệt chia cho `n*(n-1)`. Trên site gốc 489 link trên
147 bài cho ra **2,3%**, cách rất xa tình huống Mueller cảnh báo. Dùng số này để tự trấn an khi
phân vân có đang link nhiều quá không.

### Nhưng phải đo tỉ lệ trỏ pillar nhà vs pillar cụm khác

Đây là **quyết định biên tập, không có nguồn Google**. Link chéo không phạm luật, nhưng nếu một cụm
trỏ ra ngoài nhiều hơn trỏ về pillar của chính mình thì cụm đó đang nuôi pillar của cụm khác.

Đo trên site gốc, 8 cụm:

| Cụm | Trỏ pillar nhà | Trỏ pillar cụm khác | % nhà |
|---|---|---|---|
| Compliance | 5 | 0 | 100% |
| Chatbot | 17 | 3 | 85% |
| Lead Gen | 7 | 2 | 78% |
| CRM | 32 | 11 | 74% |
| Website Builder / IDX | 12 | 11 | 52% |
| AI Voice | 5 | 5 | 50% |
| Landing Pages | 5 | 9 | **36%** |
| Website Design | 5 | 10 | **33%** |
| **Tổng** | **88** | **51** | **63%** |

Hai cụm cuối trỏ ra ngoài nhiều hơn trỏ về nhà, và cả hai đều đổ vào cùng một pillar CRM. Đó là lý
do pillar CRM nhận 56 inbound trong khi pillar Website Design chỉ có 6. Không ai làm sai luật,
nhưng pillar của hai cụm đó sẽ không bao giờ khoẻ lên.

**Mốc tự soi: % trỏ pillar nhà >= 50% cho mỗi cụm.** Giống mọi mốc ở Phần 4, con số này lấy từ phân
bố thật của một site chứ không phải ngưỡng ngành, nên phải đo lại trên site của bạn.

**Cách sửa khi một cụm tụt dưới mốc: thêm link về pillar nhà, đừng gỡ link chéo.** Link chéo tồn tại
vì câu văn có lý do nhắc tới nó, gỡ đi là làm hỏng bài. Thiếu là thiếu chiều về nhà.

### Vậy câu hỏi đúng là gì

Không phải "bài này được trỏ mấy pillar" mà là **"câu chứa link này có lý do tồn tại không"**. Đó
chính là tiêu chí 2 ở mục chọn bài donor ngay dưới đây, và nó áp cho cả link lên pillar.

### Vì sao pillar KHÔNG cần trỏ xuống bài mới

Hai lý do, lý do thứ hai mới là lý do thật:

1. Lý do cũ "link từ pillar mạnh hơn vì pillar có authority" bị Mueller 03/2022 bác thẳng.
2. **Nó cộng dồn vĩnh viễn.** Mỗi bài mới lại thêm 1 link vào cùng một pillar. Trên site gốc, pillar
   CRM lên tới 22 link nội bộ và nhận 53 inbound trước khi ai đó để ý. Đúng cái Mueller cảnh báo.
   Chọn sibling thì tải phân tán ra cả cụm và pillar đứng yên.

### Chọn bài donor (bài sẽ trỏ sang bài mới), theo thứ tự

1. **Cùng cụm** theo bảng phân cụm biên tập của bạn.
2. **Có sẵn một đoạn đang nói đúng chủ đề bài mới.** Không có thì loại bài đó ra, đừng ép. Đây là
   tiêu chí quyết định. Thà lui về pillar còn hơn nhét một câu lạc lõng.
3. Chưa link sang bài mới.
4. Ưu tiên bài đã có traffic thật.

**Đường lui:** không cluster nào trong cụm đạt tiêu chí 2 thì dùng pillar. Hợp lệ, không phải thất
bại, hay gặp với cụm mới hoặc chủ đề lần đầu xuất hiện.

⚠️ **Không suy ra thành viên cụm từ link graph.** Đã thử và sai cả hai chiều: đếm "bài nào trỏ lên
pillar X" thì hút nhầm các bài link chéo cụm; đếm "bài chỉ trỏ lên đúng 1 pillar" thì loại oan các
cluster hợp lệ có link chéo. Nguồn đúng duy nhất là bảng phân cụm do người quyết định. Link graph
dùng để **đo sức khoẻ** (inbound, outbound, mồ côi), không dùng để **định nghĩa** cụm.

### Vì sao ưu tiên link thân bài, dù Google không phân biệt

Hai lý do, đều là biên tập chứ không phải SEO:

1. **Anchor bám ngữ cảnh.** Link giữa đoạn được viết thành câu có lý do, nên anchor mô tả đúng thứ
   nằm ở đầu kia. Link trong danh sách cuối bài hay bị rút thành tiêu đề trần.
2. **Người đọc đang ở đúng chỗ.** Link đặt ngay lúc nhắc tới chủ đề thì gặp người đang quan tâm chủ
   đề đó, khác với một danh sách đọc thêm sau khi họ đã đọc xong.

Nên đây là **ưu tiên lúc viết**, không phải điều kiện pass/fail. Đừng dựng ngưỡng phần trăm quanh nó.

### Mồ côi nghĩa là gì, và không nghĩa là gì

**Mồ côi = thiếu inbound biên tập.** Nó **không** có nghĩa Google không thấy bài. Nếu site có
category archive dạng `index, follow` thì vẫn có đường crawl tới mọi bài.

| Mất gì | Không mất gì |
|---|---|
| Anchor text mô tả (archive chỉ cho anchor là title trần) | ❌ **KHÔNG** bị rớt khỏi index |
| Dòng PageRank nội bộ thật (trang archive giá trị thấp, chia cho hàng chục bài) | ❌ **KHÔNG** phải Google không thấy bài |
| Tín hiệu topical relevance: không trang nào "nhận" bài này là người nhà | |

Nói gọn: mồ côi không giết bài, nhưng làm bài yếu đi đúng ở chỗ bạn vừa bỏ công viết. Chi phí sửa
gần như bằng không (thêm một câu vào một bài đã có), nên bỏ bước này để tiết kiệm 2 phút là lỗ.

### TOC không tính là internal linking

Mục lục thường là anchor nhảy trong cùng trang (`#heading`), phục vụ UX và featured snippet, trừ khi
nó link thẳng sang các trang cluster.

---

## 3. Anchor text

**Anchor text là phần chữ hiển thị của link**, tức mấy chữ xanh có gạch chân, không phải một field
riêng trong SEO plugin.

```html
<a href="https://example.com/best-crm/">best CRM for real estate agents</a>
                                       └──────── anchor text ────────┘
```

Google chỉ đọc được "trang bên kia nói về cái gì" qua chuỗi này. Nếu 5 bài khác nhau đều dùng y hệt
một chuỗi, bạn đang lặp đúng một câu mô tả 5 lần thay vì mô tả trang đó từ 5 góc.

### Bảy quy tắc

1. 🟢 **Đọc tách khỏi câu vẫn hiểu được.** Che câu đi, chỉ còn anchor, vẫn đoán được trang đích nói
   gì. Google nêu đúng phép thử này trong tài liệu chính thức.
2. 🟢 **Không dùng** `click here`, `read more`, `this post`, `here`.
3. 🟢 **Không nhồi keyword, không dài lê thê.** Khoảng 3-8 từ.
4. 🟢 **KHÔNG bắt buộc chứa keyword của trang đích nguyên văn.** Anchor chỉ cần mô tả đúng trang đích.
5. 🟢 **Đọc anchor đã dùng trước khi viết anchor mới**, chọn biến thể chưa ai dùng. Script ở Phần 6.
6. 🟢 **Mỗi bài chỉ 1 link tới cùng một trang**, không lặp anchor đó trong cùng bài.
7. 📊 **Mục tiêu: anchor khác nhau / tổng link tới 1 trang >= 70%.**

⚠️ **Quy tắc 4 là quy tắc quan trọng nhất và cũng là quy tắc hay bị làm ngược nhất.** Trên site gốc,
quy trình từng **bắt buộc** anchor trỏ pillar phải chứa `PILLAR_KW`. Vì `PILLAR_KW` cố định cho mỗi
pillar, mọi bài đổ dồn về cùng một chuỗi. Đo thực tế trên 145 bài:

| Pillar | Link trỏ tới | Anchor khác nhau | |
|---|---|---|---|
| `best-crm-for-real-estate` | 53 | 12 (23%) | **35 link dùng y hệt một chuỗi** |
| `tcpa-compliance...` | 14 | 2 (14%) | |
| `real-estate-website-builder` | 28 | 6 (21%) | |
| `real-estate-agent-crm-speed-to-lead` | 13 | 10 (77%) | đạt, viết tự do |
| `best-ai-virtual-assistant-real-estate` | 9 | 7 (78%) | đạt, viết tự do |

Mốc 70% ở quy tắc 7 lấy từ hai dòng cuối, tức **hai trang tự nhiên đạt được khi không bị ép anchor**.
Nó là mốc chạm được chứ không phải ngưỡng ngành đi mượn.

⚠️ **Đừng chỉ kiểm tra anchor trỏ pillar.** Trang non-pillar cũng dính y hệt. Ví dụ thật: một trang
nhận 5 link, cả 5 dùng chung một anchor (20% đa dạng), lọt lưới suốt nhiều tháng chỉ vì nó không
phải pillar nên nằm ngoài tầm check.

⚠️ **Khi gộp bài, phải sửa cả anchor chứ không chỉ href.** Anchor là **tên nguyên văn của trang đã
xoá** thì dù href đã trỏ đúng, bạn vẫn đang giới thiệu một trang không còn tồn tại.

### Khi phải bỏ bớt một link trùng đích trong cùng bài

Giữ cái nào? Không theo vị trí, mà theo **câu nào hỏng nếu mất link**:

- Câu cuối bài thường có dạng *"our guide to X"*, *"our roundup of X"*. Bỏ link là hứa một bài rồi
  không cho đường đi. **Giữ.**
- Anchor thân bài thường chỉ là cụm danh từ (*"a shared chat platform built for teams..."*). Bỏ link
  vẫn đọc trôi. **Gỡ cái này.**

Ưu tiên vị trí là chuyện lúc **viết**. Lúc **gỡ** thì ngược lại.

---

## 4. Mốc vận hành (quyết định biên tập, PHẢI đo lại trên site của bạn)

Không có con số nào dưới đây đến từ Google. Chúng là mốc để tự soi.

| Chỉ số | Mốc tham chiếu |
|---|---|
| Độ dài bài cluster | 1.200-2.000 chữ |
| Số cluster trên 1 pillar | 8-15, vượt 20 cân nhắc tách sub-hub |
| Cluster link lên pillar | đúng 1 lần |
| Cluster link ngang cùng cụm | 2-3 |
| Tổng link nội bộ, bài ~1.000 chữ | 4-6 |
| Pillar link tới cluster | mỗi cluster đúng 1 lần |
| Link tới money page | 1-3, đặt chỗ intent mua cao nhất |
| Money page nhận inbound | 10-20 link |
| Đa dạng anchor trên mỗi trang đích | >= 70% |

**Độ dài pillar: suy ra từ SỐ CLUSTER, đừng đặt mục tiêu số chữ.**

```
do_dai_pillar ~= 400 (mo bai) + 150 x so_cluster + 200 (ket)
```

| Số cluster | Độ dài suy ra |
|---|---|
| 8 | ~1.800 chữ |
| 15 | ~2.950 chữ |
| 25 | ~4.350 chữ |
| 30 | ~5.100 chữ |

Khoảng tham khảo của ngành là 2.000-5.000 chữ, và nó chính là hệ quả của công thức trên khi cụm có
10-30 bài. Nếu pillar rơi ngoài khoảng đó, kiểm tra **số cluster** trước khi kết luận bài quá ngắn.

⚠️ **Word count không phải ranking factor.** Mueller: *"Word count is not a ranking factor, save
yourself the trouble."* Danny Sullivan (2023): *"The best word count needed to succeed in Google
Search is not a thing, it doesn't exist."* Bài dài rank tốt vì phủ chủ đề đủ và hút backlink, không
phải vì dài.

**Ba bẫy khi áp công thức này**, cả ba đã xảy ra thật:

1. **"N bài trong cụm" thường đã GỒM pillar.** Trừ pillar ra trước khi nhân 150.
2. **Cụm có 2 pillar thì chia số cluster ra trước.** Một cụm 13 cluster trên 2 pillar nghĩa là mỗi
   pillar gánh ~6, không phải 13.
3. **Đừng áp số tuyệt đối lên bài ngắn.** Lấy "20-40 link cho pillar" áp lên pillar 1.832 chữ rồi
   kết luận "đang thiếu link" là sai hai tầng: sai vì dùng số tuyệt đối thay vì chia cho độ dài, và
   sai vì bản thân con số đó không có cơ sở (xem Phần 8).

⚠️ **Độ dài đạt không có nghĩa cụm khoẻ.** Một audit cho thấy cả 2 pillar của một cụm đều thừa chữ
nhưng một pillar có **0 link ngoài** và **7/8 link nội bộ dồn trong mục Related Reading**. Đo đủ bộ:
độ dài, link/1.000 chữ, tỷ lệ link trong thân bài, số link ngoài, density, đa dạng anchor.

---

## 5. Quy trình cho mỗi bài mới

Chia làm 2 làn. **GATE** là thứ hỏng thật và sửa được, chặn lại. **WARN** là phán đoán biên tập, chỉ
ghi nhận.

### Trước khi viết

1. Chọn trang đích (pillar) và chốt keyword riêng cho bài mới, khác keyword pillar.
2. Ưu tiên pillar **chưa bị dùng nhiều gần đây**, để tải phân tán.
3. Chạy `anchors_to(slug)` xem anchor nào đã bị dùng. **Chạy trước khi viết**, không phải sau: viết
   xong rồi mới kiểm tra thì bạn đã có sẵn một câu hay và sẽ ngại sửa.

### Lúc viết

4. Chèn 2-3 link ngang sang bài cùng cụm, **trong thân bài**, viết thành câu có lý do để bấm.
5. Link lên pillar, đúng 1 lần, anchor mô tả đúng pillar và chưa ai dùng.

### GATE trước khi publish

6. **Mọi link nội bộ phải trỏ tới URL trả 200.** Chạy `check_targets()` (Phần 6) trên nội dung lúc
   nó còn là chuỗi. Đặt **trước** publish chứ không phải sau: fail lúc đó không tốn gì.

### GATE sau khi publish

7. Bài mới có link lên pillar.
8. Bài mới có >= 2 link ngang cùng cụm.
9. Một bài donor cùng cụm đã trỏ sang bài mới.

### WARN sau khi publish, chỉ ghi nhận

- Link lên pillar lặp > 1 lần.
- Anchor trỏ pillar trùng với bài khác.
- **Anchor trỏ các link ngang trùng với bài khác.** Đừng bỏ qua cái này, xem cảnh báo ở Phần 3.
- Quá nửa link dồn cuối bài.
- Mật độ link lệch hẳn so với phần còn lại của site.

⚠️ **Sau khi đã publish, không `assert` nào được phép abort.** Bài đã lên mà script chết giữa chừng
thì bước ghi log không chạy và lần sau không ai biết bài đó tồn tại. Mọi check hậu publish gom vào
một danh sách `warnings` rồi in ra cuối. Lỗi này đã xảy ra 2 lần trong một session.

### Trường hợp bài đã lên lịch, chưa live

Slug chưa tồn tại nên trỏ bài khác vào URL còn 404 là hại. Hoãn chiều inbound lại, ghi chú để quay
lại sau giờ publish. Riêng chiều bài mới trỏ đi thì làm được ngay.

Ngoại lệ hợp lệ: hai bài viết cùng lúc, lên lịch cách nhau, bài A cố ý link sang bài B sắp live. Link
đó tự lành đúng giờ publish. Khai báo tường minh (tham số `allow` của `check_targets`), đừng dùng nó
để làm ngơ một slug gõ sai.

---

## 6. Script kiểm tra

Đổi 2 hằng số đầu file là dùng được cho site khác. Giả định WordPress REST API; site khác thì thay
phần lấy nội dung, phần còn lại giữ nguyên.

```python
# -*- coding: utf-8 -*-
"""Kiem tra internal linking. Doi SITE va BASE cho site cua ban."""
import re, json, html, gzip, time, collections
import urllib.request, urllib.error

SITE = "https://example.com"
BASE = "/news/"                      # tien to duong dan bai viet, "/" neu o goc
API  = SITE + BASE + "wp-json/wp/v2/posts"
LINK = re.compile(r'href="%s%s([a-z0-9-]+)/?"' % (re.escape(SITE), re.escape(BASE)))
ATAG = re.compile(r'<a[^>]+href="%s%s([a-z0-9-]+)/?"[^>]*>(.*?)</a>'
                  % (re.escape(SITE), re.escape(BASE)), re.S | re.I)


def _get(url):
    rq = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0",
                                              "Accept-Encoding": "gzip"})
    r = urllib.request.urlopen(rq, timeout=60)
    d = r.read()
    if r.headers.get("Content-Encoding") == "gzip":
        d = gzip.decompress(d)
    return json.loads(d.decode("utf-8", "replace"))


def all_posts(max_pages=20):
    """Toan bo bai da publish. REST tra 400 khi het trang, khong phai list rong."""
    out, page = [], 1
    while page <= max_pages:
        try:
            b = _get("%s?per_page=100&page=%d&_fields=id,slug,content&status=publish"
                     % (API, page))
        except urllib.error.HTTPError:
            break
        if not b:
            break
        out += b
        page += 1
    return out


def text_of(c):
    t = re.sub("&[a-z#0-9]+;", " ", re.sub("<[^>]+>", " ", c))
    return re.findall(r"[A-Za-z0-9,.%$-]+", t)


# ---------------------------------------------------------------- 1. anchor
def anchor_index(posts):
    """{slug_dich: [(post_id, anchor), ...]} tren toan site, bo link tu tro chinh no."""
    idx = collections.defaultdict(list)
    for p in posts:
        for sl, t in ATAG.findall(p["content"]["rendered"]):
            if sl == p["slug"]:
                continue
            idx[sl].append((p["id"], html.unescape(re.sub("<[^>]+>", "", t)).strip()))
    return idx


def anchors_to(idx, slug):
    """Moi anchor dang tro toi slug nay. Chay TRUOC khi viet anchor moi."""
    return [a for _, a in idx.get(slug, [])]


def anchor_report(idx, min_links=5, target=0.70):
    """Cac trang dich duoi muc da dang. Chi xet trang nhan >= min_links."""
    rows = []
    for sl, arr in idx.items():
        if len(arr) < min_links:
            continue
        uniq = len(set(a.lower() for _, a in arr))
        pct = uniq / len(arr)
        if pct < target:
            rows.append((pct, sl, len(arr), uniq))
    return sorted(rows)


# ---------------------------------------------------------------- 2. mo coi
def orphans(posts, idx, exclude=()):
    """Bai khong co inbound bien tap nao. exclude: slug stub/301 khong tinh."""
    return [p for p in posts
            if not idx.get(p["slug"]) and p["slug"] not in exclude]


# ---------------------------------------------------- 3. link dich khong 200
class _NoRedirect(urllib.request.HTTPRedirectHandler):
    def redirect_request(self, *a, **k):
        return None


_opener = urllib.request.build_opener(_NoRedirect)
_probe_cache = {}


def _probe(slug, tries=4):
    """(ma_http, slug_ke_tiep_neu_redirect). Co cache va co retry."""
    if slug in _probe_cache:
        return _probe_cache[slug]
    last = None
    for attempt in range(tries):
        try:
            r = _opener.open(urllib.request.Request(
                "%s%s%s/" % (SITE, BASE, slug),
                headers={"User-Agent": "Mozilla/5.0"}), timeout=40)
            out = (r.status, "")
            break
        except urllib.error.HTTPError as e:
            out = (e.code, e.headers.get("Location", "")
                   .replace(SITE + BASE, "").strip("/"))
            break
        except Exception as e:          # mang chap, connection reset
            last = e
            time.sleep(2 * (attempt + 1))
    else:
        raise RuntimeError("khong probe duoc %s sau %d lan: %s" % (slug, tries, last))
    _probe_cache[slug] = out
    return out


def check_targets(html_str, allow=()):
    """{slug: (ma_http_chang_dau, slug_dich_CUOI)} cho moi link noi bo khong tra 200.

    allow: slug duoc phep 404 vi bai do da len lich, se tu lanh.
    Go het chuoi redirect roi moi bao dich, vi co the co stub 2 hau.
    """
    bad = {}
    for sl in sorted(set(LINK.findall(html_str))):
        cur, code, first, hops = sl, None, None, 0
        while hops < 5:
            code, nxt = _probe(cur)
            if code in (301, 302, 307, 308) and nxt and nxt != cur:
                first = first if first is not None else code
                cur, hops = nxt, hops + 1
                continue
            if first is None and code != 200:
                first = code
            break
        if code == 200 and cur == sl:
            continue
        if code == 404 and sl in allow:
            continue
        bad[sl] = (first if first is not None else code, cur if cur != sl else "")
    return bad


# ---------------------------------------------------------------- 4. mat do
def density(c):
    words = len(text_of(c))
    links = len(set(LINK.findall(c)))
    return words, links, (links / words * 1000 if words else 0)


def link_density(posts):
    """Mat do link toan site so voi 'moi trang tro moi trang'. Nguong Mueller 2021.

    Tra (so_link_phan_biet, toi_da, phan_tram). Vai phan tram la binh thuong.
    """
    n = len(posts)
    tot = sum(len(set(LINK.findall(p["content"]["rendered"])) - {p["slug"]})
              for p in posts)
    mx = n * (n - 1)
    return tot, mx, (tot / mx * 100 if mx else 0)


def cluster_focus(posts, member, pillar_of):
    """Moi cum tro ve pillar nha bao nhieu %, so voi tro sang pillar cum khac.

    member    : {slug -> ten_cum} lay tu BANG PHAN CUM bien tap, khong suy tu link graph
    pillar_of : {slug_pillar -> ten_cum}
    Tra [(ten_cum, so_nha, so_khac, phan_tram_nha)], thap nhat truoc.
    Moc tu soi: >= 50%. Duoi moc thi THEM link ve pillar nha, dung go link cheo.
    """
    agg = collections.defaultdict(lambda: [0, 0])
    for p in posts:
        cum = member.get(p["slug"])
        if cum is None or p["slug"] in pillar_of:
            continue                      # bo qua bai chua gan cum va chinh pillar
        for t in set(LINK.findall(p["content"]["rendered"])):
            if t not in pillar_of:
                continue
            agg[cum][0 if pillar_of[t] == cum else 1] += 1
    out = [(c, a, b, (a / (a + b) * 100 if a + b else 0))
           for c, (a, b) in agg.items()]
    return sorted(out, key=lambda x: x[3])


if __name__ == "__main__":
    posts = all_posts()
    idx = anchor_index(posts)
    print("tong bai:", len(posts))

    print("\n=== trang duoi 70% da dang anchor ===")
    for pct, sl, n, u in anchor_report(idx):
        print("  %-50s %3d link / %3d anchor = %3.0f%%" % (sl, n, u, pct * 100))

    # Stub 301 cung hien ra nhu mo coi vi khong ai link toi, nhung do la dung y do.
    # Trang nao chinh no khong tra 200 thi khong phai mo coi that.
    stubs = {p["slug"] for p in posts if _probe(p["slug"])[0] != 200}
    print("\n=== bai mo coi (0 inbound bien tap, da tru %d stub) ===" % len(stubs))
    for p in orphans(posts, idx, exclude=stubs):
        print("  #%-6s %s" % (p["id"], p["slug"]))

    tot, mx, pct = link_density(posts)
    print("\n=== mat do link toan site ===")
    print("  %d / %d = %.1f%%  (vai %% la binh thuong)" % (tot, mx, pct))

    # Bo phan cum vao day de bat dau do; de trong thi bo qua buoc nay.
    MEMBER, PILLAR_OF = {}, {}
    if MEMBER and PILLAR_OF:
        print("\n=== ti le tro pillar nha (moc tu soi >= 50%) ===")
        for cum, a, b, pc in cluster_focus(posts, MEMBER, PILLAR_OF):
            print("  %-40s nha %3d / khac %3d = %3.0f%% %s"
                  % (cum, a, b, pc, "" if pc >= 50 else "<-- duoi moc"))

    print("\n=== link tro vao URL khong tra 200 ===")
    seen = {}
    for p in posts:
        for sl, info in check_targets(p["content"]["rendered"]).items():
            seen.setdefault((sl,) + info, []).append(p["id"])
    for k, ids in sorted(seen.items()):
        print("  %-50s %s -> %-40s tu %s" % (k[0], k[1], k[2] or "-", ids))
```

⚠️ **`_probe()` có cache và có retry, đừng bỏ hai thứ đó.** Khi quét toàn site, cùng một slug đích
bị dò lại ở hàng trăm bài. Không cache thì vừa chậm vừa gần như chắc chắn ăn `connection reset`
giữa chừng, và toàn bộ lần quét đó mất trắng. Đã xảy ra thật ngay lần chạy thử đầu tiên.

⚠️ **Hàm `all_posts()` bắt `HTTPError` chứ không chỉ kiểm tra list rỗng.** WordPress REST trả **400**
khi vượt quá số trang, không trả mảng rỗng. Quên chỗ này thì script chết giữa chừng.

⚠️ **`check_targets()` phải đo bằng HTTP, đừng đối chiếu với tài liệu nội bộ.** Xem Phần 9, lỗi số 3.

---

## 7. Kiểm tra định kỳ toàn site

Mỗi 10-15 bài publish, chạy script ở Phần 6 và nhìn 3 con số:

| Chỉ số | Diễn giải |
|---|---|
| Số bài **mồ côi** | Phải đi ngang hoặc giảm. Nếu nó tăng theo số bài publish thì bước inbound đang bị bỏ |
| Số trang **dưới 70% đa dạng anchor** | Phải giảm dần |
| Số **link trỏ vào URL không trả 200** | Phải bằng 0 |
| **% trỏ pillar nhà** của cụm thấp nhất | Phải >= 50%. Dưới mốc nghĩa là cụm đó đang nuôi pillar của cụm khác |
| **Mật độ link** toàn site | Vài phần trăm là bình thường. Chỉ đáng lo khi nó bò lên hai chữ số |

Khi đếm mồ côi, **loại các stub 301 ra khỏi danh sách**. Chúng xuất hiện như mồ côi vì không ai link
tới, nhưng đó là đúng ý đồ: không được link vào stub.

---

## 8. Danh sách nguồn CẤM dùng làm ngưỡng

Liệt kê để lần sau không ai vô tình trích lại. **Cả sáu từng được dùng làm ngưỡng cứng** trong một
quy trình production trước khi bị gỡ.

| Nguồn | Từng dùng làm gì | Vấn đề |
|---|---|---|
| AirOps "3-5 link mỗi 1.000 chữ" | ngưỡng cứng gác script | blog vendor, không có Google chống lưng |
| Wellows "1 link mỗi 200-300 chữ" | như trên | như trên |
| LinkWhisper "20-40 link cho pillar" | áp lên pillar 1.832 chữ rồi kết luận nhầm "thiếu link" | như trên, lại còn là số tuyệt đối |
| eesel "2-3 link ngang mỗi cluster" | như trên | như trên |
| [Reasonable surfer patent US8117209B1](https://patents.google.com/patent/US8117209B1/en) | chống lưng cho bảng xếp hạng giá trị link theo vị trí | nộp 2004, Google **chưa bao giờ xác nhận** đang chạy theo nó |
| Headline SEJ 2020 "Links in Primary Content Hold More Value" | như trên | **suy diễn của tác giả**. Mueller chỉ nói Google tập trung vào primary content, không nhắc link, ranking hay PageRank |

Đây đúng loại nguồn mà quy trình biên tập vẫn gỡ khỏi bài publish, nên không được dùng để gác script.

**Một nguồn hay bị trích sai theo chiều ngược lại:** nghiên cứu internal link của Zyppy (23 triệu
internal link, 1.800 site, 520 nghìn URL). Nó đo **inbound**, không đo outbound, nên đừng dùng nó để
biện minh cho một ngưỡng "bao nhiêu link mỗi bài".

---

## 9. Những lỗi đã xảy ra thật

Phần này đáng đọc nhất, vì mỗi lỗi đều **tốn công sửa lại** và đều có vẻ hợp lý lúc mắc phải.

**1. Quy trình tự tạo ra lỗi anchor trùng.** Skill bắt buộc anchor phải chứa keyword pillar. Kết quả:
35 link dùng y hệt một chuỗi. Lỗi không nằm ở người viết mà ở chính quy tắc. Khi thấy một lỗi lặp lại
đều đặn, nghi quy trình trước khi nghi người thực thi.

**2. Chỉ kiểm tra pillar nên bỏ sót trang non-pillar.** Check đa dạng anchor chỉ chạy trên pillar.
Một trang non-pillar nhận 5 link với 1 anchor duy nhất lọt lưới nhiều tháng.

**3. Đối chiếu với tài liệu thay vì đo bằng HTTP.** Dựng danh sách stub 301 bằng cách grep chữ
"merge"/"301" trong file kế hoạch nội bộ. Kết quả: báo **10 link hỏng** trong khi thật ra là **26**,
và kê oan một trang đang sống thành stub. **Tài liệu luôn trễ hơn site; mã HTTP trả về thì không.**

**4. Chỉ gỡ một hầu của chuỗi redirect.** Script in ra đích của hầu đầu tiên, mà đích đó cũng là stub.
Sửa theo nó là rơi vào stub khác. Phải gỡ hết chuỗi rồi mới báo đích cuối.

**5. Regex chỉ bắt nháy kép.** `href="..."` bỏ sót `href='...'`. WordPress xuất stylesheet bằng
**nháy đơn**. Hệ quả: một phép đo trả về "0 stylesheet", từ đó kết luận sai về CSS của theme, rồi
"sửa" một bài thành chữ trắng trên nền sáng (tương phản 1,10:1, tệ hơn trước khi sửa). Người dùng
phải gửi ảnh chụp màn hình mới phát hiện. **Luôn dùng `["\']` trong regex HTML, và kiểm tra số kết
quả có khác 0 không trước khi tin bất cứ phép đo nào.**

**6. Tin thông báo "thành công" của API.** Một quy tắc CSS được kê trong skill suốt nhiều tháng
nhưng **chưa bao giờ có tác dụng**, vì WordPress lọc thuộc tính đó khi lưu mà vẫn báo lưu thành công.
**Luôn đọc lại qua API sau khi ghi**, đừng tin thông báo.

**7. `assert` chạy sau publish làm chết bước ghi log.** Bài đã lên site nhưng không được ghi vào
tracker, lần sau không ai biết nó tồn tại. Mọi check hậu publish phải gom vào `warnings`.

**8. Đếm `grep -c` (số dòng) và tưởng là số lần xuất hiện.** Dẫn tới một báo cáo sai về việc "đã thêm
2 em dash". Khi đếm, dùng công cụ đếm đúng thứ mình muốn đếm.

**9. Suy ra thành viên cụm từ link graph.** Xem cảnh báo ở Phần 2.

**Mẫu số chung của 3, 5, 6:** tin vào một lớp trung gian (tài liệu, regex tự viết, thông báo của API)
thay vì đo thứ thật. Trước khi tin một con số, hỏi: con số này đến từ đâu, và nếu công cụ đo của tôi
hỏng thì nó sẽ ra bao nhiêu? Nếu câu trả lời là "ra 0" hoặc "ra chính con số tôi đang thấy", đi kiểm
tra công cụ đo trước.

---

## 10. Thiết lập cho một site mới

1. **Vẽ bảng phân cụm trước khi viết bài nào.** Mỗi cụm: 1 pillar + danh sách cluster, mỗi bài một
   keyword riêng. Đây là nguồn sự thật duy nhất về "bài nào thuộc cụm nào", không suy từ link graph.
2. **Chạy script Phần 6 ngay khi có khoảng 20 bài** để lấy đường cơ sở. Ghi lại 3 con số ở Phần 7.
3. **Đo lại phân bố mật độ link của chính site** rồi thay mốc ở Phần 4 bằng số thật. Mốc "lệch hẳn
   so với phần còn lại" chỉ có nghĩa khi bạn biết phần còn lại là bao nhiêu.
4. **Gắn `check_targets()` vào quy trình publish**, trước khi tạo bài, không phải sau.
5. **Đặt lịch chạy lại Phần 7** mỗi 10-15 bài.

Thứ tự ưu tiên khi dọn một site đã có sẵn nhiều bài:

| Thứ tự | Việc | Vì sao trước |
|---|---|---|
| 1 | Link trỏ vào URL không trả 200 | Rẻ nhất, lỗi rõ ràng, không cần quyết định biên tập |
| 2 | Bài mồ côi | Chặn rò rỉ, và mỗi bài mới không sửa sẽ thành món nợ mới |
| 3 | Anchor trùng trên pillar | Khối lượng lớn, cần viết lại từng câu |
| 4 | Anchor trùng trên trang non-pillar | Như trên, ít ảnh hưởng hơn |

Bài lạc chủ đề (không thuộc cụm nào) là **quyết định nội dung, không phải việc fix link**. Ép link về
pillar không liên quan thì vừa gượng vừa làm loãng cấu trúc, đúng cái Mueller cảnh báo. Ba lựa chọn:
để nguyên và chấp nhận mồ côi, gom thành một cụm riêng có pillar riêng, hoặc noindex.
