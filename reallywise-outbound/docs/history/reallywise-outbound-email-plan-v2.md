# ReallyWise: kế hoạch email outbound v2 (hướng "thử tour, rồi cùng xây")

> **Trạng thái:** DRAFT để duyệt. Chưa cập nhật Brevo.
> **Ngày:** 2026-11-11
> **Người gửi:** Eric, Growth Manager, ReallyWise
> **Đối tượng:** listing agent tại Mỹ (list lấy từ group Facebook và Reddit, nên email KHÔNG dùng địa chỉ listing)
> **Khác v1:** email 1 đưa người đọc vào tour hướng dẫn ngay. Email 2, 3, 4 dành cho người chưa click hay chưa phản hồi, với các góc khác nhau và lời mời làm "design partner" (dùng miễn phí 3 tháng, đổi lại phản hồi).

---

## 1. Hướng nội dung

| | v1 (đang có trên Brevo) | v2 (đề xuất) |
|---|---|---|
| Mục tiêu | Có phản hồi hoặc xem demo | Người đọc **đi hết tour**, thấy cả phía người mua lẫn dashboard của agent, rồi nhận lời mời thử và phản hồi |
| Email 1 | Giới thiệu + câu hỏi | Giới thiệu Property Expert + **link tour hướng dẫn** |
| Email 2 | Kịch bản + ảnh | **Lời mời design partner**: miễn phí 3 tháng, xây theo nhu cầu của họ |
| Email 3 | Link demo | **Làm giúp**: gửi một link listing, mình dựng Property Expert cho listing đó (không cần cuộc gọi, không cần yêu cầu) |
| Email 4 | Realisa | **Chốt + lối thoát**: nếu họ chủ yếu làm phía người mua, trả lời "buyer" để nhận bản phía người mua; hoặc dừng |

Nguyên tắc từ các nguồn đã tìm (chủ yếu là blog vendor, mang tính tham khảo):
- Mỗi follow-up mang **một góc mới**, không viết "just checking in".
- Lời mời design partner nên viết như **tuyển người cùng xây**, không phải bán hàng. Nêu rõ họ nhận gì, mình xin gì, mất bao lâu, và kết bằng một câu hỏi có/không.
- Email chốt (breakup) giúp người nhận dễ từ chối. Một nguồn khuyên hỏi người từ chối vì sao.
- Agent nhận rất nhiều email mỗi ngày. Tránh subject kiểu "Quick question" hoặc "Introduction".

---

## 2. Link tour (đã kiểm tra)

**Dùng link này:**

```
https://infinaqnhat.github.io/Web-Infina-AI/property-expert-demo-tour.html?agent=dashboard#tour=1
```

Tôi mở thử bằng trình duyệt tự động:
- **Link không có `#tour=1`:** chỉ hiện bong bóng "New here? Take a 30s tour", tour **không tự chạy**.
- **Có `#tour=1`:** tour mở ngay khi vào ("Realisa, 1 of 7: Meet your Property Expert").
- **Tour có 7 bước:** (1) Meet your Property Expert, (2) Buyers ask it anything, (3) Try it as a buyer (bấm một câu hỏi), (4) Now ask your own (gõ câu hỏi), (5) When a buyer wants a person, (6) khái niệm lead, (7) **"Every chat is logged for you"** với nút **"Show me my dashboard →"** dẫn sang dashboard của agent. Mỗi bước đều có "Skip tour" hoặc "Skip this step".
- **`?agent=dashboard`** làm lời ở bước 7 nói rõ đây là dashboard của agent. Đây là dạng link của slide 10 trong deck.
- Chưa kiểm chứng: Brevo có giữ phần `#tour=1` khi bọc link để theo dõi click hay không. **Cần gửi test và bấm thử** trước khi dùng thật.
- Nhược điểm: domain `github.io` không phải domain thương hiệu.

---

## 3. Chuỗi 4 email

Tất cả plain text kiểu thư cá nhân, gửi từ Eric, chữ ký và footer như bản v1. `{{FIRSTNAME}}` là `{{ contact.FIRSTNAME | default:"there" }}`.

### Email 1 | Ngày 0 | Giới thiệu + vào tour

**Mục tiêu:** bấm link và đi hết tour.
**Subject A:** `Try it as a buyer: 123 Main St`
**Subject B:** `A 24/7 expert for your listings`
**Preheader:** `A guided tour. You play the buyer, then see what lands in your dashboard.`

```
Hi {{FIRSTNAME}},

I'm Eric from ReallyWise. We built Property Expert for listing agents: an AI expert for one home that answers buyers' questions at any hour, using the listing's own documents, with sources.

When a buyer asks for a tour, you get the lead with the full chat, and every conversation is logged in your dashboard.

The fastest way to see it is a short guided tour. You play the buyer, then you see what shows up on the agent side:

Start the guided tour  [bold link to the tour URL]

No signup, and you can skip any step. It takes about a minute.

Eric
Growth Manager @ ReallyWise
eric@reallywise.ai
```

**Ghi chú:**
- "No signup" và "skip any step": đã kiểm tra trên demo (không đăng nhập, mỗi bước đều có nút bỏ qua).
- "About a minute": theo deck (slide 10). Bong bóng trong demo ghi "30s tour". Chọn một cách nói thống nhất.
- Email 1 không có ảnh để giữ nhẹ cho lần chạm đầu.

---

### Email 2 | Ngày 3 | Lời mời design partner

**Góc:** không bán, tuyển người cùng xây. Miễn phí 3 tháng.
**Subject:** `Looking for [5] listing agents to shape this`
**Preheader:** `Free for 3 months, in exchange for honest feedback.`

```
Hi {{FIRSTNAME}},

A few days ago I sent a guided tour of ReallyWise Property Expert. Whether or not you've had a chance to look, I wanted to ask you something.

I'm picking a small group of listing agents to build it with, [5] to start.

What you'd get: free use for 3 months, and I'll build around how you actually handle buyer inquiries, not a generic feature list.

What I'd ask: try it on your listings, and a short feedback interview ([20] minutes) so I understand what works and what's missing.

If that sounds interesting, just reply "in" and tell me one thing that slows you down with buyer inquiries today. If you'd like to look first, the guided tour is here:

Start the guided tour  [bold link to the tour URL]

Eric
Growth Manager @ ReallyWise
eric@reallywise.ai
```

**Ghi chú:**
- Chỗ `[5]` và `[20]` là giá trị đề xuất, bạn quyết.
- Một nguồn cảnh báo người dùng miễn phí dễ bỏ giữa chừng, nên cân nhắc yêu cầu họ cam kết cụ thể (dùng thử trên ít nhất một listing, tham gia phỏng vấn).
- Cam kết "build around how you handle buyer inquiries" cần team xác nhận (mục 6).

---

### Email 3 | Ngày 8 | Làm giúp: gửi link listing, nhận Property Expert

**Dành cho người không có nhu cầu làm design partner.** Không xin yêu cầu, không xin cuộc gọi. Họ chỉ cần trả lời bằng một link.
**Subject:** `Send me a listing link`
**Preheader:** `I'll set up a Property Expert for one of your listings. No call, no commitment.`

```
Hi {{FIRSTNAME}},

No call and no commitment on this one: send me a link to one of your current listings, and I'll set up a Property Expert for it and send you back the QR code and the link.

You can scan it yourself, ask it what a buyer would ask, and see what lands in your dashboard. It's also something you could show a seller at a listing appointment.

Just reply with the listing link.

Eric
Growth Manager @ ReallyWise
eric@reallywise.ai
```

**Ghi chú:**
- Mẫu "trả lời với X, mình gửi lại Y" là kiểu CTA ít ma sát các nguồn khuyên dùng. Một nguồn thấy lời đề nghị cụ thể (kèm sản phẩm hữu hình) hiệu quả hơn lời đề nghị chung chung (số liệu của vendor, chưa kiểm chứng).
- Một CTA duy nhất.
- Cần xác nhận: Eric/team **làm được thật** việc dựng Property Expert cho listing của họ, nhanh đến đâu, và giới hạn số lượng nếu nhiều người gửi (ví dụ "the first 10 agents").
- Câu "show a seller at a listing appointment" là gợi ý sử dụng, không nói về người dùng khác (chưa có khách hàng).

---

### Email 4 | Ngày 14 | Chốt, kèm lối thoát "buyer"

**Góc:** breakup lịch sự. Danh sách lấy từ group Facebook/Reddit có thể lẫn agent phía người mua, nên cho họ một lối thoát nếu sản phẩm không đúng phía.
**Subject:** `Last note from me`
**Preheader:** `If you're mostly on the buyer side, reply "buyer".`

```
Hi {{FIRSTNAME}},

I'll stop here so I'm not cluttering your inbox.

One thing before I go: if you're mostly on the buyer side rather than listings, reply "buyer" and I'll send you the buyer-side version instead.

Otherwise, thanks for reading, and the offer of free access while we build with your feedback stands if the timing ever changes.

Eric
Growth Manager @ ReallyWise
eric@reallywise.ai
```

**Ghi chú:**
- "Buyer-side version" là Home Concierge trong deck (slide 04). Cần xác nhận có gửi demo hay link được không. Trang `reallywise-app.infina.dev` có tab "For Buyer Agent".
- **Phương án thay thế (xin giới thiệu):** thay đoạn "buyer" bằng: *"If there's a listing agent or team lead you know who'd want this, I'd be grateful if you'd forward this note."* Chỉ giữ MỘT lời đề nghị mỗi email. Nguồn về xin giới thiệu trong email chốt rất yếu (chỉ một trang mẫu), nên coi là ý tưởng để test.

---

### Các hướng khác đã cân nhắc (chưa dùng)

| Hướng | Ý tưởng | Vì sao chưa chọn |
|---|---|---|
| Góc "giúp chốt listing" | Property Expert như điểm khác biệt khi pitch người bán. Các nguồn cho thấy người bán coi trọng uy tín, hiểu biết thị trường và kế hoạch marketing (nhiều khảo sát cũ, 2018 đến 2022) | Nguồn không trực tiếp chứng minh công nghệ 24/7 giúp chốt listing. Đã gài thành một câu ở email 3 |
| Realisa | Trợ lý buổi sáng cho agent (morning brief, nhắc việc) | Là sản phẩm khác, chưa có demo riêng. Có thể dùng cho đợt sau |
| Tài liệu hữu ích | Checklist "câu hỏi buổi tối: trả lời gì, chuyển cho agent gì" | Phải viết thêm nội dung, và không dẫn thẳng đến sản phẩm |
| Chia sẻ số liệu | Một số liệu thị trường | Chưa có số liệu có nguồn |

---

## 4. Logic gửi (Brevo automation, bạn dựng trong giao diện)

| Bước | Cấu hình |
|---|---|
| Trigger | Contact vào list (list riêng cho chuỗi này) |
| Email 1 | Ngày 0 (giới thiệu + tour) |
| Chờ 3 ngày | Email 2 (design partner) |
| Chờ 5 ngày | Email 3 (làm giúp) |
| Chờ 6 ngày | Email 4 (chốt) |
| **Thoát khi** | Đã **bấm link tour** (người này đã ấm, Eric nhắn riêng), đã trả lời (xóa khỏi list thủ công), đã hủy đăng ký |

- Brevo liệt kê điều kiện thoát theo click, mở và hủy (theo trợ giúp chính thức đã tìm thấy). Bạn kiểm tra điều kiện "link clicked" trong account.
- Theo dõi click cần bật link tracking. Nguồn về deliverability coi tracking là rủi ro nhỏ, nhưng ở đây cần để biết ai đã click.
- Người đã click nhưng chưa trả lời: Eric nhắn riêng một dòng trong ngày (mẫu ở mục 5).

---

## 5. Mẫu trả lời thủ công của Eric

**Họ trả lời "in" hoặc quan tâm:**
```
Great, thanks {{name}}. I'll send you a short note with 2 or 3 time options for a 20-minute call. Before then, could you tell me which of your current listings you'd want to try it on?
```

**Họ đã click tour nhưng chưa trả lời:**
```
Hi {{name}}, I saw you took a look at the Property Expert tour. Anything that stood out, or anything that looked off for how you work? Happy to hear it straight.
```

**Họ từ chối:**
```
Totally understand, thanks for letting me know. If you have a second, what would have made it worth trying? No pressure either way.
```

---

## 6. Việc cần xác nhận trước khi gửi

| # | Câu hỏi | Ai |
|---|---|---|
| 1 | Điều khoản lời mời: miễn phí 3 tháng, bắt đầu tính từ khi nào, kết thúc thế nào (tự tính phí, tự dừng), có cần thẻ không? | James / team |
| 2 | "Xây sản phẩm theo nhu cầu của họ" cam kết đến mức nào? Gợi ý viết "shape the roadmap" nếu chưa chắc | James / team |
| 3 | Số lượng design partner (`[5]`) và thời lượng phỏng vấn (`[20]` phút) | Eric |
| 4 | Dữ liệu agent đưa vào (hồ sơ listing, chat người mua) được lưu và bảo mật thế nào? Có thỏa thuận bảo mật không? | Team sản phẩm / pháp lý |
| 5 | Người dùng thử có thật sự dùng được Property Expert trên **listing của họ** không, hay chỉ xem demo mẫu? Lời mời ở email 3 nói "try it on your listings" | Team sản phẩm |
| 6 | Link tour dùng domain github.io. Có muốn dùng domain thương hiệu không? | Team kỹ thuật |
| 7 | Gửi test và bấm thử link: tour có tự mở không khi đi qua link tracking của Brevo? | Eric |
| 8 | Chuỗi này vẫn gửi cho list thu thập từ group Facebook và Reddit. Brevo cấm danh sách thu thập (bạn đã biết), và Facebook/Reddit cấm scraping | Eric |

---

## 7. Nguồn đã dùng

- [Salesforge: follow-up after no response](https://www.salesforge.ai/blog/follow-up-after-no-response)
- [Sequenzy: B2B email sequence templates](https://www.sequenzy.com/blog/b2b-email-sequence-templates)
- [Flowjam: cold email templates for B2B SaaS](https://www.flowjam.com/blog/cold-email-templates-for-b2b-saas-that-book-30-more-demos)
- [Prospeo: sales follow-up email after no response](https://prospeo.io/s/sales-follow-up-email-after-no-response)
- [Causo: cold outreach to design partners pre-launch](https://hub.causo.ai/guides/cold-outreach-design-partners-pre-launch-2026)
- [Mika Reyes: how to run an effective design partnership](https://www.mikareyes.com/blog/how-to-run-an-effective-design-partnership)
- [Design Partner Program Setup](https://knowledgelib-io.pages.dev/business/customer-validation/design-partner-program-setup/2026)
- [Modern Inbound: cold email for real estate tech](https://moderninbound.com/blog/cold-email-for-real-estate-tech)
- [RealEstateNews: what works in agent vendor relationships](https://www.realestatenews.com/2026/05/02/what-works-and-what-doesnt-in-agent-vendor-relationships)

Hầu hết là blog vendor nên chỉ dùng để tham khảo hướng, không phải số liệu độc lập.
- [Salesforge: soft CTAs that make prospects respond](https://www.salesforge.ai/blog/soft-ctas-that-make-your-prospects-respond-to-your-emails)
- [Skyp: the micro offer technique](https://skyp.beehiiv.com/p/the-micro-offer-technique-earn-replies-without-selling-anything)
- [Prospeo: cold email call to action examples](https://prospeo.io/s/cold-email-call-to-action-examples)
- [Follow Up Boss: how top agents win listing presentations](https://www.followupboss.com/blog/listing-presentation)
- [RealTrends: what sellers really want from a listing agent](https://www.realtrends.com/blog/2021/09/30/what-sellers-really-want-from-a-listing-agent/)
- [Prospeo: breakup email templates and timing](https://prospeo.io/s/breakup-email)
- [Close: the breakup email](https://close.com/blog/the-breakup-email)
