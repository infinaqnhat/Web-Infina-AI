# Content Plan

File này là bản đồ content đầy đủ cho `infina.ai/news` — **8 Cụm pillar + cluster**, áp dụng đúng
khung của `skills/pillar-cluster-writer/SKILL.md` (1 pillar bao quát + 2-4 cluster theo vai trò
funnel: So sánh/Evaluation-MOF, Review/Evaluation-MOF, Buying guide/Decision-BOF, Support-how-to/
Discovery-Post-purchase), bao trùm **86 bài evergreen** đã publish (loại 36 bài News/Market
Commentary — tin tức thời sự không có "chủ đề lớn" chung để làm pillar).

**RealSaleX (AI Deal Room)** — SaaS B2B cho brokerage bất động sản Mỹ, URL chưa deploy — đang chủ
động viết bài mới vào **3 trong 8 cụm** dưới đây (đánh dấu badge 🎯 RealSaleX ở từng cụm): Cụm 2
(CRM Software, góc "bổ sung intent layer"), Cụm 4 (AI Voice/Virtual Assistant/Receptionist), Cụm 7
(Lead Generation/Follow-up Automation). Các cụm còn lại là nội dung sitewide đã có sẵn, dùng để
check cannibalization trước khi lên plan mới.

Toàn bộ **10 cặp cannibalization** phát hiện khi map lại ngày 01/10/2026 đã audit xong (6 merge,
2 internal-link fix, 2 giữ nguyên không đổi) — xem mục "Cannibalization — lịch sử audit" cuối file
và `skills/post-refresh/references/refresh-log.md` cho chi tiết từng case.

---

## Lịch xuất bản RealSaleX (9 bài mới, đã publish/schedule hết — 15-23/09/2026)

| Ngày | Bài | ID | Trạng thái |
|---|---|---|---|
| 15/09/2026 | AI Outbound Calling for Real Estate (Cụm 4) | 1213 | ✅ Published |
| 16/09/2026 10:00 | AI Receptionist vs Human Receptionist (Cụm 4) | 1217 | ✅ Published |
| 17/09/2026 10:00 | AI Answering Service for Real Estate (Cụm 4) | 1219 | ✅ Published |
| 18/09/2026 10:00 | Real Estate Lead Follow-Up Automation Guide (Cụm 7, pillar) | 1223 | ✅ Published |
| 19/09/2026 10:00 | Best Lead Generation Software for Realtors (Cụm 7) | 1225 | ✅ Published |
| 20/09/2026 10:00 | Automated Lead Follow-Up 5-Step Setup Guide (Cụm 7) | 1227 | ✅ Published |
| 21/09/2026 10:00 | Facebook Lead Gen for Realtors (Cụm 7) | 1229 | ✅ Published |
| 22/09/2026 10:00 | AI Intent Layer for Real Estate CRM (Cụm 2, pillar nhẹ) | 1232 | ✅ Published |
| 23/09/2026 10:00 | CINC CRM Review (Cụm 2) | 1234 | ✅ Published |

Refresh (cùng ngày 15/09/2026, đã publish): **#147** (pillar Cụm 4), **#223** (Cụm 2, thay C2.2).
#384 (pillar Cụm 2 lúc đó, thay C3.1+C3.3) đã bị merge vào #207 ngày 01/10 — xem Cụm 2 bên dưới.

**⚠️ Lưu ý lịch sử về link nội bộ lúc rollout** (không cần hành động gì thêm, đã tự hết): các bài
Cụm 7/Cụm 2 được viết với link chéo đầy đủ ngay từ đầu, nên có vài ngày link trỏ tới bài chưa
publish (404 tạm thời) trong lúc lịch trải dài nhiều ngày — tự hết khi từng bài lần lượt lên lịch
xong theo bảng trên.

---

## Bài đã có trên site — map vào RealSaleX khi viết (check 2026-09-15, cập nhật 01/10)

Đối chiếu 110 bài publish (qua `list_posts` + fetch nội dung thật, không suy đoán từ tiêu đề) với
3 cụm RealSaleX đang viết. Phát hiện **trùng chủ đề khá nặng ở Cụm 7 và Cụm 2** — nên đã refresh
bài cũ thay vì viết đè.

| Bài đã có | FOCUS_KW đã log | Trùng ID nào | Việc đã làm |
|---|---|---|---|
| [#147 — 7 Best AI Voice Assistants for Real Estate Agents](https://infina.ai/news/best-ai-voice-assistants-for-real-estate/) | `ai voice assistants for real estate` | Cụm 4 (P1, C1.2) | ✅ Refreshed 15/09 — dùng làm pillar chính thức Cụm 4 thay vì viết P1/C1.2 mới |
| [#223 — Speed-to-Lead](https://infina.ai/news/real-estate-agent-crm-speed-to-lead/) | `real estate agent crm` | Cụm 7 (C2.2) | ✅ Refreshed 15/09 — thêm link tới pillar Cụm 7, thay thế C2.2 |
| [#207 — Best Real Estate Agent CRM Software](https://infina.ai/news/best-crm-for-real-estate/) | `best crm for real estate` | Cụm 2 (C3.1, C3.3) | ✅ **ĐỔI VAI TRÒ PILLAR (2026-10-01)**: #207 giờ là pillar chính thức Cụm 2 thay cho #384 (xem lý do ở mục Cannibalization #4 + refresh-log.md) — đã hấp thụ mục "None of These Ship a True Intent Layer" + link pillar nhẹ từ #384, và "Integrations That Matter" từ #412 |
| ~~#384 — Best CRM Software for Real Estate Agents~~ | `best crm software` | Cụm 2 (C3.1, C3.3) | ⚠️ ĐÃ MERGE (2026-10-01) vào #207, redirect 301 live. Lý do đổi hub: #207 có 15 inbound link sitewide sẵn có, #384 chỉ có 2 (từ CINC review + Intent Layer) — xem refresh-log.md |
| [#444 — Best CRM for Real Estate Agents: A Buyer's Guide](https://infina.ai/news/best-crm-buying-guide-real-estate-agents/) | `best crm` | Cụm 2 (C3.1, C3.3) | Giữ nguyên — BOF buying-guide khác funnel stage, không trùng #207 (xem Cannibalization #4) |
| [#230 — What Is CRM Software?](https://infina.ai/news/what-is-crm-software/) / [#405 — CRM Software 101](https://infina.ai/news/crm-management-real-estate-agents-beginners-guide/) | — | — | ❌ Hướng "CRM Software generic" đã bỏ hẳn khỏi plan RealSaleX, không cần động vào 2 bài này (đã cover đúng góc "CRM là gì") |
| [#214 — AI CRM for Real Estate](https://infina.ai/news/ai-crm-real-estate/) | `ai crm` | Cụm 2 (pillar nhẹ) | Đã đọc kỹ trước khi viết pillar nhẹ — khác góc (định nghĩa + tool listicle vs. "bổ sung intent layer cho CRM sẵn có"), pillar nhẹ link ngược lại #214 cho người cần chọn CRM từ đầu |
| **CINC** (brand) | — | Cụm 2 (C3.2) | ✅ Xác nhận gap thật, đã viết C3.2 |

### Bài bổ trợ / liên quan (không trùng — dùng để link thêm, đã áp dụng khi viết)

| Bài đã có | Gắn vào bài nào |
|---|---|
| [#237 — TCPA Compliance for Real Estate Agents](https://infina.ai/news/tcpa-compliance-for-real-estate-agents/) | #147, C1.1, C1.4, C2.4 (Cụm 4 + Cụm 7) |
| [#390 — AI ISAs Are Delivering 3x Higher Conversion Rates](https://infina.ai/news/ai-isa-conversion-rates-real-estate/) | #147 (Cụm 4) |
| [#1026 — Rechat AI Agent Integration for CRM](https://infina.ai/news/ai-agent-integration-for-real-estate-crm-platforms/) | (chưa dùng, vẫn còn để trích dẫn thêm khi refresh sau) |
| [#1171 — RE/MAX Leo AI CRM Assistant](https://infina.ai/news/ai-crm-assistant-brokerage-merger-rollout-agents/) | (chưa dùng, vẫn còn để trích dẫn thêm khi refresh sau) |

---

## 8 Cụm nội dung (toàn site, Pillar + Cluster)

**Chú thích trạng thái**: ✅ Hub/Pillar sống · ⚠️ Đã merge → stub (redirect 301) · 🎯 RealSaleX =
cụm đang được RealSaleX chủ động viết bài / mở rộng.

---

### Cụm 1: Chatbot / Conversational AI — 15 bài sống (19 gốc, 4 đã merge 01/10/2026)

Cụm đã audit + xử lý cannibalization đầy đủ (xem refresh-log.md). Có **2 pillar song song** vì 2
góc đủ khác biệt để không cần gộp chung: Pillar A nhắm "conversational AI / lead follow-up bot",
Pillar B nhắm "customer service platform" (rộng hơn, bao cả tool CS tổng quát như Zendesk/Intercom).

| Vai trò | Bài | Focus keyword | Funnel | Trạng thái |
|---|---|---|---|---|
| **Pillar A** | [Best Conversational AI Chatbots for Real Estate Agents in 2026](https://infina.ai/news/best-conversational-ai-chatbot-for-real-estate/) | `best conversational ai chatbot for real estate` | Discovery/TOF | ✅ Hub (đã hấp thụ 2 bài, 11 tool) |
| **Pillar B** | [12 Best Chatbot Customer Service Tools for Real Estate](https://infina.ai/news/best-chatbot-customer-service-real-estate/) | `chatbot customer service real estate` | Discovery/TOF | ✅ Hub (đã hấp thụ 2 bài, 15 tool) |
| Review/list | [7 Best Chatbot Builders for Real Estate](https://infina.ai/news/best-chatbot-builder-real-estate/) | `chatbot builder real estate` | Evaluation/MOF | — |
| Review/list | [Best No-Code Chatbot Platform for Real Estate Websites in 2026](https://infina.ai/news/no-code-chatbot-platform-real-estate/) | `no code chatbot platform real estate` | Evaluation/MOF | 🔎 góc gần trùng "Chatbot Builders" ở trên, chưa audit |
| So sánh | [Chatbot vs Conversational AI](https://infina.ai/news/chatbot-vs-conversational-ai-real-estate/) | `chatbot vs conversational ai real estate` | Evaluation/MOF | — |
| So sánh | [GoHighLevel Chatbot vs Dedicated Real Estate Chatbots](https://infina.ai/news/gohighlevel-chatbot-vs-dedicated-real-estate-chatbot/) | `gohighlevel chatbot` | Evaluation/MOF | — |
| So sánh | [AI Chat vs SMS Follow-Up for Real Estate](https://infina.ai/news/ai-chat-vs-sms-real-estate/) | `ai chat vs sms real estate` | Evaluation/MOF | — |
| So sánh | [Chatbot vs Live Agent for Real Estate](https://infina.ai/news/chatbot-vs-live-agent-real-estate/) | `chatbot vs live agent real estate` | Evaluation/MOF | — |
| So sánh/thay thế | [Zendesk Sunshine Conversations Alternative](https://infina.ai/news/zendesk-sunshine-conversations-alternative-real-estate/) | `zendesk sunshine conversations alternative` | Evaluation/MOF | — |
| ✅ Định nghĩa (HUB) | [What Is a Conversational Chatbot?](https://infina.ai/news/what-is-a-conversational-chatbot-real-estate/) | `conversational chatbot` | Discovery/TOF | ✅ HUB (2026-10-01) — đã hấp thụ seller qualification + post-showing follow-up từ bài dưới |
| ~~Định nghĩa~~ | ~~Conversational Chat for Real Estate~~ | `conversational chat real estate` | Discovery/TOF | ⚠️ ĐÃ MERGE (2026-10-01) vào dòng trên, redirect 301 live |
| Hỗ trợ (News) | [EU AI Act Disclosure Rules...](https://infina.ai/news/ai-disclosure-rules-for-real-estate-chatbots/) | `ai disclosure rules for real estate chatbots` | Post-purchase/support | — |
| Hỗ trợ (News) | [This Chatbot Reads Your Listing Photos...](https://infina.ai/news/real-estate-chatbot-that-reads-listing-photos/) | `real estate chatbot that reads listing photos` | Post-purchase/support | — |
| Hỗ trợ (News) | [A New Study Found AI Got 1 in 4 Mortgage Document Checks Wrong](https://infina.ai/news/ai-chatbot-mortgage-document-errors-real-estate-agents/) | `ai chatbot mortgage document errors real estate agents` | Post-purchase/support | — |
| Hỗ trợ (News) | [A CRMLS Test Shows How Easily an AI Chatbot Can Leak Your MLS Data](https://infina.ai/news/ai-chatbot-mls-data-security-risk-brokerages/) | `ai chatbot mls data security risk brokerages` | Post-purchase/support | — |

**4 bài đã merge (01/10/2026)**: [Best AI Chatbot for Real Estate Lead Capture](https://infina.ai/news/best-ai-chatbot-for-real-estate-lead-capture/) + [8 Best AI Chat Platforms](https://infina.ai/news/best-ai-chat-platform-real-estate/) → stub, redirect 301 sang Pillar B. [Best Conversational Chatbot Platforms...](https://infina.ai/news/best-conversational-chatbot-for-real-estate/) + [Best AI Conversational Bots for Real Estate Follow-Up](https://infina.ai/news/best-ai-conversational-bot-for-real-estate/) → stub, redirect 301 sang Pillar A. Cả 4 redirect đã verify live qua curl.

---

### Cụm 2: CRM Software — 🎯 RealSaleX (góc "CRM Add-on / Alternatives & Pricing") — 20 bài sống (22 gốc, 2 đã merge 2026-10-01)

**✅ ĐÃ AUDIT (2026-10-01)** — cụm cannibalization LỚN NHẤT đã xử lý xong, xem refresh-log.md.
Phát hiện 5 bài "best/top CRM" roundup trùng gần hết cùng 1 pool platform (Follow Up Boss/Lofty/
Wise Agent/LionDesk/kvCORE). 3 bài (#384 Pillar cũ, #207, #412) là duplicate thật → gộp vào #207
(đổi vai trò hub từ #384 sang #207 vì #207 có sẵn 15 inbound link sitewide, #384 chỉ có 2). 2 bài
còn lại (#419 teams-niche, #444 buying-guide/BOF) giữ nguyên vì differentiation thật.

| Vai trò | Bài | Focus keyword | Funnel | Trạng thái |
|---|---|---|---|---|
| **Pillar chính (ĐÃ ĐỔI 01/10)** | [Best Real Estate Agent CRM Software in 2026](https://infina.ai/news/best-crm-for-real-estate/) | `best crm for real estate` | Evaluation/MOF | ✅ = #207, giờ là HUB — đã hấp thụ #384 (Intent Layer section) + #412 (Integrations section) |
| ~~Pillar chính (cũ)~~ | ~~Best CRM Software for Real Estate Agents~~ | `best crm software` | Discovery/TOF | ⚠️ ĐÃ MERGE (2026-10-01) vào #207, redirect 301 live |
| **Pillar nhẹ 🎯 RealSaleX** | [AI Intent Layer for Real Estate CRM: What It Adds](https://infina.ai/news/ai-intent-layer-for-real-estate-crm/) | `ai intent layer for real estate crm` | Evaluation/MOF | ✅ góc "bổ sung CRM sẵn có", khác hẳn roundup — đã sửa link trỏ về #207 thay vì #384 |
| Review (brand cụ thể) 🎯 RealSaleX | [CINC CRM Review: Pricing, Features, and Buyer Follow-Up Gaps](https://infina.ai/news/cinc-crm-review-real-estate/) | `cinc crm review` | Evaluation/MOF | ✅ cluster của pillar nhẹ — đã sửa link trỏ về #207 thay vì #384 |
| So sánh (MOF) 🎯 RealSaleX — chưa viết | *Customer Engagement Platform vs CRM for Real Estate* | `customer engagement platform vs crm` | Evaluation/MOF | 🕐 Đã duyệt plan 30/09, chưa viết — xem "Mở rộng CEP" bên dưới |
| Listicle chiến lược (TOF) 🎯 RealSaleX — chưa viết | *Customer Engagement Strategies for Real Estate Agents* | niche từ `digital customer engagement` + `customer engagement examples` | Discovery/TOF | 🕐 Đã duyệt plan 30/09, chưa viết — xem "Mở rộng CEP" bên dưới |
| ~~🔎 Review/list (roundup)~~ | ~~Top CRM Tools for Real Estate Agents and Teams~~ | `crm tools for real estate` | Evaluation/MOF | ⚠️ ĐÃ MERGE (2026-10-01) vào #207, redirect 301 live |
| Review/list (niche: teams) | [Best CRM for Real Estate Teams: Top Picks for 2026](https://infina.ai/news/best-crm-for-real-estate-teams-2026/) | `best crm for real estate teams` | Evaluation/MOF | ✅ ĐÃ AUDIT: niche "teams" thật, rank tốt nhất nhóm (pos 5.0) — giữ nguyên |
| Buying guide (BOF) | [Best CRM for Real Estate Agents: A Buyer's Guide (2026)](https://infina.ai/news/best-crm-buying-guide-real-estate-agents/) | `best crm` | Decision/BOF | ✅ ĐÃ AUDIT: funnel stage khác thật (quy trình đánh giá 14 ngày, red flags) — giữ nguyên |
| Review/list (niche: free) | [Best Free CRM for Real Estate Agents in 2026](https://infina.ai/news/best-free-crm-for-real-estate-agents/) | `free crm for real estate` | Evaluation/MOF | niche hoá rõ (free tier), rủi ro thấp hơn 4 dòng trên |
| Định nghĩa | [What Is CRM Software?](https://infina.ai/news/what-is-crm-software/) | `what is crm software` | Discovery/TOF | = #230, giữ nguyên không động |
| Định nghĩa (beginner) | [CRM Software 101: A Beginner's Guide](https://infina.ai/news/crm-management-real-estate-agents-beginners-guide/) | `crm management` | Discovery/TOF | = #405, giữ nguyên không động |
| Định nghĩa (khác góc) | [AI CRM for Real Estate](https://infina.ai/news/ai-crm-real-estate/) | `ai crm` | Discovery/TOF | = #214, đã xác nhận khác góc pillar nhẹ |
| Sub-topic: marketing (strategy) | [CRM Marketing for Real Estate](https://infina.ai/news/crm-marketing-real-estate/) | `crm marketing` | Evaluation/MOF | ✅ ĐÃ AUDIT (2026-10-01): differentiation thật (funnel 5 giai đoạn) vs dòng dưới (định nghĩa category) — đã thêm link 2 chiều, giữ cả 2 |
| Sub-topic: marketing (định nghĩa) | [What Is CRM Marketing Software? A Guide for Real Estate Teams](https://infina.ai/news/crm-marketing-software-real-estate-guide/) | `crm marketing software` | Discovery/TOF | ✅ ĐÃ AUDIT (2026-10-01): không trùng pillar strategy ở trên, giữ nguyên |
| Sub-topic: pipeline | [CRM Pipeline Management](https://infina.ai/news/crm-pipeline-management/) | `crm pipeline` | Evaluation/MOF | góc riêng, chưa thấy trùng |
| Bridge → Cụm 3 | [CRM with Website Builder: Best Integrated Platforms](https://infina.ai/news/crm-with-website-builder-real-estate/) | `crm with website builder` | Evaluation/MOF | nối Cụm 3 |
| Bridge → Cụm 3 | [Real Estate CRM with IDX Integration: Best Platforms](https://infina.ai/news/real-estate-crm-with-idx/) | `real estate crm with idx` | Evaluation/MOF | nối Cụm 3 |
| Cross-link → Cụm 7 🎯 RealSaleX | [Speed-to-Lead: How Real Estate Agent CRM Closes the 15-Hour Gap](https://infina.ai/news/real-estate-agent-crm-speed-to-lead/) | `real estate agent crm` | Evaluation/MOF | = #223, dùng thay C2.2 ở Cụm 7 |
| Hỗ trợ (News) | [Rechat Just Let Claude and ChatGPT Run Real Estate CRM Workflows Directly](https://infina.ai/news/ai-agent-integration-for-real-estate-crm-platforms/) | `ai agent integration for real estate crm platforms` | Post-purchase/support | — |
| Hỗ trợ (News) | [Real's AI CRM Assistant Leo...](https://infina.ai/news/ai-crm-assistant-brokerage-merger-rollout-agents/) | `ai crm assistant brokerage merger rollout agents` | Post-purchase/support | — |
| Hỗ trợ (News) | [eXp Realty Says Its All-in-One AI Platform Cuts Software Costs by 70%](https://infina.ai/news/exp-nexus-crm-software-cost-reduction-agents/) | `exp nexus crm software cost reduction agents` | Post-purchase/support | — |
| Hỗ trợ (News) | [Nearly 10% of Borrowers Are Now Choosing ARMs...](https://infina.ai/news/arm-borrower-tracking-real-estate-agent-crm/) | `arm borrower tracking real estate agent crm` | Post-purchase/support | — |
| Hỗ trợ (News) | [Lofty Launches an MCP Server So Any AI Can Plug Into Its CRM](https://infina.ai/news/open-ai-protocol-real-estate-crm-brokerages/) | `open ai protocol real estate crm brokerages` | Post-purchase/support | — |

**Góc bắt buộc cho phần RealSaleX trong cụm này**: viết kiểu "CRM sẵn có thiếu gì mà cần thêm lớp
intent", KHÔNG viết "X vs Y CRM nào tốt hơn" — target là người đã có CRM rồi, RealSaleX bổ sung chứ
không thay thế. Internal link: pillar nhẹ ↔ C3.2 (2 chiều), pillar nhẹ ↔ #207 (pillar chính), pillar
nhẹ ↔ #214 (link chéo, không cannibalize), pillar nhẹ ↔ pillar Cụm 7 (định vị bổ sung CRM).

#### Mở rộng "Customer Engagement Platform" (CEP) — 2 bài chưa viết (2026-09-30)

**Bối cảnh**: user gửi thêm 148 keyword mới (export Google Keyword Planner) về "customer engagement
platform" (CEP), đã merge vào
`wordpress-mcp/skills/news-to-cluster-article/keywords/Infina_AI_RealSale_Keyword_Stats_2026-09-15.csv`
(commit `d0f17c3`). CEP được xác nhận là **góc định vị lại 1 phần RealSaleX**, không phải sản phẩm
tách riêng — audience vẫn brokerage/agent bất động sản Mỹ.

**Vì sao KHÔNG tạo hẳn 1 cụm "CEP" riêng** (đã cân nhắc rồi bỏ): live-SERP check cho thấy niche hóa
"customer engagement platform for real estate" đá thẳng vào sân đã có của Cụm 2 hiện tại (Sierra
Interactive, Zoho SalesIQ, Salesforce, Creatio đều frame CEP-cho-real-estate y hệt nội dung "CRM
cho real estate" đã có ở #207/#214/#230/#405). Tạo cụm mới riêng sẽ tự cannibalize nội bộ nhiều hơn
là mở ra SERP mới, nên quyết định **nhét 2 bài mới vào Cụm 2 sẵn có** (2 dòng "chưa viết" ở bảng
trên) thay vì tạo cụm 9.

**Kết quả check volume + live-SERP (2026-09-30) cho từng nhóm keyword ứng viên**:

| Nhóm keyword | Volume (tier) | Kết luận |
|---|---|---|
| `customer engagement platform`, `customer experience automation platform`, `omnichannel customer engagement platform`, `best customer engagement platform` (bare) | 500-5000 | ❌ Bỏ — SERP bị vendor tỷ đô chiếm 100% (Twilio, Salesforce, Zendesk, Braze, Talon.One, Bloomreach...), **zero** kết quả real estate dù niche hay không |
| `what is customer engagement`, `CEP customer engagement platform meaning` (bare) | 500, 50 | ❌ Bỏ — cùng lý do, toàn IBM/Salesforce/Wikipedia/Martech.zone. Lưu ý: competition index thấp (idx=1) trong file KHÔNG phản ánh độ khó SERP organic thật — đây là competition Ads, dễ gây hiểu lầm |
| `what is a customer engagement platform for real estate`, `...real estate agents need` (niche) | 500 (bare gốc) | ❌ Bỏ — SERP real estate có thật (Sierra Interactive, Zoho SalesIQ, realestatecrm.io...) nhưng nội dung đọc y hệt "CRM cho real estate" đã có → cannibalize nội bộ với #207/#214, không đáng viết bài riêng |
| `customer engagement platform vs crm` | 50, comp idx **0** | ✅ Giữ — Generic có 9+ bài (leat, courier, moengage, informatica...) nhưng **chưa site real estate nào viết bản riêng**, khớp đúng pitch RealSaleX (bổ sung CRM bằng lớp engagement/intent) |
| `digital customer engagement real estate`, `customer engagement examples real estate` (niche) | 500 (bare gốc) | ✅ Giữ — SERP real estate có thật (Spectrio, Transactly, ETG.digital, commercial-realestate-training.com) nhưng đối thủ toàn agency blog nhỏ, chưa ai làm bài resource chuẩn SEO — format listicle chiến lược/ví dụ, khác hẳn format so sánh phần mềm nên không đụng phần còn lại của Cụm 2 |

Internal link dự kiến khi viết: 2 bài CEP ↔ nhau (2 chiều), cả 2 ↔ pillar nhẹ (#1232) + #207, bài
"vs CRM" → money page RealSaleX (khi có URL).

---

### Cụm 3: Website Builder / IDX — 13 bài sống (15 gốc, 2 đã merge: case #546 cũ + case #553 2026-10-01)

| Vai trò | Bài | Focus keyword | Funnel | Trạng thái |
|---|---|---|---|---|
| **Pillar** | [Best Real Estate Website Builders for Agents and Brokers (2026)](https://infina.ai/news/real-estate-website-builder/) | `real estate website builder` | Discovery/TOF | ✅ Hub, đã hấp thụ 2 bài (case #546 cũ + case #553 2026-10-01) |
| ~~🔎 Review/list (roundup)~~ | ~~Best Real Estate Website Builder: Features, Pricing and IDX Compared~~ | `best real estate website builder` | Evaluation/MOF | ⚠️ ĐÃ MERGE (2026-10-01) vào Pillar, stub + redirect 301 live |
| Review (niche: solo agent) | [Best Real Estate Agent Website Builder for Solo Agents](https://infina.ai/news/real-estate-agent-website-builder/) | `real estate agent website builder` | Evaluation/MOF | niche rõ, rủi ro thấp |
| Review (niche: realtor) | [Best Website Builder for Realtors: Top Picks Reviewed](https://infina.ai/news/best-website-builder-for-realtors/) | `best website builder for realtors` | Evaluation/MOF | niche rõ |
| Review (niche: free) | [Free Real Estate Website Builder: What You Get vs. What You Pay For](https://infina.ai/news/free-real-estate-website-builder/) | `free real estate website builder` | Evaluation/MOF | niche rõ |
| Review (niche: investor) | [Best Website Builder for Real Estate Investors](https://infina.ai/news/best-website-builder-real-estate-investors/) | `best website builder for real estate investors` | Evaluation/MOF | niche rõ, audience khác (investor) |
| Định nghĩa (broker) | [What Is Broker IDX? Complete Guide](https://infina.ai/news/broker-idx-guide/) | `broker idx` | Discovery/TOF | audience khác dòng dưới (broker vs agent) |
| Định nghĩa (chung) | [What Is IDX in Real Estate?](https://infina.ai/news/idx-real-estate-definition-guide/) | `idx real estate` | Discovery/TOF | — |
| ✅ Review/list (roundup, HUB) | [Best IDX Website for Realtors: Top Platforms Reviewed](https://infina.ai/news/idx-website-for-realtors/) | `idx website for realtors` | Evaluation/MOF | ✅ HUB (2026-10-01) — đã hấp thụ Sierra Interactive + "How to Evaluate" từ bài dưới |
| ~~🔎 Review/list (roundup)~~ | ~~Best IDX Website for Realtors: In-Depth Platform Reviews~~ | `best idx website for realtors` | Evaluation/MOF | ⚠️ ĐÃ MERGE (2026-10-01) vào dòng trên, stub + redirect 301 live |
| Examples/inspiration | [IDX Real Estate Websites: Best Examples](https://infina.ai/news/idx-real-estate-websites-examples/) | `idx real estate websites` | Evaluation/MOF | — |
| How-to (kỹ thuật) | [IDX MLS: How the Data Feed Powers Real Estate Agent Websites](https://infina.ai/news/idx-mls-real-estate-guide/) | `idx mls` | Discovery/TOF | gần góc với dòng dưới (cùng giải thích data feed) |
| How-to (kỹ thuật) | [IDX Feed: What It Is and How to Set It Up](https://infina.ai/news/idx-feed-real-estate-setup/) | `idx feed` | Post-purchase/how-to | gần góc với dòng trên |
| Buying guide | [Real Estate Agent Websites with IDX: What to Look For Before You Buy](https://infina.ai/news/real-estate-agent-websites-with-idx/) | `real estate agent websites with idx` | Decision/BOF | — |

**3 bài đã merge trước đây**: [Real Estate Website Builder with IDX](https://infina.ai/news/real-estate-website-builder-with-idx/) → stub, redirect 301 sang Pillar #546 (case cũ). [Best IDX Website for Realtors: In-Depth Platform Reviews](https://infina.ai/news/best-idx-website-for-realtors/) → stub, redirect 301 sang `idx-website-for-realtors` (2026-10-01). [Best Real Estate Website Builder: Features, Pricing and IDX Compared](https://infina.ai/news/best-real-estate-website-builder/) → stub, redirect 301 sang Pillar `real-estate-website-builder` (2026-10-01). Xem refresh-log.md cho cả 3.

---

### Cụm 4: AI Voice / Virtual Assistant / Receptionist — 🎯 RealSaleX (🥇 ưu tiên cao nhất) — ✅ HOÀN THÀNH — 5 bài

Vì sao ưu tiên cao nhất: đúng câu pitch chính của sản phẩm ("AI agent trả lời buyer 24/7 trong Deal
Room riêng"). **Đã đổi hướng so với plan gốc sau khi check keyword + live-SERP thật (2026-09-15)**:
CSV gốc không có biến thể "real estate" nào cho cụm receptionist/call center — 5 FOCUS_KW ban đầu
đều là thuật ngữ generic. Chạy live-SERP xác nhận: `ai receptionist`/`ai call center software`
(bare) bị vendor/SaaS lớn chiếm SERP hoàn toàn; bản niche `... for real estate` mới có nhu cầu thật
(10+ đối thủ dạng listicle cho riêng "ai receptionist for real estate"). Từ đó: bỏ viết pillar/C1.2
mới, dùng #147 (đã refresh) làm pillar, chỉ viết 3 cluster với keyword niche đã verify.

| Vai trò | Bài | Focus keyword | Funnel | Trạng thái |
|---|---|---|---|---|
| **Pillar = refresh #147** | [7 Best AI Voice Assistants for Real Estate Agents](https://infina.ai/news/best-ai-voice-assistants-for-real-estate/) | `ai receptionist for real estate` | Discovery/TOF | ✅ Published (refresh 15/09) |
| So sánh | [AI Receptionist vs Human Receptionist for Real Estate: Cost & ROI](https://infina.ai/news/ai-receptionist-vs-human-receptionist-real-estate/) | `ai receptionist vs human receptionist real estate` | Evaluation/MOF | ✅ Published 16/09 |
| Buying guide | [AI Answering Service for Real Estate: How to Choose the Right One](https://infina.ai/news/ai-answering-service-for-real-estate/) | `ai answering service for real estate` | Decision/BOF | ✅ Published 17/09 |
| Support/how-to → bắc cầu Cụm 7 | [AI Outbound Calling for Real Estate: How It Works in 2026](https://infina.ai/news/ai-outbound-calling-real-estate-lead-follow-up/) | `ai outbound calling for real estate` | Post-purchase/how-to | ✅ Published 15/09 |
| Review/list (phát hiện thêm 01/10) | [7 Best AI Virtual Assistants for Real Estate](https://infina.ai/news/best-ai-virtual-assistant-real-estate/) | `ai virtual assistant real estate` | Evaluation/MOF | ✅ ĐÃ AUDIT 01/10: differentiation thật (đa kênh SMS/CRM/scheduling vs riêng voice/phone, chỉ trùng 3/7 tool) — giữ nguyên, không sửa gì |

Internal link: #147 ↔ 3 cluster (2 chiều, đã verify live). Cluster "AI Outbound Calling" ↔ pillar
Cụm 7 (chéo cụm, đã có link). Điểm khác biệt đã thêm vào #147 mà đối thủ chưa cover: mục Fair
Housing + TCPA compliance.

---

### Cụm 5: Website / Web Design — 7 bài, tất cả sống

| Vai trò | Bài | Focus keyword | Funnel | Trạng thái |
|---|---|---|---|---|
| **Pillar (HUB)** | [Real Estate Agent Website Design: What Actually Works in 2026](https://infina.ai/news/website-design-for-real-estate-agents/) | `website design for real estate agents` | Discovery/TOF | ✅ HUB (2026-10-01) — đã hấp thụ section "Common Mistakes" từ dòng dưới |
| ~~Discovery~~ | ~~Realtor Website Design: How to Stand Out and Convert More Visitors~~ | `realtor website design` | Discovery/TOF | ⚠️ ĐÃ MERGE (2026-10-01) vào Pillar, redirect 301 live |
| Examples/inspiration | [Best Real Estate Website Design: 8 Examples to Model](https://infina.ai/news/best-real-estate-website-design/) | `best real estate website design` | Evaluation/MOF | — |
| Decision (build vs buy) | [Web Design for Real Estate Agents: DIY vs. Hiring a Designer](https://infina.ai/news/web-design-for-real-estate-agents/) | `web design for real estate agents` | Decision/BOF | — |
| Buying guide (agency) | [Real Estate Web Design Companies: How to Choose the Right One](https://infina.ai/news/real-estate-web-design-companies/) | `real estate web design companies` | Decision/BOF | — |
| Review (niche: broker) | [Real Estate Broker Website Design: What Brokerage Sites Actually Need](https://infina.ai/news/real-estate-broker-website-design/) | `real estate broker website design` | Evaluation/MOF | đã refresh striking-distance 01/10 (Lofty-style keyword gap) |
| Review (niche: luxury) | [Luxury Real Estate Website Design](https://infina.ai/news/luxury-real-estate-website-design/) | `luxury real estate website design` | Evaluation/MOF | niche rõ |

---

### Cụm 6: Landing Pages — 6 bài, tất cả sống

| Vai trò | Bài | Focus keyword | Funnel | Trạng thái |
|---|---|---|---|---|
| **Pillar** | [Real Estate Landing Page: Types, Elements, and How to Build One That Converts](https://infina.ai/news/real-estate-landing-page-guide/) | `real estate landing page` | Discovery/TOF | — |
| ✅ Evaluation/MOF (cluster hợp lệ) | [High Converting Real Estate Landing Pages: What Makes Them Work](https://infina.ai/news/high-converting-real-estate-landing-pages/) | `high converting real estate landing pages` | Evaluation/MOF | ✅ ĐÃ AUDIT (2026-10-01): không trùng, là deep-dive thật của Pillar — đã fix internal link 2 chiều, không merge |
| Niche: open house | [Open House Landing Page: How to Build One That Actually Captures Leads](https://infina.ai/news/open-house-landing-page/) | `open house landing page` | Post-purchase/how-to | — |
| Niche: agent chung | [Real Estate Agent Landing Page: What to Include and How to Convert Visitors](https://infina.ai/news/real-estate-agent-landing-page/) | `real estate agent landing page` | Post-purchase/how-to | — |
| Niche: home valuation | [Home Valuation Landing Page: How to Build One That Converts Seller Leads](https://infina.ai/news/home-valuation-landing-page/) | `home valuation landing page` | Post-purchase/how-to | gần góc với dòng dưới (cùng target seller) |
| Niche: seller chung | [Seller Landing Pages Real Estate: Types That Convert](https://infina.ai/news/seller-landing-pages-real-estate/) | `seller landing pages real estate` | Post-purchase/how-to | gần góc với dòng trên |

---

### Cụm 7: Lead Generation / Follow-up Automation — 🎯 RealSaleX (🥇 ưu tiên cao nhất) — ✅ HOÀN THÀNH — 8 bài

Vì sao ưu tiên cao nhất: khớp thẳng "The Leak" trong pitch deck (40-50% lead không được follow-up).

| Vai trò | Bài | Focus keyword | Funnel | Trạng thái |
|---|---|---|---|---|
| **Pillar** | [Real Estate Lead Follow-Up Automation: The Complete 2026 Guide](https://infina.ai/news/real-estate-lead-follow-up-automation-guide/) | `real estate lead follow-up automation` | Discovery/TOF | ✅ Published 18/09 |
| Review/list | [Best Lead Generation Software for Realtors in 2026](https://infina.ai/news/best-lead-generation-software-for-realtors/) | `lead generation software for realtors` | Evaluation/MOF | ✅ Published 19/09 |
| Giải thích/pain-point = refresh #223 | [Speed-to-Lead: How Real Estate Agent CRM Closes the 15-Hour Gap](https://infina.ai/news/real-estate-agent-crm-speed-to-lead/) | `real estate agent crm` | Evaluation/MOF | ✅ #223 đã refresh 15/09, thêm link Pillar |
| Buying guide/how-to | [Automated Lead Follow-Up for Real Estate: A 5-Step Setup Guide](https://infina.ai/news/how-to-set-up-automated-lead-follow-up-real-estate/) | `automated lead follow-up for real estate` | Decision/BOF | ✅ Published 20/09 |
| Kênh cụ thể | [Facebook Lead Gen for Realtors: Turning Ad Leads Into Showings](https://infina.ai/news/facebook-lead-gen-for-realtors/) | `facebook lead gen for realtors` | Decision/BOF | ✅ Published 21/09 |
| Hỗ trợ | [Real Estate Contact Forms Are Losing the Highest-Intent Leads](https://infina.ai/news/real-estate-contact-form-conversion-rate/) | `real estate contact form conversion rate` | Post-purchase/support | — |
| Hỗ trợ (News) | [Your Next Listing Is Probably Already Sitting in Your CRM](https://infina.ai/news/database-reactivation-ai-seller-leads-real-estate-agents/) | `database reactivation ai seller leads real estate agents` | Post-purchase/support | — |
| Hỗ trợ (News) | [Realtor.com Just Named the Best Week to Buy in 2026...](https://infina.ai/news/buyer-lead-nurture-campaign-real-estate-agents/) | `buyer lead nurture campaign real estate agents` | Post-purchase/support | — |
| Hỗ trợ (News) | [Sellers Now Outnumber Buyers by 57.9%...](https://infina.ai/news/seller-lead-prioritization-real-estate-pipeline/) | `seller lead prioritization real estate pipeline` | Post-purchase/support | — |

**Đổi FOCUS_KW so với plan gốc** (bài học từ Cụm 4 — niche hoá thay vì dùng keyword generic từ CSV):
`lead generation for realestate` → `real estate lead follow-up automation` (Pillar, khớp đúng intent
bài); `lead generation software` → `lead generation software for realtors`; `lead generation
systems` → `automated lead follow-up for real estate`; `facebook lead generation ads` → `facebook
lead gen for realtors` — tất cả đã verify có SERP thật khớp định dạng dự kiến qua web search
2026-09-15.

Internal link: Pillar ↔ 3 cluster review/buying-guide/kênh (2 chiều), Pillar ↔ #223 (refresh),
Pillar ↔ cluster "AI Outbound Calling" của Cụm 4 (chéo cụm, cả 2 chiều), cluster "Facebook Lead
Gen" → #147 (mention Fair Housing/Housing Special Ad Category).

---

### Cụm 8: Compliance / Legal / Risk — 4 bài, tất cả sống

| Vai trò | Bài | Focus keyword | Funnel | Trạng thái |
|---|---|---|---|---|
| **Pillar (nhẹ)** | [TCPA Compliance for Real Estate Agents](https://infina.ai/news/tcpa-compliance-for-real-estate-agents/) | `tcpa compliance for real estate agents` | Discovery/TOF | ✅ = #237, đã link từ #147/Cụm 4/Cụm 7 |
| Hỗ trợ (News) | [AI-Written Listing Descriptions Are Creating Fair Housing Liability](https://infina.ai/news/ai-hallucination-risk-real-estate-listings/) | `ai hallucination risk real estate listings` | Post-purchase/support | — |
| Hỗ trợ (News) | [Colorado's New AI Law Sets a Deadline for Automated Decisions](https://infina.ai/news/ai-decision-making-compliance-real-estate-agents/) | `ai decision making compliance real estate agents` | Post-purchase/support | — |
| Hỗ trợ (News) | [Seller Impersonation Fraud Attempts Just Doubled](https://infina.ai/news/seller-impersonation-fraud-prevention-real-estate-agents/) | `seller impersonation fraud prevention real estate agents` | Post-purchase/support | — |

---

## Cannibalization — lịch sử audit (01/10/2026, tất cả 10 cặp đã xử lý)

Phát hiện khi map lại 8 cụm lần đầu (01/10/2026). Quy trình: đọc full nội dung từng cặp, so sánh
product/angle thật chứ không chỉ title, merge cặp nào có >60-70% nội dung trùng, giữ nguyên cặp nào
đã niche hoá đủ rõ — theo đúng `pillar-cluster-writer/SKILL.md` Bước 3.

| Ưu tiên | Cụm | Các bài nghi trùng | Kết luận |
|---|---|---|---|
| ~~1~~ | Cụm 2 | [best-crm-for-real-estate](https://infina.ai/news/best-crm-for-real-estate/) (hub mới, #207) đã hấp thụ ~~best-crm-software-real-estate-agents~~ (#384, Pillar cũ) + ~~top-crm-tools-for-real-estate-teams~~ (#412) | ✅ Đọc full nội dung 5 bài: 3/5 trùng nhau thật (cùng pool 5 platform). Merge xong, đổi vai trò Pillar từ #384 sang #207 (internal link equity có sẵn ở #207: 15 vs 2). Giữ nguyên best-crm-for-real-estate-teams-2026 (niche teams) + best-crm-buying-guide-real-estate-agents (BOF) |
| ~~2~~ | Cụm 3 | [idx-website-for-realtors](https://infina.ai/news/idx-website-for-realtors/) (hub) vs ~~best-idx-website-for-realtors~~ (merged, redirect 301 live) | ✅ Đọc full nội dung: trùng gần như toàn bộ (cùng 3/4 platform + cùng khung phân tích). Merge xong |
| ~~2~~ | Cụm 3 | [real-estate-website-builder](https://infina.ai/news/real-estate-website-builder/) (Pillar, hub) vs ~~best-real-estate-website-builder~~ (merged, redirect 301 live) | ✅ Đọc full nội dung: 5/6 platform trùng y hệt (tagline + giá + kết luận). Merge xong, giữ lại 1 FAQ "AgentFire teams vs solo" từ bài yếu |
| ~~3~~ | Cụm 2 | [crm-marketing-real-estate](https://infina.ai/news/crm-marketing-real-estate/) vs [crm-marketing-software-real-estate-guide](https://infina.ai/news/crm-marketing-software-real-estate-guide/) | ✅ Đọc full nội dung: differentiation thật (funnel 5 giai đoạn vs định nghĩa category, chỉ trùng 2/4 platform). Giữ nguyên cả 2, chỉ thêm link 2 chiều |
| ~~3~~ | Cụm 1 | [what-is-a-conversational-chatbot-real-estate](https://infina.ai/news/what-is-a-conversational-chatbot-real-estate/) (hub) vs ~~conversational-chat-real-estate~~ (merged) | ✅ Đọc full nội dung: trùng gần như hoàn toàn (y hệt 4 tool: Structurely/Ylopo rAIya/Tidio/ManyChat). Merge xong |
| ~~4~~ | Cụm 4 | [best-ai-virtual-assistant-real-estate](https://infina.ai/news/best-ai-virtual-assistant-real-estate/) vs Pillar #147 (`best-ai-voice-assistants-for-real-estate`) | ✅ Đọc full nội dung: differentiation thật (đa kênh SMS/CRM/scheduling vs riêng voice/phone, chỉ trùng 3/7 tool). Giữ nguyên cả 2, không sửa gì |
| ~~5~~ | Cụm 5 | [website-design-for-real-estate-agents](https://infina.ai/news/website-design-for-real-estate-agents/) (Pillar, hub) vs ~~realtor-website-design~~ (merged) | ✅ Đọc full nội dung: trùng gần như hoàn toàn (y hệt 3 platform: AgentFire/Real Geeks/Luxury Presence). Merge xong |
| ~~5~~ | Cụm 6 | [real-estate-landing-page-guide](https://infina.ai/news/real-estate-landing-page-guide/) (Pillar) vs [high-converting-real-estate-landing-pages](https://infina.ai/news/high-converting-real-estate-landing-pages/) (cluster) | ✅ Đọc full nội dung: KHÔNG phải duplicate, là pillar/cluster hợp lệ — chỉ thiếu internal link nên Google cannibalize. Đã fix link 2 chiều, giữ cả 2 bài |

Xem `skills/post-refresh/references/refresh-log.md` cho diễn giải đầy đủ từng case (số liệu GSC,
nội dung đã sửa, redirect đã verify).

---

## Bị loại khỏi plan (không dùng)

- **Local-intent** ("realtor near me"...) — khớp SERP local pack, sai định dạng site.
- **Consumer FSBO/tìm agent** ("sell house without realtor"...) — sai audience (người mua/bán nhà,
  không phải broker/agent).
- **Document/Transaction Management** — sản phẩm hoạt động ở giai đoạn buyer tìm hiểu/so sánh,
  không phải giai đoạn ký hợp đồng.
- **Cụm "CRM Software generic"** — #230 và #405 đã cover đúng góc "CRM là gì / CRM 101" mà hướng
  này định làm, không tạo pillar riêng, không giữ backlog (đã gộp làm 2 dòng trong Cụm 2).
- **Cụm "Customer Engagement Platform" riêng** — cannibalize với Cụm 2, gộp 2 bài vào thay vì tách
  cụm (xem "Mở rộng CEP" ở Cụm 2).

---

## Việc còn lại (toàn plan)

1. **Money page URL**: RealSaleX chưa deploy trên `infina.ai`. Khi có URL thật, quay lại cả 9 bài
   RealSaleX (Cụm 2/4/7) để thêm internal link tới money page (hiện tất cả đang ghi "chờ URL").
2. **GSC/GA4 credentials**: đã có key thật, lưu session-only (repo public, không commit key) — cần
   check lại traffic/ranking định kỳ dùng skill `post-refresh`.
3. **Mở rộng plan nếu cần thêm bài**: hạ ngưỡng volume CSV xuống dưới 500, hoặc dùng `post-refresh`
   tìm striking-distance keyword mới nảy sinh từ dữ liệu GSC thật.
4. **`references/used-keywords.md`**: cần cập nhật dần khi có bài mới publish (chuyển từ bảng
   "reserved" sang bảng "đã publish").
5. **Viết 2 bài CEP** (Cụm 2, góc Customer Engagement Platform) — plan đã duyệt 30/09, chưa viết
   bài thật. Theo đúng quy trình `skills/pillar-cluster-writer/SKILL.md` Bước 5 trở đi.
6. **Cụm 1 còn 1 cặp nghi trùng chưa audit**: "7 Best Chatbot Builders" vs "Best No-Code Chatbot
   Platform" — impression thấp, chưa ưu tiên.
7. **Cụm 6 còn 1 cặp nghi trùng nhẹ chưa audit**: "Home Valuation Landing Page" vs "Seller Landing
   Pages" — cùng target seller, impression thấp, chưa ưu tiên.
