# Download card thumbnails for given Mixkit ids and tile them with id labels (for choosing by eye).
# usage: thumbsheet.py index.json out.png id1,id2,...
import json, sys, os, subprocess, time
from PIL import Image, ImageDraw, ImageFont
idx = {v["id"]: v for v in json.load(open(sys.argv[1]))}
out, ids = sys.argv[2], sys.argv[3].split(",")
ROOT = os.environ.get("VIDEO_ROOT", os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
td = f"{ROOT}/work/stock/thumbs"; os.makedirs(td, exist_ok=True)
font = ImageFont.truetype(f"{ROOT}/fonts/Pretendard-Bold.otf", 22)
tw, th, cols = 400, 225, 4
rows = (len(ids) + cols - 1) // cols
sheet = Image.new("RGB", (cols * tw, rows * (th + 52)), (35, 35, 35))
for i, vid in enumerate(ids):
    v = idx[vid]; p = f"{td}/{vid}.jpg"
    if not os.path.exists(p):
        subprocess.run(["curl", "-s", "-m", "30", "-A", "Mozilla/5.0", "-o", p, v["thumb"]], check=False); time.sleep(0.3)
    try:
        im = Image.open(p).convert("RGB")
        im = im.resize((tw, round(im.height * tw / im.width)))
        im = im.crop((0, max(0, (im.height - th) // 2), tw, max(0, (im.height - th) // 2) + th))
    except Exception:
        im = Image.new("RGB", (tw, th), (90, 0, 0))
    x, y = (i % cols) * tw, (i // cols) * (th + 52)
    sheet.paste(im, (x, y + 52))
    d = ImageDraw.Draw(sheet)
    d.text((x + 6, y + 2), vid, font=font, fill=(255, 215, 80))
    d.text((x + 6, y + 26), v["title"][:34], font=ImageFont.truetype(f"{ROOT}/fonts/Pretendard-Medium.otf", 17), fill=(230, 230, 230))
sheet.save(out); print(out)
