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

**Trạng thái tổng quan: mới chỉ là PLAN, chưa viết bài nào.** Chờ duyệt trước khi viết thật (đúng
Bước 4 của `pillar-cluster-writer`).

---

## Nhánh 1: AI Answering / Call Center / Receptionist — 🥇 ưu tiên cao nhất

Vì sao cao nhất: đúng câu pitch chính của sản phẩm ("AI agent trả lời buyer 24/7 trong Deal Room
riêng"), không phải liên tưởng xa.

| ID | Vai trò | Tiêu đề dự kiến | Focus keyword (tier volume) | Funnel |
|---|---|---|---|---|
| P1 | **Pillar** | AI Receptionist for Real Estate: How 24/7 AI Call Answering Works | `ai receptionist` (50k, niche xuống "for real estate" khi viết) | Discovery/TOF |
| C1.1 | So sánh | AI Receptionist vs Human Receptionist: What Real Estate Teams Should Know | `ai call center` (50k) | Evaluation/MOF |
| C1.2 | Review/deep-dive | Best AI Call Center Software for Real Estate Brokerages in 2026 | `ai call center software` (5k) | Evaluation/MOF |
| C1.3 | Buying guide | How to Choose an AI Answering Service for Your Brokerage | `ai answering service` (5k) | Decision/BOF |
| C1.4 | Support/how-to (bắc cầu sang Nhánh 2) | How AI Outbound Calling Works for Real Estate Lead Follow-Up | `ai outbound call` (50k) | Post-purchase/how-to |

Internal link dự kiến: P1 ↔ C1.1/C1.2/C1.3/C1.4, C1.4 ↔ P2 (Nhánh 2), tất cả link về money page
RealSaleX.

---

## Nhánh 2: Lead Generation + Follow-up Automation — 🥇 ưu tiên cao nhất

Vì sao cao nhất: khớp thẳng "The Leak" trong pitch deck (40-50% lead không được follow-up,
follow-up 30%→90%) — đúng pain point sản phẩm giải quyết.

| ID | Vai trò | Tiêu đề dự kiến | Focus keyword (tier volume) | Funnel |
|---|---|---|---|---|
| P2 | **Pillar** | Real Estate Lead Follow-Up Automation: The Complete 2026 Guide | `lead generation for realestate` (5k) | Discovery/TOF |
| C2.1 | Review/list | Best Lead Generation Software for Realtors in 2026 | `lead generation software` (500) | Evaluation/MOF |
| C2.2 | Giải thích/pain-point | Why 40-50% of Real Estate Leads Never Get a Response (and How to Fix It) | `crm follow up` (500) | Discovery, nuôi cả P1 lẫn P2 |
| C2.3 | Buying guide/how-to | How to Set Up Automated Lead Follow-Up for Your Brokerage | `lead generation systems` (500) | Decision/BOF |
| C2.4 | Niche/kênh cụ thể | Facebook Lead Gen for Realtors: Turning Ad Leads Into Booked Showings | `facebook lead generation ads` (500) | Decision/BOF, long-tail dễ rank |

Internal link dự kiến: P2 ↔ C2.1-C2.4, C2.2 ↔ P1 (chéo nhánh), tất cả link về money page RealSaleX.

---

## Nhánh 3: CRM Add-on / Alternatives & Pricing (brand-specific) — 🥈 tốt, góc khác

Lưu ý bắt buộc khi viết (đã note từ vòng phân tích trước): viết theo góc **"X CRM thiếu gì mà cần
thêm lớp intent"**, KHÔNG viết theo góc "X vs Y CRM nào tốt hơn" — vì target là người **đã có
CRM rồi**, RealSaleX bổ sung chứ không thay thế. Mọi claim về tính năng/giá của brand đối thủ phải
verify qua web search thật (Bước 1.5-kiểu `seo-blog-writer`) trước khi viết, không suy đoán.

| ID | Vai trò | Tiêu đề dự kiến | Focus keyword (tier volume) | Funnel |
|---|---|---|---|---|
| P3 | **Pillar (nhẹ)** | Why Your Real Estate CRM Needs an AI Intent Layer (Follow Up Boss, CINC, kvCORE...) | `crm and lead generation` (500) | Evaluation/MOF |
| C3.1 | Review + gap | Follow Up Boss Review: What It Does Well and Where It Falls Short on Buyer Intent | `follow up boss reviews` (500) | Evaluation/MOF |
| C3.2 | Review + gap | CINC CRM Review: Pricing, Features, and What's Missing for Buyer Follow-Up | `cinc reviews` (500) | Evaluation/MOF |
| C3.3 | Review + gap | kvCORE Pricing and Features: Is It Enough to Convert More Buyers? | `kvcore pricing` (500) | Evaluation/MOF |

Internal link dự kiến: P3 ↔ C3.1-C3.3, P3 ↔ P2 (định vị bổ sung CRM), tất cả link về money page
RealSaleX.

---

## Nhánh 4: CRM Software (generic) — 🥉 rủi ro lệch intent, KHÔNG làm pillar riêng

`customer management software` (500k) có volume rất cao nhưng người search đang **muốn mua 1 CRM
mới** — lệch với RealSaleX (không phải CRM). Chỉ dùng dạng giáo dục, không target trực tiếp làm
FOCUS_KW chính.

| ID | Vai trò | Tiêu đề dự kiến | Focus keyword | Funnel | Gắn vào nhánh nào |
|---|---|---|---|---|---|
| C4.1 (tùy chọn, backlog) | Giải thích | Why a CRM Alone Isn't Enough to Convert Real Estate Leads | `crm follow up` hoặc biến thể dài hơn, KHÔNG dùng `customer management software` làm FOCUS_KW chính | Discovery | Cluster phụ của P2, không phải pillar riêng |

**Không tạo pillar riêng cho nhánh này.** Chỉ cân nhắc C4.1 làm 1 bài bổ sung sau khi Nhánh 1+2 đã
xong, không ưu tiên ngay.

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

1. Verify từng FOCUS_KW qua Bước 1.5 (live SERP thật: đúng search intent + check cannibalize
   ≥3-4 URL overlap với 110 bài hiện có) — bảng trên mới chỉ dựa token-matching xấp xỉ, chưa check
   SERP thật.
2. Check cannibalize 3 lớp (log/tracker sheet + sitemap thật + chính file này) trước khi chốt từng
   FOCUS_KW, theo Bước 3 của `pillar-cluster-writer`.
3. Xác nhận URL money page thật trên `infina.ai` trước khi làm internal link 2 chiều (Bước 6).
4. Chốt nhánh nào làm trước — đề xuất: **Nhánh 1 trước** (đúng lõi sản phẩm nhất, ít rủi ro trùng
   nhất), rồi Nhánh 2, Nhánh 3 sau cùng.

*(Không có mục nào trong file này là bài đã publish — cột trạng thái sẽ thêm khi bài thật được
tạo, theo đúng Bước 8.5.)*
