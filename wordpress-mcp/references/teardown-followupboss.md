# Teardown: followupboss.com (2026-10-07)

Chạy bằng `scripts/competitor_teardown.py`, 691 trang thật trong 26 giây, không bị chặn bot.
Phương pháp đầy đủ ở `competitor-pillar-teardown.md`. File này chỉ ghi kết quả và kết luận.

```bash
python3 -I wordpress-mcp/scripts/competitor_teardown.py www.followupboss.com --workers 10 --delay 0.05
```

## Quy mô

| Thư mục | Trang | Ghi chú |
|---|---|---|
| `/blog` | 368 | nội dung chính |
| `/integrations` | 209 | programmatic SEO, mỗi tool 1 trang |
| `/customer-results` | 22 | case study |
| `/features` | 19 | trang sản phẩm |
| `/guides` | 16 | lead magnet, không phải SEO |
| còn lại | 57 | so sánh đối thủ, legal, event |

## Ba cái bẫy đọc số, bắt được đủ cả ba

Bảng thô xếp 3 trang đầu là `/blog` (54% inbound), `/integrations` (33%) và `/double-your-deals`
(32%). **Không trang nào là pillar.** Hai trang đầu là archive, trang thứ ba là CTA nằm trong vùng
`<main>` nên không bị bước lọc header/footer của script loại ra. Phải trừ cả ba rồi mới xếp hạng lại.
Đây đúng là trap #4 và #5 trong guide, và lần này cả hai xuất hiện cùng lúc trên một site.

## Phát hiện lớn nhất: 1/4 blog của họ không phải nội dung SEO

| Loại | Bài | Tỷ lệ mồ côi |
|---|---|---|
| Nội dung SEO thật | 276 (75%) | 29% |
| Changelog / feature roundup 2014-2019 | 62 (17%) | **71%** |
| Interview / masterclass / case study | 29 (8%) | 14% |

62 bài changelog kiểu `april-2017-feature-roundup` là di sản blog công ty thời đầu, 71% trong số đó
không nhận một link biên tập nào. Nếu chỉ nhìn con số "367 bài blog" mà kết luận họ gấp 2,6 lần mình
thì sai: số bài thật sự cạnh tranh là **276**, tức gấp 1,9 lần.

## Cấu trúc: không phải pillar-cluster, mà là lưới có một hố trũng

8 hub mạnh nhất **link chéo lẫn nhau rất dày**, mỗi hub trỏ tới 4-5 hub còn lại. Đó là lưới, không
phải mô hình hub-and-spoke như site mình.

Ngoại lệ là `/blog/best-real-estate-crm`: **nhận 115 inbound, chỉ trỏ ra 15 link, trong đó đúng 2
link tới hub khác**. Nó hút link vào và gần như không nhả ra. Đây là money page của họ (trang mà họ
tự xếp mình số 1), và cả site được thiết kế để dồn internal PageRank về đó.

| Hub | IN | OUT | Chữ | Link/1.000 |
|---|---|---|---|---|
| `best-real-estate-crm` | **115** | 15 | 4.216 | 3,6 |
| `free-lead-generation-ideas-real-estate` | 86 | 28 | 2.554 | 11,0 |
| `real-estate-team` | 67 | 29 | 3.407 | 8,5 |
| `spheres-influence` | 66 | 14 | 3.869 | 3,6 |
| `real-estate-scripts` | 39 | 18 | 5.053 | 3,6 |
| `real-estate-drip-email` | 39 | 21 | 3.196 | 6,6 |
| `real-estate-marketing` | 37 | 32 | 3.337 | 9,6 |
| `real-estate-lead-management` | 33 | 19 | 3.284 | 5,8 |

Hub của họ dài **2.554-5.053 chữ**, trung bình ~3.400, tỷ lệ link 3,6-11/1.000. Nằm trong hoặc hơi
trên dải 3-5 mình đang dùng. Không có gì cực đoan, chỉ là làm đều tay và làm lâu.

`/guides` thì **không phải nội dung SEO**: 16 trang lead magnet, mỗi trang chỉ có đúng 1 link ra
(quay về `/guides`), 4 trang không ai trỏ vào. Cố ý làm ngõ cụt để bắt form.

## Mồ côi: 36%, tệ hơn mình

246/691 trang không có inbound biên tập, gồm 127 bài blog và 95 trang integration. So với site mình
27% trước khi vá và 13% sau Batch 1. **Một đối thủ lớn hơn, lâu đời hơn, nhiều nguồn lực hơn vẫn để
hơn 1/3 site mồ côi.** Kỷ luật link nội bộ không tự đến theo quy mô, và Bước 6.5 của mình là lợi thế
thật chứ không phải việc làm cho đẹp.

## Bản đồ chủ đề: ai sở hữu cái gì

**Họ sở hữu, mình trống hoàn toàn:**

| Mảng | Bài của họ | Ví dụ |
|---|---|---|
| Team: tuyển, onboard, ISA, văn hoá, accountability | 27 | `real-estate-team`, `agent-onboarding`, `how-to-hire-real-estate-agent-assistants` |
| Sales skill, script, coaching | ~21 | `real-estate-scripts`, `expired-listing-scripts`, `real-estate-coaching` |
| Interview / masterclass với agent thật | 29 | `interview-with-ryan-rodenbeck` |

**Mình sở hữu, họ trống hoàn toàn:** chatbot (14 bài), conversational AI (7), website builder (9),
web design (7), MLS (5), broker/brokerage (8), compliance và risk (4), mortgage (3).

**Cùng đánh:** `crm` mình 27 bài / họ 9. `lead` + `leads` + `follow` họ 51+ / mình 20.

## Kết luận

**Phân loại (bước 5 của guide): họ là cả hai.** Một outlier asset là money page CRM, cộng một
topical network thật trên lead gen và vận hành team. Không phải kiểu site chỉ ăn may một bài.

**Ba điều rút ra cho mình:**

1. **Đừng đánh trực diện vào lead gen và team ops.** Đó là lưới 8 hub, mỗi hub 3.000+ chữ, xây từ
   2014. Chi phí đuổi kịp không hợp lý.
2. **Mảng AI/chatbot/compliance/website của mình họ bỏ trống tuyệt đối.** Không phải vì mình nhanh
   hơn, mà vì đó không phải sản phẩm của họ. Đây là moat thật và nên dồn vào.
3. **Mô hình money page sink đáng học, và mình đang làm rồi.** #207 nhận 47 inbound trên 143 trang
   (33%), còn tập trung hơn tỷ lệ 115/691 (17%) của họ. Không cần đổi gì.

**Gap cấu trúc (bước 6):** trong cả lưới của họ **không có pillar nào** về compliance, AI disclosure,
chatbot, hay website/IDX. Đó là các structural node bỏ trống, và chúng khớp đúng mảng mình đã có bài.

## Lưu ý về độ chính xác

Số chữ đo bằng cách cắt `<main>`/`<article>` tới `<footer>` rồi strip tag, nên là xấp xỉ, có thể lẫn
chữ của CTA trong vùng main. Số inbound đã trừ 3 link template nói ở trên nhưng không trừ các link
template nhỏ hơn ngưỡng 25%. Phân loại changelog/interview làm bằng regex trên slug, biên có thể lệch
vài bài. Dùng để so sánh tương đối, không dùng làm số tuyệt đối.
