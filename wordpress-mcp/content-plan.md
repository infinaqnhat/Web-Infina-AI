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
| [#147 — 7 Best AI Voice Assistants for Real Estate Agents](https://infina.ai/news/best-ai-voice-assistants-for-real-estate/) | `ai voice assistants for real estate` | **P1, C1.2** | 🔴 Nặng — meta description bài này gần như y hệt pitch "answer every inbound call... 24/7" mà P1 định viết, có mention "outbound call" | **Cập nhật 2026-09-15 (đã verify SERP thật)**: bỏ hẳn viết P1/C1.2 mới, refresh #147 làm pillar chính thức của Nhánh 1, đổi FOCUS_KW sang `ai receptionist for real estate` — xem chi tiết ở mục Nhánh 1 |
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

**Không tìm thấy bài nào trùng**: C1.1, C1.3, C1.4, C2.3, C2.4 — gap thật. Riêng **C1.1/C1.3/C1.4
đã verify thêm bằng live-SERP thật** (xem mục Nhánh 1), C2.3/C2.4 vẫn mới chỉ check nội bộ site,
chưa chạy Bước 1.5.

### Bài bổ trợ / liên quan (không phải trùng — chỉ để link thêm cho nhánh dày hơn)

Sau khi loại các bài trùng nặng + verify SERP thật cho Nhánh 1, plan chỉ còn **9 bài mới cần viết**
(3 + 4 + 2) và **4 việc refresh** (#147, #223, 1 trong 3 bài CRM roundup, và tùy chọn thêm), khá
mỏng so với plan gốc 13 bài. Đối chiếu thêm với 110 bài hiện có tìm được
8 bài **không trùng chủ đề nhưng liên quan đủ gần để link vào** — không tính là node pillar/cluster
mới, chỉ dùng làm "bài liên quan"/nguồn trích dẫn số liệu ngay trong nội dung bài mới, giúp mỗi
nhánh có nhiều internal link + context hơn mà không tốn công viết thêm.

| Bài đã có | Vì sao liên quan | Gắn vào nhánh nào |
|---|---|---|
| [#237 — TCPA Compliance for Real Estate Agents](https://infina.ai/news/tcpa-compliance-for-real-estate-agents/) | Luật FCC 2026 về consent cho AI gọi/nhắn tin tự động — áp dụng trực tiếp cho AI answering lẫn AI follow-up | Nhánh 1 (P1, C1.4) + Nhánh 2 (C2.3, C2.4) |
| [#390 — AI ISAs Are Delivering 3x Higher Conversion Rates](https://infina.ai/news/ai-isa-conversion-rates-real-estate/) | Số liệu thật: 3x conversion, -35% cost/lead, 7x appointment — dẫn chứng mạnh cho cả 2 nhánh | Nhánh 1 (P1, C1.1) + Nhánh 2 (P2) |
| [#1071 — AI Chat vs SMS Follow-Up for Real Estate](https://infina.ai/news/ai-chat-vs-sms-real-estate/) | So sánh kênh follow-up trực tiếp, không trùng software roundup | Nhánh 2 (C2.3) |
| [#1078 — Chatbot vs Live Agent for Real Estate](https://infina.ai/news/chatbot-vs-live-agent-real-estate/) | Response time/conversion — hỗ trợ luận điểm tốc độ trả lời của P2 | Nhánh 2 (P2, C2.1) |
| [#521 — Real Estate Contact Forms Are Losing the Highest-Intent Leads](https://infina.ai/news/real-estate-contact-form-conversion-rate/) | Số liệu 0.6% conversion rate, 78% buyer theo người reply trước — dẫn chứng cho pain point | Nhánh 2 (C2.1, C2.4) |
| [#1122 — Your Next Listing Is Probably Already Sitting in Your CRM](https://infina.ai/news/database-reactivation-ai-seller-leads-real-estate-agents/) | Database reactivation, 10-20x ROI từ CRM cũ — góc khác với "setup follow-up mới" | Nhánh 2 (C2.3) |
| [#1026 — Rechat Just Let Claude and ChatGPT Run Real Estate CRM Workflows Directly](https://infina.ai/news/ai-agent-integration-for-real-estate-crm-platforms/) | Case thật: AI agent chạy trực tiếp trong CRM — đúng luận điểm "CRM cần thêm lớp AI/intent" của P3 | Nhánh 3 (P3) |
| [#1171 — Real's AI CRM Assistant Leo Is About to Meet 180,000 New RE/MAX Agents](https://infina.ai/news/ai-crm-assistant-brokerage-merger-rollout-agents/) | Case thật khác, quy mô lớn — thêm dẫn chứng cho P3 | Nhánh 3 (P3) |

**Vẫn còn khá mỏng?** Đúng — đây là plan chỉ dựa trên 2988 keyword volume≥500 sau khi lọc; nếu muốn
nhiều bài hơn có 2 hướng: (1) hạ ngưỡng volume xuống dưới 500 để mở thêm long-tail (rủi ro: nhiều
biến thể/lỗi chính tả không dùng được, đã thấy ở batch loại bỏ ban đầu), hoặc (2) sau khi Nhánh 1+2
publish và có GSC data thật, dùng `post-refresh` để tìm striking-distance keyword mới nảy sinh từ
chính các bài mới này, mở rộng cluster theo dữ liệu thật thay vì đoán trước.

---

## Nhánh 1: AI Answering / Call Center / Receptionist — 🥇 ưu tiên cao nhất

Vì sao cao nhất: đúng câu pitch chính của sản phẩm ("AI agent trả lời buyer 24/7 trong Deal Room
riêng"), không phải liên tưởng xa.

### Check keyword + live-SERP (2026-09-15) — đổi cả cách chọn keyword lẫn cấu trúc nhánh

Check lại toàn bộ 9.524 dòng CSV gốc (không chỉ file đã lọc volume≥500): **không có bất kỳ biến thể
nào ghép "real estate" với receptionist/call center/answering service/outbound call.** 5 FOCUS_KW
ban đầu (`ai receptionist`, `ai call center`, `ai call center software`, `ai answering service`,
`ai outbound call`) đều là thuật ngữ generic, không phân biệt ngành.

Chạy live-SERP thật (web search) cho từng keyword:

| Keyword | SERP thật | Kết luận |
|---|---|---|
| `ai receptionist` (bare) | Toàn trang sản phẩm vendor (Zoom, RingCentral, Retell AI, GoTo...) | 🔴 Navigational — không nhắm keyword bare này |
| `ai call center software` (bare) | Toàn site review SaaS lớn (Verint, Aircall, Zendesk...), 0 kết quả real estate | 🔴 Quá rộng, không cạnh tranh nổi |
| `ai receptionist for real estate` (niche, không có trong CSV) | 10+ bài "Best AI Receptionist for Real Estate... Compared" thật (cloudtalk, evs7, getaira, dialraven, callbirdai, agentzap, kennarealestate, marblism, dialnote, callagentai) | ✅ Nhu cầu có thật, nhưng rất đông đối thủ, định dạng listicle/so sánh |
| `ai answering service for real estate` (niche) | 6+ bài "X options compared" thật (elevenlabs, evs7, myaifrontdesk, withallo, beside, vocalyai, serviceagent) | ✅ Có thật, cũng khá đông |
| `ai outbound calling real estate lead follow-up` (niche) | Mix explainer + listicle (retellai, aloware, instadesk, connectcallai, lumay...), ít đối thủ site-native hơn 2 keyword trên | ✅ Cơ hội tốt nhất trong nhóm |
| "AI vs human receptionist real estate" | getaira.io đã có bài đúng góc "Cost & ROI Compared" | ✅ Góc thật, vẫn làm được nếu đủ khác biệt |

**Phát hiện thêm**: nhiều bài đối thủ nhắc **Fair Housing compliance** khi AI receptionist trả lời
câu hỏi buyer — góc này chưa bài nào của mình (kể cả #147) cover, ghép với #237 (TCPA) đã có sẵn
thành 1 lợi thế khác biệt thật, không phải phỏng đoán.

**Sửa sai của bản plan trước**: từng đề xuất "đổi P1 sang explainer để tránh trùng format với #147"
— sai, vì SERP thật cho thấy định dạng đúng cho intent này là **listicle/so sánh**, không phải
explainer (đổi format ngược SERP là lỗi theo đúng Bước 1.5). Vấn đề thật là P1 và #147 đang nhắm
**chung 1 intent** ("best AI answering cho real estate"), không phải vấn đề format.

### Cấu trúc mới

| ID | Vai trò | Tiêu đề dự kiến | Focus keyword | Funnel | Trạng thái |
|---|---|---|---|---|---|
| P1 | **Pillar = refresh #147** (không viết bài mới) | Giữ tiêu đề #147 hoặc đổi nhẹ, thêm góc RealSaleX + Fair Housing/TCPA compliance | `ai receptionist for real estate` (niche, đổi từ `ai voice assistants for real estate`) | Discovery/TOF | ✅ **Đã refresh 2026-09-15** — thêm H2 Fair Housing/TCPA (link #237), thêm đoạn dẫn chứng #390, thêm "AI Receptionist" vào intro + 1 H2, đổi seo_description. Giữ nguyên title/slug/seo_focus_keyword (chưa có GSC để biện minh đổi). Log chi tiết ở `skills/post-refresh/references/refresh-log.md`. Đã thêm link 2 chiều tới C1.4 (2026-09-15). Còn thiếu: mention RealSaleX cụ thể + link money page (chờ URL thật), link tới C1.1/C1.3 (chờ viết xong) |
| ~~C1.2~~ | ~~Review/deep-dive~~ | ~~Best AI Call Center Software...~~ | — | — | ❌ Bỏ hẳn, gộp vào refresh #147 |
| C1.1 | So sánh | AI Receptionist vs Human Receptionist: Cost, ROI, and What Real Estate Teams Should Know | `ai receptionist vs human receptionist real estate` (niche, long-tail, không có volume CSV — nhu cầu xác nhận qua SERP) | Evaluation/MOF | ✅ Viết mới, đã verify SERP |
| C1.3 | Buying guide | How to Choose an AI Answering Service for Your Brokerage | `ai answering service for real estate` (niche, đổi từ bare `ai answering service`) | Decision/BOF | ✅ Viết mới, đã verify SERP |
| C1.4 | Support/how-to (bắc cầu sang Nhánh 2) | [AI Outbound Calling for Real Estate: How It Works in 2026](https://infina.ai/news/ai-outbound-calling-real-estate-lead-follow-up/) (post ID 1213) | `ai outbound calling for real estate` | Post-purchase/how-to | ✅ **Đã publish 2026-09-15** — 891 từ, density FOCUS_KW ~2%, link nội bộ tới #147 (pillar) + #237 (TCPA), 1 external dofollow (agentzap.ai). Featured image tái sử dụng ảnh của #147. Đã quay lại update #147 thêm link 2 chiều tới bài này (nhân tiện sửa 1 câu lặp có sẵn trong bản gốc #147). Còn thiếu: link tới P2 (chưa viết) và money page (chưa có URL) |

Nhánh 1 giờ chỉ còn **3 bài viết mới + 1 refresh** (thay vì 4 bài mới + tham chiếu #147 như trước).
Internal link dự kiến: #147 (refresh, đóng vai pillar) ↔ C1.1/C1.3/C1.4, C1.4 ↔ P2 (Nhánh 2), tất cả
link về money page RealSaleX.

**Việc cần làm tiếp cho nhánh này**: khi GSC có lại credentials, check traffic/ranking thật của
#147 trước khi refresh — nếu #147 đang có traffic tốt, refresh nhẹ (thêm section mới) để không phá
vỡ ranking hiện có; nếu traffic yếu, có thể viết lại sâu hơn.

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
