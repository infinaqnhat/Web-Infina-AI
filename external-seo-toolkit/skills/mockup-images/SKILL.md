---
name: mockup-images
description: >
  Dựng ảnh minh họa THỰC TẾ cho bài blog bằng mockup HTML chụp thành JPG MOBILE-FIRST (canvas rộng 1000px, chữ đọc được trên điện thoại): tờ flyer,
  postcard, danh thiếp, logo, slide listing presentation, trang hồ sơ/bio, tin nhắn xin review, trang
  web mẫu, bảng so sánh có chú thích số. Chữ trong ảnh chính xác (không dùng AI vẽ chữ), nội dung
  hư cấu và ghi chú ngay trên ảnh. Dùng khi bài nói về một thứ nhìn thấy được mà người đọc muốn xem
  ví dụ ("examples", "templates", "layouts", "what to include"), khi infographic icon chung chung
  không cho thấy đối tượng của bài, hoặc khi người dùng nói "ảnh minh họa thực tế", "ảnh mockup",
  "ảnh ví dụ thật". Đi kèm các skill viết bài (`pillar-cluster-writer`, `news-to-cluster-article`,
  `seo-blog-writer`); không thay cho ảnh HERO (ảnh người/bối cảnh) hay ảnh STATS (số liệu).
---

# Mockup images: ảnh minh họa thực tế bằng HTML

Đúc kết từ đợt nâng ảnh Cụm 9 ngày 13/10/2026 (59 ảnh cho 20 bài). Lý do ra đời: ảnh cũ là 1 ảnh hero
+ 3 infographic icon chung chung, không cho thấy thứ bài đang nói (bài "Flyers: Examples, Templates"
không có tờ flyer nào). Kiểm 12 bài top SERP và bài của Salesforce cho thấy đối thủ hoặc không có ảnh,
hoặc dùng ảnh chụp ví dụ thật có chú thích nguồn. Bài đứng đầu SERP khó nhất (The Close, door knocking)
thậm chí không có ảnh mà vẫn thắng nhờ bảng và kịch bản copy được. Chi tiết ở
bản audit SERP ảnh của site gốc (không kèm trong toolkit; tự audit 10-12 bài top SERP cho chủ đề của bạn trước khi chọn kiểu ảnh).

## Khi nào dùng, khi nào không

| Dùng skill này | Không dùng |
|---|---|
| Bài về tài liệu/vật phẩm nhìn thấy được: flyer, postcard, thẻ, logo, slide, bio, tin nhắn, trang web, hồ sơ | Ảnh HERO có người hoặc bối cảnh (Gemini, theo skill viết bài) |
| Tiêu đề hứa "examples / templates / layouts / what to include" | Ảnh STATS mang một con số thật của bài (Gemini infographic, ≤20 ký tự) |
| Cần sơ đồ có chú thích số (anatomy) hoặc A so với B có nội dung thật | Ảnh chụp màn hình sản phẩm thật của chính site bạn (chụp màn hình sản phẩm, ghi nguồn) |

Nguyên tắc chọn: **mỗi H2 chính có một thứ cụ thể để xem thì có thể có một mockup**. Mỗi bài 2 đến 3 ảnh, giữ
hero và featured, thay 2 ảnh loại "3 icon" và "A vs B". Không đặt 2 ảnh sát nhau (xem `seo-blog-writer`).

## Quy trình

1. **Chọn cảnh.** Đọc outline bài (H2, bảng, danh sách) và chọn 2 đến 3 chỗ mà người đọc muốn xem ví dụ. Xem
   `references/scene-catalog.md` để lấy cảnh có sẵn; cảnh mới thì copy một file trong `scripts/scenes/` làm mẫu.
2. **Viết nội dung cảnh sát bài.** Chữ trong mockup phải **khớp với bài** (cùng câu mẫu, cùng số, cùng thuật ngữ). Nếu bài có
   bảng "yếu và mạnh" thì mockup dùng đúng các câu đó. Không thêm số liệu mới không có trong bài.
3. **Render.** `MOCKUP_OUT=<thư mục tạm> python3 scripts/scenes/s_m_<nhóm>.py [tên_cảnh]` ghi `m_<tên>.jpg`. Cảnh mới luôn dựng canvas **1000px rộng** (`page(h,'',note='',size=(1000,cao))`, xem mục "Dựng cảnh mobile-first"); ảnh 1600x900 là kiểu cũ, không dùng nữa. Đặt
   `MOCKUP_OUT` ra ngoài repo (scratchpad). Chạy KHÔNG kèm `-I` vì cần import `common.py` và `segno` (`pip install segno`).
4. **Kiểm cỡ chữ trên điện thoại và xem bằng mắt, bắt buộc.** `render()` in `phone min ...px ... OK/TOO SMALL`; chỉ upload khi `OK`. Rồi `python3 scripts/phone_preview.py out.jpg m_<tên>.jpg` để xem ảnh trong khung điện thoại 360px. `python3 scripts/sheet.py sheet.jpg <tên1> <tên2> ...` rồi đọc ảnh. Lỗi hay gặp: chú thích đè
   lên ảnh, chấm chỉ dẫn lệch đối tượng, chữ bị cắt, khoảng trống lớn, chữ cũ trùng lặp. Sửa tọa độ rồi render lại.
5. **Upload.** `python3 scripts/upload_staging.py <thư mục> <tên...>` lấy URL uguu, rồi `upload_media` (WordPress MCP) với alt dạng
   `<keyword chính> <mô tả ảnh>`. Ghi lại URL media mới vào một `spec.json` (mẫu `references/spec-example.json`).
6. **Chèn vào bài.** `python3 scripts/apply_mockups.py spec.json <post_id> in.html out.html [--mobile]`
   (`--mobile` đọc `spec['mobile_round'][post_id]` để THAY ảnh thế hệ 1 bằng bản mobile-first; không cờ thì đọc `spec['posts']`). Mục `media` của spec: `tên: [url, alt]` hoặc `[url, alt, caption]`; có caption thì ảnh được bọc `<figcaption class="wp-element-caption">`. Hành vi: xóa figure có alt chứa chuỗi trong
   `remove`, thay figure trong `replace`, chèn trước `<h2>` trong `before_h2`. Script kiểm **chữ (bỏ figure) và danh sách href không đổi**.
   Rồi `update_post(content=...)`.
   - **Đọc câu chữ quanh ảnh định xóa.** Nếu bài có câu như "Notice the contrast in the image above" thì **giữ** ảnh đó (ghi vào `remove` là sai); grep `image above|the image|chart|infographic` trước khi chốt `remove`.
   - **Nội dung gốc phải là bản live.** Bài `future` không đọc được qua REST công khai. Chờ publish rồi lấy
     `content.rendered`, hoặc dùng bản local chỉ khi chắc chắn nó vừa được đăng và chưa sửa. Đừng ghi đè bằng file local cũ.
   - Lưu ý trạng thái bài không đổi (vẫn `future` đúng giờ) sau `update_post`, kiểm bằng `list_posts`.
7. **Verify.** REST lại: số figure đúng, chữ và link không đổi, ảnh mới trả 200. Log vào `refresh-log.md`.

## Quy tắc thiết kế (đã rút từ lần chạy thật)

- **Hư cấu và ghi rõ.** Tên người, địa chỉ, giá, số liệu, quote đều bịa và có dòng chú thích trên ảnh ("Sample layout. Names, numbers and
  details are made up" hoặc "Fictional examples"). Quote testimonial bịa bắt buộc ghi là bịa (FTC). Dùng số điện thoại `555-01xx`,
  email `@example.com`, QR trỏ về `example.com`.
- **Không dùng thương hiệu thật**, không chụp màn hình trang của hãng khác (bản quyền). Brokerage trong mockup là "Cedar Hills Realty".
  Avatar dùng chữ cái đầu trong hình tròn, không dùng mặt người AI.
- **Ảnh nhà** dùng `assets/photos/ph_*.jpg` (5 ảnh Gemini, không chữ, không người). Cần thêm thì sinh bằng
  `skills/pillar-cluster-writer/scripts/generate_image.py` với prompt "no text, no people, no signs".
- **Giấy tờ in** (flyer, card, postcard) mô phỏng thật: tỷ lệ đúng (thẻ 1.75:1, postcard 3:2, flyer 8.5x11), có khu vực bưu phí/ghi
  "Postage area", có dòng môi giới và "license number as your state requires". Không bịa số giấy phép.
- **Chú thích số** (anatomy): chấm màu cam + đường kẻ (`callout()` + `leaders()`; không đặt thẻ `<b>` trong `callout`, dùng `<strong>`, vì CSS `.call b` là vòng tròn số); mỗi số khớp một mục trong danh sách của bài, theo cùng thứ tự.
- **Phông**: Inter (UI) và Lora (tiêu đề serif) qua Google Fonts. Chromium cần tin CA của proxy (mục dưới).
- **Bố cục**: nền #e4eaf4 gradient nhẹ, thẻ trắng đổ bóng, màu chủ đạo navy #1b2a4a, teal #14808a, cam #e0613a. Một thông điệp mỗi ảnh.
- **Chữ phải đọc được trên điện thoại (bắt buộc).** Xem `references/mobile-text-rules.md`. Tóm tắt: canvas rộng 1000px (không 16:9, `page(..., size=(1000, h))`), nhãn ≥ 38px,
  thân ≥ 44px, tiêu đề ≥ 60px, tối đa 6 mục chữ và 8 từ mỗi mục, bảng tối đa 3 cột x 5 hàng. Chữ "giả" trong vật mô phỏng được nhỏ nhưng không chứa thông tin cần đọc.
  Cả 59 cảnh đã dựng lại mobile-first (`s_m_*.py`, hậu tố `_m`) (13/10/2026; 6 ảnh đầu #1843 và #1832 đã được user duyệt trên điện thoại, 53 ảnh còn lại dựng theo cùng công thức); bản gen-1 ở canvas 1600x900 không đạt, đừng dùng cho bài mới. Danh mục: `references/scene-catalog.md`.

## Dựng cảnh mobile-first (công thức đã được duyệt)

Bản thử 6 ảnh (`s_m_plan.py`, `s_m_brand.py`) đạt `phone min` ≥ 12,2px và user xác nhận đọc ổn trên điện thoại. Công thức:

1. Canvas `size=(1000, cao)`, cao 1000 đến 1450 theo nội dung; lề trái/phải 50px, nội dung rộng 900px.
2. Tiêu đề 60 đến 64px đậm, đặt ở trên cùng, ghi **thông điệp** ("Where the budget goes", "Spend per closing"), không ghi nhãn chung chung.
3. Chữ thân và nhãn hàng 42 đến 44px, chữ phụ 38px, số liệu 44 đến 56px đậm. Sàn 38px; nếu muốn nhỏ hơn thì chữ đó là chữ "giả" (`.deco`, `.tag`, `.note`).
4. Một ý một ảnh, 3 đến 6 khối chữ. Dùng thanh ngang, thẻ xếp dọc, hàng "nhãn + số" thay cho bảng; bảng nhiều cột đổi thành thẻ xếp dọc hoặc ≤ 3 cột.
5. Vật mô phỏng (bảng tính, brand sheet, thẻ) vẫn nhìn thật nhưng chỉ mang 3 đến 5 dòng chữ to; phần còn lại là thanh xám.
6. Ghi chú "sample / made up" đặt trong `<figcaption>` của bài, không nhét vào ảnh; alt text mang chữ chính của ảnh.
7. Số liệu trong ảnh phải khớp bài (ví dụ ngân sách $500 và $1.500, tổng $300 vừa trong $500). Không thêm số mới.
8. Kiểm: `render()` phải in `OK`, `phone_preview.py`, rồi contact sheet. Đọc ảnh trước khi upload.
9. Bài đã đăng: lấy nội dung live qua REST, chạy `apply_mockups.py ... --mobile`, `update_post`, verify chữ/link/ảnh 200. Caption chứa dấu nháy thẳng sẽ bị WordPress đổi sang nháy cong, không phải lỗi. Alt có dấu `"` được `fig()` tự đổi thành `&quot;` (nếu không, thẻ img vỡ).

## Gotcha môi trường

- **Chromium báo `ERR_CERT_AUTHORITY_INVALID`** khi tải Google Fonts qua proxy: import CA vào NSS (không tắt kiểm tra TLS):
  `apt-get install -y libnss3-tools && certutil -d sql:$HOME/.pki/nssdb -A -t "C,," -n ccr-agent-proxy -i /root/.ccr/agent-proxy-ca.crt`.
- Playwright dùng Chromium có sẵn: `executable_path='/opt/pw-browsers/chromium'` (đã đặt trong `common.py`), không chạy `playwright install`.
- Python 3 trong container dùng `python3` thường, không `-I`, để import `common` và `segno`.
- Khi viết HTML bằng chuỗi Python: **không dùng `%` formatting trên chuỗi CSS dài kèm nhiều `%d`** (từng lỗi `not all arguments converted`);
  nối chuỗi và dùng hàm nhỏ `P(v)`. Ký tự `%` trong CSS phải thành `%%` nếu vẫn dùng `%`.
- Mỗi lần render một cảnh mất vài giây; render chọn lọc theo tên cảnh thay vì cả file khi chỉnh.

## Cấu trúc thư mục

```
mockup-images/
  SKILL.md
  scripts/
    common.py            CSS chung, render(), qr2() (QR thật bằng segno), page(), browser(), callout(), leaders()
    scenes/s_m_*.py      20 nhóm cảnh MOBILE-FIRST (59 ảnh canvas 1000px); copy một file làm mẫu khi dựng cảnh mới (s_mobile_demo.py là prototype)
    scenes/s_*.py        19 nhóm cảnh gen-1 (59 ảnh, canvas 1600x900, KHÔNG đạt chuẩn mobile, chỉ tham khảo nội dung): flyer, testimonials, listing presentation, card, logo, postcard, bio, GBP, plan, SEO, name, social, ads, pillar, brand, ideas, referral, gift, google ads, software
    sheet.py             contact sheet để xem lại
    phone_preview.py     mô phỏng ảnh trong bài trên điện thoại 360px (DPR 2) cạnh đoạn chữ 16px
    upload_staging.py    đưa ảnh lên uguu để upload_media
    apply_mockups.py     chèn/thay/xóa figure trong nội dung bài, có kiểm chữ và link
    patch_imgs.py        hàm dùng chung cho apply_mockups
  assets/photos/         5 ảnh nhà nền cho mockup
  references/
    mobile-text-rules.md quy tắc cỡ chữ cho điện thoại + nguồn
    scene-catalog.md     bảng cảnh có sẵn, đặt ở bài nào, mục nào
    spec-example.json    spec thật của đợt Cụm 9 (media URL, alt, quy tắc chèn)
```

Kết quả đợt chạy thật (ảnh, spec đã dùng) nằm trong repo của site gốc, không kèm toolkit; `references/spec-example.json` là mẫu.
