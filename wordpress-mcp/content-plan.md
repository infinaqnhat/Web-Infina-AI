# Content Plan — RealSaleX (AI Deal Room)

Money page: **RealSaleX (AI Deal Room)** — SaaS B2B cho brokerage bất động sản Mỹ.
URL: *chưa deploy* (bản draft `realsalex.html` trên nhánh `main`, chưa có path chính thức trên
`infina.ai`). Cập nhật URL thật vào đây ngay khi có, rồi quay lại **cả 9 bài mới** bên dưới để
thêm internal link tới money page (xem `skills/pillar-cluster-writer/SKILL.md`) — đây là việc
còn thiếu duy nhất áp dụng cho toàn bộ plan.

**🎉 Trạng thái tổng quan (2026-09-15): CẢ 3 NHÁNH ĐÃ VIẾT XONG.** 9 bài mới (3 pillar + 6 cluster)
đã viết, 4 bài cũ đã refresh, tất cả đã publish hoặc lên lịch tự động. Không cần viết thêm bài nào
trừ khi mở rộng plan sau này (xem mục cuối file).

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

## Nhánh 3: CRM Add-on / Alternatives & Pricing — 🥈 ưu tiên 2 — ✅ HOÀN THÀNH

Góc bắt buộc: viết kiểu "CRM sẵn có thiếu gì mà cần thêm lớp intent", KHÔNG viết "X vs Y CRM nào
tốt hơn" — target là người đã có CRM rồi, RealSaleX bổ sung chứ không thay thế.

| ID | Vai trò | Bài | Focus keyword | Funnel | Trạng thái |
|---|---|---|---|---|---|
| P3 | Pillar (nhẹ) | [AI Intent Layer for Real Estate CRM: What It Adds](https://infina.ai/news/?p=1232) (ID 1232) | `ai intent layer for real estate crm` | Evaluation/MOF | 🕐 Schedule 22/09 10:00 |
| ~~C3.1~~ | ~~Follow Up Boss Review~~ | ❌ Bỏ, thay bằng refresh [#384](https://infina.ai/news/best-crm-software-real-estate-agents/) | — | — | ✅ #384 đã refresh 15/09, thêm link P3 |
| C3.2 | Review + gap thật | [CINC CRM Review: Pricing, Features, and Buyer Follow-Up Gaps](https://infina.ai/news/?p=1234) (ID 1234) | `cinc crm review` | Evaluation/MOF | 🕐 Schedule 23/09 10:00 |
| ~~C3.3~~ | ~~kvCORE Pricing~~ | ❌ Bỏ, cùng xử lý qua refresh #384 | — | — | ✅ |

**Đổi FOCUS_KW so với plan gốc**: `crm and lead generation` → `ai intent layer for real estate crm`
(P3, khớp SERP thật về "AI follow-up shift to intent signals" thay vì generic CRM+leadgen). C3.2
dùng `cinc crm review` (niche cụ thể hơn `cinc reviews`). Dữ liệu CINC thật (giá từ $900/tháng,
gói Solo/Ramp/Pro/Select, điểm mạnh/yếu) đã verify qua web search trước khi viết, không suy đoán.

Internal link: P3 ↔ C3.2 (2 chiều), P3 ↔ #384 (refresh, thay C3.1/C3.3), P3 ↔ #214 (link chéo,
không cannibalize), P3 ↔ P2 (định vị bổ sung CRM).

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
