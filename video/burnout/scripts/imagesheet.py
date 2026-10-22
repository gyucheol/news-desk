# Tile candidate images with numbers (1, 2, 3...) for the owner's review (send with SendUserFile).
# usage: imagesheet.py out.png img1.png img2.png ... [--cols 3] [--title "장면 002 알람 끄는 손"]
import os, sys
from PIL import Image, ImageDraw, ImageFont

ROOT = os.environ.get("VIDEO_ROOT", os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
a = sys.argv[1:]
cols = int(a[a.index("--cols") + 1]) if "--cols" in a else 3
title = a[a.index("--title") + 1] if "--title" in a else ""
files = [x for i, x in enumerate(a[1:], 1) if not x.startswith("--") and a[i - 1] not in ("--cols", "--title")]
out = a[0]
fb = ImageFont.truetype(f"{ROOT}/fonts/Pretendard-Bold.otf", 34)
fm = ImageFont.truetype(f"{ROOT}/fonts/Pretendard-Medium.otf", 22)
tw, th, top = 640, 360, (60 if title else 0)
rows = (len(files) + cols - 1) // cols
sheet = Image.new("RGB", (cols * tw, top + rows * (th + 40)), (30, 30, 30))
d = ImageDraw.Draw(sheet)
if title:
    d.text((14, 12), title, font=fb, fill=(255, 255, 255))
for i, f in enumerate(files):
    im = Image.open(f).convert("RGB")
    im = im.resize((tw, round(im.height * tw / im.width)))
    y0 = max(0, (im.height - th) // 2)
    im = im.crop((0, y0, tw, y0 + th))
    x, y = (i % cols) * tw, top + (i // cols) * (th + 40)
    sheet.paste(im, (x, y + 40))
    d.text((x + 10, y + 4), f"{i + 1}", font=fb, fill=(255, 215, 80))
    d.text((x + 52, y + 12), os.path.basename(f)[:40], font=fm, fill=(200, 200, 200))
sheet.save(out); print(out)
