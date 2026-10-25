# 01편 v7 (2026-10-25, the owner's v7 list 10): photo 7 of the owner's first set (지우 holding the phone on the subway,
# work/owner_v3/07.png from make_photos_v3.py) with the words typed in the chat's input box softened. The owner, at
# '지우가 줄어들지 않는 숫자 1을 보며 밤새 카톡창을 들락날락하고': "휴대폰 대화창에 어떤 말을 입력해놨는데 그게 약간 ai티가
# 많이 나. 그거를 약간 뿌옇게 처리해주라."
# Seen at full size: the input box holds two rows of made-up Hangul (x 921-1009, y 552-594 in the 1984 x 1116 photo)
# and the yellow send button reads as a garbled '보내기' (x 1054-1079, y 592-608); both are softened. The chat bubbles
# above are already out of focus in the photo and stay as they are.
# How: text pixels = darker than the box's own white by more than 16 levels (median of 15 x 15 px around); the glyphs
# inside the two areas above, grown by 4 px and feathered (gaussian 2 px), take a gaussian-blurred copy of the photo
# (sigma 2 px: the rows stay as soft grey lines, as out of focus as the bubbles, and no letter can be read).
# The owner's photos are not committed (rights stay with the owner).
# usage: make_photos_v7.py <work/owner_v3/07.png> <out png>
import sys
import numpy as np
from PIL import Image, ImageFilter
from scipy import ndimage as nd

src, dst = sys.argv[1], sys.argv[2]
im = Image.open(src).convert("RGB")
assert im.size == (1984, 1116), im.size
a = np.asarray(im, np.float32)
lum = a @ np.array([0.2126, 0.7152, 0.0722], np.float32)
X0, Y0, X1, Y1 = 880, 520, 1110, 640                      # the input bar of the chat
AREAS = [(905, 540, 1030, 600), (1050, 588, 1085, 612)]     # the typed rows, the send button's word
sub = lum[Y0:Y1, X0:X1]
bg = nd.median_filter(sub, size=15)
glyph = (bg - sub > 16) & (bg > 170)
lab, n = nd.label(nd.binary_dilation(glyph, iterations=2))
m = np.zeros(lum.shape, bool)
picked = []
for i, s in enumerate(nd.find_objects(lab)):
    ys, xs = s
    cx, cy = X0 + (xs.start + xs.stop) / 2, Y0 + (ys.start + ys.stop) / 2
    if any(x0 <= cx <= x1 and y0 <= cy <= y1 for x0, y0, x1, y1 in AREAS):
        m[Y0:Y1, X0:X1] |= lab == i + 1
        picked.append((X0 + xs.start, Y0 + ys.start, X0 + xs.stop, Y0 + ys.stop, int((lab[s] == i + 1).sum())))
assert len(picked) == 3, picked                            # row 1, row 2, the button's word
alpha = nd.gaussian_filter(nd.binary_dilation(m, iterations=4).astype(np.float32), 2.0)[..., None]
soft = np.asarray(im.filter(ImageFilter.GaussianBlur(2)), np.float32)
out = a * (1 - alpha) + soft * alpha
Image.fromarray(np.clip(out + 0.5, 0, 255).astype(np.uint8)).save(dst)
print(dst, "softened:", picked)
