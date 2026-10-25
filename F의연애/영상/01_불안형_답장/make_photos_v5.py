# 01편 v5 (2026-10-25): the owner's second set of AI photos (29 webp files, 2000x1116, sent in the chat in six messages
# after v4) -> numbered PNGs for the scenes (work/owner_v5/NN.png, NN = the owner's number in the script of this
# request, "<...>(NN)": 1-13 and 15-30, there is no (14); photo 27 is used twice, the script says "(27 사진 재사용)").
# The owner: "대본 중에 여러 부분을 너가 만든 ai 그림 및 스톡 영상말고, 내가 만든 ai 사진으로 대체 할꺼야. … 그리고
# 오른쪽 밑에 워터 마크 지워줘. 안지워지면 사진을 조금 확대해서 안보이게 만들어줘."
# 1. The white star mark is taken off first by scripts/owner_wm_remove.py, as in v3 (all 29 marks had the usual
#    strength, centre alpha 0.44-0.59, so every one was recovered by the formula; none needed patch filling).
#    A trace of a few levels out of 255 is left where the star was (the block pattern the owner's compressed files
#    carry around it); it shows only when the contrast is stretched a lot (credits_v5.md 4장).
# 2. Black bars: two photos carry a black strip (measured: 17 px, mean under 1/255, then an abrupt step to the picture):
#    b1_5 at the top and bottom, b4_1 at the bottom. Three more photos were flagged by the first test but are dark
#    picture areas that run on smoothly into the picture (b3_1 right edge, b4_3 left, b5_2 right) and are kept.
# 3. Each number is matched to its file by what the photo shows against the line it is marked on (the files carry no
#    number). Inside each message the order was not the number order (as in v3): message 1 came as 5 1 2 3 4,
#    message 2 as 10 6 7 8 9, message 3 as 15 16 11 12 13, message 4 as 21 17 18 19 20, message 5 as 26 22 23 24 25,
#    message 6 as 29 27 28 30. What each photo shows is listed in credits_v5.md 3장.
# The owner's photos are not committed (rights stay with the owner).
# usage: make_photos_v5.py <dir of cleaned PNGs> <out dir>
import glob, os, sys
import numpy as np
from PIL import Image

src, dst = sys.argv[1], sys.argv[2]
os.makedirs(dst, exist_ok=True)
NUM = {1: "b1_2", 2: "b1_3", 3: "b1_4", 4: "b1_5", 5: "b1_1",
       6: "b2_2", 7: "b2_3", 8: "b2_4", 9: "b2_5", 10: "b2_1",
       11: "b3_3", 12: "b3_4", 13: "b3_5", 15: "b3_1", 16: "b3_2",
       17: "b4_2", 18: "b4_3", 19: "b4_4", 20: "b4_5", 21: "b4_1",
       22: "b5_2", 23: "b5_3", 24: "b5_4", 25: "b5_5", 26: "b5_1",
       27: "b6_2", 28: "b6_3", 29: "b6_1", 30: "b6_4"}
BARS = {"b1_5": (18, 18), "b4_1": (0, 18)}      # (top, bottom) px cut, 1 px more than measured
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
