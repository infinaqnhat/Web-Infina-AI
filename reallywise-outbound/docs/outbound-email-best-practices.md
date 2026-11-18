# Best practice email outbound (cold email) cho ReallyWise

> **Trạng thái:** DRAFT v1, tổng hợp từ web search ngày 2026-11-10 và 2026-11-11.
> **Đối tượng áp dụng:** outbound cho listing agent tại Mỹ.
> **Đi kèm:** `reallywise-outbound-email-plan.md` (nội dung chi tiết 4 email).
> **Không phải tư vấn pháp lý.**

## Cách đọc tài liệu này

Gần như mọi nguồn dưới đây là blog của công ty bán công cụ cold email hoặc dữ liệu nội bộ của họ. Con số về hiệu quả chỉ để tham khảo hướng, không phải benchmark độc lập. Mỗi ý có nhãn:

| Nhãn | Ý nghĩa |
|---|---|
| **[Đồng thuận]** | Nhiều nguồn nói giống nhau |
| **[Tranh cãi]** | Các nguồn nói khác nhau, cần test trên danh sách của mình |
| **[Chưa kiểm chứng]** | Một nguồn, hoặc không có dữ liệu công khai |
| **[Nguồn chính thức]** | Cơ quan quản lý hoặc chính sách của nhà cung cấp |

---

## 1. Cấu trúc một email cold

Cấu trúc phổ biến trong các hướng dẫn: **lý do liên hệ, lý do ngay lúc này, bạn làm gì, một dòng bằng chứng, rồi một lời hỏi nhẹ.** [Chưa kiểm chứng, tổng hợp từ nhiều guide]

| Thành phần | Quy tắc | Nhãn |
|---|---|---|
| Câu đầu | Nói về tình huống của người nhận (listing, khu vực), không mở bằng "My name is..." hay "Let me introduce myself" | Đồng thuận |
| Giới thiệu | Một câu ngắn, nêu vai trò trước tên, gắn vai trò với lĩnh vực của họ. Tên, chức danh, công ty, liên hệ để ở chữ ký | Đồng thuận (nhưng có guide vẫn khuyên giới thiệu ngắn trong thân) |
| Giá trị | Đưa giá trị trong khoảng 40 từ đầu | Chưa kiểm chứng |
| Bằng chứng | Một câu về độ tin cậy, không phải tiểu sử. Nếu để sâu trong email, hầu hết người đọc bỏ qua | Chưa kiểm chứng |
| CTA | Một lời hỏi, ít áp lực | Đồng thuận |

**Bằng chứng nên viết thế nào:** một kết quả cụ thể của khách hàng tương tự thì tốt nhất ("We helped X do Y in Z"), hoặc một câu như "I work with..." / "I built...". Nếu chưa có khách hàng hay số liệu thật thì không bịa. Có thể dùng bằng chứng sản phẩm (ví dụ "answers come from the home's own documents, with sources"). Một guide khuyên test có và không có dòng bằng chứng.

**Nếu có người quen chung,** nêu sớm ("Following up on [name]'s recommendation") vì giúp tăng tin cậy.

---

## 2. Subject line

- **Ngắn, khoảng 3 đến 5 từ.** Một nghiên cứu của Reply.io thấy reply rate giảm khi subject từ 5 từ trở lên, open rate gần như không đổi theo độ dài. Nguồn khác nói 8 từ trở lên làm giảm cả open và reply. [Đồng thuận về hướng, con số là của vendor]
- **Khớp với nội dung email.** Subject tạo cảm giác khẩn cấp hoặc gợi tò mò mà thân email không đáp ứng thì làm giảm reply. [Một nguồn]
- **Không viết toàn chữ thường.** Reply.io ghi nhận subject toàn chữ thường có open thấp hơn 3.46% và reply thấp hơn 11%. [Một nguồn]
- **Địa chỉ listing trong subject** được một số vendor cho là tăng open rate 2 đến 3 lần nhưng không có dữ liệu công khai. [Chưa kiểm chứng]
- Open rate đo bằng tracking pixel nên không đáng tin. Đo bằng reply.

---

## 3. Độ dài và định dạng

**Độ dài**
- Lemlist: dưới 120 từ, lý tưởng 80 đến 100. Prospeo: dưới 75 từ. Reply.io: template 2 đến 3 đoạn có reply rate cao nhất. [Đồng thuận về "ngắn"]
- Một bài của LeadHaste lập luận email quá ngắn có thể nhiều phản hồi "not interested" hơn, email dài hơn ít phản hồi hơn nhưng chất lượng hơn. [Tranh cãi]

**Plain text hay HTML**
- Khuyến nghị phổ biến: email đầu dùng plain text hoặc HTML rất đơn giản. Ảnh nhúng, nhiều link, tracking pixel là các tín hiệu làm tăng nguy cơ vào spam. [Đồng thuận]
- Con số "plain text hơn 15 đến 25 điểm reply rate" của FirstSales và "15% inbox placement" của LeadContact không có dữ liệu công khai truy được. [Chưa kiểm chứng]
- HubSpot thấy deliverability của HTML và plain text tương đương nếu làm đúng cách. Một case study của Migma lập luận HTML sạch có thể tăng độ tin cậy, nhưng đó là tài liệu vendor. [Tranh cãi]
- Nếu dùng HTML, luôn gửi kèm bản plain text (multipart). Giữ HTML nhẹ. Ảnh, bố cục, style để dành cho email sau, khi người nhận đã tương tác. [Đồng thuận]
- Chữ ký: các guide nói nên có tên, chức danh, công ty, thông tin liên hệ để người nhận thấy đây là người thật. Không có hướng dẫn cụ thể hơn về chữ ký trong các nguồn.

**Link và theo dõi**
- Tracking pixel và link tracking là rủi ro lớn nhất cho email cold, nhiều nguồn khuyên bỏ hoặc giảm ở email đầu. [Đồng thuận]

---

## 4. Chào hỏi và cá nhân hóa

- **Chào bằng tên:** dữ liệu vendor cho thấy tăng reply rate khiêm tốn (một nguồn: 6.4% so với 5.2% khi chào chung). Một phân tích khác ghi "Hey [Name]" cao hơn "Hi [Name]" nhưng nguồn khác khuyên "Hi" làm mặc định. [Tranh cãi]
- **Không có nghiên cứu nào so sánh có chào và không chào.** [Chưa kiểm chứng] Cách duy nhất để biết là test trên danh sách của mình.
- **Merge field lỗi tệ hơn không cá nhân hóa.** "Hi ," hoặc "Hi {{first_name}}" hiện nguyên là lỗi nghiêm trọng. Luôn đặt giá trị dự phòng cho trường trống. [Đồng thuận]
- **Cá nhân hóa mức cơ bản** (tên, công ty) tăng nhẹ (một nguồn: khoảng 8%). **Cá nhân hóa dựa trên tín hiệu thật** (listing mới, sự kiện cụ thể) hiệu quả hơn nhiều (một nguồn: 56%). Đây là dữ liệu vendor và chỉ là tương quan. [Chưa kiểm chứng]
- **Kết luận thực hành:** một câu mở đầu liên quan và cụ thể quan trọng hơn việc chọn chào "Hi" hay "Hey".

---

## 5. CTA và follow-up

**CTA**
- Một CTA duy nhất, dạng câu hỏi dễ trả lời. [Đồng thuận]
- Hunter khuyên follow-up đổi CTA để việc trả lời ít áp lực hơn ("rejection then retreat"). [Một nguồn]

**Số lượng và nhịp**
- Woodpecker: 3 đến 5 follow-up, tổng 4 đến 6 email. Close: tối đa 4 follow-up. [Đồng thuận]
- Khoảng cách tăng dần: 2 đến 3 ngày đầu, rồi 5 đến 7 ngày, rồi 7 đến 10 ngày. [Đồng thuận về hướng]
- Mỗi follow-up phải thêm một góc mới (tình huống, bằng chứng, câu hỏi khác), không chỉ "just checking in." [Đồng thuận]
- Một nguồn nói 95% reply đến trong 3 follow-up đầu nhưng không nói cách đo. [Chưa kiểm chứng]
- Gửi 10 email trở lên cho người không phản hồi không làm tăng khả năng trả lời, còn có thể bị gắn nhãn spam. [Một nguồn]
- Dừng khi có tín hiệu (trả lời, hủy, bounce), không chỉ dừng theo số lần. [Một nguồn]
- Thời điểm gửi: một vendor khuyên tránh thứ Hai và thứ Sáu. [Chưa kiểm chứng, giai thoại]

---

## 6. Hạ tầng gửi (deliverability)

*Phần tham khảo. Không nằm trong checklist của file plan.*

- **Xác thực:** SPF, DKIM, DMARC. Domain trong From phải khớp (alignment) với SPF hoặc DKIM thì DMARC mới pass. DMARC bắt đầu `p=none`, có thể nâng dần lên quarantine rồi reject. Với Outlook/Hotmail/Live, SPF và DKIM phải pass. [Đồng thuận]
- **Gmail và Yahoo yêu cầu DMARC cho bulk sender (khoảng 5,000 email mỗi ngày trở lên) từ tháng 2/2024.** Microsoft cũng dùng ngưỡng 5,000 mỗi ngày, các nhà cung cấp có thể không dùng chung một định nghĩa. Kiểm tra trên trang chính thức của từng bên trước khi dựa vào chi tiết. [Chủ yếu từ blog vendor]
- **Spam complaint dưới 0.3%** là ngưỡng thường được trích dẫn. [Đồng thuận]
- **One-click unsubscribe (RFC 8058)** cho email marketing. [Đồng thuận]
- **Hậu quả khi không tuân thủ:** các nguồn nói khác nhau (vào spam, bị từ chối SMTP, hoặc không tới được cả thư mục spam). Chưa rõ chính xác. [Tranh cãi]
- **Warm-up domain mới và giữ lượng gửi mỗi hộp thư khiêm tốn.** Không có con số thống nhất giữa các nguồn. [Đồng thuận về hướng]
- Qua xác thực không bảo đảm vào inbox. Danh tiếng riêng của từng nhà cung cấp mới quyết định.

---

## 7. Tuân thủ (US, CAN-SPAM)

[Nguồn chính thức: hướng dẫn CAN-SPAM của FTC; các điểm bổ sung từ blog]

- **Không có ngoại lệ cho B2B.** CAN-SPAM áp dụng cho mọi email thương mại, cả B2B.
- **Cần có:** header và subject không gây hiểu lầm, nêu rõ đây là quảng cáo, địa chỉ vật lý hợp lệ, cách hủy đăng ký rõ ràng.
- **Hủy đăng ký:** xử lý trong 10 ngày làm việc. Cơ chế hủy phải hoạt động ít nhất 30 ngày sau khi gửi. Không được thu phí hay yêu cầu gì ngoài địa chỉ email. Nếu có menu loại tin, phải có lựa chọn dừng mọi email marketing.
- **Sau khi hủy:** không bán hoặc chuyển địa chỉ đó (trừ nhà cung cấp dịch vụ giúp tuân thủ).
- **Mức phạt:** FTC liệt kê tới khoảng $53,088 mỗi email vi phạm. Con số này có thể đã điều chỉnh theo lạm phát, cần kiểm tra trang FTC hiện hành.
- Ngoài CAN-SPAM, tùy trường hợp có thể áp dụng luật bang (ví dụ CCPA ở California). Cần ý kiến luật sư.
- **Fair Housing** (ngành bất động sản): không dùng cụm mang tính phân biệt hoặc mô tả dân cư như "family-friendly", "safe neighborhood". Theo Brand Guideline của ReallyWise, chỉ dùng dữ liệu khách quan.

---

## 8. Riêng cho listing agent (bất động sản)

Các nguồn là blog về cold email cho bất động sản, hầu hết do vendor công cụ viết. AgentFire nhận xét cold email cho bất động sản thường mang lại ROI thấp.

- **Mở bằng câu hỏi, không phải lời chào hàng.** Email chung chung ("I'm an investor, do you have off-market deals?") bị lẫn giữa rất nhiều email tương tự agent nhận mỗi tuần. [Đồng thuận trong nhóm bài về real estate]
- **Dùng trigger cụ thể:** listing mới, listing tồn lâu, thay đổi giá. Email nêu một trigger cụ thể được đọc nhiều hơn email giới thiệu công ty. Smartlead lưu ý số liệu của họ đến từ commercial property finance, chưa đo cho outreach agent. [Một nguồn]
- **Cho giá trị cục bộ dùng được ngay** (insight về khu vực, tình huống thực). [Đồng thuận]
- **Dùng chuỗi nhiều email,** không chỉ một. [Đồng thuận]
- **Khẳng định kiểu "2 đến 3 lần hiệu quả hơn"** khi phân đoạn hoặc dùng địa chỉ trong subject không có dữ liệu công khai đi kèm. [Chưa kiểm chứng]

---

## 9. Đo lường và test

- **Chỉ số chính:** reply tích cực và cuộc hẹn đặt được. Reply rate phổ biến chỉ khoảng 3 đến 5%, campaign tốt vượt 10%. Reply rate đơn thuần có thể gây hiểu lầm nên theo dõi cả reply chất lượng. [Chưa kiểm chứng, nguồn DEV Community]
- **Chỉ số an toàn:** spam complaint, bounce, hủy đăng ký.
- **A/B test từng yếu tố một** (subject, câu mở đầu, CTA, có hay không câu giới thiệu).
- **Cỡ mẫu:** một nguồn khuyên ít nhất khoảng 200 email mỗi phiên bản khi test greeting. Một mẫu 50 đến 100 người chỉ đủ để kiểm tra vận hành và deliverability, chưa đủ kết luận phiên bản nào tốt hơn. [Một nguồn]
- Tự test với danh sách của mình thay vì tin benchmark chung.

---

## 10. Áp dụng cho sequence 4 email của ReallyWise

Dựa trên `reallywise-outbound-email-plan.md` (v1, gửi từ Eric, Growth Manager).

| Điểm | Hiện trạng | Theo best practice |
|---|---|---|
| Chào hỏi | Có "Hi {{first_name}}," (email 2 mở thẳng bằng tên) | Phù hợp. Đặt giá trị dự phòng cho `{{first_name}}` |
| Câu mở đầu | Nói về listing của họ | Đúng hướng |
| Giới thiệu bản thân | Chỉ có trong chữ ký | **Thiếu một câu ngắn** nêu bạn là ai và liên quan gì tới họ |
| Dòng bằng chứng | Chưa có | **Thiếu.** Hiện chưa có khách hàng hay số liệu có nguồn. Có thể dùng bằng chứng sản phẩm hoặc để trống |
| Độ dài | Khoảng 65 đến 85 từ | Trong khoảng khuyến nghị. Thêm câu giới thiệu sẽ dài hơn |
| CTA | Một câu hỏi mỗi email | Phù hợp |
| Định dạng | Plain text, 1 link duy nhất (email 3) | Phù hợp |
| Mỗi follow-up một góc mới | Có (tình huống, demo, Realisa) | Phù hợp |
| Số lần và nhịp | 4 email, ngày 0, 3, 7, 14 | Nằm trong khoảng nguồn khuyên |
| Footer | Có địa chỉ vật lý và cách hủy ở cả 4 email | Phù hợp CAN-SPAM |
| Số liệu | Không dùng "15 hours", "~50%" vì chưa có nguồn | Đúng |
| Fair Housing | Không nói trường học hay khu dân cư | Đúng |

**Đề xuất test tiếp theo (chưa làm):**
1. Hai phiên bản email 1: (A) như hiện tại; (B) thêm một câu giới thiệu Eric sau câu mở đầu, ví dụ "I'm Eric from ReallyWise, we build AI tools for listing agents."
2. Cần mẫu đủ lớn để kết luận (xem mục 9).

**Giai đoạn sau khi họ trả lời hoặc đặt demo:** dùng template HTML theo brand ReallyWise (600 px, header navy với logo reversed, thân nền trắng, nút navy, font dự phòng). Email cold 1 đến 4 giữ plain text.

---

## Nguồn

**Chính thức**
- [FTC: CAN-SPAM Act compliance guide for business](https://www.ftc.gov/business-guidance/resources/can-spam-act-compliance-guide-business)

**Cấu trúc, giới thiệu, bằng chứng**
- [SmartReach: cold email opening lines](https://smartreach.io/blog/how-to-start-an-email/)
- [Autoklose: cold email openers](https://www.autoklose.com/?p=6462)
- [WarmupInbox: how your first cold email should look](https://warmupinbox.com/?p=1580)
- [Woodpecker: introduction in cold email](https://woodpecker.co/blog/?p=50475)
- [Atlassian: how to introduce yourself in an email](https://www.atlassian.com/blog/loom/how-to-introduce-yourself-in-an-email)
- [Zeliq: business introduction email](https://www.zeliq.com/blog/business-introduction-email-templates)
- [Instantly: proposal email opening hook frameworks](https://instantly.ai/blog/proposal-email-opening-hook-frameworks/)
- [Beeving: anatomy of a cold email](https://beevingcom.pages.dev/learn/foundations/anatomy-of-a-cold-email/)
- [Lemlist: social proof in cold email](https://proxy.lemlist.com/blog/how-to-leverage-social-proof-in-a-cold-email)

**Subject, độ dài, chào hỏi**
- [Reply.io: subject lines according to data](https://reply.io/reply-research-subject-lines/)
- [Reply.io: how to write cold emails that convert](https://reply.io/guide-to-cold-emailing)
- [Lemlist: 47 cold email tips](https://help.lemlist.com/en/articles/4452701-47-cold-email-tips-guaranteed-to-skyrocket-your-reply-rate-to-the-moon)
- [Instantly: cold email subject line myths](https://instantly.ai/blog/cold-email-subject-line-myths-debunked-what-data-really-shows)
- [LeadHaste: cold email length 2026](https://leadhaste.com/blog/cold-email-length-best-practices-2026)
- [Instantly: email greeting benchmarks 2026](https://instantly.ai/blog/email-greeting-benchmarks-2026-industry-standards-for-reply-rates-open-rates/)
- [Prospeo: cold email greeting data](https://prospeo.io/s/cold-email-greeting)
- [Rework: personalization at scale](https://resources.rework.com/libraries/outbound-prospecting/personalization-at-scale)

**Plain text và HTML**
- [FirstSales: plain text vs HTML cold email](https://firstsales.io/blog/plain-text-vs-html-cold-email/)
- [HubSpot: plain text vs HTML email data](https://blog.hubspot.com/marketing/plain-text-vs-html-emails-data)
- [Warmforge: plain text vs HTML in cold emails](https://warmforge.ai/blog/plain-text-vs-html-in-cold-emails)
- [Hunter: is HTML harming your cold email deliverability](https://hunter.io/blog/is-html-harming-your-cold-email-deliverability/)

**Follow-up**
- [Hunter: cold email sequence](https://hunter.io/blog/cold-email-sequence)
- [Nutshell: how many follow-up emails](https://www.nutshell.com/blog/how-many-sales-emails-should-you-send)

**Deliverability**
- [Folderly: Gmail, Yahoo, Microsoft sender requirements 2026](https://lens.folderly.com/blog/gmail-yahoo-microsoft-sender-requirements-2026)
- [Instantly: 90%+ cold email deliverability](https://instantly.ai/blog/how-to-achieve-90-cold-email-deliverability-in-2025/)
- [Bitscale: SPF, DKIM, DMARC setup guide](https://bitscale.ai/blogs/cold-email-deliverability-in-2026)

**Bất động sản**
- [Omni Online Strategies: what to say in a cold email to a listing agent](https://omnionlinestrategies.com/blog/what-to-say-cold-email-listing-agent)
- [AgentFire: cold emails and CAN-SPAM for real estate](https://agentfire.com/?p=107606)
- [Smartlead: real estate cold email](https://www.smartlead.ai/email-templates/real-estate-cold-email)

**Nội bộ**
- `reallywise/brand/ReallyWise-Brand-Guideline.html` (giọng văn, màu, font, email 600 px)
- `product-presentation.html` (nội dung sản phẩm)
