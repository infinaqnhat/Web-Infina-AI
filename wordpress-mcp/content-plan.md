# Content Plan

File này gồm 2 phần: (1) content plan đang chạy cho RealSaleX, và (2) content map — toàn bộ 122
bài đã publish trên site, map theo đúng khung pillar + cluster của `pillar-cluster-writer/SKILL.md`
(86 bài evergreen chia theo pillar/cluster/funnel role, 36 bài News để riêng) — dùng để check
cannibalization trước khi viết bài mới hoặc lên plan mới. Xem "Phần 2" ở cuối file, gồm cả 1 mục
"Cannibalization cần audit" — **tất cả 10 cặp phát hiện khi map lần 01/10/2026 đã audit xong**
(6 merge, 2 internal-link fix, 2 giữ nguyên không đổi — xem chi tiết từng cặp + refresh-log.md).

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
| [#207 — Best Real Estate Agent CRM Software](https://infina.ai/news/best-crm-for-real-estate/) | `best crm for real estate` | C3.1, C3.3 | ✅ **ĐỔI VAI TRÒ PILLAR (2026-10-01)**: #207 giờ là pillar chính thức Nhánh 3 RealSaleX thay cho #384 (xem lý do ở mục Cannibalization #4 + refresh-log.md) — đã hấp thụ mục "None of These Ship a True Intent Layer" + link P3 từ #384, và "Integrations That Matter" từ #412 |
| ~~#384 — Best CRM Software for Real Estate Agents~~ | `best crm software` | C3.1, C3.3 | ⚠️ ĐÃ MERGE (2026-10-01) vào #207, redirect 301 live. Lý do đổi hub: #207 có 15 inbound link sitewide sẵn có, #384 chỉ có 2 (từ CINC review + Intent Layer) — xem refresh-log.md |
| [#444 — Best CRM for Real Estate Agents: A Buyer's Guide](https://infina.ai/news/best-crm-buying-guide-real-estate-agents/) | `best crm` | C3.1, C3.3 | Giữ nguyên — BOF buying-guide khác funnel stage, không trùng #207 (xem Cannibalization #4) |
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
| ~~C3.1~~ | ~~Follow Up Boss Review~~ | ❌ Bỏ, thay bằng refresh [#207](https://infina.ai/news/best-crm-for-real-estate/) (đã đổi pillar từ #384 sang #207, 01/10/2026) | — | — | ✅ #207 đã refresh 01/10, thêm link P3 + mục Intent Layer |
| C3.2 | Review + gap thật | [CINC CRM Review: Pricing, Features, and Buyer Follow-Up Gaps](https://infina.ai/news/?p=1234) (ID 1234) | `cinc crm review` | Evaluation/MOF | ✅ Published |
| ~~C3.3~~ | ~~kvCORE Pricing~~ | ❌ Bỏ, cùng xử lý qua refresh #207 | — | — | ✅ |
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

## Phần 2: Content Map — Toàn bộ bài đã publish trên site, map theo Pillar + Cluster

Áp dụng đúng khung của `skills/pillar-cluster-writer/SKILL.md` (1 pillar bao quát + 2-4 cluster
theo vai trò funnel: So sánh/Evaluation-MOF, Review/Evaluation-MOF, Buying guide/Decision-BOF,
Support-how-to/Discovery-Post-purchase) để map lại **86 bài evergreen** (8 cụm, loại cụm News/Market
Commentary — 36 bài tin tức thời sự không có "chủ đề lớn" chung để làm pillar, không thuộc mô hình
này) đã publish trên `infina.ai/news`, không phải chỉ RealSaleX. Việc map lại này (01/10/2026) phát
hiện thêm vài cụm có dấu hiệu cannibalization CHƯA từng audit (xem mục "Cannibalization cần audit"
ở cuối) — tương tự pattern đã xử lý xong ở cụm Chatbot (xem
`skills/post-refresh/references/refresh-log.md` 01/10/2026).

**Chú thích trạng thái**: ✅ Hub/Pillar sống · ⚠️ Đã merge → stub (redirect 301, xem bảng dưới) ·
🔎 Cần audit cannibalization (title/focus keyword gần trùng, chưa kiểm tra nội dung thật).

---

### Cụm 1: Chatbot / Conversational AI — 15 bài sống (19 gốc, 4 đã merge 01/10/2026)

Cụm duy nhất đã audit + xử lý cannibalization đầy đủ (xem refresh-log.md). Có **2 pillar song song**
vì 2 góc đủ khác biệt để không cần gộp chung: Pillar A nhắm "conversational AI / lead follow-up bot",
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

### Cụm 2: CRM Software — 20 bài sống (22 gốc, 2 đã merge 2026-10-01)

**✅ ĐÃ AUDIT (2026-10-01)** — cụm cannibalization LỚN NHẤT đã xử lý xong, xem refresh-log.md.
Phát hiện 5 bài "best/top CRM" roundup trùng gần hết cùng 1 pool platform (Follow Up Boss/Lofty/
Wise Agent/LionDesk/kvCORE). 3 bài (#384 Pillar cũ, #207, #412) là duplicate thật → gộp vào #207
(đổi vai trò hub từ #384 sang #207 vì #207 có sẵn 15 inbound link sitewide, #384 chỉ có 2). 2 bài
còn lại (#419 teams-niche, #444 buying-guide/BOF) giữ nguyên vì differentiation thật.

| Vai trò | Bài | Focus keyword | Funnel | Trạng thái |
|---|---|---|---|---|
| **Pillar chính (ĐÃ ĐỔI 01/10)** | [Best Real Estate Agent CRM Software in 2026](https://infina.ai/news/best-crm-for-real-estate/) | `best crm for real estate` | Evaluation/MOF | ✅ = #207, giờ là HUB — đã hấp thụ #384 (Intent Layer section) + #412 (Integrations section) |
| ~~Pillar chính (cũ)~~ | ~~Best CRM Software for Real Estate Agents~~ | `best crm software` | Discovery/TOF | ⚠️ ĐÃ MERGE (2026-10-01) vào #207, redirect 301 live |
| **Pillar nhẹ (RealSaleX P3)** | [AI Intent Layer for Real Estate CRM: What It Adds](https://infina.ai/news/ai-intent-layer-for-real-estate-crm/) | `ai intent layer for real estate crm` | Evaluation/MOF | ✅ góc "bổ sung CRM sẵn có", khác hẳn roundup — đã sửa link trỏ về #207 thay vì #384 |
| Review (brand cụ thể) | [CINC CRM Review: Pricing, Features, and Buyer Follow-Up Gaps](https://infina.ai/news/cinc-crm-review-real-estate/) | `cinc crm review` | Evaluation/MOF | ✅ cluster của Pillar nhẹ — đã sửa link trỏ về #207 thay vì #384 |
| ~~🔎 Review/list (roundup)~~ | ~~Top CRM Tools for Real Estate Agents and Teams~~ | `crm tools for real estate` | Evaluation/MOF | ⚠️ ĐÃ MERGE (2026-10-01) vào #207, redirect 301 live |
| Review/list (niche: teams) | [Best CRM for Real Estate Teams: Top Picks for 2026](https://infina.ai/news/best-crm-for-real-estate-teams-2026/) | `best crm for real estate teams` | Evaluation/MOF | ✅ ĐÃ AUDIT: niche "teams" thật, rank tốt nhất nhóm (pos 5.0) — giữ nguyên |
| Buying guide (BOF) | [Best CRM for Real Estate Agents: A Buyer's Guide (2026)](https://infina.ai/news/best-crm-buying-guide-real-estate-agents/) | `best crm` | Decision/BOF | ✅ ĐÃ AUDIT: funnel stage khác thật (quy trình đánh giá 14 ngày, red flags) — giữ nguyên |
| Review/list (niche: free) | [Best Free CRM for Real Estate Agents in 2026](https://infina.ai/news/best-free-crm-for-real-estate-agents/) | `free crm for real estate` | Evaluation/MOF | niche hoá rõ (free tier), rủi ro thấp hơn 4 dòng trên |
| Định nghĩa | [What Is CRM Software?](https://infina.ai/news/what-is-crm-software/) | `what is crm software` | Discovery/TOF | = #230, Nhánh 4 đã bỏ, giữ nguyên không động |
| Định nghĩa (beginner) | [CRM Software 101: A Beginner's Guide](https://infina.ai/news/crm-management-real-estate-agents-beginners-guide/) | `crm management` | Discovery/TOF | = #405, Nhánh 4 đã bỏ, giữ nguyên không động |
| Định nghĩa (khác góc) | [AI CRM for Real Estate](https://infina.ai/news/ai-crm-real-estate/) | `ai crm` | Discovery/TOF | = #214, đã xác nhận khác góc Pillar nhẹ khi viết P3 |
| Sub-topic: marketing (strategy) | [CRM Marketing for Real Estate](https://infina.ai/news/crm-marketing-real-estate/) | `crm marketing` | Evaluation/MOF | ✅ ĐÃ AUDIT (2026-10-01): differentiation thật (funnel 5 giai đoạn) vs dòng dưới (định nghĩa category) — đã thêm link 2 chiều, giữ cả 2 |
| Sub-topic: marketing (định nghĩa) | [What Is CRM Marketing Software? A Guide for Real Estate Teams](https://infina.ai/news/crm-marketing-software-real-estate-guide/) | `crm marketing software` | Discovery/TOF | ✅ ĐÃ AUDIT (2026-10-01): không trùng Pillar strategy ở trên, giữ nguyên |
| Sub-topic: pipeline | [CRM Pipeline Management](https://infina.ai/news/crm-pipeline-management/) | `crm pipeline` | Evaluation/MOF | góc riêng, chưa thấy trùng |
| Bridge → Website Builder | [CRM with Website Builder: Best Integrated Platforms](https://infina.ai/news/crm-with-website-builder-real-estate/) | `crm with website builder` | Evaluation/MOF | nối cụm 3 |
| Bridge → IDX | [Real Estate CRM with IDX Integration: Best Platforms](https://infina.ai/news/real-estate-crm-with-idx/) | `real estate crm with idx` | Evaluation/MOF | nối cụm 3 |
| Cross-link → Nhánh 2 | [Speed-to-Lead: How Real Estate Agent CRM Closes the 15-Hour Gap](https://infina.ai/news/real-estate-agent-crm-speed-to-lead/) | `real estate agent crm` | Evaluation/MOF | = #223, dùng làm C2.2 thay thế ở Nhánh 2 (Phần 1) |
| Hỗ trợ (News) | [Rechat Just Let Claude and ChatGPT Run Real Estate CRM Workflows Directly](https://infina.ai/news/ai-agent-integration-for-real-estate-crm-platforms/) | `ai agent integration for real estate crm platforms` | Post-purchase/support | — |
| Hỗ trợ (News) | [Real's AI CRM Assistant Leo...](https://infina.ai/news/ai-crm-assistant-brokerage-merger-rollout-agents/) | `ai crm assistant brokerage merger rollout agents` | Post-purchase/support | — |
| Hỗ trợ (News) | [eXp Realty Says Its All-in-One AI Platform Cuts Software Costs by 70%](https://infina.ai/news/exp-nexus-crm-software-cost-reduction-agents/) | `exp nexus crm software cost reduction agents` | Post-purchase/support | — |
| Hỗ trợ (News) | [Nearly 10% of Borrowers Are Now Choosing ARMs...](https://infina.ai/news/arm-borrower-tracking-real-estate-agent-crm/) | `arm borrower tracking real estate agent crm` | Post-purchase/support | — |
| Hỗ trợ (News) | [Lofty Launches an MCP Server So Any AI Can Plug Into Its CRM](https://infina.ai/news/open-ai-protocol-real-estate-crm-brokerages/) | `open ai protocol real estate crm brokerages` | Post-purchase/support | — |

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

### Cụm 4: AI Voice / Virtual Assistant / Receptionist — 5 bài (= Nhánh 1 RealSaleX, xem Phần 1)

Cụm này trùng hoàn toàn với Nhánh 1 đã map chi tiết ở Phần 1 (P1/C1.1/C1.3/C1.4) — không lặp lại
bảng, chỉ thêm 1 bài phát hiện mới chưa từng đưa vào plan RealSaleX:

| Vai trò | Bài | Focus keyword | Funnel | Trạng thái |
|---|---|---|---|---|
| 🔎 Review/list (roundup) | [7 Best AI Virtual Assistants for Real Estate](https://infina.ai/news/best-ai-virtual-assistant-real-estate/) | `ai virtual assistant real estate` | Evaluation/MOF | 🔎 publish 17/06, TRƯỚC khi Nhánh 1 được lên plan (15/09) — chưa từng đối chiếu với Pillar #147 (`best-ai-voice-assistants-for-real-estate`), 2 bài có thể trùng nội dung thật (voice vs virtual assistant) |

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

### Cụm 7: Lead Generation / Follow-up Automation — 8 bài (= Nhánh 2 RealSaleX, xem Phần 1)

Trùng hoàn toàn với Nhánh 2 đã map chi tiết ở Phần 1 (P2/C2.1/C2.3/C2.4 + #223). Các bài còn lại
trong cụm là News hỗ trợ, chưa gắn vào plan RealSaleX:

| Vai trò | Bài | Focus keyword | Funnel | Trạng thái |
|---|---|---|---|---|
| Hỗ trợ | [Real Estate Contact Forms Are Losing the Highest-Intent Leads](https://infina.ai/news/real-estate-contact-form-conversion-rate/) | `real estate contact form conversion rate` | Post-purchase/support | — |
| Hỗ trợ (News) | [Your Next Listing Is Probably Already Sitting in Your CRM](https://infina.ai/news/database-reactivation-ai-seller-leads-real-estate-agents/) | `database reactivation ai seller leads real estate agents` | Post-purchase/support | — |
| Hỗ trợ (News) | [Realtor.com Just Named the Best Week to Buy in 2026...](https://infina.ai/news/buyer-lead-nurture-campaign-real-estate-agents/) | `buyer lead nurture campaign real estate agents` | Post-purchase/support | — |
| Hỗ trợ (News) | [Sellers Now Outnumber Buyers by 57.9%...](https://infina.ai/news/seller-lead-prioritization-real-estate-pipeline/) | `seller lead prioritization real estate pipeline` | Post-purchase/support | — |

---

### Cụm 8: Compliance / Legal / Risk — 4 bài, tất cả sống

| Vai trò | Bài | Focus keyword | Funnel | Trạng thái |
|---|---|---|---|---|
| **Pillar (nhẹ)** | [TCPA Compliance for Real Estate Agents](https://infina.ai/news/tcpa-compliance-for-real-estate-agents/) | `tcpa compliance for real estate agents` | Discovery/TOF | ✅ = #237, đã link từ #147/C1.1/C1.4/C2.4 |
| Hỗ trợ (News) | [AI-Written Listing Descriptions Are Creating Fair Housing Liability](https://infina.ai/news/ai-hallucination-risk-real-estate-listings/) | `ai hallucination risk real estate listings` | Post-purchase/support | — |
| Hỗ trợ (News) | [Colorado's New AI Law Sets a Deadline for Automated Decisions](https://infina.ai/news/ai-decision-making-compliance-real-estate-agents/) | `ai decision making compliance real estate agents` | Post-purchase/support | — |
| Hỗ trợ (News) | [Seller Impersonation Fraud Attempts Just Doubled](https://infina.ai/news/seller-impersonation-fraud-prevention-real-estate-agents/) | `seller impersonation fraud prevention real estate agents` | Post-purchase/support | — |

---

### Cannibalization cần audit (phát hiện khi map pillar+cluster, 01/10/2026 — CHƯA xử lý)

Theo đúng mức độ rủi ro giảm dần. Cách xử lý gợi ý: lặp lại quy trình đã dùng cho cụm Chatbot
(đọc full nội dung từng cặp, so sánh product/angle thật chứ không chỉ title, merge cặp nào có
>60-70% nội dung trùng, giữ nguyên cặp nào đã niche hoá đủ rõ).

| Ưu tiên | Cụm | Các bài nghi trùng | Vì sao đáng ngại |
|---|---|---|---|
| ~~1~~ | CRM Software | ✅ **ĐÃ XỬ LÝ (2026-10-01)**: [best-crm-for-real-estate](https://infina.ai/news/best-crm-for-real-estate/) (hub mới, #207) đã hấp thụ ~~best-crm-software-real-estate-agents~~ (#384, Pillar cũ) + ~~top-crm-tools-for-real-estate-teams~~ (#412) | Đọc full nội dung 5 bài: 3/5 trùng nhau thật (cùng pool 5 platform). Merge xong, đổi vai trò Pillar từ #384 sang #207 (internal link equity có sẵn ở #207: 15 vs 2). Giữ nguyên best-crm-for-real-estate-teams-2026 (niche teams) + best-crm-buying-guide-real-estate-agents (BOF). Xem refresh-log.md |
| ~~2~~ | Website Builder / IDX | ✅ **ĐÃ XỬ LÝ (2026-10-01)**: [idx-website-for-realtors](https://infina.ai/news/idx-website-for-realtors/) (hub) vs ~~best-idx-website-for-realtors~~ (merged, redirect 301 live) | Đọc full nội dung: trùng gần như toàn bộ (cùng 3/4 platform + cùng khung phân tích). Merge xong, xem refresh-log.md |
| ~~2~~ | Website Builder / IDX | ✅ **ĐÃ XỬ LÝ (2026-10-01)**: [real-estate-website-builder](https://infina.ai/news/real-estate-website-builder/) (Pillar, hub) vs ~~best-real-estate-website-builder~~ (merged, redirect 301 live) | Đọc full nội dung: 5/6 platform trùng y hệt (tagline + giá + kết luận). Merge xong, giữ lại 1 FAQ "AgentFire teams vs solo" từ bài yếu. Xem refresh-log.md |
| ~~3~~ | CRM Software | ✅ **ĐÃ XỬ LÝ (2026-10-01)**: [crm-marketing-real-estate](https://infina.ai/news/crm-marketing-real-estate/) vs [crm-marketing-software-real-estate-guide](https://infina.ai/news/crm-marketing-software-real-estate-guide/) | Đọc full nội dung: differentiation thật (funnel 5 giai đoạn vs định nghĩa category, chỉ trùng 2/4 platform). Giữ nguyên cả 2, chỉ thêm link 2 chiều |
| ~~3~~ | Chatbot | ✅ **ĐÃ XỬ LÝ (2026-10-01)**: [what-is-a-conversational-chatbot-real-estate](https://infina.ai/news/what-is-a-conversational-chatbot-real-estate/) (hub) vs ~~conversational-chat-real-estate~~ (merged) | Đọc full nội dung: trùng gần như hoàn toàn (y hệt 4 tool: Structurely/Ylopo rAIya/Tidio/ManyChat). Merge xong, redirect 301 live |
| ~~4~~ | AI Voice | ✅ **ĐÃ XỬ LÝ (2026-10-01)**: [best-ai-virtual-assistant-real-estate](https://infina.ai/news/best-ai-virtual-assistant-real-estate/) vs Pillar #147 (`best-ai-voice-assistants-for-real-estate`) | Đọc full nội dung: differentiation thật (đa kênh SMS/CRM/scheduling vs riêng voice/phone, chỉ trùng 3/7 tool). Giữ nguyên cả 2, không sửa gì |
| ~~5~~ | Website Design | ✅ **ĐÃ XỬ LÝ (2026-10-01)**: [website-design-for-real-estate-agents](https://infina.ai/news/website-design-for-real-estate-agents/) (Pillar, hub) vs ~~realtor-website-design~~ (merged) | Đọc full nội dung: trùng gần như hoàn toàn (y hệt 3 platform: AgentFire/Real Geeks/Luxury Presence). Merge xong, redirect 301 live |
| ~~5~~ | Landing Pages | ✅ **ĐÃ XỬ LÝ (2026-10-01)**: [real-estate-landing-page-guide](https://infina.ai/news/real-estate-landing-page-guide/) (Pillar) vs [high-converting-real-estate-landing-pages](https://infina.ai/news/high-converting-real-estate-landing-pages/) (cluster) | Đọc full nội dung: KHÔNG phải duplicate, là pillar/cluster hợp lệ — chỉ thiếu internal link nên Google cannibalize. Đã fix link 2 chiều, giữ cả 2 bài. Xem refresh-log.md |

**Lưu ý**: bảng trên chỉ dựa trên title + focus keyword (suy luận, chưa đọc nội dung thật) — đúng
quy trình `pillar-cluster-writer/SKILL.md` Bước 3, phải đọc full nội dung từng cặp trước khi kết
luận có cannibalize thật hay không (có thể chỉ là tên gần giống nhưng nội dung đã niche hoá đủ,
giống trường hợp #4 niche "investor" trong cụm Website Builder).
