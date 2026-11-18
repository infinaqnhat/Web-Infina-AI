#!/usr/bin/env python3
"""So sanh do giong nhau giua 2 anh bang average hash (aHash), dung Pillow (co san).

Dung truoc khi chon anh moi chen vao bai da co san anh khac (vd anh dai dien), de tranh
chon nham 1 anh key art/press photo bi nhieu bao dung lai giong het nhau.

Usage:
    python3 check_image_similarity.py anh_cu.jpg anh_moi.jpg

Ket qua in ra Hamming distance tren tong 64 bit:
    0-5   : gan nhu chac chan cung 1 anh (chi khac crop/resize/nen), KHONG nen dung ca 2
    6-15  : kha giong nhau (cung chu de/bo cuc), can nhac doi anh khac neu muon da dang
    >15   : du khac biet de dung song song trong cung 1 bai
"""
import sys
from PIL import Image


def ahash(path, size=8):
    img = Image.open(path).convert("L").resize((size, size), Image.LANCZOS)
    pixels = list(img.getdata())
    avg = sum(pixels) / len(pixels)
    return "".join("1" if p > avg else "0" for p in pixels)


def hamming(a, b):
    return sum(c1 != c2 for c1, c2 in zip(a, b))


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python3 check_image_similarity.py <anh_1> <anh_2>", file=sys.stderr)
        sys.exit(1)

    h1 = ahash(sys.argv[1])
    h2 = ahash(sys.argv[2])
    dist = hamming(h1, h2)

    if dist <= 5:
        verdict = "TRUNG NHAU (khong nen dung ca 2 trong cung 1 bai)"
    elif dist <= 15:
        verdict = "KHA GIONG (can nhac doi anh khac)"
    else:
        verdict = "DU KHAC BIET"

    print(f"Hamming distance: {dist}/64 -> {verdict}")
