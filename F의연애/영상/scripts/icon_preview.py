# Preview F의 연애 icon screens: renders one kind at several moments into a contact sheet (for checking by eye).
# usage: icon_preview.py out.png module kind "t1,t2,..." [dur] ['{"json": "args"}'] ['[at1, at2]']
# FY_FONT=pretendard (or another fy_common.FAMILIES key) renders the lettering in another font for comparison.
import json, os, sys, importlib
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from PIL import Image, ImageDraw
out, mod, kind, ts = sys.argv[1], sys.argv[2], sys.argv[3], [float(x) for x in sys.argv[4].split(",")]
dur = float(sys.argv[5]) if len(sys.argv) > 5 else 4.0
args = json.loads(sys.argv[6]) if len(sys.argv) > 6 else {}
at = json.loads(sys.argv[7]) if len(sys.argv) > 7 else []
fn = importlib.import_module(mod).KINDS[kind]
tiles = [fn(t, dur, args, at) for t in ts]
cols = min(3, len(tiles)); rows = (len(tiles) + cols - 1) // cols
tw, th = 960, 540
sheet = Image.new("RGB", (cols * tw, rows * (th + 30)), (40, 40, 40))
d = ImageDraw.Draw(sheet)
for i, im in enumerate(tiles):
    x, y = (i % cols) * tw, (i // cols) * (th + 30)
    sheet.paste(im.resize((tw, th), Image.LANCZOS), (x, y + 30))
    d.text((x + 8, y + 6), f"{kind}  t={ts[i]:.2f}s", fill=(255, 215, 80))
    # guides: bottom subtitle box zone (y 918-1002 px of 1080) in red; drawing limits (y 860, x 120 / 1800) in blue
    d.rectangle([x, y + 30 + round(918 * th / 1080), x + tw - 1, y + 30 + round(1002 * th / 1080)], outline=(200, 40, 40))
    d.line([(x, y + 30 + round(860 * th / 1080)), (x + tw - 1, y + 30 + round(860 * th / 1080))], fill=(70, 70, 190))
    for gx in (120, 1800):
        d.line([(x + round(gx * tw / 1920), y + 30), (x + round(gx * tw / 1920), y + 30 + th - 1)], fill=(70, 70, 190))
sheet.save(out); print(out)
