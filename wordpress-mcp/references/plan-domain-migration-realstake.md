# Plan SEO: chuyển domain `infina.ai` → `realstake.ai`

Soạn 15/10/2026. Quyết định của sếp: đổi tên sản phẩm thành **realstake.ai** và **đổi cả domain**. File này là checklist cho
SEO (Claude), dev và người phụ trách. Dữ liệu lấy trực tiếp từ site ngày 15/10 (REST, sitemap, repo). Không có con số cam kết
về mức tụt hay thời gian hồi phục: Google không đưa ra, kết quả phụ thuộc việc làm đúng các bước dưới đây.

## 0. Câu hỏi cần sếp chốt TRƯỚC khi làm (chặn mọi bước sau)

| # | Câu hỏi | Vì sao quan trọng |
|---|---|---|
| 1 | **Toàn bộ `infina.ai` chuyển sang `realstake.ai`, hay chỉ sản phẩm bất động sản + blog?** Root hiện có 8 URL (`/`, `/vn`, `/inside`, `/work`, `/personal`, `/about`, `/focus-alignment`, `/careers`) trông như site công ty | Nếu chuyển cả domain thì dùng được công cụ Change of Address của GSC. Nếu chỉ chuyển một phần thì không dùng được, và phải redirect từng URL |
| 2 | Tên hiển thị và cách viết: `RealStake AI`, `Realstake AI` hay `realstake.ai`? | Phải thống nhất trước khi đổi nội dung (20 bài nhắc tên, schema, alt, anchor) |
| 3 | Blog giữ đường dẫn `/news/` trên domain mới? | Giữ nguyên đường dẫn thì map URL 1-1 đơn giản nhất. **Khuyến nghị giữ** |
| 4 | Domain `realstake.ai` đã mua, đã trỏ DNS, từng có lịch sử gì? | Domain cũ từng bị spam hoặc bị phạt sẽ kéo cả site. Cần kiểm trước (Wayback, GSC, backlink) |
| 5 | Ngày chuyển dự kiến | Nên tránh tuần đang đẩy bài mới. Wave 3 lên lịch 19-21/10 |
| 6 | Domain cũ `infina.ai` còn dùng cho thương hiệu Infina khác (app, email, fintech) không? | Nếu còn dùng thì redirect chỉ áp cho phần chuyển, và vẫn phải giữ domain cũ |

## 1. Hiện trạng đo được (15/10/2026)

| Hạng mục | Số liệu |
|---|---|
| Bài blog đã publish | 159 (thêm 25 bài Cụm 9 đang lên lịch 14-21/10) |
| URL gốc trong sitemap `infina.ai/sitemap.xml` | 8 |
| Link nội bộ tuyệt đối `https://infina.ai/news/...` trong nội dung bài | **1.061** link trong 148 bài |
| Link tới money page `https://infina.ai/` trong bài | 20 |
| URL ảnh tuyệt đối `infina.ai/news/wp-content/...` trong bài | **514** |
| Bài nhắc tên "Infina" trong thân bài | 20 (danh sách ở `files/domain-migration/posts-mention-infina-brand.csv`) |
| Tác giả bài | 1 user "Infina AI" (schema `Person` tên Infina AI) |
| File trong repo hardcode `infina.ai` | trang tĩnh `home.html`, `about.html`, `inside.html`, `personal.html`, `nav.js`, `footer.js`, theme `wordpress-theme/infina-ai-news` (header/footer/templates), `ghost-theme`, `static-news`, nhiều file doc |
| Bản đồ URL cũ → mới (giả định giữ đường dẫn) | `files/domain-migration/url-map.csv` (167 dòng) |

Vì mọi bài tôi viết dùng URL tuyệt đối, **search-replace ở tầng database** là cách duy nhất hợp lý. Bài đang lên lịch (`future`) nằm trong
cùng database nên được thay luôn. Không cập nhật từng bài qua công cụ MCP.

## 2. Nguyên tắc

1. Mỗi URL cũ 301 sang **đúng URL tương ứng** trên domain mới. Không dồn về trang chủ.
2. Giữ nguyên đường dẫn, slug, title, nội dung chính. **Không đổi nội dung SEO trong cùng đợt chuyển** (chỉ đổi tên thương hiệu, domain, canonical). Đổi nhiều thứ cùng lúc sẽ không biết nguyên nhân nếu tụt.
3. Redirect ở tầng server hoặc CDN, một bước, không chuỗi (`http`/`www`/domain cũ → đích cuối, đúng 1 hop).
4. Giữ redirect và quyền sở hữu domain cũ ít nhất 1 năm, nên giữ vô thời hạn.
5. Cho Google thấy tín hiệu đồng nhất: canonical, sitemap, link nội bộ, hreflang đều trỏ domain mới.

## 3. Giai đoạn 0: chuẩn bị (T-3 đến T-1 tuần)

- [ ] Sếp chốt 6 câu hỏi ở mục 0.
- [ ] **Baseline GSC:** export 16 tháng pages + queries của `infina.ai` (CSV) để so sau chuyển. Lưu vào `files/domain-migration/baseline/`.
- [ ] **Baseline vị trí và AI Overview:** danh sách top query và screenshot AI Overview (như bài #438 đang được trích), vì sau chuyển nguồn trích sẽ đổi tên.
- [ ] Kiểm `realstake.ai`: Wayback Machine, `site:realstake.ai`, backlink lạ, SSL, DNS. Đăng ký GSC property **Domain** cho cả hai domain (cần quyền DNS).
- [ ] Audit backlink của `infina.ai` (GSC > Links, bất kỳ tool nào có sẵn). Danh sách link ngoài quan trọng cần nhờ cập nhật sau chuyển.
- [ ] Hạ DNS TTL của `infina.ai` xuống thấp trước ngày chuyển 48 giờ.
- [ ] Liệt kê mọi nơi dùng domain: GA4 data stream, Clarity, Google Ads, email (link trong template), social profile, app store, CRM, form webhook, Zapier, Cloudflare, sitemap ping, Rank Math redirects, nhà cung cấp OAuth.
- [ ] Quyết định có đóng băng đăng bài mới trong tuần chuyển không (khuyến nghị: không đặt lịch bài trong ±3 ngày quanh ngày chuyển).

## 4. Giai đoạn 1: staging (dev + SEO)

- [ ] Dựng bản sao trên staging với domain mới, **`noindex` và chặn robots**. Ghi vào checklist: bắt buộc gỡ `noindex` ở bước cutover.
- [ ] WordPress: `wp search-replace 'https://infina.ai' 'https://realstake.ai' --all-tables --precise` (an toàn với dữ liệu serialize), kiểm cả `siteurl`, `home`, GUID bảng ảnh, option của Rank Math, widget/menu.
- [ ] Theme `wordpress-theme/infina-ai-news` (header, footer, templates, style) và trang tĩnh trong repo: thay domain và tên thương hiệu.
- [ ] **Schema** (Rank Math > Titles & Meta > Local SEO / Organization): tên mới, logo, URL, `sameAs`; thêm `alternateName: "Infina AI"` trong giai đoạn đầu để Google nối hai tên. Cập nhật tác giả Person (tên, URL `/news/author/...`).
- [ ] Canonical, `og:url`, `og:site_name`, `twitter:site`, title template có tên thương hiệu (suffix `| Infina AI`) đều sang tên mới.
- [ ] **Sitemap:** `sitemap.xml` (8 URL) và `news/sitemap_index.xml` sinh URL domain mới. `robots.txt` trỏ sitemap mới.
- [ ] **hreflang** (`/vn` và bản EN): cập nhật cặp domain mới, đảm bảo tự tham chiếu đúng.
- [ ] Lập luật redirect ở server/CDN (mẫu nginx):
  ```nginx
  server { server_name infina.ai www.infina.ai;
           return 301 https://realstake.ai$request_uri; }
  ```
  Rồi test mọi dòng `url-map.csv` (script kiểm: HTTP 301, đích đúng, 1 hop, đích trả 200). Gồm cả **ảnh** `wp-content/uploads` và `wp-json` nếu có tích hợp.
- [ ] Chạy crawl staging (Screaming Frog hoặc script `competitor_teardown.py` của repo): không còn link tới `infina.ai`, không 404, không chuỗi redirect, canonical đúng.

## 5. Giai đoạn 2: ngày chuyển (cutover)

Thứ tự quan trọng:

1. Gỡ `noindex` và robots chặn trên domain mới.
2. Bật redirect 301 từ `infina.ai` sang `realstake.ai`.
3. Chạy lại script kiểm 167 URL + ảnh. Mọi dòng phải đạt.
4. GSC: submit sitemap mới trong property `realstake.ai`.
5. GSC: property `infina.ai` > Settings > **Change of Address** > chọn `realstake.ai` (chỉ khi đã chốt chuyển toàn bộ domain ở câu 1). Công cụ chỉ chấp nhận khi redirect đã chạy.
6. Request Indexing cho khoảng 10 URL quan trọng nhất (money page, pillar #1825, hub #1832, bài có traffic).
7. Cập nhật kết nối công cụ (xem mục 7).

## 6. Giai đoạn 3: sau chuyển (4-8 tuần)

| Việc | Tần suất | Dấu hiệu cần xử lý |
|---|---|---|
| Coverage và crawl stats trên property mới | 2 ngày đầu mỗi ngày, rồi hằng tuần | URL "Crawled/Discovered, currently not indexed" tăng, 5xx, redirect error |
| Impressions và clicks (so baseline) | Hằng tuần | Giảm sâu và kéo dài quá vài tuần |
| Index trên `site:realstake.ai` và `site:infina.ai` | Hằng tuần | Domain cũ vẫn giữ nhiều URL sau nhiều tuần |
| Brand query `realstake`, `infina ai` | Hằng tuần | Không hiện trang mới sau 3-4 tuần |
| AI Overview của top query (nguồn trích) | 2 tuần | Nguồn trích đổi tên, hoặc mất trích dẫn |
| Backlink: nhờ cập nhật link của 20-30 nguồn quan trọng | Liên tục | Link vẫn trỏ domain cũ |
| Trang About / money page nêu "RealStake AI (formerly Infina AI)" | Giữ ít nhất 6-12 tháng | - |

Kế hoạch lùi: giữ cấu hình cũ sẵn sàng; chỉ gỡ redirect khi đã xác nhận lỗi không sửa được, và không bao giờ bỏ domain cũ.

## 7. Công cụ, script và file nội bộ phải cập nhật

| Nơi | Việc |
|---|---|
| **Kết nối WordPress MCP** (`update_post`, `list_posts`, `create_post`) | Endpoint hiện nằm trên `infina.ai/news/wp-json`. Sau chuyển phải đổi URL kết nối và khóa. Kiểm lại ngay sau cutover |
| `SEO_GSC_SITE_URL` | `https://infina.ai/news/` → property mới. Service account `search-console-api@...` phải được thêm vào property mới (Settings > Users) |
| `scripts/gsc_client.py`, `ga4_client.py` | Đổi site URL, kiểm quyền GA4 |
| Skills: `pillar-cluster-writer`, `news-to-cluster-article`, `post-refresh` | Quy tắc "money page `https://infina.ai/`", slug tuyệt đối `https://infina.ai/news/<slug>/`, ví dụ trong playbook |
| `used-keywords.md`, `content-plan.md`, `teardown-infina-table.md`, `tracker-rows-cum9.tsv` | URL cột tracker (164 dòng). Sheet Google "Published article" cần thay hàng loạt (Find and replace) |
| 6 trigger chèn ảnh + trigger 21/10, 18/10 | Các prompt có URL `infina.ai`. Cập nhật trước ngày chuyển |
| `mockups-cum9/spec.json` | URL ảnh tuyệt đối trong `media` |
| `render_snapshot.py`, `external-seo-toolkit` | Domain mặc định |

## 8. Đổi tên thương hiệu trong nội dung (làm cùng đợt, tách khỏi SEO nội dung)

- 20 bài có câu "Infina AI, our own product, is an AI assistant for real estate agents" và anchor money page. Thay theo tên đã chốt ở câu 2.
- 8 bài Wave 3 và các bài Cụm 9 chưa publish có cùng câu; đợt search-replace DB và một pass đổi tên sẽ phủ cả bài `future`.
- Tên tác giả hiển thị "Infina AI" → tên mới. Khi có người thật đứng tên (đã ghi nhận: để sau), làm một lần.
- `alt` ảnh và schema nếu có tên cũ. `og:site_name`. Favicon và logo nếu đổi.
- Giữ cụm "(formerly Infina AI)" ở trang About và money page một thời gian.
- Ảnh sản phẩm hoặc mockup có chữ "Infina" (kiểm trong `mockups-cum9/final`): mockup hiện dùng tên giả, không bị ảnh hưởng.

## 9. Việc giao

| Ai | Việc |
|---|---|
| **Sếp** | Chốt mục 0 (6 câu), cấp domain, quyền DNS, quyết định tên hiển thị |
| **Dev** | Staging, search-replace DB, theme và trang tĩnh trong repo, redirect server/CDN, sitemap, robots, hreflang, SSL, đổi cấu hình WordPress |
| **SEO (Claude)** | Baseline GSC, bản đồ URL, script kiểm redirect và crawl, danh sách bài đổi tên, cập nhật skill và doc nội bộ, theo dõi sau chuyển, báo cáo hằng tuần |
| **Bạn** | Sheet tracker (Find and replace), nhờ cập nhật backlink, thông báo kênh social, GA4/Clarity/Ads |

## 10. Lịch đề xuất (nếu cutover vào ngày D)

| Mốc | Việc |
|---|---|
| D-14 | Sếp chốt mục 0, mua và kiểm domain, baseline GSC |
| D-10 | Dev dựng staging, chạy search-replace thử |
| D-5 | Crawl staging, sửa lỗi, kiểm redirect map, cập nhật skill/trigger |
| D-2 | Hạ TTL, đóng băng đặt lịch bài trong tuần chuyển |
| D | Cutover theo mục 5 |
| D+1 đến D+7 | Kiểm hằng ngày, Request Indexing, báo cáo |
| D+28 | Báo cáo so baseline, quyết định bước tiếp |

## 11. Rủi ro chính

1. **Tụt tạm thời** lượng truy cập: có thể xảy ra, không có con số bảo đảm.
2. **Quên một nhóm URL** (ảnh, `/vn`, tác giả, feed) → 404. Chống bằng script kiểm toàn bộ map và crawl.
3. **Link nội bộ vẫn trỏ domain cũ** → redirect chain, chậm index. Chống bằng search-replace và crawl sau.
4. **Mất nguồn trích AI Overview** dưới tên mới trong một thời gian.
5. **Công cụ tự động gãy** (MCP, GSC, trigger) vì domain cũ. Mục 7 là danh sách cần xử lý trước ngày D.
6. **Trùng thời điểm** với đợt đăng bài mới hoặc sửa nội dung lớn → khó tìm nguyên nhân khi tụt.
