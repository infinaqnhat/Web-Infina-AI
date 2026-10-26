# Refresh Log

Log các lần đã check/sửa bài qua skill `post-refresh`, dùng để tránh check lại 1 trang quá dày
(chờ ít nhất 2-3 tuần sau khi sửa để Google phản ánh thay đổi vào dữ liệu) và theo dõi hiệu quả
các lần sửa trước. Thêm dòng mới vào **đầu bảng**, không phải cuối bảng. Khi bảng vượt khoảng
100-150 dòng, xóa bớt các dòng cũ nhất ở cuối để tránh phình file tốn context khi đọc.

| Ngày check | URL | Chẩn đoán | Đã sửa gì | Kết quả | Số liệu trước khi sửa |
|---|---|---|---|---|---|
| 2026-10-23 | https://infina.ai/news/listing-leads/ (#2262, hub Cụm 10) | Inbound link cho bài news mới #2349 (`price-reduction-conversation-with-sellers`), bước 6.5c của routine daily | Thêm 1 câu 'If the home later sits, our guide to a price reduction conversation with sellers shows how to raise it.' vào đoạn 'Prepare before you arrive' (mục Turn a Seller Lead Into a Listing Appointment) | đã sửa; verify REST: chỉ thêm 1 câu và 1 link, không mất gì | #2262 live từ 14:00 hôm nay, chưa có số liệu GSC |
| 2026-10-23 | https://infina.ai/news/real-estate-lead-follow-up-automation-guide/ (#1223, pillar Cụm 7) + https://infina.ai/news/crm-pipeline-management/ (#277) + https://infina.ai/news/crm-management-real-estate-agents-beginners-guide/ (#405) | Theo yêu cầu: gộp chủ đề lead management vào pillar Cụm 7 thay vì tạo Cụm 11 (plan `plan-cum-11-lead-management.md`: volume chỉ 500/50, trùng Cụm 2 và 7). Không dùng GSC. | **#1223**: thêm đoạn giới thiệu và H2 "Real Estate Lead Management: Where Follow-Up Fits" (định nghĩa 5 việc, ảnh `nywzSUwz.jpg`, 3 H3: cách chia lead cho team theo Real Geeks và iHomefinder kèm ảnh `yuPmMTpu.jpg`, bảng tính spreadsheet hay CRM, cách tính lead conversion rate theo công thức của Follow Up Boss, không nêu benchmark), link thêm tới #2260, #277, #405, #207, #1415, #1278. **#277**: thêm H2 "Lead Management vs Pipeline: What to Track for Every Lead" (bảng 6 trường, cách đo từng stage), link #1223 và #405. **#405**: thêm 2 H2 ("Is CRM Management the Same as Lead Management?", "Spreadsheet or CRM: Have You Outgrown a Sheet?"), link #1223 và #277. Title, meta, focus keyword giữ nguyên | đã sửa; verify bằng REST: 3 bài chỉ thêm nội dung (1223 sửa đúng 1 đoạn mở bài, 277 và 405 không xóa dòng nào), không mất link hay ảnh cũ, 1223 thêm 2 ảnh (3 thành 5) | 1223 (13/10): 2.483 chữ; 277 (12/10): 1.703 chữ; 405 (12/10): 1.166 chữ. Cả ba vừa sửa trong 2 tuần trước đó (bỏ qua quy tắc chờ 2-3 tuần theo yêu cầu của user) |
| 2026-10-23 | 18 bài Cụm 9 và liên quan: #1746, #1843, #1853, #1859, #1877, #1889, #1895, #1901, #1937, #1943, #1949, #1955, #1961, #1967, #1977, #1979, #2165, #2183 | Audit link nội bộ toàn site 23/10 (167 bài, đối chiếu rule trong internal-linking-guide và Bước 5/6.5). Phát hiện: đa dạng anchor dưới 70% ở 11 đích (tệ nhất #1843 24%, #1832 25%, #1825 41%); 4 bài Cụm 9 có dưới 2 link ngang (#1843 0, #1853 1, #1889 1, #1901 1); #1746 (Cụm 2) không trỏ lên pillar cụm; 5 bài chỉ có 1 inbound (#1901, #1943, #1977, #2183, #2189). | Việc 1: thêm link ngang cho #1843 (software, advertising), #1853 (referral), #1889 (name ideas, luxury), #1901 (social); thêm link lên pillar cho #1746 (best-crm-for-real-estate); thêm inbound cho 5 bài yếu: software từ #1843, google ads từ #1859, closing gifts từ #1961, email signature từ #1895, luxury từ #1889. Việc 2: viết lại anchor tới 3 đích tệ nhất, chỉ đổi chữ trong thẻ a, giữ nguyên href: tới #1843 đổi 9 anchor, tới #1832 đổi 7, tới #1825 đổi 8 (ở 18 bài trên); mọi anchor mới ≤8 từ, mô tả đúng trang đích. Verify REST sau khi ghi: text khớp bản dựng, href khớp, số ảnh không đổi, mọi link và ảnh 200. | Đo lại 23/10: đa dạng anchor tới #1843 76% (13/17), #1832 83% (10/12), #1825 77% (17/22); Cụm 9 còn 0 bài dưới 2 link ngang và 0 bài thiếu link pillar; inbound của 5 bài yếu lên 2 mỗi bài. Còn dưới 70%: 8 đích (bio, GBP, farming, postcards, business card, social, CRM marketing, CEP vs CRM). Cụm 1-8 còn 53/74 bài dưới 2 link ngang (nợ cũ, chưa làm) | Trước: #1843 24%, #1832 25%, #1825 41%; Cụm 9 4/26 bài dưới 2 link ngang |
| 2026-10-21 | https://infina.ai/news/real-estate-marketing/ (#1825, pillar) + https://infina.ai/news/real-estate-branding/ (#1832, hub) + #1877, #1967, #1961 | Verify + đợt link ngược wave 3 Cụm 9 sau khi cả 8 bài (#2165–#2207) live. Verify: 8 bài `publish` đúng giờ (19/10 10:00 tới 21/10 14:00), trang 200, mỗi bài 4 ảnh (hero + 3 mockup) và featured, mọi link nội bộ 200. Trước khi sửa: các bài wave 3 mới chỉ có link từ nhau. | Pillar #1825 Related Reading +6 bullet (farming, open house, video, door knocking, cold calling, letters). Hub #1832 +2 (luxury, email signature). #1877: farming (trong câu về farm area) + letters (sau câu về strangers in a farm area). #1967: open house + door knocking (2 mục trong phần distribute). #1961: cold calling (bước 'stay in touch'). Anchor ≤8 từ, mỗi cặp nguồn-đích một anchor, không trùng anchor đã dùng tới các đích này. Verify REST: text khớp bản push, link cũ giữ nguyên, ảnh không đổi, mọi link/ảnh 200. Inbound sau pass: farming 5, open house 2, video 2, luxury 1, email signature 1, letters 4, door knocking 3, cold calling 2. | Chờ GSC sau 2-3 tuần | Pillar 20 link Related Reading, hub 7. WARN còn lại: anchor 'real estate farming' trùng 2 lần trong wave 3 (#2195, #2201 trỏ #2165); #2183 và #2189 mới có 1 inbound (chỉ từ hub) |
| 2026-10-18 | https://infina.ai/news/real-estate-marketing/ (#1825, pillar) + https://infina.ai/news/real-estate-branding/ (#1832, hub) | Đợt link ngược wave 2 Cụm 9 sau khi cả 8 cluster live (#1937–#1979, status publish). Trước khi sửa: 8 bài wave 2 chưa có link từ pillar/hub. | Pillar Related Reading +8 bullet (GBP, Google Ads, testimonials, listing presentation, referral, flyer, closing gifts, realtor name), anchor ≤8 từ, mỗi bài 1 anchor. Hub Related Reading +2 bullet (testimonials, realtor name ideas), đổi câu intro. Verify REST: text khớp bản push, 23 link nội bộ pillar và 8 link hub không trùng, ảnh 6 và 5 như cũ. Inbound: mỗi bài ≥1 (testimonials và name ideas có 2). | Chờ GSC sau 2-3 tuần | Pillar 15 link Related Reading, hub 3 link |
| 2026-10-15 | https://infina.ai/news/real-estate-marketing/ (#1825, pillar) + https://infina.ai/news/real-estate-branding/ (#1832, hub) | Đợt link ngược wave 1 Cụm 9 sau khi cả 10 cluster live (200, category 392, có featured). Trước khi sửa: pillar chỉ link xuống 1 cluster (plan), hub chưa link xuống card/logo/bio; #1871, #1877, #1895, #1901 chưa có inbound nào từ Cụm 9. | Pillar: thêm mục Related Reading trước Final Thoughts với 6 link, mỗi cluster đúng 1 lần (ideas, advertising, social, seo, postcards, software), anchor 5-8 từ chưa dùng ở nơi khác. Hub: thêm Related Reading với 3 link (card, logo, bio). Verify live bằng REST: nội dung khớp bản dự kiến, không link trùng. | đã sửa | Inbound Cụm 9 sau sửa: pillar 8, hub 7, plan 8, ideas 3, advertising 3, social 2, seo 1, postcards 1, card 3, logo 2, bio 1, software 1 (mọi cluster wave 1 đều ≥1). Wave 2 (8 bài, 16-18/10) sẽ thêm vào cùng mục Related Reading khi live. |
| 2026-10-15 | https://infina.ai/news/best-free-crm-for-real-estate-agents/ (#438) | Routine 2 tuần/lần (GSC 14/09-12/10, 60 trang, 16 trang striking-distance). Các trang impressions cao nhất (#1056, #89, #207, #546, #637, #610, #1069) đều đã sửa trong 2-3 tuần nên bỏ qua. #438 là bất thường lớn nhất: 5.340 impr, vị trí TB 3,7, 6 click (CTR 0,11% so kỳ vọng ~11%). Hai query chính xếp rất cao nhưng 0 click: `crm for real estate agents free` (951 impr, pos 1,9) và `best free crm for realtors` (696 impr, pos 1,4). Kỳ trước chỉ 173 impr (pos 11,2), nên đây là bậc nhảy mới. **ĐÍNH CHÍNH cùng ngày (user gửi screenshot)**: vị trí 1,4-1,9 là vị trí trong khối **AI Overview**: Infina AI được trích làm nguồn (chip 'Infina AI +2') và có thẻ riêng ở cột phải với snippet lấy từ thân bài, không phải meta. Zero click là do AI Overview, không phải title/meta kém, và benchmark CTR theo vị trí không áp dụng cho impressions kiểu này. Gap rõ trên trang: query dùng `realtors` nhưng title, meta và thân bài gần như không có từ này (3 lần, đều trong anchor Related Reading); meta description dài 190 ký tự nên bị cắt. Không đổi title/slug/focus keyword (chưa đủ bằng chứng, bài đang xếp hạng cao). | (Tác động thực tế của sửa này gần như bằng 0 với các query AI Overview, vì snippet ở thẻ cột phải lấy từ thân bài.) Viết lại meta description (159 ký tự, có `realtors`, nêu HubSpot/Zoho/Bitrix24/Wise Agent trial và khi nào nên nâng cấp). Thêm `and realtors` vào câu thứ hai của phần mở bài. Nội dung khác giữ nguyên, đã verify live bằng REST. Chưa sửa các lỗi phụ đã thấy: bảng ghi 'Up to 3 users' ở cột Contact Cap và 'Unlimited (trial)' của Wise Agent chưa có nguồn, bài chưa link money page. | đã sửa | 28 ngày 14/09-12/10: 5.340 impr, 6 click, CTR 0,11%, pos 3,66. Kỳ trước 17/08-13/09: 173 impr, 1 click, pos 11,2. Không đổi title. Việc nên làm tiếp: sửa số liệu chưa có nguồn trong bảng (cột Contact Cap), đối chiếu giới hạn HubSpot/Zoho với trang chính hãng, và thêm Bigin by Zoho, Freshsales, Agile CRM mà AI Overview đang liệt kê (có nguồn) để giữ vị trí được trích. |
| 2026-10-13 | 20 bài → money page https://infina.ai/: #1232, #1449, #1234, #1487, #1223, #1227, #147, #1106, #1056, #1100, #110, #918 (ưu tiên 1) + #89, #1078, #1071, #223, #930, #1415, #1825, #214 (ưu tiên 2) | Money page live nhưng 0/153 bài link về trong thân bài (chỉ có link sitewide từ theme, anchor chung chung). | Thêm đúng 1 link/bài tới `https://infina.ai/` (URL sạch, không #fragment/UTM), 1 câu "Infina AI, our own product, ...", anchor ≤8 từ; 4 anchor khớp từ khoá "AI assistant for real estate agents" (#1449, #147, #1106, #1825). Verify qua REST sau mỗi bài: text khớp bản gốc + câu mới, không mất link nào, ngày/category/ảnh không đổi. Kế hoạch: `references/plan-money-page-links.md`. | 20/20 xong | n/a |
| 2026-10-13 | (docs) content-plan.md, pillar-cluster-writer/SKILL.md, cluster-roles.md, teardown-infina-table.md, used-keywords.md, plan-cum-9 | Đổi tên sản phẩm: RealSaleX / Real Sale X / AI Deal Room → **Infina AI**; money page `https://infina.ai/` đã live. | Thay tên ở nhãn 🎯, tiêu đề cụm, đoạn bối cảnh của skill; đóng mục "Money page URL" trong Việc còn lại. Các dòng log cũ bên dưới giữ nguyên tên cũ (lịch sử). | Chưa thêm link nào trong bài | n/a |
| 2026-10-06 | https://infina.ai/news/tcpa-compliance-for-real-estate-agents/ (#237) | Khép nốt link cross-cluster còn thiếu sau đợt verify 8/8 cụm. Bài #1462 (real-estate-broker-crm, Cụm 2, publish 04/10) có H2 "Compliance and Record Retention at the Brokerage Level" trỏ lên pillar #237 của Cụm 8, nhưng chiều ngược lại chưa có. Fetch REST xác nhận #237 chỉ link ra 3 bài cluster Cụm 8 + 2 link chéo sang Cụm 4 và Cụm 7, không có link nào xuống #1462. | Thêm 1 đoạn mới vào H2 "TCPA Compliance for Real Estate Agents in Practice", ngay sau đoạn nói về chọn AI platform. Góc: lưu trữ hồ sơ consent ở cấp brokerage khác cấp agent, nên cần hệ thống tập trung. Anchor text đúng FOCUS_KW của bài đích (`real estate broker crm`). Đoạn thêm có chèn 1 lần FOCUS_KW của chính #237 để bù density sau khi tăng số từ. | đã sửa xong, verify REST 2 chiều: #237 → #1462 LINKED, #1462 → #237 LINKED | #237 trước khi sửa: 1.053 từ, 6 lần FOCUS_KW, density 0,57%. Sau khi sửa: 1.154 từ, 7 lần, density 0,61%, vẫn trong ngưỡng Rank Math 0,5-2,5%. Không đụng title/SEO/category. |
| 2026-10-02 | Toàn bộ Cụm 8 (Compliance / Legal / Risk) — Pillar #237 + 3 bài cluster | **Verify internal link thật, hoàn tất chuỗi Cụm 1/2/3/4/5/6/7**: fetch 4 bài qua WP REST API. Đây là cụm tệ nhất trong cả 8 cụm đã check — pillar #237 không link ra bất kỳ bài nào trong 3 bài cluster của chính nó (chỉ link chéo cụm sang Cụm 4 "AI Voice" và Cụm 7 "Lead Generation"), dù content-plan.md ghi chú "đã link từ #147/Cụm 4/Cụm 7" — ghi chú đó đúng cho chiều NGOÀI link VÀO, nhưng pillar chưa từng tự link RA 3 bài con của nó. Chiều ngược: #492 (ai-decision-making-compliance-real-estate-agents) đã tự link về pillar #237 từ trước; #475 (ai-hallucination-risk-real-estate-listings) và #1260 (seller-impersonation-fraud-prevention-real-estate-agents) hoàn toàn chưa link về pillar. | Thêm link trên 3 bài: (1) Pillar #237 — nối thêm 3 link vào đoạn "Related Reading" có sẵn, trỏ đủ cả 3 bài cluster (ai-hallucination-risk, ai-decision-making-compliance, seller-impersonation-fraud). (2) #475 — thêm 1 câu vào đoạn Related Reading có sẵn, link về pillar #237 (TCPA compliance). (3) #1260 — thêm 1 câu tương tự vào đoạn Related Reading có sẵn, link về pillar #237 (giữ nguyên 2 link chéo cụm cũ tới #223 CRM pipeline và AI chatbot MLS data security). Verify lại cả 4 bài qua REST API — link 2 chiều đầy đủ. | đã sửa xong, verify đủ 3/3 bài sửa (4/4 bài verify) | Cụm nhỏ nhất (chỉ 4 bài) nhưng tỷ lệ thiếu link cao nhất — pillar ban đầu được viết độc lập trước khi 3 bài "Hỗ trợ (News)" ra đời, và không ai quay lại bổ sung link ra. Đây là cụm CUỐI CÙNG trong 8 cụm — **toàn bộ 8/8 cụm nội dung của site giờ đã được verify internal link thật qua REST API**, không còn cụm nào dựa vào nhãn "✓ exist" chưa kiểm chứng của artifact RealSaleX Content Map cũ. |
| 2026-10-02 | Toàn bộ Cụm 5 (Website / Web Design) — Pillar #975 + 5 bài cluster | **Verify internal link thật, tiếp nối Cụm 1/2/3/4/6/7**: fetch 6 bài qua WP REST API. Chiều cluster→pillar hoàn hảo — cả 5 bài cluster (best-real-estate-website-design, web-design-for-real-estate-agents, real-estate-web-design-companies, real-estate-broker-website-design, luxury-real-estate-website-design) đều đã tự link về pillar #975 từ đầu. Chỉ 1 gap: pillar #975 chỉ link ra 1/5 bài cluster (best-real-estate-website-design), thiếu 4 bài còn lại. | Thêm 4 link vào đoạn "Related Reading" có sẵn của pillar #975. Verify lại — pillar giờ link đủ cả 5 bài. | đã sửa xong, verify đủ (1/1 bài sửa, 6/6 bài verify) | Cụm nhỏ nhất và sửa nhanh nhất trong các cụm đã check — chỉ 1 bài cần sửa. Cùng pattern với Cụm 3/4/7: cluster→pillar tốt nhưng pillar quên link ngược ra hết các bài con khi mở rộng cụm. Còn 1 cụm cuối chưa verify: Compliance/Legal/Risk (Cụm 8). |
| 2026-10-02 | Toàn bộ Cụm 7 (Lead Generation / Follow-up Automation) — Pillar #1223 + 8 bài | **Verify internal link thật, tiếp nối Cụm 1/2/3/4/6**: cụm này content-plan.md đánh dấu "✅ HOÀN THÀNH" nhưng chưa từng verify link thật. Fetch 9 bài qua WP REST API. Phát hiện: pillar #1223 thiếu link ra 4/8 bài (3 bài "Hỗ trợ News" #1122/#1272/#1278 + 1 bài "Hỗ trợ" #521) — các bài review/buying-guide/kênh chính thì đã link 2 chiều đầy đủ từ đầu (giống pattern Cụm 4, không phải Cụm 1/2/3). Chiều ngược: #521 (contact form) hoàn toàn không link về pillar, chỉ link 3 trang stub/merged cũ (best-ai-chat-platform-real-estate, best-ai-chatbot-for-real-estate-lead-capture, conversational-chat-real-estate — cả 3 đều verify redirect 301 đúng, chỉ gián tiếp không tối ưu); #1122 (database reactivation) chỉ link chéo cụm qua #223 chứ không link thẳng pillar; #1278 (seller lead prioritization) hoàn toàn không link pillar, chỉ link 2 bài CRM cụm khác. | Thêm link trên 4 bài: (1) Pillar #1223 — thêm đoạn "Related Reading" link cả 4 bài thiếu. (2) #521 — thêm 1 câu link pillar vào đoạn "Related Reading" có sẵn (giữ nguyên 3 link stub cũ, không trong phạm vi sửa lần này). (3) #1122 — thêm 1 câu link pillar vào đoạn "Related Reading" có sẵn. (4) #1278 — thêm 1 câu link pillar vào đoạn "Related Reading" có sẵn. Verify lại toàn bộ 9 bài qua REST API — mọi link 2 chiều đều đủ. | đã sửa xong, verify đủ 4/4 bài sửa (9/9 bài verify) | Cụm "✅ HOÀN THÀNH" trong content-plan.md không đồng nghĩa với "internal link đã đúng" — chỉ có nghĩa nội dung đã viết xong. Bài học lặp lại từ các cụm trước: luôn verify link thật bằng REST API, không tin trạng thái "hoàn thành"/"published" một mình. Còn 2 cụm chưa verify: Website Design (Cụm 5), Compliance/Legal/Risk (Cụm 8). |
| 2026-10-02 | Toàn bộ Cụm 3 (Website Builder / IDX) — 2 hub (#546, #610) + 10 bài cluster | **Verify internal link thật, tiếp nối Cụm 1/2/4/6**: fetch 12 bài qua WP REST API (cụm 2 hub: #546 Website Builder pillar chính + #610 IDX sub-hub). Chiều cluster→pillar chính RẤT TỐT — cả 11 bài còn lại đều đã tự link về #546 từ trước (khác hẳn các cụm trước). Nhưng phát hiện 2 gap lớn: (1) Pillar chính #546 chỉ link ra 1/10 bài cluster (chỉ best-website-builder-for-realtors), thiếu hẳn 9 bài còn lại kể cả IDX sub-hub #610. (2) #610 (IDX sub-hub, do content-plan.md đánh dấu "✅ HUB 2026-10-01") không hề được 5 bài IDX khác (idx-real-estate-definition-guide, idx-real-estate-websites-examples, idx-mls-real-estate-guide, idx-feed-real-estate-setup, real-estate-agent-websites-with-idx) link tới — toàn bộ 5 bài này chỉ link lên #546 + broker-idx-guide, bỏ qua hẳn sub-hub #610 dù nó mới được dựng làm hub cho riêng mảng IDX. | Thêm link trên 7 bài: (1) #546 — thêm 1 câu dài trong đoạn "Related Reading" có sẵn, link đủ 10 bài cluster (bao gồm cả #610). (2) #610 — thêm vào đoạn "Related Resources" có sẵn, link tới cả 5 bài IDX còn lại. (3) 5 bài IDX (idx-real-estate-definition-guide, idx-real-estate-websites-examples, idx-mls-real-estate-guide, idx-feed-real-estate-setup, real-estate-agent-websites-with-idx) — mỗi bài thêm 1 câu vào đoạn "Related Resources" có sẵn, link về #610. Verify lại toàn bộ 12 bài qua REST API — mọi link 2 chiều đều đủ. | đã sửa xong, verify đủ 7/7 bài sửa (12/12 bài verify) | Đây là cụm đầu tiên có pattern "cluster→pillar tốt nhưng pillar→cluster thiếu" NGƯỢC với Cụm 1 (thiếu cả 2 chiều) — có thể do khi viết từng bài cluster, tác giả nhớ link về pillar, nhưng khi viết pillar ban đầu (trước khi toàn bộ cluster tồn tại) không quay lại bổ sung link ra sau này. Bài học: khi 1 cụm có sub-hub mới dựng (như #610 do content-plan đánh dấu audit 01/10), luôn check xem sub-hub có được các bài cùng mảng con trỏ về chưa — dễ bị bỏ sót vì sub-hub "mới" hơn các bài khác. Còn 3 cụm chưa verify: Website Design (Cụm 5), Lead Generation (Cụm 7), Compliance/Legal/Risk (Cụm 8). |
| 2026-10-02 | Toàn bộ Cụm 4 (AI Voice/Virtual Assistant/Receptionist) — Pillar #147 + 4 bài (3 cluster + #110) | **Verify internal link thật, tiếp nối Cụm 1/2/6**: content-plan.md claim cụm này "Internal link: #147 ↔ 3 cluster (2 chiều, đã verify live)" — khác các cụm trước (ghi "dự kiến"/chưa verify), nên kỳ vọng tốt hơn. Verify thực tế đúng như vậy phần lớn: #1217 (receptionist vs human), #1219 (answering service), #1213 (outbound calling), #110 (virtual assistant) đều đã link về pillar #147 từ trước, và #110 + #1213 đã được pillar link ngược sẵn. Chỉ thiếu 1 chỗ: pillar #147 KHÔNG link tới #1217 và #1219 (2/4 bài cluster). | Thêm 2 câu vào đoạn "Looking for more ways to automate..." cuối bài pillar #147, link tới #1217 (AI receptionist vs human) và #1219 (AI answering service). Verify lại — pillar giờ link đủ cả 4 bài trong cụm. | đã sửa xong, verify đủ | Đây là cụm đầu tiên trong 4 cụm đã check mà claim "đã verify live" hóa ra gần đúng sự thật (chỉ thiếu 2/13 khả năng, so với Cụm 1 gần như toàn bộ sai và Cụm 2 thiếu phần lớn) — có thể vì cụm RealSaleX ưu tiên cao nhất nên được làm kỹ hơn lúc viết. Còn 4 cụm chưa verify: Website Builder/IDX (Cụm 3), Website Design (Cụm 5), Lead Generation (Cụm 7), Compliance/Legal/Risk (Cụm 8). |
| 2026-10-02 | Toàn bộ Cụm 6 (Landing Pages) — Pillar #930 + 5 bài cluster | **Verify internal link thật, tiếp nối Cụm 1 + Cụm 2**: fetch full content 6 bài qua WP REST API + `grep href` cả 2 chiều. Cụm này nhỏ (6 bài) và tình trạng link tốt hơn cả Cụm 2 — hầu hết cluster đã tự link lẫn nhau (#936 ↔ #942 2 chiều có sẵn từ audit cannibalization trước đó). Phát hiện: Pillar #930 mô tả rõ "home valuation landing page" trong nội dung nhưng KHÔNG link tới #936 (chỉ link #948 + #918), và hoàn toàn thiếu link tới #924, #936, #942. Chiều ngược lại: chỉ #948 link về pillar; #918, #924, #936, #942 đều KHÔNG link về pillar #930 dù plan/artifact claim đã có. | Thêm link trên 5 bài: (1) Pillar #930 — link hoá cụm từ "home valuation landing page" đang có sẵn trỏ về #936, thêm "Related Reading" với #924 + #942. (2) #918, #924, #936, #942 — mỗi bài thêm 1 câu/nối vào đoạn liên quan có sẵn trỏ về pillar #930 (3 bài chưa có "Related Reading" nào — tạo mới; #918 đã có sẵn "Related Reading" — nối thêm câu vào, không tạo H2 trùng). Verify lại cả 6 bài qua WP REST API — tất cả đã có link 2 chiều đầy đủ với pillar. | đã sửa xong, verify đủ 6/6 bài | Cụm nhỏ nhất trong 8 cụm (chỉ 6 bài so với 20 của Cụm 1/2) nên sửa nhanh. Còn 5 cụm chưa verify: Website Builder/IDX (Cụm 3), AI Voice (Cụm 4), Website/Web Design (Cụm 5), Lead Generation (Cụm 7, đã "HOÀN THÀNH" theo content-plan.md nhưng chưa verify link thật), Compliance/Legal/Risk (Cụm 8). |
| 2026-10-02 | Toàn bộ Cụm 2 (CRM Software) — 2 pillar (#207, #1232) + 18 bài cluster | **Verify internal link thực tế vs artifact content map, tiếp nối việc đã làm với Cụm 1 hôm trước**: fetch full content 20 bài qua WP REST API + `grep href` cả 2 chiều. Kết quả tốt hơn Cụm 1 nhiều — phần lớn link cluster→pillar đã tồn tại thật (khác với Cụm 1 gần như toàn bộ là "claim nhưng chưa làm"). Phát hiện cụ thể: Pillar chính #207 chỉ thực sự link tới 1/13 cluster claimed (chỉ Pillar nhẹ), thiếu hẳn 13 link ra. Pillar nhẹ #1232 thiếu 3/5 link ra (Rechat MCP #1026, RE/MAX Leo #1171, Lofty MCP #1329). Chiều ngược lại: #214 (AI CRM for RE) thiếu link về Pillar nhẹ; #1026 và #1329 có link nhưng trỏ vào 2 trang stub đã merge (`best-crm-software-real-estate-agents` = #384 cũ, `top-crm-tools-for-real-estate-teams` = #412 cũ) thay vì thẳng pillar đúng (vẫn hoạt động nhờ redirect 301 nhưng không tối ưu, và #1026/#1329 lẽ ra phải trỏ Pillar nhẹ chứ không phải Pillar chính); #1171 (RE/MAX Leo) thiếu hẳn link về Pillar nhẹ; #1184 (eXp Nexus) link qua stub thay vì thẳng Pillar chính; #1323 (ARM Borrower) thiếu hẳn link về Pillar chính (không có link nào, kể cả qua stub). | Thêm/sửa link trên 8 bài: (1) Pillar chính #207 — thêm "Related Reading" với 13 link (best-crm-teams-2026, buying-guide, free-crm, what-is-crm-software, crm-101, crm-marketing x2, crm-pipeline, crm+website-builder, crm+idx, speed-to-lead, exp-nexus, arm-borrower). (2) Pillar nhẹ #1232 — thêm "Related Reading" với 3 link (Rechat, RE/MAX Leo, Lofty MCP). (3) #214 — thêm link Pillar nhẹ vào đoạn "Related guides" có sẵn. (4) #1026 — thêm link Pillar nhẹ + đổi link pillar chính từ stub sang URL thật #207. (5) #1171 — thêm link Pillar nhẹ vào đoạn Related Reading có sẵn. (6) #1184 — đổi link pillar chính từ stub sang URL thật #207. (7) #1323 — thêm cả link Pillar chính #207 (trước đó hoàn toàn không có) vào đoạn Related Reading có sẵn. (8) #1329 — đổi link "crm tools for real estate" từ stub sang URL thật #207 + thêm link Pillar nhẹ. Verify lại từng bài qua WP REST API — tất cả 8/8 đã đúng. | đã sửa xong, verify đủ 8/8 bài | Cụm 2 có internal link tốt hơn hẳn Cụm 1 (phần lớn cluster đã tự link về pillar từ đầu khi viết), chỉ có khoảng 1/3 số bài cần vá. 2 case link-qua-stub (#1026, #1184, #1329) là do bài được viết ở thời điểm #384/#412 còn là pillar riêng, sau khi merge 01/10 link cũ vẫn còn trỏ qua slug đã merge — nên luôn check lại link cũ sau mỗi lần đổi vai trò pillar, không chỉ thêm link mới. 6 cụm còn lại (Landing Pages, AI Voice, Website Design, Website Builder, IDX, Lead Gen) vẫn CHƯA được verify link thật. |
| 2026-10-01 | Toàn bộ Cụm 1 (Chatbot/Conversational AI) — 2 pillar (#1056, #89) + 10 bài cluster | **Verify internal link thực tế trên live site vs artifact content map**: artifact đánh dấu toàn bộ link nội bộ trong Cụm 1 là "✓ exist" (đã verify) nhưng chưa từng check thật — user hỏi ý nghĩa chip màu xanh dương "(dự kiến)" trong artifact rồi yêu cầu verify, chọn phạm vi "Chỉ Cụm 1 trước". Fetch full content qua WP REST API + `grep href` cho cả 2 chiều (pillar→cluster và cluster→pillar): phát hiện Pillar A (#1056) chỉ có 1/9 link dự kiến thực sự tồn tại, Pillar B (#89) có 2/5 (và không link thẳng sang Pillar A), và 10/11 bài cluster KHÔNG link ngược về pillar của mình như artifact claim (chỉ `chatbot-vs-live-agent-real-estate` đúng) — một số bài (#117, #172, #189, #1146) trỏ vào trang stub đã merge (`best-ai-chatbot-for-real-estate-lead-capture`) thay vì thẳng pillar (stub vẫn redirect 301 đúng nên không gãy, nhưng không tối ưu); `ai-chat-vs-sms-real-estate` (#1071) không có internal link nào cả. | Thêm link thiếu trên cả 12 bài: (1) Pillar A — thêm "Related Reading" với 7 link (Pillar B, Chatbot Builders, GoHighLevel vs Dedicated, AI Chat vs SMS, What Is Conv. Chatbot, Chatbot Reads Photos, Mortgage Doc Errors). (2) Pillar B — thêm "Related Reading" với 5 link (Pillar A, Chatbot vs Live Agent, Zendesk Alternative, EU AI Act Disclosure, MLS Data Leak). (3) 7 bài cluster (#117, #123, #138, #1071, #172, #1100, #1114) — thêm 1 câu "Related" link về Pillar A mỗi bài. (4) 3 bài cluster (#189, #1050, #1146) — thêm link về Pillar B vào đoạn "Related Reading/guides" có sẵn. Verify lại từng bài qua WP REST API sau khi update — tất cả 12/12 đã có đủ link. | đã sửa xong, verify đủ 12/12 bài | Phát hiện quan trọng: artifact content map đã "optimistically" đánh dấu link nội bộ là exist mà không verify thật trong các lần cập nhật trước — cần nhớ không tin nhãn "exist" trong artifact cho các cụm còn lại (2-8), phải check lại thật khi tới lượt. 7 cụm còn lại (CRM, Landing Pages, AI Voice, Website Design, Website Builder, IDX, Lead Gen) CHƯA được verify link — việc còn lại theo đúng scope user chọn ("Chỉ Cụm 1 trước"). |
| 2026-10-01 | https://infina.ai/news/best-chatbot-builder-real-estate/ (#117, hub) + https://infina.ai/news/no-code-chatbot-platform-real-estate/ (#1076, merged) + https://infina.ai/news/home-valuation-landing-page/ (#936) + https://infina.ai/news/seller-landing-pages-real-estate/ (#942) | **Audit cặp cuối cùng còn lại trong danh sách "Việc còn lại" (sau 10 cặp chính 01/10)**: 2 cặp nghi trùng nhẹ phát hiện khi map pillar+cluster, impression thấp nên để dành cuối cùng. (A) `best-chatbot-builder-real-estate` (#117, ~0 impr) vs `no-code-chatbot-platform-real-estate` (#1076, 86 impr pos 13.9): MERGE — trùng 4/7 tool (Tidio/ManyChat/Landbot/Intercom) với "best for" tagline gần như y hệt, cùng khung "How to Choose" theo persona, #1076 đã tự link sang #117 gọi là "full guide". (B) `home-valuation-landing-page` (#936, 87 impr pos 5.8, có click) vs `seller-landing-pages-real-estate` (#942, 70 impr pos 11.2): GIỮ NGUYÊN — không phải duplicate, #942 là bài tổng quan 4 loại seller landing page (home valuation/listing consultation/expired listing/market report) đã tự link xuống #936 gọi là "detailed breakdown of this specific type", chỉ thiếu link ngược lại. | Đã sửa: (1) Gộp 3 platform riêng của #1076 (Chatfuel, GoHighLevel, Botsonic) vào #117 — đổi "7 Best" → "10 Best" (cả title lẫn H2), mở rộng "How to Choose" thêm 3 dòng. (2) Thu gọn #1076 thành stub trỏ về #117. (3) Thêm 1 câu link từ #936 sang #942 (trước đó chỉ 1 chiều #942→#936). (4) User set redirect 301 qua Rank Math: #1076 → #117 — verify đúng ngay lần đầu qua `curl -I`, follow redirect ra #117 status 200; verify link mới từ #936 sang #942 đã sống qua `curl`. | đã sửa xong (1 merge + 1 link fix, redirect đã verify) | Cả 4 bài đều impression thấp (0-87, 28 ngày 03/09-01/10/2026) — mức độ ưu tiên thấp nhất, chủ yếu dọn dẹp duplicate content/internal-link hơn là fix ranking gấp. **Đây là 2 cặp cuối cùng trong toàn bộ danh sách cannibalization phát hiện khi map pillar+cluster 01/10/2026 — coi như đã audit xong hết.** |
| 2026-10-01 | https://infina.ai/news/what-is-a-conversational-chatbot-real-estate/ (#172, hub) + https://infina.ai/news/conversational-chat-real-estate/ (#196, merged) + https://infina.ai/news/website-design-for-real-estate-agents/ (#975, Pillar, hub) + https://infina.ai/news/realtor-website-design/ (#987, merged) | **Audit cannibalization #5-8 (batch, ưu tiên thấp — impression gần như 0 trong 28 ngày) từ đợt re-map 86 bài**: audit 4 cặp cùng lúc. (A) `crm-marketing-real-estate` (#263) vs `crm-marketing-software-real-estate-guide` (#450): GIỮ NGUYÊN — differentiation thật (chiến lược/funnel 5 giai đoạn vs định nghĩa category phần mềm), chỉ trùng 2/4 platform, #450 đã tự link sang #263. (B) `what-is-a-conversational-chatbot-real-estate` (#172) vs `conversational-chat-real-estate` (#196): MERGE — trùng gần như hoàn toàn, y hệt 4 tool (Structurely/Ylopo rAIya/Tidio/ManyChat) cùng mô tả, cùng bảng so sánh Traditional vs Conversational. (C) `best-ai-virtual-assistant-real-estate` (#110) vs Pillar `best-ai-voice-assistants-for-real-estate` (#147): GIỮ NGUYÊN — differentiation thật (đa kênh SMS/CRM/scheduling vs riêng voice/phone), chỉ trùng 3/7 tool. (D) `website-design-for-real-estate-agents` (#975, Pillar) vs `realtor-website-design` (#987): MERGE — trùng gần như hoàn toàn, y hệt 3 platform (AgentFire/Real Geeks/Luxury Presence) cùng tagline, #987 đã tự link sang #975 gọi là "full breakdown". | Đã sửa: (1) Thêm đoạn "Seller lead qualification and post-showing follow-up" vào #172 (nội dung duy nhất từ #196), thu gọn #196 thành stub trỏ về #172. (2) Thêm section mới "Common Real Estate Website Design Mistakes" vào #975 (nội dung duy nhất từ #987: stock photo/no neighborhood content/slow speed), thu gọn #987 thành stub trỏ về #975. (3) Thêm 1 câu link từ #263 sang #450 (trước đó chỉ 1 chiều). (4) KHÔNG động vào #110/#147 (AI Virtual vs Voice Assistant) — giữ nguyên. User set 2 redirect 301 qua Rank Math: #196 → #172, #987 → #975 — verify đúng cả 2 ngay lần đầu qua `curl -I`, follow redirect ra đúng hub status 200. | đã sửa xong (2 merge + 1 link fix + 1 giữ nguyên không đổi, 2 redirect thật đã verify) | Cả 4 bài merge/giữ đều impression rất thấp hoặc không hiện trong GSC 28 ngày (03/09-01/10/2026) — mức độ ưu tiên thấp nhất trong danh sách audit, chủ yếu dọn dẹp duplicate content để tránh rủi ro dài hạn hơn là fix ranking gấp |
| 2026-10-01 | https://infina.ai/news/best-crm-for-real-estate/ (#207, HUB MỚI) + https://infina.ai/news/best-crm-software-real-estate-agents/ (#384, Pillar cũ, merged) + https://infina.ai/news/top-crm-tools-for-real-estate-teams/ (#412, merged) | **Audit cannibalization #4 (ưu tiên GSC impressions) — cụm CRM 5 bài, lớn nhất từ trước đến giờ** từ đợt re-map 86 bài. 5 bài roundup "best/top CRM" cùng pool platform cốt lõi (Follow Up Boss/Lofty/Wise Agent/LionDesk/kvCORE): #384 Pillar chính thức (31 impr, pos 15.5, 5 platform), #207 (148 impr, pos 9.9, 8 platform — giàu nhất), #412 (81 impr, pos 7.1, y hệt 5 platform của #384, "best for X" gần như sao chép), #419 teams (20 impr, pos 5.0 — rank tốt nhất nhóm, niche "teams" thật), #444 buying guide (27 impr, pos 10.6, BOF quy trình đánh giá 14 ngày — funnel khác thật). Kết luận: #384+#207+#412 là duplicate thật (3-way), #419+#444 là differentiation thật (giữ nguyên, giống case Landing Pages). Phát hiện thêm: nội dung #384 tự link sang #207 gọi là "the full pillar overview" — mâu thuẫn vai trò. Verify internal link sitewide: #207 có 15 inbound link từ các bài CRM cluster khác (best-free-crm, what-is-crm-software, crm-marketing, crm-pipeline-management, real-estate-crm-with-idx, v.v. + chính #384 cũng tự link); #384 chỉ có 2 inbound (từ cinc-crm-review-real-estate + ai-intent-layer-for-real-estate-crm, cả 2 thuộc cụm RealSaleX P3). User ban đầu duyệt giữ #384 làm hub theo đề xuất gốc, nhưng sau khi thấy dữ liệu internal-link, user chọn đổi: **#207 làm HUB mới thay vì #384** (dù #384 là Pillar chính thức theo content-plan.md) — vì #207 đã có sẵn link equity + rank tốt hơn + nội dung giàu hơn, tránh phải sửa 15 bài khác. | Đã sửa: (1) Gộp vào #207: mục "None of These Ship a True Intent Layer" từ #384 (bridge sang RealSaleX P3 ai-intent-layer-for-real-estate-crm) + mục "Integrations That Matter" từ #412. (2) Thu gọn #384 và #412 thành stub "This guide has moved" trỏ về #207. (3) Sửa 2 link nội bộ (cinc-crm-review-real-estate ID1234, ai-intent-layer-for-real-estate-crm ID1232) đang trỏ sang #384 (sắp bị stub) → đổi sang #207. (4) User set 2 redirect 301 qua Rank Math: #384 → #207, #412 → #207 — verify đúng cả 2 ngay lần đầu qua `curl -I`, follow redirect ra #207 status 200. (5) Update content-plan.md: đổi vai trò "Pillar chính thức Nhánh 3 RealSaleX" từ #384 sang #207 ở cả Phần 1 (RealSaleX) và Phần 2 (Cụm 2 CRM). KHÔNG động vào #419 (teams) và #444 (buying guide) — giữ nguyên, differentiation thật. | đã sửa xong (content merge + 2 redirect thật, đã verify, đổi hub theo dữ liệu internal-link thay vì theo thiết kế pillar ban đầu) | #384: 31 impr pos 15.5; #207: 148 impr pos 9.9; #412: 81 impr pos 7.1 (28 ngày 03/09-01/10/2026) — cần check lại sau 3-4 tuần (lâu hơn bình thường vì đây là thay đổi cấu trúc + đổi vai trò pillar, cần thời gian Google re-crawl và gộp tín hiệu từ 2 trang) xem #207 có lên hạng cho cụm "best crm software"/"crm tools for real estate teams" không, và #384/#412 có rớt khỏi index không |
| 2026-10-01 | https://infina.ai/news/real-estate-landing-page-guide/ (#930, Pillar) + https://infina.ai/news/high-converting-real-estate-landing-pages/ (#948, cluster) | **Audit cannibalization #3 (ưu tiên GSC impressions) từ đợt re-map 86 bài**: KHÁC 2 case trước — không phải duplicate content, mà đúng cấu trúc pillar→cluster hợp lệ (Pillar #930 = overview rộng 4 loại landing page + elements cơ bản + platform build; #948 = deep-dive thật về "điều gì làm landing page convert cao" với 7 section chi tiết: message match, single CTA, form length theo traffic temperature, social proof, mobile/speed, A/B test). Vấn đề thật: Pillar có 1 H2 tên trùng chính xác intent của #948 ("What Separates High-Converting Real Estate Landing Pages") nhưng chỉ viết tóm tắt ~150 từ rồi dừng, KHÔNG link sang #948 đầy đủ hơn — khiến Google thấy 2 trang cùng claim trả lời 1 câu hỏi, 1 trang nông (Pillar, pos 19.4) 1 trang sâu (cluster #948, pos 6.1, đã có click). #948 cũng chưa link ngược về Pillar. User duyệt: không merge, chỉ sửa internal link. | Đã sửa: (1) Rút gọn H2 "What Separates High-Converting..." trong #930 còn 1 đoạn ngắn + link rõ ràng sang #948 (bỏ đoạn ví dụ trùng lặp). (2) Thêm 1 đoạn mới ngay đầu #948 link ngược về #930 cho ai mới bắt đầu build landing page từ số 0. (3) Verify cả 2 link sống 2 chiều qua curl. KHÔNG đổi title/slug/SEO của cả 2 bài, không redirect (cả 2 tiếp tục sống riêng, mỗi bài giữ nguyên vai trò pillar/cluster). | đã sửa xong (internal-link fix, đã verify, không phải merge) | #930: 164 impr pos 19.4, 0 click; #948: 100 impr pos 6.1, 1 click (28 ngày 03/09-01/10/2026) — cần check lại sau 3-4 tuần xem #930 có hết cannibalize với #948 cho cụm "high-converting" không (position nên cải thiện vì rõ passing authority 1 chiều thay vì tự cạnh tranh) |
| 2026-10-01 | https://infina.ai/news/real-estate-website-builder/ (#546/id546, hub) + https://infina.ai/news/best-real-estate-website-builder/ (#553/id553, merged) | **Audit cannibalization #2 (ưu tiên GSC impressions) từ đợt re-map 86 bài**: 5/6 platform trong #553 (Real Geeks/AgentFire/Sierra Interactive/kvCORE/Placester) trùng y hệt 5/6 platform trong Pillar #546 — cùng "Best for" tagline, cùng giá, cùng kết luận. Khung "4 điều tách biệt best platform" của #553 trùng với "What to Look For" của Pillar. "How to Choose by tier" của #553 gần như sao chép logic Pillar. #553 gần như không đóng góp nội dung mới — khác case IDX trước (nơi bài yếu có hẳn 1 platform riêng). Điểm duy nhất đáng giữ: #553 rank pos 3.4 cho "is agentfire a good fit for real estate teams or just solo agents?" (21 impr) — Pillar chưa trả lời câu này. Verify: #546 đang tự link sang #553 trong "Related Reading" (cannibalization nội bộ), không có bài nào khác trên site link tới #553. User duyệt merge #553 vào #546 (Pillar đã rank tốt hơn, pos 8.8 vs 9.7). | Đã sửa: (1) Thêm 1 FAQ mới vào #546 "Is AgentFire a good fit for real estate teams, or just solo agents?" để giữ tín hiệu rank tốt của #553 cho câu hỏi đó. (2) Sửa đoạn "Related Reading" của #546, gỡ link tự trỏ sang #553 (giữ lại link best-website-builder-for-realtors). (3) Thu gọn #553 thành stub "This guide has moved" trỏ thẳng về #546. (4) User set redirect 301 qua Rank Math: #553 → #546, verify đúng ngay lần đầu (rút kinh nghiệm từ lỗi dán nhầm text mũi tên ở case IDX trước) — `curl -I` trả `HTTP/2 301` location sạch, follow redirect ra #546 status 200. | đã sửa xong (content merge + 301 redirect thật, đã verify) | #546: 240 impr pos 8.8; #553: 79 impr pos 9.7 (28 ngày 03/09-01/10/2026) — cần check lại sau 3-4 tuần xem #546 có lên hạng cho cụm query "agentfire teams/solo" không, và #553 có rớt khỏi index (dấu hiệu Google theo redirect) không |
| 2026-10-01 | https://infina.ai/news/idx-website-for-realtors/ (#48/id610, hub) + https://infina.ai/news/best-idx-website-for-realtors/ (#54/id649, merged) | **Audit cannibalization #1 (ưu tiên theo GSC impressions) từ đợt re-map 86 bài evergreen pillar+cluster**: 2 bài gần như trùng lặp nội dung hoàn toàn chứ không chỉ overlap chủ đề — cùng target "best idx website for realtors", cùng review 3 platform giống hệt nhau (Real Geeks/AgentFire/Showcase IDX) với mô tả gần như y hệt câu chữ, cùng khung phân tích (mobile speed/lead capture/NAR compliance), cùng đoạn Related Resources. Khác biệt duy nhất ở #54: thêm platform Sierra Interactive + mục "How to Evaluate". Cả 2 đều rank rất kém (pos 37.6 và 47.1) dù tổng impression cao (1359/28 ngày) — dấu hiệu Google chia tín hiệu giữa 2 URL cùng intent. Verify không có bài nào khác trên site link tới #54. User duyệt merge #54 vào #48 (giữ #48 vì impr cao hơn 3.75x). | Đã sửa: (1) Thêm vào #48 nội dung duy nhất của #54: đoạn review Sierra Interactive vào mục Top Platforms, cập nhật giá vào Cost Breakdown, thêm H2 mới "How to Evaluate the Best IDX Website for Realtors for Your Market" (trước Related Resources). (2) Thu gọn #54 thành stub "This guide has moved" trỏ thẳng về #48. (3) User set redirect 301 qua Rank Math: #54 → #48 — lần đầu set sai (dán nhầm cả text mũi tên vào field Destination URL khiến location header chứa chuỗi literal " → "), đã phát hiện qua `curl -I` và báo user sửa lại, lần 2 verify đúng: `curl -I` trả `HTTP/2 301` với `location: https://infina.ai/news/idx-website-for-realtors/` sạch, follow redirect (`curl -sL`) ra đúng #48 status 200. | đã sửa xong (content merge + 301 redirect thật, đã verify) | #48: 1078 impr pos 37.6; #54: 281 impr pos 47.1 (28 ngày 03/09-01/10/2026), cả 2 đều 0 click — cần check lại sau 3-4 tuần xem #48 có lên hạng cho cụm "best idx website for realtors" không, và #54 có rớt khỏi index (dấu hiệu Google theo redirect) không |
| 2026-10-01 | https://infina.ai/news/best-chatbot-customer-service-real-estate/ (#89, hub) + https://infina.ai/news/best-ai-chat-platform-real-estate/ (#99, merged) + https://infina.ai/news/best-ai-chatbot-for-real-estate-lead-capture/ (#58, merged) | **Phase 2 cannibalization chatbot cluster** (tiếp Phase 1 cùng ngày). #99 "8 Best AI Chat Platforms" (107 impr, pos8.2): 6/8 tool trùng #89, chỉ Lofty là riêng. #58 "Best AI Chatbot for Real Estate Lead Capture" (289 impr, pos6.9 — đang rank khá tốt nhưng vẫn 8/10 tool trùng #89, chỉ Perspective AI + Conferbot riêng). User duyệt merge cả 2 vào #89 (pillar lớn nhất trong nhóm CS-platform, 494 impr). | Đã sửa: (1) Thêm 3 tool mới vào #89 từ nội dung duy nhất của #99/#58: Lofty (từ #99, anchor #lofty), Perspective AI + Conferbot (từ #58, anchor #perspective-ai/#conferbot) — đổi "12 Best" → "15 Best", thêm 3 dòng bảng so sánh, thêm đoạn vào "How to Choose". (2) Thu gọn #99 và #58 thành stub "This Guide Has Moved" trỏ về #89. (3) Gỡ link "Also read: Best AI Chatbot for Real Estate Lead Capture" cũ trong #89 (trỏ sang #58 sắp bị stub). (4) Tìm thấy 2 bài khác (gohighlevel-chatbot-vs-dedicated #138, chatbot-vs-conversational-ai-real-estate #123) có link "Related guides" trỏ sang #58 — đã sửa cả 2 thành trỏ thẳng về #89 (đổi cả URL và anchor text) để tránh vòng qua trang stub. (5) User cần tự set 2 redirect 301 thủ công qua Rank Math: #99 → #89, #58 → #89. | đã sửa content/stub xong; **redirect 301 cho #99 và #58 CHƯA set (cần user tự làm qua Rank Math)** | #89: 494 impr pos12.7; #99: 107 impr pos8.2; #58: 289 impr pos6.9 (28 ngày 03/09-01/10/2026) — cần check lại sau 3-4 tuần xem #89 có lên hạng cho cụm Lofty/Perspective AI/Conferbot không, và #99/#58 có rớt khỏi index không — NHƯNG chỉ có hiệu lực SAU KHI user set redirect thủ công. Sau Phase 1+2, cụm 16 bài chatbot coi như đã xử lý xong (6 bài gốc → 2 hub, 10 bài khác giữ nguyên/đã resolved) |
| 2026-10-01 | https://infina.ai/news/best-conversational-ai-chatbot-for-real-estate/ (#1056, hub) + https://infina.ai/news/best-ai-conversational-bot-for-real-estate/ (#1069, merged) + https://infina.ai/news/best-conversational-chatbot-for-real-estate/ (#1063, merged) | **Audit cannibalization sitewide (16 bài "chatbot cho real estate")**: soát title + nội dung đầy đủ cả 16 bài. Kết luận: 7 bài hoàn toàn khác biệt (comparison/educational hoặc news/cluster article — gohighlevel-chatbot-vs-dedicated, ai-chat-vs-sms, chatbot-vs-conversational-ai, chatbot-vs-live-agent, ai-chatbot-mortgage-document-errors, ai-disclosure-rules, real-estate-chatbot-that-reads-listing-photos), 2 bài không cần làm gì (best-ai-chatbot-for-real-estate đã tự redirect sang #58 từ trước; best-conversational-ai-chatbot-for-real-estate-in-2026 404 thật, chỉ là dấu vết cũ GSC), 1 bài overlap thấp để lại (no-code-chatbot-platform-real-estate, chỉ 3/7 tool trùng, góc "no-code builder" riêng). Còn lại 6 bài dùng chung 1 pool ~15-18 tool (Structurely/Roof AI/Tidio/Intercom/Ylopo/ManyChat/Drift/ChatBot.com/Crescendo/Real Geeks/Lofty/GoHighLevel...) với tổng 3216 impr/28 ngày: #1056 (2114 impr, pos18.1), #89 (494 impr, pos12.7), #58 (289 impr, pos6.9 — đang rank khá tốt, để dành Phase 2), #1069 (140 impr, pos10.0, 5/7 tool trùng #1056), #99 (107 impr, pos8.2, để dành Phase 2), #1063 (72 impr, pos8.9, 6/7 tool trùng #89 — yếu nhất). User duyệt Phase 1: merge #1069 + #1063 vào #1056 (pillar mạnh nhất, cùng pool tool nhất). Để dành #99 và #58 cho Phase 2 sau khi theo dõi kết quả. | Đã sửa: (1) Thêm 3 tool mới vào #1056 từ nội dung duy nhất của #1069/#1063 mà #1056 chưa có: CINC AI + Follow Up Boss AI (từ #1069, anchor #cinc-ai), BotPenguin (từ #1063, anchor #botpenguin) — đổi "The 8 Best" → "The 11 Best", thêm 3 dòng vào bảng so sánh, thêm 2 gạch đầu dòng vào "How to Choose". KHÔNG đưa ManyChat/Drift/ChatBot.com từ #1063 vào #1056 vì các tool này đã có sẵn ở #89/#58 (tránh tạo cannibalization mới). (2) Thu gọn #1069 và #1063 thành stub (title "This Guide Has Moved", content 2 đoạn trỏ về #1056 kèm anchor tương ứng, #1063 có thêm link phụ sang #89 cho nhánh Intercom/Zendesk/Drift). (3) Verify không còn bài nào khác trên site link tới #1069/#1063. (4) User cần tự vào Rank Math set 2 redirect 301 thủ công: #1069 → #1056, #1063 → #1056 (MCP không có tool redirect tự động). | đã sửa content/stub xong; **redirect 301 cho #1069 và #1063 CHƯA set (cần user tự làm qua Rank Math)**; Phase 2 (#99, #58) chưa làm | #1056: 2114 impr pos18.1; #1069: 140 impr pos10.0; #1063: 72 impr pos8.9 (28 ngày 03/09-01/10/2026) — cần check lại sau 3-4 tuần xem #1056 có lên hạng cho các cụm query CINC/Follow Up Boss/BotPenguin không, và #1069/#1063 có rớt khỏi index (dấu hiệu Google theo redirect) không — NHƯNG chỉ có hiệu lực SAU KHI user set redirect thủ công |
| 2026-10-01 | https://infina.ai/news/best-chatbot-customer-service-real-estate/ (#89) | Striking-distance (pos trung bình 12.7, impr 494, 0 click). Soát 56 query GSC hiện ra riêng, thấy 2 pattern: (1) Cannibalization sitewide — site có 16 bài "chatbot cho real estate" khác nhau (best-conversational-ai-chatbot-for-real-estate, best-ai-conversational-bot-for-real-estate, v.v.), khiến query bare như "real estate chatbot" (impr 18, pos 33.2), "chatbot for realtors" (impr 8, pos 40.5) rank rất xấu — KHÔNG sửa lần này, scope quá lớn, để dành audit/xử lý riêng theo từng cặp giống case #546. (2) Gap content thật cho riêng trang này: cụm query property management/multifamily/leasing/tenant (impr ~25, pos 30-91) — "apartment chatbot software" (impr5, pos50.6), "property management chatbot" (impr5, pos64.2), "multifamily chat bot" (impr2, pos51), "leasing chatbot platforms" (impr3, pos30.3). Check nội dung: 0 lần nhắc multifamily/landlord/apartment/leasing/tenant/rental — bài chỉ review 12 tool customer-service hướng agent/brokerage (Zendesk, Intercom, Freshdesk, Structurely...), hoàn toàn thiếu góc tenant-facing. Verify SERP thật: sub-niche riêng có tên tuổi (EliseAI, Yardi ChatIQ, Respage, Haven, MRI Software). | Đã sửa: (1) Thêm H2 mới "Chatbot Customer Service for Property Management and Multifamily Teams" (sau "How to Choose", trước FAQ) — giải thích 12 tool trên là cho sales-side, nêu tên EliseAI/Yardi ChatIQ/Respage cho property management/multifamily. (2) Thêm entry vào TOC. (3) Thêm 1 câu hỏi FAQ mới "What's the best chatbot for property management or multifamily customer service?". Giữ nguyên title/slug/seo_focus_keyword/seo_description và 12 tool hiện có. Vấn đề cannibalization sitewide (16 bài) CHƯA xử lý, để làm riêng sau. | đã sửa (phần content gap riêng trang); cannibalization sitewide còn pending | pos trung bình 12.7, impr 494 (28 ngày 03/09-01/10/2026), 0 click — cần check lại sau 2-3 tuần xem cụm query property management/multifamily có cải thiện vị trí không |
| 2026-10-01 | https://infina.ai/news/best-crm-for-real-estate/ (#207) | Striking-distance (pos trung bình 9.9, impr 148, click 2, CTR 1.35% so benchmark ~3% cho pos 8-10). Soát 21 query GSC hiện ra riêng (tổng impr ~46/148, phần còn lại bị GSC ẩn): đa số query liên quan AI đã rank tốt (pos 1-10), trừ 1 query lệch hẳn: "best real estate crm with ai" — impr 8, pos 29.5. Verify SERP thật cho query này: top kết quả liên tục nhắc Lofty là pick #1 cho "AI CRM". Phát hiện gốc rễ: bài đang review đúng sản phẩm đó dưới brand name cũ "Chime" (link chime.me) — nhưng Chime đã rebrand thành Lofty từ 2023, và chime.me hiện redirect thẳng sang lofty.com (verify qua curl -L). Bài chưa nhắc AI assistant/AI content generator/AI IDX recommendation của Lofty, cũng chưa có câu nào chứa cụm "best real estate CRM with AI". | Đã sửa: (1) Đổi H3 mục #5 "Chime — Best CRM for Real Estate Lead Generation + Nurture" → "Lofty (formerly Chime) — Best CRM for Real Estate with AI Built In", viết lại đoạn nhấn AI sales assistant/AI content generator/AI IDX recommendations, có câu chứa cụm "best real estate CRM with AI", đổi link chime.me → lofty.com. (2) Đổi dòng "Best for" mục #5 thêm "most AI-native CRM". (3) Đổi dòng bảng so sánh "Chime" → "Lofty (formerly Chime)", cột AI Follow-Up ✓✓ → ✓✓✓. (4) Đổi 1 câu ở đoạn "How to Choose" từ "kvCORE and Chime" → "kvCORE and Lofty" + thêm câu Lofty mạnh nhất cho brokerage ưu tiên AI. Giữ nguyên title/slug/seo_focus_keyword/seo_description và 7 CRM còn lại. | đã sửa | pos trung bình 9.9, impr 148 (28 ngày 03/09-01/10/2026), click 2, CTR 1.35% so benchmark ~3% — cần check lại sau 2-3 tuần (~giữa đến cuối tháng 10/2026) xem query "best real estate crm with ai" có cải thiện vị trí không |
| 2026-10-01 | https://infina.ai/news/real-estate-broker-website-design/ (#1005) | Striking-distance (pos trung bình ở vùng 8-20, cần optimize). Soát query GSC riêng cho trang: query chính dạng ngắn "broker web design" (biến thể rút gọn của "broker website design") xuất hiện với impression đáng kể nhưng KHÔNG tồn tại ở dạng ngắn/trần (bare) này trong nội dung bài — bài chỉ luôn viết đầy đủ "real estate broker website design" (bôi đậm, lặp lại nhiều lần) chứ chưa bao giờ viết tắt thành "broker website design" hay "broker web design" đứng riêng. Đây là gap phrasing giống pattern đã gặp ở #1056 (thiếu biến thể ngắn của keyword chính). | Đã sửa: (1) Thêm câu "Broker website design, often shortened to just broker web design, has to work for three different audiences at once instead of one." vào ngay sau câu mở đầu của đoạn đầu tiên (H2 đầu bài) — phủ cả 2 cách viết tắt "broker website design" và "broker web design" ở dạng bare, không đổi phần còn lại của đoạn hay các đoạn khác. (2) seo_description đổi từ "Real estate broker website design is different from agent websites. Here's what brokerage sites need to do - and the design decisions that support recruiting, retention, and brand." thành "Real estate broker website design (broker web design) differs from agent sites. See what brokerage websites must do - and the design choices that drive recruiting, retention, and brand." — chèn thêm "(broker web design)" ngay sau keyword chính. Giữ nguyên title/H1/slug/seo_focus_keyword/toàn bộ nội dung còn lại. | đã sửa | Striking-distance, pos trung bình vùng 8-20 — cần check lại sau 2-3 tuần (~giữa đến cuối tháng 10/2026) xem query "broker web design"/"broker website design" dạng ngắn có cải thiện vị trí không |
| 2026-10-01 | https://infina.ai/news/real-estate-website-builder/ (#546) + https://infina.ai/news/real-estate-website-builder-with-idx/ (#637) | Striking-distance ban đầu: #546 pos gộp 8.8, impr 240, CTR 0.42% so benchmark 3.0%. Soát 34 query GSC riêng cho #546: top query thật ("best real estate website builders with idx" 15 impr, "best real estate idx website builders" 10 impr) đều ở pos 20-23, KHÔNG gần top 10 như số gộp gợi ý. Nguyên nhân: cannibalization thật (không chỉ title) giữa 3 bài trên site — #546 (2567 từ, pillar), #553 best-real-estate-website-builder (1354 từ), #637 real-estate-website-builder-with-idx (677 từ, yếu nhất) — cả 3 đều review ĐÚNG 5 platform (Real Geeks, AgentFire, Sierra Interactive, kvCORE, Placester/4-5 tuỳ bài) với ĐÚNG cùng kết luận "best for X persona" (chỉ viết lại câu chữ, không khác nội dung thật). Verify: không có trang nào khác trên site link tới #637 ngoài chính #546 (1 link duy nhất trong Related Reading). User chọn hướng gộp #637 vào #546. | Đã sửa: (1) Thêm H2 mới "All-in-One Builder vs. a General Website Plus a Separate IDX Widget" vào #546 (giữa section #vs-custom và #cost) — nội dung duy nhất lấy từ #637 mà #546 CHƯA có (rủi ro Zapier/stitching 2 vendor, lợi thế hỗ trợ 1 đầu mối, checklist verify MLS board + mobile trước khi đăng ký), thêm entry vào TOC. (2) Xoá link tới #637 khỏi Related Reading của #546 (chỉ còn link #553 + best-website-builder-for-realtors). (3) Thu gọn #637 thành stub (title đổi "This Guide Has Moved", content chỉ còn 2 đoạn trỏ thẳng về #546 kèm anchor #idx-considerations + #comparison, seo_title/seo_description cũng đổi theo). (4) WP MCP không có tool xoá post/set redirect, nhưng Rank Math (plugin SEO site đang dùng) có sẵn field "Redirect" ngay trong meta box Advanced của từng post — user tự vào edit #637, bật toggle Redirect, chọn 301 Permanent Move, Destination URL = `https://infina.ai/news/real-estate-website-builder/`, save. Đã verify qua `curl -I`: `/real-estate-website-builder-with-idx/` trả đúng HTTP 301 → `/real-estate-website-builder/`. | đã sửa xong (content merge + 301 redirect thật, đã verify) | #546: pos gộp 8.8, impr 240 (28 ngày 03/09-01/10/2026), CTR 0.42% so benchmark 3.0%. #637: không nằm trong top candidate striking-distance riêng (impr thấp hơn), nhưng góp phần cannibalization. Check lại sau 3-4 tuần (lâu hơn bình thường vì đây là thay đổi cấu trúc, cần thời gian Google re-crawl và gộp tín hiệu) xem #546 có lên hạng cho cụm "website builder with idx" không, và #637 có rớt hẳn khỏi index (dấu hiệu Google đã theo redirect) không |
| 2026-10-01 | https://infina.ai/news/best-conversational-ai-chatbot-for-real-estate/ (#1056) | Striking-distance (pos trung bình 18.1, impr 2114 toàn trang, CTR ~0% so benchmark 1.5%). Soát toàn bộ 87 query GSC riêng cho trang: Gap #1 (lớn nhất, 316 impr, pos 23-29) — cụm `conversational ai for/in real estate` KHÔNG có chữ "chatbot", nội dung bài luôn ghép cứng "conversational AI chatbot", không có câu trả lời trực tiếp định nghĩa "conversational AI for real estate" đứng riêng. Gap #2 (~250-300 impr gộp, pos 26-45) — cụm generic `ai chatbot for real estate` / `real estate ai chatbot` (không "conversational", không "best"), bài ít nhấn cụm ngắn này. Đã check cannibalization với #58 (best-ai-chatbot-for-real-estate-lead-capture) và #147 (best-ai-voice-assistants-for-real-estate) — overlap không đáng kể (volume phía kia quá nhỏ, 1-2 impr), không phải nguyên nhân chính. SERP thật cho "best conversational ai for real estate": bài mình có mặt top kết quả, đối thủ futurocorp.com title gần giống nhưng bỏ chữ "Chatbot". SERP cho "conversational ai in real estate": top 9 toàn bài overview/định nghĩa, không có listicle nào — lệch intent với bài mình (dạng listicle). Nhiều query dạng câu hỏi dài (AI Overview/answer-engine style) đứng pos 1-11 nhưng 0 click — không phải gap content, bỏ qua. | User duyệt 2026-10-01. Đã sửa: (1) Viết lại đoạn mở đầu H2 "What Is a Conversational AI Chatbot for Real Estate?" — câu đầu giờ bắt đầu bằng "Conversational AI for real estate is software that..." và thêm câu "it becomes an AI chatbot for real estate: a conversational AI chatbot for real estate that..." để phủ cả 3 cách diễn đạt (conversational AI for real estate / AI chatbot for real estate / conversational AI chatbot for real estate gốc), không đổi phần còn lại của đoạn. (2) seo_description đổi từ "Discover the best conversational AI chatbots for real estate agents in 2026. Compare top tools..." thành "Discover the best conversational AI for real estate agents in 2026. Compare top AI chatbot tools...". (3) Giữ nguyên title/H1/slug/seo_focus_keyword như đã chốt. | đã sửa | pos trung bình 18.1, impr 2114 (toàn trang, 28 ngày 03/09-01/10/2026), 7 click (ẩn trong query bị GSC anonymize), CTR ~0% so benchmark 1.5% (pos 11-20) — cần check lại sau 2-3 tuần (~giữa đến cuối tháng 10/2026) xem vị trí 2 cụm gap có cải thiện không |
| 2026-09-15 | https://infina.ai/news/best-ai-voice-assistants-for-real-estate/ (#147) | Không có GSC/GA4 (thiếu credentials) nên không chẩn đoán được theo số liệu thật. Refresh chủ động theo content-plan.md Nhánh 1 RealSaleX: đóng vai pillar cho cụm AI Answering/Call Center, mở rộng keyword coverage sang `ai receptionist for real estate` (niche, verify qua live-SERP), thêm góc compliance đối thủ chưa cover. | Thêm đoạn nêu số liệu AI ISA (link #390), đổi H2 "What Do AI Voice Assistants..." thêm "(AI Receptionists)", thêm H2 mới "Compliance Real Estate Teams Can't Skip: Fair Housing and TCPA" (link nội bộ tới #237), đổi seo_description. KHÔNG đổi title/slug/seo_focus_keyword (giữ nguyên vì chưa có dữ liệu ranking thật để biện minh đổi keyword chính). | đã sửa | Không có (thiếu GSC) — cần check lại traffic/ranking sau khi có credentials |

### 2026-10-07 18:15: khép link ngược cho #1487 sau khi bài live

Trigger hẹn giờ `trig_01QKUirTwx6aQz1EHkdxbc9o` chạy sau khi #1487
(`customer-engagement-platform-vs-crm`) publish lúc 07/10 10:00 UTC. Đây là Bước 6.5 của skill
`news-to-cluster-article`: chiều pillar trỏ xuống cluster không tự xảy ra.

| Bài sửa | Thêm gì | Đặt ở đâu |
|---|---|---|
| **#207** `best-crm-for-real-estate` | 1 đoạn link xuống #1487 | Cuối section "None of These Ship a True Intent Layer", nối tiếp lập luận CRM vs lớp bổ sung |
| **#1232** `ai-intent-layer-for-real-estate-crm` | 1 đoạn link xuống #1487 | Section "This Does Not Replace Your CRM", đúng chỗ bàn ranh giới thay thế hay bổ sung |

Verify 2 chiều qua REST: #207 → #1487 ✅, #1232 → #1487 ✅, #1487 → cả hai ✅.

Sau sửa: #207 4.321 chữ / 22 link (5,1/1.000). #1232 754 chữ / 8 link (10,6/1.000).

Làm thêm trong lúc sửa #1232 vì đang ghi đè full content: gỡ 9 dash, và nâng density FOCUS_KW
`ai intent layer for real estate crm` từ **0,28% lên 0,53%** (đang dưới sàn Rank Math 0,5% từ trước,
không phải do lần sửa này gây ra).

⚠️ Hai việc ghi nhận, chưa xử lý:
- **#1487 đang có 1 link nội bộ trỏ tới URL 404**: nó link sang `real-estate-customer-engagement-strategies`
  (#1488), bài này tới 08/10 10:00 mới live. Link tự lành sau đó. Để nguyên thay vì sửa rồi khôi phục,
  vì sẽ tốn 2 lần ghi đè full content trên bài 1.345 chữ. Check-in 08/10 sẽ verify lại.
- Phần "generate 3 ảnh" trong nội dung trigger đã lạc hậu: #1487 có sẵn featured image (media 1493,
  alt chứa FOCUS_KW) cộng 2 ảnh trong bài. Không chạy lại Gemini.

---

## 2026-10-08 — Dọn anchor text trùng trỏ về #207 (29 bài)

**Nguyên nhân gốc, không phải lỗi người viết.** SKILL.md bắt buộc anchor trỏ pillar phải chứa
`PILLAR_KW` nguyên văn, lặp ở 4 chỗ (dòng 421, 448, 452, 513). `PILLAR_KW` cố định cho mỗi pillar
nên làm đúng skill là tạo ra anchor trùng. Ràng buộc đó đã gỡ ở commit `7b01bcf`.

**Hiện trạng trước khi sửa:** 53 link trỏ về `best-crm-for-real-estate`, chỉ 12 anchor khác nhau
(23%), trong đó **35 link dùng y hệt** `best crm for real estate agents`.

**Đã sửa 29 bài**, đổi 30 anchor (bài #918 có 2 occurrence):

| Nhóm | Bài |
|---|---|
| IDX | 655, 643, 631, 622, 616, 610, 604, 598 |
| Website / web design | 1011, 1005, 999, 993, 981, 975 |
| Website builder | 561, 567, 573, 579, 585, 546 |
| Landing page | 948, 942, 936, 930, 924, 918 |
| CRM / tin tức | 1462, 1458, 1243 |

**Giữ nguyên 5 anchor exact-match** ở #405, #419, #438, #444, #450. Lý do: nghiên cứu Zyppy
(23 triệu internal link) cho thấy trang có **ít nhất 1** exact-match anchor có traffic cao hơn hẳn.
Vấn đề là 35 cái giống nhau, không phải bản thân exact match. Năm bài giữ lại đều là thành viên cụm
CRM, nơi anchor exact match là tự nhiên nhất.

**Kết quả: 23% → 79% anchor khác nhau**, vượt mốc 70% trong SKILL.md.

**Cách làm, để lần sau lặp lại được:** sinh toàn bộ nội dung mới ở local, assert mỗi chuỗi tìm kiếm
xuất hiện đúng 1 lần, rồi mới gọi `update_post`. Sau đó fetch lại cả 29 bài và diff từng dòng với
bản local: **28/29 khớp tuyệt đối**, bài còn lại (#598) chỉ khác do WordPress tự chuẩn hoá thuộc
tính `style` (bỏ space sau dấu `;`). Không có lỗi truyền nội dung nào.

⚠️ **Đã kiểm tra trước khi ghi đè:** các bài này dùng HTML thuần với class kiểu block
(`<figure class="wp-block-image">`), do chính skill viết ra, **không phải block Gutenberg thật**,
nên ghi `content.rendered` ngược lại không làm mất cấu trúc gì.

⚠️ **Còn lại, chưa làm:** 6 pillar khác vẫn dưới mốc 70%, nặng nhất là
`tcpa-compliance-for-real-estate-agents` (14 link / 2 anchor, 14%) và
`real-estate-website-builder` (28 link / 6 anchor, 21%).

⚠️ **Hai lỗi có sẵn, phát hiện trong lúc sửa, không thuộc phạm vi lần này:**
- #948 có `<figure class="wp-block-image aligncenter"></figure>` rỗng, thiếu hẳn thẻ `<img>`.
- #1462 có `<table>` không bọc `<div style="overflow-x:auto;">`, sẽ vỡ layout mobile ở 4 cột.

---

## 2026-10-08 — Bọc overflow cho 20 bảng trong 16 bài, và sửa lỗi gốc trong SKILL.md

**Lỗi gốc không nằm ở nội dung mà ở chính skill.** Skill kê `<div style="overflow-x:auto;">`, nhưng
WordPress lọc `style` qua `safecss_filter_attr()` và **`overflow-x` không nằm trong danh sách property
được phép**, nên thuộc tính bị xoá sạch mỗi lần ghi. Cách sửa đó **chưa bao giờ chạy**: đo 08/10 thấy
16 bài có `<table>` và 0 bài nào có wrapper còn hiệu lực.

Kiểm chứng bằng cách ghi cả hai biến thể lên `#1415` rồi đọc lại qua REST:

| Thuộc tính | Sau khi WordPress lọc |
|---|---|
| `overflow-x:auto` | **bị xoá** |
| `overflow:auto` | sống |
| `display:block`, `max-width:100%` | sống |

**Mức độ tràn, đo bằng Chromium ở viewport 375px** (không suy từ CSS):

| Bài | Cột | Trước | Sau |
|---|---|---|---|
| #546 | 6 | 565px (**+190px**) | 375px |
| #89 | 4 | 468px | 375px |
| #1462 | 4 | 438px | 375px |
| #207 | 5 | 424px | 375px |

**Đã sửa 16 bài, 20 bảng** (89, 123, 138, 172, 189, 207, 438, 546, 1056, 1071, 1078, 1415, 1449,
1462, 1487, 1501). 16 bảng bọc mới, 4 bảng chỉ vá `style` vào `<div>` đã có sẵn. Verify: fetch lại
cả 16, **16/16 giống hệt bản dự định** sau khi bỏ khác biệt khoảng trắng, mọi bài đều đạt
`số wrapper == số bảng`, không còn `overflow-x`, độ sâu `<figure>` ≤ 1.

⚠️ **Đính chính, viết lại 08/10 sau khi phát hiện phép đo của chính tôi sai.** Ba khẳng định ở bản ghi
đầu tiên của mục này đều sai: "theme không có rule nào cho table", "chỉ cần bọc div", và "đã sửa `th` sang
`color:#ffffff`, lên 14,06:1". Nguyên nhân ở cuối mục. Phần `overflow-x` bị `safecss_filter_attr()`
lọc (bảng ở trên) là đúng và vẫn giữ nguyên.

### Đính chính 1: theme CÓ style table, và tự lo cuộn ngang

Theme đang chạy `infina-ai-news` **v1.0.9** có đủ rule cho bảng, đọc thẳng từ
`https://infina.ai/news/wp-content/themes/infina-ai-news/style.css?ver=1.0.9`:

```css
.post-content .wp-block-table { margin: 1.8em 0; overflow-x: auto }
.post-content table           { width: 100%; border-collapse: collapse; font-size: 15px }
.post-content th,
.post-content td              { border: 1px solid var(--border); padding: 12px 16px }
.post-content thead th        { background: var(--blue-soft) /* #EEF3FF */;
                                color: var(--navy) /* #001F5C */; font-weight: 700 }
.post-content tbody tr:nth-child(even) { background: #fafbfc }
```

Nên thứ duy nhất cần làm là **bọc `<table>` trong `<figure class="wp-block-table">`**: chính class đó
kích hoạt `overflow-x: auto` của theme, không cần style nội tuyến nào. 16 bài đã sửa hiện mang cả
`<figure class="wp-block-table">` lẫn `<div style="overflow:auto">` bên trong; cái div là thừa chứ
không hại nên để nguyên, nhưng bài mới chỉ cần figure.

Theme trong repo (`wordpress-theme/infina-ai-news/style.css`) là **v1.0.5**, lệch 64 dòng so với bản
live, và toàn bộ rule table ở trên **chỉ có ở bản live**. Muốn biết theme style gì thì tải thẳng file
CSS từ site, đừng đọc file trong repo.

### Đính chính 2: tiêu đề bảng #438, tôi sửa thành tệ hơn trước khi sửa đúng

| Lần | `tr` | `th` | Nền thật sự thấy | Tương phản |
|---|---|---|---|---|
| Ban đầu | `background:#1a2b4c` | `color:#001F5C` | `#EEF3FF` (theme đặt trên `th`) | **1,11:1** |
| Tôi "sửa" 08/10 | `background:#1a2b4c` | `color:#ffffff` | `#EEF3FF` | **1,10:1**, tệ hơn |
| Đúng | xoá hết `style` | xoá hết `style` | `#EEF3FF` | **13,99:1** |

Nền `#1a2b4c` đặt trên `tr` không bao giờ hiện ra vì theme set nền thẳng trên `th`; còn `color` đặt
nội tuyến thì thắng theme. Cách sửa đúng là **xoá sạch `style` trên `tr`/`th`/`td`**, để theme lo.
Đã xoá 57 thuộc tính `style` ở `#438`. Verify lại 4 bài đại diện (#546 6 cột, #89 4 cột, #207 5 cột,
#438 5 cột): cả 4 đều nằm trong `figure.wp-block-table` với `overflow-x: auto`, tương phản header
**13,99:1**, không tràn ở viewport 375px.

### Nguyên nhân gốc: một regex thiếu nháy đơn

```python
re.findall(r'<link[^>]+href="([^"]+\.css[^"]*)"', html)           # SAI, chỉ bắt nháy kép
re.findall(r"""<link[^>]+href=["']([^"']+\.css[^"']*)["']""", h)  # ĐÚNG, bắt cả nháy đơn
```

WordPress xuất `<link rel='stylesheet' href='...'>` bằng **nháy đơn**. Regex cũ trả về 0 stylesheet,
từ đó tôi tưởng site chỉ có CSS inline, render local thiếu hẳn CSS của theme, đo ra những con số
không có thật, rồi "sửa" `#438` thành chữ trắng trên nền sáng. Người dùng bắt được bằng ảnh chụp
màn hình.

Quy tắc rút ra: khi render local để đo, **phải nạp cả stylesheet ngoài vào snapshot**, và kiểm tra số
stylesheet nạp được có khác 0 không trước khi tin bất cứ phép đo nào. Script
`wordpress-mcp/skills/post-refresh/scripts/render_snapshot.py` làm đúng việc đó.

### Ba chỗ đã sửa trong SKILL.md

1. `overflow-x:auto` → `overflow:auto`, kèm giải thích WordPress lọc gì.
2. Ghi đúng rule table thật của theme v1.0.9, và markup chuẩn chỉ cần `<figure class="wp-block-table">`.
   Kèm cảnh báo theme trong repo là bản cũ, không dùng làm nguồn tra cứu.
3. Cấm set `style` màu trên `tr`/`th`/`td`, kèm bảng 3 dòng lịch sử `#438` và cách đo cho đúng.

### Đã khôi phục ảnh thiếu ở #948

Lúc đầu tôi báo "cần Gemini key, hiện không có trong env" rồi dừng. Sai quy trình: key **nằm trong
Google Drive** (`Gemini Key Realstake.txt`), đã có cách lấy từ trước, chỉ là tôi quên bước đó.

Quy trình đúng, lặp lại được:
1. `search_files` trong Drive tìm `Gemini Key Realstake.txt`, lấy nội dung bằng `download_file_content`
   (trả về base64).
2. Giải mã và ghi thẳng ra `gkey` trong scratchpad bằng `python3 -I -c '...'`, mở file với
   `os.open(..., 0o600)`. **Không bao giờ ghi vào repo.**
3. `cd` sang scratchpad rồi gọi `gen_article_images.py` bằng đường dẫn tuyệt đối, vì script đọc
   `gkey` từ thư mục đang chạy.

Ảnh sinh ra là infographic so sánh độ dài form (5 ô so với 2 ô, kèm cột chiều cao khác nhau), đặt
đúng sau đoạn nói form 2 bước chuyển đổi tốt hơn 20-30%. Không chữ, đúng quy tắc infographic
text-free. Alt chứa FOCUS_KW.

Verify: `#948` giờ có 3 figure, **0 figure rỗng**, **3/3 alt chứa FOCUS_KW**, ảnh mới trả HTTP 200
(`image/jpeg`, 69.102 byte). Đã xác nhận key không lọt vào repo (`grep -rl "AIzaSy"` trong repo trả
về rỗng).

---

## 2026-10-08 — Batch A: gỡ 26 link trỏ vào stub 301, 20 bài

Mọi link nội bộ giờ trỏ thẳng tới URL trả 200. Trước đó có **26 link đi qua redirect 301**,
trong đó 1 link đi qua **2 hầu** (`top-crm-tools-real-estate-teams` → `top-crm-tools-for-real-estate-teams`
→ `best-crm-for-real-estate`). Link qua redirect vẫn chạy nhưng loãng tín hiệu và sẽ chết khi dọn redirect.

| Stub (301) | Đích thật | Link |
|---|---|---|
| `best-ai-chatbot-for-real-estate-lead-capture` | `best-chatbot-customer-service-real-estate` | 13 |
| `best-ai-chat-platform-real-estate` | `best-chatbot-customer-service-real-estate` | 7 |
| `conversational-chat-real-estate` | `what-is-a-conversational-chatbot-real-estate` | 3 |
| `top-crm-tools-for-real-estate-teams` | `best-crm-for-real-estate` | 2 |
| `top-crm-tools-real-estate-teams` | `best-crm-for-real-estate` (2 hầu) | 1 |

**Cách xử lý, 3 loại:**

1. **20 link đổi href, giữ nguyên anchor.**
2. **5 anchor là TÊN NGUYÊN VĂN của trang đã xoá** (`Best AI Chatbot for Real Estate Lead Capture`)
   thì viết lại cho đúng đích mới, mỗi bài một biến thể khác nhau (#110, #117, #172, #207, #214).
   Để nguyên là đang giới thiệu một trang không còn tồn tại.
3. **5 chỗ sau khi đổi sẽ thành 2 link cùng trỏ 1 pillar** thì bỏ bớt 1.

⚠️ **Chính sách bỏ bớt link trong cùng bài, đã phải đảo lại giữa chừng.** Ban đầu tôi giữ link
thân bài và gỡ link cuối bài, theo đúng ưu tiên "link thân bài tốt hơn". Đọc lại 5 câu thì thấy hỏng:
câu cuối bài luôn có dạng *"our guide to X"*, *"our roundup of X"*, bỏ link đi thành hứa một bài rồi
không cho đường đi. Anchor thân bài ngược lại chỉ là cụm danh từ (*"a real estate AI chat platform
built for team-wide use..."*), bỏ link vẫn đọc trôi. Nên **gỡ link thân bài, giữ link cuối bài**.
Quy tắc rút ra: ưu tiên vị trí là chuyện lúc VIẾT; lúc GỠ thì chọn theo câu nào hỏng nếu mất link.

Riêng `#521` có 2 câu cuối bài cùng trỏ về `#89`, không câu nào bỏ link được, nên xoá hẳn 1 câu.

**20 bài đã sửa:** 110, 117, 172, 189, 207, 214, 286, 293, 513, 521, 528, 899, 1034, 1134, 1140,
1158, 1191, 1209, 1266, 1308.

**Verify sau khi sửa** (HTTP từng slug đích, không suy từ nội dung):

| Chỉ số | Kết quả |
|---|---|
| Slug đích không trả 200 | **1/113**, là `real-estate-customer-engagement-strategies` (#1488, live 08/10 10:00) |
| Link còn trỏ vào stub 301 | **0** |
| Bài tôi sửa có >1 link cùng 1 pillar | **0** |

Đa dạng anchor của 3 đích **tăng chứ không giảm**, dù chúng nhận thêm 26 link:

| Đích | Trước | Sau |
|---|---|---|
| `best-chatbot-customer-service-real-estate` | 12 link / 6 anchor, 50% | 28 / 19, **68%** |
| `what-is-a-conversational-chatbot-real-estate` | 9 / 8, 89% | 11 / 10, **91%** |
| `best-crm-for-real-estate` | 53 / 42, 79% | 55 / 44, **80%** |

Đổi hướng không dồn thêm tải lên pillar: Google đã gộp tín hiệu qua 301 từ trước, việc này chỉ bỏ
cái hầu ở giữa.

⚠️ **4 bài có sẵn 2 link cùng trỏ 1 pillar, có từ trước, không thuộc Batch A:** `#1449`,
`#918` (cả hai → `#207`), `#481` (→ `#172`), `#390` (→ `#89`). Đã đối chiếu với bản chụp trước khi
sửa để chắc không phải do lần này gây ra. Để lại cho đợt dọn anchor.

⚠️ **Claim "78% of buyers choose the first agent to respond" còn ở `#521` và `#172`**, ngoài `#207`
đã biết. Phát hiện dọc đường, không sửa vì ngoài phạm vi Batch A.

⚠️ **Một lỗi phương pháp đã bắt được trước khi nó gây hậu quả.** Bản kê stub đầu tiên của tôi
dựng bằng cách grep chữ "merge"/"301" trong `content-plan.md`, nên `what-is-a-conversational-chatbot-real-estate`
lọt vào oan (nó là đích, không phải stub) và bản kê báo nhầm 10 link. Cách đúng là **HTTP từng
slug đích** rồi xem mã trả về, không suy từ tài liệu. Làm lại cho ra 26 link chứ không phải 10.

---

## 2026-10-08 10:16 — Verify #1488 sau khi live, lần đầu chạy Bước 6.5 bản mới

`#1488` (`real-estate-customer-engagement-strategies`) publish đúng lịch 08/10 10:00. Đây là **bài đầu
tiên chạy qua Bước 6.5 phiên bản Option B**, nên ghi lại đầy đủ để đối chiếu về sau.

### Chiều về: không động tới pillar, đúng rule mới

| Kiểm tra | Kết quả |
|---|---|
| URL `#1488` | HTTP **200**, hết 404 |
| `#1487` vẫn link sang `#1488` | **có**, anchor `real estate customer engagement tactics` |
| Số bài phải sửa thêm để có inbound | **0** |

Inbound đến từ `#1487`, một **cluster cùng cụm**, đúng nguồn ưu tiên. **Không thêm link nào từ `#207`
hay `#1232`.** Theo cách cũ thì đây là link thứ 54 đổ vào `#207`; theo rule mới pillar đứng yên.

### Chạy khối GATE/WARN nguyên văn từ SKILL.md

```
1185 chu, 6 link, 5.1/1000 chu, than bai 6 / cuoi bai 0
```

**GATE pass cả 3:** link lên pillar đúng 1 lần, >= 2 link ngang cùng cụm, bài donor đã trỏ sang.

Mật độ 5,1 link/1.000 chữ nằm trong mốc 4-6. **100% link nằm trong thân bài** (6 thân / 0 cuối), so
với hiện trạng toàn site 41% thân bài. Ảnh 3/3 (1 featured + 2 trong bài), 0 figure rỗng, cả 3 alt
đều chứa FOCUS_KW `real estate customer engagement`. Không cần generate thêm ảnh.

### 3 WARN, do chính check mới thêm sáng nay bắt được

```
WARN: anchor 'ai intent layer for real estate crm'  -> ai-intent-layer-for-real-estate-crm   da duoc 9 bai khac dung
WARN: anchor 'crm marketing for real estate'        -> crm-marketing-real-estate             da duoc 5 bai khac dung
WARN: anchor 'customer engagement platform vs crm'  -> customer-engagement-platform-vs-crm   da duoc 2 bai khac dung
```

⚠️ **Cả 3 đều là anchor trỏ tới LINK NGANG, không phải pillar.** Check cũ chỉ soát `PILLAR_SLUG` nên
sẽ báo **0 warning** cho đúng bài này. Đây là bằng chứng đầu tiên, trên một bài thật, rằng việc mở rộng
WARN sang link ngang là đúng: nó bắt được lỗi ngay lần chạy đầu tiên.

Cả 3 là WARN chứ không phải GATE nên **không sửa bài**, chỉ ghi nhận. Riêng
`ai-intent-layer-for-real-estate-crm` đáng chú ý: nó đang ở 12 link / 3 anchor (25%), bài này làm thành
13 link / 3 anchor, tức **tụt xuống 23%**. Thuộc đợt dọn anchor chưa chạy.

### Rút ra cho lần sau

Quy tắc 5 ở mục anchor (đọc anchor đã dùng **trước khi viết**) hiện chỉ được nhắc cho anchor trỏ
pillar. Bài này cho thấy phải chạy `anchors_to()` cho **cả 2-3 slug link ngang** trước khi viết, không
chỉ cho pillar. WARN bắt được là tốt, nhưng bắt trước khi viết thì không tạo ra nợ.

---

## 2026-10-09 | Đợt D: gỡ mồ côi cho 10 bài real estate

### Vấn đề

Quét toàn site (147 bài publish) tìm bài không có **một link nội bộ nào trỏ vào**. Ra 21 bài, sau khi
đã loại 12 slug là stub 301 (trang của chính nó không trả 200 nên không tính là bài). Trong 21 bài đó,
10 bài thuộc chủ đề real estate, 11 bài còn lại là bài AI/tech không cùng cụm nào.

Đợt D xử lý 10 bài real estate: mỗi bài được **đúng 1 link vào, từ một bài cùng cụm**, chèn trong
thân bài chứ không phải mục cuối bài. Không dùng pillar làm nguồn dẫn, theo đúng luật: pillar là nơi
nhận link, không phải nơi phát link cho từng bài news.

### Phát hiện: 9/10 bài không có cụm được ghi ở đâu cả

Chỉ #1467 có pillar/cụm ghi trong `references/used-keywords.md`. 9 bài còn lại là bài News hằng ngày,
không nằm trong bảng cụm của `content-plan.md` và cũng không có dòng nào trong used-keywords.

Vì vậy cụm của từng bài được xác định bằng tay, lấy **chính link pillar mà bài đó trỏ ra** làm căn cứ
đối chiếu. Đây là lý do gốc khiến 10 bài này mồ côi: không có bảng nào ghi chúng thuộc cụm nào thì
cũng không có bước nào bắt phải dẫn link vào chúng.

### Bảng nguồn dẫn

| Bài nguồn | Dẫn vào | Anchor |
|---|---|---|
| #223 | #1415 | what a real estate lead now costs |
| #172 | #1341 | assistants that write the post-tour text themselves |
| #1254 | #1209 | one brokerage has its AI read the contract and pay the commission |
| #1213 | #1467 | the seller check-in calls nobody has hours for |
| #1100 | #1335 | a room visualiser turning listing photos into showing requests |
| #622 | #1197 | one MLS now runs its own AI search with no lead forms |
| #1134 | #1191 | a mortgage broker finder now lives inside ChatGPT |
| #1308 | #1158 | the chatbot sycophantic about home prices |
| #1529 | #1128 | what brokerage leaders now say worries them most |
| #1462 | #1034 | an AI hybrid brokerage charges a flat fee instead |

Mỗi anchor là một cụm mô tả riêng, không lặp lại anchor nào đã dùng ở bài khác. Trước khi ghi, mỗi
bài đều qua `assert c.count(anchor) == 1`, đếm em dash trước/sau không đổi, và độ dài chỉ tăng
158-292 ký tự.

### 4 lỗi câu chữ bị bắt khi đọc lại, không phải khi chạy máy

Script chèn đúng vị trí anchor nhưng câu đọc lên thì hỏng. Cả 4 chỉ lộ ra khi đọc lại nguyên đoạn:

- **#622**: câu chèn cắt ngang một mệnh đề, làm đứt câu gốc. Phải neo lại vào ranh giới câu.
- **#1308**: chèn xong thành câu dài lê thê không ngắt.
- **#1529**: thành ba vế "and ... and ... and" liên tiếp, đọc rối.
- **#223**: câu chèn nằm chen giữa "không có độ trễ nào" và "Capture is automatic and immediate",
  tách đôi ý đang liền mạch. Chuyển xuống cuối đoạn thì đọc trôi.

Ngoài ra #1213 lần chạy đầu fail assert vì anchor trong script là "...route anything nuanced to a
human." trong khi bản live là "...to a human quickly." Assert làm đúng việc của nó.

### Kết quả

Đếm lại trên bản live sau khi sửa: cả 10 bài đều nhận đúng 1 link vào từ đúng bài nguồn đã định.
Số bài mồ côi **21 → 11**. 11 bài còn lại đúng bằng nhóm bài AI/tech (#1, #14, #26, #31, #34, #37,
#41, #44, #47, #50, #53). Nhóm này không sửa được bằng link vì không thuộc cụm nào, cần quyết định
hướng xử lý chứ không phải thêm link.

### Rút ra cho lần sau

Bài News mới viết xong mà không bài nào dẫn vào thì vài tháng sau không ai biết nó mồ côi, vì không
có bảng nào ghi nó thuộc cụm nào để mà soát. Nên ghi cụm của bài News vào used-keywords ngay lúc
đăng, để lần quét sau có căn cứ đối chiếu thay vì phải suy ra từ link pillar.

---

## 2026-10-09 | Đợt B: đa dạng anchor cho 10 pillar

### Vấn đề

Quy tắc 7 trong `external-seo-toolkit/references/internal-linking-guide.md` đặt mốc **anchor khác
nhau / tổng link tới 1 trang >= 70%**. Đo lại trên bản live: **9/10 pillar dưới mốc**, chỉ
`best-crm-for-real-estate` đạt (81%).

| Pillar | Trước | Sau |
|---|---|---|
| `tcpa-compliance-for-real-estate-agents` | 13% | 100% |
| `real-estate-website-builder` | 19% | 100% |
| `website-design-for-real-estate-agents` | 20% | 100% |
| `ai-intent-layer-for-real-estate-crm` | 23% | 100% |
| `real-estate-landing-page-guide` | 40% | 100% |
| `real-estate-lead-follow-up-automation-guide` | 41% | 100% |
| `best-conversational-ai-chatbot-for-real-estate` | 44% | 100% |
| `best-ai-voice-assistants-for-real-estate` | 55% | 100% |
| `best-chatbot-customer-service-real-estate` | 67% | 100% |
| `best-crm-for-real-estate` | 81% | 81% (không động) |

Tổng: **80 anchor viết lại trên 63 bài**, cộng 2 link trùng bị gỡ.

### Cách làm: sửa vào bản làm việc cục bộ trước, đẩy sau

63 bài nhưng 80 anchor, nghĩa là nhiều bài dính 2-3 pillar cùng lúc (#138 dính 3, #1488 dính 3).
Nếu sửa pillar nào đẩy pillar đó thì lần đẩy sau sẽ đè mất sửa của lần trước, vì `update_post`
luôn ghi đè toàn bộ nội dung.

Cách làm: dựng một kho cục bộ `b_work.pkl`, mỗi patch là bộ ba `(post_id, chuỗi_cũ, chuỗi_mới)` và
`assert` chuỗi cũ xuất hiện **đúng 1 lần** trước khi thay. Sửa hết 10 pillar vào kho đó, rồi mới
đẩy mỗi bài đúng 1 lần. Đổi 80 lần ghi thành 63 lần, và không còn khả năng đè nhau.

### Nguyên tắc viết anchor

Theo quy tắc 4 của guide, anchor **không bắt buộc chứa keyword của trang đích**, chỉ cần mô tả
đúng trang đích. Đó chính là nguyên nhân gốc: ép anchor phải chứa `PILLAR_KW` thì mọi bài đổ dồn
về cùng một chuỗi.

Nên 80 anchor mới đều mô tả trang đích từ góc riêng của bài nguồn. Ví dụ với pillar TCPA, 15 bài
dẫn vào bằng 15 cách khác nhau: "where those FCC rules actually land", "which callbacks need
consent on file", "who is liable when an agent leaves", "how a stop request has to propagate",
"the rules on automated calls and texts". Không anchor nào chứa chữ TCPA, nhưng đọc tách khỏi câu
vẫn đoán được trang đích nói gì, đúng phép thử của quy tắc 1.

### Máy kiểm xong vẫn phải đọc lại: 10 câu bị lặp từ

Toàn bộ 80 patch qua được assert, 0 em dash mới, thẻ `<a>` cân bằng. Nhưng đọc lại từng câu thì
thấy **10 chỗ câu đọc lên bị vướng**, không chỗ nào máy bắt được:

- **#528** "shared chat layer" lặp 2 lần trong cùng một câu
- **#936** "platforms" lặp, cộng "behavioral" rồi "behavior" ngay sau
- **#1219** "the 7 answering tools we rated" đặt làm đích của "our own comparison is in" nghe không xuôi
- **#1225** "the system that works the leads" sai ngữ pháp, phải là "those leads"
- **#1227** chữ "first" bị treo ở cuối câu sau khi đổi anchor
- **#1234** "activity log" lặp lại chỉ sau 8 chữ
- **#1462** "surfaces/surfacing ... that moved" lặp ý câu ngay trên
- **#1473** "website builders" rồi "website side" trong cùng câu
- **#1488** anchor có dấu phẩy ở giữa làm câu khó đọc
- **#1529** "Inbound" rồi "inbound" liền nhau

Đây là lần thứ hai trong tuần bài học này lặp lại (đợt D bắt 4 chỗ tương tự). **Assert kiểm được
chuỗi có tồn tại không, không kiểm được câu đọc lên có xuôi không.** Phải đọc.

### Phát hiện thêm: 17 bài phạm quy tắc 6

Quét ra **17 bài có 2 link trỏ cùng một trang đích**, vi phạm quy tắc 6 (mỗi bài chỉ 1 link tới 1
đích). Hai cái dính đúng pillar đang sửa nên xử lý luôn:

- **#918** trỏ 2 link tới `real-estate-website-builder`. Giữ link giữa bài có ngữ cảnh, gỡ link
  trong đoạn đọc thêm cuối bài.
- **#390** trỏ 2 link tới `best-chatbot-customer-service-real-estate`. Giữ link đầu với anchor mô
  tả, gỡ link thứ hai dùng anchor chung chung.

**15 bài còn lại trỏ tới trang không phải pillar nên để lại**, nằm ngoài phạm vi đợt B:
#230, #299, #419, #461, #475, #481, #492, #498, #504, #513, #528, #975, #1243, #1449, và #918
(với `best-crm-for-real-estate`).

### Verify

Fetch lại toàn bộ 147 bài qua REST sau khi đẩy, so từng bài với bản local: **63/63 khớp
byte-for-byte**. Đo lại đa dạng anchor trên bản live: cả 10 pillar đều >= 70%.

Số trên bản live cao hơn bản local vài link (website-builder 27 thay vì 25) vì bản live đếm cả
link nằm trong 12 trang stub 301. Stub không phải trang thật nên không tính khi đặt mục tiêu.

### Còn lại

- **9 anchor dài quá 9 từ** (quy tắc 3 đề 3-8 từ), tất cả đều có sẵn từ trước, không phải anchor
  mới viết: #492, #1217, #610, #622, #214, #1227, #1449, #390, #528.
- **15 bài phạm quy tắc 6** liệt kê ở trên.

## 2026-10-09 | Đợt C: đa dạng anchor cho 12 trang không phải pillar

### Vấn đề

Cùng mốc quy tắc 7 (anchor khác nhau / tổng link >= 70%) nhưng áp cho trang không phải pillar có
từ 5 link trỏ vào. Đo trên bản live: **12 trang dưới mốc**. Ước lượng ban đầu là 11 trang / 30
anchor, đo lại ra 12 trang / 38 anchor tối thiểu.

| Trang đích | Trước | Sau |
|---|---|---|
| `ai-crm-real-estate` | 9/23 = 39% | 17/22 = 77% |
| `crm-pipeline-management` | 5/12 = 42% | 9/12 = 75% |
| `chatbot-vs-conversational-ai-real-estate` | 6/11 = 55% | 9/11 = 82% |
| `broker-idx-guide` | 3/10 = 30% | 8/10 = 80% |
| `crm-marketing-real-estate` | 3/9 = 33% | 7/9 = 78% |
| `idx-website-for-realtors` | 4/8 = 50% | 6/8 = 75% |
| `best-chatbot-builder-real-estate` | 4/8 = 50% | 6/7 = 86% |
| `follow-up-boss-real-estate-crm` | 3/6 = 50% | 5/6 = 83% |
| `what-does-crm-mean-in-real-estate` | 1/5 = 20% | 3/4 = 75% |
| `best-crm-for-real-estate-teams-2026` | 1/5 = 20% | 4/5 = 80% |
| `ai-outbound-calling-real-estate-lead-follow-up` | 3/5 = 60% | 4/5 = 80% |
| `open-house-landing-page` | 1/5 = 20% | 4/5 = 80% |

Tổng: **39 anchor viết lại, 3 link trùng bị gỡ, trên 34 bài** (đo bằng so link trước/sau, không
phải ước lượng).

### Cách làm

Cùng cách đợt B: dựng toàn bộ patch trong bản làm việc cục bộ, mỗi patch `assert count == 1`,
kiểm số em dash, rồi đẩy mỗi bài đúng 1 lần. Đặt mục tiêu **75%** thay vì 70% để có biên, và chỉ
sửa **số anchor tối thiểu** cho mỗi trang đích, không viết lại hết. Anchor mới mô tả trang đích từ
góc của bài nguồn, không ép chứa keyword (quy tắc 4). Ví dụ trang `ai-crm-real-estate` có 8 bài
dẫn vào bằng 8 cách khác nhau: "what an AI-driven CRM actually automates", "the AI features worth
paying for in a CRM", "AI that qualifies leads inside the CRM", "CRMs with AI at the core"...

### Đọc lại bắt thêm 6 chỗ câu vướng

Máy kiểm (assert, em dash, thẻ `<a>` cân bằng) qua hết, nhưng đọc lại từng câu thì còn 6 chỗ phải
sửa: lặp "actually", câu "that is a useful question" nghe sáo, lặp "landing page", lặp
"follow-up", lặp "marketing automation", lặp "top IDX" và "search quality". Đây là lần thứ ba bài
học này lặp lại (đợt D 4 chỗ, đợt B 10 chỗ). Assert kiểm được chuỗi có tồn tại, không kiểm được
câu có xuôi không.

### Phát hiện thêm: quy tắc 6

Ba bài trong phạm vi có 2 link cùng một đích, đã xử lý luôn:

- **#230** trỏ 2 link tới `what-does-crm-mean-in-real-estate`. Giữ link đầu (đổi anchor), gỡ link
  thứ hai.
- **#461** trỏ 2 link tới `best-chatbot-builder-real-estate`. Gỡ link ở mục Related Reading, câu
  được viết lại cho liền mạch.
- **#498** trỏ 2 link tới `ai-crm-real-estate`. Gỡ link thứ hai, đổi câu thành "settle that before
  adding a back office layer on top".

**12 bài còn lại vẫn vi phạm quy tắc 6** và nằm ngoài phạm vi đợt C vì đích không thuộc 12 trang
trên: #299, #419, #475, #481, #492, #504, #513, #528, #975, #1243, #1449, và #918 (với
`best-crm-for-real-estate`).

### Sự cố trong lúc đẩy

Đẩy tay từng bài (không có chế độ patch) nên có 1 lỗi chép: lần đẩy đầu của **#461** tôi gõ lại
anchor từ trí nhớ thay vì copy đúng từ `cout/461.html`. Phát hiện ngay khi đối chiếu lại, đã đẩy
lại bản đúng trước khi verify. Bài học: khi đẩy hàng loạt phải copy nguyên văn từ file đã
proofread, không gõ lại.

### Verify

Fetch lại toàn bộ 147 bài qua REST, so 34 bài với bản local: **34/34 khớp về chữ và link**. 3 bài
(#461, #498, #504) lệch 8 ký tự so với byte-for-byte, và chỉ do WordPress chuẩn hóa thuộc tính
`style` của thẻ `<img>` (`max-width: 100%; height: auto;` thành `max-width: 100%;height: auto`).
Không liên quan nội dung.

Chạy lại `c_audit.py` trên bản live: **0 trang non-pillar dưới 70%**. Chạy lại đo 10 pillar: tất cả
vẫn >= 70% (thấp nhất `best-crm-for-real-estate` 80%), nên đợt C không làm tụt pillar nào.

### Còn lại

- **12 bài phạm quy tắc 6** liệt kê ở trên.
- **9 anchor dài quá 9 từ** có sẵn từ trước, chưa động (xem đợt B).
- **Đợt E**: 11 bài AI/tech mồ côi (#1, #14, #26, #31, #34, #37, #41, #44, #47, #50, #53), chờ quyết
  định giữ nguyên, lập cluster riêng, hay noindex.

## 2026-10-12 | Đợt E: 11 bài AI/tech lạc chủ đề, quyết định để nguyên

### Quyết định

11 bài (#1, #14, #26, #31, #34, #37, #41, #44, #47, #50, #53, tổng khoảng 2.780 chữ, đăng
06-07/2026) là tin AI/tech chung, có trước khi site chuyển hẳn sang bất động sản. Ba lựa chọn đã
nêu từ plan mồ côi 07/10: để nguyên, đưa về draft, hoặc redirect. Chủ site chọn **để nguyên, chỉ
ghi quyết định**.

**Không có thay đổi nào trên site trong đợt này.** Không `update_post`, không redirect, không gỡ
bài. Chỉ cập nhật tài liệu: `content-plan.md` (Batch 3 đánh dấu đã quyết) và
`references/teardown-infina-table.md` (ghi chú cột "Mồ côi").

### Lý do và hệ quả

- Vá link cho nhóm này sẽ làm loãng topical authority bất động sản mà không giúp gì, nên không vá.
- 11 bài này **là ngoại lệ có chủ đích**, không tính vào số trang mồ côi khi đo ở các lần
  teardown sau. Mốc mồ côi hợp lệ giờ là 0 trang thuộc 8 cụm và News real estate.
- Công cụ WordPress hiện có không đặt được `noindex` (`update_post` chỉ có title, description,
  focus keyword), nên `noindex` không phải lựa chọn khả thi nếu sau này đổi ý.

### Còn lại

- File `exports/teardown-infina-table.{docx,html}` được dựng từ bản md cũ, chưa dựng lại sau ghi
  chú này. Bản md là nguồn đúng.
- Nếu sau này muốn gỡ nhóm này, chưa có dữ liệu traffic/backlink của 11 URL (chưa có quyền GSC
  trong môi trường). Nên kiểm tra GSC trước khi chuyển draft hoặc redirect.

## 2026-10-12 | Đợt F: 12 bài vi phạm quy tắc 6 (hai link cùng đích trong một bài)

### Việc đã làm

12 bài (#299, #419, #475, #481, #492, #504, #513, #528, #975, #1243, #1449, #918) có hai link
trỏ cùng một URL đích trong cùng bài, vi phạm quy tắc 6 của guide. Mỗi bài sửa đúng **một** link:

- Giữ link trong thân bài (có ngữ cảnh), bỏ hoặc viết lại link trùng ở mục Related Reading.
- Khi câu Related Reading chỉ còn lại mỗi link trùng, viết lại câu để vẫn đọc được, không để câu
  cụt hoặc bỏ cả mục.
- Dùng `update_post` với toàn bộ nội dung (không có chế độ patch), mỗi bài đã đọc lại bản live trước
  khi đẩy.

### Kết quả đo lại trên bản live

- 12/12 bài khớp bản đã soát (WordPress chuẩn hóa style của thẻ `img`, khác vài ký tự, vô hại).
- Số bài có hai link cùng đích trên toàn site: **0**.
- Toàn bộ pillar vẫn đạt tỉ lệ anchor khác nhau >= 70%.

### Còn mở (không thuộc đợt này)

- Tiêu đề #299 có dấu gạch dài (em dash).
- 9 anchor dài hơn 9 từ (có từ trước).

## 2026-10-12 | Chốt bộ vai trò bài trong cụm: 9 họ

### Quyết định

Cột "Vai trò" trong bảng cụm của `content-plan.md` từng có **67 giá trị khác nhau**, không máy nào
phân loại được. Chủ site chốt gom về **9 họ**: `pillar`, `review`, `compare`, `buying-guide`,
`explainer`, `how-to`, `niche`, `news-support`, `bridge`.

### Thay đổi

- Tạo `references/cluster-roles.md`: định nghĩa từng họ, cách link, số bài hiện có, bảng ánh xạ
  nhãn cũ sang họ.
- `content-plan.md`: **87/87** dòng có URL được gán họ. Mã đặt ở đầu ô, nhãn cũ giữ phía sau để
  không mất thông tin (niche, brand, HUB...).
- `skills/news-to-cluster-article/SKILL.md` Bước 4: thêm mục 5, bài News luôn là `news-support`, trỏ
  về `references/cluster-roles.md`.
- `external-seo-toolkit/references/internal-linking-guide.md` mục 5: thêm bước khai vai trò.

### Lưu ý

- Bộ 9 họ là do trợ lý gom từ dữ liệu có sẵn. Chủ site chốt con số 9 nhưng **chưa duyệt từng nhãn**.
  Nhãn nào xếp sai họ thì sửa mã trong `content-plan.md` và bảng ánh xạ cuối `cluster-roles.md`.
- Vai trò chỉ phục vụ biên tập và script đo, không phải tín hiệu SEO.

## 2026-10-12 | Đợt G: cụm 5 và 6 về mốc 50%, rút ngắn 8 anchor quá dài

### Phát hiện trước khi sửa: cách sửa trong guide không làm được

Đo lại trên bản live (150 bài, thành viên cụm lấy từ `content-plan.md`): Cụm 5 trỏ pillar nhà **5, ra
ngoài 10 = 33%**. Cụm 6 trỏ pillar nhà **5, ra ngoài 9 = 36%**. Số 36% hôm nay làm tròn từ 35,7%
(5/14), guide ghi cùng con số.

Guide khuyên "thêm link về pillar nhà, đừng gỡ link chéo". Với hai cụm này **không thể làm vậy**:
quy tắc 6 cho mỗi bài một link tới một đích, và cả 5 bài cluster của mỗi cụm đã link về pillar nhà
rồi. Số link nhà đã chạm trần 5, chỉ còn cách giảm số link ra ngoài. Ba cụm khác cũng sát mốc: Cụm 4
đang đúng 50% (5/10).

### Việc đã làm (9 bài, mỗi bài bỏ đúng 1 câu có link chéo)

- Cụm 5: bỏ câu trỏ `best-crm-for-real-estate` ở #981, #993, #999, #1005, #1011. Giữ link sang
  `real-estate-website-builder` vì liên quan trực tiếp tới chủ đề website. Kết quả 5/10 = **50%**.
- Cụm 6: bỏ câu trỏ `real-estate-website-builder` ở #948, #918, #936, #942. Giữ link sang
  `best-crm-for-real-estate` vì landing page luôn nối tới khâu follow-up. Kết quả 5/10 = **50%**.
- Mỗi câu bị bỏ là câu đóng của đoạn Related Reading hoặc một câu đứng riêng, không câu nào bị cắt
  cụt. Ở #918 câu đó chiếm cả đoạn nên bỏ nguyên đoạn.
- Đây là **ngoại lệ so với lời khuyên "đừng gỡ link chéo"**, có chủ đích và đã ghi vào guide.
- Hệ quả: pillar CRM mất 5 link vào từ cụm 5, `real-estate-website-builder` mất 4 từ cụm 6.

### Anchor quá dài (>9 từ)

8 anchor viết lại về 3-8 từ, giữ nguyên câu, đổi thứ tự chữ quanh anchor khi cần: #492, #610, #622,
#214, #1227, #1449, #390, #528. Danh sách cũ ghi 9 bài, nhưng **#1217 đã không còn anchor dài**
(đang 5, 7 và 6 từ).

**Số "9" trước đây chỉ đếm trong phạm vi đợt B.** Quét toàn site hôm nay thấy **46 anchor dài hơn 9
từ, trên 37 bài**, còn lại **38 trên 29 bài** sau đợt này. Trong 38 có 7 anchor nằm trong trang stub
301 mà tên trang gộp là anchor có chủ đích, nên thực sự còn **31** để quyết định có sửa tiếp không.

### Verify

- Fetch lại 17 bài từ bản live, so với file đã soát: **17/17 khớp** (sau khi chuẩn hóa style `img`).
  Một bài (#1011) lệch lần đầu vì chép thừa chữ "investment" ở đoạn cuối, đã đẩy lại và khớp.
- Số bài có hai link cùng đích: **0**.
- Anchor đa dạng sau đợt: `best-crm-for-real-estate` 40/50 = 80%, `ai-crm-real-estate` 18/23 = 78%,
  các pillar còn lại không đổi.
- Chỉ số tỉ lệ nhà toàn site: Cụm 1 88%, Cụm 2 74%, Cụm 3 64%, Cụm 4 50%, Cụm 5 50%, Cụm 6 50%,
  Cụm 7 70%, Cụm 8 83%.

### Còn lại

- 31 anchor dài ngoài phạm vi (nhiều bài News viết gần đây, trong đó có 2 anchor của #1732 do skill
  này viết). Quy tắc 3 viết "khoảng 3-8 từ" nên đây là việc biên tập, chưa phải lỗi cứng.
- Cụm 4, 5, 6 đang đúng mốc 50%, bài mới trong cụm phải link về pillar nhà và hạn chế link ra pillar
  khác, nếu không sẽ tụt dưới mốc ngay.

## 2026-10-12 | Đợt H: rút ngắn toàn bộ anchor dài, skill chặn anchor quá 8 từ

### Yêu cầu và phạm vi

Chủ site yêu cầu "sửa nốt 31 anchor dài" và "update skill viết bài để anchor không quá 8 chữ". Ngưỡng
8 từ (không phải 9) nên phạm vi rộng hơn con số 31 đã báo trước đó, vì con số 31 đếm anchor dài hơn 9 từ.

Đo lại bản live trước khi sửa, không kể 7 trang stub 301 (anchor là tên trang gộp, có chủ đích):
**64 anchor dài hơn 8 từ, trên 41 bài** (33 anchor đúng 9 từ, 31 anchor từ 10 từ trở lên).

### Việc đã làm

- 41 bài, `update_post` toàn bài, mỗi bài đã so với bản live sau khi đẩy.
- Mọi anchor rút về **3-8 từ**. Cách rút: để link chỉ bao phần danh từ cốt lõi, phần còn lại của mệnh
  đề dời ra ngoài thẻ `<a>`, giữ nguyên ý câu. Ví dụ `how a real estate agent CRM closes the 15-hour
  response gap` (11 từ) thành `how a CRM closes the 15-hour response gap` (8 từ).
- Các anchor trỏ cùng một đích được viết lại thành biến thể khác nhau để không làm giảm đa dạng
  (ví dụ 5 anchor trỏ `ai-chatbot-mls-data-security-risk-brokerages` giờ là 5 chuỗi khác nhau).
- Bài News do skill này viết (#1732, #1739, #1746) cũng được sửa.
- Apostrophe mới dùng cùng kiểu với bài chứa nó (entity `&#8217;` hay ký tự `’`).

### Verify

- **41/41 bài khớp** bản đã soát sau khi fetch lại từ REST (chuẩn hóa style `img`). Lần đẩy đầu của #1011
  (đợt G) từng lệch một chữ do chép sai; cơ chế đối chiếu này tồn tại vì lỗi đó.
- Anchor dài hơn 8 từ ngoài stub: **0**. Còn đúng 7 anchor trong trang stub 301.
- Bài có hai link cùng đích: 0. Không target nào có tối thiểu 5 link mà đa dạng anchor dưới 70%:
  `best-crm-for-real-estate` 78%, `ai-crm-real-estate` 78%, `real-estate-website-builder` 96%.
- Tỉ lệ link về pillar nhà không đổi so với đợt G: Cụm 4, 5, 6 đều 50%.

### Thay đổi trong skill

- `SKILL.md`, quy tắc anchor số 3: từ "khoảng 3-8 từ" thành **tối đa 8 từ, giới hạn cứng**, kèm cách rút.
- `SKILL.md`, Bước 6: thêm hàm `long_anchors()` và GATE `assert` trước `create_post`. Hàm đã chạy thử
  trên 3 ca (đạt, quá dài, link ngoài).
- `SKILL.md`, Bước 6.5: câu chèn vào bài donor cũng phải qua `long_anchors()`.
- `internal-linking-guide.md`: quy tắc 3 thành tối đa 8 từ, thêm GATE trước publish số 7, đánh số lại
  các GATE sau publish.

### Còn lại

- 7 anchor trong trang stub 301 giữ nguyên (tên trang gộp làm anchor là có chủ đích).
- Check mới chỉ quét bài mới trước khi publish. Bài cũ viết sau này bị chỉnh tay vẫn có thể lọt, nên
  vẫn nên chạy `long_anchors()` trong lần quét định kỳ toàn site.

## 2026-10-12, Đợt I: pillar Cụm 9 `real estate marketing` (#1825)

- Đăng pillar mới `/real-estate-marketing/` (#1825): 2.305 chữ, density 0,52%, 13 H2, 2 bảng, 4 ảnh AI (HERO ảnh thật, STATS làm featured, COMPARISON, DEMO), 1 nguồn ngoài dofollow (Virginia REALTORS tóm tắt NAR 2025 Profile: 43% người mua qua referral, 18% qua agent cũ, 66% người bán qua referral hoặc agent cũ), 6 link nội bộ ra #1223, #975, #930, #1415, #1229, #263 (anchor ≤8 từ, `check_targets` 200 hết).
- Category: ban đầu "CRM Software" (85). Cùng ngày user yêu cầu tạo category riêng: lần đầu tạo bằng tên thất bại do lỗi snippet (xem SKILL.md mục category), sau khi user dán lại snippet đã tạo "Real Estate Marketing" (ID 392) và gán #1825, verify qua REST.
- Tiêu đề đổi từ bản plan ("The Complete Guide for Agents") sang "Real Estate Marketing Guide: What to Do, Spend and Measure" vì bản plan trùng 0,75 từ với title #598 (vượt ngưỡng 0,6). Slug giữ nguyên `real-estate-marketing`.
- Donor: #1152 (Related Reading thêm 1 câu, anchor "real estate marketing guide for agents"), đã diff live khớp.
- Độ dài 2.305 chữ gần mốc 2.400 của công thức wave 1; mục Related Reading chưa có vì chưa có cluster. Khi cluster lên, thêm mục này và tỉa bớt link chéo sang cụm khác để mốc "trỏ pillar nhà ≥50%" đạt.
- Ảnh HERO sinh lần 1 lộ chữ DELL trên laptop, đã sinh lại với "unbranded laptop".

## 2026-10-12, Đợt J: hub Cụm 9 `real estate branding` (#1832)

- Đăng hub `/real-estate-branding/` (#1832): 1.715 chữ, density 0,70%, 12 H2, 1 bảng, 4 ảnh AI, category Real Estate Marketing (392). Nguồn ngoài dofollow: trang NAR "logo use with a firm name" (đã mở trang gốc: dấu REALTOR® đứng cạnh tên công ty nhưng không nằm trong tên công ty; hội viên dùng được trên name card; người có license không phải hội viên không dùng logo REALTOR® trên card). Bỏ câu về tên team vì không tìm được nguồn xác nhận.
- Link nội bộ: lên pillar #1825 (1 lần), ra #975 và #1011 (đều Cụm 5), anchor ≤8 từ, 3/3 trả 200.
- Chiều về: pillar #1825 thêm 1 câu trỏ sang hub trong mục "Direct Mail, Print, and Branding Basics" (anchor "practical real estate branding guide"), đã diff live khớp. Cần thêm: hub trỏ ngược pillar đã có sẵn nên hai bài link 2 chiều.
- Title 0,60 và slug 0,67 trùng từ với vài bài khác, vì slug là keyword đầu cụm đã duyệt.
- Ảnh STATS có nhãn tên icon (Target, Name Tag...) chỉ gần đúng 5 phần của brand, chấp nhận được.

## 2026-10-12, Đợt K: cluster Cụm 9 `real estate marketing plan` (#1843)

- Đăng cluster đầu tiên của Cụm 9, `/real-estate-marketing-plan/` (#1843): 1.784 chữ, density 0,56%, 11 H2, 4 bảng, 4 ảnh AI, category Real Estate Marketing (392).
- Nguồn ngoài: NAR Member Profile 2025 (thu nhập gộp trung vị $58.100, chi phí kinh doanh trung vị $8.010 cho 2024, đã mở trang gốc; bài NAR không tách chi phí marketing nên bài nói rõ không có benchmark chính thức) và 24 CFR 100.75 trên Cornell LII (quảng cáo nhà ở, đã đọc điều khoản). Các con số chuyển đổi funnel, tỷ lệ 10% GCI và bảng chia ngân sách được ghi rõ là ví dụ minh họa, không phải benchmark.
- Link: lên pillar #1825, sang hub #1832 (brand sheet), ra #1223 (Cụm 7, 1 link cross-pillar). 3/3 trả 200, anchor ≤8 từ.
- Chiều về: #1825 thêm 1 câu trong mục "How to Build a Real Estate Marketing Plan in Five Steps" (anchor "real estate marketing plan template"), diff live khớp.
- SERP thưởng file template tải về; bài này chỉ có template dạng bảng copy được. Nếu muốn file thật cần làm Google Sheet hoặc CSV và đưa lên site, chưa làm.
- Ảnh DEMO sinh lần 1 bị nhãn LEARN lặp hai lần và gắn sai icon, đã sinh lại theo luồng thẳng, kiểm lại sạch.

### Bổ sung Đợt K: file template tải về (12/10/2026)

- Đã làm file `references/files/real-estate-marketing-plan-template.xlsx` (5 sheet: Start Here, Goal Backward, Budget, Plan, Quarterly Review; công thức kiểm bằng thư viện `formulas`, khớp số trong bài: 13 / 26 / 130 / 11, 6.000 USD = 500 USD/tháng). LibreOffice trong container không mở được file nào nên chưa mở thử bằng Excel hay Sheets thật.
- User upload lên Media Library (`/wp-content/uploads/2026/10/real-estate-marketing-plan-template.xlsx`); tải về qua HTTP 200 và so sánh từng byte với bản trong repo, giống hệt. `upload_media` của MCP chỉ nhận ảnh nên việc upload file không phải ảnh phải làm tay.
- Link tải đã gắn vào #1843 (đoạn "Prefer a spreadsheet?" ngay sau phần giới thiệu template) và nhắc trong #1825 (câu "includes a free Excel download"), diff live khớp.
- Google Drive connector chỉ share theo email, không đặt được "anyone with the link", nên không dùng cách Google Sheet "Make a copy"; chưa tạo file nào trên Drive.

## 2026-10-12, Đợt L: cluster Cụm 9 `real estate marketing ideas` (#1853), lên lịch

- Tạo #1853 `/real-estate-marketing-ideas/` ở trạng thái **future, 13/10/2026 10:00** (giờ site = UTC). 1.877 chữ, density 0,58%, 13 H2, 30 ý tưởng đánh số mỗi ý có nhãn Cost/Effort, 1 bảng "Ten Quick Wins", 4 ảnh AI, category Real Estate Marketing (392).
- Nguồn ngoài: 24 CFR 100.75 (quảng cáo nhà ở) và 12 CFR 1024.14 trên Cornell LII (RESPA Section 8, đã đọc điều khoản: cấm đưa/nhận thứ có giá trị theo thỏa thuận giới thiệu dịch vụ settlement, có ngoại lệ cho hoạt động quảng bá thông thường không gắn với giới thiệu). Link ra 1 bài cụm khác: `tcpa-compliance-for-real-estate-agents` (Cụm 8).
- **Lý do lên lịch thay vì đăng ngay (rule 1, tối đa 3 bài/ngày giờ site):** ngày 12/10 đã đăng 3 bài (#1825 04:06, #1832 04:16, #1843 08:12), đủ trần. Hệ quả cần biết: routine news 18:11 UTC ngày 12/10 sẽ đếm 3/3 và dừng, tức hôm nay không có bài news. Lỗi này do mình không đếm trần khi đăng liên tiếp 3 bài Cụm 9.
- **Quy ước lịch cho các cluster Cụm 9 còn lại:** tối đa 2 bài evergreen mỗi ngày, đặt 10:00 giờ site (và 14:00 nếu cần bài thứ hai), chừa 1 slot cho routine news 18:xx UTC. Trước khi tạo luôn `list_posts` future+publish để đếm.
- **Việc chờ sau 13/10 10:00:** (a) diff nội dung live với file; (b) thêm link vào pillar #1825 (không thêm trước vì đích chưa 200); (c) bài chưa có inbound nào cho tới (b).

### Cụm 9 wave 1: `real estate advertising` (#1859)

- Lên lịch #1859 `/real-estate-advertising/` ngày **13/10/2026 14:00** (giờ site = UTC): slot evergreen thứ hai của ngày, news 18:11 vẫn còn chỗ (ngày 13/10 = 2 evergreen + 1 news = 3). 1.724 chữ, density 0,64%, 11 H2, 3 bảng, 4 ảnh AI.
- Số chi phí chỉ lấy từ trang Ylopo mở trực tiếp (bài đăng 18/12/2024: CPL trung bình 66,69 USD, Facebook 5 đến 30 USD, Google 50 đến 150 USD, tối thiểu khoảng 1.500 USD/tháng) và ghi rõ là ước tính của một vendor bán dịch vụ. Ví dụ cost per closing là minh họa có nêu giả định.
- **Không dùng và không link số liệu của #1415** (xem cảnh báo bên dưới): bài đó ghi CPL 503 USD kèm 8.010 USD/năm và 2.850 USD/tháng, gán cho Ylopo, nhưng trang Ylopo đã mở không có các số đó.
- Link tới #1853 (đang scheduled 10:00 cùng ngày, sớm hơn bài này 4 giờ) nên hợp lệ khi bài này lên. `check_targets` bỏ qua slug scheduled sớm hơn.

### Cảnh báo chưa xử lý: số liệu của #1415 (`cost-per-lead-for-real-estate-agents`) không khớp nguồn đã gán

- #1415 viết "theo breakdown 2026 của Ylopo": CPL trung bình 503 USD (năm trước 448 USD), paid 480 USD, organic 416 USD, agent chi khoảng 8.010 USD/năm và 2.850 USD/tháng cho digital, tỷ lệ chốt lead mua 2% đến 5%.
- Trang Ylopo được gán (`ylopo.com/blog/how-much-do-real-estate-leads-cost`), mở ngày 12/10/2026, là bài đăng 18/12/2024 và ghi CPL trung bình 66,69 USD, Facebook 5 đến 30 USD, Google 50 đến 150 USD, không có các số 503/448/480/416/2.850.
- Con số 8.010 USD trùng đúng với chi phí kinh doanh trung vị toàn bộ của NAR Member Profile 2025 (8.010 USD, không phải riêng marketing), nên có khả năng đã bị gán nhầm nguồn.
- Chưa sửa #1415 vì chưa hỏi user. Đề xuất: viết lại các con số theo trang Ylopo thật hoặc gỡ phần số liệu, và kiểm tra các bài khác từng trích "503 USD". #1825 chỉ link tới #1415 với anchor "average cost per lead for agents" và không lặp các con số.

### Cụm 9 wave 1: `social media for realtors` (#1865)

- Lên lịch #1865 `/social-media-for-realtors/` ngày **14/10/2026 10:00**. 1.680 chữ, density 0,60%, 13 H2, 3 bảng, 4 ảnh AI. Link tới #1859 (scheduled 13/10 14:00, sớm hơn) hợp lệ khi bài này lên.
- Nguồn ngoài: FTC Endorsement Guides Q&A (đã mở trang: tiết lộ liên hệ vật chất, và lời chứng thực khách hàng nếu khách được báo trước có thể được trả/đăng) và 24 CFR 100.75. Không dùng số liệu người dùng nền tảng vì không có nguồn xác minh; bảng nền tảng chỉ mô tả mục đích. Không tìm được văn bản Article 12 Code of Ethics trên trang NAR nên không trích.

### Cụm 9 wave 1: `real estate seo` (#1871)

- Lên lịch #1871 `/real-estate-seo/` ngày **14/10/2026 14:00**. 1.790 chữ, density 0,62%, 13 H2, 4 bảng, 4 ảnh AI. Link tới #1859 (13/10 14:00) và #1865 (14/10 10:00) đều sớm hơn bài này.
- Nguồn ngoài đã mở trang gốc: Google Business Profile help "Improve your local ranking" (relevance, distance, prominence; không thể trả tiền để lên hạng) và SEO Starter Guide của Google Search Central (tiêu đề duy nhất, thay đổi cần thời gian). Không đưa số liệu xếp hạng hay traffic của site này vì không có quyền GSC.
- Lần soạn đầu quên link lên pillar (gate `no pillar link` bắt được), đã thêm câu link về #1825 trước khi tạo bài.

### Cụm 9 wave 1: `postcards real estate` (#1877)

- Lên lịch #1877 `/real-estate-postcards/` ngày **15/10/2026 10:00**. 1.854 chữ, density 0,54% (keyword `postcards real estate` là cụm khó viết tự nhiên nên dùng dạng "postcards real estate agents send/mail"), 13 H2, 3 bảng, 4 ảnh AI.
- Số liệu USPS đã mở trang gốc: EDDM không cần tên/địa chỉ (gửi "Postal Customer"), tối thiểu 200 và tối đa 5.000 mảnh/ngày/ZIP, cước retail flats 0,26 USD/mảnh (trang nói giá có thể đổi); DMM 101 mục 6.2.2 giới hạn kích thước postcard First-Class (3,5 x 5 inch tối thiểu, 4,25 x 6 inch tối đa, dày 0,007 đến 0,016 inch, nặng tối đa 3,5 oz). Ví dụ chi phí 400 nhà/tháng là minh họa với giá in giả định 0,30 USD/thẻ.
- Lần soạn đầu thiếu placeholder `{{STATS}}` (gate ảnh chỉ kiểm datum, không kiểm placeholder; `finalize` bắt được), đã thêm.

### Cụm 9 wave 1: `real estate agent business card` (#1883)

- Lên lịch #1883 `/real-estate-agent-business-card/` ngày **15/10/2026 14:00** (slot 2 của ngày; 15/10 = #1877 10:00 + #1883 14:00 + news 18:xx). 1.814 chữ, density 0,72%, 14 H2, 3 bảng, 4 ảnh AI. Cluster branding nên lên hub #1832, không link pillar #1825.
- Nguồn ngoài đã mở: trang NAR về dùng dấu REALTOR® với tên công ty (thẻ hội viên dùng được; không đưa vào tên công ty; người có license không phải hội viên không dùng logo trên thẻ). Không bịa giá in; kích thước 3,5 x 2 inch là chuẩn phổ biến, bài nói rõ giá tùy nhà in. SEO title lần đầu 62 ký tự và description 160, đã rút xuống trước khi tạo bài.
- Link tới #1853 (publish 13/10) và #1843 (đã live) đều hợp lệ khi bài lên.

### Cụm 9 wave 1: `real estate agent logo` (#1889)

- Lên lịch #1889 `/real-estate-agent-logo/` ngày **16/10/2026 10:00**. 1.824 chữ, density 0,55%, 13 H2, 3 bảng, 4 ảnh AI. Link tới #1883 (15/10 14:00) sớm hơn nên hợp lệ khi bài này lên.
- Nguồn ngoài đã mở: USPTO "What is a trademark" (logo là nhãn hiệu, đăng ký không bắt buộc nhưng bảo hộ rộng hơn, quyền chưa đăng ký giới hạn trong khu vực kinh doanh; trang không nói về việc tra cứu nên bài chỉ khuyên tra cứu như lời khuyên chứ không gán cho USPTO) và NAR logo use with firm name. Bài không nêu giá, không nêu số liệu thị trường logo.
- Lần đầu ảnh STATS (5 loại logo) đặt nhầm dưới mục "Overused", đã chuyển lên sau bảng 5 loại trước khi tạo bài.

### Cụm 9 wave 1: `real estate agent bio` (#1895)

- Lên lịch #1895 `/real-estate-agent-bio/` ngày **16/10/2026 14:00**. 1.692 chữ, density 0,65%, 11 H2, 3 bảng, 6 ví dụ bio (tên và chi tiết hoàn toàn hư cấu, ghi rõ trong bài), 4 ảnh AI. Link tới #1883 và #1889 đều lên trước bài này.
- Nguồn ngoài đã mở: FTC "Advertising FAQs: A Guide for Small Business" (quảng cáo phải trung thực, có bằng chứng trước khi chạy) và 24 CFR 100.75. Bài không đưa số liệu thật nào về agent; các con số trong ví dụ và bảng là minh họa, có ghi chú.
- Đã sửa trong ví dụ "Relocation specialist" cụm "helps families" thành "helps people" để khỏi mô tả khách theo tình trạng gia đình, nhất quán với cảnh báo fair housing trong bài (bản sửa này đã có trong bản đăng).

### Cụm 9 wave 1: `real estate marketing software` (#1901)

- Lên lịch #1901 `/real-estate-marketing-software/` ngày **17/10/2026 10:00**. 1.729 chữ, density 0,69%, 12 H2, 3 bảng, 4 ảnh AI.
- **Khác plan:** tiêu đề đổi từ "Best Real Estate Marketing Software in 2026" sang "Real Estate Marketing Software: What to Use for Each Job in 2026" vì bài không xếp hạng vendor (giá và tính năng đổi liên tục, không có nguồn độc lập để xếp hạng). Bài là hướng dẫn chọn công cụ theo công việc, kèm bảng, stack miễn phí, câu hỏi trước khi mua.
- Chỉ nêu sự kiện đã xác minh: Mailchimp (trang pricing: gói free dưới 250 contact, tối đa 500 email/tháng, không có scheduling và branded template), Buffer (free: 3 tài khoản, 10 bài lên lịch mỗi tài khoản), FTC CAN-SPAM guide (opt-out trong 10 ngày làm việc, không thể giao khoán trách nhiệm). Follow Up Boss, Lofty, Rechat chỉ mô tả theo nội dung các bài đã có trên site (#1746, #1329, #1026). Canva trả 403 khi mở trang pricing nên bài không nêu gói hay giá của Canva, chỉ nói "design tool with templates".
- Có 2 link cross-pillar (#450 Cụm 2 và #1225 Cụm 7) vì plan Cụm 9 yêu cầu bài này link #1225 và #263, trái với quy tắc thông thường tối đa 1; đã ghi nhận là ngoại lệ có chủ đích.

### Đã xử lý: số liệu của #1415 (12/10/2026)

- Viết lại toàn bộ #1415 theo số liệu thật của trang Ylopo (bài đăng 18/12/2024, tác giả Aaron Franklin, Ylopo): CPL trung bình 66,69 USD; Facebook/Instagram khoảng 5 đến 30 USD; Google Ads khoảng 50 đến 150 USD; Zillow Premier Agent khoảng 20 đến 150 USD trở lên, có thể vượt 1.000 USD ở zip code cạnh tranh nhất; remarketing database khoảng 2 đến 3 USD; referral network 25 đến 40% hoa hồng khi chốt; gợi ý tối thiểu khoảng 1.500 USD/tháng; team top chi 8.000 USD+/tháng; 46% agent chi 0 đến 250 USD/tháng. Bài ghi rõ đây là số của một vendor bán dịch vụ lead gen và trang gốc tự mâu thuẫn ở vài chỗ (khoảng giá buyer lead khác nhau giữa các mục).
- Đã gỡ: CPL 503/448 USD, paid 480/organic 416, 8.010 USD/năm, 2.850 USD/tháng, "tỷ lệ chốt lead mua 2 đến 5%" và câu "phản hồi trong 5 phút chuyển đổi cao hơn hẳn" (đều không có nguồn). Tiêu đề đổi từ "...Just Hit $503" sang "Cost Per Lead for Real Estate Agents: What Leads Really Cost"; SEO title, meta description và og:title đều đã đổi, trang live không còn "$503". Slug, category 85, featured image, tags, ngày đăng và 2 link Related Reading giữ nguyên; alt ảnh thứ hai đã bỏ "503 dollars".
- Ví dụ cost per closing (25 lead x 60 USD, 2% so với 4%) là minh họa có nêu giả định, trùng với bài #1859.
- Đã quét 150 bài live ngày 12/10: chỉ #1415 chứa 503/8.010/2.850 do nguồn Ylopo. Con số 8.010 USD hợp lệ ở #1843 vì đó là chi phí kinh doanh trung vị của NAR Member Profile 2025, không phải chi phí marketing.
- Chưa cập nhật: dòng tracker Google Sheet của #1415 (không truy cập được), tiêu đề cũ vẫn có thể còn ở đó.

## 2026-10-12: duyệt wave 2 Cụm 9 và đặt chỗ 8 keyword

- 8 keyword wave 2 đã ghi vào `used-keywords.md` (bảng reserved) và `content-plan.md`: `google ads for realtors`, `google business profile for realtors`, `flyer for real estate`, `listing presentation`, `closing gifts real estate`, `real estate testimonials`, `realtor name ideas`, `real estate agent referral`. Không keyword nào trùng bảng published hay plan hiện có.
- Ranh giới cần giữ khi viết: Google Ads không viết lại tổng quan (#1859) và không viết Facebook (#1229); Google Business Profile đào sâu hơn checklist trong #1871; flyer khác postcard (#1877); testimonials, name ideas lên hub #1832.
- `real estate agent referral`: kiểm SERP 12/10, kết quả lẫn hai ý định (phí giới thiệu giữa các agent và cách nhận thêm giới thiệu). Quyết định viết cả hai và đặt tiêu đề phản ánh điều đó. Mức phần trăm phí referral chỉ nêu khi mở được nguồn gốc.
- Chưa viết bài nào của wave 2.

## 2026-10-12: tạm dừng routine news và xếp lại lịch 3 bài/ngày

- Theo yêu cầu của user, **tạm dừng routine "Daily news-to-cluster-article"** (trigger `trig_011KKDV99Pa12bj8TJssRo9x`, `enabled=false`) để chừa slot cho đợt nội dung Cụm 9. **Phải bật lại khi muốn có bài tin hàng ngày.**
- Xếp lại 7 bài đang `future` để đủ trần 3 bài/ngày (10:00, 14:00, 18:00 giờ site = UTC), thứ tự giữ nguyên để link giữa các cluster luôn trỏ tới bài lên trước:
  - 13/10: #1853 ideas (10:00), #1859 advertising (14:00), #1865 social (18:00)
  - 14/10: #1871 seo (10:00), #1877 postcards (14:00), #1883 business card (18:00)
  - 15/10: #1889 logo (10:00), #1895 bio (14:00), #1901 software (18:00)
- Ngày 12/10 đã đủ 3 bài (#1825, #1832, #1843). Bài mới 16/10 trở đi (wave 2) có thể xếp 3 bài/ngày.
- Chưa xác minh được nội dung 7 bài vừa đổi ngày còn nguyên vì bài `future` không đọc được qua REST công khai; sẽ kiểm khi chúng lên.
- Các lịch nhắc kiểm tra đã dời: 13/10 19:00, 14/10 19:00, 15/10 19:30 UTC (bước inbound link pillar/hub làm ở lần cuối).


## 2026-10-13: Cụm 9 wave 2 viết xong và lên lịch (8 bài)

- Lịch (giờ site = UTC, tối đa 3 bài/ngày, routine news vẫn đang tạm dừng): 16/10 10:00 #1937 Google Business Profile, 14:00 #1943 Google Ads, 18:00 #1949 testimonials; 17/10 10:00 #1955 listing presentation, 14:00 #1961 referral, 18:00 #1967 flyer; 18/10 10:00 #1977 closing gifts, 14:00 #1979 realtor name ideas. Tổng hợp theo thứ tự này để link giữa các bài chỉ trỏ tới bài lên trước.
- Cả 8 bài đạt gate: check_seo (density >= 0,5%, >= 1 link ngoài, >= 2 link nội bộ, kw trong H2 và alt, link pillar hoặc hub), không anchor nội bộ dài hơn 8 từ, SEO title <= 60, description <= 155, không dấu gạch dài, kiểm HTTP 200 mọi link nội bộ không phải bài đã lên lịch, mỗi ảnh được xem trực tiếp. Hai ảnh cmp sinh lại vì nhãn bị in hai lần, một ảnh hero sinh lại vì cắt mất mặt.
- Quy tắc link: mỗi bài 1 link lên pillar #1825 (marketing) hoặc hub #1832 (testimonials, name ideas), tối đa 1 link ra pillar cụm khác (#1223 ở Google Ads, #918 ở flyer, crm-marketing-real-estate ở referral và closing gifts).
- **Chưa làm (đã hẹn qua trigger):** inbound cho 8 bài mới (pillar #1825 Related Reading thêm đủ wave 2, hub #1832 Related Reading cho testimonials và name ideas, và ít nhất 1 bài donor cùng cụm cho mỗi bài), vì không được link tới bài chưa lên.

### Cụm 9 wave 2: `google business profile for realtors` (#1937)

- Lên lịch #1937 `/google-business-profile-for-realtors/` ngày **16/10/2026 10:00**. 1.487 chữ, density 0,67%.
- Chỉ nêu điều đã xác minh từ Google Business Profile Help: agent là practitioner được liệt kê tên, 1 profile mỗi practitioner, staff không có profile riêng, virtual office không đủ điều kiện, service-area business ẩn địa chỉ, tên không được thêm tagline hoặc mô tả dịch vụ (có thể bị suspend), xác minh khiến profile dễ hiện hơn. Review: chính sách Maps coi review có ưu đãi (tiền, giảm giá, hàng/dịch vụ miễn phí) là incentivized và không cho phép; FTC rule review hiệu lực 21/10/2024. Không nêu loại category cụ thể của Google vì chưa xác minh danh sách hiện tại.

### Cụm 9 wave 2: `google ads for realtors` (#1943)

- Lên lịch #1943 `/google-ads-for-realtors/` ngày **16/10/2026 14:00**. 1.272 chữ, density 0,79%.
- Quy tắc nhà ở của Google Ads (US/Canada) lấy từ trang Housing in personalized advertising: không nhắm theo giới tính, tuổi, tình trạng cha mẹ, hôn nhân, ZIP code; cho phép bán kính tối thiểu 1 km và thành phố; chính sách xét cả landing page; trang không nêu tên agent nên bài viết "nên coi là bị áp dụng". Giá lead $50-150 chỉ dẫn từ Ylopo (đã gắn nhãn quan điểm một vendor). Không nêu CPC cụ thể.

### Cụm 9 wave 2: `real estate testimonials` (#1949)

- Lên lịch #1949 `/real-estate-testimonials/` ngày **16/10/2026 18:00**. 1.377 chữ, density 0,80%.
- FTC rule hiệu lực 21/10/2024: cấm testimonial giả, mua review gắn cảm xúc, insider review không công khai, ngăn review bằng đe dọa hoặc cáo buộc sai; Q&A của FTC nói testimonial doanh nghiệp tự đăng trên website của mình cũng bị điều chỉnh. Không nêu mức phạt vì trang FTC không ghi số. NAR (qua Virginia REALTORS): 66% seller tìm agent qua referral hoặc agent cũ, 35% nói danh tiếng là yếu tố quyết định. Ví dụ testimonial trong bài là bịa và đã ghi rõ.

### Cụm 9 wave 2: `listing presentation` (#1955)

- Lên lịch #1955 `/listing-presentation/` ngày **17/10/2026 10:00**. 1.413 chữ, density 0,78%.
- NAR settlement FAQs (trang chỉ hiện câu hỏi, không hiện câu trả lời đầy đủ): có hiệu lực 17/08/2024; cấm đăng offer of compensation trên MLS; buyer cần thỏa thuận bằng văn bản trước khi xem nhà; có disclosure "not set by law and is fully negotiable". Bài chỉ nêu những điểm này và dặn tuân theo chính sách brokerage và luật bang. Số liệu seller từ NAR qua Virginia REALTORS: ưu tiên marketing, định giá cạnh tranh, bán trong khung thời gian; 35% nhắc danh tiếng; 66% qua referral hoặc agent cũ.

### Cụm 9 wave 2: `real estate agent referral` (#1961)

- Lên lịch #1961 `/real-estate-agent-referral/` ngày **17/10/2026 14:00**. 1.289 chữ, density 0,78%.
- Xác minh SERP 12/10 là lẫn hai ý (cách nhận referral và referral fee), bài viết cả hai. 12 CFR 1024.14: cấm đưa hoặc nhận fee/kickback/thing of value cho referral settlement-service; ngoại lệ cho cooperative brokerage và referral giữa agent và broker, chỉ khi mọi bên là real estate broker, không áp dụng với mortgage broker. 25-40% hoa hồng chỉ dẫn từ Ylopo và ghi rõ không phải quy tắc agent-to-agent. NAR: 43% buyer qua referral, 18% agent cũ, hơn 9/10 buyer dùng lại agent.

### Cụm 9 wave 2: `flyer for real estate` (#1967)

- Lên lịch #1967 `/flyer-for-real-estate/` ngày **17/10/2026 18:00**. 1.233 chữ, density 0,65%.
- USPS: không đặt matter không dán tem vào, gắn lên, hay treo vào mail receptacle (DMM, FAQ của USPS về flyer trả lời không); bài khuyên tuân theo và kiểm tra luật địa phương về phát tận nhà. Không nêu số liệu hiệu quả của flyer vì không có nguồn độc lập.

### Cụm 9 wave 2: `closing gifts real estate` (#1977)

- Lên lịch #1977 `/closing-gifts-real-estate/` ngày **18/10/2026 10:00**. 1.310 chữ, density 0,69%.
- IRS Publication 463: khấu trừ tối đa $25 cho mỗi người mỗi năm thuế với quà kinh doanh; chi phí phụ như gói quà, khắc chữ, vận chuyển thường không tính nếu không làm tăng đáng kể giá trị; cần lưu chi phí, ngày, mô tả. Edition 2025 là bản mới nhất tìm được. RESPA: không hứa quà để đổi lấy referral; bài dặn hỏi broker.

### Cụm 9 wave 2: `realtor name ideas` (#1979)

- Lên lịch #1979 `/realtor-name-ideas/` ngày **18/10/2026 14:00**. 1.346 chữ, density 0,67%.
- NAR: REALTOR® không được là một phần của tên firm. SBA: hầu hết bang không cho đăng ký tên đã có người đăng ký; nên kiểm tra USPTO; đăng ký DBA khi dùng tên khác; domain không cần khớp tên. Tên ví dụ là bịa và đã ghi rõ. Không nêu quy tắc cụ thể từng bang (không xác minh), chỉ dặn hỏi broker và state commission.

## 2026-10-13: Cụm 9, nâng ảnh minh họa thực tế cho 7 bài (mockup HTML)

- Lý do: ảnh cũ của Cụm 9 là 1 ảnh hero + 3 infographic icon chung chung, không cho thấy đối tượng bài nói tới (tờ flyer, hồ sơ Google, slide). Tiêu đề hứa "examples, templates" nhưng không có ví dụ nào. Kiểm 12 bài top SERP (`references/serp-image-audit-wave3.md`) và bài Salesforce cho thấy ảnh ví dụ thật là hướng tốt hơn ảnh stock.
- Cách làm: dựng 21 mockup 1600x900 bằng HTML + Playwright, chữ chính xác, nội dung hư cấu và ghi chú trên ảnh. Mã nguồn, ảnh và quy tắc chèn nằm ở `references/files/mockups-cum9/`.
- Đã áp dụng ngày 13/10: #1949 testimonials (cards, ask, site), #1955 listing presentation (pricing slide, marketing plan slide, 12-slide outline), #1967 flyers (4 layouts, anatomy, crowded vs clean). Bỏ 2 ảnh cũ mỗi bài (loại 3 icon và A vs B), giữ hero và ảnh featured. Chữ và link không đổi, status vẫn `future` đúng giờ.
- Chờ publish rồi chèn (bài future không đọc được nội dung qua REST): #1877 postcards, #1883 business cards (trigger 14/10 19:30 UTC), #1889 logos, #1895 bio (trigger 15/10 15:30 UTC).
- Còn lại, ưu tiên trung bình: #1937 Google Business Profile, #1843 Marketing Plan (chụp template xlsx thật), #1871 SEO, #1979 Name Ideas, #1865 Social, #1859 Advertising.

## 2026-10-13: Cụm 9, mockup nhóm ưu tiên trung bình (18 ảnh, 6 bài)

- Dựng 18 mockup mới (GBP, marketing plan, SEO, name ideas, social, ads) bằng skill `mockup-images`; `plan_template` dựng lại từ dữ liệu file xlsx thật.
- Đã cập nhật: #1937 (future), #1979 (future), #1843 (đã live, lấy bản live làm gốc, kiểm chữ và link không đổi, 5 figure, ảnh 200).
- Chờ publish rồi chèn: #1859, #1865 (trigger 13/10 19:45 UTC), #1871 (trigger 14/10 11:00 UTC).
- Phát hiện: bản local `plan_content.html` của #1843 đã lệch bản live (live có thêm link tải xlsx), xác nhận lại quy tắc luôn lấy nội dung live làm gốc.

## 2026-10-13: Cụm 9, mockup nhóm ưu tiên thấp (20 ảnh, 7 bài)

- Dựng 20 mockup (pillar, brand, ideas, referral, gift, google ads, software) bằng skill `mockup-images`.
- Đã cập nhật: #1825 pillar (live, +3 ảnh, giữ ảnh COMPARISON vì bài viện dẫn "image above"), #1832 hub (live, +3), #1961, #1977, #1943 (wave 2 future). Kiểm bản live: chữ và link không đổi, ảnh trả 200.
- Chờ publish: #1853 (trigger 13/10 10:30 UTC), #1901 (trigger 15/10 18:30 UTC).
- Bài học: luôn grep câu viện dẫn ảnh ("image above") trước khi xóa ảnh cũ.

- 2026-10-13 — #1843, #1832: thay 6 ảnh mockup thế hệ 1 bằng bản mobile-first (canvas 1000px, chữ ≥12px trên điện thoại). Chữ và link không đổi.

- 2026-10-13 — Skill `mockup-images` cập nhật theo bản mobile-first đã duyệt: canvas 1000px mặc định, công thức dựng cảnh, `apply_mockups.py --mobile`, caption trong spec, catalog 6 cảnh `_m`, spec-example có `mobile_round`.

- 2026-10-13 — Làm lại toàn bộ ảnh mockup Cụm 9 theo mobile-first (59 ảnh, media 2051–2111). Đã thay ảnh gen-1 ở #1825, #1853, #1937, #1943, #1949, #1955, #1961, #1967, #1977, #1979, #1843, #1832; 8 bài còn lại (#1859 #1865 #1871 #1877 #1883 #1889 #1895 #1901) sẽ nhận ảnh `_m` khi publish qua trigger. Chữ và link không đổi (đã kiểm với bài live #1825, #1853).

- 2026-10-13 — #1859, #1865: chèn 3 ảnh mockup mobile-first mỗi bài (đã publish 14:00 và 18:00 UTC), thay 3 ảnh icon cũ; chữ và link không đổi.

- 2026-10-14 — Image refresh theo rule mobile-first cho 6 bài có traffic SEO: #981 best-real-estate-website-design, #1011 luxury-real-estate-website-design, #207 best-crm-for-real-estate, #546 real-estate-website-builder, #610 idx-website-for-realtors, #616 idx-real-estate-websites-examples. Thay 10 infographic Gemini chữ nhỏ (có số bịa, rating, dấu tích, tên hãng) bằng mockup theo tiêu chí lấy từ chính bài, không số liệu mới. Chữ và link không đổi. Chưa đổi: #1056 (ảnh chụp màn hình hãng, user bảo giữ). Số liệu GSC trước khi sửa: #981 27 click/641 impr/vị trí 11,2; #1056 5/1.845/15,8; #207 2/712/10,5; #610 1/1.139/36,1; #546 1/613/8,0; #1011 4/175/7,1; #616 2/411/42,7.

- 2026-10-14 — Rút alt ảnh mockup về ≤ 110 ký tự trong 20 bài (#1825, #1832, #1843, #1853, #1859, #1865, #981, #1011, #207, #546, #610, #616 và 8 bài wave 2 đang lên lịch). Chữ và link không đổi; alt thư viện media chưa đổi (không có công cụ).

- 2026-10-14 — Chèn ảnh mockup mobile-first vào #1871 real-estate-seo ngay sau khi publish (seo_results_m, seo_profile_m thay ảnh gen-1, seo_plan_m). 4 figure thành 5; chữ và link không đổi (đã verify bằng REST), 5 ảnh trả 200.

- 2026-10-14 — Verify 3 bài Cụm 9 wave 1 đã publish đúng giờ: #1871 (10:00), #1877 (14:00), #1883 (18:00). Status publish, category 392, featured set, URL 200, đúng 3 bài trong ngày 14/10. Chữ live khớp file local sau khi bỏ figure; link nội bộ và ngoài đều 200 (support.google.com chỉ 404 với HEAD, GET 200). #1871 đã có mockup mobile-first; #1877 và #1883 chờ trigger chèn ảnh.

- 2026-10-14 — Chèn ảnh mockup mobile-first vào #1877 real-estate-postcards và #1883 real-estate-agent-business-card ngay sau khi publish. Cả hai 4 figure thành 5; chữ và link không đổi (verify bằng REST), ảnh trả 200.

- 2026-10-15 — Chèn ảnh mockup mobile-first vào #1889 real-estate-agent-logo và #1895 real-estate-agent-bio ngay sau khi publish. Cả hai 4 figure thành 5; chữ và link không đổi (verify bằng REST), ảnh trả 200.

- 2026-10-15 — Chèn ảnh mockup mobile-first vào #1901 real-estate-marketing-software ngay sau khi publish. 4 figure thành 5; chữ và link không đổi (verify bằng REST), ảnh trả 200. Hoàn tất toàn bộ wave 1 Cụm 9.

- 2026-10-26 — Cụm 10 inbound pass wave 1 (8 bài live: #2260 pillar, #2262 hub, 6 cluster 24–25/10). Verify 8 bài: publish, ảnh 200, link nội bộ 200, không em dash. Thêm link vào: pillar #2260 (+6 bullet Related Reading), hub #2262 (+2 link trong bài, +3 bullet), #2302 → circle-prospecting; donor mới: #2207 và #2195 → expired-listings, #2165 và #2201 → circle-prospecting, #1961 → sphere-of-influence-real-estate, #1415 → companies + pillar, #1225 → companies, #1272 và #1317 → buyer-leads, #1825 (pillar marketing) → pillar lead gen (1 câu + 1 bullet). Anchor 3–8 từ, đa dạng. Verify bằng REST: chỉ thêm, số ảnh không đổi (#1825 diff chỉ 2 dòng thêm). Chưa làm (tùy chọn): #1223 → free-real-estate-leads. Wave 2 (bài 9–13) hẹn 28/10.

- 2026-10-26 — Cụm 12: thêm 1 link tới pillar #2330 `sphere-of-influence-real-estate` vào 6 bài cũ: #1825 ("working your sphere of influence"), #1853 ("a sphere of influence plan for agents"), #1977 ("how to build a sphere list"), #1949 ("keeping your sphere in touch"), #1223 ("working past clients and your sphere"), #263 ("building a sphere of influence list"). Verify bằng REST: chỉ thêm 1 câu, số ảnh không đổi (6, 4, 5, 5, 5, 4), không em dash mới, anchor ≤8 từ, publish. #263 vốn có em dash trong nội dung cũ, không sửa.
