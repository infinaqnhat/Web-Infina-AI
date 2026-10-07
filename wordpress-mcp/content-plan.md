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

### Vá 35 trang mồ côi (plan 2026-10-07)

**Phát hiện**: chạy `scripts/competitor_teardown.py` trên chính site, 35/130 trang (27%) không nhận
một internal link nào từ bài khác. Đã verify lại bằng REST trên 143 bài live, không phải lỗi crawl.

**Nguyên nhân gốc**: skill `news-to-cluster-article` kết thúc ở Bước 7 (log tracker). Không có bước
nào thêm link NGƯỢC từ pillar xuống bài mới. Mỗi bài News viết ra tự link lên pillar rồi nằm im,
nên mồ côi tích tụ dần theo từng bài publish.

**Phân loại 35 trang:**

| Nhóm | Số | Xử lý |
|---|---|---|
| A. Bài bất động sản mồ côi | 23 | Vá link, chia 2 batch dưới |
| B. Bài AI/tech lạc chủ đề (06-07/2026, ID #14-#53) | 11 | Cần quyết định riêng, xem cuối |
| C. Trang index `/news` | 1 | Không phải mồ côi, bỏ qua |

---

#### Batch 1: sửa 5 trang, vá được 17/23 bài

Cả 5 đích đều là hub/pillar thật, nên link xuống vừa đúng chuẩn pillar-cluster vừa truyền được
authority. Mỗi lần sửa là nối thêm link vào đoạn "Related Reading" có sẵn, không viết lại bài.

| Sửa trang | Thêm link tới |
|---|---|
| `ai-crm-real-estate` | ai-back-office-automation-real-estate-brokerages, ai-chief-of-staff-for-real-estate-agents, ai-deployment-maturity-real-estate-firms, ai-likely-to-sell-alerts-real-estate-agents, crm-for-real-estate-agents, real-estate-ai-adoption-statistics-2026 |
| `real-estate-agent-crm-speed-to-lead` | ai-home-valuation-tool-real-estate-agent-website, ai-powered-follow-up-messages-real-estate-agents, google-home-listing-ads-real-estate-agent-leads, mortgage-rate-spike-real-estate-agent-response |
| `crm-pipeline-management` | ai-relationship-manager-for-real-estate-leads, ai-usage-without-measurable-impact-real-estate-agents, financing-readiness-signals-for-real-estate-buyer-leads |
| `best-ai-virtual-assistant-real-estate` | ai-digital-human-brokerage-website-adoption, ai-job-substitution-risk-real-estate-agents |
| `crm-management-real-estate-agents-beginners-guide` | ai-academy-role-based-learning-mls-subscribers, ai-video-marketing-automation-real-estate-agents |

⚠️ `crm-for-real-estate-agents` (#247, Cụm 2, publish 01/08) là **bài cluster thật chứ không phải
News**, mồ côi từ đầu. Ưu tiên cao nhất trong batch này.

#### Batch 2: 6 bài còn lại, KHÔNG route về bài News anh em

Thuật toán phủ tối thiểu gợi ý sửa 6 bài News khác, nhưng News trỏ News thì gần như không truyền
authority. Route thẳng về pillar đúng chủ đề thay vì theo link có sẵn:

| Bài mồ côi | Pillar nên trỏ xuống |
|---|---|
| ai-contract-data-extraction-closing-automation-agents | #237 TCPA (Cụm 8) hoặc #207 |
| mls-ai-conversational-search-broker-attribution-agents | pillar Cụm 1 Chatbot |
| chatgpt-app-mortgage-matchup-real-estate-agent-visibility | pillar Cụm 5 Website / Web Design |
| chatgpt-sycophantic-pricing-advice-real-estate-agents | #147 AI Voice (Cụm 4) |
| agentic-ai-risk-concerns-real-estate-brokerage-leaders | #237 TCPA (Cụm 8) |
| ai-flat-fee-brokerage-model-real-estate-agents | #207 CRM (Cụm 2) |

#### Batch 3: 11 bài lạc chủ đề, cần bạn quyết

`ai-cannot-learn-while-it-works`, `claude-fable-5-is-back`, `is-openai-in-trouble`,
`claude-code-just-shipped-artifacts`, `genai-economy-first-revenue-number`,
`microsoft-just-sent-6000-engineers-into-enterprise-buildings`,
`most-ai-tools-stop-working-when-you-close-your-laptop`,
`the-u-s-governments-reported-ban-on-foreign-access-to-anthropics-models`,
`ai-just-moved-from-a-separate-tab-into-your-slack`,
`claude-code-has-500000-lines-of-code-only-1-6-of-it-is-actually-ai`,
`yc-spring-2026-the-agent-economy-has-actuaries-now`

Đây là tin AI/tech chung từ 06-07/2026, có trước khi site chuyển hẳn sang bất động sản. Không thuộc
cụm nào và không nên thuộc cụm nào. Vá link cho chúng sẽ làm loãng topical authority bất động sản
chứ không giúp gì. Ba lựa chọn: để nguyên, `noindex`, hoặc gỡ.

---

#### Chặn tái diễn: ✅ ĐÃ LÀM 2026-10-07

Đã thêm **Bước 6.5** vào `news-to-cluster-article/SKILL.md`, nằm giữa Bước 6 (publish) và Bước 7
(log tracker), đánh dấu BẮT BUỘC:

1. Fetch full content hiện tại của PILLAR_URL (vì `update_post` ghi đè toàn bộ `content`).
2. Nối 1 câu vào đoạn "Related Reading" có sẵn, anchor text chứa FOCUS_KW của bài mới.
3. Verify 2 chiều bằng REST, có sẵn hàm `linked()` trong skill, đã test trên cặp #237 ↔ #1501.
4. Bài `status: future` thì hoãn bước này tới sau giờ publish, không trỏ pillar vào URL còn 404.
5. Mỗi 10-15 bài, chạy lại script teardown trên chính site để đếm trang `IN=0`, số đó phải đi ngang
   hoặc giảm.

Còn lại Batch 1, 2, 3 bên dưới là phần vá 35 trang đã mồ côi sẵn.

---

### Cụm 1: Chatbot / Conversational AI, 14 bài sống (19 gốc, 5 đã merge 01/10/2026)

Cụm đã audit + xử lý cannibalization đầy đủ (xem refresh-log.md). Có **2 pillar song song** vì 2
góc đủ khác biệt để không cần gộp chung: Pillar A nhắm "conversational AI / lead follow-up bot",
Pillar B nhắm "customer service platform" (rộng hơn, bao cả tool CS tổng quát như Zendesk/Intercom).

**Internal link đã verify + fix (01/10/2026)**: phát hiện link nội bộ claimed trong content map
trước đó phần lớn chưa từng được verify thật (chỉ 1/11 cluster article thực sự link ngược về đúng
pillar của nó). Đã fetch live content qua WP REST API, xác nhận và vá thiếu link 2 chiều cho cả 12
bài (2 pillar + 10 cluster) — xem chi tiết refresh-log.md. 7 cụm còn lại (CRM, Landing Pages, AI
Voice, Website Design, Website Builder, IDX, Lead Gen) **chưa verify link thật**, không nên tin nhãn
"exist" cũ trong artifact cho các cụm đó cho tới khi được check lại.

**Keyword research mới (2026-10-01)**: user gửi thêm ~1520 keyword export (Google Keyword Planner)
về chủ đề "chatbot" và "conversational AI" nói chung, đã merge vào file keyword stats (1486 keyword
mới/không trùng, tổng file giờ 11158 dòng). Đã rà soát: **chỉ có 1 keyword thật sự niche real estate
trong toàn bộ data mới** (`conversational ai for real estate`, vol 50, comp idx 2 — tình cờ đã là
focus keyword của Pillar A, không phát hiện gap mới). ~1485 keyword còn lại là market research
chung cho "chatbot/conversational AI" (ứng dụng học ngoại ngữ, tool enterprise như Amazon Connect/
Azure/AWS, app chat AI tiêu dùng...) — không niche real estate, **chưa thấy cơ hội bài mới nào từ
đợt keyword này** (khác hẳn đợt CEP trước, lúc đó tìm ra 2 bài mới rõ ràng). Giữ nguyên plan Cụm 1
hiện tại, không thêm bài.

| Vai trò | Bài | Focus keyword | Funnel | Trạng thái |
|---|---|---|---|---|
| **Pillar A** | [Best Conversational AI Chatbots for Real Estate Agents in 2026](https://infina.ai/news/best-conversational-ai-chatbot-for-real-estate/) | `best conversational ai chatbot for real estate` | Discovery/TOF | ✅ Hub (đã hấp thụ 2 bài, 11 tool) |
| **Pillar B** | [12 Best Chatbot Customer Service Tools for Real Estate](https://infina.ai/news/best-chatbot-customer-service-real-estate/) | `chatbot customer service real estate` | Discovery/TOF | ✅ Hub (đã hấp thụ 2 bài, 15 tool) |
| ✅ Review/list (HUB) | [10 Best Chatbot Builders for Real Estate](https://infina.ai/news/best-chatbot-builder-real-estate/) | `chatbot builder real estate` | Evaluation/MOF | ✅ HUB (2026-10-01) — đã hấp thụ Chatfuel/GoHighLevel/Botsonic từ bài dưới |
| ~~Review/list~~ | ~~Best No-Code Chatbot Platform for Real Estate Websites in 2026~~ | `no code chatbot platform real estate` | Evaluation/MOF | ⚠️ ĐÃ MERGE (2026-10-01) vào dòng trên, redirect 301 live |
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

### Cụm 2: CRM Software, 🎯 RealSaleX (góc "CRM Add-on / Alternatives & Pricing"), 23 bài sống (22 gốc, 2 đã merge 2026-10-01, +3 bài lấp gap publish 02-04/10)

**✅ ĐÃ AUDIT (2026-10-01)** — cụm cannibalization LỚN NHẤT đã xử lý xong, xem refresh-log.md.
Phát hiện 5 bài "best/top CRM" roundup trùng gần hết cùng 1 pool platform (Follow Up Boss/Lofty/
Wise Agent/LionDesk/kvCORE). 3 bài (#384 Pillar cũ, #207, #412) là duplicate thật → gộp vào #207

**Internal link đã verify + fix (02/10/2026)**: tiếp nối việc verify Cụm 1 — check link thật qua WP
REST API cho cả 20 bài (2 pillar + 18 cluster). Internal link ở cụm này tốt hơn hẳn Cụm 1 (phần lớn
cluster đã tự link về pillar sẵn), nhưng vẫn thiếu: Pillar chính #207 chỉ link thật tới 1/13 cluster
claimed, Pillar nhẹ #1232 thiếu 3/5. Đã vá xong 8 bài (2 pillar + 6 cluster) — xem chi tiết refresh-log.md.
Phát hiện thêm: vài bài (#1026, #1184, #1329) link qua slug stub cũ (#384/#412 trước khi merge 01/10)
thay vì thẳng pillar hiện tại — vẫn chạy được nhờ redirect 301 nhưng đã đổi sang link trực tiếp. 6 cụm
còn lại (Landing Pages, AI Voice, Website Design, Website Builder, IDX, Lead Gen) **chưa verify link thật**.
(đổi vai trò hub từ #384 sang #207 vì #207 có sẵn 15 inbound link sitewide, #384 chỉ có 2). 2 bài
còn lại (#419 teams-niche, #444 buying-guide/BOF) giữ nguyên vì differentiation thật.

| Vai trò | Bài | Focus keyword | Funnel | Trạng thái |
|---|---|---|---|---|
| **Pillar chính (ĐÃ ĐỔI 01/10)** | [Best Real Estate Agent CRM Software in 2026](https://infina.ai/news/best-crm-for-real-estate/) | `best crm for real estate` | Evaluation/MOF | ✅ = #207, giờ là HUB — đã hấp thụ #384 (Intent Layer section) + #412 (Integrations section) |
| ~~Pillar chính (cũ)~~ | ~~Best CRM Software for Real Estate Agents~~ | `best crm software` | Discovery/TOF | ⚠️ ĐÃ MERGE (2026-10-01) vào #207, redirect 301 live |
| **Pillar nhẹ 🎯 RealSaleX** | [AI Intent Layer for Real Estate CRM: What It Adds](https://infina.ai/news/ai-intent-layer-for-real-estate-crm/) | `ai intent layer for real estate crm` | Evaluation/MOF | ✅ góc "bổ sung CRM sẵn có", khác hẳn roundup — đã sửa link trỏ về #207 thay vì #384 |
| Review (brand cụ thể) 🎯 RealSaleX | [CINC CRM Review: Pricing, Features, and Buyer Follow-Up Gaps](https://infina.ai/news/cinc-crm-review-real-estate/) | `cinc crm review` | Evaluation/MOF | ✅ cluster của pillar nhẹ — đã sửa link trỏ về #207 thay vì #384 |
| Review (brand cụ thể) 🎯 RealSaleX | [Follow Up Boss Real Estate CRM Review: Pricing, Features, and the Follow-Up Gap](https://infina.ai/news/follow-up-boss-real-estate-crm/) | `follow up boss real estate crm` | Evaluation/MOF | ✅ Published 02/10 = #1449, 1.539 từ, density 0.65%, 2 bảng giá + 3 ảnh AI. Link ra #207/#444/#1232/#1234/#1223 |
| Review/list (niche: broker) | [Real Estate Broker CRM: What Brokerages Need That Agent CRMs Miss](https://infina.ai/news/real-estate-broker-crm/) | `real estate broker crm` | Evaluation/MOF | ✅ Published 04/10 = #1462, 1.559 từ, density 0.83%. SERP check vs #419: 0 URL trùng. Có H2 riêng "Broker CRM vs Team CRM" phân tuyến. Link ngược đã verify live 06/10: #207 ✅, #419 ✅, #237 ✅ (link cross-cluster 2 chiều, bổ sung 06/10) |
| Định nghĩa (niche RE) | [What Does CRM Mean in Real Estate? A Plain-English Guide for Agents](https://infina.ai/news/what-does-crm-mean-in-real-estate/) | `what does crm mean in real estate` | Discovery/TOF | ✅ Published 03/10 = #1458, 1.141 từ, density 0.61%. SERP check: 0 URL trùng với #230 nên không cannibalize. Link ngược đã verify live 06/10: #230 ✅, #207 ✅, #405 ✅, đủ cả 3 chiều |
| So sánh (MOF) 🎯 RealSaleX | [Customer Engagement Platform vs CRM for Real Estate: Where Each One Stops](https://infina.ai/news/customer-engagement-platform-vs-crm/) | `customer engagement platform vs crm` | Evaluation/MOF | 🕐 Scheduled 07/10 10:00 = #1487, 1.341 từ, density 0,60%. SERP generic sạch real estate (leat, cxtoday, courier, flarelane, salesmanago). External link: NAR REALTORS Technology Report (52% agent dùng AI soạn email follow-up, verify first-hand). Ảnh: 3/3 đã gắn (1 HERO ảnh người 35mm + 2 infographic phẳng). ⏳ còn link ngược từ #207/#1232 (chờ bài live) |
| Listicle chiến lược (TOF) 🎯 RealSaleX | [Real Estate Customer Engagement: 7 Tactics That Earn a Reply](https://infina.ai/news/real-estate-customer-engagement-strategies/) | `real estate customer engagement` | Discovery/TOF | 🕐 Scheduled 08/10 10:00 = #1488, 1.184 từ, density 0,59%. Chốt FOCUS_KW trong nhóm đã duyệt 30/09 (`digital customer engagement` + `customer engagement examples`), chọn biến thể 4 từ vì cụm 5 từ không lặp tự nhiên đủ để đạt sàn density. SERP: easysend, brillio, twilio, MRI, Sierra glossary, 0 URL trùng với SERP #1487 và 0 URL trùng với SERP bài chatbot customer service. Ảnh: 3/3 đã gắn (1 HERO ảnh người 35mm + 2 infographic phẳng). ⏳ còn link ngược từ #207/#1232 (chờ bài live) |
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

**Keyword research mới (2026-10-02)**: user gửi thêm 456 keyword export (Google Keyword Planner)
về chủ đề "real estate CRM", đã merge vào file keyword stats (394 keyword mới/không trùng, 62 đã
có sẵn; tổng file giờ 11552 dòng). Khác 2 batch trước, đây là **export theo geo Hoa Kỳ với volume
thực tế** (5.000 / 500 / 50) chứ không phải số liệu bị thổi phồng của export cũ — chính xác hơn
cho thị trường US đang target.

Rà soát 31 keyword có volume ≥500/tháng: **phần lớn đã được phủ về ngữ nghĩa** bởi các bài hiện có,
KHÔNG nên viết bài mới vì sẽ cannibalize — `real estate crm` / `best real estate crm` /
`real estate crm software|systems|programs` (5.000/mo) trùng intent pillar chính #207; `crm real
estate meaning` / `what does crm mean in real estate` trùng #230 + #405; `free real estate crm`
trùng bài free-CRM; `real estate crm with website` trùng bridge `crm-with-website-builder-real-estate`.

**Gap thật sự phát hiện được — nhóm competitor/brand keyword** (chưa có bài nào, đúng góc "CRM
Add-on / Alternatives & Pricing" đã chốt cho RealSaleX ở cụm này): `follow up boss real estate crm`
(5.000/mo, competition Thấp — cơ hội lớn nhất), `lofty real estate crm`, `zoho real estate crm`,
`hubspot real estate crm`, `salesforce real estate crm` (mỗi cái 500/mo), cùng `real estate crm cost`
và `real estate crm pricing` (500/mo, đúng mảng "Pricing" trong định vị cụm).

#### Mở rộng "CRM gap từ US keyword data", 3 bài, đã publish xong (plan 2026-10-02, publish 02-04/10)

**Bối cảnh**: từ batch 394 keyword US-geo merge ngày 02/10, rà soát toàn bộ 378 keyword US-relevant
(đã lọc geo Ấn/Dubai/Úc + nhóm job/tuyển dụng) và map với 20 bài sống của cụm. Phần lớn keyword
volume cao là **biến thể roundup** của pillar #207 (`real estate crm`, `best real estate crm`,
`real estate crm software|systems|programs`, `top 10 real estate crm` — tổng ~25.000/mo) → **KHÔNG
viết bài mới**, chỉ tối ưu on-page #207 để hứng biến thể (xem mục "Việc on-page" bên dưới). Sau khi
loại nhóm đó, còn đúng 3 gap thật đáng viết bài riêng.

**Live-SERP check (2026-10-02)** — theo đúng quy trình đã áp dụng cho batch CEP:

| Nhóm keyword | Volume | SERP thật | Kết luận |
|---|---|---|---|
| `follow up boss real estate crm` + `fub real estate crm` | 5.050, comp **Thấp** | Capterra (nhiều ccTLD = trang intl yếu), FitSmallBusiness, SoftwarePundit, Google Workspace Marketplace. Biến thể "alternatives" còn yếu hơn: goliathdata, theaicareerlab, costbench, stackscored — toàn aggregator chất lượng thấp | ✅ Viết — **chưa publisher real-estate-native nào sở hữu SERP này**, mà FUB lại là CRM phổ biến nhất trong nhóm khách RealSaleX nhắm (người đã có CRM) |
| `real estate broker crm` + `real estate crm for brokers` | 5.050 | Toàn trang vendor (TotalBrokerage, Propertybase, Wise Agent broker page, BrokerSmart, ClientEdge) + softwarefinder, sell.do (Ấn). Chỉ Zapier có bài editorial | ✅ Viết — SERP thiếu hẳn bài editorial trung lập, và nhu cầu brokerage (roster, chia hoa hồng, back-office) khác thật so với agent/team |
| `what does crm mean in real estate` + 15 biến thể định nghĩa | 3.000 | Nimble, Luxury Presence, Empire Learning, MRI, Blaze, Zenu (Úc), Planfix — vendor blog + 1 site đào tạo RE, không ai thống trị | ✅ Viết — TOF dễ rank nhất, và #230 hiện tại viết **generic cho mọi business**, không niche real estate |
| `commercial real estate crm` (5 kw) | 1.150 | — | ❌ Bỏ — sạch gap nhưng **lệch ICP**: broker thương mại ≠ agent residential mà RealSaleX nhắm |
| `yardi`, `mri`, `valuation`, `rental`, `underwriting software` | ~1.500 | — | ❌ Bỏ — property management/enterprise software, sai audience hoàn toàn |
| DIY template (`excel`, `google sheets`, `notion`, `open source`) | 600 | — | ❌ Bỏ — intent là người *không* muốn trả tiền cho CRM, lead chất lượng thấp |

**Bài 1 — Follow Up Boss review** (ưu tiên cao nhất: volume lớn nhất + competition thấp nhất)
- FOCUS_KW: `follow up boss real estate crm` · phụ: `fub real estate crm`, `real estate crm pricing`
- SEO_TITLE dự kiến: *Follow Up Boss Real Estate CRM Review: Pricing, Features, and the Follow-Up Gap*
- Vai trò/funnel: Review (brand cụ thể) 🎯 RealSaleX — **dùng đúng format #1234 (CINC review)**, Evaluation/MOF
- Góc bắt buộc: theo rule cụm — KHÔNG viết "FUB vs X cái nào tốt hơn". Viết "FUB mạnh ở đâu, hổng
  chỗ nào (không có lớp intent/dự đoán), RealSaleX bổ sung lên trên FUB". Target chính là người
  **đang dùng FUB rồi**, không phải người đang chọn CRM đầu tiên.
- Outline H2: (1) What Follow Up Boss Is Built For — lead routing, 250+ integration, cấu trúc team ·
  (2) Follow Up Boss Pricing in 2026 — Grow $69/user, Pro $499/10 user, Platform $1.000/30 user ·
  (3) What Follow Up Boss Does Well · (4) Where Follow Up Boss Leaves Gaps — reactive chứ không
  predictive, chi phí/user đau với solo agent · (5) Who Should Still Use Follow Up Boss ·
  (6) Adding an Intent Layer on Top of Follow Up Boss ← pitch RealSaleX · (7) Related Reading
- Internal link: → #207 (pillar chính), → #1232 (pillar nhẹ, 2 chiều), → #1234 (CINC review, cross
  review 2 chiều), → #1223 (pillar Cụm 7, vì FUB là công cụ follow-up)

**Bài 2 — Real estate broker CRM** (volume ngang bài 1 nhưng công viết nặng hơn)
- FOCUS_KW: `real estate broker crm` · phụ: `real estate crm for brokers`, `best real estate crm system`
- SEO_TITLE dự kiến: *Real Estate Broker CRM: What Brokerages Need That Agent CRMs Miss*
- Vai trò/funnel: Review/list (niche: broker), Evaluation/MOF
- ⚠️ **Chống cannibalize với #419** (`best crm for real estate teams`): phải phân tuyến rõ ngay
  trong bài — #419 nhắm **team leader trong 1 brokerage** (5-20 agent, chủ yếu lo lead routing);
  bài này nhắm **chủ brokerage** (50+ agent, lo roster/onboarding agent, chia hoa hồng, lưu trữ hồ
  sơ tuân thủ, transaction back-office, giữ chân/tuyển agent). Dành hẳn 1 H2 để tách 2 nhu cầu này.
- Outline H2: (1) What a Real Estate Broker CRM Has to Do That an Agent CRM Does Not · (2) Agent
  Roster, Lead Distribution, and Commission Splits · (3) Compliance and Record Retention at the
  Brokerage Level ← cầu nối Cụm 8 · (4) Best Real Estate Broker CRM Platforms in 2026 —
  TotalBrokerage, Lone Wolf/Propertybase, BoldTrail, Wise Agent (broker tier), Sierra Interactive ·
  (5) Broker CRM vs Team CRM: Which One You Actually Need ← H2 xử lý cannibalization ·
  (6) What Brokerage CRMs Still Do Not Do ← pitch RealSaleX
- Internal link: → #207, → #419 (2 chiều, bắt buộc để Google phân biệt 2 intent), → #237 (Cụm 8
  compliance), → #1232

**Bài 3 — CRM nghĩa là gì trong real estate** (dễ rank nhất, nên viết sớm để gom traffic TOF)
- FOCUS_KW: `what does crm mean in real estate` (chọn biến thể câu hỏi vì tự nhiên trong title +
  dễ ăn featured snippet) · phụ gom vào H2/body: `crm real estate meaning`, `real estate crm
  meaning`, `meaning of crm in real estate`, `crm full form in real estate`, `real estate crm
  definition`, `what is real estate crm software`, `crm used in real estate`, `role of crm in real estate`
- SEO_TITLE dự kiến: *What Does CRM Mean in Real Estate? A Plain-English Guide for Agents*
- Vai trò/funnel: Định nghĩa (niche real estate), Discovery/TOF
- ⚠️ **Chống cannibalize với #230** (`what is crm software`): #230 định nghĩa CRM cho **mọi loại
  hình doanh nghiệp** (H2 hiện tại toàn "Types of CRM Software", "Top CRM Software Platforms"), bài
  mới chỉ nói **CRM trong ngữ cảnh bất động sản**. Link 2 chiều và nêu thẳng phạm vi khác nhau.
- Outline H2: (1) What Does CRM Mean in Real Estate? — đoạn định nghĩa ngắn tối ưu snippet, kèm
  "CRM full form" = Customer Relationship Management · (2) What a Real Estate CRM Actually Stores —
  contact + mức quan tâm bất động sản + nguồn lead + hoạt động MLS/IDX (chỗ khác biệt lớn nhất so
  với CRM generic) · (3) How a Real Estate CRM Differs From a Generic Business CRM ← chỗ link #230 ·
  (4) What Agents Use a CRM For Day to Day · (5) Do You Need a CRM as a New Agent? ← hứng
  `best crm for new real estate agents` · (6) Related Reading
- Internal link: → #207, → #230 (2 chiều), → #405 (beginner guide), → #214

**Thứ tự viết đề xuất**: Bài 3 (dễ nhất, gom TOF) → Bài 1 (ROI cao nhất) → Bài 2 (nặng nhất).

**Kết quả thực tế (cập nhật 2026-10-06)**: viết xong cả 3, thứ tự publish là Bài 1 → Bài 3 → Bài 2
do rule tối đa 3 bài/ngày và giờ publish 10:00 cho bài evergreen.

| Bài | Post | Publish | Số từ | Density | Link ngược đã verify live 06/10 |
|---|---|---|---|---|---|
| Bài 1 Follow Up Boss | #1449 | 02/10 | 1.539 | 0,65% | #207, #1232, #1234, #1223 |
| Bài 3 Định nghĩa CRM | #1458 | 03/10 | 1.141 | 0,61% | #230, #207, #405 (đủ 3/3) |
| Bài 2 Broker CRM | #1462 | 04/10 | 1.559 | 0,83% | #207, #419, #237 (đủ 3/3) |

✅ **Nhóm này đã khép hoàn toàn (06/10)**: link cuối cùng còn thiếu là #237 → #1462 đã bổ sung, đặt
trong H2 "TCPA Compliance for Real Estate Agents in Practice" với góc lưu trữ hồ sơ consent ở cấp
brokerage. Anchor text dùng đúng FOCUS_KW `real estate broker crm`. Density của #237 sau khi thêm
đoạn: 0,61% (7 lần / 1.154 từ), vẫn trong ngưỡng Rank Math 0,5-2,5%.

**Việc on-page kèm theo (không phải bài mới)**: bổ sung biến thể `real estate crm systems`,
`real estate crm programs`, `real estate crm platforms`, `top 10 real estate crm` vào title tag/H2
của #207 để pillar tự hứng ~25.000/mo biến thể roundup thay vì tách bài gây cannibalize.

#### Mở rộng "Customer Engagement Platform" (CEP), 2 bài, đã viết xong (plan 2026-09-30, scheduled 07-08/10)

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

**Kết quả thực tế (2026-10-06)**: viết xong cả 2, scheduled vào slot evergreen 10:00.

| Bài | Post | Scheduled | FOCUS_KW | Số từ | Density |
|---|---|---|---|---|---|
| So sánh (MOF) | #1487 | 07/10 10:00 | `customer engagement platform vs crm` | 1.341 | 0,60% |
| Listicle (TOF) | #1488 | 08/10 10:00 | `real estate customer engagement` | 1.184 | 0,59% |

Link 2 chiều giữa 2 bài đã xong ngay khi tạo (#1488 → #1487 trong H2 "Do You Need Software",
#1487 → #1488 ở đoạn kết). Cả 2 đều trỏ lên #207 và #1232, cộng link chéo sang #237 (TCPA) và
#1223 (Cụm 7). External link của cả 2 là NAR REALTORS Technology Report, đọc trực tiếp từ trang
NAR chứ không lấy qua search summary.

**Ảnh (2026-10-06)**: 6/6 ảnh đã generate và gắn xong. Key Gemini lấy từ Google Drive folder "Key"
theo đúng nguồn credential ghi trong `post-refresh/SKILL.md`, không phải từ thư mục uploads đã mất
khi container được cấp lại ngày 05/10. Mỗi bài 1 HERO ảnh người 35mm + 2 infographic phẳng
navy/xanh, không chữ trong ảnh, alt của cả 6 ảnh đều chứa FOCUS_KW của bài tương ứng. Ảnh metrics
của #1488 phải generate lại 1 lần vì viền thẻ ra không liền, có bậc thừa ở 2 cạnh bên.

⏳ **Việc còn lại của nhóm này**: link ngược từ #207 và #1232 xuống 2 bài này, để sau khi bài live
thật thay vì trỏ vào URL còn 404. Đã hẹn self check-in 07/10 10:15 và 08/10 10:15 để làm.

---

### Cụm 3: Website Builder / IDX, 14 bài sống (15 gốc, 2 đã merge: case #546 cũ + case #553 2026-10-01, +1 bài News publish 03/10)

**Internal link đã verify + fix (02/10/2026)**: check link thật qua WP REST API cho 12 bài live tìm
thấy (chênh 1 so với "13 bài sống" ghi ở trên, không ảnh hưởng việc fix). Cluster→pillar chính #546
vốn đã tốt (11/11 tự link sẵn), nhưng pillar #546 chỉ link ra 1/10 cluster, và IDX sub-hub #610 (dòng
"✅ HUB 2026-10-01" bên dưới) hoàn toàn không được 5 bài IDX khác trỏ về. Đã vá xong 7 bài — xem chi
tiết refresh-log.md. 3 cụm còn lại (Website Design, Lead Generation, Compliance) **chưa verify link thật**.

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
| Hỗ trợ (News) | [Compass Gave an MLS Until October 6, and Agent Search Sites Are Caught in the Middle](https://infina.ai/news/off-mls-listings-on-agent-idx-websites/) | `off mls listings on agent idx websites` | Post-purchase/support | ✅ Published 03/10 = #1473. Góc: listing ngoài MLS không vào được IDX feed. Category 153 "Real Estate Websites" (SKILL.md chưa liệt kê ID này) |

**3 bài đã merge trước đây**: [Real Estate Website Builder with IDX](https://infina.ai/news/real-estate-website-builder-with-idx/) → stub, redirect 301 sang Pillar #546 (case cũ). [Best IDX Website for Realtors: In-Depth Platform Reviews](https://infina.ai/news/best-idx-website-for-realtors/) → stub, redirect 301 sang `idx-website-for-realtors` (2026-10-01). [Best Real Estate Website Builder: Features, Pricing and IDX Compared](https://infina.ai/news/best-real-estate-website-builder/) → stub, redirect 301 sang Pillar `real-estate-website-builder` (2026-10-01). Xem refresh-log.md cho cả 3.

---

### Cụm 4: AI Voice / Virtual Assistant / Receptionist, 🎯 RealSaleX (🥇 ưu tiên cao nhất), ✅ HOÀN THÀNH, 6 bài (+1 bài News publish 02/10)

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
| Hỗ trợ (News) | [Nearly 1 in 5 Homes Cut Price in September, and Agents Are Running Out of Call Hours](https://infina.ai/news/ai-voice-calls-for-listing-price-updates/) | `ai voice calls for listing price updates` | Post-purchase/support | ✅ Published 02/10 = #1467. Pillar #147 lần đầu được dùng làm PILLAR_URL cho bài News (đa dạng link equity) |

Internal link: #147 ↔ 3 cluster (2 chiều, đã verify live). Cluster "AI Outbound Calling" ↔ pillar
Cụm 7 (chéo cụm, đã có link). Điểm khác biệt đã thêm vào #147 mà đối thủ chưa cover: mục Fair
Housing + TCPA compliance.

**Internal link re-verify (02/10/2026)**: check lại qua WP REST API — claim "đã verify live" ở trên
gần đúng, chỉ thiếu pillar #147 chưa link tới #1217 và #1219 (2/4 bài). Đã thêm, giờ pillar link đủ
cả 4 bài (3 cluster + #110). Xem chi tiết refresh-log.md.

---

### Cụm 5: Website / Web Design, 7 bài, tất cả sống

**Internal link đã verify + fix (02/10/2026)**: check link thật qua WP REST API cho cả 6 bài. Chiều
cluster→pillar đã tốt sẵn (5/5), chỉ pillar #975 thiếu link ra 4/5 cluster. Đã vá xong — xem chi tiết
refresh-log.md. Còn 1 cụm chưa verify: Compliance/Legal/Risk (Cụm 8).

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

### Cụm 6: Landing Pages, 6 bài, tất cả sống

**Internal link đã verify + fix (02/10/2026)**: check link thật qua WP REST API cho cả 6 bài. Pillar
thiếu link tới 3/5 cluster (#924, #936, #942); 4/5 cluster (#918, #924, #936, #942) thiếu link ngược
về pillar dù content-plan claim đã có. Đã vá xong toàn bộ — xem chi tiết refresh-log.md. 5 cụm còn
lại (Website Builder/IDX, AI Voice, Website Design, Lead Generation, Compliance) **chưa verify link thật**.

| Vai trò | Bài | Focus keyword | Funnel | Trạng thái |
|---|---|---|---|---|
| **Pillar** | [Real Estate Landing Page: Types, Elements, and How to Build One That Converts](https://infina.ai/news/real-estate-landing-page-guide/) | `real estate landing page` | Discovery/TOF | — |
| ✅ Evaluation/MOF (cluster hợp lệ) | [High Converting Real Estate Landing Pages: What Makes Them Work](https://infina.ai/news/high-converting-real-estate-landing-pages/) | `high converting real estate landing pages` | Evaluation/MOF | ✅ ĐÃ AUDIT (2026-10-01): không trùng, là deep-dive thật của Pillar — đã fix internal link 2 chiều, không merge |
| Niche: open house | [Open House Landing Page: How to Build One That Actually Captures Leads](https://infina.ai/news/open-house-landing-page/) | `open house landing page` | Post-purchase/how-to | — |
| Niche: agent chung | [Real Estate Agent Landing Page: What to Include and How to Convert Visitors](https://infina.ai/news/real-estate-agent-landing-page/) | `real estate agent landing page` | Post-purchase/how-to | — |
| Niche: home valuation | [Home Valuation Landing Page: How to Build One That Converts Seller Leads](https://infina.ai/news/home-valuation-landing-page/) | `home valuation landing page` | Post-purchase/how-to | ✅ ĐÃ AUDIT (2026-10-01): không trùng — là 1 trong 4 loại seller landing page của dòng dưới, đã thêm link ngược |
| Niche: seller chung | [Seller Landing Pages Real Estate: Types That Convert](https://infina.ai/news/seller-landing-pages-real-estate/) | `seller landing pages real estate` | Post-purchase/how-to | ✅ ĐÃ AUDIT (2026-10-01): bài tổng quan 4 loại (home valuation/listing consultation/expired listing/market report), đã tự link xuống dòng trên từ trước |

---

### Cụm 7: Lead Generation / Follow-up Automation, 🎯 RealSaleX (🥇 ưu tiên cao nhất), ✅ HOÀN THÀNH, 8 bài

Vì sao ưu tiên cao nhất: khớp thẳng "The Leak" trong pitch deck (40-50% lead không được follow-up).

**Internal link đã verify + fix (02/10/2026)**: "✅ HOÀN THÀNH" chỉ có nghĩa nội dung đã viết xong,
chưa có nghĩa link đã đúng — check qua WP REST API phát hiện pillar #1223 thiếu link ra 4/8 bài (3
bài Hỗ trợ/News + #521), và 3 trong số đó không link ngược về pillar. Đã vá xong — xem chi tiết
refresh-log.md. Còn 2 cụm chưa verify: Website Design (Cụm 5), Compliance/Legal/Risk (Cụm 8).

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

### Cụm 8: Compliance / Legal / Risk, 6 bài, tất cả sống (+1 News wire fraud 04/10, +1 News private listing law 06/10)

| Vai trò | Bài | Focus keyword | Funnel | Trạng thái |
|---|---|---|---|---|
| **Pillar (nhẹ)** | [TCPA Compliance for Real Estate Agents](https://infina.ai/news/tcpa-compliance-for-real-estate-agents/) | `tcpa compliance for real estate agents` | Discovery/TOF | ✅ = #237, đã link từ #147/Cụm 4/Cụm 7 |
| Hỗ trợ (News) | [AI-Written Listing Descriptions Are Creating Fair Housing Liability](https://infina.ai/news/ai-hallucination-risk-real-estate-listings/) | `ai hallucination risk real estate listings` | Post-purchase/support | — |
| Hỗ trợ (News) | [Colorado's New AI Law Sets a Deadline for Automated Decisions](https://infina.ai/news/ai-decision-making-compliance-real-estate-agents/) | `ai decision making compliance real estate agents` | Post-purchase/support | — |
| Hỗ trợ (News) | [Seller Impersonation Fraud Attempts Just Doubled](https://infina.ai/news/seller-impersonation-fraud-prevention-real-estate-agents/) | `seller impersonation fraud prevention real estate agents` | Post-purchase/support | — |
| Hỗ trợ (News) | [Two Wire Fraud Companies Just Merged, and the Agent Is Still the Weak Link](https://infina.ai/news/how-agents-protect-clients-from-wire-fraud/) | `how agents protect clients from wire fraud` | Post-purchase/support | ✅ Published 04/10 = #1481. Góc wire fraud lúc closing, khác #1260 (impersonation phía seller). Link 2 chiều với pillar #237 |
| Hỗ trợ (News) | [Three States Now Force Private Listings Public the Moment You Market Them](https://infina.ai/news/private-listing-marketing-rules/) | `private listing marketing rules` | Post-purchase/support | ✅ Published 06/10 = #1501, 876 từ, density 0,57%, 4 ảnh. Nguồn verify first-hand: CT Office of Legislative Research public act summary cho PA 26-23 (sSB 340) và Senate Bill Report cho WA SB 6091, không lấy số liệu từ search summary. Link 2 chiều với pillar #237 đã verify. Category 1 "News" vì bài thuần pháp lý, không có góc AI như #492/#1260/#1481 |

**Internal link đã verify + fix (02/10/2026)**: fetch 4 bài qua WP REST API. Đây là cụm có tình
trạng tệ nhất trong cả 8 cụm — pillar #237 KHÔNG link tới bất kỳ bài nào trong 3 bài cluster của
chính nó (chỉ link chéo cụm sang Cụm 4/Cụm 7), dù content-plan.md claim "đã link từ #147/Cụm
4/Cụm 7" (đúng, nhưng đó là chiều NGOÀI vào, không phải pillar tự link RA cluster của mình).
Chiều ngược: #492 (ai-decision-making-compliance) đã tự link về pillar #237 từ trước; #475
(ai-hallucination-risk) và #1260 (seller-impersonation-fraud) thì chưa link về pillar. Đã sửa: (1)
pillar #237 — nối thêm 3 link vào đoạn "Related Reading" có sẵn, trỏ tới cả 3 bài cluster. (2) #475
— thêm 1 câu vào đoạn Related Reading có sẵn, link về pillar #237. (3) #1260 — thêm 1 câu tương tự,
link về pillar #237 (giữ nguyên 2 link chéo cụm cũ). Verify lại cả 4 bài qua REST API — link 2 chiều
đầy đủ. Đây là cụm cuối cùng trong 8 cụm — **toàn bộ 8/8 cụm nội dung của site giờ đã được verify
internal link thật qua REST API (không còn cụm nào dựa vào claim "✓ exist" chưa kiểm chứng của
artifact RealSaleX Content Map cũ)**.

---

## Cannibalization — lịch sử audit (01/10/2026, tất cả 12 cặp đã xử lý)

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
| ~~6~~ | Cụm 1 | [best-chatbot-builder-real-estate](https://infina.ai/news/best-chatbot-builder-real-estate/) (hub) vs ~~no-code-chatbot-platform-real-estate~~ (merged, redirect 301 live) | ✅ Đọc full nội dung: trùng 4/7 tool (Tidio/ManyChat/Landbot/Intercom) với "best for" tagline gần như y hệt, cùng khung "How to Choose". Merge xong, đổi "7 Best" → "10 Best" |
| ~~6~~ | Cụm 6 | [home-valuation-landing-page](https://infina.ai/news/home-valuation-landing-page/) vs [seller-landing-pages-real-estate](https://infina.ai/news/seller-landing-pages-real-estate/) | ✅ Đọc full nội dung: KHÔNG phải duplicate — seller-landing-pages là bài tổng quan 4 loại, home-valuation là deep-dive 1 trong 4 loại đó. Đã fix link 2 chiều, giữ cả 2 bài |

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

**Tất cả cặp nghi trùng phát hiện khi map 8 Cụm (01/10/2026) đã audit xong** — bao gồm 2 cặp cuối
cùng (Chatbot Builders vs No-Code Chatbot Platform ở Cụm 1, Home Valuation vs Seller Landing Pages
ở Cụm 6), xem "Cannibalization — lịch sử audit" bên dưới.
