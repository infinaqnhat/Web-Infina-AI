# infina.ai/news: bảng mảng nội dung, mỗi URL một dòng

Crawl 2026-10-23 qua WP REST API (bản đầu 2026-10-09, làm mới hoàn toàn lần này). **178 bài publish, 166 bài thật** (12 stub 301
tách riêng ở cuối file). Không có bài draft/scheduled/pending nào tại thời điểm crawl: cả 28 bài Cụm 9 đã đăng.
Cụm 10 (lead generation) mới ở mức **đã duyệt, chưa viết**, xem mục riêng sau Cụm 9; không nằm trong số 178 bài.

Cùng format với `teardown-followupboss-table.md` để đặt cạnh nhau mà so. Kết luận chiến lược của
đối thủ ở `teardown-followupboss.md`, phương pháp ở `competitor-pillar-teardown.md`. File này là dữ
liệu thô của **site mình**, dạng bảng để tự soi.

## Đọc bảng này thế nào

| Cột | Nghĩa |
|---|---|
| Vai trò | Lấy nguyên nhãn trong `content-plan.md`. `PILLAR` in đậm. Bài không có trong plan để trống thành `cluster` |
| URL | `#ID` là post ID trong WordPress, dùng thẳng được với `update_post` |
| IN | Số **bài thật khác** trỏ vào (không tính 12 stub 301 là bài nguồn), đếm trong thân bài. Link đi qua stub 301 đã quy về đích thật và ghi rõ `(n qua stub)` |
| Chữ | Đếm sau khi bóc hết thẻ HTML khỏi `content.rendered`. Xấp xỉ |
| Sửa lần cuối | Trường `modified` của REST API |
| FOCUS_KW đã log | Lấy từ `references/used-keywords.md`, **không phải** đọc từ Rank Math. ⚠️ nghĩa là dòng đó trong log ghi nguồn là "suy đoán từ slug" chứ không phải tracker |
| Pillar bài trỏ lên | ✅ = có trỏ lên pillar của chính cụm mình. ↗ = chỉ trỏ lên pillar của cụm khác. ❌ = không trỏ lên pillar nào |
| Post title | H1 thật của bài |

## Tám điều phải biết trước khi dùng số trong bảng

**1. Cụm ở đây là dữ liệu thật, không phải suy đoán.** Khác hẳn bảng FUB. Với FUB mình phải suy
thành viên cụm từ link graph vì không có file plan nào. Với site mình thì `content-plan.md` là nguồn
đúng, nên cột Vai trò và việc một bài thuộc cụm nào đều đọc thẳng từ bảng trong file đó. Chỗ nào
phải suy thì có ghi rõ ở điều 2 và 3.

**2. 51 bài không nằm trong bảng cụm nào của plan.** Đây không phải lỗi crawl. `content-plan.md` tự
khai ngay dòng đầu là nó chỉ bao bài evergreen và **loại bài News ra khỏi phạm vi** (từ Cụm 9 trở đi plan có ghi cả bài tin hỗ trợ vào bảng cụm, nên con số này giảm so với lần crawl 09/10). Nên 40 bài
News real estate và 11 bài AI/tech nằm ngoài 9 cụm là đúng thiết kế của plan, không phải thiếu sót
khi dựng bảng này. Cái đáng chú ý là hệ quả của nó, xem điều 6.

**3. Hai chỗ plan ghi trong prose nhưng quên ghi vào bảng.** `#247 crm-for-real-estate-agents` được
plan ghi rõ ở phần vá mồ côi là "bài cluster thật chứ không phải News", thuộc Cụm 2, nhưng **không
có dòng nào trong bảng Cụm 2**. Mình đã xếp nó vào Cụm 2 theo prose và đánh dấu Vai trò là
`cluster (thiếu ở bảng plan)`. Tương tự `#1529` được mô tả trong phần prose của Cụm 1 nhưng pillar
mà nó khai lại là `#214` của Cụm 2, nên mình để nó ở nhóm News chưa gắn cụm thay vì tự chọn hộ.

**4. `#223` nằm ở hai cụm và đó là chủ ý của plan.** Bảng Cụm 2 ghi vai trò nó là
"Cross-link → Cụm 7", bảng Cụm 7 ghi nó là bài giải thích pain-point. Mình xếp nó về Cụm 7 và giữ
nguyên ghi chú cross-link. Site mình là lưới chứ không phải cây, nên sẽ còn gặp kiểu này.

**5. Cột FOCUS_KW không phải đọc từ Rank Math.** WP REST **không phơi** focus keyword của Rank Math
ra ngoài, kiểm tra rồi: trường `meta` chỉ có `{"footnotes": ""}`. Nên cột này lấy từ
`used-keywords.md`, tức là một file ghi tay. Hệ quả: **146/166 bài có keyword log, 20 bài không có**,
và trong 146 bài đó **13 bài ghi nguồn là "suy đoán từ slug"** chứ không phải lấy từ tracker. Dùng
cột này để khoanh vùng chủ đề, đừng dùng làm bằng chứng về cái gì đang set thật trong Rank Math.

**6. Cột IN của site mình sạch hơn cột IN của FUB, vì lý do kỹ thuật.** Với FUB mình phải trừ tay 3
link template. Ở đây `content.rendered` chỉ trả về thân bài, menu và footer của theme không lọt vào,
nên không có gì phải trừ. Đổi lại con số sẽ **thấp hơn** số link thật mà người đọc nhìn thấy trên
trang, vì thiếu phần điều hướng của theme.

**7. Số chữ lệch 1-3% so với vài con số đã ghi trong `content-plan.md`.** Ví dụ `#1529` ở đây là
1.032 còn plan ghi 1.019. `#89` ở đây 3.932 còn plan ghi 3.991. Nguyên nhân là cách bóc thẻ khác
nhau, chỗ thì tính chữ trong bảng và caption, chỗ thì không. Dùng để so tương đối giữa các bài trong
chính file này thì được, đừng dùng để cãi nhau với số trong file khác.

**8. Dash trong cột Post title là chữ của bài, giữ nguyên.** Có đúng 1 bài còn em dash trong tiêu đề
là `#299`. Quy tắc không dùng dash áp cho bài mình viết mới, không áp cho việc trích lại tiêu đề đang
có. Dòng này là để biết mà đi sửa, không phải để sửa trong bảng.

## Tóm tắt 11 nhóm (cộng Cụm 10 đã duyệt, chưa viết)

| Cụm | Trang | Pillar | Tổng chữ | Mồ côi | Không trỏ pillar nào | Thiếu FOCUS_KW |
|---|---|---|---|---|---|---|
| Cụm 1: Chatbot / Conversational AI | 13 | `best-conversational-ai-chatbot-for-real-estate` (9 IN, 3,038 chữ); `best-chatbot-customer-service-real-estate` (26 IN, 3,932 chữ) | 21,263 | 0 | 0 | 0 |
| Cụm 2: CRM Software | 27 | `best-crm-for-real-estate` (49 IN, 4,354 chữ); `ai-intent-layer-for-real-estate-crm` (13 IN, 772 chữ) | 34,498 | 0 | 0 | 4 |
| Cụm 3: Website Builder / IDX | 14 | `real-estate-website-builder` (22 IN, 3,037 chữ) | 16,643 | 0 | 0 | 1 |
| Cụm 4: AI Voice / Virtual Assistant / Receptionist | 6 | `best-ai-voice-assistants-for-real-estate` (11 IN, 2,287 chữ) | 7,320 | 0 | 0 | 0 |
| Cụm 5: Website / Web Design | 6 | `website-design-for-real-estate-agents` (10 IN, 1,805 chữ) | 6,777 | 0 | 0 | 0 |
| Cụm 6: Landing Pages | 6 | `real-estate-landing-page-guide` (7 IN, 1,897 chữ) | 8,316 | 0 | 0 | 0 |
| Cụm 7: Lead Generation / Follow-up Automation | 9 | `real-estate-lead-follow-up-automation-guide` (20 IN, 2,483 chữ) | 8,338 | 0 | 0 | 2 |
| Cụm 8: Compliance / Legal / Risk | 6 | `tcpa-compliance-for-real-estate-agents` (22 IN, 1,909 chữ) | 6,005 | 0 | 0 | 1 |
| Cụm 9: Marketing và Branding | 28 | `real-estate-marketing` (22 IN, 2,624 chữ); `real-estate-branding` (12 IN, 1,829 chữ) | 44,661 | 0 | 0 | 0 |
| Cụm 10: Lead Generation, nguồn lead (đã duyệt, chưa viết) | 0 live / 13 dự kiến | `real estate lead generation` và `listing leads` (dự kiến, chưa có URL) | n/a | n/a | n/a | n/a |
| Bài News real estate chưa gắn cụm trong plan | 40 | không có | 29,506 | 0 | 18 | 12 |
| Ngoài chủ đề real estate (AI/tech) | 11 | không có | 2,784 | 11 | 11 | 0 |

**Ba thứ đáng nhìn nhất trong bảng tóm tắt này.**

**Cột "Không trỏ pillar nào" vẫn là cột đau nhất.** 9 cụm trong plan đều sạch: 0 bài nào không trỏ lên
pillar. Nhưng nhóm News có **18 trong 40 bài không trỏ lên bất kỳ pillar nào** (lần crawl 09/10 là 19/40), và
nhóm AI/tech thì cả 11 bài đều vậy. Nghĩa là việc sửa link nội bộ từ trước tới giờ mới chỉ chạm tới phần nằm
trong plan, còn khoảng 2/5 số bài News thì chưa.

**Cột "Mồ côi" vẫn chỉ còn đúng 11 bài AI/tech, và nhóm này đã được quyết định để nguyên (Đợt E, 12/10), nên không tính là việc tồn đọng.** Toàn bộ 9 cụm
và cả 40 bài News đều có ít nhất 1 link vào, gồm cả 28 bài Cụm 9 mới đăng 12–21/10. 11 bài còn lại không sửa được bằng link vì chúng không
thuộc chủ đề nào của site.

**Pillar nhẹ `ai-intent-layer-for-real-estate-crm` vẫn gánh 13 link vào với 772 chữ.** Nó có 7 thẻ
H2 trên 10 đoạn văn, tức là gần như mỗi H2 chỉ có 1 đoạn. Đây vẫn là pillar mỏng nhất site, và nó đang
nhận nhiều link hơn 5 trong 11 pillar còn lại. So để thấy: pillar Cụm 2 chính có 49 link vào và
4,354 chữ.

---

## Cụm 1: Chatbot / Conversational AI  (13 trang, 21,263 chữ)

| Vai trò | URL | IN | Chữ | Sửa lần cuối | FOCUS_KW đã log | Pillar bài trỏ lên | Post title |
|---|---|---|---|---|---|---|---|
| **Pillar B** | [#89 /best-chatbot-customer-service-real-estate](https://infina.ai/news/best-chatbot-customer-service-real-estate/) | 26 | 3,932 | 2026-10-13 | `chatbot customer service real estate` | *(là pillar)* | 15 Best Chatbot Customer Service Tools for Real Estate Teams (2026) |
| So sánh | [#123 /chatbot-vs-conversational-ai-real-estate](https://infina.ai/news/chatbot-vs-conversational-ai-real-estate/) | 10 | 1,725 | 2026-10-12 | `chatbot vs conversational ai real estate` | ✅ `best-conversational-ai-chatbot-for-real-estate`, `best-chatbot-customer-service-real-estate`; ↗ `best-ai-voice-assistants-for-real-estate` | Chatbot vs Conversational AI: What’s the Difference and Which Does Real Estate Need? |
| **Pillar A** | [#1056 /best-conversational-ai-chatbot-for-real-estate](https://infina.ai/news/best-conversational-ai-chatbot-for-real-estate/) | 9 | 3,038 | 2026-10-13 | `best conversational ai chatbot for real estate` | *(là pillar)* | Best Conversational AI Chatbots for Real Estate Agents in 2026 |
| ✅ Định nghĩa (HUB) | [#172 /what-is-a-conversational-chatbot-real-estate](https://infina.ai/news/what-is-a-conversational-chatbot-real-estate/) | 9 | 1,458 | 2026-10-09 | `conversational chatbot` | ✅ `best-conversational-ai-chatbot-for-real-estate`, `best-chatbot-customer-service-real-estate` | What Is a Conversational Chatbot? A Real Estate Agent’s Guide (2026) |
| ✅ Review/list (HUB) | [#117 /best-chatbot-builder-real-estate](https://infina.ai/news/best-chatbot-builder-real-estate/) | 7 | 2,506 | 2026-10-09 | `chatbot builder real estate` | ✅ `best-conversational-ai-chatbot-for-real-estate`, `best-chatbot-customer-service-real-estate`; ↗ `best-ai-voice-assistants-for-real-estate` | 10 Best Chatbot Builders for Real Estate Agents in 2026 |
| So sánh | [#138 /gohighlevel-chatbot-vs-dedicated-real-estate-chatbot](https://infina.ai/news/gohighlevel-chatbot-vs-dedicated-real-estate-chatbot/) | 7 | 1,541 | 2026-10-09 | `gohighlevel chatbot` | ✅ `best-conversational-ai-chatbot-for-real-estate`, `best-chatbot-customer-service-real-estate`; ↗ `best-ai-voice-assistants-for-real-estate` | GoHighLevel Chatbot vs Dedicated Real Estate Chatbots: Which Does Your Team Actually Need? |
| Hỗ trợ (News) | [#1146 /ai-chatbot-mls-data-security-risk-brokerages](https://infina.ai/news/ai-chatbot-mls-data-security-risk-brokerages/) | 5 | 778 | 2026-10-09 | `ai chatbot mls data security risk brokerages` | ✅ `best-chatbot-customer-service-real-estate` | A CRMLS Test Shows How Easily an AI Chatbot Can Leak Your MLS Data |
| So sánh/thay thế | [#189 /zendesk-sunshine-conversations-alternative-real-estate](https://infina.ai/news/zendesk-sunshine-conversations-alternative-real-estate/) | 5 | 1,078 | 2026-10-09 | `zendesk sunshine conversations alternative` | ✅ `best-chatbot-customer-service-real-estate` | Zendesk Sunshine Conversations Alternative for Real Estate Chatbots (2026) |
| So sánh | [#1071 /ai-chat-vs-sms-real-estate](https://infina.ai/news/ai-chat-vs-sms-real-estate/) | 2 | 1,367 | 2026-10-13 | `ai chat vs sms real estate` | ✅ `best-conversational-ai-chatbot-for-real-estate`, `best-chatbot-customer-service-real-estate` | AI Chat vs SMS Follow-Up for Real Estate: Which Converts More Leads? |
| Hỗ trợ (News) | [#1114 /ai-chatbot-mortgage-document-errors-real-estate-agents](https://infina.ai/news/ai-chatbot-mortgage-document-errors-real-estate-agents/) | 2 | 788 | 2026-10-09 | `ai chatbot mortgage document errors real estate agents` | ✅ `best-conversational-ai-chatbot-for-real-estate` | A New Study Found AI Got 1 in 4 Mortgage Document Checks Wrong |
| Hỗ trợ (News) | [#1050 /ai-disclosure-rules-for-real-estate-chatbots](https://infina.ai/news/ai-disclosure-rules-for-real-estate-chatbots/) | 2 | 891 | 2026-10-01 | `ai disclosure rules for real estate chatbots` | ✅ `best-chatbot-customer-service-real-estate` | EU AI Act Disclosure Rules Are Already Changing Your Real Estate Chatbot |
| So sánh | [#1078 /chatbot-vs-live-agent-real-estate](https://infina.ai/news/chatbot-vs-live-agent-real-estate/) | 2 | 1,371 | 2026-10-13 | `chatbot vs live agent real estate` | ✅ `best-chatbot-customer-service-real-estate` | Chatbot vs Live Agent for Real Estate: Response Time and Conversion Compared |
| Hỗ trợ (News) | [#1100 /real-estate-chatbot-that-reads-listing-photos](https://infina.ai/news/real-estate-chatbot-that-reads-listing-photos/) | 2 | 790 | 2026-10-13 | `real estate chatbot that reads listing photos` | ✅ `best-conversational-ai-chatbot-for-real-estate`, `best-chatbot-customer-service-real-estate` | This Chatbot Reads Your Listing Photos to Stop 47 Calls a Week |

## Cụm 2: CRM Software  (27 trang, 34,498 chữ)

| Vai trò | URL | IN | Chữ | Sửa lần cuối | FOCUS_KW đã log | Pillar bài trỏ lên | Post title |
|---|---|---|---|---|---|---|---|
| **Pillar chính (ĐÃ ĐỔI 01/10)** | [#207 /best-crm-for-real-estate](https://infina.ai/news/best-crm-for-real-estate/) | 49 | 4,354 | 2026-10-14 | `best crm for real estate` | *(là pillar)* | Best Real Estate Agent CRM Software in 2026 (Compared) |
| Định nghĩa (khác góc) | [#214 /ai-crm-real-estate](https://infina.ai/news/ai-crm-real-estate/) | 23 | 1,755 | 2026-10-13 | `ai crm` | ✅ `best-crm-for-real-estate`, `ai-intent-layer-for-real-estate-crm`; ↗ `best-chatbot-customer-service-real-estate` | AI CRM for Real Estate: How Agents Use AI to Convert More Leads (2026) |
| Sub-topic: marketing (strategy) | [#263 /crm-marketing-real-estate](https://infina.ai/news/crm-marketing-real-estate/) | 15 | 1,384 | 2026-10-12 | `crm marketing` | ✅ `best-crm-for-real-estate` | CRM Marketing for Real Estate: How to Turn Your Database into a Deal Machine |
| **Pillar nhẹ 🎯 Infina AI** | [#1232 /ai-intent-layer-for-real-estate-crm](https://infina.ai/news/ai-intent-layer-for-real-estate-crm/) | 13 | 772 | 2026-10-13 | `ai intent layer for real estate crm` | *(là pillar)* | AI Intent Layer for Real Estate CRM: What It Adds |
| Sub-topic: pipeline | [#277 /crm-pipeline-management](https://infina.ai/news/crm-pipeline-management/) | 12 | 1,703 | 2026-10-12 | `crm pipeline` | ✅ `best-crm-for-real-estate` | CRM Pipeline Management: Build a Sales Pipeline That Actually Closes |
| Hỗ trợ (News) | [#1026 /ai-agent-integration-for-real-estate-crm-platforms](https://infina.ai/news/ai-agent-integration-for-real-estate-crm-platforms/) | 6 | 871 | 2026-10-09 | `ai agent integration for real estate crm platforms` | ✅ `best-crm-for-real-estate`, `ai-intent-layer-for-real-estate-crm` | Rechat Just Let Claude and ChatGPT Run Real Estate CRM Workflows Directly |
| Định nghĩa (beginner) | [#405 /crm-management-real-estate-agents-beginners-guide](https://infina.ai/news/crm-management-real-estate-agents-beginners-guide/) | 6 | 1,166 | 2026-10-12 | `crm management` | ✅ `best-crm-for-real-estate` | CRM Software 101: A Beginner’s Guide for Real Estate Agents |
| Review (brand cụ thể) 🎯 Infina AI | [#1449 /follow-up-boss-real-estate-crm](https://infina.ai/news/follow-up-boss-real-estate-crm/) | 6 | 1,546 | 2026-10-13 | `follow up boss real estate crm` | ✅ `best-crm-for-real-estate`, `ai-intent-layer-for-real-estate-crm`; ↗ `real-estate-lead-follow-up-automation-guide` | Follow Up Boss Real Estate CRM Review: Pricing, Features, and the Follow-Up Gap |
| Review/list (niche: teams) | [#419 /best-crm-for-real-estate-teams-2026](https://infina.ai/news/best-crm-for-real-estate-teams-2026/) | 5 | 1,177 | 2026-10-12 | `best crm for real estate teams 2026` ⚠️ | ✅ `best-crm-for-real-estate` | Best CRM for Real Estate Teams: Top Picks for 2026 |
| Buying guide (BOF) | [#444 /best-crm-buying-guide-real-estate-agents](https://infina.ai/news/best-crm-buying-guide-real-estate-agents/) | 4 | 1,135 | 2026-10-09 | `best crm` | ✅ `best-crm-for-real-estate` | Best CRM for Real Estate Agents: A Buyer’s Guide (2026) |
| So sánh (MOF) 🎯 Infina AI | [#1487 /customer-engagement-platform-vs-crm](https://infina.ai/news/customer-engagement-platform-vs-crm/) | 4 | 1,365 | 2026-10-13 | `customer engagement platform vs crm` | ✅ `best-crm-for-real-estate`, `ai-intent-layer-for-real-estate-crm`; ↗ `real-estate-lead-follow-up-automation-guide`, `tcpa-compliance-for-real-estate-agents` | Customer Engagement Platform vs CRM for Real Estate: Where Each One Stops |
| Review/list (niche: broker) | [#1462 /real-estate-broker-crm](https://infina.ai/news/real-estate-broker-crm/) | 4 | 1,578 | 2026-10-12 | `real estate broker crm` | ✅ `best-crm-for-real-estate`, `ai-intent-layer-for-real-estate-crm`; ↗ `real-estate-lead-follow-up-automation-guide`, `tcpa-compliance-for-real-estate-agents` | Real Estate Broker CRM: What Brokerages Need That Agent CRMs Miss |
| Định nghĩa (niche RE) | [#1458 /what-does-crm-mean-in-real-estate](https://infina.ai/news/what-does-crm-mean-in-real-estate/) | 4 | 1,128 | 2026-10-12 | `what does crm mean in real estate` | ✅ `best-crm-for-real-estate` | What Does CRM Mean in Real Estate? A Plain-English Guide for Agents |
| Định nghĩa | [#230 /what-is-crm-software](https://infina.ai/news/what-is-crm-software/) | 4 | 1,598 | 2026-10-12 | `what is crm software` | ✅ `best-crm-for-real-estate` | What Is CRM Software? Complete Guide for Businesses in 2026 |
| Sub-topic: marketing (định nghĩa) | [#450 /crm-marketing-software-real-estate-guide](https://infina.ai/news/crm-marketing-software-real-estate-guide/) | 3 | 997 | 2026-10-09 | `crm marketing software` | ✅ `best-crm-for-real-estate` | What Is CRM Marketing Software? A Guide for Real Estate Teams |
| Bridge → Cụm 3 | [#585 /crm-with-website-builder-real-estate](https://infina.ai/news/crm-with-website-builder-real-estate/) | 3 | 1,185 | 2026-10-09 | `crm with website builder` | ✅ `best-crm-for-real-estate`; ↗ `real-estate-website-builder` | CRM with Website Builder: Best Integrated Platforms for Real Estate Teams |
| Hỗ trợ (News) | [#1184 /exp-nexus-crm-software-cost-reduction-agents](https://infina.ai/news/exp-nexus-crm-software-cost-reduction-agents/) | 3 | 775 | 2026-10-12 | `exp nexus crm software cost reduction agents` | ✅ `best-crm-for-real-estate` | eXp Realty Says Its All-in-One AI Platform Cuts Software Costs by 70% |
| Review/list (niche: free) | [#438 /best-free-crm-for-real-estate-agents](https://infina.ai/news/best-free-crm-for-real-estate-agents/) | 2 | 1,181 | 2026-10-15 | `free crm for real estate` | ✅ `best-crm-for-real-estate` | Best Free CRM for Real Estate Agents in 2026 |
| Review (brand cụ thể) 🎯 Infina AI | [#1234 /cinc-crm-review-real-estate](https://infina.ai/news/cinc-crm-review-real-estate/) | 2 | 647 | 2026-10-13 | `cinc crm review` | ✅ `best-crm-for-real-estate`, `ai-intent-layer-for-real-estate-crm` | CINC CRM Review: Pricing, Features, and Buyer Follow-Up Gaps |
| Hỗ trợ (News) | [#1329 /open-ai-protocol-real-estate-crm-brokerages](https://infina.ai/news/open-ai-protocol-real-estate-crm-brokerages/) | 2 | 582 | 2026-10-11 | – | ✅ `best-crm-for-real-estate`, `ai-intent-layer-for-real-estate-crm` | Lofty Launches an MCP Server So Any AI Can Plug Into Its CRM |
| Hỗ trợ (News) | [#1739 /real-estate-brokerage-technology-adoption-rates](https://infina.ai/news/real-estate-brokerage-technology-adoption-rates/) | 2 | 1,244 | 2026-10-12 | – | ✅ `best-crm-for-real-estate` | Brokerage-Provided Tech Sees 15% to 20% Adoption, and Brokers Want One Interface |
| Hỗ trợ (News) | [#1171 /ai-crm-assistant-brokerage-merger-rollout-agents](https://infina.ai/news/ai-crm-assistant-brokerage-merger-rollout-agents/) | 1 | 864 | 2026-10-12 | `ai crm assistant brokerage merger rollout agents` | ✅ `ai-intent-layer-for-real-estate-crm` | Real’s AI CRM Assistant Leo Is About to Meet 180,000 New RE/MAX Agents |
| Hỗ trợ (News) | [#1323 /arm-borrower-tracking-real-estate-agent-crm](https://infina.ai/news/arm-borrower-tracking-real-estate-agent-crm/) | 1 | 571 | 2026-10-02 | – | ✅ `best-crm-for-real-estate` | Nearly 10% of Borrowers Are Now Choosing ARMs as Rates Top 7% |
| Hỗ trợ (News) | [#1746 /bring-your-own-ai-assistant-real-estate-brokerages](https://infina.ai/news/bring-your-own-ai-assistant-real-estate-brokerages/) | 1 | 1,236 | 2026-10-23 | – | ✅ `best-crm-for-real-estate` | eXp Wants Agents to Connect Their Own AI to Brokerage Data, Not Use Its Chatbot |
| cluster (thiếu ở bảng plan) | [#247 /crm-for-real-estate-agents](https://infina.ai/news/crm-for-real-estate-agents/) | 1 | 1,731 | 2026-10-12 | `crm for real estate agents` ⚠️ | ✅ `best-crm-for-real-estate` | CRM for Real Estate Agents: How to Choose the Right One in 2026 |
| Bridge → Cụm 3 | [#643 /real-estate-crm-with-idx](https://infina.ai/news/real-estate-crm-with-idx/) | 1 | 771 | 2026-10-09 | `real estate crm with idx` | ✅ `best-crm-for-real-estate`; ↗ `real-estate-website-builder` | Real Estate CRM with IDX Integration: Best Platforms in 2026 |
| Listicle chiến lược (TOF) 🎯 Infina AI | [#1488 /real-estate-customer-engagement-strategies](https://infina.ai/news/real-estate-customer-engagement-strategies/) | 1 | 1,182 | 2026-10-09 | `real estate customer engagement` | ✅ `best-crm-for-real-estate`, `ai-intent-layer-for-real-estate-crm`; ↗ `real-estate-lead-follow-up-automation-guide`, `tcpa-compliance-for-real-estate-agents` | Real Estate Customer Engagement: 7 Tactics That Earn a Reply |

## Cụm 3: Website Builder / IDX  (14 trang, 16,643 chữ)

| Vai trò | URL | IN | Chữ | Sửa lần cuối | FOCUS_KW đã log | Pillar bài trỏ lên | Post title |
|---|---|---|---|---|---|---|---|
| **Pillar** | [#546 /real-estate-website-builder](https://infina.ai/news/real-estate-website-builder/) | 22 | 3,037 | 2026-10-14 | `real estate website builder` | *(là pillar)* | Best Real Estate Website Builders for Agents and Brokers (2026) |
| Định nghĩa (broker) | [#598 /broker-idx-guide](https://infina.ai/news/broker-idx-guide/) | 9 | 2,357 | 2026-10-08 | `broker idx` | ✅ `real-estate-website-builder`; ↗ `best-crm-for-real-estate` | What Is Broker IDX? Complete Guide for Real Estate Agents (2026) |
| ✅ Review/list (roundup, HUB) | [#610 /idx-website-for-realtors](https://infina.ai/news/idx-website-for-realtors/) | 8 | 865 | 2026-10-14 | `idx website for realtors` | ✅ `real-estate-website-builder`; ↗ `best-crm-for-real-estate` | Best IDX Website for Realtors: Top Platforms Reviewed (2026) |
| How-to (kỹ thuật) | [#622 /idx-mls-real-estate-guide](https://infina.ai/news/idx-mls-real-estate-guide/) | 3 | 797 | 2026-10-12 | `idx mls` | ✅ `real-estate-website-builder`; ↗ `best-crm-for-real-estate` | IDX MLS: How the Data Feed Powers Real Estate Agent Websites |
| Review (niche: solo agent) | [#567 /real-estate-agent-website-builder](https://infina.ai/news/real-estate-agent-website-builder/) | 3 | 1,167 | 2026-10-09 | `real estate agent website builder` | ✅ `real-estate-website-builder`; ↗ `best-crm-for-real-estate` | Best Real Estate Agent Website Builder for Solo Agents in 2026 |
| Buying guide | [#655 /real-estate-agent-websites-with-idx](https://infina.ai/news/real-estate-agent-websites-with-idx/) | 3 | 685 | 2026-10-09 | `real estate agent websites with idx` | ✅ `real-estate-website-builder`; ↗ `best-crm-for-real-estate` | Real Estate Agent Websites with IDX: What to Look For Before You Buy |
| Review (niche: realtor) | [#561 /best-website-builder-for-realtors](https://infina.ai/news/best-website-builder-for-realtors/) | 2 | 1,025 | 2026-10-12 | `best website builder for realtors` | ✅ `real-estate-website-builder`; ↗ `best-crm-for-real-estate` | Best Website Builder for Realtors: Top Picks Reviewed (2026) |
| How-to (kỹ thuật) | [#631 /idx-feed-real-estate-setup](https://infina.ai/news/idx-feed-real-estate-setup/) | 2 | 702 | 2026-10-09 | `idx feed` | ✅ `real-estate-website-builder`; ↗ `best-crm-for-real-estate` | IDX Feed: What It Is and How to Set It Up on Your Website |
| Định nghĩa (chung) | [#604 /idx-real-estate-definition-guide](https://infina.ai/news/idx-real-estate-definition-guide/) | 2 | 999 | 2026-10-09 | `idx real estate` | ✅ `real-estate-website-builder`; ↗ `best-crm-for-real-estate` | What Is IDX in Real Estate? Definition, Setup, and How It Works |
| Examples/inspiration | [#616 /idx-real-estate-websites-examples](https://infina.ai/news/idx-real-estate-websites-examples/) | 2 | 758 | 2026-10-14 | `idx real estate websites` | ✅ `real-estate-website-builder`; ↗ `best-crm-for-real-estate` | IDX Real Estate Websites: Best Examples and What Makes Them Work |
| Hỗ trợ (News) | [#1473 /off-mls-listings-on-agent-idx-websites](https://infina.ai/news/off-mls-listings-on-agent-idx-websites/) | 2 | 859 | 2026-10-09 | `off mls listings on agent idx websites` | ✅ `real-estate-website-builder` | Compass Gave an MLS Until October 6, and Agent Search Sites Are Caught in the Middle |
| Review (niche: investor) | [#579 /best-website-builder-real-estate-investors](https://infina.ai/news/best-website-builder-real-estate-investors/) | 1 | 1,009 | 2026-10-09 | `best website builder for real estate investors` | ✅ `real-estate-website-builder`; ↗ `best-crm-for-real-estate` | Best Website Builder for Real Estate Investors in 2026 |
| Review (niche: free) | [#573 /free-real-estate-website-builder](https://infina.ai/news/free-real-estate-website-builder/) | 1 | 1,102 | 2026-10-09 | `free real estate website builder` | ✅ `real-estate-website-builder`; ↗ `best-crm-for-real-estate` | Free Real Estate Website Builder: What You Get vs. What You Pay For |
| Hỗ trợ (News) | [#1732 /real-estate-website-built-from-crm-data](https://infina.ai/news/real-estate-website-built-from-crm-data/) | 1 | 1,281 | 2026-10-12 | – | ✅ `real-estate-website-builder` | Rechat Now Builds the Agent Website From the CRM, Not Next to It |

## Cụm 4: AI Voice / Virtual Assistant / Receptionist  (6 trang, 7,320 chữ)

| Vai trò | URL | IN | Chữ | Sửa lần cuối | FOCUS_KW đã log | Pillar bài trỏ lên | Post title |
|---|---|---|---|---|---|---|---|
| **Pillar = refresh #147** | [#147 /best-ai-voice-assistants-for-real-estate](https://infina.ai/news/best-ai-voice-assistants-for-real-estate/) | 11 | 2,287 | 2026-10-13 | `ai voice assistants for real estate` | *(là pillar)* | 7 Best AI Voice Assistants for Real Estate Agents in 2026 |
| Review/list (phát hiện thêm 01/10) | [#110 /best-ai-virtual-assistant-real-estate](https://infina.ai/news/best-ai-virtual-assistant-real-estate/) | 7 | 1,800 | 2026-10-13 | `ai virtual assistant real estate` | ✅ `best-ai-voice-assistants-for-real-estate`; ↗ `best-chatbot-customer-service-real-estate` | 7 Best AI Virtual Assistants for Real Estate Agents in 2026 |
| Support/how-to → bắc cầu Cụm 7 | [#1213 /ai-outbound-calling-real-estate-lead-follow-up](https://infina.ai/news/ai-outbound-calling-real-estate-lead-follow-up/) | 5 | 926 | 2026-10-09 | `ai outbound calling real estate lead follow up` | ✅ `best-ai-voice-assistants-for-real-estate`; ↗ `tcpa-compliance-for-real-estate-agents` | AI Outbound Calling for Real Estate: How It Works in 2026 |
| So sánh | [#1217 /ai-receptionist-vs-human-receptionist-real-estate](https://infina.ai/news/ai-receptionist-vs-human-receptionist-real-estate/) | 2 | 714 | 2026-10-09 | `ai receptionist vs human receptionist real estate` | ✅ `best-ai-voice-assistants-for-real-estate`; ↗ `tcpa-compliance-for-real-estate-agents` | AI Receptionist vs Human Receptionist for Real Estate: Cost & ROI |
| Buying guide | [#1219 /ai-answering-service-for-real-estate](https://infina.ai/news/ai-answering-service-for-real-estate/) | 1 | 699 | 2026-10-09 | `ai answering service for real estate` | ✅ `best-ai-voice-assistants-for-real-estate`; ↗ `tcpa-compliance-for-real-estate-agents` | AI Answering Service for Real Estate: How to Choose the Right One |
| Hỗ trợ (News) | [#1467 /ai-voice-calls-for-listing-price-updates](https://infina.ai/news/ai-voice-calls-for-listing-price-updates/) | 1 | 894 | 2026-10-09 | `ai voice calls for listing price updates` | ✅ `best-ai-voice-assistants-for-real-estate`; ↗ `tcpa-compliance-for-real-estate-agents` | Nearly 1 in 5 Homes Cut Price in September, and Agents Are Running Out of Call Hours |

## Cụm 5: Website / Web Design  (6 trang, 6,777 chữ)

| Vai trò | URL | IN | Chữ | Sửa lần cuối | FOCUS_KW đã log | Pillar bài trỏ lên | Post title |
|---|---|---|---|---|---|---|---|
| **Pillar (HUB)** | [#975 /website-design-for-real-estate-agents](https://infina.ai/news/website-design-for-real-estate-agents/) | 10 | 1,805 | 2026-10-12 | `website design for real estate agents` | *(là pillar)* | Website Design for Real Estate Agents: What Actually Works in 2026 |
| Review (niche: luxury) | [#1011 /luxury-real-estate-website-design](https://infina.ai/news/luxury-real-estate-website-design/) | 4 | 1,089 | 2026-10-14 | `luxury real estate website design` | ✅ `website-design-for-real-estate-agents`; ↗ `real-estate-website-builder` | Luxury Real Estate Website Design: Features That Signal Premium to Buyers |
| Examples/inspiration | [#981 /best-real-estate-website-design](https://infina.ai/news/best-real-estate-website-design/) | 1 | 1,011 | 2026-10-14 | `best real estate website design` | ✅ `website-design-for-real-estate-agents`; ↗ `real-estate-website-builder` | Best Real Estate Website Design: 8 Examples to Model in 2026 |
| Review (niche: broker) | [#1005 /real-estate-broker-website-design](https://infina.ai/news/real-estate-broker-website-design/) | 1 | 989 | 2026-10-12 | `real estate broker website design` | ✅ `website-design-for-real-estate-agents`; ↗ `real-estate-website-builder` | Real Estate Broker Website Design: What Brokerage Sites Actually Need |
| Buying guide (agency) | [#999 /real-estate-web-design-companies](https://infina.ai/news/real-estate-web-design-companies/) | 1 | 932 | 2026-10-12 | `real estate web design companies` | ✅ `website-design-for-real-estate-agents`; ↗ `real-estate-website-builder` | Real Estate Web Design Companies: How to Choose the Right One |
| Decision (build vs buy) | [#993 /web-design-for-real-estate-agents](https://infina.ai/news/web-design-for-real-estate-agents/) | 1 | 951 | 2026-10-12 | `web design for real estate agents` | ✅ `website-design-for-real-estate-agents`; ↗ `real-estate-website-builder` | Web Design for Real Estate Agents: DIY vs. Hiring a Designer |

## Cụm 6: Landing Pages  (6 trang, 8,316 chữ)

| Vai trò | URL | IN | Chữ | Sửa lần cuối | FOCUS_KW đã log | Pillar bài trỏ lên | Post title |
|---|---|---|---|---|---|---|---|
| Niche: open house | [#918 /open-house-landing-page](https://infina.ai/news/open-house-landing-page/) | 8 | 1,705 | 2026-10-13 | `open house landing page` | ✅ `real-estate-landing-page-guide`; ↗ `best-crm-for-real-estate` | Open House Landing Page: How to Build One That Actually Captures Leads |
| **Pillar** | [#930 /real-estate-landing-page-guide](https://infina.ai/news/real-estate-landing-page-guide/) | 7 | 1,897 | 2026-10-13 | `real estate landing page` | *(là pillar)* | Real Estate Landing Page: Types, Elements, and How to Build One That Converts |
| Niche: seller chung | [#942 /seller-landing-pages-real-estate](https://infina.ai/news/seller-landing-pages-real-estate/) | 3 | 1,024 | 2026-10-12 | `seller landing pages real estate` | ✅ `real-estate-landing-page-guide`; ↗ `best-crm-for-real-estate` | Seller Landing Pages Real Estate: Types That Convert and How to Build Them |
| Niche: home valuation | [#936 /home-valuation-landing-page](https://infina.ai/news/home-valuation-landing-page/) | 2 | 1,165 | 2026-10-12 | `home valuation landing page` | ✅ `real-estate-landing-page-guide`; ↗ `best-crm-for-real-estate` | Home Valuation Landing Page: How to Build One That Converts Seller Leads |
| ✅ Evaluation/MOF (cluster hợp lệ) | [#948 /high-converting-real-estate-landing-pages](https://infina.ai/news/high-converting-real-estate-landing-pages/) | 1 | 1,289 | 2026-10-12 | `high converting real estate landing pages` | ✅ `real-estate-landing-page-guide`; ↗ `best-crm-for-real-estate` | High Converting Real Estate Landing Pages: What Makes Them Work in 2026 |
| Niche: agent chung | [#924 /real-estate-agent-landing-page](https://infina.ai/news/real-estate-agent-landing-page/) | 1 | 1,236 | 2026-10-09 | `real estate agent landing page` | ✅ `real-estate-landing-page-guide`; ↗ `best-crm-for-real-estate` | Real Estate Agent Landing Page: What to Include and How to Convert Visitors |

## Cụm 7: Lead Generation / Follow-up Automation  (9 trang, 8,338 chữ)

| Vai trò | URL | IN | Chữ | Sửa lần cuối | FOCUS_KW đã log | Pillar bài trỏ lên | Post title |
|---|---|---|---|---|---|---|---|
| **Pillar** | [#1223 /real-estate-lead-follow-up-automation-guide](https://infina.ai/news/real-estate-lead-follow-up-automation-guide/) | 20 | 2,483 | 2026-10-13 | `real estate lead follow-up automation` | *(là pillar)* | Real Estate Lead Follow-Up Automation: The Complete 2026 Guide |
| Giải thích/pain-point = refresh #223 | [#223 /real-estate-agent-crm-speed-to-lead](https://infina.ai/news/real-estate-agent-crm-speed-to-lead/) | 13 | 1,560 | 2026-10-13 | `real estate agent crm` | ✅ `real-estate-lead-follow-up-automation-guide`; ↗ `best-crm-for-real-estate` | Speed-to-Lead 2026: How Real Estate Agent CRM Closes the 15-Hour Gap |
| Review/list | [#1225 /best-lead-generation-software-for-realtors](https://infina.ai/news/best-lead-generation-software-for-realtors/) | 4 | 602 | 2026-10-09 | `lead generation software for realtors` | ✅ `real-estate-lead-follow-up-automation-guide` | Best Lead Generation Software for Realtors in 2026 |
| Buying guide/how-to | [#1227 /how-to-set-up-automated-lead-follow-up-real-estate](https://infina.ai/news/how-to-set-up-automated-lead-follow-up-real-estate/) | 4 | 577 | 2026-10-13 | `automated lead follow-up for real estate` | ✅ `real-estate-lead-follow-up-automation-guide` | Automated Lead Follow-Up for Real Estate: A 5-Step Setup Guide |
| Kênh cụ thể | [#1229 /facebook-lead-gen-for-realtors](https://infina.ai/news/facebook-lead-gen-for-realtors/) | 3 | 542 | 2026-10-09 | `facebook lead gen for realtors` | ✅ `real-estate-lead-follow-up-automation-guide`; ↗ `best-ai-voice-assistants-for-real-estate` | Facebook Lead Gen for Realtors: Turning Ad Leads Into Showings |
| Hỗ trợ (News) | [#1122 /database-reactivation-ai-seller-leads-real-estate-agents](https://infina.ai/news/database-reactivation-ai-seller-leads-real-estate-agents/) | 2 | 756 | 2026-10-09 | `database reactivation ai seller leads real estate agents` | ✅ `real-estate-lead-follow-up-automation-guide` | Your Next Listing Is Probably Already Sitting in Your CRM |
| Hỗ trợ (News) | [#1278 /seller-lead-prioritization-real-estate-pipeline](https://infina.ai/news/seller-lead-prioritization-real-estate-pipeline/) | 2 | 582 | 2026-10-09 | – | ✅ `real-estate-lead-follow-up-automation-guide` | Sellers Now Outnumber Buyers by 57.9%, the Widest Gap on Record |
| Hỗ trợ (News) | [#1272 /buyer-lead-nurture-campaign-real-estate-agents](https://infina.ai/news/buyer-lead-nurture-campaign-real-estate-agents/) | 1 | 569 | 2026-09-19 | – | ✅ `real-estate-lead-follow-up-automation-guide` | Realtor.com Just Named the Best Week to Buy in 2026, and Everyone Read It |
| Hỗ trợ | [#521 /real-estate-contact-form-conversion-rate](https://infina.ai/news/real-estate-contact-form-conversion-rate/) | 1 | 667 | 2026-10-12 | `real estate contact form conversion rate` | ✅ `real-estate-lead-follow-up-automation-guide`; ↗ `best-chatbot-customer-service-real-estate` | Real Estate Contact Forms Are Losing the Highest-Intent Leads |

## Cụm 8: Compliance / Legal / Risk  (6 trang, 6,005 chữ)

| Vai trò | URL | IN | Chữ | Sửa lần cuối | FOCUS_KW đã log | Pillar bài trỏ lên | Post title |
|---|---|---|---|---|---|---|---|
| **Pillar (nhẹ)** | [#237 /tcpa-compliance-for-real-estate-agents](https://infina.ai/news/tcpa-compliance-for-real-estate-agents/) | 22 | 1,909 | 2026-10-12 | `tcpa compliance for real estate agents` | *(là pillar)* | TCPA Compliance for Real Estate Agents: What Is Actually in Force for AI Texting and Calling |
| Hỗ trợ (News) | [#475 /ai-hallucination-risk-real-estate-listings](https://infina.ai/news/ai-hallucination-risk-real-estate-listings/) | 4 | 956 | 2026-10-12 | `ai hallucination risk real estate listings` | ✅ `tcpa-compliance-for-real-estate-agents` | AI-Written Listing Descriptions Are Creating Fair Housing Liability: Here’s What to Check |
| Hỗ trợ (News) | [#492 /ai-decision-making-compliance-real-estate-agents](https://infina.ai/news/ai-decision-making-compliance-real-estate-agents/) | 3 | 699 | 2026-10-12 | `ai decision making compliance real estate agents` | ✅ `tcpa-compliance-for-real-estate-agents` | Colorado’s New AI Law Sets a Deadline for Automated Decisions in Real Estate |
| Hỗ trợ (News) | [#1260 /seller-impersonation-fraud-prevention-real-estate-agents](https://infina.ai/news/seller-impersonation-fraud-prevention-real-estate-agents/) | 2 | 640 | 2026-10-09 | – | ✅ `tcpa-compliance-for-real-estate-agents` | Seller Impersonation Fraud Attempts Just Doubled. Here Is How to Catch It Earlier |
| Hỗ trợ (News) | [#1481 /how-agents-protect-clients-from-wire-fraud](https://infina.ai/news/how-agents-protect-clients-from-wire-fraud/) | 1 | 928 | 2026-10-09 | `how agents protect clients from wire fraud` | ✅ `tcpa-compliance-for-real-estate-agents` | Two Wire Fraud Companies Just Merged, and the Agent Is Still the Weak Link |
| Hỗ trợ (News) | [#1501 /private-listing-marketing-rules](https://infina.ai/news/private-listing-marketing-rules/) | 1 | 873 | 2026-10-09 | `private listing marketing rules` | ✅ `tcpa-compliance-for-real-estate-agents` | Three States Now Force Private Listings Public the Moment You Market Them |

## Cụm 9: Marketing và Branding  (28 bài, 44,661 chữ, 28 đã đăng, làm mới 2026-10-23)

**Tiến độ:** pillar #1825 và hub branding #1832 đăng 12/10. Wave 1 (10 bài, #1843–#1901) đăng 12–15/10, wave 2 (8 bài, #1937–#1979)
đăng 16–18/10, wave 3 (8 bài, #2165–#2207) đăng 19–21/10. Cả 28 bài đã có link ngược (đợt 15/10, 18/10 và 21/10). Từ 23/10 mọi bài trong
cụm có ít nhất 2 link ngang cùng cụm và anchor tới 3 đích chính (#1843, #1832, #1825) đạt trên 70% khác nhau. Bảng dưới là **số đo thật**
(IN, chữ, ngày sửa), cùng format với các cụm khác; density và trạng thái lúc viết nằm ở `content-plan.md` và `plan-cum-9-marketing-branding.md`.

| Vai trò | URL | IN | Chữ | Sửa lần cuối | FOCUS_KW đã log | Pillar bài trỏ lên | Post title |
|---|---|---|---|---|---|---|---|
| **Pillar** | [#1825 /real-estate-marketing](https://infina.ai/news/real-estate-marketing/) | 22 | 2,624 | 2026-10-21 | `real estate marketing` | *(là pillar)* | Real Estate Marketing Guide: What to Do, Spend and Measure |
| how-to Wave 1 | [#1843 /real-estate-marketing-plan](https://infina.ai/news/real-estate-marketing-plan/) | 17 | 1,883 | 2026-10-23 | `real estate marketing plan` | ✅ `real-estate-marketing`, `real-estate-branding`; ↗ `real-estate-lead-follow-up-automation-guide` | Real Estate Marketing Plan: Template and Budget |
| **Hub branding** | [#1832 /real-estate-branding](https://infina.ai/news/real-estate-branding/) | 12 | 1,829 | 2026-10-21 | `real estate branding` | *(là pillar)* | Real Estate Branding: A Practical Guide for Agents and Teams |
| niche Wave 1 | [#1895 /real-estate-agent-bio](https://infina.ai/news/real-estate-agent-bio/) | 6 | 1,723 | 2026-10-23 | `real estate agent bio` | ✅ `real-estate-branding` | Real Estate Agent Bio: Examples and a Template |
| niche Wave 1 | [#1883 /real-estate-agent-business-card](https://infina.ai/news/real-estate-agent-business-card/) | 6 | 1,845 | 2026-10-14 | `real estate agent business card` | ✅ `real-estate-branding`; ↗ `website-design-for-real-estate-agents` | Real Estate Business Cards: Ideas, Templates and What to Print |
| how-to Wave 2 | [#1961 /real-estate-agent-referral](https://infina.ai/news/real-estate-agent-referral/) | 6 | 1,353 | 2026-10-23 | `real estate agent referral` | ✅ `real-estate-marketing` | Real Estate Agent Referral: Get More and Pay Fees Correctly |
| how-to Wave 1 | [#1865 /social-media-for-realtors](https://infina.ai/news/social-media-for-realtors/) | 6 | 1,703 | 2026-10-14 | `social media for realtors` | ✅ `real-estate-marketing`, `real-estate-branding` | Social Media for Realtors: A Weekly Routine That Fits a Production Schedule |
| explainer Wave 1 | [#1859 /real-estate-advertising](https://infina.ai/news/real-estate-advertising/) | 5 | 1,751 | 2026-10-23 | `real estate advertising` | ✅ `real-estate-marketing` | Real Estate Advertising: Channels, Costs and Examples |
| niche Wave 1 | [#1889 /real-estate-agent-logo](https://infina.ai/news/real-estate-agent-logo/) | 5 | 1,874 | 2026-10-23 | `real estate agent logo` | ✅ `real-estate-branding` | Real Estate Logos: Ideas and How to Design One |
| how-to Wave 3 | [#2165 /real-estate-farming](https://infina.ai/news/real-estate-farming/) | 5 | 1,731 | 2026-10-23 | `real estate farming` | ✅ `real-estate-marketing`; ↗ `tcpa-compliance-for-real-estate-agents` | Real Estate Farming: How to Pick a Farm and Work It for a Year |
| how-to Wave 1 | [#1877 /real-estate-postcards](https://infina.ai/news/real-estate-postcards/) | 5 | 1,910 | 2026-10-23 | `postcards real estate` | ✅ `real-estate-marketing`, `real-estate-branding`; ↗ `real-estate-landing-page-guide` | Real Estate Postcards and Mailers That Get Opened |
| how-to Wave 2 | [#1949 /real-estate-testimonials](https://infina.ai/news/real-estate-testimonials/) | 5 | 1,416 | 2026-10-23 | `real estate testimonials` | ✅ `real-estate-branding` | Real Estate Testimonials: How to Ask, Examples and Rules |
| how-to Wave 2 | [#1967 /flyer-for-real-estate](https://infina.ai/news/flyer-for-real-estate/) | 4 | 1,288 | 2026-10-23 | `flyer for real estate` | ✅ `real-estate-marketing`, `real-estate-branding` | Real Estate Flyers: Examples, Templates and What to Include |
| how-to Wave 2 | [#1937 /google-business-profile-for-realtors](https://infina.ai/news/google-business-profile-for-realtors/) | 4 | 1,514 | 2026-10-23 | `google business profile for realtors` | ✅ `real-estate-marketing` | Google Business Profile for Realtors: Setup, Fields and Reviews |
| how-to Wave 3 | [#2195 /real-estate-prospecting-letters](https://infina.ai/news/real-estate-prospecting-letters/) | 4 | 1,326 | 2026-10-20 | `real estate prospecting letters` | ✅ `real-estate-marketing`; ↗ `tcpa-compliance-for-real-estate-agents` | Real Estate Prospecting Letters: Templates for Sellers, Expired Listings and Just Sold |
| how-to Wave 3 | [#2201 /door-knocking-for-real-estate-agents](https://infina.ai/news/door-knocking-for-real-estate-agents/) | 3 | 1,295 | 2026-10-21 | `door knocking for real estate agents` | ✅ `real-estate-marketing`; ↗ `tcpa-compliance-for-real-estate-agents` | Door Knocking for Real Estate Agents: Script, Etiquette and a Safe Routine |
| review Wave 1 | [#1853 /real-estate-marketing-ideas](https://infina.ai/news/real-estate-marketing-ideas/) | 3 | 1,910 | 2026-10-23 | `real estate marketing ideas` | ✅ `real-estate-marketing`; ↗ `tcpa-compliance-for-real-estate-agents`, `website-design-for-real-estate-agents` | 30 Real Estate Marketing Ideas, With Cost and Effort |
| niche Wave 2 | [#1979 /realtor-name-ideas](https://infina.ai/news/realtor-name-ideas/) | 3 | 1,373 | 2026-10-23 | `realtor name ideas` | ✅ `real-estate-branding` | Realtor Name Ideas: Formulas, Examples and Rules to Check |
| how-to Wave 2 | [#1977 /closing-gifts-real-estate](https://infina.ai/news/closing-gifts-real-estate/) | 2 | 1,326 | 2026-10-23 | `closing gifts real estate` | ✅ `real-estate-marketing` | Closing Gifts for Real Estate Clients: Ideas, Budget and Rules |
| how-to Wave 2 | [#1943 /google-ads-for-realtors](https://infina.ai/news/google-ads-for-realtors/) | 2 | 1,298 | 2026-10-23 | `google ads for realtors` | ✅ `real-estate-marketing`; ↗ `real-estate-lead-follow-up-automation-guide` | Google Ads for Realtors: Setup, Targeting Rules and Budget |
| how-to Wave 2 | [#1955 /listing-presentation](https://infina.ai/news/listing-presentation/) | 2 | 1,438 | 2026-10-23 | `listing presentation` | ✅ `real-estate-marketing` | Listing Presentation: Template, Sample Script and Examples |
| how-to Wave 3 | [#2183 /luxury-real-estate-marketing](https://infina.ai/news/luxury-real-estate-marketing/) | 2 | 1,316 | 2026-10-23 | `luxury real estate marketing` | ✅ `real-estate-marketing`, `real-estate-branding` | Luxury Real Estate Marketing and Branding: What Changes at the High End |
| how-to Wave 3 | [#2171 /open-house-ideas-for-realtors](https://infina.ai/news/open-house-ideas-for-realtors/) | 2 | 1,498 | 2026-10-19 | `open house ideas for realtors` | ✅ `real-estate-marketing`; ↗ `tcpa-compliance-for-real-estate-agents` | Open House Ideas for Realtors: Before, During and After |
| how-to Wave 3 | [#2207 /real-estate-cold-calling-scripts](https://infina.ai/news/real-estate-cold-calling-scripts/) | 2 | 1,279 | 2026-10-21 | `real estate cold calling scripts` | ✅ `real-estate-marketing`; ↗ `tcpa-compliance-for-real-estate-agents` | Real Estate Cold Calling Scripts and the Do Not Call Rules |
| how-to Wave 3 | [#2189 /real-estate-email-signature](https://infina.ai/news/real-estate-email-signature/) | 2 | 1,216 | 2026-10-20 | `real estate email signature` | ✅ `real-estate-branding`; ↗ `tcpa-compliance-for-real-estate-agents` | Real Estate Email Signature: What to Include, Examples and Required Disclosures |
| review Wave 1 | [#1901 /real-estate-marketing-software](https://infina.ai/news/real-estate-marketing-software/) | 2 | 1,752 | 2026-10-23 | `real estate marketing software` | ✅ `real-estate-marketing` | Real Estate Marketing Software: What to Use for Each Job in 2026 |
| how-to Wave 1 | [#1871 /real-estate-seo](https://infina.ai/news/real-estate-seo/) | 2 | 1,837 | 2026-10-14 | `real estate seo` | ✅ `real-estate-marketing`; ↗ `website-design-for-real-estate-agents` | Real Estate SEO for Agents: What Actually Moves Local Rankings |
| how-to Wave 3 | [#2177 /real-estate-video-marketing](https://infina.ai/news/real-estate-video-marketing/) | 2 | 1,353 | 2026-10-19 | `real estate video marketing` | ✅ `real-estate-marketing` | Real Estate Video Marketing: Video Ideas, Scripts and a Simple Setup |

### Còn lại cho Cụm 9

| # | Việc | Khi nào | Ai |
|---|---|---|---|
| 1 | Dán rows tracker vào sheet "Published article": wave 3 (#157–164), file `files/tracker-rows-cum9.tsv` (wave 1 và 2 đã dán) | Bất cứ lúc nào | **Bạn** |
| 2 | Sửa title bài #1415 trong tracker | Bất cứ lúc nào | **Bạn** |
| 3 | Request Indexing trong GSC cho 28 URL mới (ưu tiên pillar, hub, bài 5k volume: advertising, SEO, postcards, business card, logo, flyer) | Sau khi live | **Bạn** |
| 4 | ~~Bật lại news routine hằng ngày~~ **Đã bật lại 23/10**, chạy 18:06 UTC mỗi ngày, prompt đã cập nhật (Bước 6.5, ≥2 link ngang, inbound donor, tránh keyword Cụm 9 và 10) | Xong | Claude |
| 5 | Link money page `infina.ai/`: Cụm 9 hiện có 9/28 bài link, 19 bài chưa. Đề xuất chỉ thêm ở khoảng 6–8 bài hợp ngữ cảnh (software, referral, listing presentation, GBP, social) | Chờ bạn duyệt | Bạn quyết, Claude làm |
| 6 | Đo sau 4–8 tuần bằng `post-refresh` (GSC), tìm striking-distance keyword | Cuối 11/2026 | Claude |

**Luồng link đã chốt:** mỗi cluster 1 link lên pillar nhà (business card, logo, bio, name ideas, testimonials, luxury, email signature lên hub branding;
hub branding lên pillar marketing). Tối đa 1 link ra pillar cụm khác mỗi bài, nằm trong thân bài. Pillar và hub link xuống mọi cluster đúng 1 lần
trong mục Related Reading (pillar #1825 hiện có 20 bullet, hub #1832 có 7).

### Việc tồn đọng ngoài Cụm 9

| Việc | Ghi chú |
|---|---|
| Money page `https://infina.ai/` (Infina AI) | Hiện 28 bài blog link tới (đo 23/10). Chưa link: #1213, #1217, #1219, #1225, #1229. Dev còn làm prerender/SSR, title/meta/JSON-LD trong HTML, soft 404, redirect, sitemap, ảnh nặng, JS bundle (xem `realsalex-seo-dev-handoff.md`). Sau khi dev deploy: verify lại và Request Indexing |
| Link ngang cho Cụm 1–8 | Đo 23/10: 53/74 bài dưới 2 link ngang cùng cụm (nợ cũ, viết trước quy tắc 08/10). Chưa làm |
| Đa dạng anchor dưới 70% | Còn 8 đích: bio, GBP, farming, postcards, business card, social, CRM marketing, CEP vs CRM |
| Footer "© 2026 Infina" và khối testimonials trên money page | Chưa chỉnh (mục #18, #19 trong bảng đề xuất SEO), chưa kiểm lại 23/10 |
| `realsalex-landing-spec.md` trên `main` | Vẫn dùng tên cũ Real Sale X / AI Deal Room, chưa đổi sang Infina AI |
| Nhóm News: 18 bài không trỏ pillar nào, 11 bài AI/tech mồ côi | 11 bài AI/tech đã quyết định để nguyên (Đợt E). 18 bài News chưa xử lý |
| Đổi domain sang realstake.ai | Chờ sếp chốt tên, kế hoạch ở `plan-domain-migration-realstake.md` |

---

## Cụm 10: Lead Generation, nguồn lead cho agent  (ĐÃ DUYỆT 23/10, 13 bài, chưa viết, chưa có URL, đăng 26-31/10)

**Trạng thái (23/10/2026):** plan ở `plan-cum-10-lead-generation.md`, **đã duyệt cả 13 bài**, keyword đã đặt chỗ trong `used-keywords.md`
và ghi vào `content-plan.md`. Lịch đăng 26/10 đến 31/10, inbound pass 29/10 và 1/11, audit 2/11. Hiện **0 bài live** về expired, FSBO, circle prospecting, listing leads, buyer leads, SOI, free leads, Zillow leads
(đã đối chiếu 178 slug live). Bảng này là kế hoạch, nên không có cột IN, chữ hay ngày sửa như các cụm khác. Sau khi bài lên, chạy lại crawl để thay
bằng số đo thật. Volume là bucket US (50 / 500 / 5k), "L/TB/C" là cạnh tranh ads.

**Ranh giới:** Cụm 9 = được nhìn thấy. **Cụm 10 = lead đến từ đâu.** Cụm 7 = chăm lead sau khi tới. Keyword `lead generation for realestate` đã gán cho pillar
Cụm 7 (#1223) từ 15/09; Cụm 10 nhận `real estate lead generation` theo nghĩa nguồn lead, hai pillar link ngang cho nhau.

| # | Vai trò | Bài dự kiến | Focus keyword (bucket, ads) | Wave | Trạng thái |
|---|---|---|---|---|---|
| 1 | **Pillar** | [#2260 /real-estate-lead-generation](https://infina.ai/news/real-estate-lead-generation/) Real Estate Lead Generation: 10 Lead Sources Compared | `real estate lead generation` 5k TB (gom `real estate leads`, `real estate lead gen`, `real estate agent leads`, `leads in real estate`, `agent lead generation`, `online lead generation real estate`, đều 5k) | Hub, đăng trước | Đã viết, scheduled 23/10 10:00 UTC |
| 2 | **Pillar** (sub-hub) | [#2262 /listing-leads](https://infina.ai/news/listing-leads/) Listing Leads: How to Find Sellers and Win More Listings | `listing leads` 5k TB (gom `listing leads for realtors`, `real estate listing leads`, `seller leads real estate`, `seller leads for realtors`) | Hub, đăng trước | Đã viết, scheduled 23/10 14:00 UTC |
| 3 | how-to | [#2322 /expired-listings](https://infina.ai/news/expired-listings/) Expired Listings: How to Find Them and Reach the Owners | `expired listings` 500 TB (+ `expired mls listings`, `expired real estate listings`) | Wave 1 | Đã viết, scheduled 24/10 10:00 UTC, 1457 từ |
| 4 | how-to | [#2326 /circle-prospecting](https://infina.ai/news/circle-prospecting/) Circle Prospecting: Radius, Triggers and a Weekly Routine | `circle prospecting` 500 TB | Wave 1 | Đã viết, scheduled 24/10 14:00 UTC, 1281 từ |
| 5 | how-to | [#2330 /sphere-of-influence-real-estate](https://infina.ai/news/sphere-of-influence-real-estate/) Sphere of Influence in Real Estate: How to Build and Work It | `sphere of influence` | Wave 1 | Đã viết, scheduled 24/10 18:00 UTC, 1365 từ |
| 6 | how-to | [#2302 /buyer-leads-for-real-estate-agents](https://infina.ai/news/buyer-leads-for-real-estate-agents/) Buyer Leads for Real Estate Agents: Sources and Follow-Up | `buyer leads for real estate agents` 500 C | Wave 1 | Đã viết, scheduled 25/10 10:00 UTC, 1682 từ |
| 7 | how-to | [#2320 /free-real-estate-leads](https://infina.ai/news/free-real-estate-leads/) Free Real Estate Leads: A Zero-Budget Weekly Plan | `free real estate leads` 500 TB | Wave 1 | Đã viết, scheduled 25/10 14:00 UTC, 1651 từ |
| 8 | review | [#2332 /real-estate-lead-generation-companies](https://infina.ai/news/real-estate-lead-generation-companies/) Real Estate Lead Generation Companies: What to Compare | `real estate lead generation companies` 500 TB | Wave 1 | Đã viết, scheduled 25/10 18:00 UTC, 1697 từ |
| 9 | how-to | [#2315 /expired-listing-scripts](https://infina.ai/news/expired-listing-scripts/) Expired Listing Scripts: What to Say and How to Follow Up | `expired listing script` 500 TB | Wave 2 | Đã viết, scheduled 26/10 10:00 UTC, 1411 từ |
| 10 | review | [#2324 /zillow-leads-for-real-estate-agents](https://infina.ai/news/zillow-leads-for-real-estate-agents/) Zillow Leads for Real Estate Agents: How They Work | `zillow leads` 5k C | Wave 2 | Đã viết, scheduled 27/10 14:00 UTC, 1502 từ |
| 11 | niche | [#2334 /probate-real-estate-leads](https://infina.ai/news/probate-real-estate-leads/) Probate Real Estate Leads: How Agents Find and Serve Them | `probate real estate leads` 500 L | Wave 2 | Đã viết, scheduled 26/10 18:00 UTC, 1382 từ |
| 12 | niche | [#2304 /fsbo-leads](https://infina.ai/news/fsbo-leads/) FSBO Leads: How Agents Find and Convert Owner Sellers | `fsbo leads` 50 C | Wave 2 | Đã viết, scheduled 27/10 10:00 UTC, 1394 từ |
| 13 | niche | [#2328 /real-estate-open-house-sign-in-sheet](https://infina.ai/news/real-estate-open-house-sign-in-sheet/) Real Estate Open House Sign In Sheet: Free Template | `real estate open house sign in sheet` 500 C | Wave 2 | Đã viết, scheduled 26/10 14:00 UTC, 1216 từ |

### Inbound dự kiến từ bài đã có (làm sau mỗi wave)

| Bài đã có | Link tới (bài số trong bảng trên) |
|---|---|
| #2207 cold calling scripts | 3, 9 |
| #2195 prospecting letters | 3 |
| #2165 farming, #2201 door knocking | 4 |
| #1961 referral | 5 |
| #2171 open house ideas, #918 open house landing page | 13 |
| #1415 cost per lead | 1, 8, 10 |
| #1225 lead gen software | 8 |
| #1272 buyer nurture, #1317 financing readiness | 6 |
| #1223 pillar Cụm 7, #1825 pillar Cụm 9 | 1 |

### Không viết trong cụm này (đã thuộc bài khác)

`open house flyer` 5k (refresh #1967), cold calling và DNC (#2207), thư prospecting (#2195), door knocking (#2201), farming (#2165), Facebook lead ads (#1229),
`lead management system` (Cụm 2), landing page seller và home valuation (#942, #936, #1308).

**Cần bạn chốt:** làm cả 13 bài hay cắt (FSBO, motivated seller trước)? Một pillar + một sub-hub hay chỉ một pillar? Có làm bài Zillow không? Ngày bắt đầu (đề xuất 26/10).

---

## Bài News real estate chưa gắn cụm trong plan  (40 trang, 29,506 chữ)

| Vai trò | URL | IN | Chữ | Sửa lần cuối | FOCUS_KW đã log | Pillar bài trỏ lên | Post title |
|---|---|---|---|---|---|---|---|
| cluster | [#1140 /ai-citation-content-real-estate-agent-websites](https://infina.ai/news/ai-citation-content-real-estate-agent-websites/) | 3 | 746 | 2026-10-09 | `ai citation content real estate agent websites` | ↗ `best-chatbot-customer-service-real-estate` | A 50-Year Broker’s Advice on What Actually Gets an AI Citation |
| cluster | [#1415 /cost-per-lead-for-real-estate-agents](https://infina.ai/news/cost-per-lead-for-real-estate-agents/) | 3 | 1,083 | 2026-10-13 | – | ↗ `real-estate-lead-follow-up-automation-guide` | Cost Per Lead for Real Estate Agents: What Leads Really Cost |
| cluster | [#1106 /ai-assistant-instead-of-software-stack-real-estate-agents](https://infina.ai/news/ai-assistant-instead-of-software-stack-real-estate-agents/) | 2 | 808 | 2026-10-13 | `ai assistant instead of software stack real estate agents` | **❌ không** | Before You Buy Software Number 12, Ask Your AI Assistant to Replace It |
| cluster | [#390 /ai-isa-conversion-rates-real-estate](https://infina.ai/news/ai-isa-conversion-rates-real-estate/) | 2 | 660 | 2026-10-12 | `ai isa conversion rates real estate` | ↗ `best-chatbot-customer-service-real-estate` | AI ISAs Are Delivering 3x Higher Conversion Rates for Real Estate Teams |
| cluster | [#481 /ai-training-gap-for-real-estate-agents](https://infina.ai/news/ai-training-gap-for-real-estate-agents/) | 2 | 707 | 2026-10-12 | `ai training gap for real estate agents` | **❌ không** | 70% of Agents Want More AI Training: Here’s the Confidence Gap Behind That Number |
| cluster | [#1093 /ai-usage-without-measurable-impact-real-estate-agents](https://infina.ai/news/ai-usage-without-measurable-impact-real-estate-agents/) | 2 | 747 | 2026-10-09 | `ai usage without measurable impact real estate agents` | **❌ không** | 41% of Agents Use AI. Almost Half Say It Changed Nothing. |
| cluster | [#1152 /ai-video-marketing-automation-real-estate-agents](https://infina.ai/news/ai-video-marketing-automation-real-estate-agents/) | 2 | 720 | 2026-10-12 | `ai video marketing automation real estate agents` | ↗ `real-estate-marketing` | Keller Williams Just Gave Agents an AI Tool That Claims to Save 10 Hours a Week |
| cluster | [#461 /autonomous-ai-workforce-real-estate-teams](https://infina.ai/news/autonomous-ai-workforce-real-estate-teams/) | 2 | 704 | 2026-10-12 | `autonomous ai workforce real estate teams` | **❌ không** | Real Estate’s Next AI Shift: From Chatbots to an AI Workforce for Real Estate Teams |
| cluster | [#1609 /real-estate-ai-pricing-per-task](https://infina.ai/news/real-estate-ai-pricing-per-task/) | 2 | 1,337 | 2026-10-09 | `real estate ai pricing` | ↗ `real-estate-lead-follow-up-automation-guide` | Rechat’s AI Keeps Doing More Work. The Price Has Not Moved. |
| cluster | [#1128 /agentic-ai-risk-concerns-real-estate-brokerage-leaders](https://infina.ai/news/agentic-ai-risk-concerns-real-estate-brokerage-leaders/) | 1 | 729 | 2026-10-09 | `agentic ai risk concerns real estate brokerage leaders` | **❌ không** | Brokerage Leaders’ AI Worry Score Just Jumped, and Agentic AI Is Why |
| cluster | [#1203 /ai-academy-role-based-learning-mls-subscribers](https://infina.ai/news/ai-academy-role-based-learning-mls-subscribers/) | 1 | 713 | 2026-09-13 | `ai academy role based learning mls subscribers` | **❌ không** | Bright MLS Is Building an AI Academy for 100,000 Agents |
| cluster | [#1254 /ai-back-office-automation-real-estate-brokerages](https://infina.ai/news/ai-back-office-automation-real-estate-brokerages/) | 1 | 597 | 2026-10-12 | – | **❌ không** | 53% of Brokerages Now Plan AI for Back-Office Work, Up From 23% in 2024 |
| cluster | [#498 /ai-backoffice-transaction-management-real-estate](https://infina.ai/news/ai-backoffice-transaction-management-real-estate/) | 1 | 637 | 2026-10-12 | `ai backoffice transaction management real estate` | **❌ không** | Inside Real Estate’s ComplianceAI Shows Where Back Office AI Is Headed |
| cluster | [#1302 /ai-chief-of-staff-for-real-estate-agents](https://infina.ai/news/ai-chief-of-staff-for-real-estate-agents/) | 1 | 573 | 2026-09-24 | – | **❌ không** | SERHANT. Unveils Dot, an AI That Runs Agents’ Days Without Being Asked |
| cluster | [#1178 /ai-comparative-market-analysis-minutes-real-estate-agents](https://infina.ai/news/ai-comparative-market-analysis-minutes-real-estate-agents/) | 1 | 806 | 2026-10-12 | `ai comparative market analysis minutes real estate agents` | **❌ không** | Compass Says Its AI Just Cut CMA Prep From 90 Minutes to 15 |
| cluster | [#1209 /ai-contract-data-extraction-closing-automation-agents](https://infina.ai/news/ai-contract-data-extraction-closing-automation-agents/) | 1 | 751 | 2026-10-08 | `ai contract data extraction closing automation agents` | ↗ `best-crm-for-real-estate` | HomeSmart’s AI Now Reads a Contract and Automates the Closing Behind It |
| cluster | [#504 /ai-data-readiness-for-real-estate-brokerages](https://infina.ai/news/ai-data-readiness-for-real-estate-brokerages/) | 1 | 671 | 2026-10-12 | `ai data readiness for real estate brokerages` | **❌ không** | AI’s Impact on Real Estate Is Shrinking, and Bad Data Is Why |
| cluster | [#1020 /ai-deployment-maturity-real-estate-firms](https://infina.ai/news/ai-deployment-maturity-real-estate-firms/) | 1 | 1,132 | 2026-08-25 | `ai deployment maturity real estate firms` | **❌ không** | Only 9% of Real Estate Firms Have Actually Scaled Their AI, New Survey Finds |
| cluster | [#1165 /ai-digital-human-brokerage-website-adoption](https://infina.ai/news/ai-digital-human-brokerage-website-adoption/) | 1 | 825 | 2026-10-12 | `ai digital human brokerage website adoption` | **❌ không** | A Real Brokerage Just Put an AI Avatar Named Mae on Its Website |
| cluster | [#1529 /ai-drafted-messages-agent-approval](https://infina.ai/news/ai-drafted-messages-agent-approval/) | 1 | 1,032 | 2026-10-09 | `ai drafted messages agent approval` | ↗ `ai-intent-layer-for-real-estate-crm`, `real-estate-lead-follow-up-automation-guide`, `tcpa-compliance-for-real-estate-agents` | Realtor.com’s New AI Drafts the Message, Then Waits for You to Approve It |
| cluster | [#1034 /ai-flat-fee-brokerage-model-real-estate-agents](https://infina.ai/news/ai-flat-fee-brokerage-model-real-estate-agents/) | 1 | 875 | 2026-10-08 | `ai flat fee brokerage model real estate agents` | **❌ không** | TurboHome’s AI Hybrid Model Just Cut a Home Buying Commission by Thousands |
| cluster | [#1308 /ai-home-valuation-tool-real-estate-agent-website](https://infina.ai/news/ai-home-valuation-tool-real-estate-agent-website/) | 1 | 584 | 2026-10-09 | – | ↗ `best-chatbot-customer-service-real-estate` | 37% of Buyers Would Let AI Handle a Home Purchase With Minimal Human Help |
| cluster | [#513 /ai-job-substitution-risk-real-estate-agents](https://infina.ai/news/ai-job-substitution-risk-real-estate-agents/) | 1 | 757 | 2026-10-12 | `ai job substitution risk real estate agents` | ↗ `best-chatbot-customer-service-real-estate` | Harvard Study Puts a Number on AI’s Threat to Real Estate Agent Jobs |
| cluster | [#1296 /ai-likely-to-sell-alerts-real-estate-agents](https://infina.ai/news/ai-likely-to-sell-alerts-real-estate-agents/) | 1 | 531 | 2026-09-23 | – | **❌ không** | Compass Got 15,000 Agents to Generate 97,000 AI Conversations in Weeks |
| cluster | [#1335 /ai-listing-visualization-feature-real-estate-agents](https://infina.ai/news/ai-listing-visualization-feature-real-estate-agents/) | 1 | 509 | 2026-09-29 | – | **❌ không** | Interactive Room Visualization Is Driving Up to 170% More Showing Requests |
| cluster | [#1341 /ai-post-tour-follow-up-assistant-real-estate-crm](https://infina.ai/news/ai-post-tour-follow-up-assistant-real-estate-crm/) | 1 | 677 | 2026-10-09 | – | ↗ `ai-intent-layer-for-real-estate-crm` | A $4B AI Housing Startup Just Automated the Post-Tour Follow-Up Text |
| cluster | [#1290 /ai-powered-follow-up-messages-real-estate-agents](https://infina.ai/news/ai-powered-follow-up-messages-real-estate-agents/) | 1 | 534 | 2026-10-09 | – | ↗ `real-estate-lead-follow-up-automation-guide` | NAR’s 2026 Report Shows AI Use Climbing, but Concentrated in One Place |
| cluster | [#899 /ai-property-research-tools-real-estate-teams](https://infina.ai/news/ai-property-research-tools-real-estate-teams/) | 1 | 649 | 2026-10-12 | `ai property research tools real estate teams` | ↗ `best-crm-for-real-estate` | ATTOM’s New AI Agents Let You Ask Property Questions in Plain English |
| cluster | [#1284 /ai-relationship-manager-for-real-estate-leads](https://infina.ai/news/ai-relationship-manager-for-real-estate-leads/) | 1 | 569 | 2026-09-21 | – | ↗ `best-conversational-ai-chatbot-for-real-estate` | Real Brokerage’s Leo 2.0 Is Holding Hundreds of Conversations at Once |
| cluster | [#1134 /ai-visibility-reddit-seeding-backlash-real-estate-agents](https://infina.ai/news/ai-visibility-reddit-seeding-backlash-real-estate-agents/) | 1 | 775 | 2026-10-09 | `ai visibility reddit seeding backlash real estate agents` | ↗ `best-chatbot-customer-service-real-estate` | Agents Are Seeding Reddit to Win ChatGPT Recommendations, and Reddit Just Pushed Back |
| cluster | [#293 /answer-engine-optimization-for-real-estate-agents](https://infina.ai/news/answer-engine-optimization-for-real-estate-agents/) | 1 | 792 | 2026-10-08 | `answer engine optimization for real estate agents` | ↗ `best-chatbot-customer-service-real-estate` | Why 91% of Real Estate Agents Are Invisible to AI Search (And What to Do About It) |
| cluster | [#1191 /chatgpt-app-mortgage-matchup-real-estate-agent-visibility](https://infina.ai/news/chatgpt-app-mortgage-matchup-real-estate-agent-visibility/) | 1 | 768 | 2026-10-12 | `chatgpt app mortgage matchup real estate agent visibility` | ↗ `best-chatbot-customer-service-real-estate` | UWM’s New ChatGPT App Shows Where AI Search Is Headed for Agents Too |
| cluster | [#1158 /chatgpt-sycophantic-pricing-advice-real-estate-agents](https://infina.ai/news/chatgpt-sycophantic-pricing-advice-real-estate-agents/) | 1 | 867 | 2026-10-08 | `chatgpt sycophantic pricing advice real estate agents` | ↗ `best-chatbot-customer-service-real-estate` | Coldwell Banker’s CEO Just Called ChatGPT ‘Sycophantic’ About Home Prices |
| cluster | [#299 /declining-ai-trust-real-estate-agents](https://infina.ai/news/declining-ai-trust-real-estate-agents/) | 1 | 707 | 2026-10-12 | `declining ai trust real estate agents` | **❌ không** | Homebuyer Trust in AI Just Dropped 14 Points — What That Means for Real Estate Agents |
| cluster | [#528 /embedded-ai-real-estate-brokerage-platforms](https://infina.ai/news/embedded-ai-real-estate-brokerage-platforms/) | 1 | 673 | 2026-10-12 | `embedded ai real estate brokerage platforms` | ↗ `best-chatbot-customer-service-real-estate` | Lone Wolf Just Bet the Future of Real Estate AI Isn’t a Separate App |
| cluster | [#1317 /financing-readiness-signals-for-real-estate-buyer-leads](https://infina.ai/news/financing-readiness-signals-for-real-estate-buyer-leads/) | 1 | 535 | 2026-10-09 | – | ↗ `ai-intent-layer-for-real-estate-crm` | Down Payments Just Hit a Four-Year Q2 Low While Payments Jumped 74% |
| cluster | [#1266 /google-home-listing-ads-real-estate-agent-leads](https://infina.ai/news/google-home-listing-ads-real-estate-agent-leads/) | 1 | 580 | 2026-10-08 | – | ↗ `best-chatbot-customer-service-real-estate` | Google Just Took Home Listing Ads Nationwide, and Zillow Stock Dropped |
| cluster | [#1197 /mls-ai-conversational-search-broker-attribution-agents](https://infina.ai/news/mls-ai-conversational-search-broker-attribution-agents/) | 1 | 752 | 2026-10-12 | `mls ai conversational search broker attribution agents` | **❌ không** | Northwest MLS Just Launched an AI Home Search With Zero Ads and Zero Lead Forms |
| cluster | [#1243 /mortgage-rate-spike-real-estate-agent-response](https://infina.ai/news/mortgage-rate-spike-real-estate-agent-response/) | 1 | 557 | 2026-10-12 | – | ↗ `best-crm-for-real-estate` | Mortgage Rates Just Hit a 52-Week High: What It Means for Agent Response Times |
| cluster | [#286 /real-estate-ai-adoption-statistics-2026](https://infina.ai/news/real-estate-ai-adoption-statistics-2026/) | 1 | 837 | 2026-10-12 | `real estate ai adoption statistics 2026` | ↗ `best-chatbot-customer-service-real-estate` | Real Estate’s AI Holdouts Are Nearly Extinct: What the 2026 Adoption Data Means for Agents Still on the Fence |

## Ngoài chủ đề real estate (AI/tech)  (11 trang, 2,784 chữ)

| Vai trò | URL | IN | Chữ | Sửa lần cuối | FOCUS_KW đã log | Pillar bài trỏ lên | Post title |
|---|---|---|---|---|---|---|---|
| cluster | [#41 /ai-cannot-learn-while-it-works](https://infina.ai/news/ai-cannot-learn-while-it-works/) | 0 | 323 | 2026-07-31 | `ai cannot learn while it works` ⚠️ | **❌ không** | AI cannot learn while it works |
| cluster | [#31 /ai-just-moved-from-a-separate-tab-into-your-slack](https://infina.ai/news/ai-just-moved-from-a-separate-tab-into-your-slack/) | 0 | 191 | 2026-07-31 | `ai just moved from a separate tab into your slack` ⚠️ | **❌ không** | AI just moved from a separate tab into your Slack |
| cluster | [#34 /claude-code-has-500000-lines-of-code-only-1-6-of-it-is-actually-ai](https://infina.ai/news/claude-code-has-500000-lines-of-code-only-1-6-of-it-is-actually-ai/) | 0 | 469 | 2026-07-31 | `claude code has 500000 lines of code only 1 6 of it is actually ai` ⚠️ | **❌ không** | Claude Code has 500,000 lines of code. Only 1.6% of it is actually AI |
| cluster | [#50 /claude-code-just-shipped-artifacts](https://infina.ai/news/claude-code-just-shipped-artifacts/) | 0 | 66 | 2026-07-31 | `claude code just shipped artifacts` ⚠️ | **❌ không** | Claude Code just shipped Artifacts |
| cluster | [#14 /claude-fable-5-is-back](https://infina.ai/news/claude-fable-5-is-back/) | 0 | 195 | 2026-07-30 | `claude fable 5 is back` ⚠️ | **❌ không** | Claude Fable 5 is back |
| cluster | [#1 /genai-economy-first-revenue-number](https://infina.ai/news/genai-economy-first-revenue-number/) | 0 | 292 | 2026-08-17 | `genai economy first revenue number` ⚠️ | **❌ không** | The GenAI economy just got its first real revenue number |
| cluster | [#53 /is-openai-in-trouble](https://infina.ai/news/is-openai-in-trouble/) | 0 | 89 | 2026-07-31 | `is openai in trouble` ⚠️ | **❌ không** | Is OpenAI in trouble? |
| cluster | [#44 /microsoft-just-sent-6000-engineers-into-enterprise-buildings](https://infina.ai/news/microsoft-just-sent-6000-engineers-into-enterprise-buildings/) | 0 | 314 | 2026-07-31 | `microsoft just sent 6000 engineers into enterprise buildings` ⚠️ | **❌ không** | Microsoft just sent 6,000 engineers into enterprise buildings |
| cluster | [#47 /most-ai-tools-stop-working-when-you-close-your-laptop](https://infina.ai/news/most-ai-tools-stop-working-when-you-close-your-laptop/) | 0 | 354 | 2026-07-31 | `most ai tools stop working when you close your laptop` ⚠️ | **❌ không** | Most AI tools stop working when you close your laptop |
| cluster | [#37 /the-u-s-governments-reported-ban-on-foreign-access-to-anthropics-models](https://infina.ai/news/the-u-s-governments-reported-ban-on-foreign-access-to-anthropics-models/) | 0 | 84 | 2026-07-31 | `the u s governments reported ban on foreign access to anthropics models` ⚠️ | **❌ không** | The U.S. government’s reported ban on foreign access to Anthropic’s models |
| cluster | [#26 /yc-spring-2026-the-agent-economy-has-actuaries-now](https://infina.ai/news/yc-spring-2026-the-agent-economy-has-actuaries-now/) | 0 | 407 | 2026-07-31 | `yc spring 2026 the agent economy has actuaries now` ⚠️ | **❌ không** | YC Spring 2026: The Agent Economy Has Actuaries Now |

---

## Phụ lục: 12 stub 301

Đây vẫn là 12 post thật trong WordPress nhưng trang của chúng trả 301 chứ không phải 200 (đã kiểm lại bằng HTTP ngày 2026-10-23, cả 12
đều còn 301), nên không tính vào 166 bài ở trên.

**Cả 12 đều đang ở IN = 0, tức là không còn bài nào trỏ vào slug cũ nữa.** Đây là kết quả của đợt
sửa 02/10, lúc đó phát hiện #1026, #1184 và #1329 còn link qua slug stub và đã đổi sang trỏ thẳng.
Nghĩa là 12 redirect này hiện chỉ còn phục vụ link từ bên ngoài site và backlink cũ, không phục vụ
link nội bộ nào. Cũng vì vậy cột IN của 166 bài ở trên không có dòng nào ghi "qua stub".

| URL stub | IN (vẫn còn bài trỏ vào) | Redirect 301 tới | Chữ còn lại |
|---|---|---|---|
| [#99 /best-ai-chat-platform-real-estate](https://infina.ai/news/best-ai-chat-platform-real-estate/) | 0 | `best-chatbot-customer-service-real-estate` | 48 |
| [#58 /best-ai-chatbot-for-real-estate-lead-capture](https://infina.ai/news/best-ai-chatbot-for-real-estate-lead-capture/) | 0 | `best-chatbot-customer-service-real-estate` | 53 |
| [#1069 /best-ai-conversational-bot-for-real-estate](https://infina.ai/news/best-ai-conversational-bot-for-real-estate/) | 0 | `best-conversational-ai-chatbot-for-real-estate` | 52 |
| [#1063 /best-conversational-chatbot-for-real-estate](https://infina.ai/news/best-conversational-chatbot-for-real-estate/) | 0 | `best-conversational-ai-chatbot-for-real-estate` | 68 |
| [#384 /best-crm-software-real-estate-agents](https://infina.ai/news/best-crm-software-real-estate-agents/) | 0 | `best-crm-for-real-estate` | 49 |
| [#649 /best-idx-website-for-realtors](https://infina.ai/news/best-idx-website-for-realtors/) | 0 | `idx-website-for-realtors` | 44 |
| [#553 /best-real-estate-website-builder](https://infina.ai/news/best-real-estate-website-builder/) | 0 | `real-estate-website-builder` | 48 |
| [#196 /conversational-chat-real-estate](https://infina.ai/news/conversational-chat-real-estate/) | 0 | `what-is-a-conversational-chatbot-real-estate` | 57 |
| [#1076 /no-code-chatbot-platform-real-estate](https://infina.ai/news/no-code-chatbot-platform-real-estate/) | 0 | `best-chatbot-builder-real-estate` | 46 |
| [#637 /real-estate-website-builder-with-idx](https://infina.ai/news/real-estate-website-builder-with-idx/) | 0 | `real-estate-website-builder` | 74 |
| [#987 /realtor-website-design](https://infina.ai/news/realtor-website-design/) | 0 | `website-design-for-real-estate-agents` | 47 |
| [#412 /top-crm-tools-for-real-estate-teams](https://infina.ai/news/top-crm-tools-for-real-estate-teams/) | 0 | `best-crm-for-real-estate` | 36 |
