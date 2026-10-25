# 01편 v3 (2026-10-25): the owner's own AI photos (29 files, sent in the chat as webp, 2000x1116) -> numbered PNGs for
# the scenes (work/owner_v3/NN.png, NN = the owner's number in the script, "<...>(NN)"), plus the two extra pictures of
# the brain explainer (photo 4).
# 1. The white star mark at the bottom right is taken off first by scripts/owner_wm_remove.py (in: the webp files, out:
#    the same names as PNG). The owner: "오른쪽 밑에 워터 마크 지워줘. 안지워지면 사진을 조금 확대해서 안보이게".
# 2. Black bars: three photos carry a black strip at the top (and bottom) edge (measured: rows darker than 6/255 with
#    almost no variation, 16-17 px). They are cut off here so the frame is filled by the picture.
# 3. Each number is matched to its file by what the photo shows against the line it is marked on (the files carry no
#    number; the owner sent them in six messages, 1-5, 6-10, 11-15, 16-20, 21-25, 27-30). No photo 26 was sent and the
#    script uses (23) twice, so "입원 첫날" shows photo 23 again. Photo 16 has no line in the script and is not used.
# 4. Photo 4 (brain): brain_red.png is the same picture with the brain tinted red and a soft red light around it
#    (render.py fades it in at "위협적으로"); the brain is found by its brightness (pale brain on a dark blue room).
# The owner's photos are not committed (rights stay with the owner).
# usage: make_photos_v3.py <dir of cleaned PNGs> <out dir>
import glob, os, sys
import numpy as np
from PIL import Image, ImageFilter

src, dst = sys.argv[1], sys.argv[2]
os.makedirs(dst, exist_ok=True)
NUM = {1: "b1_2", 2: "b1_3", 3: "b1_4", 4: "b1_5", 5: "b1_1",
       6: "b2_2", 7: "b2_3", 8: "b2_4", 9: "b2_5", 10: "b2_1",
       11: "b3_1", 12: "b3_2", 13: "b3_3", 14: "b3_4", 15: "b3_5",
       16: "b4_2", 17: "b4_3", 18: "b4_4", 19: "b4_5", 20: "b4_1",
       21: "b5_5", 22: "b5_1", 23: "b5_2", 24: "b5_3", 25: "b5_4",
       27: "b6_1", 28: "b6_2", 29: "b6_3", 30: "b6_4"}
BARS = {"b1_1": (18, 0), "b6_1": (18, 17), "b6_2": (18, 17)}      # (top, bottom) px cut, 1 px more than measured
for n, key in sorted(NUM.items()):
    p = glob.glob(f"{src}/{key}_*.png")
    assert len(p) == 1, (n, key, p)
    im = Image.open(p[0]).convert("RGB")
    t, b = BARS.get(key, (0, 0))
    a = np.asarray(im, np.float64)
    if t:
        assert a[:t - 1].mean() < 3 and a[:t - 1].std() < 3, (key, "top bar not black")
    if b:
        assert a[-(b - 1):].mean() < 3 and a[-(b - 1):].std() < 3, (key, "bottom bar not black")
    im = im.crop((0, t, im.width, im.height - b))
    w, h = im.size                                   # 16:9 from the middle (render.py would do the same)
    tw, th = (w, round(w * 9 / 16)) if round(w * 9 / 16) <= h else (round(h * 16 / 9), h)
    x0, y0 = (w - tw) // 2, (h - th) // 2
    im = im.crop((x0, y0, x0 + tw, y0 + th))
    im.save(f"{dst}/{n:02d}.png")
    print(f"{n:02d} <- {os.path.basename(p[0])}, {im.size[0]}x{im.size[1]}")

# brain explainer: red version of photo 4
im = Image.open(f"{dst}/04.png").convert("RGB")
a = np.asarray(im, np.float32) / 255
lum = a @ np.array([0.2126, 0.7152, 0.0722], np.float32)
m = np.clip((lum - 0.24) / 0.22, 0, 1)               # brain (lum 0.45-0.95) vs room and plinth (below 0.24)
mi = Image.fromarray((m * 255).astype(np.uint8)).filter(ImageFilter.GaussianBlur(1.5))
m = np.asarray(mi, np.float32)[..., None] / 255
red = np.array([0.93, 0.16, 0.14], np.float32)
tint = lum[..., None] * red * 1.2                     # the brain's own light and shade, in red
out = a * (1 - 0.75 * m) + tint * 0.75 * m
glow = np.asarray(mi.filter(ImageFilter.GaussianBlur(60)), np.float32)[..., None] / 255
out = out + (1 - m) * glow * red * 0.42               # red light falling on the room around it
Image.fromarray((np.clip(out, 0, 1) * 255 + 0.5).astype(np.uint8)).save(f"{dst}/04_red.png")
print("04_red.png")
