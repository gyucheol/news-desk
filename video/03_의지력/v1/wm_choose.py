# 별 자리를 두 방법으로 채운 뒤 주변과 더 잘 맞는 쪽을 고름(03편 v1, 2026-10-29).
#  R1 = 투명도 계산으로 되살린 그림(wm_remove_v3.py) + 테두리 띠 메움(wm_post.py) = photos_clean의 지금 파일
#  R2 = 원본에서 별 자리를 비워 두고 주변의 비슷한 7x7 조각을 옮겨 채움(검은 배경의 잔상, 무늬 바닥에 강함)
# 점수: 별 자리 안과 바로 바깥 고리의 평균, 흩어짐, 잔무늬 세기 차이(작을수록 주변과 같음).
# usage: wm_choose.py <orig dir> <clean dir> <cx> <cy> <width> <alpha npy>
import glob, os, sys
import numpy as np
from PIL import Image
from scipy import ndimage as ndi
from numpy.lib.stride_tricks import sliding_window_view as swv
od, cd, CX, CY, W, ap = sys.argv[1], sys.argv[2], float(sys.argv[3]), float(sys.argv[4]), int(sys.argv[5]), sys.argv[6]
s = W / 2000.0
A = np.load(ap); h, w = A.shape
x0, y0 = int(round(CX - 68 * s)), int(round(CY - 68 * s))
hole0 = ndi.binary_dilation(A > 0.01, iterations=2)
ring = ndi.binary_dilation(hole0, iterations=max(3, int(10 * s))) & ~ndi.binary_dilation(hole0, iterations=2)
SR = int(40 * s) + 6
P = 7; r = P // 2

def fill(R, hole):
    R = R.copy(); known = ~hole.copy()
    H_, W_ = hole.shape
    while (~known).any():
        front = (~known) & ndi.binary_dilation(known)
        ys, xs = np.nonzero(front)
        # fill pixels with most known neighbours first
        cnt = ndi.convolve(known.astype(int), np.ones((P, P), int), mode="constant")[ys, xs]
        order = np.argsort(-cnt)
        for y, x in zip(ys[order], xs[order]):
            if known[y, x]:
                continue
            ya, yb, xa, xb = y - r, y + r + 1, x - r, x + r + 1
            if ya < 0 or xa < 0 or yb > H_ or xb > W_:
                known[y, x] = True; continue
            tgt = R[ya:yb, xa:xb]; tm = known[ya:yb, xa:xb]
            sy0, sy1 = max(r, y - SR), min(H_ - r - 1, y + SR)
            sx0, sx1 = max(r, x - SR), min(W_ - r - 1, x + SR)
            reg = R[sy0 - r:sy1 + r + 1, sx0 - r:sx1 + r + 1]
            kreg = known[sy0 - r:sy1 + r + 1, sx0 - r:sx1 + r + 1]
            cand = swv(reg, (P, P), axis=(0, 1))          # (ny, nx, 3, P, P)
            kc = swv(kreg, (P, P), axis=(0, 1)).all(axis=(2, 3))
            d = ((cand - tgt.transpose(2, 0, 1)[None, None]) ** 2 * tm[None, None, None]).sum(axis=(2, 3, 4))
            d[~kc] = np.inf
            if not np.isfinite(d).any():
                known[y, x] = True; continue
            iy, ix = np.unravel_index(np.argmin(d), d.shape)
            R[y, x] = reg[iy + r, ix + r]
            known[y, x] = True
    return R

def score(R):
    g = R.mean(2)
    hf = g - ndi.gaussian_filter(g, 1.0)
    def st(m): return np.array([g[m].mean(), g[m].std(), hf[m].std()])
    a, b = st(hole0), st(ring)
    return float(np.abs(a - b).sum())

res = []
for cp in sorted(glob.glob(f"{cd}/in*.png")):
    im = Image.open(cp).convert("RGB")
    if im.size[0] != W:
        continue
    name = os.path.basename(cp)[:-4]
    op = glob.glob(f"{od}/{name}.*")[0]
    O = np.asarray(Image.open(op).convert("RGB"), np.float64)
    C = np.asarray(im, np.float64)
    pad = P + SR
    ya, yb, xa, xb = y0 - pad, y0 + h + pad, x0 - pad, x0 + w + pad
    big = O[ya:yb, xa:xb].copy()
    hb = np.zeros(big.shape[:2], bool); hb[pad:pad + h, pad:pad + w] = hole0
    R2 = fill(big, hb)[pad:pad + h, pad:pad + w]
    R1 = C[y0:y0 + h, x0:x0 + w]
    s1, s2 = score(R1), score(R2)
    pick = "fill" if s2 < s1 else "recover"
    if pick == "fill":
        C[y0:y0 + h, x0:x0 + w] = R2
        Image.fromarray(np.clip(C + 0.5, 0, 255).astype(np.uint8)).save(cp)
    res.append((name, round(s1, 2), round(s2, 2), pick))
    print(name, "recover", round(s1, 2), "fill", round(s2, 2), "->", pick, flush=True)
