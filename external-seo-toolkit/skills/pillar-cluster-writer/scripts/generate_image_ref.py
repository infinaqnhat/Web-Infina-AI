#!/usr/bin/env python3
"""Generate 1 image via Gemini, using 1+ reference photos + text prompt (image-to-image).

Usage: python3 generate_image_ref.py output.png "<prompt>" ref1.jpg [ref2.jpg ...]

Dung ref1/ref2... la anh that (san pham that hoac anh minh hoa loai san pham that tim duoc qua
web search) de Gemini bam sat dung hinh dang/ty le/bo cuc, thay vi doan mo theo text thuan (de bi
sai cau truc, xem SKILL.md Buoc 5.2 ly do bat buoc dung script nay thay vi generate_image.py cho
hau het truong hop).
"""
import base64
import json
import mimetypes
import os
import sys
import urllib.request
import urllib.error

MODEL = "gemini-3.1-flash-lite-image"


def main():
    if len(sys.argv) < 4:
        print("Usage: python3 generate_image_ref.py output.png \"<prompt>\" ref1.jpg [ref2.jpg ...]", file=sys.stderr)
        sys.exit(1)

    out_path, prompt = sys.argv[1], sys.argv[2]
    ref_paths = sys.argv[3:]
    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        print("Missing GEMINI_API_KEY env var", file=sys.stderr)
        sys.exit(1)

    parts = [{"text": prompt}]
    for ref_path in ref_paths:
        mime = mimetypes.guess_type(ref_path)[0] or "image/jpeg"
        with open(ref_path, "rb") as f:
            ref_b64 = base64.b64encode(f.read()).decode("ascii")
        parts.append({"inlineData": {"mimeType": mime, "data": ref_b64}})

    url = (
        f"https://generativelanguage.googleapis.com/v1beta/models/{MODEL}:generateContent"
        f"?key={api_key}"
    )
    payload = {
        "contents": [{"parts": parts}],
        "generationConfig": {"responseModalities": ["IMAGE"]},
    }
    req = urllib.request.Request(
        url,
        data=json.dumps(payload).encode("utf-8"),
        headers={"Content-Type": "application/json"},
        method="POST",
    )
    try:
        with urllib.request.urlopen(req, timeout=90) as resp:
            data = json.load(resp)
    except urllib.error.HTTPError as e:
        print(e.read().decode("utf-8"), file=sys.stderr)
        raise

    resp_parts = data["candidates"][0]["content"]["parts"]
    image_part = next(p for p in resp_parts if "inlineData" in p)
    image_bytes = base64.b64decode(image_part["inlineData"]["data"])

    with open(out_path, "wb") as f:
        f.write(image_bytes)
    print(f"Saved {out_path} ({len(image_bytes)} bytes)")


if __name__ == "__main__":
    main()
