# Content Plan

File này gồm 2 phần: (1) content plan đang chạy cho RealSaleX, và (2) content map — danh sách
toàn bộ bài đã publish trên site, nhóm theo cụm nội dung, dùng để check cannibalization trước khi
viết bài mới hoặc lên plan mới (xem mục "Content Map" ở cuối file).

---

## Phần 1: RealSaleX (AI Deal Room)

Money page: **RealSaleX (AI Deal Room)** — SaaS B2B cho brokerage bất động sản Mỹ.
URL: *chưa deploy* (bản draft `realsalex.html` trên nhánh `main`, chưa có path chính thức trên
`infina.ai`). Cập nhật URL thật vào đây ngay khi có, rồi quay lại **cả 9 bài mới** bên dưới để
thêm internal link tới money page (xem `skills/pillar-cluster-writer/SKILL.md`) — đây là việc
còn thiếu duy nhất áp dụng cho toàn bộ plan.

**🎉 Trạng thái tổng quan (2026-09-15): CẢ 3 NHÁNH GỐC ĐÃ VIẾT XONG.** 9 bài mới (3 pillar + 6
cluster) đã viết, 4 bài cũ đã refresh, tất cả đã publish hoặc lên lịch tự động.

**🆕 Mở rộng (2026-09-30): thêm 2 bài vào Nhánh 3** (C3.4, C3.5 — góc "Customer Engagement
Platform"), đã duyệt plan, **chưa viết**. Xem chi tiết ở mục Nhánh 3 bên dưới.

## Lịch xuất bản đầy đủ (đã check trần 3 bài/ngày, chừa slot cho pipeline tin tức ~18h mỗi ngày)

| Ngày | Bài | ID | Trạng thái |
|---|---|---|---|
| 15/09/2026 | C1.4 — AI Outbound Calling for Real Estate | 1213 | ✅ Published |
| 16/09/2026 10:00 | C1.1 — AI Receptionist vs Human Receptionist | 1217 | 🕐 Scheduled |
| 17/09/2026 10:00 | C1.3 — AI Answering Service for Real Estate | 1219 | 🕐 Scheduled |
| 18/09/2026 10:00 | P2 — Real Estate Lead Follow-Up Automation Guide | 1223 | 🕐 Scheduled |
| 19/09/2026 10:00 | C2.1 — Best Lead Generation Software for Realtors | 1225 | 🕐 Scheduled |
| 20/09/2026 10:00 | C2.3 — Automated Lead Follow-Up 5-Step Setup Guide | 1227 | 🕐 Scheduled |
| 21/09/2026 10:00 | C2.4 — Facebook Lead Gen for Realtors | 1229 | 🕐 Scheduled |
| 22/09/2026 10:00 | P3 — AI Intent Layer for Real Estate CRM | 1232 | 🕐 Scheduled |
| 23/09/2026 10:00 | C3.2 — CINC CRM Review | 1234 | 🕐 Scheduled |

Refresh (cùng ngày 15/09/2026, đã publish, không cần schedule): **#147** (pillar Nhánh 1),
**#223** (thay C2.2, Nhánh 2), **#384** (thay C3.1+C3.3, Nhánh 3).

**Việc cần làm sau mỗi lần 1 bài trong bảng trên tự publish đúng giờ** (không cần nhắc, tự theo dõi
phiên sau):
1. Nếu bài đó là **pillar** (P1=#147 đã xong, P2, P3): quay lại các cluster liên quan để xác nhận
   link 2 chiều đã đúng (thường đã có sẵn trong nội dung, chỉ cần verify live).
2. Thêm dòng vào `references/used-keywords.md` (chuyển từ bảng "reserved" sang bảng "đã publish").
3. Paste dòng mới vào tracker sheet ("Infina News — Published Articles Tracker") — đưa file `.tsv`
   mỗi lần có bài live mới.
4. Khi GSC có lại credentials, check traffic/ranking thật của các bài — ưu tiên refresh nhẹ thay vì
   viết lại nếu bài đang có traffic.

**⚠️ Lưu ý về link nội bộ trong lúc rollout**: các bài trong Nhánh 2/3 đã được viết với link chéo
đầy đủ giữa nhau ngay từ đầu (không đợi từng bài publish rồi mới thêm link như cách làm ở Nhánh 1).
Vì lên lịch trải dài nhiều ngày, sẽ có **vài ngày link nội bộ trỏ tới bài chưa publish** (404/không
truy cập được cho tới đúng ngày) — tự hết khi từng bài lần lượt lên lịch xong theo bảng trên, không
cần sửa gì thêm.

---

## Bài đã có trên site — map vào plan (check 2026-09-15)

Đối chiếu 110 bài publish (qua `list_posts` + fetch nội dung thật, không suy đoán từ tiêu đề) với
3 nhánh. Phát hiện **trùng chủ đề khá nặng ở Nhánh 2 và Nhánh 3** — 2 nhánh này đã có sẵn 1 phần
nội dung tương đương trên site, nên đã refresh bài cũ thay vì viết đè.

| Bài đã có | FOCUS_KW đã log | Trùng ID nào | Việc đã làm |
|---|---|---|---|
| [#147 — 7 Best AI Voice Assistants for Real Estate Agents](https://infina.ai/news/best-ai-voice-assistants-for-real-estate/) | `ai voice assistants for real estate` | P1, C1.2 | ✅ Refreshed 15/09 — dùng làm pillar chính thức Nhánh 1 thay vì viết P1/C1.2 mới |
| [#223 — Speed-to-Lead](https://infina.ai/news/real-estate-agent-crm-speed-to-lead/) | `real estate agent crm` | C2.2 | ✅ Refreshed 15/09 — thêm link tới P2, thay thế C2.2 |
| [#384 — Best CRM Software for Real Estate Agents](https://infina.ai/news/best-crm-software-real-estate-agents/) | `best crm software` | C3.1, C3.3 | ✅ Refreshed 15/09 — thêm mục "None of These Ship a True Intent Layer" + link P3, thay thế C3.1/C3.3 |
| [#207 — Best Real Estate Agent CRM Software](https://infina.ai/news/best-crm-for-real-estate/) | `best crm for real estate` | C3.1, C3.3 | Không cần refresh riêng — đã xử lý qua #384 |
| [#444 — Best CRM for Real Estate Agents: A Buyer's Guide](https://infina.ai/news/best-crm-buying-guide-real-estate-agents/) | `best crm` | C3.1, C3.3 | Không cần refresh riêng — đã xử lý qua #384 |
| [#230 — What Is CRM Software?](https://infina.ai/news/what-is-crm-software/) / [#405 — CRM Software 101](https://infina.ai/news/crm-management-real-estate-agents-beginners-guide/) | — | Nhánh 4 | ❌ Nhánh 4 bỏ hẳn, không cần động vào 2 bài này |
| [#214 — AI CRM for Real Estate](https://infina.ai/news/ai-crm-real-estate/) | `ai crm` | P3 | Đã đọc kỹ trước khi viết P3 — khác góc (định nghĩa + tool listicle vs. "bổ sung intent layer cho CRM sẵn có"), P3 link ngược lại #214 cho người cần chọn CRM từ đầu |
| **CINC** (brand) | — | C3.2 | ✅ Xác nhận gap thật, đã viết C3.2 |

### Bài bổ trợ / liên quan (không trùng — dùng để link thêm, đã áp dụng khi viết)

| Bài đã có | Gắn vào bài nào |
|---|---|
| [#237 — TCPA Compliance for Real Estate Agents](https://infina.ai/news/tcpa-compliance-for-real-estate-agents/) | #147, C1.1, C1.4, C2.4 |
| [#390 — AI ISAs Are Delivering 3x Higher Conversion Rates](https://infina.ai/news/ai-isa-conversion-rates-real-estate/) | #147 |
| [#1026 — Rechat AI Agent Integration for CRM](https://infina.ai/news/ai-agent-integration-for-real-estate-crm-platforms/) | (chưa dùng, vẫn còn để trích dẫn thêm khi refresh sau) |
| [#1171 — RE/MAX Leo AI CRM Assistant](https://infina.ai/news/ai-crm-assistant-brokerage-merger-rollout-agents/) | (chưa dùng, vẫn còn để trích dẫn thêm khi refresh sau) |

---

## Nhánh 1: AI Answering / Call Center / Receptionist — 🥇 ưu tiên cao nhất — ✅ HOÀN THÀNH

Vì sao cao nhất: đúng câu pitch chính của sản phẩm ("AI agent trả lời buyer 24/7 trong Deal Room
riêng"). **Đã đổi hướng so với plan gốc sau khi check keyword + live-SERP thật (2026-09-15)**: CSV
gốc không có biến thể "real estate" nào cho cụm receptionist/call center — 5 FOCUS_KW ban đầu đều
là thuật ngữ generic. Chạy live-SERP xác nhận: `ai receptionist`/`ai call center software` (bare)
bị vendor/SaaS lớn chiếm SERP hoàn toàn; bản niche `... for real estate` mới có nhu cầu thật (10+
đối thủ dạng listicle cho riêng "ai receptionist for real estate"). Từ đó: bỏ viết P1/C1.2 mới,
dùng #147 (đã refresh) làm pillar, chỉ viết 3 cluster với keyword niche đã verify.

| ID | Vai trò | Bài | Focus keyword | Funnel | Trạng thái |
|---|---|---|---|---|---|
| P1 | Pillar = refresh #147 | [#147](https://infina.ai/news/best-ai-voice-assistants-for-real-estate/) | `ai receptionist for real estate` | Discovery/TOF | ✅ Published (refresh 15/09) |
| C1.1 | So sánh | [AI Receptionist vs Human Receptionist for Real Estate: Cost & ROI](https://infina.ai/news/?p=1217) (ID 1217) | `ai receptionist vs human receptionist real estate` | Evaluation/MOF | 🕐 Schedule 16/09 10:00 |
| C1.3 | Buying guide | [AI Answering Service for Real Estate: How to Choose the Right One](https://infina.ai/news/?p=1219) (ID 1219) | `ai answering service for real estate` | Decision/BOF | 🕐 Schedule 17/09 10:00 |
| C1.4 | Support/how-to → bắc cầu Nhánh 2 | [AI Outbound Calling for Real Estate: How It Works in 2026](https://infina.ai/news/ai-outbound-calling-real-estate-lead-follow-up/) (ID 1213) | `ai outbound calling for real estate` | Post-purchase/how-to | ✅ Published 15/09 |

Internal link: #147 ↔ C1.1/C1.3/C1.4 (2 chiều, đã verify live), C1.4 ↔ P2 (Nhánh 2, đã có link).
Điểm khác biệt đã thêm vào #147 mà đối thủ chưa cover: mục Fair Housing + TCPA compliance.

---

## Nhánh 2: Lead Generation + Follow-up Automation — 🥇 ưu tiên cao nhất — ✅ HOÀN THÀNH

Vì sao cao nhất: khớp thẳng "The Leak" trong pitch deck (40-50% lead không được follow-up).

| ID | Vai trò | Bài | Focus keyword | Funnel | Trạng thái |
|---|---|---|---|---|---|
| P2 | Pillar | [Real Estate Lead Follow-Up Automation: The Complete 2026 Guide](https://infina.ai/news/?p=1223) (ID 1223) | `real estate lead follow-up automation` | Discovery/TOF | 🕐 Schedule 18/09 10:00 |
| C2.1 | Review/list | [Best Lead Generation Software for Realtors in 2026](https://infina.ai/news/?p=1225) (ID 1225) | `lead generation software for realtors` | Evaluation/MOF | 🕐 Schedule 19/09 10:00 |
| ~~C2.2~~ | ~~Giải thích/pain-point~~ | ❌ Bỏ, thay bằng refresh [#223](https://infina.ai/news/real-estate-agent-crm-speed-to-lead/) | — | — | ✅ #223 đã refresh 15/09, thêm link P2 |
| C2.3 | Buying guide/how-to | [Automated Lead Follow-Up for Real Estate: A 5-Step Setup Guide](https://infina.ai/news/?p=1227) (ID 1227) | `automated lead follow-up for real estate` | Decision/BOF | 🕐 Schedule 20/09 10:00 |
| C2.4 | Kênh cụ thể | [Facebook Lead Gen for Realtors: Turning Ad Leads Into Showings](https://infina.ai/news/?p=1229) (ID 1229) | `facebook lead gen for realtors` | Decision/BOF | 🕐 Schedule 21/09 10:00 |

**Đổi FOCUS_KW so với plan gốc** (bài học từ Nhánh 1 — niche hoá thay vì dùng keyword generic từ
CSV): `lead generation for realestate` → `real estate lead follow-up automation` (P2, khớp đúng
intent bài); `lead generation software` → `lead generation software for realtors` (C2.1); `lead
generation systems` → `automated lead follow-up for real estate` (C2.3); `facebook lead generation
ads` → `facebook lead gen for realtors` (C2.4) — tất cả đã verify có SERP thật khớp định dạng dự
kiến (listicle cho C2.1, mix explainer/how-to cho C2.3, mix cho C2.4) qua web search 2026-09-15.

Internal link: P2 ↔ C2.1/C2.3/C2.4 (2 chiều), P2 ↔ #223 (refresh), P2 ↔ C1.4 (chéo nhánh, cả 2
chiều), C2.4 → #147 (mention Fair Housing/Housing Special Ad Category).

---

## Nhánh 3: CRM Add-on / Alternatives & Pricing — 🥈 ưu tiên 2 — 🕐 Phần gốc đã xong, đang mở rộng

Góc bắt buộc: viết kiểu "CRM sẵn có thiếu gì mà cần thêm lớp intent", KHÔNG viết "X vs Y CRM nào
tốt hơn" — target là người đã có CRM rồi, RealSaleX bổ sung chứ không thay thế.

| ID | Vai trò | Bài | Focus keyword | Funnel | Trạng thái |
|---|---|---|---|---|---|
| P3 | Pillar (nhẹ) | [AI Intent Layer for Real Estate CRM: What It Adds](https://infina.ai/news/?p=1232) (ID 1232) | `ai intent layer for real estate crm` | Evaluation/MOF | ✅ Published |
| ~~C3.1~~ | ~~Follow Up Boss Review~~ | ❌ Bỏ, thay bằng refresh [#384](https://infina.ai/news/best-crm-software-real-estate-agents/) | — | — | ✅ #384 đã refresh 15/09, thêm link P3 |
| C3.2 | Review + gap thật | [CINC CRM Review: Pricing, Features, and Buyer Follow-Up Gaps](https://infina.ai/news/?p=1234) (ID 1234) | `cinc crm review` | Evaluation/MOF | ✅ Published |
| ~~C3.3~~ | ~~kvCORE Pricing~~ | ❌ Bỏ, cùng xử lý qua refresh #384 | — | — | ✅ |
| C3.4 | So sánh (MOF) | *Customer Engagement Platform vs CRM for Real Estate* | `customer engagement platform vs crm` | Evaluation/MOF | 🕐 Đã duyệt plan 30/09, chưa viết |
| C3.5 | Listicle chiến lược (TOF) | *Customer Engagement Strategies for Real Estate Agents* | niche từ `digital customer engagement` + `customer engagement examples` | Discovery/TOF | 🕐 Đã duyệt plan 30/09, chưa viết |

**Đổi FOCUS_KW so với plan gốc**: `crm and lead generation` → `ai intent layer for real estate crm`
(P3, khớp SERP thật về "AI follow-up shift to intent signals" thay vì generic CRM+leadgen). C3.2
dùng `cinc crm review` (niche cụ thể hơn `cinc reviews`). Dữ liệu CINC thật (giá từ $900/tháng,
gói Solo/Ramp/Pro/Select, điểm mạnh/yếu) đã verify qua web search trước khi viết, không suy đoán.

Internal link: P3 ↔ C3.2 (2 chiều), P3 ↔ #384 (refresh, thay C3.1/C3.3), P3 ↔ #214 (link chéo,
không cannibalize), P3 ↔ P2 (định vị bổ sung CRM).

### C3.4 + C3.5 — mở rộng "Customer Engagement Platform" (2026-09-30)

**Bối cảnh**: user gửi thêm 148 keyword mới (export Google Keyword Planner) về "customer engagement
platform" (CEP), đã merge vào
`wordpress-mcp/skills/news-to-cluster-article/keywords/Infina_AI_RealSale_Keyword_Stats_2026-09-15.csv`
(commit `d0f17c3`). CEP được xác nhận là **góc định vị lại 1 phần RealSaleX**, không phải sản phẩm
tách riêng — audience vẫn brokerage/agent bất động sản Mỹ, money page vẫn RealSaleX (chưa deploy).

**Vì sao KHÔNG tạo hẳn 1 "Nhánh CEP" riêng** (đã cân nhắc rồi bỏ): live-SERP check cho thấy niche
hóa "customer engagement platform for real estate" đá thẳng vào sân đã có của Nhánh 3 hiện tại
(Sierra Interactive, Zoho SalesIQ, Salesforce, Creatio đều frame CEP-cho-real-estate y hệt nội dung
"CRM cho real estate" đã có ở #207/#384/#214/#230/#405). Tạo nhánh mới riêng sẽ tự cannibalize nội
bộ nhiều hơn là mở ra SERP mới, nên quyết định **nhét 2 bài mới vào Nhánh 3 sẵn có** thay vì tạo
nhánh 5.

**Kết quả check volume + live-SERP (2026-09-30) cho từng nhóm keyword ứng viên**:

| Nhóm keyword | Volume (tier) | Kết luận |
|---|---|---|
| `customer engagement platform`, `customer experience automation platform`, `omnichannel customer engagement platform`, `best customer engagement platform` (bare) | 500-5000 | ❌ Bỏ — SERP bị vendor tỷ đô chiếm 100% (Twilio, Salesforce, Zendesk, Braze, Talon.One, Bloomreach...), **zero** kết quả real estate dù niche hay không |
| `what is customer engagement`, `CEP customer engagement platform meaning` (bare) | 500, 50 | ❌ Bỏ — cùng lý do, toàn IBM/Salesforce/Wikipedia/Martech.zone. Lưu ý: competition index thấp (idx=1) trong file KHÔNG phản ánh độ khó SERP organic thật — đây là competition Ads, dễ gây hiểu lầm |
| `what is a customer engagement platform for real estate`, `...real estate agents need` (niche) | 500 (bare gốc) | ❌ Bỏ — SERP real estate có thật (Sierra Interactive, Zoho SalesIQ, realestatecrm.io...) nhưng nội dung đọc y hệt "CRM cho real estate" đã có → cannibalize nội bộ với #207/#384/#214, không đáng viết bài riêng |
| `customer engagement platform vs crm` | 50, comp idx **0** | ✅ Giữ — C3.4. Generic có 9+ bài (leat, courier, moengage, informatica...) nhưng **chưa site real estate nào viết bản riêng**, khớp đúng pitch RealSaleX (bổ sung CRM bằng lớp engagement/intent) |
| `digital customer engagement real estate`, `customer engagement examples real estate` (niche) | 500 (bare gốc) | ✅ Giữ — C3.5. SERP real estate có thật (Spectrio, Transactly, ETG.digital, commercial-realestate-training.com) nhưng đối thủ toàn agency blog nhỏ, chưa ai làm bài resource chuẩn SEO — format listicle chiến lược/ví dụ, khác hẳn format so sánh phần mềm nên không đụng Nhánh 3 hiện có |

Internal link dự kiến khi viết: C3.4 ↔ C3.5 (2 chiều), cả 2 ↔ P3 (#1232) + #384, C3.4 → money page
RealSaleX (khi có URL).

---

## Nhánh 4: CRM Software (generic) — ❌ đã bỏ hẳn

#230 và #405 đã cover đúng góc "CRM là gì / CRM 101" mà nhánh này định làm — không tạo pillar
riêng, không giữ backlog.

---

## Bị loại khỏi plan (không dùng)

- **Local-intent** ("realtor near me"...) — khớp SERP local pack, sai định dạng site.
- **Consumer FSBO/tìm agent** ("sell house without realtor"...) — sai audience (người mua/bán nhà,
  không phải broker/agent).
- **Document/Transaction Management** — sản phẩm hoạt động ở giai đoạn buyer tìm hiểu/so sánh,
  không phải giai đoạn ký hợp đồng.
- **Website/IDX, Reviews/Reputation** — không liên quan sản phẩm hoặc đã có pillar cũ cover.

---

## Việc còn lại (toàn plan)

1. **Money page URL**: chưa deploy trên `infina.ai`. Khi có URL thật, quay lại cả 9 bài mới +
   3 bài refresh để thêm internal link tới money page (hiện tất cả đang ghi "chờ URL").
2. **GSC/GA4 credentials**: đã có key thật (verify hoạt động 2026-09-15), nhưng chỉ lưu session-only
   (repo public, không commit key) — cần check lại traffic/ranking của các bài mới sau khi chúng đủ
   thời gian lên SERP (2-3 tuần), dùng skill `post-refresh`.
3. **Mở rộng plan nếu cần thêm bài**: 2 hướng đã note trước — hạ ngưỡng volume CSV xuống dưới 500,
   hoặc dùng `post-refresh` tìm striking-distance keyword mới nảy sinh từ chính 9 bài vừa viết sau
   khi có dữ liệu GSC thật.
4. **`references/used-keywords.md`**: cần cập nhật dần khi mỗi bài trong lịch ở trên tự publish
   (chuyển từ bảng "reserved" sang bảng "đã publish").
5. **Viết C3.4 + C3.5** (Nhánh 3, góc Customer Engagement Platform) — plan đã duyệt 30/09, chưa
   viết bài thật. Theo đúng quy trình `skills/pillar-cluster-writer/SKILL.md` Bước 5 trở đi.

---

## Phần 2: Content Map — Toàn bộ bài đã publish trên site

Danh sách đầy đủ các bài đã publish trên `infina.ai/news`, nhóm theo cụm nội dung (content
cluster), kèm focus keyword — dùng để check cannibalization trước khi viết bài mới hoặc lên content
plan (khác phạm vi với Phần 1 ở trên — phần này cover TOÀN BỘ site, không chỉ RealSaleX).

**Nguồn**: Google Sheet ["Infina AI News Published Articles Tracker, SEO KW"](https://docs.google.com/spreadsheets/d/1uVI1tPQxhTUk4qj8NWZSi-EReEwe2ZKIyIt_eQGeFOs/edit), tab "Published article" (export 01/10/2026, 122 bài). Cập nhật tay mỗi khi có bài mới — không tự động đồng bộ lại với Sheet hay WordPress.

**Cách dùng**: Ctrl+F / grep cụm từ khóa định dùng trước khi viết bài mới. Nếu thấy khớp hoặc gần khớp với 1 bài trong cùng cụm, đọc kỹ nội dung bài đó trước — tránh lặp lại pattern cannibalization đã xảy ra ở cụm Chatbot (xem ghi chú ⚠️/✅ bên dưới, chi tiết đầy đủ ở `skills/post-refresh/references/refresh-log.md`).

### Chatbot / Conversational AI (19 bài)

| # | Date | Title | Focus Keyword | Note |
|---|---|---|---|---|
| 1 | 05/06/2026 | [Best AI Chatbot for Real Estate Lead Capture](https://infina.ai/news/best-ai-chatbot-for-real-estate-lead-capture/) | `ai chatbot for real estate lead capture` | ⚠️ ĐÃ MERGE (01/10/2026) → stub, redirect 301 sang `best-chatbot-customer-service-real-estate` |
| 2 | 09/06/2026 | [12 Best Chatbot Customer Service Tools for Real Estate](https://infina.ai/news/best-chatbot-customer-service-real-estate/) | `chatbot customer service real estate` | ✅ HUB — đã hấp thụ nội dung từ best-ai-chat-platform-real-estate + best-ai-chatbot-for-real-estate-lead-capture, hiện review 15 tool |
| 3 | 13/06/2026 | [8 Best AI Chat Platforms for Real Estate Teams](https://infina.ai/news/best-ai-chat-platform-real-estate/) | `ai chat platform real estate` | ⚠️ ĐÃ MERGE (01/10/2026) → stub, redirect 301 sang `best-chatbot-customer-service-real-estate` |
| 5 | 21/06/2026 | [7 Best Chatbot Builders for Real Estate](https://infina.ai/news/best-chatbot-builder-real-estate/) | `chatbot builder real estate` |  |
| 6 | 25/06/2026 | [Chatbot vs Conversational AI](https://infina.ai/news/chatbot-vs-conversational-ai-real-estate/) | `chatbot vs conversational ai real estate` |  |
| 7 | 29/06/2026 | [GoHighLevel Chatbot vs Dedicated Real Estate Chatbots](https://infina.ai/news/gohighlevel-chatbot-vs-dedicated-real-estate-chatbot/) | `gohighlevel chatbot` |  |
| 9 | 14/07/2026 | [What Is a Conversational Chatbot?](https://infina.ai/news/what-is-a-conversational-chatbot-real-estate/) | `conversational chatbot` |  |
| 10 | 21/07/2026 | [Zendesk Sunshine Conversations Alternative](https://infina.ai/news/zendesk-sunshine-conversations-alternative-real-estate/) | `zendesk sunshine conversations alternative` |  |
| 11 | 28/07/2026 | [Conversational Chat for Real Estate](https://infina.ai/news/conversational-chat-real-estate/) | `conversational chat real estate` |  |
| 73 | 27/08/2026 | [Best Conversational AI Chatbots for Real Estate Agents in 2026](https://infina.ai/news/best-conversational-ai-chatbot-for-real-estate/) | `best conversational ai chatbot for real estate` | ✅ HUB — đã hấp thụ nội dung từ best-ai-conversational-bot-for-real-estate + best-conversational-chatbot-for-real-estate, hiện review 11 tool |
| 74 | 27/08/2026 | [Best Conversational Chatbot Platforms for Real Estate Lead Qualification in 2026](https://infina.ai/news/best-conversational-chatbot-for-real-estate/) | `best conversational chatbot for real estate` | ⚠️ ĐÃ MERGE (01/10/2026) → stub, redirect 301 sang `best-conversational-ai-chatbot-for-real-estate` |
| 75 | 28/08/2026 | [Best AI Conversational Bots for Real Estate Follow-Up in 2026](https://infina.ai/news/best-ai-conversational-bot-for-real-estate/) | `best ai conversational bot for real estate` | ⚠️ ĐÃ MERGE (01/10/2026) → stub, redirect 301 sang `best-conversational-ai-chatbot-for-real-estate` |
| 76 | 28/08/2026 | [AI Chat vs SMS Follow-Up for Real Estate: Which Converts More Leads?](https://infina.ai/news/ai-chat-vs-sms-real-estate/) | `ai chat vs sms real estate` |  |
| 77 | 29/08/2026 | [Best No-Code Chatbot Platform for Real Estate Websites in 2026](https://infina.ai/news/no-code-chatbot-platform-real-estate/) | `no code chatbot platform real estate` |  |
| 78 | 29/08/2026 | [Chatbot vs Live Agent for Real Estate: Response Time and Conversion Compared](https://infina.ai/news/chatbot-vs-live-agent-real-estate/) | `chatbot vs live agent real estate` |  |
| 79 | 24/08/2026 | [EU AI Act Disclosure Rules Are Already Changing Your Real Estate Chatbot](https://infina.ai/news/ai-disclosure-rules-for-real-estate-chatbots/) | `ai disclosure rules for real estate chatbots` |  |
| 81 | 26/08/2026 | [This Chatbot Reads Your Listing Photos to Stop 47 Calls a Week](https://infina.ai/news/real-estate-chatbot-that-reads-listing-photos/) | `real estate chatbot that reads listing photos` |  |
| 83 | 28/08/2026 | [A New Study Found AI Got 1 in 4 Mortgage Document Checks Wrong](https://infina.ai/news/ai-chatbot-mortgage-document-errors-real-estate-agents/) | `ai chatbot mortgage document errors real estate agents` |  |
| 88 | 03/09/2026 | [A CRMLS Test Shows How Easily an AI Chatbot Can Leak Your MLS Data](https://infina.ai/news/ai-chatbot-mls-data-security-risk-brokerages/) | `ai chatbot mls data security risk brokerages` |  |

### CRM Software (22 bài)

| # | Date | Title | Focus Keyword | Note |
|---|---|---|---|---|
| 12 | 29/07/2026 | [Best Real Estate Agent CRM Software in 2026](https://infina.ai/news/best-crm-for-real-estate/) | `best crm for real estate` |  |
| 13 | 30/07/2026 | [AI CRM for Real Estate](https://infina.ai/news/ai-crm-real-estate/) | `ai crm` |  |
| 14 | 07/08/2026 | [What Is CRM Software?](https://infina.ai/news/what-is-crm-software/) | `what is crm software` |  |
| 15 | 10/08/2026 (scheduled) | [Speed-to-Lead: How Real Estate Agent CRM Closes the 15-Hour Gap](https://infina.ai/news/real-estate-agent-crm-speed-to-lead/) | `real estate agent crm` |  |
| 17 | 02/08/2026 | [CRM Marketing for Real Estate: How to Turn Your Database into a Deal Machine](https://infina.ai/news/crm-marketing-real-estate/) | `crm marketing` |  |
| 18 | 03/08/2026 | [CRM Pipeline Management: Build a Sales Pipeline That Actually Closes](https://infina.ai/news/crm-pipeline-management/) | `crm pipeline` |  |
| 22 | 11/08/2026 (scheduled) | [Best CRM Software for Real Estate Agents: Full Comparison (2026)](https://infina.ai/news/best-crm-software-real-estate-agents/) | `best crm software` |  |
| 24 | 11/08/2026 | [CRM Software 101: A Beginner's Guide for Real Estate Agents](https://infina.ai/news/crm-management-real-estate-agents-beginners-guide/) | `crm management` |  |
| 25 | 06/08/2026 | [Top CRM Tools for Real Estate Agents and Teams (2026)](https://infina.ai/news/top-crm-tools-real-estate-teams/) | `crm tools for real estate` |  |
| 26 | 05/08/2026 | [Best CRM for Real Estate Teams: Top Picks for 2026](https://infina.ai/news/best-crm-real-estate-teams-2026/) | `best crm for real estate teams` |  |
| 27 | 04/08/2026 | [Best Free CRM for Real Estate Agents in 2026](https://infina.ai/news/best-free-crm-for-real-estate-agents/) | `free crm for real estate` |  |
| 28 | 27/07/2026 | [Best CRM for Real Estate Agents: A Buyer's Guide (2026)](https://infina.ai/news/best-crm-buying-guide-real-estate-agents/) | `best crm` |  |
| 29 | 26/07/2026 | [What Is CRM Marketing Software? A Guide for Real Estate Teams](https://infina.ai/news/crm-marketing-software-real-estate-guide/) | `crm marketing software` |  |
| 45 | 13/08/2026 | [CRM with Website Builder: Best Integrated Platforms for Real Estate Teams](https://infina.ai/news/crm-with-website-builder-real-estate/) | `crm with website builder` |  |
| 53 | 17/08/2026 | [Real Estate CRM with IDX Integration: Best Platforms in 2026](https://infina.ai/news/real-estate-crm-with-idx/) | `real estate crm with idx` |  |
| 64 | 22/08/2026 | [Rechat Just Let Claude and ChatGPT Run Real Estate CRM Workflows Directly](https://infina.ai/news/ai-agent-integration-for-real-estate-crm-platforms/) | `ai agent integration for real estate crm platforms` |  |
| 92 | 07/09/2026 | [Real's AI CRM Assistant Leo Is About to Meet 180,000 New RE/MAX Agents](https://infina.ai/news/ai-crm-assistant-brokerage-merger-rollout-agents/) | `ai crm assistant brokerage merger rollout agents` |  |
| 94 | 09/09/2026 | [eXp Realty Says Its All-in-One AI Platform Cuts Software Costs by 70%](https://infina.ai/news/exp-nexus-crm-software-cost-reduction-agents/) | `exp nexus crm software cost reduction agents` |  |
| 106 | 22/09/2026 | [AI Intent Layer for Real Estate CRM: What It Adds](https://infina.ai/news/ai-intent-layer-for-real-estate-crm/) | `ai intent layer for real estate crm` |  |
| 107 | 23/09/2026 | [CINC CRM Review: Pricing, Features, and Buyer Follow-Up Gaps](https://infina.ai/news/cinc-crm-review-real-estate/) | `cinc crm review` |  |
| 120 | 27/09/2026 | [Nearly 10% of Borrowers Are Now Choosing ARMs as Rates Top 7%](https://infina.ai/news/arm-borrower-tracking-real-estate-agent-crm/) | `arm borrower tracking real estate agent crm` |  |
| 121 | 28/09/2026 | [Lofty Launches an MCP Server So Any AI Can Plug Into Its CRM](https://infina.ai/news/open-ai-protocol-real-estate-crm-brokerages/) | `open ai protocol real estate crm brokerages` |  |

### Website Builder / IDX (15 bài)

| # | Date | Title | Focus Keyword | Note |
|---|---|---|---|---|
| 39 | 20/08/2026 | [Best Real Estate Website Builders for Agents and Brokers (2026)](https://infina.ai/news/real-estate-website-builder/) | `real estate website builder` | ✅ HUB — đã hấp thụ nội dung từ real-estate-website-builder-with-idx (merge case cũ, trước 01/10/2026) |
| 40 | 20/08/2026 | [Best Real Estate Website Builder: Features, Pricing and IDX Compared](https://infina.ai/news/best-real-estate-website-builder/) | `best real estate website builder` | ⚠️ Cùng cụm với real-estate-website-builder (hub) — đã gỡ link chéo khi xử lý case merge trước đó nhưng CHƯA merge nội dung, vẫn là bài riêng. Theo dõi thêm nếu cannibalize. |
| 41 | 12/08/2026 | [Best Real Estate Agent Website Builder for Solo Agents in 2026](https://infina.ai/news/real-estate-agent-website-builder/) | `real estate agent website builder` |  |
| 42 | 20/08/2026 | [Best Website Builder for Realtors: Top Picks Reviewed (2026)](https://infina.ai/news/best-website-builder-for-realtors/) | `best website builder for realtors` |  |
| 43 | 12/08/2026 | [Free Real Estate Website Builder: What You Get vs. What You Pay For](https://infina.ai/news/free-real-estate-website-builder/) | `free real estate website builder` |  |
| 44 | 13/08/2026 | [Best Website Builder for Real Estate Investors in 2026](https://infina.ai/news/best-website-builder-real-estate-investors/) | `best website builder for real estate investors` |  |
| 46 | 14/08/2026 | [What Is Broker IDX? Complete Guide for Real Estate Agents (2026)](https://infina.ai/news/broker-idx-guide/) | `broker idx` |  |
| 47 | 14/08/2026 | [What Is IDX in Real Estate? Definition, Setup, and How It Works](https://infina.ai/news/idx-real-estate-definition-guide/) | `idx real estate` |  |
| 48 | 15/08/2026 | [Best IDX Website for Realtors: Top Platforms Reviewed (2026)](https://infina.ai/news/idx-website-for-realtors/) | `idx website for realtors` | ⚠️ Title/FK rất gần best-idx-website-for-realtors (#54) — CHƯA audit, nghi ngờ trùng, nên đọc kỹ cả 2 trước khi sửa bài nào |
| 49 | 15/08/2026 | [IDX Real Estate Websites: Best Examples and What Makes Them Work](https://infina.ai/news/idx-real-estate-websites-examples/) | `idx real estate websites` |  |
| 50 | 16/08/2026 | [IDX MLS: How the Data Feed Powers Real Estate Agent Websites](https://infina.ai/news/idx-mls-real-estate-guide/) | `idx mls` |  |
| 51 | 16/08/2026 | [IDX Feed: What It Is and How to Set It Up on Your Website](https://infina.ai/news/idx-feed-real-estate-setup/) | `idx feed` |  |
| 52 | 17/08/2026 | [Real Estate Website Builder with IDX: Top Options Compared (2026)](https://infina.ai/news/real-estate-website-builder-with-idx/) | `real estate website builder with idx` | ⚠️ ĐÃ MERGE (01/10/2026) → stub, redirect 301 sang `real-estate-website-builder` |
| 54 | 18/08/2026 | [Best IDX Website for Realtors: In-Depth Platform Reviews](https://infina.ai/news/best-idx-website-for-realtors/) | `best idx website for realtors` | ⚠️ Title/FK rất gần idx-website-for-realtors (#48) — CHƯA audit, nghi ngờ trùng, nên đọc kỹ cả 2 trước khi sửa bài nào |
| 55 | 18/08/2026 | [Real Estate Agent Websites with IDX: What to Look For Before You Buy](https://infina.ai/news/real-estate-agent-websites-with-idx/) | `real estate agent websites with idx` |  |

### AI Voice / Virtual Assistant / Receptionist (5 bài)

| # | Date | Title | Focus Keyword | Note |
|---|---|---|---|---|
| 4 | 17/06/2026 | [7 Best AI Virtual Assistants for Real Estate](https://infina.ai/news/best-ai-virtual-assistant-real-estate/) | `ai virtual assistant real estate` |  |
| 8 | 03/07/2026 | [7 Best AI Voice Assistants for Real Estate](https://infina.ai/news/best-ai-voice-assistants-for-real-estate/) | `ai voice assistants for real estate` |  |
| 99 | 15/09/2026 | [AI Outbound Calling for Real Estate: How It Works in 2026](https://infina.ai/news/ai-outbound-calling-real-estate-lead-follow-up/) | `ai outbound calling for real estate` |  |
| 100 | 16/09/2026 | [AI Receptionist vs Human Receptionist for Real Estate: Cost & ROI](https://infina.ai/news/ai-receptionist-vs-human-receptionist-real-estate/) | `ai receptionist vs human receptionist real estate` |  |
| 101 | 17/09/2026 | [AI Answering Service for Real Estate: How to Choose the Right One](https://infina.ai/news/ai-answering-service-for-real-estate/) | `ai answering service for real estate` |  |

### Website / Web Design (7 bài)

| # | Date | Title | Focus Keyword | Note |
|---|---|---|---|---|
| 66 | 23/08/2026 | [Real Estate Agent Website Design: What Actually Works in 2026](https://infina.ai/news/website-design-for-real-estate-agents/) | `website design for real estate agents` |  |
| 67 | 23/08/2026 | [Best Real Estate Website Design: 8 Examples to Model in 2026](https://infina.ai/news/best-real-estate-website-design/) | `best real estate website design` |  |
| 68 | 24/08/2026 | [Realtor Website Design: How to Stand Out and Convert More Visitors](https://infina.ai/news/realtor-website-design/) | `realtor website design` |  |
| 69 | 24/08/2026 | [Web Design for Real Estate Agents: DIY vs. Hiring a Designer](https://infina.ai/news/web-design-for-real-estate-agents/) | `web design for real estate agents` |  |
| 70 | 25/08/2026 | [Real Estate Web Design Companies: How to Choose the Right One](https://infina.ai/news/real-estate-web-design-companies/) | `real estate web design companies` |  |
| 71 | 25/08/2026 | [Real Estate Broker Website Design: What Brokerage Sites Actually Need](https://infina.ai/news/real-estate-broker-website-design/) | `real estate broker website design` |  |
| 72 | 26/08/2026 | [Luxury Real Estate Website Design: Features That Signal Premium to Buyers](https://infina.ai/news/luxury-real-estate-website-design/) | `luxury real estate website design` |  |

### Landing Pages (6 bài)

| # | Date | Title | Focus Keyword | Note |
|---|---|---|---|---|
| 57 | 19/08/2026 | [Open House Landing Page: How to Build One That Actually Captures Leads](https://infina.ai/news/open-house-landing-page/) | `open house landing page` |  |
| 58 | 19/08/2026 | [Real Estate Agent Landing Page: What to Include and How to Convert Visitors](https://infina.ai/news/real-estate-agent-landing-page/) | `real estate agent landing page` |  |
| 59 | 21/08/2026 | [Real Estate Landing Page: Types, Elements, and How to Build One That Converts](https://infina.ai/news/real-estate-landing-page-guide/) | `real estate landing page` |  |
| 60 | 21/08/2026 | [Home Valuation Landing Page: How to Build One That Converts Seller Leads](https://infina.ai/news/home-valuation-landing-page/) | `home valuation landing page` |  |
| 61 | 22/08/2026 | [Seller Landing Pages Real Estate: Types That Convert and How to Build Them](https://infina.ai/news/seller-landing-pages-real-estate/) | `seller landing pages real estate` |  |
| 62 | 22/08/2026 | [High Converting Real Estate Landing Pages: What Makes Them Work in 2026](https://infina.ai/news/high-converting-real-estate-landing-pages/) | `high converting real estate landing pages` |  |

### Lead Generation / Follow-up Automation (8 bài)

| # | Date | Title | Focus Keyword | Note |
|---|---|---|---|---|
| 37 | 18/08/2026 | [Real Estate Contact Forms Are Losing the Highest-Intent Leads](https://infina.ai/news/real-estate-contact-form-conversion-rate/) | `real estate contact form conversion rate` |  |
| 84 | 29/08/2026 | [Your Next Listing Is Probably Already Sitting in Your CRM](https://infina.ai/news/database-reactivation-ai-seller-leads-real-estate-agents/) | `database reactivation ai seller leads real estate agents` |  |
| 102 | 18/09/2026 | [Real Estate Lead Follow-Up Automation: The Complete 2026 Guide](https://infina.ai/news/real-estate-lead-follow-up-automation-guide/) | `real estate lead follow-up automation` |  |
| 103 | 19/09/2026 | [Best Lead Generation Software for Realtors in 2026](https://infina.ai/news/best-lead-generation-software-for-realtors/) | `lead generation software for realtors` |  |
| 104 | 20/09/2026 | [Automated Lead Follow-Up for Real Estate: A 5-Step Setup Guide](https://infina.ai/news/how-to-set-up-automated-lead-follow-up-real-estate/) | `automated lead follow-up for real estate` |  |
| 105 | 21/09/2026 | [Facebook Lead Gen for Realtors: Turning Ad Leads Into Showings](https://infina.ai/news/facebook-lead-gen-for-realtors/) | `facebook lead gen for realtors` |  |
| 112 | 19/09/2026 | [Realtor.com Just Named the Best Week to Buy in 2026, and Everyone Read It](https://infina.ai/news/buyer-lead-nurture-campaign-real-estate-agents/) | `buyer lead nurture campaign real estate agents` |  |
| 113 | 20/09/2026 | [Sellers Now Outnumber Buyers by 57.9%, the Widest Gap on Record](https://infina.ai/news/seller-lead-prioritization-real-estate-pipeline/) | `seller lead prioritization real estate pipeline` |  |

### Compliance / Legal / Risk (4 bài)

| # | Date | Title | Focus Keyword | Note |
|---|---|---|---|---|
| 16 | 07/08/2026 | [TCPA Compliance for Real Estate Agents: What the 2026 FCC Rules Mean for AI Texting and Calling](https://infina.ai/news/tcpa-compliance-for-real-estate-agents/) | `tcpa compliance for real estate agents` |  |
| 31 | 12/08/2026 | [AI-Written Listing Descriptions Are Creating Fair Housing Liability — Here's What to Check](https://infina.ai/news/ai-hallucination-risk-real-estate-listings/) | `ai hallucination risk real estate listings` |  |
| 33 | 14/08/2026 | [Colorado's New AI Law Sets a Deadline for Automated Decisions in Real Estate](https://infina.ai/news/ai-decision-making-compliance-real-estate-agents/) | `ai decision making compliance real estate agents` |  |
| 110 | 17/09/2026 | [Seller Impersonation Fraud Attempts Just Doubled. Here Is How to Catch It Earlier](https://infina.ai/news/seller-impersonation-fraud-prevention-real-estate-agents/) | `seller impersonation fraud prevention real estate agents` |  |

### News / Market Commentary (36 bài)

| # | Date | Title | Focus Keyword | Note |
|---|---|---|---|---|
| 19 | 07/08/2026 | [Real Estate's AI Holdouts Are Nearly Extinct: What the 2026 Adoption Data Means for Agents Still on the Fence](https://infina.ai/news/real-estate-ai-adoption-statistics-2026/) | `real estate ai adoption statistics 2026` |  |
| 20 | 08/08/2026 | [Why 91% of Real Estate Agents Are Invisible to AI Search (And What to Do About It)](https://infina.ai/news/answer-engine-optimization-for-real-estate-agents/) | `answer engine optimization for real estate agents` |  |
| 21 | 09/08/2026 | [Homebuyer Trust in AI Just Dropped 14 Points — What That Means for Real Estate Agents](https://infina.ai/news/declining-ai-trust-real-estate-agents/) | `declining ai trust real estate agents` |  |
| 23 | 10/08/2026 | [AI ISAs Are Delivering 3x Higher Conversion Rates for Real Estate Teams — Here's the Data](https://infina.ai/news/ai-isa-conversion-rates-real-estate/) | `ai isa conversion rates real estate` |  |
| 30 | 11/08/2026 | [Real Estate's Next AI Shift: From Chatbots to an AI Workforce for Real Estate Teams](https://infina.ai/news/autonomous-ai-workforce-real-estate-teams/) | `autonomous ai workforce real estate teams` |  |
| 32 | 13/08/2026 | [70% of Agents Want More AI Training — Here's the Confidence Gap Behind That Number](https://infina.ai/news/ai-training-gap-for-real-estate-agents/) | `ai training gap for real estate agents` |  |
| 34 | 15/08/2026 | [Inside Real Estate's ComplianceAI Shows Where Back Office AI Is Headed](https://infina.ai/news/ai-backoffice-transaction-management-real-estate/) | `ai backoffice transaction management real estate` |  |
| 35 | 16/08/2026 | [AI's Impact on Real Estate Is Shrinking, and Bad Data Is Why](https://infina.ai/news/ai-data-readiness-for-real-estate-brokerages/) | `ai data readiness for real estate brokerages` |  |
| 36 | 17/08/2026 | [Harvard Study Puts a Number on AI's Threat to Real Estate Agent Jobs](https://infina.ai/news/ai-job-substitution-risk-real-estate-agents/) | `ai job substitution risk real estate agents` |  |
| 38 | 19/08/2026 | [Lone Wolf Just Bet the Future of Real Estate AI Isn't a Separate App](https://infina.ai/news/embedded-ai-real-estate-brokerage-platforms/) | `embedded ai real estate brokerage platforms` |  |
| 56 | 20/08/2026 | [ATTOM's New AI Agents Let You Ask Property Questions in Plain English](https://infina.ai/news/ai-property-research-tools-real-estate-teams/) | `ai property research tools real estate teams` |  |
| 63 | 21/08/2026 | [Only 9% of Real Estate Firms Have Actually Scaled Their AI, New Survey Finds](https://infina.ai/news/ai-deployment-maturity-real-estate-firms/) | `ai deployment maturity real estate firms` |  |
| 65 | 23/08/2026 | [TurboHome's AI Hybrid Model Just Cut a Home Buying Commission by Thousands](https://infina.ai/news/ai-flat-fee-brokerage-model-real-estate-agents/) | `ai flat fee brokerage model real estate agents` |  |
| 80 | 25/08/2026 | [41% of Agents Use AI. Almost Half Say It Changed Nothing.](https://infina.ai/news/ai-usage-without-measurable-impact-real-estate-agents/) | `ai usage without measurable impact real estate agents` |  |
| 82 | 27/08/2026 | [Before You Buy Software Number 12, Ask Your AI Assistant to Replace It](https://infina.ai/news/ai-assistant-instead-of-software-stack-real-estate-agents/) | `ai assistant instead of software stack real estate agents` |  |
| 85 | 30/08/2026 | [Brokerage Leaders' AI Worry Score Just Jumped, and Agentic AI Is Why](https://infina.ai/news/agentic-ai-risk-concerns-real-estate-brokerage-leaders/) | `agentic ai risk concerns real estate brokerage leaders` |  |
| 86 | 31/08/2026 | [Agents Are Seeding Reddit to Win ChatGPT Recommendations, and Reddit Just Pushed Back](https://infina.ai/news/ai-visibility-reddit-seeding-backlash-real-estate-agents/) | `ai visibility reddit seeding backlash real estate agents` |  |
| 87 | 02/09/2026 | [A 50-Year Broker's Advice on What Actually Gets an AI Citation](https://infina.ai/news/ai-citation-content-real-estate-agent-websites/) | `ai citation content real estate agent websites` |  |
| 89 | 2026-04-09 | [Keller Williams Just Gave Agents an AI Tool That Claims to Save 10 Hours a Week](https://infina.ai/news/ai-video-marketing-automation-real-estate-agents/) | `ai video marketing automation real estate agents` |  |
| 90 | 05/09/2026 | [Coldwell Banker's CEO Just Called ChatGPT 'Sycophantic' About Home Prices](https://infina.ai/news/chatgpt-sycophantic-pricing-advice-real-estate-agents/) | `chatgpt sycophantic pricing advice real estate agents` |  |
| 91 | 06/09/2026 | [A Real Brokerage Just Put an AI Avatar Named Mae on Its Website](https://infina.ai/news/ai-digital-human-brokerage-website-adoption/) | `ai digital human brokerage website adoption` |  |
| 93 | 08/09/2026 | [Compass Says Its AI Just Cut CMA Prep From 90 Minutes to 15](https://infina.ai/news/ai-comparative-market-analysis-minutes-real-estate-agents/) | `ai comparative market analysis minutes real estate agents` |  |
| 95 | 10/09/2026 | [UWM's New ChatGPT App Shows Where AI Search Is Headed for Agents Too](https://infina.ai/news/chatgpt-app-mortgage-matchup-real-estate-agent-visibility/) | `chatgpt app mortgage matchup real estate agent visibility` |  |
| 96 | 11/09/2026 | [Northwest MLS Just Launched an AI Home Search With Zero Ads and Zero Lead Forms](https://infina.ai/news/mls-ai-conversational-search-broker-attribution-agents/) | `mls ai conversational search broker attribution agents` |  |
| 97 | 13/09/2026 | [Bright MLS Is Building an AI Academy for 100,000 Agents](https://infina.ai/news/ai-academy-role-based-learning-mls-subscribers/) | `ai academy role based learning mls subscribers` |  |
| 98 | 14/09/2026 | [HomeSmart's AI Now Reads a Contract and Automates the Closing Behind It](https://infina.ai/news/ai-contract-data-extraction-closing-automation-agents/) | `ai contract data extraction closing automation agents` |  |
| 108 | 16/09/2026 | [Mortgage Rates Just Hit a 52-Week High: What It Means for Agent Response Times](https://infina.ai/news/mortgage-rate-spike-real-estate-agent-response/) | `mortgage rate spike real estate agent response` |  |
| 109 | 16/09/2026 | [53% of Brokerages Now Plan AI for Back-Office Work, Up From 23% in 2024](https://infina.ai/news/ai-back-office-automation-real-estate-brokerages/) | `ai back office automation real estate brokerages` |  |
| 111 | 18/09/2026 | [Google Just Took Home Listing Ads Nationwide, and Zillow Stock Dropped](https://infina.ai/news/google-home-listing-ads-real-estate-agent-leads/) | `google home listing ads real estate agent leads` |  |
| 114 | 21/09/2026 | [Real Brokerage's Leo 2.0 Is Holding Hundreds of Conversations at Once](https://infina.ai/news/ai-relationship-manager-for-real-estate-leads/) | `ai relationship manager for real estate leads` |  |
| 115 | 22/09/2026 | [NAR's 2026 Report Shows AI Use Climbing, but Concentrated in One Place](https://infina.ai/news/ai-powered-follow-up-messages-real-estate-agents/) | `ai powered follow up messages real estate agents` |  |
| 116 | 23/09/2026 | [Compass Got 15,000 Agents to Generate 97,000 AI Conversations in Weeks](https://infina.ai/news/ai-likely-to-sell-alerts-real-estate-agents/) | `ai likely to sell alerts real estate agents` |  |
| 117 | 24/09/2026 | [SERHANT. Unveils Dot, an AI That Runs Agents' Days Without Being Asked](https://infina.ai/news/ai-chief-of-staff-for-real-estate-agents/) | `ai chief of staff for real estate agents` |  |
| 118 | 25/09/2026 | [37% of Buyers Would Let AI Handle a Home Purchase With Minimal Human Help](https://infina.ai/news/ai-home-valuation-tool-real-estate-agent-website/) | `ai home valuation tool real estate agent website` |  |
| 119 | 26/09/2026 | [Down Payments Just Hit a Four-Year Q2 Low While Payments Jumped 74%](https://infina.ai/news/financing-readiness-signals-for-real-estate-buyer-leads/) | `financing readiness signals for real estate buyer leads` |  |
| 122 | 29/09/2026 | [Interactive Room Visualization Is Driving Up to 170% More Showing Requests](https://infina.ai/news/ai-listing-visualization-feature-real-estate-agents/) | `ai listing visualization feature real estate agents` |  |
