# ReallyWise: option B, chuỗi 4 email có "pay per closing"

> **Ngày:** 2026-11-12
> **Trạng thái:** email 3 mới đã lưu trên Brevo (template ID 15, inactive). Email 1, 2, 4 dùng lại template ID 1, 2, 3 của option A. Chưa gửi cho ai.
> **Quan trọng:** email 3 (pay per closing) có **rủi ro pháp lý** ở Mỹ (xem mục 4). Không nên gửi trước khi luật sư xem.

## 1. Chuỗi

| # | Ngày | Tên | Nguồn nội dung |
|---|---|---|---|
| 1 | 0 | Product intro | Email 1 của option A (hoặc 1B nếu biết listing mới) |
| 2 | 3 | Incentive: free 3 tháng | Email 2 của option A |
| 3 | 8 | **Pay per closing** | **Mới** |
| 4 | 14 | Close the loop | Email 3 của option A |

Lịch gửi đề xuất ngày 0, 3, 8, 14: các khoảng chờ tăng dần (3, 5, 6 ngày), tổng 2 tuần. Chọn ngày bắt đầu để email rơi vào ngày thường và tránh tuần Lễ Tạ ơn (thứ Năm 26/11/2026).

Logic của chuỗi: email 2 mời dùng thử miễn phí 3 tháng đầu. Email 3 là lựa chọn dành cho người ngại trả phí hàng tháng. Email 4 đóng vòng lặp và mời mô tả nhu cầu khác.

---

## 2. Nội dung 4 email

`{{FIRSTNAME}}` là `{{ contact.FIRSTNAME | default:"there" }}`. Chữ ký và footer như các email trước (Eric, Growth Manager @ ReallyWise, địa chỉ 68 Circular Rd #02-01 Singapore 049422, dòng "Not relevant? Reply stop... or unsubscribe").

### Email 1 | Ngày 0 | Product intro
**Subject:** `Try it as a buyer: 123 Main St`
```
Hi {{FIRSTNAME}},

I'm Eric, Growth Manager at ReallyWise. We build AI tools for real estate agents, and one of them is Property Expert, made for listing agents.

It turns each of your listings into a 24/7 expert. Buyers scan the yard sign or open a link and ask anything about the home, and it answers from the listing's own documents (disclosures, inspection report, HOA), with sources. When a buyer asks for a tour, you get the lead with the full chat, and every conversation is logged in your dashboard.

Here's a short guided tour, about a minute. You play the buyer, then you see what shows up on the agent side:

Start the guided tour  [link tour, #tour=1]

No signup, and you can skip any step.

[chữ ký] [GIF demo gắn link tour]
```
(Bản 1B cho agent có listing mới: xem file `reallywise-outbound-sequence-summary.md`.)

### Email 2 | Ngày 3 | Incentive
**Subject:** `Free for your first 3 months`
```
Hi {{FIRSTNAME}},

A few days ago I sent you a guided tour of Property Expert. If it looked useful, here's a reason to try it on your own listings.

Listing agents who open an account by the end of Q1 2027 and try Property Expert get their first 3 months free. Set it up for a current listing, put the QR code or link on the sign or in your listing materials, and see what buyers actually ask.

Create your first Property Expert  [link reallywise-app]

If you try it, I'd love to hear what worked and what didn't. Just reply to this email.

[chữ ký] [ảnh dashboard agent gắn link]
```

### Email 3 | Ngày 8 | Pay per closing (MỚI)
**Subject:** `Not into a monthly fee?`
**Preheader:** `Pay only if the listing sells.`
```
Hi {{FIRSTNAME}},

I realize a monthly subscription isn't how every agent likes to buy software. So here's another way to use Property Expert: pay per closing.

You set it up on a listing at no upfront cost. Only if that listing sells and closes do we take 7% of your commission on it. If it doesn't sell, you pay nothing.

For example, on an $800,000 home with a 2.75% listing-side commission ($22,000), that's $1,540, due at closing.

If you'd rather go this way, just reply "closing" with the listing you'd like to start with, and I'll set it up and send the terms in writing.

[chữ ký]
```
Không có link, không có ảnh. CTA là trả lời "closing". Phép tính ví dụ đã kiểm tra: 800,000 x 2.75% = 22,000; 7% của 22,000 = 1,540. Không có mức trần, nên với nhà 2 triệu USD (2.75% = 55,000) phí là 3,850.

### Email 4 | Ngày 14 | Close the loop
**Subject:** `Should I close the loop?`
```
Hi {{FIRSTNAME}},

I'll close the loop here so I'm not cluttering your inbox. It looks like Property Expert may not be what you need right now, and that's completely fine.

If there's something else in your day-to-day as a realtor that you wish a tool handled, I'd like to hear it. Our team is happy to set up an interview to talk it through and build around what you need.

Just reply to this email and describe what you have in mind. Even a couple of lines is enough.

Thanks for your time.

[chữ ký]
```

---

## 3. Mức chia sẻ hoa hồng: tham chiếu và đề xuất

**Các chương trình "trả khi chốt giao dịch" trên thị trường (lead gen, phí giới thiệu):**

| Chương trình | Mức | Nguồn / độ tin cậy |
|---|---|---|
| HomeLight | **33%** hoa hồng gộp của agent (nâng từ 25% vào 10/2022; 30% với giao dịch trên 4 triệu USD trước đó) | Tin của Inman/RealTrends 2022, trang trợ giúp của HomeLight còn ghi 33% |
| Zillow Flex | Khoảng **30 đến 40%**, có nguồn ghi tới 35% hoa hồng gộp, tùy khu vực và giá | Blog bên thứ ba, không có bảng phí chính thức |
| Opcity | 33 đến 38% | Một blog duy nhất, chưa xác nhận |
| Chung ngành | 15 đến 40%, phổ biến 25 đến 40% | Một bài hướng dẫn |

Không tìm thấy mức "chuẩn ngành" cho mô hình pay-per-close của phần mềm. Một số nhà cung cấp tính phí cố định thay vì phần trăm. Các nguồn đều là blog/vendor nên chỉ để tham chiếu.

**Hoa hồng phía listing để tính ví dụ:** khảo sát agent ghi trung bình khoảng 2.76% đến 3.01% (Clever, FastExpert; khảo sát tự chọn). Môi giới giảm giá khoảng 1 đến 1.5%.

**Mức chia đã chốt (Eric): 7% hoa hồng phía listing, không có mức trần.**
- Chỉ trên listing đã dùng Property Expert, chỉ khi giao dịch đóng.
- Ví dụ: nhà $800,000 với hoa hồng phía listing 2.75% ($22,000) thì phí là **$1,540**. Nhà $2,000,000 (hoa hồng $55,000) thì phí là **$3,850**.
- Lý do mức này thấp hơn nhiều so với các chương trình 25 đến 40%: các chương trình đó trả cho việc **tạo ra khách hàng**, còn Property Expert giúp chuyển đổi người mua hỏi về listing **đã có** của agent. (Đây là nhận định của tôi, không có nguồn trực tiếp.)
- 7% là mức cao nhất trong vùng 3 đến 7% tôi đã đề xuất. Không có mức trần nghĩa là phí tăng theo giá nhà, agent có nhà đắt có thể thấy đây là khoản lớn, và cũng làm tăng sự chú ý về mặt pháp lý (mục 4). Có thể test phản ứng trước khi áp dụng rộng.
- Còn cần chốt: **hoa hồng nào** làm cơ sở (phía listing, tổng gộp hay thực nhận), thời điểm thu và ai trả (agent hay môi giới).

---

## 4. Rủi ro pháp lý (cần luật sư xem trước khi gửi email 3)

Đây không phải tư vấn pháp lý. Những gì tìm thấy:
- **RESPA Section 8** (quy định liên bang, [12 CFR 1024.14](https://www.consumerfinance.gov/rules-policy/regulations/1024/14/)) cấm trả hoặc nhận bất kỳ khoản nào có giá trị cho việc **giới thiệu** hoạt động dịch vụ thanh toán, và việc vi phạm có thể là tội hình sự. Khoản trả hợp lệ phải tương xứng với dịch vụ thực sự cung cấp.
- Cục Bảo vệ Tài chính Người tiêu dùng (CFPB) có một ý kiến tư vấn (2/2023) về các nền tảng so sánh dịch vụ thanh toán số, cho rằng việc nhận "thứ có giá trị" cho hoạt động giới thiệu là phí giới thiệu bị cấm.
- Một bình luận về các nền tảng ghép agent nói việc bán lead không nên gắn với **kết quả giao dịch** hoặc **phần trăm hoa hồng** của môi giới. Mô hình "chia theo % hoa hồng khi chốt" khá giống điều này, nên là cấu trúc rủi ro cao. Đây là một nguồn bình luận, không phải kết luận pháp lý.
- **Luật từng bang khác nhau.** Colorado cho phép phí giới thiệu trả cho người không có license trong một số trường hợp nếu có thông báo bằng văn bản và không vướng RESPA, kèm khuyến nghị hỏi luật sư. California được mô tả là nghiêm hơn (không trả phí giới thiệu cho người không có license nếu khoản vay được bảo hiểm liên bang), từ một nguồn môi giới.
- ReallyWise là công ty công nghệ (không phải môi giới có license). Cần xem xét việc nhận phần trăm hoa hồng bán nhà có bị coi là chia hoa hồng cho người không có license hoặc phí giới thiệu hay không.

**Việc nên làm:** nhờ luật sư về RESPA và luật cấp phép bất động sản từng bang cho cấu trúc "phần trăm hoa hồng khi chốt". Hỏi thêm các cấu trúc thay thế (ví dụ phí cố định cho dịch vụ phần mềm). Trong lúc chờ, dùng **option A** (3 email) không có email pay per closing.

---

## 5. Việc cần xác nhận

| # | Việc | Ai |
|---|---|---|
| 1 | Ý kiến luật sư về mô hình chia hoa hồng khi chốt (RESPA, luật bang) | James / pháp lý |
| 2 | Mức 7% không cap đã chốt. Còn cần chốt cơ sở tính (hoa hồng phía listing, tổng gộp hay thực nhận), thời điểm và cách thu (agent hay môi giới trả) | James / team |
| 3 | Điều khoản bằng văn bản gửi cho agent ("send the terms in writing") | Pháp lý |
| 4 | Định nghĩa "listing đã dùng Property Expert" và cách xác định giao dịch thuộc chương trình | Team sản phẩm |
| 5 | Tất cả mục đã nêu ở các email trước (điều khoản free 3 tháng, luồng mở tài khoản, cam kết build theo nhu cầu, test link tour và reply-to) | Như trước |

---

## 6. Nguồn

- [RealTrends: HomeLight hikes referral fees for agents](https://www.realtrends.com/articles/homelight-hikes-referral-fees-for-agents)
- [Inman: HomeLight raises real estate agent referral fee to 33%](https://inman.com/2022/10/25/homelight-raises-real-estate-agent-referral-fee-to-33)
- [HomeLight help: what does HomeLight cost](https://help.homelight.com/hc/en-us/articles/360002947414-what-does-homelight-cost-)
- [Clever: real estate referral fees explained](https://listwithclever.com/real-estate-blog/realtor-referral-how-do-referral-agents-work/)
- [The Close: pay-at-closing real estate leads](https://theclose.com/real-estate-leads-pay-at-closing)
- [CFPB: Regulation X, 12 CFR 1024.14 (RESPA Section 8)](https://www.consumerfinance.gov/rules-policy/regulations/1024/14/)
- [Colorado DRE: RESPA and referral fees position](https://dre.colorado.gov/sites/dre/files/documents/Commission%20Position%2003%20-%20RESPA%20and%20Referral%20Fees.pdf)
- [HousingWire: broker-to-broker referral exemption does not apply to agent matching platforms (opinion)](https://develop.housingwire.com/articles/opinion-broker-to-broker-referral-exemption-does-not-apply-to-agent-matching-platforms)
- [Clever: is a 6% commission still standard in 2026](https://listwithclever.com/?p=10982)
- [FastExpert: real estate agent commissions](https://fastexpert.com/blog/real-estate-agent-commissions-by-state)
