# secrets/

Thư mục này **không chứa secret thật** trong bản toolkit gốc, chỉ là nơi dự phòng để lưu key khi
bạn tự thiết lập cho site cụ thể (xem `README.md` ở thư mục gốc để biết vì sao cần bước dự
phòng này, không chỉ dựa vào biến môi trường).

Sau khi setup, thư mục này nên có (tùy bạn dùng tính năng nào):

- `gsc-service-account.json` — Google service account key (JSON gốc, không nén 1 dòng), dùng
  cho GSC và có thể dùng chung cho GA4 nếu đã add cùng service account vào GA4 property.
- `clarity-token.txt` — token JWT của Microsoft Clarity Data Export API, chỉ 1 dòng, không có
  ký tự xuống dòng thừa ở cuối.

**Cảnh báo bắt buộc đọc trước khi commit:**

- Chỉ lưu các file này vào repo nếu repo là **private** và bạn đã cân nhắc chấp nhận rủi ro (bất
  kỳ ai có quyền đọc repo đều đọc được key).
- Không bao giờ commit key thật vào 1 repo public hoặc 1 repo sẽ được chia sẻ/fork rộng rãi.
- Nếu không muốn lưu secret trong repo, bỏ qua thư mục này, chỉ set qua biến môi trường của
  session/environment (`SEO_GSC_SA_JSON`, `SEO_CLARITY_TOKEN`, `SEO_MCP_KEY`), các script trong
  toolkit đều ưu tiên đọc biến môi trường trước, chỉ fallback đọc file trong thư mục này khi
  biến môi trường trống.
