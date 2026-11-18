# ReallyWise: tổng hợp việc crawl email realtor (đến 2026-11-13)

> **Kết luận ngắn:** chưa crawl được danh sách email nào dùng được. Chỉ có một danh sách đại lý mới có license (DRE, 282 dòng, **không có email**) và vài lần chạy thử nhỏ trên Apify. **Chưa chạy** actor nào cho group Facebook hay Reddit.

---

## 1. Những gì đã thực sự chạy

### 1.1 Nguồn dữ liệu miễn phí: DRE California (đại lý mới có license)
- **File chính thức:** `https://secure.dre.ca.gov/datafile/new_licensees.xls` (DRE cập nhật mỗi thứ Hai, tải miễn phí).
- **Đã tải và chuyển sang CSV:** 282 dòng, ngày cấp license 2026-11-03 đến 2026-11-06.
  - Gồm 224 Salesperson, 24 Officer, 19 Corporation, 15 Broker.
  - 217 trong 224 Salesperson có địa chỉ tại CA. 163 người là "Licensed NBA" (chưa gắn broker, địa chỉ nhiều khả năng là nhà riêng). 61 người có gắn broker hoặc công ty (55 broker/công ty khác nhau).
- **Có:** tên, số license, loại và trạng thái license, ngày cấp, địa chỉ gửi thư, thành phố, county, ZIP, broker liên kết.
- **Không có:** email, số điện thoại.
- **Cột `email` trong CSV: 0/282 có dữ liệu.**
- File: `/tmp/claude-0/-home-user-Web-Infina-AI/8904b2f3-570f-5b4a-8b6e-10de19b9d66c/scratchpad/dre_new_licensees_2026-11-03_to_06.csv` (cũng đã gửi bạn dưới dạng file đính kèm).
- Lưu ý từ trang DRE: địa chỉ "provided for reference only and not intended for mass mailing purposes".

### 1.2 Các lần chạy Apify (bằng key trong biến môi trường `Apify_key`)

| # | Actor | Cách dùng | Kết quả | Chi phí |
|---|---|---|---|---|
| 1 | `j0401/ca-dre` (tra cứu license DRE) | Thử 20 record Salesperson, lọc Licensed | Trả về theo số license tăng dần (cũ nhất trước), không có bộ lọc theo ngày cấp. Có 208,406 salesperson đang licensed. Không có email | khoảng $0.001 |
| 2 | `get-leads/real-estate-agent-scraper` (nguồn Google Maps + website của agent) | 10 truy vấn "tên + real estate agent + thành phố" cho 10 đại lý mới nhất trong file DRE | 23 kết quả, 11 có email. **0/10 người mục tiêu** được tìm thấy. Email là của đại lý khác, **không dùng** | $0.069 |
| 3 | `nexgendata/person-business-email-finder` | 8 người (tên + broker công ty) | **0 dòng kết quả** (chưa rõ nguyên nhân, có thể do cách nhập) | $0.005 |
| 4 | `j0401/ca-dre` (chế độ profile) | Tra license của một listing agent (lấy từ listing Zillow) | Xác nhận loại license, ngày cấp, hạn và broker. Không có email | gần như $0 |
| 5 | `get-leads/real-estate-agent-scraper` | 2 truy vấn tên agent + brokerage + thành phố | 6 kết quả, **không có đúng agent cần tìm**, chỉ có người khác trùng tên (email của người khác, không dùng) | khoảng $0.02 (ước tính) |
| 6 | `nexgendata/person-business-email-finder` | tên agent + domain của brokerage | Chỉ ra **địa chỉ đoán theo mẫu** (first.last, firstlast, flast, first) tại domain của brokerage. Độ tin cậy "domain-only", **chưa xác minh** hộp thư (cổng kiểm tra 25 bị đóng) | không bị tính phí kết quả |

**Tổng chi phí Apify do tôi chạy:** khoảng $0.1 (lần 1 đến 3 tổng $0.075 đã xác nhận, lần 4 đến 6 ước tính khoảng $0.03).

### 1.3 Kết quả thực tế
- **Email dùng được: 0.**
- **Group Facebook: chưa crawl.**
- **Reddit (r/realtors hoặc subreddit khác): chưa crawl.** Tôi cũng không mở được trang reddit.com để xem nội dung subreddit.
- **Google Maps:** chỉ có 2 lần chạy thử nhỏ (mục 2 và 5), không có lần crawl theo khu vực nào.
- **Import vào Brevo:** chưa import contact nào. Brevo hiện có 3 list gần như trống.

---

## 2. Các cách crawl đã thử và nhận xét

| Cách | Đã làm | Nhận xét |
|---|---|---|
| Danh sách đại lý mới từ DRE (file miễn phí) | Đã tải và xuất CSV | Nguồn tin cậy, miễn phí, cập nhật hàng tuần, nhưng không có email |
| Tên + thành phố tìm trên Google Maps rồi lấy email từ website | Đã thử 2 lần | Chỉ tìm được đại lý đã hoạt động và có trang riêng. Với người mới có license (chưa có website), tỉ lệ trúng 0/10 |
| Tên + broker rồi đoán email theo mẫu | Đã thử 2 lần | Lần 1 không ra kết quả. Lần 2 chỉ ra địa chỉ đoán, chưa xác minh, không an toàn để gửi |
| Tra số license trên DRE | Đã thử | Xác nhận danh tính và broker, không cho email |
| Tìm web theo tên, số license, brokerage | Đã thử cho một agent cụ thể | Không ra hồ sơ phù hợp |

---

## 3. Các actor đã tìm thấy nhưng **chưa chạy**

**Reddit (README đã đọc qua tìm kiếm, chưa chạy):**
- `blackfalcondata/reddit-email-scraper`: nhận link subreddit (ví dụ `https://www.reddit.com/r/realtors/`), quét tiêu đề, nội dung bài, bình luận, bio công khai và `mailto:`. Giá $0.002 mỗi record có email + $0.008 mỗi lần khởi động. Đề xuất dùng trước.
- `pro100chok/reddit-scraper-all-in-one`: đọc bio của người dùng rồi vào tối đa 5 website được liên kết để lấy email. Khoảng $0.002 mỗi kết quả.
- `avinashchby/reddit-community-leads`: chỉ đọc bio của người đăng gần đây, cần proxy dân cư, chưa có đánh giá. Không khuyên dùng.
- Lưu ý: Reddit không có trường email, nên email chỉ có khi người dùng tự viết vào bài hoặc bio.

**Facebook (chưa chạy, chưa có actor đi thẳng từ group ra email):**
- `scraply/facebook-group-member-scraper`, `delectable_incubator/facebook-group-member-scraper-low-cost`: lấy danh sách thành viên và link profile, cần đăng nhập hoặc cookie Facebook, không xuất email.
- `scraperoka/facebook-email-scraper`, `scraper-mind/facebook-email-scraper`: lấy email từ bio và bài đăng công khai theo từ khóa, không đi từ group.
- Cách làm gián tiếp: lấy link profile từ group rồi chạy bộ trích email. Hầu hết profile cá nhân không để email công khai. Rủi ro cao: Facebook cấm scraping và dễ khóa tài khoản dùng cookie.

**Các actor khác từ kết quả tìm (chưa đọc kỹ, chưa chạy):**
- Realtor/Zillow: `realtorscraper/realtor-agents-scraper-with-email` (tra theo ID), `contactminerlabs/realtor-email-scraper`, `propertyapi/realtor-agent-email-finder`, `scraperoka/real-estate-agent-email-scraper`, `contacts-api/real-estate-agent-email-scraper`, `scrapedrift/zillow-b2b-email-scraper`.
- Tìm email theo tên và domain: `ryanclinton/waterfall-contact-enrichment`, `clearpath/email-finder-api`, `automation-lab/email-finder`.
- Chưa thử dịch vụ tra ngược theo địa chỉ (skip trace).

---

## 4. Việc khác liên quan (không phải crawl)
- **Danh sách "Zillow Detail Scraper"** trong lịch sử Apify (nhiều lần chạy $0.003 từ 3/11 đến 11/11) **không phải do tôi chạy**. Có thể do team thử sản phẩm hoặc trang tạo Property Expert gọi. Tôi chưa kiểm chứng.
- **SMS:** đã trao đổi, không khuyên gửi SMS marketing lạnh tới số từ listing vì TCPA (xem lần trả lời trước).
- **Brevo:** chính sách chống spam của Brevo cấm danh sách thu thập (scraped) hoặc mua cho cả email, SMS, WhatsApp. Bạn đã biết và quyết định.

---

## 5. Gợi ý bước tiếp theo
1. **Crawl theo khu vực bằng actor Google Maps** (`get-leads/real-estate-agent-scraper`, $0.003 mỗi lead): đưa thành phố hoặc ZIP, không đưa từng tên. Lần thử nhỏ thấy 11/23 có email (khoảng 48%, mẫu quá nhỏ). Ra đại lý đã hoạt động, không phải người mới có license.
2. **Chạy thử Reddit:** `blackfalcondata/reddit-email-scraper` trên r/realtors, giới hạn nhỏ (ví dụ 100 record) để đo tỉ lệ ra email trước khi chạy lớn.
3. **Bỏ qua group Facebook** trừ khi có cách chắc chắn và chấp nhận rủi ro tài khoản.
4. **Xác minh email trước khi gửi** (kể cả khi đoán theo mẫu), để tránh bounce.
5. Cần email gắn với listing mới của agent: lấy từ Zillow/MLS thông tin agent (tên, số license, brokerage) rồi tìm email qua website hoặc profile công khai, như đã thử cho một agent cụ thể (chưa ra).

---

## 6. File dữ liệu
Các file dữ liệu (CSV 282 đại lý mới của DRE, kết quả thô của các lần chạy) chứa thông tin cá nhân của người khác nên **không** nằm trong repo. Xem `data/README.md` để biết cách tạo lại CSV DRE bằng script.
