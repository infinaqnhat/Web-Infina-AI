#!/usr/bin/env python3
"""Sinh ảnh 16:9 cho bài viết bằng Gemini, crop, rồi stage lên uguu.se.

    python3 -I gen_article_images.py spec.json

spec.json:
    [{"name": "hero", "alt": "...", "prompt": "..."}, ...]

Mỗi ảnh được ghi ra <name>.jpg trong thư mục đang chạy và in ra 1 dòng kèm URL uguu. Lấy URL
đó đưa vào `upload_media` (ảnh trong thân bài) hoặc thẳng vào `image_url` của
`update_post` (featured image, tránh tạo attachment mồ côi).

Chỉ dùng thư viện chuẩn của Python cộng Pillow. Lý do: `requests` KHÔNG có sẵn
trong container mới, và `python3 -I` bỏ qua user site-packages nên `pip install
requests` cũng không cứu được. Đoạn code dùng `requests` trong SKILL.md chỉ chạy
khi môi trường đã có sẵn nó; script này thì chạy ở mọi nơi.

API key đọc từ file `gkey` trong thư mục ĐANG CHẠY, hoặc `--key-file <path>`, hoặc
biến `GEMINI_KEY_FILE`. KHÔNG đọc từ thư mục chứa script, vì thư mục đó nằm trong repo
và key tuyệt đối không được commit. Cách chạy quen thuộc: cd sang scratchpad (nơi có
gkey) rồi gọi script bằng đường dẫn tuyệt đối.
"""
import base64, io, json, os, sys, time, uuid
import urllib.request, urllib.error
from PIL import Image

HERE = os.path.dirname(os.path.abspath(__file__))
MODEL = "gemini-3.1-flash-lite-image"
NEG = (" no extra fingers, no floating objects, no readable text on screen, "
       "no garbled letters, no mirrored text, no screen facing away from user, "
       "no logos, no brand names.")


def key():
    """Đọc key từ file NGOÀI repo. Thứ tự: --key-file, GEMINI_KEY_FILE, ./gkey trong cwd."""
    cands = []
    if "--key-file" in sys.argv:
        cands.append(sys.argv[sys.argv.index("--key-file") + 1])
    if os.environ.get("GEMINI_KEY_FILE"):
        cands.append(os.environ["GEMINI_KEY_FILE"])
    cands.append(os.path.join(os.getcwd(), "gkey"))
    for path in cands:
        if os.path.isfile(path):
            with open(path) as f:
                return f.read().strip()
    raise SystemExit("Khong tim thay file key. Dat gkey trong thu muc dang chay, hoac truyen "
                     "--key-file <path>, hoac set GEMINI_KEY_FILE. Dung de key trong repo.")


def post_json(url, payload, timeout=180):
    req = urllib.request.Request(
        url, data=json.dumps(payload).encode(),
        headers={"Content-Type": "application/json"}, method="POST")
    with urllib.request.urlopen(req, timeout=timeout) as r:
        return json.load(r)


def crop_169(raw):
    img = Image.open(io.BytesIO(raw)).convert("RGB")
    w, h = img.size
    t = 16 / 9
    if w / h < t - 0.05:
        nh = int(w / t); top = (h - nh) // 2
        img = img.crop((0, top, w, top + nh))
    elif w / h > t + 0.05:
        nw = int(h * t); left = (w - nw) // 2
        img = img.crop((left, 0, left + nw, h))
    buf = io.BytesIO()
    img.save(buf, format="JPEG", quality=92)
    return buf.getvalue(), img.size


def gemini(prompt, retries=3):
    url = ("https://generativelanguage.googleapis.com/v1beta/models/"
           f"{MODEL}:generateContent?key={key()}")
    last = None
    for a in range(retries):
        try:
            data = post_json(url, {"contents": [{"parts": [{"text": prompt}]}],
                                   "generationConfig": {"responseModalities": ["IMAGE"]}})
            for p in data["candidates"][0]["content"]["parts"]:
                if "inlineData" in p:
                    return crop_169(base64.b64decode(p["inlineData"]["data"]))
            raise RuntimeError("no inlineData in response")
        except Exception as e:
            last = e
            print(f"  retry {a+1}: {type(e).__name__}: {str(e)[:160]}", flush=True)
            time.sleep(2 * (a + 1))
    raise last


def upload_uguu(img_bytes):
    b = uuid.uuid4().hex
    body = (f"--{b}\r\n"
            'Content-Disposition: form-data; name="files[]"; filename="img.jpg"\r\n'
            "Content-Type: image/jpeg\r\n\r\n").encode() + img_bytes + f"\r\n--{b}--\r\n".encode()
    req = urllib.request.Request(
        "https://uguu.se/upload", data=body,
        headers={"Content-Type": f"multipart/form-data; boundary={b}"}, method="POST")
    with urllib.request.urlopen(req, timeout=120) as r:
        d = json.load(r)
    if not d.get("success"):
        raise RuntimeError(f"uguu failed: {d}")
    return d["files"][0]["url"]


def main():
    spec = json.load(open(sys.argv[1]))
    out = {}
    for item in spec:
        print(f"[{item['name']}] generating ...", flush=True)
        img, size = gemini(item["prompt"] + NEG)
        open(os.path.join(os.getcwd(), item["name"] + ".jpg"), "wb").write(img)
        url = upload_uguu(img)
        out[item["name"]] = {"url": url, "alt": item["alt"]}
        print(f"  {size[0]}x{size[1]}  {len(img)}B  {url}", flush=True)
    json.dump(out, open(os.path.join(os.getcwd(), "urls.json"), "w"), indent=2)


if __name__ == "__main__":
    main()
