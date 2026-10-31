# 썸네일용 사용자 AI 그림 2장(2752x1536)의 오른쪽 아래 별 표시 지우기 (2026-10-31).
# 별은 흰색(255)을 일정한 불투명도로 덮은 것으로 보고(채널마다 같은 값: 그림1 0.495~0.500, 그림2 0.516),
# 두 그림에서 같은 자리·같은 모양이므로 두 그림의 추정 불투명도 지도를 평균해 모양을 만들고(상관 0.997),
# 그림마다 세기를 맞춘 뒤 거꾸로 섞어 별 밑의 원래 바닥 무늬를 되살립니다: 원래 = (보이는 값 - a*255) / (1 - a).
# usage: wm_fix2752.py in.png out.png [in2.png out2.png ...]
import sys
import numpy as np
from PIL import Image
from scipy import ndimage as ndi
CX, CY = 2640.1, 1423.3
x0, y0, x1, y1 = 2540, 1324, 2740, 1524
yy, xx = np.mgrid[y0:y1, x0:x1]; rr = np.hypot(xx - CX, yy - CY)
ring = (rr > 60) & (rr < 92)


def surface(O):
    X = np.stack([np.ones(ring.sum()), xx[ring] - CX, yy[ring] - CY, (xx[ring] - CX) ** 2, (yy[ring] - CY) ** 2, (xx[ring] - CX) * (yy[ring] - CY)], 1)
    Xa = np.stack([np.ones(xx.size), (xx - CX).ravel(), (yy - CY).ravel(), ((xx - CX) ** 2).ravel(), ((yy - CY) ** 2).ravel(), ((xx - CX) * (yy - CY)).ravel()], 1)
    B = np.zeros(O.shape)
    for c in range(3):
        coef, *_ = np.linalg.lstsq(X, O[..., c][ring], rcond=None); B[..., c] = (Xa @ coef).reshape(xx.shape)
    return B


pairs = list(zip(sys.argv[1::2], sys.argv[2::2]))
imgs = [np.asarray(Image.open(a).convert('RGB'), np.float64) for a, _ in pairs]
est = []
for im in imgs:
    O = im[y0:y1, x0:x1]; B = surface(O)
    est.append(((O - B) / np.clip(255 - B, 1, None)).mean(2))
inner = rr < 18
shape = np.mean([e / np.median(e[inner]) for e in est], 0)       # 1.0 inside the star, fractional on its edge
shape[rr > 52] = 0
shape = np.clip(shape, 0, 1.05)
shape[shape < 0.03] = 0
# 세기: 별 안쪽을 되살린 밝기가 바로 바깥(별 끝에서 2~14 px, 오른쪽에 물건이 있는 쪽은 뺌)과 같아지는 값(0.002 간격)
near = (rr > 50) & (rr < 62) & (xx < CX + 30)
starm = shape > 0.5
for (a, b), im, e in zip(pairs, imgs, est):
    O = im[y0:y1, x0:x1]
    target = O[near].mean()
    best = None
    for amp in np.arange(0.44, 0.58, 0.002):
        A = np.clip(shape * amp, 0, 0.95)[..., None]
        R = (O - 255 * A) / (1 - A)
        d = abs(R[starm].mean() - target)
        if best is None or d < best[0]:
            best = (d, amp)
    amp = float(best[1])
    A = np.clip(shape * amp, 0, 0.95)[..., None]
    R = (O - 255 * A) / (1 - A)
    out = im.copy(); out[y0:y1, x0:x1] = np.clip(R, 0, 255)
    Image.fromarray((out + 0.5).astype(np.uint8)).save(b)
    star = starm; ringm = near
    print(a, '-> ', b, '| strength %.3f' % amp, '| inside mean', R[star].mean(0).round(1), 'around', O[ringm].mean(0).round(1),
          '| inside std %.1f around std %.1f' % (R[star].std(), O[ringm].std()))
