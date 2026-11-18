# ReallyWise: kế hoạch email outbound cho listing agent (Mỹ)

> **Trạng thái:** DRAFT v1 để duyệt nội dung. Chưa gửi gì, chưa tạo template HTML.
> **Ngày:** 2026-11-11
> **Đối tượng:** listing agent tại Mỹ
> **Sản phẩm trong email:** Property Expert (chính), Realisa (nhắc ở email 4)
> **Người gửi:** Eric, Growth Manager của ReallyWise (sender "Eric RWise" <eric@reallywise.ai>). Email viết ở ngôi thứ nhất, giọng của Eric.
> **Ngôn ngữ email:** English (US). Phần kế hoạch viết tiếng Việt.

---

## 1. Mục tiêu và nguyên tắc

**Mục tiêu của sequence:** có được một phản hồi ("yes, show me") hoặc một lượt xem demo từ listing agent. Chưa bán trực tiếp.

**Định vị trong một câu:** mỗi listing có một chuyên gia AI trả lời người mua 24/7 bằng hồ sơ của chính căn nhà, và báo cho agent khi người mua muốn xem nhà.

**Nguyên tắc nội dung (từ ReallyWise Brand Guideline v1.0 và các nghiên cứu cold email đã tìm):**

| Nguyên tắc | Áp dụng |
|---|---|
| Rõ trước, khéo sau | Nói thẳng sản phẩm làm gì, không dùng từ hoa mỹ |
| Có bằng chứng, không hứa quá | Không dùng số liệu chưa có nguồn. Không "guaranteed" |
| Sentence case, không emoji | Subject và nội dung viết hoa đầu câu như bình thường |
| Tên viết đúng | **ReallyWise** (R và W hoa, viết liền, không ".ai"). Tên tính năng giữ nguyên: Property Expert, Home Concierge, Realisa |
| Xưng "you" với người đọc | Agent xưng "I" khi ký bằng tên người thật |
| Fair Housing | Không nói về trường học, "khu an toàn", "family-friendly", hay đặc điểm dân cư |
| Ngắn, một ý, một CTA | Mỗi email khoảng 60 đến 100 từ (nguồn khuyên dưới 120). Một câu hỏi hoặc một link |
| Câu đầu về người nhận, không mở bằng "My name is..." | Mở bằng listing của họ. Giới thiệu bản thân đặt sau câu mở đầu |
| Một câu giới thiệu ngắn | Vai trò của Eric gắn với việc họ quan tâm (email 1). Tên, chức danh, liên hệ ở chữ ký |
| Một dòng bằng chứng, chỉ bằng chứng thật | Hiện dùng bằng chứng sản phẩm ("from the home's own documents, with sources"). Không bịa khách hàng hay số liệu |
| Mỗi follow-up có góc mới | Không viết "just checking in" |
| Plain text cho email đầu | Không ảnh nhúng, không nút, không tracking pixel ở email 1 và 2 |

---

## 2. Điều kiện trước khi gửi (checklist)

Chưa làm xong các mục này thì chưa gửi.

- [ ] **Footer CAN-SPAM:** tên người gửi, địa chỉ vật lý, cách hủy đăng ký. Hủy phải được xử lý trong 10 ngày làm việc, tốt nhất là ngay lập tức. Không bán hoặc chuyển địa chỉ đã hủy.
- [ ] **Header hủy đăng ký one-click** (RFC 8058) nếu công cụ hỗ trợ. Giữ spam complaint dưới 0.3%.
- [ ] **Danh sách suppression:** lưu mọi người đã hủy hoặc bounce, không gửi lại.
- [ ] **Các tuyên bố sản phẩm đã được team xác nhận** (xem mục 8).
- [ ] **Test nhỏ trước:** 50 đến 100 người, rồi mới tăng.
- [ ] Luật sư hoặc compliance xem lại. Tài liệu này không phải tư vấn pháp lý.

---

## 3. Tổng quan sequence

Khoảng cách tăng dần: 3 ngày, 4 ngày, 7 ngày. Tổng 14 ngày, 4 email. Dừng ngay khi họ trả lời hoặc hủy.

| # | Ngày | Vai trò | Góc nội dung | CTA | Link |
|---|---|---|---|---|---|
| 1 | 0 | Mở đầu | Nỗi đau câu hỏi buổi tối + Property Expert trả lời từ hồ sơ nhà | Câu hỏi: có muốn xem trên listing của bạn không | Không |
| 2 | 3 | Góc mới | Kịch bản cụ thể: người mua quét QR, hỏi HVAC, xin xem nhà | Câu hỏi: đây có phải khoảng trống bạn muốn lấp | Không |
| 3 | 7 | Bằng chứng | Demo chạy thật, hơn một phút | Mở demo | 1 link demo |
| 4 | 14 | Chốt | Cho đường lui + một dòng về Realisa | Trả lời "demo" | Không |

Email 2, 3, 4 gửi cùng thread với email 1 (subject bắt đầu bằng "Re:" do công cụ tự thêm).

---

## 4. Biến cần có trong danh sách

| Biến | Ý nghĩa | Ghi chú |
|---|---|---|
| `{{first_name}}` | Tên agent | Bắt buộc. Đặt giá trị dự phòng "there" nếu trống (thành "Hi there,"). Merge field lỗi ("Hi ," hay "Hi {{first_name}}" hiện nguyên) tệ hơn không cá nhân hóa |
| `{{address}}` | Địa chỉ listing đầy đủ | Cần nguồn dữ liệu listing |
| `{{street}}` | Số nhà và tên đường (ví dụ "1428 Maple Ave") | Dùng trong subject |
| `{{physical_address}}` | Địa chỉ vật lý của công ty | Bắt buộc (CAN-SPAM). Chưa có |
| `{{demo_link}}` | Link demo | Chưa chốt domain, xem mục 8 |

### Người gửi và chữ ký (persona Eric)

| Mục | Giá trị |
|---|---|
| Người gửi | Eric, Growth Manager, ReallyWise |
| From | Eric RWise <eric@reallywise.ai> (theo sender hiện có). Có thể cân nhắc đổi tên hiển thị thành "Eric from ReallyWise" cho khớp cách viết tên của brand |
| Reply-to | Cùng địa chỉ, Eric đọc và trả lời |
| Giọng văn | Ngôi thứ nhất ("I"), thẳng, ngắn, như một Growth Manager nhắn cho đồng nghiệp trong ngành. Không văn phong quảng cáo |

**Chữ ký (dùng cho cả 4 email, plain text):**

```
Eric
Growth Manager, ReallyWise
eric@reallywise.ai
{{physical_address}}

Not relevant? Reply "stop" and I won't write again.
```

Ghi chú chữ ký:
- Không logo, không banner, không link website. Domain `reallywise.ai` chưa deploy theo README, và email cold nên hạn chế link và ảnh.
- Chưa có số điện thoại (bạn chưa cung cấp). Nếu muốn thêm, đặt dưới email.
- Mỗi email đều có địa chỉ vật lý và cách hủy đăng ký (yêu cầu CAN-SPAM với email thương mại).
- Dòng "Not relevant?..." dùng thống nhất ở cả 4 email.

**Bản dự phòng khi chưa có địa chỉ listing** (ví dụ danh sách chỉ có tên và email agent): dùng các câu thay thế ở mục 6.

---

## 5. Nội dung chi tiết 4 email

Tất cả là plain text. Số từ là ước lượng.

### Email 1 | Ngày 0 | Mở đầu

**Subject A:** `{{street}} buyer questions`
**Subject B:** `Question about {{street}}`

```
Hi {{first_name}},

Congrats on the new listing at {{address}}. When a buyer wonders about the roof, HVAC or HOA late at night, you're usually offline.

I'm Eric from ReallyWise. We built Property Expert for listing agents: when a buyer scans the yard sign or opens a link, it answers from the home's own documents, with sources, and alerts you if they ask for a tour.

Would it be useful to see how that would look on {{address}}?

Eric
Growth Manager, ReallyWise
eric@reallywise.ai
{{physical_address}}

Not relevant? Reply "stop" and I won't write again.
```

*(khoảng 77 từ, chưa tính chữ ký)*

**Ghi chú:**
- Câu "you're usually offline" là giả thuyết, chưa có số liệu. Nếu không muốn khẳng định, đổi thành "when you can't answer right away".
- **Cấu trúc theo best practice:** câu mở đầu về listing của họ, rồi một câu giới thiệu Eric, rồi giá trị kèm bằng chứng sản phẩm, rồi một câu hỏi nhẹ.
- **Câu giới thiệu** ("I'm Eric from ReallyWise. We built Property Expert for listing agents") đặt sau câu mở đầu, không mở bằng "My name is...". Chức danh, liên hệ ở chữ ký.
- **Dòng bằng chứng:** chưa có khách hàng hay số liệu có nguồn, nên dùng bằng chứng sản phẩm ("answers from the home's own documents, with sources"). Khi có kết quả thật của một khách hàng tương tự thì thêm một câu ngắn ở đây.
- Email 2, 3, 4 gửi cùng thread nên không cần giới thiệu lại.
- Nguồn trong deck: slide 03 (Property Expert), slide 09 (How it works).
- "Answers come from the home's own documents" phụ thuộc agent hoặc team tải hồ sơ nhà lên. Cần xác nhận quy trình (xem mục 8).

**Bản dự phòng (không có địa chỉ listing):**

```
Hi {{first_name}},

When a buyer wonders about the roof, HVAC or HOA late at night, most listing agents are offline.

I'm Eric from ReallyWise. We built Property Expert for listing agents: when a buyer scans the yard sign or opens a link, it answers from the home's own documents, with sources, and alerts you if they ask for a tour.

Would it be useful to see how that would look on one of your listings?
```

Subject dự phòng: `After-hours buyer questions`

**Bản đối chứng (control) để A/B test: không có câu giới thiệu Eric**

```
Hi {{first_name}},

Congrats on the new listing at {{address}}. When a buyer wonders about the roof, HVAC or HOA late at night, you're usually offline.

ReallyWise Property Expert answers those when a buyer scans the yard sign or opens a link. Answers come from the home's own documents, with sources, and you get an alert when a buyer asks for a tour.

Would it be useful to see how that would look on {{address}}?
```

Dùng cùng chữ ký, cùng subject, cùng nhóm đối tượng. Chỉ khác ở câu giới thiệu.

---

### Email 2 | Ngày 3 | Góc mới: kịch bản cụ thể

**Subject:** cùng thread với email 1 (ví dụ `Re: {{street}} buyer questions`)

```
Hi {{first_name}}, here's what it looks like from the buyer's side.

Tuesday night, someone scans the sign at {{address}} and asks, "Any HVAC issues?"

They get an answer from the inspection report, with the source and date. Then they ask, "Can I tour this Saturday?" You get a tour request with the full chat, so you know what they care about before you call back.

Is that a gap you'd want covered on your listings?

Eric
Growth Manager, ReallyWise
eric@reallywise.ai
{{physical_address}}

Not relevant? Reply "stop" and I won't write again.
```

*(khoảng 75 từ, chưa tính chữ ký)*

**Ghi chú:**
- Nguồn trong deck: slide 03 (ví dụ chat "Any HVAC issues?", "Can I schedule a tour this Saturday?", thông báo "New tour request"), slide 04 (Selling side).
- Đây là kịch bản minh họa, không nêu là kết quả thật của khách hàng.
- Không dùng trường học hay mô tả khu dân cư (Fair Housing).

**Bản dự phòng (không có địa chỉ):** thay "at {{address}}" bằng "at one of your listings", và "the sign at {{address}}" bằng "the sign at one of your listings".

---

### Email 3 | Ngày 7 | Bằng chứng: demo

**Subject A:** `See it as a buyer`
**Subject B:** `60-second demo`

```
Hi {{first_name}},

Rather than describe it, here's a working demo on a sample listing in Austin. Ask it anything a buyer would, then open the agent view to see the lead it creates.

{{demo_link}}

It takes a little over a minute. If it looks useful, I can show you how it would work on {{address}}.

Eric
Growth Manager, ReallyWise
eric@reallywise.ai
{{physical_address}}

Not relevant? Reply "stop" and I won't write again.
```

*(khoảng 55 từ, chưa tính chữ ký)*

**Ghi chú:**
- Nguồn trong deck: slide 10 ("Be the buyer", guided demo khoảng 1 phút) và slide 11 ("Be the agent", 6 bước).
- Câu "I can show you how it would work on {{address}}" chỉ dùng nếu team làm được demo theo listing của từng agent (xem mục 8). Nếu chưa, đổi thành "If it looks useful, I'm happy to walk you through it live."
- Đây là email duy nhất có link. Có thể bật theo dõi click chỉ cho link này.
- Không đặt `{{demo_link}}` bằng link github.io nếu tránh được (domain lạ làm giảm độ tin cậy).

---

### Email 4 | Ngày 14 | Chốt

**Subject:** cùng thread (ví dụ `Re: {{street}} buyer questions`), hoặc `Should I close the loop?`

```
Hi {{first_name}},

I'll stop here so I don't clutter your inbox.

One last thing: Realisa, the assistant inside ReallyWise, sends agents a morning brief with tour requests, deadlines and buyers who've gone quiet, and drafts the follow-ups.

If after-hours buyer questions aren't a priority right now, no problem. If they are, reply "demo" and I'll send a link.

Eric
Growth Manager, ReallyWise
eric@reallywise.ai
{{physical_address}}

Not relevant? Reply "stop" and I won't write again.
```

*(khoảng 58 từ, chưa tính chữ ký)*

**Ghi chú:**
- Nguồn trong deck: slide 06 (Realisa, morning brief "3 buyers quiet for 5 days, I drafted a follow-up for each").
- Email chốt, lịch sự, cho đường lui. Không thêm áp lực.

---

## 6. Xử lý phản hồi

Soạn sẵn câu trả lời ngắn, người thật gửi. Không tự động trả lời nội dung phức tạp.

| Loại phản hồi | Cách xử lý |
|---|---|
| "Yes / show me" | Gửi `{{demo_link}}` và đề xuất 15 phút. Không nói giá nếu chưa chốt |
| "Not now" | Cảm ơn, hỏi có nên liên hệ lại sau 3 tháng, ghi chú vào CRM |
| "Who are you / how did you get my email?" | Trả lời trung thực về nguồn email (ghi rõ nguồn thật), nói ngắn về sản phẩm, đề nghị xóa nếu họ muốn |
| "Stop / unsubscribe" | Xử lý ngay, thêm vào suppression, xác nhận bằng một dòng. Hạn chót pháp lý là 10 ngày làm việc |
| Auto-reply, out of office | Giữ trong sequence, dời lịch nếu có ngày quay lại |
| Bounce | Thêm vào suppression, không gửi lại |

---

## 7. Cách đo và test

- **Chỉ số chính:** số reply tích cực, số cuộc hẹn demo đặt được, số click vào demo (email 3).
- **Chỉ số an toàn:** spam complaint (giữ dưới 0.3%), bounce, số hủy đăng ký. Tạm dừng nếu bounce hoặc complaint tăng bất thường.
- **Không dùng open rate làm chỉ số chính** (tracking pixel không chính xác và làm giảm deliverability).
- **A/B test từng yếu tố một:** ví dụ email 1 có và không có câu giới thiệu Eric (bản đối chứng ở mục 5), hoặc Subject A và B, giữ nguyên các phần còn lại.
- **Mẫu đầu tiên 50 đến 100 người** chỉ để kiểm tra vận hành và deliverability, chưa đủ để kết luận phiên bản nào tốt hơn. Một nguồn khuyên ít nhất khoảng 200 email mỗi phiên bản khi A/B test (chưa kiểm chứng). Sau khi xem kết quả mới mở rộng.
- Ghi lại: danh sách đã gửi, ngày, phản hồi, để lần sau không gửi trùng.

Tham chiếu: các con số reply rate phổ biến trên blog (khoảng 3 đến 5% là trung bình, trên 10% là tốt) chỉ mang tính tham khảo vì đến từ vendor.

---

## 8. Việc cần xác nhận trước khi gửi

| # | Câu hỏi | Ai trả lời |
|---|---|---|
| 1 | Địa chỉ vật lý của công ty để đưa vào chữ ký (CAN-SPAM) là gì? Eric có muốn thêm số điện thoại không? | Eric / James |
| 2 | Link demo dùng domain nào? Domain `reallywise.ai` đã deploy chưa? Demo hiện trỏ tới `reallywise.ai/expert/123-main-street` | Team kỹ thuật |
| 3 | Có làm được demo trên đúng listing của từng agent không? Quy trình tải hồ sơ nhà (disclosure, inspection) thế nào? | Team sản phẩm |
| 4 | Các tuyên bố "answers with sources", "never guesses", "no login, no form" có đúng với bản đang chạy không? | Team sản phẩm |
| 5 | Có số liệu nào đã có nguồn (ví dụ thời gian reply trung bình, % lead không được follow-up) để dùng không? Hiện deck ghi "15 hours" và "~50%" nhưng không có nguồn | Team / marketing |
| 6 | Nguồn danh sách listing agent và trigger "new listing" lấy từ đâu? Email lấy từ đâu và có hợp lệ để gửi không? | Compliance / growth |
| 7 | Công cụ cold email nào được dùng và điều khoản của công cụ đó có cho phép outbound không? | Growth |
| 8 | Tên "Property Expert", "Realisa" có giữ nguyên trong email không? (Hiện giữ nguyên.) | Brand |
| 9 | Có bằng chứng thật (khách hàng, pilot, số liệu có nguồn) để thêm một câu proof vào email 1 không? Nếu chưa có thì giữ bằng chứng sản phẩm như hiện tại | Team / James |
| 10 | Câu giới thiệu "We built Property Expert for listing agents" có đúng cách team muốn mô tả sản phẩm không? | Brand / James |

---

## 9. Bước tiếp theo

1. Duyệt nội dung 4 email ở mục 5, chỉnh giọng văn nếu cần.
2. Chốt các mục trong mục 8.
3. Làm template HTML theo brand ReallyWise (header navy, logo reversed, thân trắng, nút navy, font dự phòng, rộng 600 px) cho giai đoạn sau khi họ trả lời hoặc đặt demo. Email cold 1 đến 4 giữ plain text.
4. Dựng danh sách test 50 đến 100 người và chạy thử.

---

## Phụ lục: nguồn nội dung

- Deck sản phẩm: `product-presentation.html` (slide 03 Property Expert, slide 04 Selling side, slide 06 Realisa, slide 09 How it works, slide 10 và 11 demo).
- Brand: `reallywise/brand/ReallyWise-Brand-Guideline.html` (giọng văn, màu, font, email 600 px).
- Quy định và best practice outbound đã tổng hợp ở các tin nhắn trước (CAN-SPAM, điều kiện bulk sender của Gmail/Yahoo, chính sách chống spam của Brevo, hướng dẫn cold email). Nhiều nguồn là blog vendor nên các con số chỉ để tham khảo.
