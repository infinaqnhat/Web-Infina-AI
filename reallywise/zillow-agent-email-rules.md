# Rule: lấy email listing agent từ link Zillow

Cập nhật: 2026-11-13. Script: `reallywise/scripts/zillow_agent_emails.py`.

## 1. Mục tiêu
Từ một link listing Zillow (`zillow.com/homedetails/.../<zpid>_zpid/`), lấy listing agent và email **công khai** của agent đó.

## 2. Chạy nhanh
```bash
export Apify_key=...
python3 reallywise/scripts/zillow_agent_emails.py links.txt -o agents.csv
```
- `links.txt`: mỗi dòng một link. Link có `?utm_...` vẫn dùng được.
- `--max-cost`: trần chi phí USD mỗi bước (mặc định 1.0).
- `--no-google`: bỏ bước dự phòng tìm Google.
- Cột CSV: `listing_url, zpid, address, agent_name, agent_phone, license, brokerage, profile_url, email, email_source, status`.

## 3. Quy trình 3 bước (thứ tự bắt buộc)

| Bước | Actor | Đầu vào | Đầu ra |
|---|---|---|---|
| 1 | `trakk/zillow-scraper`, `mode: "DETAIL"` | link listing | tên agent, số điện thoại, license, brokerage, `profile_url` Zillow |
| 2 | `parsebird/zillow-agent-leads-finder`, `enrichEmails: true` | `startUrls` là profile Zillow | email công khai trên profile hoặc website của agent |
| 3 (dự phòng) | `apify/google-search-scraper` | "tên + brokerage + license + email" | email trong kết quả tìm kiếm (thường là trang agent của brokerage) |

Chỉ chuyển sang bước sau khi bước trước không ra email.

## 4. Quy tắc khi chạy
1. **Luôn xuất phát từ listing agent**, không đoán người khác. Không dùng email của agent trùng tên hoặc cùng khu vực.
2. **Bước 2: mỗi profile chạy một lần**, dù nhiều listing cùng agent.
3. **Bước 3: gom tất cả agent thiếu email vào một lần chạy.** Apify yêu cầu trần chi phí tối thiểu $0.5 cho actor này, nên chạy lẻ từng người rất phí.
4. **Bước 3 chỉ nhận email** nằm trong kết quả có chứa họ của agent, và bỏ email chung (`info@`, `contact@`, `support@`, `admin@`, `sales@`...).
5. Email ưu tiên theo thứ tự: profile Zillow, website riêng của agent, trang agent của brokerage.
6. Dòng có `email_source = google_search` phải được kiểm tra tay trước khi dùng (mở URL nguồn trong `status`).
7. Không dùng địa chỉ **đoán theo mẫu** (ví dụ `ten.ho@brokerage.com`) và không dùng email DRE. Chỉ dùng email do agent hoặc brokerage tự công khai.

## 5. Lỗi thường gặp
- **`scrapersdelight/zillow-agent-leads-scraper` với `startUrls` trả 0 dòng.** Phải truyền `zpids` thay vì link. Actor này hay trả `agentEmail: null` nên không dùng làm bước chính.
- **Zillow không đưa email vào listing** (`mustDisplayAttributionListAgentEmail = False`). Vì vậy bước 1 chỉ cho tên, điện thoại, license, brokerage.
- **Tên profile lệch.** Zillow có thể trả `screenName` là `Alma Realtor` trong khi link là `Alma-Realtor`. Script đã bỏ ký tự đặc biệt trước khi so khớp. Nếu tự viết lại, phải làm tương tự.
- **Listing không có profile agent** (ví dụ phân khúc cao như Atherton). Bước 2 bị bỏ qua, chuyển sang bước 3.
- **Trang brokerage chặn tự động** (`ggsir.com` trả 202 rỗng, `sothebysrealty.com/eng/agents` trả 405). Không fetch trực tiếp, dùng Google Search Scraper.
- **`intelscrape/real-estate-listing-scraper` bị FAILED** khi thử. Không dùng.
- `apify/google-search-scraper` báo lỗi nếu đặt trần chi phí dưới $0.5.
- Tìm theo tên trên `afanasenko/zillow-agent-leads-scraper` hoặc `parsebird` (`agentName`) có thể ra agent khác. Không dùng email của họ.

## 6. Kết quả đã kiểm chứng (5 link, 2026-11-13)
| Agent | Cách lấy | Kết quả |
|---|---|---|
| Lauren Regan (eXp, Antioch) | profile Zillow | có email |
| Alma Hodzic (eXp, Antioch) | profile Zillow | có email |
| Johnny Heckenberg (Coldwell Banker, San Mateo) | profile Zillow | có email |
| Ted Bartlett (Compass, San Francisco) | profile Zillow | có email |
| Christopher Mogensen (Golden Gate Sotheby's, Atherton) | Google, không có profile Zillow | có email, cần kiểm tra |

Mẫu nhỏ (5), đều ở Bay Area. Chưa đủ để ước tỉ lệ ra email chung.

## 7. Chi phí tham khảo
- Bước 1 và 2: vài cent mỗi link, chưa kiểm tra số chính xác.
- Bước 3: tối thiểu khoảng $0.5 mỗi lô, bất kể lô có bao nhiêu agent.

## 8. Tuân thủ
- Chỉ dùng email công khai. Cần **xác minh email** (bounce check) trước khi gửi.
- Brevo cấm danh sách thu thập (scraped) hoặc mua cho email, SMS và WhatsApp. Cân nhắc trước khi import vào Brevo.
- Với SMS lạnh tới số từ listing, lưu ý TCPA. Không khuyên gửi.
- Địa chỉ trong file DRE ghi rõ không dùng cho gửi thư hàng loạt.
