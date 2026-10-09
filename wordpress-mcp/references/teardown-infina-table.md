# infina.ai/news: bảng mảng nội dung, mỗi URL một dòng

Crawl 2026-10-09 qua WP REST API. **147 bài publish, 135 bài thật** (12 stub 301 tách riêng ở cuối
file). Không có bài draft/scheduled/pending nào tại thời điểm crawl.

Cùng format với `teardown-followupboss-table.md` để đặt cạnh nhau mà so. Kết luận chiến lược của
đối thủ ở `teardown-followupboss.md`, phương pháp ở `competitor-pillar-teardown.md`. File này là dữ
liệu thô của **site mình**, dạng bảng để tự soi.

## Đọc bảng này thế nào

| Cột | Nghĩa |
|---|---|
| Vai trò | Lấy nguyên nhãn trong `content-plan.md`. `PILLAR` in đậm. Bài không có trong plan để trống thành `cluster` |
| URL | `#ID` là post ID trong WordPress, dùng thẳng được với `update_post` |
| IN | Số **bài khác** trỏ vào, đếm trong thân bài. Link đi qua stub 301 đã quy về đích thật và ghi rõ `(n qua stub)` |
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

**2. 52 bài không nằm trong bảng cụm nào của plan.** Đây không phải lỗi crawl. `content-plan.md` tự
khai ngay dòng đầu là nó chỉ bao 86 bài evergreen và **loại bài News ra khỏi phạm vi**. Nên 40 bài
News real estate và 11 bài AI/tech nằm ngoài 8 cụm là đúng thiết kế của plan, không phải thiếu sót
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
`used-keywords.md`, tức là một file ghi tay. Hệ quả: **118/135 bài có keyword log, 17 bài không có**,
và trong 118 bài đó **13 bài ghi nguồn là "suy đoán từ slug"** chứ không phải lấy từ tracker. Dùng
cột này để khoanh vùng chủ đề, đừng dùng làm bằng chứng về cái gì đang set thật trong Rank Math.

**6. Cột IN của site mình sạch hơn cột IN của FUB, vì lý do kỹ thuật.** Với FUB mình phải trừ tay 3
link template. Ở đây `content.rendered` chỉ trả về thân bài, menu và footer của theme không lọt vào,
nên không có gì phải trừ. Đổi lại con số sẽ **thấp hơn** số link thật mà người đọc nhìn thấy trên
trang, vì thiếu phần điều hướng của theme.

**7. Số chữ lệch 1-3% so với vài con số đã ghi trong `content-plan.md`.** Ví dụ `#1529` ở đây là
1.031 còn plan ghi 1.019, `#89` ở đây 3.888 còn plan ghi 3.991. Nguyên nhân là cách bóc thẻ khác
nhau, chỗ thì tính chữ trong bảng và caption, chỗ thì không. Dùng để so tương đối giữa các bài trong
chính file này thì được, đừng dùng để cãi nhau với số trong file khác.

**8. Dash trong cột Post title là chữ của bài, giữ nguyên.** Có đúng 1 bài còn em dash trong tiêu đề
là `#299`. Quy tắc không dùng dash áp cho bài mình viết mới, không áp cho việc trích lại tiêu đề đang
có. Dòng này là để biết mà đi sửa, không phải để sửa trong bảng.

## Tóm tắt 10 nhóm


| Cụm | Trang | Pillar | Tổng chữ | Mồ côi | Không trỏ pillar nào | Thiếu FOCUS_KW |
|---|---|---|---|---|---|---|
| Cụm 1: Chatbot / Conversational AI | 13 | `best-chatbot-customer-service-real-estate` (26 IN, 3,888 chữ); `best-conversational-ai-chatbot-for-real-estate` (9 IN, 2,993 chữ) | 20,922 | 0 | 0 | 0 |
| Cụm 2: CRM Software | 25 | `best-crm-for-real-estate` (52 IN, 4,287 chữ); `ai-intent-layer-for-real-estate-crm` (13 IN, 742 chữ) | 31,549 | 0 | 0 | 2 |
| Cụm 3: Website Builder / IDX | 13 | `real-estate-website-builder` (25 IN, 2,985 chữ) | 15,113 | 0 | 0 | 0 |
| Cụm 4: AI Voice / Virtual Assistant / Receptionist | 6 | `best-ai-voice-assistants-for-real-estate` (11 IN, 2,219 chữ) | 7,195 | 0 | 0 | 0 |
| Cụm 5: Website / Web Design | 6 | `website-design-for-real-estate-agents` (5 IN, 1,799 chữ) | 6,805 | 0 | 0 | 0 |
| Cụm 6: Landing Pages | 6 | `real-estate-landing-page-guide` (5 IN, 1,873 chữ) | 8,316 | 0 | 0 | 0 |
| Cụm 7: Lead Generation / Follow-up Automation | 9 | `real-estate-lead-follow-up-automation-guide` (17 IN, 2,453 chữ) | 8,208 | 0 | 0 | 2 |
| Cụm 8: Compliance / Legal / Risk | 6 | `tcpa-compliance-for-real-estate-agents` (15 IN, 1,904 chữ) | 6,017 | 0 | 0 | 1 |
| Bài News real estate chưa gắn cụm trong plan | 40 | không có | 29,224 | 0 | 19 | 12 |
| Ngoài chủ đề real estate (AI/tech) | 11 | không có | 2,780 | 11 | 11 | 0 |

**Ba thứ đáng nhìn nhất trong bảng tóm tắt này.**

**Cột "Không trỏ pillar nào" là cột đau nhất.** 8 cụm trong plan đều sạch: 0 bài nào không trỏ lên
pillar. Nhưng nhóm News 40 bài thì có **19 bài không trỏ lên bất kỳ pillar nào**, và nhóm AI/tech
thì cả 11 bài đều vậy. Nghĩa là việc sửa link nội bộ từ trước tới giờ mới chỉ chạm tới phần nằm
trong plan, còn gần nửa số bài News thì chưa.

**Cột "Mồ côi" giờ chỉ còn đúng 11 bài AI/tech.** Toàn bộ 8 cụm và cả 40 bài News đều đã có ít nhất
1 link vào, sau đợt vá mồ côi ngày 09/10. 11 bài còn lại không sửa được bằng link vì chúng không
thuộc chủ đề nào của site.

**Pillar nhẹ `ai-intent-layer-for-real-estate-crm` đang gánh 13 link vào với 742 chữ.** Nó có 7 thẻ
H2 trên 10 đoạn văn, tức là gần như mỗi H2 chỉ có 1 đoạn. Đây là pillar mỏng nhất site, và nó lại
đang nhận nhiều link hơn 6 trong 10 pillar còn lại. So để thấy: pillar Cụm 2 chính có 52 link vào và
4.287 chữ.

---


## Cụm 1: Chatbot / Conversational AI  (13 trang, 20,922 chữ)

| Vai trò | URL | IN | Chữ | Sửa lần cuối | FOCUS_KW đã log | Pillar bài trỏ lên | Post title |
|---|---|---|---|---|---|---|---|
| **Pillar B** | [#89 /best-chatbot-customer-service-real-estate](https://infina.ai/news/best-chatbot-customer-service-real-estate/) | 26 | 3,888 | 2026-10-08 | `chatbot customer service real estate` | *(là pillar)* | 15 Best Chatbot Customer Service Tools for Real Estate Teams (2026) |
| So sánh | [#123 /chatbot-vs-conversational-ai-real-estate](https://infina.ai/news/chatbot-vs-conversational-ai-real-estate/) | 10 | 1,697 | 2026-10-08 | `chatbot vs conversational ai real estate` | ✅ `best-chatbot-customer-service-real-estate`, `best-conversational-ai-chatbot-for-real-estate`; ↗ `best-ai-voice-assistants-for-real-estate` | Chatbot vs Conversational AI: What’s the Difference and Which Does Real Estate Need? |
| **Pillar A** | [#1056 /best-conversational-ai-chatbot-for-real-estate](https://infina.ai/news/best-conversational-ai-chatbot-for-real-estate/) | 9 | 2,993 | 2026-10-08 | `best conversational ai chatbot for real estate` | *(là pillar)* | Best Conversational AI Chatbots for Real Estate Agents in 2026 |
| Định nghĩa (HUB) | [#172 /what-is-a-conversational-chatbot-real-estate](https://infina.ai/news/what-is-a-conversational-chatbot-real-estate/) | 9 | 1,428 | 2026-10-09 | `conversational chatbot` | ✅ `best-chatbot-customer-service-real-estate`, `best-conversational-ai-chatbot-for-real-estate` | What Is a Conversational Chatbot? A Real Estate Agent’s Guide (2026) |
| Review/list (HUB) | [#117 /best-chatbot-builder-real-estate](https://infina.ai/news/best-chatbot-builder-real-estate/) | 7 | 2,469 | 2026-10-08 | `chatbot builder real estate` | ✅ `best-chatbot-customer-service-real-estate`, `best-conversational-ai-chatbot-for-real-estate`; ↗ `best-ai-voice-assistants-for-real-estate` | 10 Best Chatbot Builders for Real Estate Agents in 2026 |
| So sánh | [#138 /gohighlevel-chatbot-vs-dedicated-real-estate-chatbot](https://infina.ai/news/gohighlevel-chatbot-vs-dedicated-real-estate-chatbot/) | 7 | 1,522 | 2026-10-08 | `gohighlevel chatbot` | ✅ `best-chatbot-customer-service-real-estate`, `best-conversational-ai-chatbot-for-real-estate`; ↗ `best-ai-voice-assistants-for-real-estate` | GoHighLevel Chatbot vs Dedicated Real Estate Chatbots: Which Does Your Team Actually Need? |
| So sánh/thay thế | [#189 /zendesk-sunshine-conversations-alternative-real-estate](https://infina.ai/news/zendesk-sunshine-conversations-alternative-real-estate/) | 5 | 1,050 | 2026-10-08 | `zendesk sunshine conversations alternative` | ✅ `best-chatbot-customer-service-real-estate` | Zendesk Sunshine Conversations Alternative for Real Estate Chatbots (2026) |
| Hỗ trợ (News) | [#1146 /ai-chatbot-mls-data-security-risk-brokerages](https://infina.ai/news/ai-chatbot-mls-data-security-risk-brokerages/) | 4 | 777 | 2026-10-01 | `ai chatbot mls data security risk brokerages` | ✅ `best-chatbot-customer-service-real-estate` | A CRMLS Test Shows How Easily an AI Chatbot Can Leak Your MLS Data |
| So sánh | [#1071 /ai-chat-vs-sms-real-estate](https://infina.ai/news/ai-chat-vs-sms-real-estate/) | 2 | 1,334 | 2026-10-08 | `ai chat vs sms real estate` | ✅ `best-chatbot-customer-service-real-estate`, `best-conversational-ai-chatbot-for-real-estate` | AI Chat vs SMS Follow-Up for Real Estate: Which Converts More Leads? |
| Hỗ trợ (News) | [#1114 /ai-chatbot-mortgage-document-errors-real-estate-agents](https://infina.ai/news/ai-chatbot-mortgage-document-errors-real-estate-agents/) | 2 | 786 | 2026-10-01 | `ai chatbot mortgage document errors real estate agents` | ✅ `best-conversational-ai-chatbot-for-real-estate` | A New Study Found AI Got 1 in 4 Mortgage Document Checks Wrong |
| Hỗ trợ (News) | [#1050 /ai-disclosure-rules-for-real-estate-chatbots](https://infina.ai/news/ai-disclosure-rules-for-real-estate-chatbots/) | 2 | 888 | 2026-10-01 | `ai disclosure rules for real estate chatbots` | ✅ `best-chatbot-customer-service-real-estate` | EU AI Act Disclosure Rules Are Already Changing Your Real Estate Chatbot |
| So sánh | [#1078 /chatbot-vs-live-agent-real-estate](https://infina.ai/news/chatbot-vs-live-agent-real-estate/) | 2 | 1,329 | 2026-10-08 | `chatbot vs live agent real estate` | ✅ `best-chatbot-customer-service-real-estate` | Chatbot vs Live Agent for Real Estate: Response Time and Conversion Compared |
| Hỗ trợ (News) | [#1100 /real-estate-chatbot-that-reads-listing-photos](https://infina.ai/news/real-estate-chatbot-that-reads-listing-photos/) | 2 | 761 | 2026-10-09 | `real estate chatbot that reads listing photos` | ✅ `best-chatbot-customer-service-real-estate`, `best-conversational-ai-chatbot-for-real-estate` | This Chatbot Reads Your Listing Photos to Stop 47 Calls a Week |

## Cụm 2: CRM Software  (25 trang, 31,549 chữ)

| Vai trò | URL | IN | Chữ | Sửa lần cuối | FOCUS_KW đã log | Pillar bài trỏ lên | Post title |
|---|---|---|---|---|---|---|---|
| **Pillar chính (ĐÃ ĐỔI 01/10)** | [#207 /best-crm-for-real-estate](https://infina.ai/news/best-crm-for-real-estate/) | 52 | 4,287 | 2026-10-08 | `best crm for real estate` | *(là pillar)* | Best Real Estate Agent CRM Software in 2026 (Compared) |
| Định nghĩa (khác góc) | [#214 /ai-crm-real-estate](https://infina.ai/news/ai-crm-real-estate/) | 22 | 1,700 | 2026-10-08 | `ai crm` | ✅ `ai-intent-layer-for-real-estate-crm`, `best-crm-for-real-estate`; ↗ `best-chatbot-customer-service-real-estate` | AI CRM for Real Estate: How Agents Use AI to Convert More Leads (2026) |
| **Pillar nhẹ (RealSaleX)** | [#1232 /ai-intent-layer-for-real-estate-crm](https://infina.ai/news/ai-intent-layer-for-real-estate-crm/) | 13 | 742 | 2026-10-07 | `ai intent layer for real estate crm` | *(là pillar)* | AI Intent Layer for Real Estate CRM: What It Adds |
| Sub-topic: pipeline | [#277 /crm-pipeline-management](https://infina.ai/news/crm-pipeline-management/) | 12 | 1,674 | 2026-10-07 | `crm pipeline` | ✅ `best-crm-for-real-estate` | CRM Pipeline Management: Build a Sales Pipeline That Actually Closes |
| Sub-topic: marketing (strategy) | [#263 /crm-marketing-real-estate](https://infina.ai/news/crm-marketing-real-estate/) | 9 | 1,350 | 2026-10-01 | `crm marketing` | ✅ `best-crm-for-real-estate` | CRM Marketing for Real Estate: How to Turn Your Database into a Deal Machine |
| Định nghĩa (beginner) | [#405 /crm-management-real-estate-agents-beginners-guide](https://infina.ai/news/crm-management-real-estate-agents-beginners-guide/) | 6 | 1,145 | 2026-10-07 | `crm management` | ✅ `best-crm-for-real-estate` | CRM Software 101: A Beginner’s Guide for Real Estate Agents |
| Review (brand cụ thể)  RealSaleX | [#1449 /follow-up-boss-real-estate-crm](https://infina.ai/news/follow-up-boss-real-estate-crm/) | 6 | 1,534 | 2026-10-08 | `follow up boss real estate crm` | ✅ `ai-intent-layer-for-real-estate-crm`, `best-crm-for-real-estate`; ↗ `real-estate-lead-follow-up-automation-guide` | Follow Up Boss Real Estate CRM Review: Pricing, Features, and the Follow-Up Gap |
| Review/list (niche: teams) | [#419 /best-crm-for-real-estate-teams-2026](https://infina.ai/news/best-crm-for-real-estate-teams-2026/) | 5 | 1,191 | 2026-10-04 | `best crm for real estate teams 2026` ⚠️ | ✅ `best-crm-for-real-estate` | Best CRM for Real Estate Teams: Top Picks for 2026 |
| Hỗ trợ (News) | [#1026 /ai-agent-integration-for-real-estate-crm-platforms](https://infina.ai/news/ai-agent-integration-for-real-estate-crm-platforms/) | 4 | 868 | 2026-10-02 | `ai agent integration for real estate crm platforms` | ✅ `ai-intent-layer-for-real-estate-crm`, `best-crm-for-real-estate` | Rechat Just Let Claude and ChatGPT Run Real Estate CRM Workflows Directly |
| Buying guide (BOF) | [#444 /best-crm-buying-guide-real-estate-agents](https://infina.ai/news/best-crm-buying-guide-real-estate-agents/) | 4 | 1,123 | 2026-08-11 | `best crm` | ✅ `best-crm-for-real-estate` | Best CRM for Real Estate Agents: A Buyer’s Guide (2026) |
| Định nghĩa (niche RE) | [#1458 /what-does-crm-mean-in-real-estate](https://infina.ai/news/what-does-crm-mean-in-real-estate/) | 4 | 1,130 | 2026-10-08 | `what does crm mean in real estate` | ✅ `best-crm-for-real-estate` | What Does CRM Mean in Real Estate? A Plain-English Guide for Agents |
| Định nghĩa | [#230 /what-is-crm-software](https://infina.ai/news/what-is-crm-software/) | 4 | 1,604 | 2026-10-03 | `what is crm software` | ✅ `best-crm-for-real-estate` | What Is CRM Software? Complete Guide for Businesses in 2026 |
| So sánh (MOF)  RealSaleX | [#1487 /customer-engagement-platform-vs-crm](https://infina.ai/news/customer-engagement-platform-vs-crm/) | 3 | 1,338 | 2026-10-08 | `customer engagement platform vs crm` | ✅ `ai-intent-layer-for-real-estate-crm`, `best-crm-for-real-estate`; ↗ `real-estate-lead-follow-up-automation-guide`, `tcpa-compliance-for-real-estate-agents` | Customer Engagement Platform vs CRM for Real Estate: Where Each One Stops |
| Review/list (niche: broker) | [#1462 /real-estate-broker-crm](https://infina.ai/news/real-estate-broker-crm/) | 3 | 1,580 | 2026-10-09 | `real estate broker crm` | ✅ `ai-intent-layer-for-real-estate-crm`, `best-crm-for-real-estate`; ↗ `real-estate-lead-follow-up-automation-guide`, `tcpa-compliance-for-real-estate-agents` | Real Estate Broker CRM: What Brokerages Need That Agent CRMs Miss |
| Review/list (niche: free) | [#438 /best-free-crm-for-real-estate-agents](https://infina.ai/news/best-free-crm-for-real-estate-agents/) | 2 | 1,175 | 2026-10-08 | `free crm for real estate` | ✅ `best-crm-for-real-estate` | Best Free CRM for Real Estate Agents in 2026 |
| Review (brand cụ thể)  RealSaleX | [#1234 /cinc-crm-review-real-estate](https://infina.ai/news/cinc-crm-review-real-estate/) | 2 | 607 | 2026-10-02 | `cinc crm review` | ✅ `ai-intent-layer-for-real-estate-crm`, `best-crm-for-real-estate` | CINC CRM Review: Pricing, Features, and Buyer Follow-Up Gaps |
| Sub-topic: marketing (định nghĩa) | [#450 /crm-marketing-software-real-estate-guide](https://infina.ai/news/crm-marketing-software-real-estate-guide/) | 2 | 985 | 2026-08-11 | `crm marketing software` | ✅ `best-crm-for-real-estate` | What Is CRM Marketing Software? A Guide for Real Estate Teams |
| Bridge → Cụm 3 | [#585 /crm-with-website-builder-real-estate](https://infina.ai/news/crm-with-website-builder-real-estate/) | 2 | 1,149 | 2026-10-08 | `crm with website builder` | ✅ `best-crm-for-real-estate`; ↗ `real-estate-website-builder` | CRM with Website Builder: Best Integrated Platforms for Real Estate Teams |
| Hỗ trợ (News) | [#1171 /ai-crm-assistant-brokerage-merger-rollout-agents](https://infina.ai/news/ai-crm-assistant-brokerage-merger-rollout-agents/) | 1 | 861 | 2026-10-02 | `ai crm assistant brokerage merger rollout agents` | ✅ `ai-intent-layer-for-real-estate-crm` | Real’s AI CRM Assistant Leo Is About to Meet 180,000 New RE/MAX Agents |
| Hỗ trợ (News) | [#1323 /arm-borrower-tracking-real-estate-agent-crm](https://infina.ai/news/arm-borrower-tracking-real-estate-agent-crm/) | 1 | 570 | 2026-10-02 | – | ✅ `best-crm-for-real-estate` | Nearly 10% of Borrowers Are Now Choosing ARMs as Rates Top 7% |
| cluster (thiếu ở bảng plan) | [#247 /crm-for-real-estate-agents](https://infina.ai/news/crm-for-real-estate-agents/) | 1 | 1,704 | 2026-08-10 | `crm for real estate agents` ⚠️ | ✅ `best-crm-for-real-estate` | CRM for Real Estate Agents: How to Choose the Right One in 2026 |
| Hỗ trợ (News) | [#1184 /exp-nexus-crm-software-cost-reduction-agents](https://infina.ai/news/exp-nexus-crm-software-cost-reduction-agents/) | 1 | 741 | 2026-10-02 | `exp nexus crm software cost reduction agents` | ✅ `best-crm-for-real-estate` | eXp Realty Says Its All-in-One AI Platform Cuts Software Costs by 70% |
| Hỗ trợ (News) | [#1329 /open-ai-protocol-real-estate-crm-brokerages](https://infina.ai/news/open-ai-protocol-real-estate-crm-brokerages/) | 1 | 558 | 2026-10-02 | – | ✅ `ai-intent-layer-for-real-estate-crm`, `best-crm-for-real-estate` | Lofty Launches an MCP Server So Any AI Can Plug Into Its CRM |
| Bridge → Cụm 3 | [#643 /real-estate-crm-with-idx](https://infina.ai/news/real-estate-crm-with-idx/) | 1 | 752 | 2026-10-08 | `real estate crm with idx` | ✅ `best-crm-for-real-estate`; ↗ `real-estate-website-builder` | Real Estate CRM with IDX Integration: Best Platforms in 2026 |
| Listicle chiến lược (TOF)  RealSaleX | [#1488 /real-estate-customer-engagement-strategies](https://infina.ai/news/real-estate-customer-engagement-strategies/) | 1 | 1,181 | 2026-10-06 | `real estate customer engagement` | ✅ `ai-intent-layer-for-real-estate-crm`, `best-crm-for-real-estate`; ↗ `real-estate-lead-follow-up-automation-guide`, `tcpa-compliance-for-real-estate-agents` | Real Estate Customer Engagement: 7 Tactics That Earn a Reply |

## Cụm 3: Website Builder / IDX  (13 trang, 15,113 chữ)

| Vai trò | URL | IN | Chữ | Sửa lần cuối | FOCUS_KW đã log | Pillar bài trỏ lên | Post title |
|---|---|---|---|---|---|---|---|
| **Pillar** | [#546 /real-estate-website-builder](https://infina.ai/news/real-estate-website-builder/) | 25 | 2,985 | 2026-10-08 | `real estate website builder` | *(là pillar)* | Best Real Estate Website Builders for Agents and Brokers (2026) |
| Định nghĩa (broker) | [#598 /broker-idx-guide](https://infina.ai/news/broker-idx-guide/) | 9 | 2,328 | 2026-10-08 | `broker idx` | ✅ `real-estate-website-builder`; ↗ `best-crm-for-real-estate` | What Is Broker IDX? Complete Guide for Real Estate Agents (2026) |
| Review/list (roundup, HUB) | [#610 /idx-website-for-realtors](https://infina.ai/news/idx-website-for-realtors/) | 8 | 834 | 2026-10-08 | `idx website for realtors` | ✅ `real-estate-website-builder`; ↗ `best-crm-for-real-estate` | Best IDX Website for Realtors: Top Platforms Reviewed (2026) |
| How-to (kỹ thuật) | [#622 /idx-mls-real-estate-guide](https://infina.ai/news/idx-mls-real-estate-guide/) | 3 | 781 | 2026-10-09 | `idx mls` | ✅ `real-estate-website-builder`; ↗ `best-crm-for-real-estate` | IDX MLS: How the Data Feed Powers Real Estate Agent Websites |
| Review (niche: solo agent) | [#567 /real-estate-agent-website-builder](https://infina.ai/news/real-estate-agent-website-builder/) | 3 | 1,155 | 2026-10-08 | `real estate agent website builder` | ✅ `real-estate-website-builder`; ↗ `best-crm-for-real-estate` | Best Real Estate Agent Website Builder for Solo Agents in 2026 |
| Review (niche: realtor) | [#561 /best-website-builder-for-realtors](https://infina.ai/news/best-website-builder-for-realtors/) | 2 | 1,011 | 2026-10-08 | `best website builder for realtors` | ✅ `real-estate-website-builder`; ↗ `best-crm-for-real-estate` | Best Website Builder for Realtors: Top Picks Reviewed (2026) |
| How-to (kỹ thuật) | [#631 /idx-feed-real-estate-setup](https://infina.ai/news/idx-feed-real-estate-setup/) | 2 | 688 | 2026-10-08 | `idx feed` | ✅ `real-estate-website-builder`; ↗ `best-crm-for-real-estate` | IDX Feed: What It Is and How to Set It Up on Your Website |
| Định nghĩa (chung) | [#604 /idx-real-estate-definition-guide](https://infina.ai/news/idx-real-estate-definition-guide/) | 2 | 987 | 2026-10-08 | `idx real estate` | ✅ `real-estate-website-builder`; ↗ `best-crm-for-real-estate` | What Is IDX in Real Estate? Definition, Setup, and How It Works |
| Examples/inspiration | [#616 /idx-real-estate-websites-examples](https://infina.ai/news/idx-real-estate-websites-examples/) | 2 | 723 | 2026-10-08 | `idx real estate websites` | ✅ `real-estate-website-builder`; ↗ `best-crm-for-real-estate` | IDX Real Estate Websites: Best Examples and What Makes Them Work |
| Buying guide | [#655 /real-estate-agent-websites-with-idx](https://infina.ai/news/real-estate-agent-websites-with-idx/) | 2 | 673 | 2026-10-08 | `real estate agent websites with idx` | ✅ `real-estate-website-builder`; ↗ `best-crm-for-real-estate` | Real Estate Agent Websites with IDX: What to Look For Before You Buy |
| Review (niche: investor) | [#579 /best-website-builder-real-estate-investors](https://infina.ai/news/best-website-builder-real-estate-investors/) | 1 | 997 | 2026-10-08 | `best website builder for real estate investors` | ✅ `real-estate-website-builder`; ↗ `best-crm-for-real-estate` | Best Website Builder for Real Estate Investors in 2026 |
| Review (niche: free) | [#573 /free-real-estate-website-builder](https://infina.ai/news/free-real-estate-website-builder/) | 1 | 1,093 | 2026-10-08 | `free real estate website builder` | ✅ `real-estate-website-builder`; ↗ `best-crm-for-real-estate` | Free Real Estate Website Builder: What You Get vs. What You Pay For |
| Hỗ trợ (News) | [#1473 /off-mls-listings-on-agent-idx-websites](https://infina.ai/news/off-mls-listings-on-agent-idx-websites/) | 1 | 858 | 2026-10-03 | `off mls listings on agent idx websites` | ✅ `real-estate-website-builder` | Compass Gave an MLS Until October 6, and Agent Search Sites Are Caught in the Middle |

## Cụm 4: AI Voice / Virtual Assistant / Receptionist  (6 trang, 7,195 chữ)

| Vai trò | URL | IN | Chữ | Sửa lần cuối | FOCUS_KW đã log | Pillar bài trỏ lên | Post title |
|---|---|---|---|---|---|---|---|
| **Pillar** (refresh #147) | [#147 /best-ai-voice-assistants-for-real-estate](https://infina.ai/news/best-ai-voice-assistants-for-real-estate/) | 11 | 2,219 | 2026-10-02 | `ai voice assistants for real estate` | *(là pillar)* | 7 Best AI Voice Assistants for Real Estate Agents in 2026 |
| Review/list (phát hiện thêm 01/10) | [#110 /best-ai-virtual-assistant-real-estate](https://infina.ai/news/best-ai-virtual-assistant-real-estate/) | 7 | 1,771 | 2026-10-08 | `ai virtual assistant real estate` | ✅ `best-ai-voice-assistants-for-real-estate`; ↗ `best-chatbot-customer-service-real-estate` | 7 Best AI Virtual Assistants for Real Estate Agents in 2026 |
| Support/how-to → bắc cầu Cụm 7 | [#1213 /ai-outbound-calling-real-estate-lead-follow-up](https://infina.ai/news/ai-outbound-calling-real-estate-lead-follow-up/) | 5 | 914 | 2026-10-09 | `ai outbound calling real estate lead follow up` | ✅ `best-ai-voice-assistants-for-real-estate`; ↗ `tcpa-compliance-for-real-estate-agents` | AI Outbound Calling for Real Estate: How It Works in 2026 |
| So sánh | [#1217 /ai-receptionist-vs-human-receptionist-real-estate](https://infina.ai/news/ai-receptionist-vs-human-receptionist-real-estate/) | 2 | 709 | 2026-09-15 | `ai receptionist vs human receptionist real estate` | ✅ `best-ai-voice-assistants-for-real-estate`; ↗ `tcpa-compliance-for-real-estate-agents` | AI Receptionist vs Human Receptionist for Real Estate: Cost & ROI |
| Buying guide | [#1219 /ai-answering-service-for-real-estate](https://infina.ai/news/ai-answering-service-for-real-estate/) | 1 | 686 | 2026-09-15 | `ai answering service for real estate` | ✅ `best-ai-voice-assistants-for-real-estate`; ↗ `tcpa-compliance-for-real-estate-agents` | AI Answering Service for Real Estate: How to Choose the Right One |
| Hỗ trợ (News) | [#1467 /ai-voice-calls-for-listing-price-updates](https://infina.ai/news/ai-voice-calls-for-listing-price-updates/) | 1 | 896 | 2026-10-02 | `ai voice calls for listing price updates` | ✅ `best-ai-voice-assistants-for-real-estate`; ↗ `tcpa-compliance-for-real-estate-agents` | Nearly 1 in 5 Homes Cut Price in September, and Agents Are Running Out of Call Hours |

## Cụm 5: Website / Web Design  (6 trang, 6,805 chữ)

| Vai trò | URL | IN | Chữ | Sửa lần cuối | FOCUS_KW đã log | Pillar bài trỏ lên | Post title |
|---|---|---|---|---|---|---|---|
| **Pillar (HUB)** | [#975 /website-design-for-real-estate-agents](https://infina.ai/news/website-design-for-real-estate-agents/) | 5 | 1,799 | 2026-10-08 | `website design for real estate agents` | *(là pillar)* | Website Design for Real Estate Agents: What Actually Works in 2026 |
| Examples/inspiration | [#981 /best-real-estate-website-design](https://infina.ai/news/best-real-estate-website-design/) | 1 | 1,015 | 2026-10-08 | `best real estate website design` | ✅ `website-design-for-real-estate-agents`; ↗ `best-crm-for-real-estate`, `real-estate-website-builder` | Best Real Estate Website Design: 8 Examples to Model in 2026 |
| Review (niche: luxury) | [#1011 /luxury-real-estate-website-design](https://infina.ai/news/luxury-real-estate-website-design/) | 1 | 1,086 | 2026-10-08 | `luxury real estate website design` | ✅ `website-design-for-real-estate-agents`; ↗ `best-crm-for-real-estate`, `real-estate-website-builder` | Luxury Real Estate Website Design: Features That Signal Premium to Buyers |
| Review (niche: broker) | [#1005 /real-estate-broker-website-design](https://infina.ai/news/real-estate-broker-website-design/) | 1 | 1,001 | 2026-10-08 | `real estate broker website design` | ✅ `website-design-for-real-estate-agents`; ↗ `best-crm-for-real-estate`, `real-estate-website-builder` | Real Estate Broker Website Design: What Brokerage Sites Actually Need |
| Buying guide (agency) | [#999 /real-estate-web-design-companies](https://infina.ai/news/real-estate-web-design-companies/) | 1 | 941 | 2026-10-08 | `real estate web design companies` | ✅ `website-design-for-real-estate-agents`; ↗ `best-crm-for-real-estate`, `real-estate-website-builder` | Real Estate Web Design Companies: How to Choose the Right One |
| Decision (build vs buy) | [#993 /web-design-for-real-estate-agents](https://infina.ai/news/web-design-for-real-estate-agents/) | 1 | 963 | 2026-10-08 | `web design for real estate agents` | ✅ `website-design-for-real-estate-agents`; ↗ `best-crm-for-real-estate`, `real-estate-website-builder` | Web Design for Real Estate Agents: DIY vs. Hiring a Designer |

## Cụm 6: Landing Pages  (6 trang, 8,316 chữ)

| Vai trò | URL | IN | Chữ | Sửa lần cuối | FOCUS_KW đã log | Pillar bài trỏ lên | Post title |
|---|---|---|---|---|---|---|---|
| Niche: open house | [#918 /open-house-landing-page](https://infina.ai/news/open-house-landing-page/) | 5 | 1,724 | 2026-10-08 | `open house landing page` | ✅ `real-estate-landing-page-guide`; ↗ `best-crm-for-real-estate`, `real-estate-website-builder` | Open House Landing Page: How to Build One That Actually Captures Leads |
| **Pillar** | [#930 /real-estate-landing-page-guide](https://infina.ai/news/real-estate-landing-page-guide/) | 5 | 1,873 | 2026-10-08 | `real estate landing page` | *(là pillar)* | Real Estate Landing Page: Types, Elements, and How to Build One That Converts |
| Niche: seller chung | [#942 /seller-landing-pages-real-estate](https://infina.ai/news/seller-landing-pages-real-estate/) | 3 | 1,038 | 2026-10-08 | `seller landing pages real estate` | ✅ `real-estate-landing-page-guide`; ↗ `best-crm-for-real-estate`, `real-estate-website-builder` | Seller Landing Pages Real Estate: Types That Convert and How to Build Them |
| Niche: home valuation | [#936 /home-valuation-landing-page](https://infina.ai/news/home-valuation-landing-page/) | 2 | 1,167 | 2026-10-08 | `home valuation landing page` | ✅ `real-estate-landing-page-guide`; ↗ `best-crm-for-real-estate`, `real-estate-website-builder` | Home Valuation Landing Page: How to Build One That Converts Seller Leads |
| Evaluation/MOF (cluster hợp lệ) | [#948 /high-converting-real-estate-landing-pages](https://infina.ai/news/high-converting-real-estate-landing-pages/) | 1 | 1,292 | 2026-10-08 | `high converting real estate landing pages` | ✅ `real-estate-landing-page-guide`; ↗ `best-crm-for-real-estate`, `real-estate-website-builder` | High Converting Real Estate Landing Pages: What Makes Them Work in 2026 |
| Niche: agent chung | [#924 /real-estate-agent-landing-page](https://infina.ai/news/real-estate-agent-landing-page/) | 1 | 1,222 | 2026-10-08 | `real estate agent landing page` | ✅ `real-estate-landing-page-guide`; ↗ `best-crm-for-real-estate` | Real Estate Agent Landing Page: What to Include and How to Convert Visitors |

## Cụm 7: Lead Generation / Follow-up Automation  (9 trang, 8,208 chữ)

| Vai trò | URL | IN | Chữ | Sửa lần cuối | FOCUS_KW đã log | Pillar bài trỏ lên | Post title |
|---|---|---|---|---|---|---|---|
| **Pillar** | [#1223 /real-estate-lead-follow-up-automation-guide](https://infina.ai/news/real-estate-lead-follow-up-automation-guide/) | 17 | 2,453 | 2026-10-07 | `real estate lead follow-up automation` | *(là pillar)* | Real Estate Lead Follow-Up Automation: The Complete 2026 Guide |
| Giải thích/pain-point = refresh #223 | [#223 /real-estate-agent-crm-speed-to-lead](https://infina.ai/news/real-estate-agent-crm-speed-to-lead/) | 13 | 1,517 | 2026-10-09 | `real estate agent crm` | ✅ `real-estate-lead-follow-up-automation-guide`; ↗ `best-crm-for-real-estate` | Speed-to-Lead 2026: How Real Estate Agent CRM Closes the 15-Hour Gap |
| Buying guide/how-to | [#1227 /how-to-set-up-automated-lead-follow-up-real-estate](https://infina.ai/news/how-to-set-up-automated-lead-follow-up-real-estate/) | 4 | 539 | 2026-09-15 | `automated lead follow-up for real estate` | ✅ `real-estate-lead-follow-up-automation-guide` | Automated Lead Follow-Up for Real Estate: A 5-Step Setup Guide |
| Review/list | [#1225 /best-lead-generation-software-for-realtors](https://infina.ai/news/best-lead-generation-software-for-realtors/) | 3 | 587 | 2026-10-08 | `lead generation software for realtors` | ✅ `real-estate-lead-follow-up-automation-guide` | Best Lead Generation Software for Realtors in 2026 |
| Hỗ trợ (News) | [#1122 /database-reactivation-ai-seller-leads-real-estate-agents](https://infina.ai/news/database-reactivation-ai-seller-leads-real-estate-agents/) | 2 | 760 | 2026-10-02 | `database reactivation ai seller leads real estate agents` | ✅ `real-estate-lead-follow-up-automation-guide` | Your Next Listing Is Probably Already Sitting in Your CRM |
| Hỗ trợ (News) | [#1278 /seller-lead-prioritization-real-estate-pipeline](https://infina.ai/news/seller-lead-prioritization-real-estate-pipeline/) | 2 | 583 | 2026-10-02 | – | ✅ `real-estate-lead-follow-up-automation-guide` | Sellers Now Outnumber Buyers by 57.9%, the Widest Gap on Record |
| Hỗ trợ (News) | [#1272 /buyer-lead-nurture-campaign-real-estate-agents](https://infina.ai/news/buyer-lead-nurture-campaign-real-estate-agents/) | 1 | 568 | 2026-09-19 | – | ✅ `real-estate-lead-follow-up-automation-guide` | Realtor.com Just Named the Best Week to Buy in 2026, and Everyone Read It |
| Kênh cụ thể | [#1229 /facebook-lead-gen-for-realtors](https://infina.ai/news/facebook-lead-gen-for-realtors/) | 1 | 532 | 2026-09-15 | `facebook lead gen for realtors` | ✅ `real-estate-lead-follow-up-automation-guide`; ↗ `best-ai-voice-assistants-for-real-estate` | Facebook Lead Gen for Realtors: Turning Ad Leads Into Showings |
| Hỗ trợ | [#521 /real-estate-contact-form-conversion-rate](https://infina.ai/news/real-estate-contact-form-conversion-rate/) | 1 | 669 | 2026-10-08 | `real estate contact form conversion rate` | ✅ `real-estate-lead-follow-up-automation-guide`; ↗ `best-chatbot-customer-service-real-estate` | Real Estate Contact Forms Are Losing the Highest-Intent Leads |

## Cụm 8: Compliance / Legal / Risk  (6 trang, 6,017 chữ)

| Vai trò | URL | IN | Chữ | Sửa lần cuối | FOCUS_KW đã log | Pillar bài trỏ lên | Post title |
|---|---|---|---|---|---|---|---|
| **Pillar (nhẹ)** | [#237 /tcpa-compliance-for-real-estate-agents](https://infina.ai/news/tcpa-compliance-for-real-estate-agents/) | 15 | 1,904 | 2026-10-07 | `tcpa compliance for real estate agents` | *(là pillar)* | TCPA Compliance for Real Estate Agents: What Is Actually in Force for AI Texting and Calling |
| Hỗ trợ (News) | [#475 /ai-hallucination-risk-real-estate-listings](https://infina.ai/news/ai-hallucination-risk-real-estate-listings/) | 4 | 976 | 2026-10-07 | `ai hallucination risk real estate listings` | ✅ `tcpa-compliance-for-real-estate-agents` | AI-Written Listing Descriptions Are Creating Fair Housing Liability: Here’s What to Check |
| Hỗ trợ (News) | [#492 /ai-decision-making-compliance-real-estate-agents](https://infina.ai/news/ai-decision-making-compliance-real-estate-agents/) | 3 | 707 | 2026-08-24 | `ai decision making compliance real estate agents` | ✅ `tcpa-compliance-for-real-estate-agents` | Colorado’s New AI Law Sets a Deadline for Automated Decisions in Real Estate |
| Hỗ trợ (News) | [#1260 /seller-impersonation-fraud-prevention-real-estate-agents](https://infina.ai/news/seller-impersonation-fraud-prevention-real-estate-agents/) | 2 | 636 | 2026-10-07 | – | ✅ `tcpa-compliance-for-real-estate-agents` | Seller Impersonation Fraud Attempts Just Doubled. Here Is How to Catch It Earlier |
| Hỗ trợ (News) | [#1481 /how-agents-protect-clients-from-wire-fraud](https://infina.ai/news/how-agents-protect-clients-from-wire-fraud/) | 1 | 923 | 2026-10-07 | `how agents protect clients from wire fraud` | ✅ `tcpa-compliance-for-real-estate-agents` | Two Wire Fraud Companies Just Merged, and the Agent Is Still the Weak Link |
| Hỗ trợ (News) | [#1501 /private-listing-marketing-rules](https://infina.ai/news/private-listing-marketing-rules/) | 1 | 871 | 2026-10-08 | `private listing marketing rules` | ✅ `tcpa-compliance-for-real-estate-agents` | Three States Now Force Private Listings Public the Moment You Market Them |

## Bài News real estate chưa gắn cụm trong plan  (40 trang, 29,224 chữ)

| Vai trò | URL | IN | Chữ | Sửa lần cuối | FOCUS_KW đã log | Pillar bài trỏ lên | Post title |
|---|---|---|---|---|---|---|---|
| cluster | [#1106 /ai-assistant-instead-of-software-stack-real-estate-agents](https://infina.ai/news/ai-assistant-instead-of-software-stack-real-estate-agents/) | 2 | 777 | 2026-08-27 | `ai assistant instead of software stack real estate agents` | **❌ không** | Before You Buy Software Number 12, Ask Your AI Assistant to Replace It |
| cluster | [#1140 /ai-citation-content-real-estate-agent-websites](https://infina.ai/news/ai-citation-content-real-estate-agent-websites/) | 2 | 748 | 2026-10-08 | `ai citation content real estate agent websites` | ↗ `best-chatbot-customer-service-real-estate` | A 50-Year Broker’s Advice on What Actually Gets an AI Citation |
| cluster | [#390 /ai-isa-conversion-rates-real-estate](https://infina.ai/news/ai-isa-conversion-rates-real-estate/) | 2 | 686 | 2026-08-20 | `ai isa conversion rates real estate` | ↗ `best-chatbot-customer-service-real-estate` | AI ISAs Are Delivering 3x Higher Conversion Rates for Real Estate Teams |
| cluster | [#481 /ai-training-gap-for-real-estate-agents](https://infina.ai/news/ai-training-gap-for-real-estate-agents/) | 2 | 714 | 2026-08-14 | `ai training gap for real estate agents` | **❌ không** | 70% of Agents Want More AI Training: Here’s the Confidence Gap Behind That Number |
| cluster | [#1093 /ai-usage-without-measurable-impact-real-estate-agents](https://infina.ai/news/ai-usage-without-measurable-impact-real-estate-agents/) | 2 | 742 | 2026-08-25 | `ai usage without measurable impact real estate agents` | **❌ không** | 41% of Agents Use AI. Almost Half Say It Changed Nothing. |
| cluster | [#461 /autonomous-ai-workforce-real-estate-teams](https://infina.ai/news/autonomous-ai-workforce-real-estate-teams/) | 2 | 703 | 2026-08-12 | `autonomous ai workforce real estate teams` | **❌ không** | Real Estate’s Next AI Shift: From Chatbots to an AI Workforce for Real Estate Teams |
| cluster | [#1128 /agentic-ai-risk-concerns-real-estate-brokerage-leaders](https://infina.ai/news/agentic-ai-risk-concerns-real-estate-brokerage-leaders/) | 1 | 729 | 2026-08-30 | `agentic ai risk concerns real estate brokerage leaders` | **❌ không** | Brokerage Leaders’ AI Worry Score Just Jumped, and Agentic AI Is Why |
| cluster | [#1203 /ai-academy-role-based-learning-mls-subscribers](https://infina.ai/news/ai-academy-role-based-learning-mls-subscribers/) | 1 | 711 | 2026-09-13 | `ai academy role based learning mls subscribers` | **❌ không** | Bright MLS Is Building an AI Academy for 100,000 Agents |
| cluster | [#1254 /ai-back-office-automation-real-estate-brokerages](https://infina.ai/news/ai-back-office-automation-real-estate-brokerages/) | 1 | 598 | 2026-10-09 | – | **❌ không** | 53% of Brokerages Now Plan AI for Back-Office Work, Up From 23% in 2024 |
| cluster | [#498 /ai-backoffice-transaction-management-real-estate](https://infina.ai/news/ai-backoffice-transaction-management-real-estate/) | 1 | 658 | 2026-08-17 | `ai backoffice transaction management real estate` | **❌ không** | Inside Real Estate’s ComplianceAI Shows Where Back Office AI Is Headed |
| cluster | [#1302 /ai-chief-of-staff-for-real-estate-agents](https://infina.ai/news/ai-chief-of-staff-for-real-estate-agents/) | 1 | 572 | 2026-09-24 | – | **❌ không** | SERHANT. Unveils Dot, an AI That Runs Agents’ Days Without Being Asked |
| cluster | [#1178 /ai-comparative-market-analysis-minutes-real-estate-agents](https://infina.ai/news/ai-comparative-market-analysis-minutes-real-estate-agents/) | 1 | 810 | 2026-09-08 | `ai comparative market analysis minutes real estate agents` | **❌ không** | Compass Says Its AI Just Cut CMA Prep From 90 Minutes to 15 |
| cluster | [#1209 /ai-contract-data-extraction-closing-automation-agents](https://infina.ai/news/ai-contract-data-extraction-closing-automation-agents/) | 1 | 749 | 2026-10-08 | `ai contract data extraction closing automation agents` | ↗ `best-crm-for-real-estate` | HomeSmart’s AI Now Reads a Contract and Automates the Closing Behind It |
| cluster | [#504 /ai-data-readiness-for-real-estate-brokerages](https://infina.ai/news/ai-data-readiness-for-real-estate-brokerages/) | 1 | 680 | 2026-08-17 | `ai data readiness for real estate brokerages` | **❌ không** | AI’s Impact on Real Estate Is Shrinking, and Bad Data Is Why |
| cluster | [#1020 /ai-deployment-maturity-real-estate-firms](https://infina.ai/news/ai-deployment-maturity-real-estate-firms/) | 1 | 1,128 | 2026-08-25 | `ai deployment maturity real estate firms` | **❌ không** | Only 9% of Real Estate Firms Have Actually Scaled Their AI, New Survey Finds |
| cluster | [#1165 /ai-digital-human-brokerage-website-adoption](https://infina.ai/news/ai-digital-human-brokerage-website-adoption/) | 1 | 825 | 2026-09-06 | `ai digital human brokerage website adoption` | **❌ không** | A Real Brokerage Just Put an AI Avatar Named Mae on Its Website |
| cluster | [#1529 /ai-drafted-messages-agent-approval](https://infina.ai/news/ai-drafted-messages-agent-approval/) | 1 | 1,031 | 2026-10-09 | `ai drafted messages agent approval` | ↗ `ai-intent-layer-for-real-estate-crm`, `real-estate-lead-follow-up-automation-guide`, `tcpa-compliance-for-real-estate-agents` | Realtor.com’s New AI Drafts the Message, Then Waits for You to Approve It |
| cluster | [#1034 /ai-flat-fee-brokerage-model-real-estate-agents](https://infina.ai/news/ai-flat-fee-brokerage-model-real-estate-agents/) | 1 | 872 | 2026-10-08 | `ai flat fee brokerage model real estate agents` | **❌ không** | TurboHome’s AI Hybrid Model Just Cut a Home Buying Commission by Thousands |
| cluster | [#1308 /ai-home-valuation-tool-real-estate-agent-website](https://infina.ai/news/ai-home-valuation-tool-real-estate-agent-website/) | 1 | 582 | 2026-10-09 | – | ↗ `best-chatbot-customer-service-real-estate` | 37% of Buyers Would Let AI Handle a Home Purchase With Minimal Human Help |
| cluster | [#513 /ai-job-substitution-risk-real-estate-agents](https://infina.ai/news/ai-job-substitution-risk-real-estate-agents/) | 1 | 771 | 2026-10-08 | `ai job substitution risk real estate agents` | ↗ `best-chatbot-customer-service-real-estate` | Harvard Study Puts a Number on AI’s Threat to Real Estate Agent Jobs |
| cluster | [#1296 /ai-likely-to-sell-alerts-real-estate-agents](https://infina.ai/news/ai-likely-to-sell-alerts-real-estate-agents/) | 1 | 530 | 2026-09-23 | – | **❌ không** | Compass Got 15,000 Agents to Generate 97,000 AI Conversations in Weeks |
| cluster | [#1335 /ai-listing-visualization-feature-real-estate-agents](https://infina.ai/news/ai-listing-visualization-feature-real-estate-agents/) | 1 | 508 | 2026-09-29 | – | **❌ không** | Interactive Room Visualization Is Driving Up to 170% More Showing Requests |
| cluster | [#1341 /ai-post-tour-follow-up-assistant-real-estate-crm](https://infina.ai/news/ai-post-tour-follow-up-assistant-real-estate-crm/) | 1 | 673 | 2026-10-01 | – | ↗ `ai-intent-layer-for-real-estate-crm` | A $4B AI Housing Startup Just Automated the Post-Tour Follow-Up Text |
| cluster | [#1290 /ai-powered-follow-up-messages-real-estate-agents](https://infina.ai/news/ai-powered-follow-up-messages-real-estate-agents/) | 1 | 535 | 2026-09-22 | – | ↗ `real-estate-lead-follow-up-automation-guide` | NAR’s 2026 Report Shows AI Use Climbing, but Concentrated in One Place |
| cluster | [#899 /ai-property-research-tools-real-estate-teams](https://infina.ai/news/ai-property-research-tools-real-estate-teams/) | 1 | 651 | 2026-10-08 | `ai property research tools real estate teams` | ↗ `best-crm-for-real-estate` | ATTOM’s New AI Agents Let You Ask Property Questions in Plain English |
| cluster | [#1284 /ai-relationship-manager-for-real-estate-leads](https://infina.ai/news/ai-relationship-manager-for-real-estate-leads/) | 1 | 568 | 2026-09-21 | – | ↗ `best-conversational-ai-chatbot-for-real-estate` | Real Brokerage’s Leo 2.0 Is Holding Hundreds of Conversations at Once |
| cluster | [#1152 /ai-video-marketing-automation-real-estate-agents](https://infina.ai/news/ai-video-marketing-automation-real-estate-agents/) | 1 | 700 | 2026-09-04 | `ai video marketing automation real estate agents` | **❌ không** | Keller Williams Just Gave Agents an AI Tool That Claims to Save 10 Hours a Week |
| cluster | [#1134 /ai-visibility-reddit-seeding-backlash-real-estate-agents](https://infina.ai/news/ai-visibility-reddit-seeding-backlash-real-estate-agents/) | 1 | 773 | 2026-10-09 | `ai visibility reddit seeding backlash real estate agents` | ↗ `best-chatbot-customer-service-real-estate` | Agents Are Seeding Reddit to Win ChatGPT Recommendations, and Reddit Just Pushed Back |
| cluster | [#293 /answer-engine-optimization-for-real-estate-agents](https://infina.ai/news/answer-engine-optimization-for-real-estate-agents/) | 1 | 780 | 2026-10-08 | `answer engine optimization for real estate agents` | ↗ `best-chatbot-customer-service-real-estate` | Why 91% of Real Estate Agents Are Invisible to AI Search (And What to Do About It) |
| cluster | [#1191 /chatgpt-app-mortgage-matchup-real-estate-agent-visibility](https://infina.ai/news/chatgpt-app-mortgage-matchup-real-estate-agent-visibility/) | 1 | 770 | 2026-10-08 | `chatgpt app mortgage matchup real estate agent visibility` | ↗ `best-chatbot-customer-service-real-estate` | UWM’s New ChatGPT App Shows Where AI Search Is Headed for Agents Too |
| cluster | [#1158 /chatgpt-sycophantic-pricing-advice-real-estate-agents](https://infina.ai/news/chatgpt-sycophantic-pricing-advice-real-estate-agents/) | 1 | 866 | 2026-10-08 | `chatgpt sycophantic pricing advice real estate agents` | ↗ `best-chatbot-customer-service-real-estate` | Coldwell Banker’s CEO Just Called ChatGPT ‘Sycophantic’ About Home Prices |
| cluster | [#1415 /cost-per-lead-for-real-estate-agents](https://infina.ai/news/cost-per-lead-for-real-estate-agents/) | 1 | 805 | 2026-10-08 | – | ↗ `real-estate-lead-follow-up-automation-guide` | The Average Cost Per Lead for Real Estate Agents Just Hit $503 |
| cluster | [#299 /declining-ai-trust-real-estate-agents](https://infina.ai/news/declining-ai-trust-real-estate-agents/) | 1 | 709 | 2026-08-20 | `declining ai trust real estate agents` | **❌ không** | Homebuyer Trust in AI Just Dropped 14 Points — What That Means for Real Estate Agents |
| cluster | [#528 /embedded-ai-real-estate-brokerage-platforms](https://infina.ai/news/embedded-ai-real-estate-brokerage-platforms/) | 1 | 675 | 2026-10-08 | `embedded ai real estate brokerage platforms` | ↗ `best-chatbot-customer-service-real-estate` | Lone Wolf Just Bet the Future of Real Estate AI Isn’t a Separate App |
| cluster | [#1317 /financing-readiness-signals-for-real-estate-buyer-leads](https://infina.ai/news/financing-readiness-signals-for-real-estate-buyer-leads/) | 1 | 534 | 2026-09-26 | – | ↗ `ai-intent-layer-for-real-estate-crm` | Down Payments Just Hit a Four-Year Q2 Low While Payments Jumped 74% |
| cluster | [#1266 /google-home-listing-ads-real-estate-agent-leads](https://infina.ai/news/google-home-listing-ads-real-estate-agent-leads/) | 1 | 579 | 2026-10-08 | – | ↗ `best-chatbot-customer-service-real-estate` | Google Just Took Home Listing Ads Nationwide, and Zillow Stock Dropped |
| cluster | [#1197 /mls-ai-conversational-search-broker-attribution-agents](https://infina.ai/news/mls-ai-conversational-search-broker-attribution-agents/) | 1 | 752 | 2026-09-11 | `mls ai conversational search broker attribution agents` | **❌ không** | Northwest MLS Just Launched an AI Home Search With Zero Ads and Zero Lead Forms |
| cluster | [#1243 /mortgage-rate-spike-real-estate-agent-response](https://infina.ai/news/mortgage-rate-spike-real-estate-agent-response/) | 1 | 575 | 2026-10-08 | – | ↗ `best-crm-for-real-estate` | Mortgage Rates Just Hit a 52-Week High: What It Means for Agent Response Times |
| cluster | [#286 /real-estate-ai-adoption-statistics-2026](https://infina.ai/news/real-estate-ai-adoption-statistics-2026/) | 1 | 824 | 2026-10-08 | `real estate ai adoption statistics 2026` | ↗ `best-chatbot-customer-service-real-estate` | Real Estate’s AI Holdouts Are Nearly Extinct: What the 2026 Adoption Data Means for Agents Still on the Fence |
| cluster | [#1609 /real-estate-ai-pricing-per-task](https://infina.ai/news/real-estate-ai-pricing-per-task/) | 1 | 1,331 | 2026-10-09 | `real estate ai pricing` | ↗ `real-estate-lead-follow-up-automation-guide` | Rechat’s AI Keeps Doing More Work. The Price Has Not Moved. |

## Ngoài chủ đề real estate (AI/tech)  (11 trang, 2,780 chữ)

| Vai trò | URL | IN | Chữ | Sửa lần cuối | FOCUS_KW đã log | Pillar bài trỏ lên | Post title |
|---|---|---|---|---|---|---|---|
| cluster | [#41 /ai-cannot-learn-while-it-works](https://infina.ai/news/ai-cannot-learn-while-it-works/) | 0 | 323 | 2026-07-31 | `ai cannot learn while it works` ⚠️ | **❌ không** | AI cannot learn while it works |
| cluster | [#31 /ai-just-moved-from-a-separate-tab-into-your-slack](https://infina.ai/news/ai-just-moved-from-a-separate-tab-into-your-slack/) | 0 | 191 | 2026-07-31 | `ai just moved from a separate tab into your slack` ⚠️ | **❌ không** | AI just moved from a separate tab into your Slack |
| cluster | [#34 /claude-code-has-500000-lines-of-code-only-1-6-of-it-is-actually-ai](https://infina.ai/news/claude-code-has-500000-lines-of-code-only-1-6-of-it-is-actually-ai/) | 0 | 468 | 2026-07-31 | `claude code has 500000 lines of code only 1 6 of it is actually ai` ⚠️ | **❌ không** | Claude Code has 500,000 lines of code. Only 1.6% of it is actually AI |
| cluster | [#50 /claude-code-just-shipped-artifacts](https://infina.ai/news/claude-code-just-shipped-artifacts/) | 0 | 66 | 2026-07-31 | `claude code just shipped artifacts` ⚠️ | **❌ không** | Claude Code just shipped Artifacts |
| cluster | [#14 /claude-fable-5-is-back](https://infina.ai/news/claude-fable-5-is-back/) | 0 | 195 | 2026-07-30 | `claude fable 5 is back` ⚠️ | **❌ không** | Claude Fable 5 is back |
| cluster | [#1 /genai-economy-first-revenue-number](https://infina.ai/news/genai-economy-first-revenue-number/) | 0 | 291 | 2026-08-17 | `genai economy first revenue number` ⚠️ | **❌ không** | The GenAI economy just got its first real revenue number |
| cluster | [#53 /is-openai-in-trouble](https://infina.ai/news/is-openai-in-trouble/) | 0 | 88 | 2026-07-31 | `is openai in trouble` ⚠️ | **❌ không** | Is OpenAI in trouble? |
| cluster | [#44 /microsoft-just-sent-6000-engineers-into-enterprise-buildings](https://infina.ai/news/microsoft-just-sent-6000-engineers-into-enterprise-buildings/) | 0 | 313 | 2026-07-31 | `microsoft just sent 6000 engineers into enterprise buildings` ⚠️ | **❌ không** | Microsoft just sent 6,000 engineers into enterprise buildings |
| cluster | [#47 /most-ai-tools-stop-working-when-you-close-your-laptop](https://infina.ai/news/most-ai-tools-stop-working-when-you-close-your-laptop/) | 0 | 354 | 2026-07-31 | `most ai tools stop working when you close your laptop` ⚠️ | **❌ không** | Most AI tools stop working when you close your laptop |
| cluster | [#37 /the-u-s-governments-reported-ban-on-foreign-access-to-anthropics-models](https://infina.ai/news/the-u-s-governments-reported-ban-on-foreign-access-to-anthropics-models/) | 0 | 84 | 2026-07-31 | `the u s governments reported ban on foreign access to anthropics models` ⚠️ | **❌ không** | The U.S. government’s reported ban on foreign access to Anthropic’s models |
| cluster | [#26 /yc-spring-2026-the-agent-economy-has-actuaries-now](https://infina.ai/news/yc-spring-2026-the-agent-economy-has-actuaries-now/) | 0 | 407 | 2026-07-31 | `yc spring 2026 the agent economy has actuaries now` ⚠️ | **❌ không** | YC Spring 2026: The Agent Economy Has Actuaries Now |


---

## Phụ lục: 12 stub 301

Đây vẫn là 12 post thật trong WordPress nhưng trang của chúng trả 301 chứ không phải 200, nên không
tính vào 135 bài ở trên.

**Cả 12 đều đang ở IN = 0, tức là không còn bài nào trỏ vào slug cũ nữa.** Đây là kết quả của đợt
sửa 02/10, lúc đó phát hiện #1026, #1184 và #1329 còn link qua slug stub và đã đổi sang trỏ thẳng.
Nghĩa là 12 redirect này hiện chỉ còn phục vụ link từ bên ngoài site và backlink cũ, không phục vụ
link nội bộ nào. Cũng vì vậy cột IN của 135 bài ở trên không có dòng nào ghi "qua stub".


| URL stub | IN (vẫn còn bài trỏ vào) | Redirect 301 tới | Chữ còn lại |
|---|---|---|---|
| [#99 /best-ai-chat-platform-real-estate](https://infina.ai/news/best-ai-chat-platform-real-estate/) | 0 | `best-chatbot-customer-service-real-estate` | 46 |
| [#58 /best-ai-chatbot-for-real-estate-lead-capture](https://infina.ai/news/best-ai-chatbot-for-real-estate-lead-capture/) | 0 | `best-chatbot-customer-service-real-estate` | 51 |
| [#1069 /best-ai-conversational-bot-for-real-estate](https://infina.ai/news/best-ai-conversational-bot-for-real-estate/) | 0 | `best-conversational-ai-chatbot-for-real-estate` | 50 |
| [#1063 /best-conversational-chatbot-for-real-estate](https://infina.ai/news/best-conversational-chatbot-for-real-estate/) | 0 | `best-conversational-ai-chatbot-for-real-estate` | 65 |
| [#384 /best-crm-software-real-estate-agents](https://infina.ai/news/best-crm-software-real-estate-agents/) | 0 | `best-crm-for-real-estate` | 48 |
| [#649 /best-idx-website-for-realtors](https://infina.ai/news/best-idx-website-for-realtors/) | 0 | `idx-website-for-realtors` | 43 |
| [#553 /best-real-estate-website-builder](https://infina.ai/news/best-real-estate-website-builder/) | 0 | `real-estate-website-builder` | 47 |
| [#196 /conversational-chat-real-estate](https://infina.ai/news/conversational-chat-real-estate/) | 0 | `what-is-a-conversational-chatbot-real-estate` | 56 |
| [#1076 /no-code-chatbot-platform-real-estate](https://infina.ai/news/no-code-chatbot-platform-real-estate/) | 0 | `best-chatbot-builder-real-estate` | 45 |
| [#637 /real-estate-website-builder-with-idx](https://infina.ai/news/real-estate-website-builder-with-idx/) | 0 | `real-estate-website-builder` | 72 |
| [#987 /realtor-website-design](https://infina.ai/news/realtor-website-design/) | 0 | `website-design-for-real-estate-agents` | 46 |
| [#412 /top-crm-tools-for-real-estate-teams](https://infina.ai/news/top-crm-tools-for-real-estate-teams/) | 0 | `best-crm-for-real-estate` | 35 |
