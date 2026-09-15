# Content Plan — RealSaleX (AI Deal Room)

Money page: **RealSaleX (AI Deal Room)** — SaaS B2B cho brokerage bất động sản Mỹ.
URL: *chưa deploy* (bản draft `realsalex.html` trên nhánh `main`, chưa có path chính thức trên
`infina.ai`). Cập nhật URL thật vào đây ngay khi có, trước khi tạo bất kỳ internal link nào tới
money page (xem `skills/pillar-cluster-writer/SKILL.md`).

Nguồn dữ liệu: 1.859 keyword "sạch" lọc từ `keywords/Infina_AI_RealSale_Keyword_Stats_2026-09-15.csv`
(volume ≥500, đã loại overlap ≥60% với tracker/WordPress hiện có), gom cluster theo token/chủ đề
(xấp xỉ, chưa verify SERP thật — xem lưu ý ở cuối file). Độ ưu tiên dựa theo mức độ khớp đúng
sản phẩm RealSaleX (AI agent trả lời buyer 24/7, bổ sung lớp intent cho CRM sẵn có, KHÔNG thay thế
CRM).

**Trạng thái tổng quan: PLAN đã đối chiếu với 110 bài hiện có trên site (2026-09-15).** Chưa viết
bài mới nào. Không có credentials GSC/GA4 tại thời điểm check này nên **không xác nhận được traffic/
ranking thật** — chỉ đối chiếu được chủ đề/on-page (title, meta description, mention brand) qua nội
dung thật đã fetch. Xem mục "Bài đã có trên site" ngay dưới trước khi viết bất kỳ ID nào.

---

## Bài đã có trên site — map vào plan (check 2026-09-15)

Đối chiếu 110 bài publish (qua `list_posts` + fetch nội dung thật, không suy đoán từ tiêu đề) với
4 nhánh bên dưới. Phát hiện **trùng chủ đề khá nặng ở Nhánh 2 và Nhánh 3** — 2 nhánh này đã có sẵn
1 phần nội dung tương đương trên site, viết bài mới ở đúng góc cũ sẽ tự cannibalize chính mình.

| Bài đã có | FOCUS_KW đã log | Trùng ID nào | Mức độ | Việc nên làm |
|---|---|---|---|---|
| [#147 — 7 Best AI Voice Assistants for Real Estate Agents](https://infina.ai/news/best-ai-voice-assistants-for-real-estate/) | `ai voice assistants for real estate` | **P1, C1.2** | 🔴 Nặng — meta description bài này gần như y hệt pitch "answer every inbound call... 24/7" mà P1 định viết, có mention "outbound call" | Đổi format P1 sang explainer (khác intent với listicle #147), verify lại bằng SERP thật trước khi chốt |
| [#223 — Speed-to-Lead: How Real Estate Agent CRM Closes the 15-Hour Gap](https://infina.ai/news/real-estate-agent-crm-speed-to-lead/) | `real estate agent crm` | **C2.2** | 🔴 Nặng — đã có đúng số liệu 15-hour/40-50%, đã mention Follow Up Boss + kvCORE | Bỏ viết C2.2 mới, refresh bài này (skill `post-refresh`) + thêm link về money page |
| [#384 — Best CRM Software for Real Estate Agents: Full Comparison](https://infina.ai/news/best-crm-software-real-estate-agents/) | `best crm software` | **C3.1, C3.3** | 🔴 Nặng — đã cover Follow Up Boss + kvCORE | Bỏ viết C3.1/C3.3 dạng bài riêng, refresh 1 trong 3 bài CRM roundup thay vì tạo bài mới |
| [#207 — Best Real Estate Agent CRM Software in 2026](https://infina.ai/news/best-crm-for-real-estate/) | `best crm for real estate` | **C3.1, C3.3** | 🔴 Nặng — cùng lý do trên | (gộp chung xử lý với #384) |
| [#444 — Best CRM for Real Estate Agents: A Buyer's Guide](https://infina.ai/news/best-crm-buying-guide-real-estate-agents/) | `best crm` | **C3.1, C3.3** | 🔴 Nặng — cùng lý do trên | (gộp chung xử lý với #384) |
| [#230 — What Is CRM Software?](https://infina.ai/news/what-is-crm-software/) | `what is crm software` | **C4.1** | 🔴 Nặng — đúng góc giáo dục "CRM là gì" | Bỏ hẳn C4.1 |
| [#405 — CRM Software 101](https://infina.ai/news/crm-management-real-estate-agents-beginners-guide/) | `crm management` | **C4.1** | 🔴 Nặng — cùng lý do trên | (gộp chung xử lý với #230) |
| [#214 — AI CRM for Real Estate](https://infina.ai/news/ai-crm-real-estate/) | `ai crm` | **P3** | 🟡 Cần verify | Chủ đề "AI + CRM" liền kề P3 ("AI Intent Layer cho CRM"), check SERP thật trước khi chốt P3 |
| [#390 — AI ISAs Are Delivering 3x Higher Conversion Rates](https://infina.ai/news/ai-isa-conversion-rates-real-estate/) | — | **C2.1** | 🟡 Nhẹ | Góc khác (ISA con người, không phải phần mềm), khả năng vẫn viết được C2.1 nhưng nên đọc lại trước |
| [#521 — Real Estate Contact Forms Are Losing the Highest-Intent Leads](https://infina.ai/news/real-estate-contact-form-conversion-rate/) | — | **C2.1** | 🟡 Nhẹ | Góc form capture, không phải lead-gen software roundup — khả năng vẫn ổn |
| **CINC** (brand) | — | **C3.2** | ✅ Không tìm thấy ở bài nào | Gap thật, giữ nguyên trong plan |

**Không tìm thấy bài nào trùng**: C1.1, C1.3, C1.4, C2.3, C2.4 — 5 slot này vẫn là gap thật theo dữ
liệu đã check, nhưng vẫn cần chạy Bước 1.5 (live-SERP) trước khi viết như quy trình yêu cầu, đây
chỉ là kết quả check trên site mình, chưa check SERP Google thật.

---

## Nhánh 1: AI Answering / Call Center / Receptionist — 🥇 ưu tiên cao nhất

Vì sao cao nhất: đúng câu pitch chính của sản phẩm ("AI agent trả lời buyer 24/7 trong Deal Room
riêng"), không phải liên tưởng xa.

| ID | Vai trò | Tiêu đề dự kiến | Focus keyword (tier volume) | Funnel | Trạng thái |
|---|---|---|---|---|---|
| P1 | **Pillar** | AI Receptionist for Real Estate: How 24/7 AI Call Answering Works | `ai receptionist` (50k, niche xuống "for real estate" khi viết) | Discovery/TOF | 🔴 Trùng #147 — đổi format sang explainer trước khi viết |
| C1.1 | So sánh | AI Receptionist vs Human Receptionist: What Real Estate Teams Should Know | `ai call center` (50k) | Evaluation/MOF | ✅ Gap, viết mới được |
| C1.2 | Review/deep-dive | Best AI Call Center Software for Real Estate Brokerages in 2026 | `ai call center software` (5k) | Evaluation/MOF | 🔴 Trùng #147 (cùng format listicle) — cân nhắc gộp vào refresh #147 thay vì bài riêng |
| C1.3 | Buying guide | How to Choose an AI Answering Service for Your Brokerage | `ai answering service` (5k) | Decision/BOF | ✅ Gap, viết mới được |
| C1.4 | Support/how-to (bắc cầu sang Nhánh 2) | How AI Outbound Calling Works for Real Estate Lead Follow-Up | `ai outbound call` (50k) | Post-purchase/how-to | ✅ Gap (chỉ 1 mention nhỏ ở #147), viết mới được |

Internal link dự kiến: P1 ↔ C1.1/C1.3/C1.4, C1.4 ↔ P2 (Nhánh 2), P1 ↔ #147 (refresh, link chéo 2
chiều thay vì cannibalize), tất cả link về money page RealSaleX.

---

## Nhánh 2: Lead Generation + Follow-up Automation — 🥇 ưu tiên cao nhất

Vì sao cao nhất: khớp thẳng "The Leak" trong pitch deck (40-50% lead không được follow-up,
follow-up 30%→90%) — đúng pain point sản phẩm giải quyết.

| ID | Vai trò | Tiêu đề dự kiến | Focus keyword (tier volume) | Funnel | Trạng thái |
|---|---|---|---|---|---|
| P2 | **Pillar** | Real Estate Lead Follow-Up Automation: The Complete 2026 Guide | `lead generation for realestate` (5k) | Discovery/TOF | ✅ Gap, viết mới được |
| C2.1 | Review/list | Best Lead Generation Software for Realtors in 2026 | `lead generation software` (500) | Evaluation/MOF | 🟡 Đọc lại #390/#521 trước, khả năng vẫn viết được |
| ~~C2.2~~ | ~~Giải thích/pain-point~~ | ~~Why 40-50% of Real Estate Leads Never Get a Response~~ | `crm follow up` (500) | Discovery | ❌ **Bỏ, trùng #223** — refresh #223 thay thế |
| C2.3 | Buying guide/how-to | How to Set Up Automated Lead Follow-Up for Your Brokerage | `lead generation systems` (500) | Decision/BOF | ✅ Gap, viết mới được |
| C2.4 | Niche/kênh cụ thể | Facebook Lead Gen for Realtors: Turning Ad Leads Into Booked Showings | `facebook lead generation ads` (500) | Decision/BOF, long-tail dễ rank | ✅ Gap, viết mới được |

Internal link dự kiến: P2 ↔ C2.1/C2.3/C2.4, P2 ↔ #223 (refresh, thay cho C2.2), P2 ↔ P1 (chéo
nhánh), tất cả link về money page RealSaleX.

---

## Nhánh 3: CRM Add-on / Alternatives & Pricing (brand-specific) — 🥈 tốt, góc khác

Lưu ý bắt buộc khi viết (đã note từ vòng phân tích trước): viết theo góc **"X CRM thiếu gì mà cần
thêm lớp intent"**, KHÔNG viết theo góc "X vs Y CRM nào tốt hơn" — vì target là người **đã có
CRM rồi**, RealSaleX bổ sung chứ không thay thế. Mọi claim về tính năng/giá của brand đối thủ phải
verify qua web search thật (Bước 1.5-kiểu `seo-blog-writer`) trước khi viết, không suy đoán.

| ID | Vai trò | Tiêu đề dự kiến | Focus keyword (tier volume) | Funnel | Trạng thái |
|---|---|---|---|---|---|
| P3 | **Pillar (nhẹ)** | Why Your Real Estate CRM Needs an AI Intent Layer (Follow Up Boss, CINC, kvCORE...) | `crm and lead generation` (500) | Evaluation/MOF | 🟡 Đọc lại #214 trước, khả năng vẫn viết được nếu góc khác rõ |
| ~~C3.1~~ | ~~Review + gap~~ | ~~Follow Up Boss Review~~ | `follow up boss reviews` (500) | Evaluation/MOF | ❌ **Bỏ, trùng #384/#207/#444** — refresh 1 trong 3 bài đó, thêm mục "gap buyer intent" |
| C3.2 | Review + gap | CINC CRM Review: Pricing, Features, and What's Missing for Buyer Follow-Up | `cinc reviews` (500) | Evaluation/MOF | ✅ Gap thật (không tìm thấy CINC ở bài nào), viết mới được |
| ~~C3.3~~ | ~~Review + gap~~ | ~~kvCORE Pricing and Features~~ | `kvcore pricing` (500) | Evaluation/MOF | ❌ **Bỏ, trùng #384/#207/#444** — cùng lý do C3.1 |

Internal link dự kiến: P3 ↔ C3.2, P3 ↔ #384 (chọn 1 bài refresh làm đại diện cho Follow Up
Boss/kvCORE), P3 ↔ P2 (định vị bổ sung CRM), tất cả link về money page RealSaleX.

---

## Nhánh 4: CRM Software (generic) — ❌ đã bỏ hẳn, không còn cân nhắc

Lý do ban đầu (🥉 rủi ro lệch intent) nay có thêm bằng chứng trực tiếp: #230 và #405 đã cover đúng
góc "CRM là gì / CRM 101" mà C4.1 định viết. Không tạo pillar riêng, không còn giữ C4.1 ở dạng
backlog nữa.

---

## Bị loại khỏi plan (không dùng)

- **Local-intent** ("realtor near me"...) — khớp SERP local pack, sai định dạng site.
- **Consumer FSBO/tìm agent** ("sell house without realtor"...) — audience là người mua/bán nhà,
  lệch với audience thật (broker/agent).
- **Document/Transaction Management** — sản phẩm hoạt động ở giai đoạn buyer tìm hiểu/so sánh,
  không phải giai đoạn ký hợp đồng.
- **Website/IDX, Reviews/Reputation** — không liên quan sản phẩm hoặc đã có pillar cũ cover.

---

## Việc cần làm trước khi viết bài thật (theo đúng quy trình `pillar-cluster-writer`)

1. ✅ Đã đối chiếu với 110 bài hiện có trên site (2026-09-15) — xem mục "Bài đã có trên site" ở
   trên. Còn thiếu: chạy Bước 1.5 (live-SERP Google thật) cho từng FOCUS_KW còn lại (✅/🟡 ở trên),
   bảng hiện tại mới là token-matching + đối chiếu nội bộ, chưa check SERP ngoài.
2. Check cannibalize 3 lớp đầy đủ (log/tracker sheet + sitemap thật + chính file này) trước khi
   chốt từng FOCUS_KW, theo Bước 3 của `pillar-cluster-writer`.
3. Xác nhận URL money page thật trên `infina.ai` trước khi làm internal link 2 chiều (Bước 6).
4. Với 3 slot bị bỏ (C2.2, C3.1, C3.3) và Nhánh 4: lên kế hoạch refresh bài cũ (#223, #384 hoặc
   #207/#444, #230/#405) qua skill `post-refresh` thay vì viết bài mới — cần chạy GSC/GA4 (đang
   thiếu credentials) để biết bài nào trong nhóm trùng đang có traffic tốt nhất, ưu tiên refresh
   bài đó.
5. Chốt nhánh nào làm trước — đề xuất: **Nhánh 1 trước** (P1 đổi format + C1.1/C1.3/C1.4 viết mới),
   rồi Nhánh 2 (C2.1/C2.3/C2.4 viết mới + refresh #223), Nhánh 3 sau cùng (C3.2 viết mới + refresh
   1 bài CRM roundup).

*(Không có mục nào trong file này là bài đã publish — cột trạng thái sẽ thêm khi bài thật được
tạo, theo đúng Bước 8.5.)*
