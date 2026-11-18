# ReallyWise: kế hoạch email outbound v3 (3 email)

> **Trạng thái:** DRAFT để duyệt. Chưa cập nhật Brevo.
> **Ngày:** 2026-11-11
> **Người gửi:** Eric, Growth Manager, ReallyWise (thư cá nhân, plain text, chữ ký + footer như bản trước)
> **Đối tượng:** listing agent tại Mỹ. Email không dùng địa chỉ listing.
> **Thay v2:** chuỗi rút còn 3 email theo hướng mới của Eric.

## 1. Chuỗi

| # | Ngày | Tên | Mục tiêu | Link | Media |
|---|---|---|---|---|---|
| 1 | 0 | Product intro | Giới thiệu Eric + Property Expert, dẫn vào tour | Tour hướng dẫn | GIF demo (dưới chữ ký, gắn link tour) |
| 2 | 4 | Incentive: thử để nhận ưu đãi | Free 3 tháng đầu nếu mở tài khoản và dùng thử trong thời gian này | Trang tạo Property Expert | Ảnh dashboard agent (dưới chữ ký, gắn link) |
| 3 | 11 | Close the loop | Sản phẩm chưa phải thứ bạn cần. Nếu có nhu cầu khác, trả lời để phỏng vấn và build theo nhu cầu | Không | Không (chỉ chữ) |

**Link dùng trong email:**
- Tour (email 1): `https://infinaqnhat.github.io/Web-Infina-AI/property-expert-demo-tour.html?agent=dashboard#tour=1`. Đã kiểm tra: phần `#tour=1` làm tour 7 bước mở ngay khi vào, bước cuối "Show me my dashboard →" dẫn sang dashboard của agent.
- Tạo tài khoản (email 2): `https://reallywise-app.infina.dev` (trang "Create Property Expert", hiện mang tên INFINA AI).

---

## 2. Nội dung chi tiết

`{{FIRSTNAME}}` là `{{ contact.FIRSTNAME | default:"there" }}`.

### Email 1 | Ngày 0 | Product intro

**Subject A:** `Try it as a buyer: 123 Main St`
**Subject B:** `A 24/7 expert for your listings`
**Preheader:** `A short guided tour: you play the buyer, then see what lands in your dashboard.`

```
Hi {{FIRSTNAME}},

I'm Eric, Growth Manager at ReallyWise. We build AI tools for real estate agents, and one of them is Property Expert, made for listing agents.

It turns each of your listings into a 24/7 expert. Buyers scan the yard sign or open a link and ask anything about the home, and it answers from the listing's own documents (disclosures, inspection report, HOA), with sources. When a buyer asks for a tour, you get the lead with the full chat, and every conversation is logged in your dashboard.

Here's a short guided tour, about a minute. You play the buyer, then you see what shows up on the agent side:

Start the guided tour  [bold link: tour]

No signup, and you can skip any step.

Eric
Growth Manager @ ReallyWise
eric@reallywise.ai

[GIF demo, gắn link tour]
```

**Ghi chú:**
- Một CTA duy nhất: link tour.
- "No signup, skip any step": đã kiểm tra trên demo.
- GIF = buyer hỏi về HVAC, nhận câu trả lời kèm nguồn Inspection Report, hỏi xem nhà, agent nhận thông báo "New lead".

---

### Email 2 | Ngày 4 | Incentive: thử để nhận ưu đãi

**Subject:** `Free for your first 3 months`
**Preheader:** `Open an account and try Property Expert on your listings. The first 3 months are on us.`

```
Hi {{FIRSTNAME}},

A few days ago I sent you a guided tour of Property Expert. If it looked useful, here's a reason to try it on your own listings.

Listing agents who open an account by the end of Q1 2027 and try Property Expert get their first 3 months free. Set it up for a current listing, put the QR code or link on the sign or in your listing materials, and see what buyers actually ask.

Create your first Property Expert  [bold link: reallywise-app]

If you try it, I'd love to hear what worked and what didn't. Just reply to this email.

Eric
Growth Manager @ ReallyWise
eric@reallywise.ai

[Ảnh dashboard agent, gắn link]
```

**Ghi chú:**
- Hạn đăng ký: đến hết Q1 2027 (theo Eric).
- Điều khoản "free 3 tháng đầu" cần chốt (mục 4).

---

### Email 3 | Ngày 11 | Close the loop

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

**Ghi chú:**
- Không link, không ảnh. CTA là trả lời email.
- Cam kết "build around what you need" cần team xác nhận (mục 4).

---

## 3. Gửi và theo dõi

- Trigger: contact vào list riêng. Khoảng chờ: 4 ngày rồi 7 ngày.
- Thoát khi: đã trả lời (xóa khỏi list thủ công), đã tạo tài khoản, đã hủy đăng ký.
- Theo dõi click link tour (email 1): người đã click là người ấm, Eric có thể nhắn riêng một dòng trong ngày.
- Trả lời thủ công: nếu họ mô tả nhu cầu ở email 3, cảm ơn và đề xuất 2 hoặc 3 khung giờ phỏng vấn (20 phút).

## 4. Việc cần xác nhận

| # | Câu hỏi | Ai |
|---|---|---|
| 1 | "Free 3 tháng đầu": áp dụng khi nào, sau 3 tháng thì sao (tự tính phí, tự dừng), có cần thẻ không? Hạn đăng ký ưu đãi: đến hết Q1 2027 (Eric đã chốt). | James / team |
| 2 | Luồng "mở tài khoản" ở `reallywise-app.infina.dev` có đúng như email nói không, và ưu đãi có áp dụng tự động không? Trang hiện mang tên INFINA AI | Team sản phẩm |
| 3 | "Build around what you need": cam kết đến mức nào, ai chạy phỏng vấn? | James / team |
| 4 | Gửi test và bấm thử link tour qua link tracking của Brevo: tour có tự mở không? | Eric |
| 5 | GIF và ảnh đang lấy từ GitHub (tên nhánh và GitHub Pages). Nên chuyển sang chỗ ổn định | Team kỹ thuật |
| 6 | Template 4, 10, 11 trên Brevo không còn dùng, cần xóa tay | Eric |
