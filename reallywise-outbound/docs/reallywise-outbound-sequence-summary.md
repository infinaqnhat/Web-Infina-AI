# ReallyWise: tóm tắt chuỗi email outbound cho listing agent (option A: 3 email, option B: 4 email)

> **Ngày:** 2026-11-12 (cập nhật)
> **Người gửi:** Eric, Growth Manager, ReallyWise (sender "Eric RWise" <eric@reallywise.ai>)
> **Đối tượng:** listing agent tại Mỹ
> **Kiểu thư:** cá nhân, plain text, có ảnh/GIF dưới chữ ký ở email 1 và 2
> **Trạng thái trên Brevo:** option A đã lưu 3 template (ID 1, 2, 3). Option B thêm 1 template (ID 15, email pay per closing). Tất cả inactive, chưa gửi cho ai.

---

## 1. Tóm tắt chuỗi

| # | Ngày | Tên | Mục tiêu | Link | Media | Template Brevo |
|---|---|---|---|---|---|---|
| 1 | 0 | Product intro (hoặc 1B nếu biết listing mới) | Giới thiệu Eric và Property Expert, dẫn vào tour hướng dẫn | Tour (có `#tour=1`) | GIF demo, gắn link tour | ID 1 |
| 2 | 3 | Incentive: thử để nhận ưu đãi | Free 3 tháng đầu nếu mở tài khoản và dùng thử đến hết Q1 2027 | Trang tạo Property Expert | Ảnh dashboard agent, gắn link | ID 2 |
| 3 | 10 | Close the loop | Sản phẩm có thể chưa phải thứ họ cần. Mời mô tả nhu cầu khác để phỏng vấn và build | Không | Không | ID 3 |

**Lịch gửi đề xuất:** ngày 0, 3, 10 (chờ 3 ngày, rồi 7 ngày). Chọn ngày bắt đầu để email rơi vào ngày thường (bắt đầu thứ Hai thì email 2 và 3 rơi vào thứ Năm). Tránh tuần Lễ Tạ ơn (thứ Năm 26/11/2026). Ví dụ: bắt đầu thứ Hai 30/11, rồi 3/12, rồi 10/12.

**Link:**
- Tour: `https://infinaqnhat.github.io/Web-Infina-AI/property-expert-demo-tour.html?agent=dashboard#tour=1`. Đã kiểm tra: `#tour=1` làm tour 7 bước mở ngay, bước cuối "Show me my dashboard →" dẫn sang dashboard của agent.
- Tạo tài khoản: `https://reallywise-app.infina.dev` (trang "Create Property Expert", hiện mang tên INFINA AI).

**Phần chung ở cuối mỗi email:**

```
Eric
Growth Manager @ ReallyWise
eric@reallywise.ai

[ảnh/GIF nếu có]

ReallyWise, 68 Circular Rd #02-01, Singapore 049422
Not relevant? Reply "stop" and I won't write again, or unsubscribe.
```

`{{FIRSTNAME}}` trong email là `{{ contact.FIRSTNAME | default:"there" }}`.

---

## 2. Nội dung chi tiết

### Email 1 | Ngày 0 | Product intro

**Subject:** `Try it as a buyer: 123 Main St` (phương án B: `A 24/7 expert for your listings`)
**Preheader:** `A short guided tour: you play the buyer, then see what lands in your dashboard.`

```
Hi {{FIRSTNAME}},

I'm Eric, Growth Manager at ReallyWise. We build AI tools for real estate agents, and one of them is Property Expert, made for listing agents.

It turns each of your listings into a 24/7 expert. Buyers scan the yard sign or open a link and ask anything about the home, and it answers from the listing's own documents (disclosures, inspection report, HOA), with sources. When a buyer asks for a tour, you get the lead with the full chat, and every conversation is logged in your dashboard.

Here's a short guided tour, about a minute. You play the buyer, then you see what shows up on the agent side:

Start the guided tour  [link đậm: tour]

No signup, and you can skip any step.

Eric
Growth Manager @ ReallyWise
eric@reallywise.ai
```

**Media:** GIF `rw-demo-buyer.gif` (174 KB, 16 giây) dưới chữ ký, gắn link tour. Buyer hỏi về HVAC, nhận câu trả lời kèm nguồn Inspection Report, hỏi xem nhà, agent nhận thông báo "New lead". Khung đầu của GIF là câu trả lời đã hoàn tất, để ứng dụng thư chỉ hiện khung đầu (như Outlook) vẫn đủ ý.

---

### Email 1B | Ngày 0 | Product intro (biết listing mới + có tour riêng cho listing đó)

**Dùng khi:** danh sách có địa chỉ listing mới của từng agent VÀ team đã dựng sẵn Property Expert cho listing đó, có link tour riêng. Email 2 và 3 giữ nguyên.
**Subject:** `A 24/7 expert for {{STREET}}` (thiếu dữ liệu: `A 24/7 expert for your listings`)
**Preheader:** `A short guided tour: you play the buyer, then see what lands in your dashboard.`

```
Hi {{FIRSTNAME}},

Congrats on the new listing at {{STREET}}. Buyers will have questions about it at all hours, and most agents can't answer at 10pm.

I'm Eric, Growth Manager at ReallyWise. We build AI tools for real estate agents, and one of them is Property Expert, made for listing agents.

I went ahead and set one up for {{STREET}}. Buyers scan the yard sign or open a link and ask anything about the home, and it answers from the listing's own details, with sources. When a buyer asks for a tour, you get the lead with the full chat, and every conversation is logged in your dashboard.

Here's a short guided tour of it, about a minute. You play the buyer, then you see the agent side:

Start the guided tour  [link đậm: {{TOUR_LINK}}, tour riêng của listing đó]

No signup, and you can skip any step.

Eric
Growth Manager @ ReallyWise
eric@reallywise.ai

[GIF demo, gắn link {{TOUR_LINK}}]
Sample home shown. Your own Property Expert is at the link above.
```

`{{STREET}}` là `{{ contact.LISTING_STREET }}` (ví dụ "1428 Maple Ave"). `{{TOUR_LINK}}` là `{{ contact.TOUR_LINK }}`.

**Dữ liệu cần có cho mỗi contact (thuộc tính Brevo, loại Text, cần tạo thủ công):**
- `LISTING_STREET`: số nhà và tên đường.
- `TOUR_LINK`: link tour hướng dẫn của Property Expert dựng riêng cho listing đó (dạng có `#tour=1` để tour mở ngay).
- Import với cột: EMAIL, FIRSTNAME, LISTING_STREET, TOUR_LINK.

**Hành vi dự phòng:**
- Thiếu `TOUR_LINK`: mẫu tự dùng văn bản chung của email 1 và link tour mẫu (123 Main Street).
- Thiếu `LISTING_STREET`: lời chúc và subject chuyển sang câu chung.

**Việc team phải làm trước khi gửi:**
- Dựng Property Expert cho từng listing và lấy link tour riêng. Tôi **không tạo được** các link này.
- Xác nhận Property Expert dựng từ listing trả lời được những gì. Đoạn email nói "answers from the listing's own details" (chi tiết listing), không nhắc hồ sơ disclosure hay inspection report vì bản dựng sẵn từ link listing có thể chưa có các tài liệu đó.
- Xác nhận link tour riêng có tự mở tour (`#tour=1`) giống tour mẫu hay không.
- Chỉ gửi khi địa chỉ chính xác và listing thật sự mới (ví dụ niêm yết trong 30 ngày gần đây).

**Ghi chú nội dung:**
- "Most agents can't answer at 10pm" là giả thuyết, chưa có số liệu.
- GIF vẫn quay trên căn mẫu 123 Main Street, nên có dòng chú thích "Sample home shown." Nếu có ảnh chụp từ Property Expert của chính listing đó thì thay GIF bằng ảnh đó.

---

### Email 2 | Ngày 3 | Incentive: thử để nhận ưu đãi

**Subject:** `Free for your first 3 months`
**Preheader:** `Open an account and try Property Expert on your listings. The first 3 months are on us.`

```
Hi {{FIRSTNAME}},

A few days ago I sent you a guided tour of Property Expert. If it looked useful, here's a reason to try it on your own listings.

Listing agents who open an account by the end of Q1 2027 and try Property Expert get their first 3 months free. Set it up for a current listing, put the QR code or link on the sign or in your listing materials, and see what buyers actually ask.

Create your first Property Expert  [link đậm: reallywise-app]

If you try it, I'd love to hear what worked and what didn't. Just reply to this email.

Eric
Growth Manager @ ReallyWise
eric@reallywise.ai
```

**Media:** ảnh dashboard agent (`pp-pdf-agent.jpg`, màn hình Chats) dưới chữ ký, gắn link tạo tài khoản.

---

### Email 3 | Ngày 10 | Close the loop

**Subject:** `Should I close the loop?`
**Preheader:** `If Property Expert isn't a fit, tell me what you do need.`

```
Hi {{FIRSTNAME}},

I'll close the loop here so I'm not cluttering your inbox. It looks like Property Expert may not be what you need right now, and that's completely fine.

If there's something else in your day-to-day as a realtor that you wish a tool handled, I'd like to hear it. Our team is happy to set up an interview to talk it through and build around what you need.

Just reply to this email and describe what you have in mind. Even a couple of lines is enough.

Thanks for your time.

Eric
Growth Manager @ ReallyWise
eric@reallywise.ai
```

**Media:** không có. CTA duy nhất là trả lời email.

---

## 2B. Option B: chuỗi 4 email có "pay per closing"

Dành cho người ngại trả phí hàng tháng. Chi tiết đầy đủ, mức chia và nguồn nằm trong file `reallywise-outbound-option-b-pay-per-closing.md`.

| # | Ngày | Tên | Template Brevo |
|---|---|---|---|
| 1 | 0 | Product intro | ID 1 (như option A) |
| 2 | 3 | Incentive: free 3 tháng đầu | ID 2 (như option A) |
| 3 | 8 | **Pay per closing (mới)** | **ID 15** |
| 4 | 14 | Close the loop | ID 3 (như email 3 của option A) |

Lịch gửi đề xuất ngày 0, 3, 8, 14. Chung subject/chữ ký/footer với option A.

### Email B3 | Ngày 8 | Pay per closing

**Subject:** `Not into a monthly fee?`
**Preheader:** `Pay only if the listing sells.`

```
Hi {{FIRSTNAME}},

I realize a monthly subscription isn't how every agent likes to buy software. So here's another way to use Property Expert: pay per closing.

You set it up on a listing at no upfront cost. Only if that listing sells and closes do we take 7% of your commission on it. If it doesn't sell, you pay nothing.

For example, on an $800,000 home with a 2.75% listing-side commission ($22,000), that's $1,540, due at closing.

If you'd rather go this way, just reply "closing" with the listing you'd like to start with, and I'll set it up and send the terms in writing.

Eric
Growth Manager @ ReallyWise
eric@reallywise.ai
```

**Mức chia (Eric chốt):** 7% hoa hồng phía listing, **không có mức trần**, chỉ khi giao dịch đóng và chỉ trên listing đã dùng Property Expert. Ví dụ $800,000 x 2.75% = $22,000, phí $1,540. Nhà $2,000,000 (hoa hồng $55,000) thì phí $3,850. Các chương trình lead gen trả theo phần trăm hoa hồng trên thị trường thu khoảng 25 đến 40% (HomeLight 33%), nhưng đó là phí tạo ra khách hàng, khác với Property Expert.

**Cảnh báo pháp lý:** cấu trúc "chia phần trăm hoa hồng khi chốt" có rủi ro với RESPA Section 8 và luật cấp phép bất động sản từng bang (ReallyWise không phải môi giới có license). Nên có ý kiến luật sư **trước khi gửi** email này. Không phải tư vấn pháp lý.

**Cần chốt thêm:** cơ sở tính (hoa hồng phía listing, tổng gộp hay thực nhận), thời điểm và cách thu, ai trả (agent hay môi giới), và điều khoản bằng văn bản gửi agent.

---

## 3. Cách chạy

- **Trigger:** contact vào list riêng cho chuỗi này (list tạo trước, import contact sau khi bật automation).
- **Thoát khi:** đã trả lời (xóa khỏi list thủ công), đã tạo tài khoản, đã hủy đăng ký. Brevo không tự phát hiện reply.
- **Người bấm link tour ở email 1:** Eric nhắn riêng một dòng trong ngày.
- **Gói Free Brevo:** tối đa 300 email mỗi ngày. Nên thêm contact theo đợt 50 đến 100 người.
- **Theo dõi:** reply tích cực, số người bấm tour, số tài khoản tạo, bounce, hủy đăng ký.

**Trả lời thủ công của Eric:**
- *Họ mô tả nhu cầu:* "Thanks, that's really helpful. I'll send 2 or 3 time options for a 20-minute call to talk it through."
- *Họ đã bấm tour nhưng chưa trả lời:* "Hi {{name}}, I saw you took a look at the Property Expert tour. Anything that stood out, or anything that looked off for how you work?"
- *Họ hỏi về ưu đãi:* trả lời theo điều khoản đã chốt (mục 4).

---

## 4. Việc cần làm và xác nhận

| # | Việc | Ai |
|---|---|---|
| 1 | Gửi test cả 3 email cho chính mình, bấm thử link tour (qua link tracking của Brevo, tour có tự mở không?) và bấm **Reply** (template 1 và 3 chưa có reply-to, cần kiểm tra thư có về hộp thư của Eric không) | Eric |
| 2 | Chốt điều khoản "free 3 tháng đầu": tính từ khi nào, sau 3 tháng thì sao (tự tính phí hay tự dừng), có cần thẻ không | James / team |
| 3 | Kiểm tra luồng mở tài khoản ở `reallywise-app.infina.dev` đúng như email nói, ưu đãi áp dụng tự động. Trang đang mang tên INFINA AI | Team sản phẩm |
| 4 | Cam kết "build around what you need" ở email 3: đến mức nào, ai chạy phỏng vấn | James / team |
| 5 | Chuyển GIF và ảnh sang chỗ ổn định (hiện là GitHub: GIF theo tên nhánh, ảnh theo GitHub Pages) | Team kỹ thuật |
| 6 | Xóa tay trên Brevo các template không dùng: ID 4, 10, 11 | Eric |
| 7 | Dựng automation trong giao diện Brevo (3 bước cho option A, 4 bước cho option B; connector không tạo được automation) | Eric |
| 8 | Option B: ý kiến luật sư về mô hình chia hoa hồng khi chốt (RESPA, luật bang) và chốt điều khoản (xem mục 2B) trước khi gửi email B3 | James / pháp lý |

---

## 5. Cơ sở (tham khảo)

Các nguồn là blog của công ty công cụ cold email nên chỉ để tham khảo hướng:
- [Salesforge: follow-up after no response](https://www.salesforge.ai/blog/follow-up-after-no-response)
- [Hunter: cold email sequence](https://hunter.io/blog/cold-email-sequence)
- [Prospeo: breakup email](https://prospeo.io/s/breakup-email)
- [Causo: cold outreach to design partners](https://hub.causo.ai/guides/cold-outreach-design-partners-pre-launch-2026)
- [Prospeo: cold email call to action examples](https://prospeo.io/s/cold-email-call-to-action-examples)
