"""Assemble the demo GIF from frames recorded by scripts/record_demo_frames.js.

Usage:  python3 -I scripts/make_demo_gif.py build/frames assets/rw-demo-buyer.gif
The first GIF frame is the "answered" state on purpose: some email clients (Outlook desktop)
show only the first frame. (frame index, duration ms) pairs below match the original recording.
"""
import glob, sys
from PIL import Image

frames_dir, out = sys.argv[1], sys.argv[2]
fs = sorted(glob.glob(f"{frames_dir}/f*.png"))
seq = [(15, 1400), (0, 1300), (4, 700), (5, 700), (9, 900), (15, 2200), (21, 1600), (24, 800), (27, 900), (30, 2600), (38, 3200)]
box = (320, 0, 1260, 800); W = 800; H = round(800 * W / 940)
imgs = [(Image.open(fs[i]).convert("RGB").crop(box).resize((W, H), Image.LANCZOS), d) for i, d in seq]
mosaic = Image.new("RGB", (W, H * len(imgs)))
for k, (im, _) in enumerate(imgs):
    mosaic.paste(im, (0, k * H))
pal = mosaic.quantize(colors=256, method=Image.MEDIANCUT, dither=Image.NONE)
frames = [im.quantize(palette=pal, dither=Image.NONE) for im, _ in imgs]
frames[0].save(out, save_all=True, append_images=frames[1:], duration=[d for _, d in imgs], loop=0, optimize=True, disposal=1)
print("wrote", out)
