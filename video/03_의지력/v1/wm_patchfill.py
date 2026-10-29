# 무늬가 있는 바닥 위의 별(62번 입력 = 사용자 사진 61번)은 비슷한 무늬 조각을 옮겨 채움(owner_wm_remove.py의 patch_fill).
# usage: wm_patchfill.py <original> <clean png to overwrite> <cx> <cy> <width> <alpha npy>
import sys
import numpy as np
from PIL import Image
from scipy import ndimage as ndi
orig, outp, CX, CY, W, ap = sys.argv[1], sys.argv[2], float(sys.argv[3]), float(sys.argv[4]), int(sys.argv[5]), sys.argv[6]
s = W / 2000.0
A = np.load(ap); h, w = A.shape
x0, y0 = int(round(CX - 68 * s)), int(round(CY - 68 * s))
img = np.asarray(Image.open(orig).convert("RGB"), np.float64)
R = img[y0:y0 + h, x0:x0 + w].copy()
hole = ndi.binary_dilation(A > 0.01, iterations=2)

def patch_fill(R, hole, psz=7, search=36):
    R = R.copy(); known = ~hole.copy(); r = psz // 2
    Hh, Ww = hole.shape
    while (~known).any():
        edge = (~known) & ndi.binary_dilation(known)
        ys, xs = np.nonzero(edge)
        for y, x in zip(ys, xs):
            ya, yb, xa, xb = max(y - r, 0), min(y + r + 1, Hh), max(x - r, 0), min(x + r + 1, Ww)
            tgt = R[ya:yb, xa:xb]; tm = known[ya:yb, xa:xb]
            best, bv = None, None
            for sy in range(max(r, y - search), min(Hh - r, y + search)):
                for sx in range(max(r, x - search), min(Ww - r, x + search)):
                    ck = known[sy - (y - ya):sy + (yb - y), sx - (x - xa):sx + (xb - x)]
                    if ck.shape != tm.shape or not ck.all():
                        continue
                    cand = R[sy - (y - ya):sy + (yb - y), sx - (x - xa):sx + (xb - x)]
                    v = np.sum(((cand - tgt) ** 2)[tm])
                    if bv is None or v < bv:
                        bv, best = v, (sy, sx)
            if best is not None:
                R[y, x] = R[best[0], best[1]]
            known[y, x] = True
    return R

F = patch_fill(R, hole)
clean = np.asarray(Image.open(outp).convert("RGB"), np.float64)
clean[y0:y0 + h, x0:x0 + w] = F
Image.fromarray(np.clip(clean + 0.5, 0, 255).astype(np.uint8)).save(outp)
print("filled", int(hole.sum()), "px")
