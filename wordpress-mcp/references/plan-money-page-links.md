# Plan: link blog posts to the money page https://infina.ai/ (chờ duyệt, chưa làm)

Cập nhật 13/10/2026. Link tới **`https://infina.ai/`** (URL sạch, không `#fragment`, không UTM). Mỗi bài đúng 1 link. Anchor ≤8 từ, đa dạng. Mọi câu đều ghi "Infina AI, our own product" để công khai đây là sản phẩm của mình. Chỉ dùng điều trang money page đã nói (trả lời câu hỏi về listing 24/7, hiện nguồn, cho agent thấy câu hỏi của buyer, QR/link).

Không cần chờ dev xong: URL đích không đổi. Sau khi dev deploy thì verify lại và Request Indexing.

| # | Ưu tiên | Bài | Chữ | Vị trí chèn | Câu đề xuất (anchor trong [ ]) |
|---|---|---|---|---|---|
| 1 | P1 | #1232 `ai-intent-layer-for-real-estate-crm` | 743 | What an Intent Layer Actually Adds | One example is Infina AI, our own product: [an AI assistant that shows buyer intent] by turning each buyer's questions about a listing into signals you can act on. |
| 2 | P1 | #1449 `follow-up-boss-real-estate-crm` | 1511 | Can You Add an Intent Layer on Top of Follow Up Boss? | Infina AI, our own product, is built as an add-on rather than a CRM replacement: an [AI assistant for real estate agents] that answers buyer questions on each listing and shows you what they asked. |
| 3 | P1 | #1234 `cinc-crm-review-real-estate` | 615 | What's Missing for Buyer Follow-Up | If you want to see what buyers ask before anyone calls them, Infina AI, our own product, adds [an AI assistant on top of your CRM] that answers questions on each listing. |
| 4 | P1 | #1487 `customer-engagement-platform-vs-crm` | 1340 | What to Check Before You Add an Engagement Layer | For listings, one option is Infina AI, our own product, which gives each property [its own AI assistant for buyers] that answers at any hour. |
| 5 | P1 | #1223 `real-estate-lead-follow-up-automation-guide` | 2456 | Where AI Changes the Equation | One way to apply this is Infina AI, our own product, which [answers buyer questions on each listing] at any hour and shows you what they asked. |
| 6 | P1 | #1227 `how-to-set-up-automated-lead-follow-up-real-estate` | 551 | Step 5: Where to Add AI Once the Basics Work | A simple place to start is Infina AI, our own product: paste a listing link and get [an AI assistant that answers 24/7] for that home. |
| 7 | P1 | #147 `best-ai-voice-assistants-for-real-estate` | 2246 | Before Related Reading | If you want buyers to get answers without a phone call, Infina AI, our own product, is an [AI assistant for real estate agents] that turns a listing link into a private page where buyers can ask questions at any time. |
| 8 | P1 | #1106 `ai-assistant-instead-of-software-stack-real-estate-agents` | 779 | Before Related Reading | This is the idea behind Infina AI, our own product: an [AI assistant for real estate agents] that handles listing questions instead of adding another tool to the stack. |
| 9 | P1 | #1056 `best-conversational-ai-chatbot-for-real-estate` | 3006 | Where the Handoff to a Human Belongs | In this article's terms, Infina AI, our own product, is [an AI assistant for your listings] that answers buyers and shows you what they asked, so you decide when to step in. |
| 10 | P1 | #1100 `real-estate-chatbot-that-reads-listing-photos` | 763 | The Bigger Trend | Infina AI, our own product, works from the listing itself: [an AI expert for any listing] that answers buyer questions using listing data and shows its sources. |
| 11 | P1 | #110 `best-ai-virtual-assistant-real-estate` | 1774 | After the list of 7 tools | Infina AI, our own product, is one more option: [an AI assistant for each listing] that answers buyers at any hour and shows you their questions. |
| 12 | P1 | #918 `open-house-landing-page` | 1676 | How to Promote Your Open House Landing Page | Infina AI, our own product, lets you print [a QR code that opens an AI assistant] on a sign or flyer so visitors can ask questions at any hour. |
| 13 | P2 | #89 `best-chatbot-customer-service-real-estate` | 3915 | Before You Switch It On | Infina AI, our own product, is [an AI assistant that answers buyers 24/7] for a single listing. |
| 14 | P2 | #1078 `chatbot-vs-live-agent-real-estate` | 1341 | The Hybrid Model | Infina AI, our own product, follows that model: [an AI assistant that hands off to you] by showing you each question so you can join when a buyer is ready. |
| 15 | P2 | #1071 `ai-chat-vs-sms-real-estate` | 1343 | The Winning Strategy | Infina AI, our own product, uses chat rather than texts: [AI chat on every listing] that buyers open from a link or QR code. |
| 16 | P2 | #223 `real-estate-agent-crm-speed-to-lead` | 1538 | Why Most Agents Still Have a Speed-to-Lead Problem | Infina AI, our own product, helps on the listing side by [answering buyer questions instantly] so a buyer is not left waiting. |
| 17 | P2 | #930 `real-estate-landing-page-guide` | 1880 | What Separates High-Converting Pages | Infina AI, our own product, pairs a listing page with [a built-in AI expert] that answers questions. |
| 18 | P2 | #1415 `cost-per-lead-for-real-estate-agents` | 1060 | Lowering Your Effective Cost Per Lead | Infina AI, our own product, [answers every buyer question instantly] on each listing, so a lead is not left waiting for a reply. |
| 19 | P2 | #1825 `real-estate-marketing (pillar)` | 2340 | follow-up section | Infina AI, our own product, is an [AI assistant for real estate agents] for the follow-up and listing-question side of this plan. |
| 20 | P2 | #214 `ai-crm-real-estate` | 1739 | After choosing an AI CRM | Infina AI, our own product, adds [an AI assistant beyond the CRM] that answers listing questions. |

**Anchor đúng từ khoá "AI assistant for real estate agents":** #1449, #147, #1106, #1825 (4/20). Còn lại là anchor mô tả.

**Để dành, chưa link:** #1213, #1217, #1219 (voice, ít khớp sản phẩm), #1225, #1229 (bài mỏng, ít khớp).

## Cách làm khi duyệt
- `update_post` từng bài, chỉ thêm 1 câu có link vào đúng mục, không đổi ngày/category; diff nội dung trước và sau; ghi `refresh-log.md`.
- P1 (12 bài) làm trước; P2 (8 bài) sau nếu bạn duyệt.
- Sau khi dev deploy: kiểm tra HTML trang chủ có title/meta/JSON-LD/H1, rồi Request Indexing trong Search Console.

## Cần bạn quyết
1. Danh sách P1 (12 bài), vị trí và câu: có đổi bài/câu nào không?
2. Có làm luôn P2 (8 bài) trong cùng lượt không?
3. Câu "Infina AI, our own product" ở mọi bài: giữ nguyên hay rút gọn?
