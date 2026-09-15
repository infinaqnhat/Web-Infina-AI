# External SEO Toolkit

Bộ công cụ SEO WordPress di động: viết bài chuẩn SEO, theo dõi Google Search Console (+ GA4/
Clarity tùy chọn), refresh bài cũ dựa trên data thật. Được tách ra từ 1 site production khác
để tái dùng cho site/repo mới. **Không bao gồm** phần mạng xã hội (Facebook/TikTok),
chỉ tập trung blog + Search Console monitor + đăng bài qua WordPress.

## Đọc file này trước khi làm bất cứ điều gì

Nếu bạn là Claude và vừa được kết nối vào 1 repo mới có chứa thư mục `external-seo-toolkit/`
này (ví dụ do người dùng tải zip về rồi upload lên repo khác), đây chính là tài liệu bootstrap.
Đọc hết file này trước khi chạy bất kỳ skill nào bên trong.

## Cấu trúc thư mục

```
external-seo-toolkit/
├── README.md                              # File này
├── wp-mcp-server-snippet.php              # Snippet cài lên WordPress đích để Claude gọi được
│                                           # (chỉ có tool cho bài viết — xem ghi chú dưới nếu
│                                           # cần dùng skill pillar-cluster-writer)
├── secrets/
│   └── README.md                          # Hướng dẫn, không chứa key thật
├── references/
│   ├── content-planning-framework.md      # Best practice keyword research, độ dài bài, pillar-cluster
│   ├── content-strategy-framework.md      # Khung 7 bước keyword→content plan + GEO/zero-click 2026
│   │                                       # + Bước 1.5 check rủi ro bản quyền/nội dung cấm
│   └── used-keywords-template.md          # Đổi tên thành used-keywords.md khi dùng
└── skills/
    ├── seo-blog-writer/
    │   ├── SKILL.md                       # Quy trình viết bài chuẩn Rank Math SEO
    │   └── references/content-planning-framework.md
    ├── pillar-cluster-writer/
    │   ├── SKILL.md                       # Lên plan + viết bộ pillar+cluster gắn money page
    │   └── scripts/
    │       ├── generate_image_ref.py      # Generate ảnh AI bám sát ảnh tham chiếu thật (ưu tiên)
    │       └── generate_image.py          # Generate ảnh AI chay bằng text (phương án cuối)
    └── post-refresh/
        ├── SKILL.md                       # Quy trình rà + refresh bài cũ qua GSC/GA4/Clarity
        ├── references/
        │   ├── post-refresh-playbook.md   # Khung chẩn đoán triệu chứng GSC
        │   ├── refresh-log.md             # Log các lần đã sửa (bắt đầu trống)
        │   └── content-planning-framework.md
        └── scripts/
            ├── gsc_client.py              # Client Google Search Console API
            ├── ga4_client.py              # Client Google Analytics 4 Data API (tùy chọn)
            ├── clarity_client.py          # Client Microsoft Clarity Data Export API (tùy chọn)
            ├── check_image_similarity.py  # So sánh ảnh trùng (aHash, dùng Pillow)
            └── generate_image.py          # Generate ảnh minh họa qua Gemini (tùy chọn)
```

**Cập nhật 2026-09-15 — đã đồng bộ tool quản lý sản phẩm:** `wp-mcp-server-snippet.php` giờ có đầy
đủ tool WooCommerce (`create_product`/`update_product`/`delete_product`/`get_product`/`list_products`,
`create_product_variation`/`update_product_variation`/`list_product_variations`, cùng nhóm quản lý
money page `set_affiliate_redirect`/`delete_affiliate_redirect`/`list_affiliate_redirects` (cloak link
`/go/<slug>`) và `set_product_faq`/`delete_product_faq` (FAQPage schema)), port trực tiếp từ snippet
gốc của site production kia và genericize (đổi prefix riêng của site đó thành
`seo_mcp_`/`seo_go`/`_seo_faq_schema`, bỏ tên miền/Shopee cứng trong mô tả tool). Skill
`pillar-cluster-writer` giờ dùng được trọn vẹn Bước 6/6.1/6.2 (link 2 chiều money page, CTA cloak link,
FAQ schema) trên site mới mà không cần tự viết thêm code PHP. **Yêu cầu:** site đích phải chạy
WooCommerce (các tool sản phẩm sẽ báo lỗi rõ ràng nếu WooCommerce chưa bật, không âm thầm hỏng).

## Checklist setup cho site mới (làm theo đúng thứ tự)

### 1. Cài kết nối WordPress MCP trên site đích

Site WordPress cần cài snippet `wp-mcp-server-snippet.php` (qua plugin WPCode hoặc file
functions.php của theme con) để Claude gọi được API tạo/sửa bài. Snippet đã sẵn sàng dùng,
chỉ cần:

1. Dán nguyên nội dung file vào WPCode (PHP Snippet, Insert Method: Auto Insert, Location: Run
   Everywhere), hoặc nơi tương đương trên site đích.
2. Set secret thật cho `SEO_MCP_SECRET` theo 1 trong 2 cách ghi chú ngay đầu file PHP (định nghĩa
   hằng số trong `wp-config.php`, hoặc set qua WP-CLI/`update_option`). Sinh secret ngẫu nhiên
   bằng `php -r "echo bin2hex(random_bytes(24));"`.
3. Kiểm tra endpoint hoạt động: `POST https://domain-that/wp-json/seo-mcp/v1/blog?key=<secret>`
   với body JSON-RPC `{"jsonrpc":"2.0","method":"tools/list","id":1}` phải trả về danh sách tool.
4. Trong Claude Code, kết nối site này qua 1 MCP connector riêng (không dùng chung connector với
   site production cũ), hoặc lưu `SEO_MCP_SECRET`/endpoint để gọi thẳng qua `curl` nếu không dùng
   connector.

### 2. Tạo Google service account cho Search Console (bắt buộc nếu dùng skill `post-refresh`)

1. Tạo project trên Google Cloud Console, bật Search Console API và Google Analytics Data API.
2. Tạo service account, tải key dạng JSON.
3. Vào Google Search Console của site đích, Settings > Users and permissions > Add user, thêm
   đúng email của service account (dạng `...@...iam.gserviceaccount.com`), quyền `Restricted`
   (chỉ đọc) là đủ.
4. Set biến môi trường `SEO_GSC_SA_JSON` = nội dung JSON key nén thành 1 dòng:
   ```bash
   python3 -c "import json;print(json.dumps(json.load(open('key.json'))))"
   ```
   Hoặc lưu file JSON gốc (không nén) vào `secrets/gsc-service-account.json` nếu repo private và
   chấp nhận lưu secret trong repo (xem cảnh báo trong `secrets/README.md`).
5. Set biến `SEO_GSC_SITE_URL` = domain đầy đủ của site đích (vd `https://domain-cua-ban.com/`).

### 3. (Tùy chọn) Thêm Google Analytics 4

1. Vào GA4 Admin > Account Access Management, thêm đúng email service account ở bước 2 (không
   cần key riêng, dùng chung), quyền Viewer trở lên.
2. Lấy Property ID trong GA4 Admin > Property Settings (dãy số, KHÔNG phải Measurement ID dạng
   `G-XXXXXXX`).
3. Set biến `SEO_GA4_PROPERTY_ID` = property ID đó.

### 4. (Tùy chọn) Thêm Microsoft Clarity

1. Vào project Clarity của site đích, tạo API token cho Data Export API.
2. Set biến `SEO_CLARITY_TOKEN`, hoặc lưu vào `secrets/clarity-token.txt` (1 dòng, không có
   ký tự xuống dòng thừa).

### 5. Điền context site vào skill viết bài

Mở `skills/seo-blog-writer/SKILL.md`, điền các mục `[ĐIỀN: ...]` ở đầu file (tên site, domain,
ngách sản phẩm, cấu trúc blog subfolder/subdomain, tông giọng viết).

Nếu cũng dùng `skills/pillar-cluster-writer/SKILL.md` (viết bộ bài gắn 1 trang sản phẩm/money
page cụ thể, không riêng bài đơn lẻ): điền thêm mục `[ĐIỀN: ...]` ở đầu file đó (nền tảng bán
hàng, file guideline on-page riêng nếu có, tên file content plan/log keyword), và đọc
`references/content-strategy-framework.md` trước khi lên plan cụm đầu tiên.

### 6. Khởi tạo file theo dõi

- Copy `references/used-keywords-template.md` thành `references/used-keywords.md`. Nếu site đã
  có bài từ trước, seed lại bảng từ `post-sitemap.xml` hoặc tool `list_posts` (đọc title/slug
  các bài cũ, backfill focus keyword theo cách đoán từ title, ghi rõ nguồn `suy đoán`).
- `skills/post-refresh/references/refresh-log.md` để trống là được, tự điền dần khi refresh bài.

### 7. (Tùy chọn) Nếu cũng cần content pillar tin tức tự động

Toolkit này KHÔNG bao gồm skill kiểu "news-to-post" (rà tin + viết + đăng tự động hàng ngày) vì
đó là phần đặc thù theo ngách của site gốc (rulebook nguồn tin, tiêu chí lọc). Nếu site mới cũng
cần dạng này, viết mới 1 skill riêng theo đúng ngách của site đó, có thể tham khảo cấu trúc
6 bước (kiểm tra trùng → rà tin → tra keyword → chọn tin → viết → đăng) làm khung, nhưng phần
rulebook (nguồn tin cụ thể, tiêu chí chọn) phải viết lại hoàn toàn.

## Biến môi trường cần thiết (tổng hợp)

| Biến | Bắt buộc cho | Ghi chú |
|---|---|---|
| `SEO_MCP_KEY` | Đăng/sửa bài WordPress | Secret đã set trong `wp-mcp-server-snippet.php` |
| `SEO_GSC_SA_JSON` | Skill `post-refresh` | Nội dung JSON service account, nén 1 dòng |
| `SEO_GSC_SITE_URL` | Skill `post-refresh` | Domain đầy đủ, có `https://` và `/` cuối |
| `SEO_GA4_PROPERTY_ID` | GA4 (tùy chọn) | Số property, không phải Measurement ID |
| `SEO_CLARITY_TOKEN` | Clarity (tùy chọn) | Token JWT Data Export API |
| `GEMINI_API_KEY` | Generate ảnh AI (tùy chọn) | Chỉ cần nếu dùng `generate_image.py` |

## Cách dùng sau khi setup xong

- **Viết bài mới, đơn lẻ** (tin tức, review, so sánh không gắn cụ thể 1 trang sản phẩm): dùng
  skill `seo-blog-writer` (đọc `skills/seo-blog-writer/SKILL.md`), sau khi viết xong đăng qua tool
  WordPress MCP đã kết nối ở bước 1.
- **Viết bộ bài pillar+cluster gắn 1 trang sản phẩm/money page cụ thể** (tránh rủi ro thin
  affiliate/doorway page): dùng skill `pillar-cluster-writer` (đọc
  `skills/pillar-cluster-writer/SKILL.md`), skill này tự gọi `seo-blog-writer` ở Bước 5 cho từng
  bài, không cần chạy tay 2 skill riêng.
- **Check/refresh bài cũ**: dùng skill `post-refresh` (đọc `skills/post-refresh/SKILL.md`), kéo
  data GSC/GA4/Clarity thật rồi chẩn đoán theo `post-refresh-playbook.md` trước khi đề xuất sửa.
- Cả 3 skill đều tự đối chiếu `references/used-keywords.md` để tránh viết trùng chủ đề đã có.
- `references/content-strategy-framework.md` là lý thuyết nền chung cho cả `seo-blog-writer` lẫn
  `pillar-cluster-writer` — đọc lại khi lên plan 1 cụm nội dung mới hoặc khi cần đánh giá lại
  hướng đang làm, không phải quy trình thực thi từng bước.

## Nguồn gốc

Bộ toolkit này được rút ra và tổng quát hóa từ skill thật đã dùng production cho 1 site thương
mại điện tử ngách đồ chơi retro khác, qua nhiều vòng chỉnh sửa dựa trên case thật (lỗi
CTR benchmark, lỗi heading giả, lỗi ảnh trùng, giới hạn thật của Clarity API...). Phần case cụ
thể của site gốc đã được lược bỏ khi tách ra đây, chỉ giữ lại khung phương pháp chung.
