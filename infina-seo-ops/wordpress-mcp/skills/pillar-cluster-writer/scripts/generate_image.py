#!/usr/bin/env python3
"""Generate 1 anh qua Gemini (Nano Banana 2 Lite) cho slide TikTok carousel.

Dung bien moi truong GEMINI_API_KEY (khong hardcode key vao file/script nay).

Usage:
    python3 generate_image.py "<prompt tieng Anh, mo ta chi tiet>" output.png
"""
import base64
import json
import os
import sys
import urllib.request

MODEL = "gemini-3.1-flash-lite-image"
API_URL = f"https://generativelanguage.googleapis.com/v1beta/models/{MODEL}:generateContent"


def generate_image(prompt: str, output_path: str) -> None:
    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        print("Loi: chua co bien moi truong GEMINI_API_KEY.", file=sys.stderr)
        sys.exit(1)

    payload = json.dumps({"contents": [{"parts": [{"text": prompt}]}]}).encode()
    req = urllib.request.Request(
        f"{API_URL}?key={api_key}",
        data=payload,
        headers={"Content-Type": "application/json"},
        method="POST",
    )
    with urllib.request.urlopen(req, timeout=60) as resp:
        data = json.load(resp)

    parts = data["candidates"][0]["content"]["parts"]
    for part in parts:
        if "inlineData" in part:
            img_bytes = base64.b64decode(part["inlineData"]["data"])
            with open(output_path, "wb") as f:
                f.write(img_bytes)
            print(f"Da luu {output_path} ({len(img_bytes)} bytes, mime={part['inlineData']['mimeType']})")
            return

    print("Loi: response khong co anh (co the bi tu choi vi noi dung nhay cam).", file=sys.stderr)
    sys.exit(1)


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python3 generate_image.py \"<prompt>\" output.png", file=sys.stderr)
        sys.exit(1)
    generate_image(sys.argv[1], sys.argv[2])
