# Take the white 4-point star mark off the bottom right of the owner's AI photos (F의 연애 01 v3, 2026-10-25: "오른쪽 밑에
# 워터 마크 지워줘. 안지워지면 사진을 조금 확대해서 안보이게 만들어줘"). The mark sits at the same place and size in all
# 29 photos (2000x1116, centre about (1918, 1034), tips about 36 px out), white blended over the picture:
#   O = (1 - a_k) B + 255 a_k,   a_k = 1 - (1 - a)^k
# a = the mark's alpha map, measured as the median over the 12 photos whose background around the mark is flattest
# (B there from a quadratic surface fitted to a ring just outside the star); k = how strongly the mark was put on in
# that photo (photos edited again in the generator carry a more opaque mark).
# Per photo:
# - normal mark (centre alpha about 0.5): k is the value in 0.8..1.4 that makes the star's outline vanish (energy of
#   the gradient across the outline in the recovered picture), then B = (O - 255 a_k) / (1 - a_k) exactly;
# - strong mark (centre alpha above 0.68: 4 photos, 0.75-0.93): too little of the picture is left under it, so the star
#   is filled from the picture around it by copying the best-matching 7x7 patches, from the outside in;
# - then a 3x3 median on a thin band along the outline (compression ringing), and each outline pixel is held within the
#   range of its nearest inside and outside values (a 1-2 px line seen at 3x on flat walls).
# Checked by eye on before/after sheets of all 29 corners at 2x and 3x (the sheet this writes).
# usage: owner_wm_remove.py <dir of the owner's webp files> <alpha_out.npy> <out dir> <sheet.png>
import glob, os, sys
import numpy as np
from PIL import Image
from scipy import ndimage as ndi

src, ap, dst, sheet_p = sys.argv[1:5]
os.makedirs(dst, exist_ok=True)
x0, x1_, y0, y1_ = 1850, 1990, 966, 1106
h, w = y1_ - y0, x1_ - x0
yy, xx = np.mgrid[y0:y1_, x0:x1_]
cx, cy = 1918.0, 1034.0
rr = np.hypot(xx - cx, yy - cy)
ring = (rr > 52) & (rr < 68)


def surface(O):
    X = np.stack([np.ones(ring.sum()), xx[ring] - cx, yy[ring] - cy, (xx[ring] - cx) ** 2, (yy[ring] - cy) ** 2,
                  (xx[ring] - cx) * (yy[ring] - cy)], 1)
    Xa = np.stack([np.ones(xx.size), (xx - cx).ravel(), (yy - cy).ravel(), ((xx - cx) ** 2).ravel(),
                   ((yy - cy) ** 2).ravel(), ((xx - cx) * (yy - cy)).ravel()], 1)
    B = np.zeros(O.shape); res = []
    for c in range(3):
        coef, *_ = np.linalg.lstsq(X, O[..., c][ring], rcond=None)
        B[..., c] = (Xa @ coef).reshape(xx.shape); res.append(np.std(O[..., c][ring] - X @ coef))
    return B, float(np.mean(res))


_ims = {os.path.basename(p): np.asarray(Image.open(p).convert("RGB"), np.float64) for p in sorted(glob.glob(f"{src}/*.webp"))}
_est = []
for _n, _img in _ims.items():
    _O = _img[y0:y1_, x0:x1_]; _B, _rs = surface(_O)
    _est.append((_rs, ((_O - _B) / np.clip(255 - _B, 1, None)).mean(2)))
_est.sort(key=lambda t: t[0])
A = np.median(np.stack([a for _, a in _est[:12]]), 0)
A[rr >= 46] = 0
A = np.clip(A, 0, 0.97)
A[A < 0.015] = 0
np.save(ap, A)
gy, gx = np.gradient(ndi.gaussian_filter(A, 0.7))
gm = np.hypot(gx, gy)
band = gm > 0.25 * gm.max()                      # the star's outline
nx, ny = gx / (gm + 1e-9), gy / (gm + 1e-9)
starm = ndi.binary_dilation(A > 0.01, iterations=2)


def recover(O, k):
    ak = (1 - (1 - A) ** k)[..., None]
    return (O - 255 * ak) / np.clip(1 - ak, 0.05, None), ak[..., 0]


def outline_energy(R, ak):
    g = R.mean(2)
    dy, dx = np.gradient(g)
    d = dx * nx + dy * ny
    m = band & (ak < 0.9)
    return float(np.mean(d[m] ** 2)) if m.any() else 1e18


def patch_fill(R, hole, psz=7, search=40, rng=None):
    """Fill `hole` pixels of R (h, w, 3) by copying the best-matching known patch, onion-peel order."""
    R = R.copy(); known = ~hole.copy(); r = psz // 2
    Hh, Ww = hole.shape
    while (~known).any():
        edge = (~known) & ndi.binary_dilation(known)
        ys, xs = np.nonzero(edge)
        for y, x in zip(ys, xs):
            ya, yb, xa, xb = max(y - r, 0), min(y + r + 1, Hh), max(x - r, 0), min(x + r + 1, Ww)
            tgt = R[ya:yb, xa:xb]; tm = known[ya:yb, xa:xb]
            best, bv = None, None
            for sy in range(max(r, y - search), min(Hh - r, y + search), 2):
                for sx in range(max(r, x - search), min(Ww - r, x + search), 2):
                    cand_known = known[sy - (y - ya):sy + (yb - y), sx - (x - xa):sx + (xb - x)]
                    if cand_known.shape != tm.shape or not cand_known.all():
                        continue
                    cand = R[sy - (y - ya):sy + (yb - y), sx - (x - xa):sx + (xb - x)]
                    v = np.sum(((cand - tgt) ** 2)[tm])
                    if bv is None or v < bv:
                        bv, best = v, (sy, sx)
            if best is not None:
                R[y, x] = R[best[0], best[1]]
            known[y, x] = True
    return R


inside = ndi.binary_erosion(A >= 0.45, iterations=1)
outside = ~ndi.binary_dilation(A > 0, iterations=1)
edge = ndi.binary_dilation(A > 0, iterations=2) & ~inside
d_in, i_in = ndi.distance_transform_edt(~inside, return_indices=True)
d_out, i_out = ndi.distance_transform_edt(~outside, return_indices=True)


def side_mean(R, m, s=1.2):
    """Average of R over mask m near each pixel (normalised Gaussian), so one noisy pixel does not set the range."""
    wgt = ndi.gaussian_filter(m.astype(float), s)
    return np.stack([ndi.gaussian_filter(R[..., c] * m, s) / np.clip(wgt, 1e-6, None) for c in range(3)], 2)


def edge_clamp(R, t=2.0):
    vin = side_mean(R, inside)[i_in[0], i_in[1]]
    vout = side_mean(R, outside)[i_out[0], i_out[1]]
    lo, hi = np.minimum(vin, vout) - t, np.maximum(vin, vout) + t
    out = R.copy()
    out[edge] = np.clip(R[edge], lo[edge], hi[edge])
    return out


files = sorted(glob.glob(f"{src}/*.webp"))
tiles = []
for p in files:
    name = os.path.basename(p)
    img = np.asarray(Image.open(p).convert("RGB"), np.float64)
    O = img[y0:y0 + h, x0:x0 + w]
    B, _ = surface(O)
    core = A > 0.4
    a_obs = float(np.median(((O - B) / np.clip(255 - B, 1, None)).mean(2)[core]))
    if a_obs > 0.68:                             # the mark was put on several times: no picture left under it
        k, E = float("nan"), [0.0]
        hole = starm.copy()
        R = patch_fill(O.copy(), ndi.binary_dilation(hole, iterations=2))
    else:
        ks = np.arange(0.8, 1.41, 0.02)
        E = [outline_energy(*recover(O, k)) for k in ks]
        k = float(ks[int(np.argmin(E))])
        R, ak = recover(O, k)
        hole = np.zeros_like(starm)
    # soften compression ringing along the outline only
    med = np.stack([ndi.median_filter(R[..., c], size=3) for c in range(3)], 2)
    bm = ndi.binary_dilation(band, iterations=1)[..., None]
    R = np.where(bm, 0.5 * R + 0.5 * med, R)
    R = np.clip(edge_clamp(R), 0, 255)
    full = img.copy(); full[y0:y0 + h, x0:x0 + w] = R
    Image.fromarray((full + 0.5).astype(np.uint8)).save(f"{dst}/{os.path.splitext(name)[0]}.png")
    print(f"{name}: centre alpha {a_obs:.2f}, k {k:.2f}, filled {int(hole.sum())} px")
    tiles.append((O, R))
T = 280
sheet = Image.new("RGB", (8 * T, ((len(tiles) + 3) // 4) * T), (40, 40, 40))
for i, (O, R) in enumerate(tiles):
    a = Image.fromarray(O.astype(np.uint8)).resize((T, T), Image.NEAREST)
    b = Image.fromarray((R + 0.5).astype(np.uint8)).resize((T, T), Image.NEAREST)
    sheet.paste(a, ((i % 4) * 2 * T, (i // 4) * T)); sheet.paste(b, ((i % 4) * 2 * T + T, (i // 4) * T))
sheet.save(sheet_p)
print(sheet_p)
