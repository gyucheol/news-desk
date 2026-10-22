# Paper-collage assets for the F의 연애 sample v3: same paper look as v2, but crisp solid ink and
# text drawn at (or above) its on-screen size. Fonts are read from ~/.fonts/ using the file names in FONTS.
# Usage: python3 assets3.py <out_dir> <raw_potato_png_dir> <cc0_texture_dir>
import json, math, os, sys
import numpy as np
from PIL import Image, ImageDraw, ImageFont, ImageFilter, ImageChops

OUT, RAW = sys.argv[1], sys.argv[2]
os.makedirs(OUT, exist_ok=True)
F = os.path.expanduser('~/.fonts/')
FONTS = {
    'song': '1cX2aUDWAJH5-EIC7DIhr1E.ttf', 'bhs': 'ea8Aad44WunzF9a-dL6toA8r8nqV.ttf',
    'codeB': '8QIYdjzHisX_8vv59_xMxtPFW4IXROws8xgecsU.ttf', 'code': '8QIVdjzHisX_8vv59_xMxtPFW4IXROwsy6Q.ttf',
    'my': '9Btx3DZF0dXLMZlywRbVRNhxy1Lr.ttf', 'myEB': '9Bty3DZF0dXLMZlywRbVRNhxy2pLVFA0.ttf',
    'elite': 'XLYgIZbkc4JPUL5CVArUVL0nhnc.ttf', 'pen': 'daaDSSYiLGqEal3MvdA_FOL_3FkN2z4.ttf',
    'sansB': 'PbyxFmXiEBPT4ITbgNA5Cgms3VYcOA-vvnIzzg01eLQ.ttf', 'gaegu': 'TuGSUVB6Up9NU573jvw7.ttf',
    'hahm': 'BngXUXpCQ3nKpIo0TfPyfCdXfaeU4RiUP9jo.ttf', 'hahmEB': 'BngXUXpCQ3nKpIo0TfPyfCdXfaeU4RjKP9jo.ttf', 'serifB': '3JnoSDn90Gmq2mr3blnHaTZXbOtLJDvui3JOncgBf852.ttf',
}
def font(k, s): return ImageFont.truetype(F + FONTS[k], s)
META = {}
INK = (28, 24, 21)
RED = (172, 36, 30)

# ---------- numeric helpers ----------
def boxblur(a, r):
    r = int(r)
    if r < 1: return a
    k = 2 * r + 1
    p = np.pad(a, ((r + 1, r), (0, 0)), mode='edge'); c = np.cumsum(p, 0); a = (c[k:] - c[:-k]) / k
    p = np.pad(a, ((0, 0), (r + 1, r)), mode='edge'); c = np.cumsum(p, 1); a = (c[:, k:] - c[:, :-k]) / k
    return a
def gblur(a, r):
    for _ in range(3): a = boxblur(a, max(1, int(r)))
    return a
def up(a, W, H):
    return np.asarray(Image.fromarray(a.astype(np.float32), 'F').resize((W, H), Image.BICUBIC))

def crumple(W, H, seed, n=None, creases=7, letter=False, contrast=1.0, scale=4, slope=0.16):
    """Shading map (~1.0 mean) of crumpled paper: multi-scale facets + long creases, lit from upper left."""
    rng = np.random.default_rng(seed)
    w, h = max(8, W // scale), max(8, H // scale)
    ys, xs = np.mgrid[0:h, 0:w].astype(np.float32)
    gx = np.zeros((h, w), np.float32); gy = np.zeros((h, w), np.float32)
    base_n = max(24, int(W * H / 5000))
    for nn, mk in ((base_n, slope), (max(8, base_n // 5), slope * 0.55)):
        sx = rng.uniform(-10, w + 10, nn); sy = rng.uniform(-10, h + 10, nn)
        ang = rng.uniform(0, 2 * np.pi, nn); mag = rng.gamma(2.0, mk / 2, nn)
        best = np.full((h, w), 1e9, np.float32); idx = np.zeros((h, w), np.int32)
        for i in range(nn):
            d = (xs - sx[i]) ** 2 + (ys - sy[i]) ** 2; m = d < best; best[m] = d[m]; idx[m] = i
        gx += (np.cos(ang) * mag)[idx]; gy += (np.sin(ang) * mag)[idx]
    for _ in range(creases):
        a0 = rng.uniform(0, np.pi); nx, ny = np.cos(a0), np.sin(a0)
        px, py = rng.uniform(0, w), rng.uniform(0, h)
        s = (xs - px) * nx + (ys - py) * ny
        amp = rng.normal(0, slope * 0.9)
        fade = np.exp(-(((xs - px) * -ny + (ys - py) * nx) / (rng.uniform(0.3, 0.9) * max(w, h))) ** 2)
        loc = np.exp(-(s / rng.uniform(12, 40)) ** 2)
        gx += amp * np.tanh(s / 0.8) * fade * loc * nx; gy += amp * np.tanh(s / 0.8) * fade * loc * ny
    if letter:
        for y0 in (h / 3, 2 * h / 3):
            gy += rng.choice([-1, 1]) * 0.22 * np.tanh((ys - y0) / 0.6) * np.exp(-((ys - y0) / 26) ** 2)
    gx = gblur(gx, 1) * 0.6 + gx * 0.4; gy = gblur(gy, 1) * 0.6 + gy * 0.4
    nz = gblur(rng.normal(0, 1, (h, w)).astype(np.float32), 2)
    ngy, ngx = np.gradient(nz); gx += ngx * 0.9; gy += ngy * 0.9
    GX, GY = up(gx, W, H), up(gy, W, H)
    fine = gblur(rng.normal(0, 1, (H, W)).astype(np.float32), 1)
    fgy, fgx = np.gradient(fine)
    GX = GX + fgx * 0.25; GY = GY + fgy * 0.25
    L = np.array([-0.45, -0.55, 0.7]); L /= np.linalg.norm(L)
    nxv, nyv = -GX, -GY
    dif = (nxv * L[0] + nyv * L[1] + L[2]) / np.sqrt(nxv ** 2 + nyv ** 2 + 1)
    shade = dif / dif.mean()
    return np.clip(1 + contrast * (shade - 1), 0.62, 1.3).astype(np.float32)

CC0 = sys.argv[3] if len(sys.argv) > 3 else None
_NM = {}
def _tex(id, kind):
    key = (id, kind)
    if key not in _NM:
        im = Image.open(f'{CC0}/{id}/{id}_2K-JPG_{kind}.jpg')
        _NM[key] = np.asarray(im.convert('RGB' if kind != 'Displacement' else 'L'), np.float32)
    return _NM[key]
def _crop(a, W, H, rng, zoom):
    S = a.shape[0]
    cw = min(S, S * zoom); ch = cw * H / W
    if ch > S: ch = S; cw = ch * W / H
    x0 = rng.uniform(0, S - cw); y0 = rng.uniform(0, S - ch)
    return x0, y0, cw, ch
def _resize(ch2d, box, W, H):
    x0, y0, cw, chh = box
    im = Image.fromarray(ch2d.astype(np.float32), 'F').crop((int(x0), int(y0), int(x0 + cw), int(y0 + chh)))
    return np.asarray(im.resize((W, H), Image.BICUBIC))
def real_crumple(W, H, seed, contrast=1.0, zoom=1.0, id='Paper003'):
    """Shading from a CC0 scanned crumpled-paper normal map (ambientCG Paper003), lit from upper left."""
    rng = np.random.default_rng(seed)
    n = _tex(id, 'NormalGL'); box = _crop(n, W, H, rng, zoom)
    nx = _resize(n[..., 0] / 127.5 - 1, box, W, H); ny = -_resize(n[..., 1] / 127.5 - 1, box, W, H); nz = _resize(n[..., 2] / 127.5 - 1, box, W, H)
    if rng.random() < 0.5: nx = nx[:, ::-1] * -1; ny = ny[:, ::-1]; nz = nz[:, ::-1]
    L = np.array([-0.6, -0.55, 0.58]); L /= np.linalg.norm(L)
    dif = (nx * L[0] + ny * L[1] + nz * L[2]) / np.sqrt(nx ** 2 + ny ** 2 + nz ** 2 + 1e-6)
    disp = _resize(_tex(id, 'Displacement') / 255, box, W, H)
    if nx.base is not None: pass
    ao = np.clip(1 - 0.9 * (gblur(disp.astype(np.float32), 18) - disp), 0.75, 1.05)
    shade = dif / dif.mean() * ao
    return np.clip(1 + contrast * (shade - 1), 0.55, 1.35).astype(np.float32)
def base_color(W, H, seed, base, kind='Paper006', zoom=0.6, strength=1.0):
    """Real paper fiber colour (CC0 scan) re-tinted to the requested base colour."""
    rng = np.random.default_rng(seed + 5)
    c = _tex(kind, 'Color'); box = _crop(c, W, H, rng, zoom)
    ch = np.dstack([_resize(c[..., i], box, W, H) for i in range(3)])
    lum = ch.mean(2, keepdims=True); lum = lum / lum.mean()
    var = 1 + strength * (lum - 1) * 1.6
    return np.array(base, np.float32)[None, None, :] * var

def paper(W, H, seed, base=(226, 212, 183), contrast=0.6, stains=1, edge=0.35, letter=False, n=230, creases=7, scale=4, fiber='Paper006'):
    rng = np.random.default_rng(seed + 100)
    if CC0:
        sh = real_crumple(W, H, seed, contrast=contrast * 0.9, zoom=min(1.0, max(0.25, W / 2048)))
        img = base_color(W, H, seed, base, kind=fiber, zoom=min(1.0, max(0.2, W / 2600)))
    else:
        sh = crumple(W, H, seed, n=n, creases=creases, letter=letter, contrast=contrast, scale=scale)
        img = np.zeros((H, W, 3), np.float32); img[:] = base
    lf = up(gblur(rng.normal(0, 1, (max(4, H // 40), max(4, W // 40))).astype(np.float32), 1), W, H)
    img *= (1 + 0.05 * lf)[..., None]
    img[..., 2] *= (1 - 0.05 * np.clip(lf, 0, None))
    img += rng.normal(0, 3.2, (H, W))[..., None]
    yy, xx = np.mgrid[0:H, 0:W].astype(np.float32)
    for _ in range(stains):
        cx, cy = rng.uniform(0.15, 0.85) * W, rng.uniform(0.15, 0.85) * H
        R0 = rng.uniform(0.06, 0.14) * min(W, H)
        th = np.arctan2(yy - cy, xx - cx); r = np.sqrt((xx - cx) ** 2 + (yy - cy) ** 2)
        wob = 1 + 0.05 * np.sin(th * 3 + rng.uniform(0, 6)) + 0.03 * np.sin(th * 7 + rng.uniform(0, 6))
        rr = r / wob
        ring = np.exp(-((rr - R0) / (R0 * 0.035)) ** 2) * 0.55 + np.clip(1 - rr / R0, 0, 1) * 0.10
        ring *= (0.6 + 0.4 * np.cos(th - rng.uniform(0, 6)))
        img -= ring[..., None] * np.array([38, 55, 78])
    d = np.minimum(np.minimum(xx, W - 1 - xx), np.minimum(yy, H - 1 - yy))
    e = np.clip(1 - d / (0.16 * min(W, H)), 0, 1) ** 2
    img *= (1 - edge * e)[..., None]
    img[..., 2] -= 14 * e
    img *= sh[..., None]
    spk = rng.random((H, W)) > 0.9993
    img[spk] *= 0.55
    return np.clip(img, 0, 255).astype(np.uint8)

def torn_mask(w, h, rough=6.0, seed=0, margin=12, step=5):
    rng = np.random.default_rng(seed)
    def jit(n):
        if n < 2: return np.zeros(n)
        a = np.cumsum(rng.normal(0, 1, n)); a -= np.linspace(a[0], a[-1], n)
        a = a / (np.abs(a).max() + 1e-6) * rough * 0.7 + rng.normal(0, rough * 0.32, n)
        return a
    pts = []
    xs = np.arange(margin, w - margin, step); j = jit(len(xs)); pts += [(x, margin + j[i]) for i, x in enumerate(xs)]
    ys = np.arange(margin, h - margin, step); j = jit(len(ys)); pts += [(w - margin + j[i], y) for i, y in enumerate(ys)]
    xs = np.arange(w - margin, margin, -step); j = jit(len(xs)); pts += [(x, h - margin + j[i]) for i, x in enumerate(xs)]
    ys = np.arange(h - margin, margin, -step); j = jit(len(ys)); pts += [(margin + j[i], y) for i, y in enumerate(ys)]
    m = Image.new('L', (w, h), 0); ImageDraw.Draw(m).polygon(pts, fill=255)
    return m

def cutout(rgb, rough=6.0, seed=0, rim=True, rimcol=(242, 236, 222)):
    if isinstance(rgb, np.ndarray): rgb = Image.fromarray(rgb)
    w, h = rgb.size
    m = torn_mask(w, h, rough, seed)
    if rim and rough > 2:
        inner = m.filter(ImageFilter.MinFilter(7))
        rimm = np.asarray(ImageChops.subtract(m, inner), np.float32) / 255
        rng = np.random.default_rng(seed + 7)
        rimm *= np.clip(gblur(rng.random((h, w)).astype(np.float32), 2) * 3 - 0.9, 0, 1)
        base = np.asarray(rgb.convert('RGB'), np.float32)
        base = base * (1 - rimm[..., None]) + np.array(rimcol) * rimm[..., None]
        rgb = Image.fromarray(np.clip(base, 0, 255).astype(np.uint8))
    out = rgb.convert('RGBA'); out.putalpha(m)
    return out

def shade_multiply(img, seed, contrast=0.5, n=60, creases=4):
    a = np.asarray(img.convert('RGBA'), np.float32)
    sh = real_crumple(a.shape[1], a.shape[0], seed, contrast=contrast, zoom=min(1.0, max(0.25, a.shape[1] / 2048))) if CC0 else crumple(a.shape[1], a.shape[0], seed, n=n, creases=creases, contrast=contrast, scale=3)
    a[..., :3] *= sh[..., None]
    return Image.fromarray(np.clip(a, 0, 255).astype(np.uint8), 'RGBA')

def ink_texture(alpha, seed, holes=0.06, soft=1):
    """Make printed/stamped ink uneven: alpha array 0..1 -> 0..1."""
    rng = np.random.default_rng(seed)
    h, w = alpha.shape
    n = gblur(rng.random((h, w)).astype(np.float32), 2)
    patch = np.clip((n - 0.40) * 7, 0.55, 1)
    spk = (rng.random((h, w)) > holes).astype(np.float32)
    a = alpha * patch * spk
    if soft: a = gblur(a, 1) * 0.6 + a * 0.4
    return np.clip(a, 0, 1)

def text_layer(size, items, seed=0, ink=INK, texture=False):
    """items: list of (xy, text, fontkey, px, color or None). Returns RGBA ink layer."""
    w, h = size
    m = Image.new('L', (w, h), 0); d = ImageDraw.Draw(m)
    col = Image.new('RGB', (w, h), ink); dc = ImageDraw.Draw(col)
    for (x, y), t, fk, px, c in items:
        d.text((x, y), t, font=font(fk, px), fill=255)
        if c: dc.text((x, y), t, font=font(fk, px), fill=c)
    a = np.asarray(m, np.float32) / 255
    if texture: a = ink_texture(a, seed)
    out = np.dstack([np.asarray(col), (a * 255).astype(np.uint8)])
    return Image.fromarray(out, 'RGBA')

def halftone(gray, cell=7, angle=45, gain=1.0):
    H, W = gray.shape
    g = gblur(gray.astype(np.float32), max(1, cell // 3))
    th = np.deg2rad(angle); c, s = np.cos(th), np.sin(th)
    yy, xx = np.mgrid[0:H, 0:W].astype(np.float32)
    u = (xx * c + yy * s) / cell; v = (-xx * s + yy * c) / cell
    fu = u - np.floor(u) - 0.5; fv = v - np.floor(v) - 0.5
    d = np.sqrt(fu ** 2 + fv ** 2)
    dark = np.clip(1 - g, 0, 1) * gain
    r = np.sqrt(dark / np.pi)
    return np.clip((r - d) * cell * 1.4 + 0.5, 0, 1)

def save(img, name, **meta):
    img.save(os.path.join(OUT, name + '.png'))
    META[name] = dict(w=img.size[0], h=img.size[1], **meta)

def newsprint(w, h, seed, base=(238, 233, 220)):
    return paper(w, h, seed, base=base, contrast=0.28, stains=0, edge=0.08, n=120, creases=4, scale=3)

def paste(dst, src, xy):
    dst.alpha_composite(src, (int(xy[0]), int(xy[1])))

# ---------- backgrounds ----------
save(Image.fromarray(paper(2112, 1188, 1, base=(234, 224, 202), contrast=0.7, stains=1, edge=0.18, letter=True)), 'bg_paper')
save(Image.fromarray(paper(2112, 1188, 2, base=(160, 121, 82), contrast=1.7, stains=1, edge=0.38, creases=9, fiber='Paper004')), 'bg_kraft')
save(Image.fromarray(paper(2112, 1188, 3, base=(36, 34, 32), contrast=1.0, stains=0, edge=0.25, creases=8)), 'bg_dark')

# ---------- newspaper fragments (text = our own script lines, decorative) ----------
CORPUS = ("카톡을 보냈는데 삼십 분째 일이 안 사라집니다 처음엔 바쁜가 보다 했죠 그런데 한 시간이 지나면 생각이 바뀝니다 "
          "내가 뭘 잘못했나 오늘은 그 한 시간 동안 머릿속에서 벌어지는 일을 풀어 보겠습니다 심리학 연구로 보면 이건 성격이 "
          "예민해서 생기는 일이 아닙니다 마음속 경보 장치가 열심히 일하고 있는 겁니다 금요일 저녁 일곱 시 썸 타는 사람에게 "
          "메시지를 보냅니다 오늘 하루 어땠어요 삼십 분이 지납니다 프로필 사진을 눌러 봅니다 어제 나눈 대화를 처음부터 다시 "
          "읽습니다 그때 그 농담 별로였나 내가 너무 자주 연락했나 애착은 위협을 느낄 때 소중한 사람 곁으로 가게 만드는 마음의 "
          "경보 장치입니다 ").split()
def news_fragment(w, h, seed, headline):
    rng = np.random.default_rng(seed)
    bg = Image.fromarray(newsprint(w, h, seed)).convert('RGBA')
    y = 44
    head = text_layer((w, h), [((40, y), headline, 'song', 70, None)], seed, ink=(40, 36, 33)) if headline else None; y += 112 if headline else 20
    body = []
    cols = max(1, (w - 60) // 300); colw = (w - 80) // cols
    for ci in range(cols):
        yy = y; x = 40 + ci * colw
        while yy < h - 50:
            line = ''
            while len(line) < colw // 23: line += CORPUS[rng.integers(len(CORPUS))] + ' '
            body.append(((x, yy), line[: colw // 23], 'my', 21, None)); yy += 31
    bl = text_layer((w, h), body, seed + 1, ink=(70, 64, 58))
    a = np.asarray(bl, np.float32); a[..., 3] *= 0.5; bl = Image.fromarray(a.astype(np.uint8), 'RGBA')
    bg.alpha_composite(bl)
    if head: bg.alpha_composite(head)
    dr = ImageDraw.Draw(bg)
    dr.line([(40, 34), (w - 40, 34)], fill=(40, 36, 33, 200), width=3)
    dr.line([(40, y - 16), (w - 40, y - 16)], fill=(40, 36, 33, 150), width=2)
    return cutout(bg, rough=7, seed=seed)
for i, (w, h, hl) in enumerate([(760, 980, ''), (980, 620, ''), (640, 720, ''), (860, 760, '')]):
    save(news_fragment(w, h, 40 + i, hl), f'news{i + 1}')

# ---------- printed phone clipping ----------
def phone_clip(S=1.2):
    # drawn 1.2x larger than v2 so it is shown at native size (no upscaling blur)
    q = lambda v: int(round(v * S))
    W, H = q(600), q(940)
    base = Image.fromarray(newsprint(W, H, 51, base=(233, 229, 218))).convert('RGBA')
    ink = Image.new('L', (W, H), 0); d = ImageDraw.Draw(ink)
    x0, y0, x1, y1 = q(60), q(50), q(540), q(890)
    d.rounded_rectangle([x0, y0, x1, y1], radius=q(62), outline=255, width=q(11))
    d.line([(x0 + 6, y0 + q(120)), (x1 - 6, y0 + q(120))], fill=255, width=q(4))
    d.text((x0 + q(36), y0 + q(48)), '‹  그 사람', font=font('sansB', q(42)), fill=255)
    # 2026-10-23 is a Friday (2026-10-24 would be a Saturday)
    dt = '10월 23일 금요일'; fd = font('sansB', q(30)); bd = fd.getbbox(dt)
    cx = W // 2; tw = bd[2] - bd[0]
    d.rounded_rectangle([cx - tw // 2 - q(22), q(212), cx + tw // 2 + q(22), q(264)], radius=q(26), outline=255, width=q(3))
    d.text((cx - tw // 2 - bd[0], q(238) - (bd[1] + bd[3]) // 2), dt, font=fd, fill=255)
    bub = [q(150), q(300), q(520), q(392)]
    d.rounded_rectangle(bub, radius=q(26), outline=255, width=q(5))
    d.text((q(174), q(322)), '오늘 하루 어땠어요?', font=font('sansB', q(36)), fill=255)
    d.rounded_rectangle([x0 + q(30), y1 - q(86), x1 - q(110), y1 - q(36)], radius=q(25), outline=255, width=q(3))
    a = np.asarray(ink, np.float32) / 255
    fill = Image.new('L', (W, H), 0); ImageDraw.Draw(fill).rounded_rectangle([b + o for b, o in zip(bub, (5, 5, -5, -5))], radius=q(22), fill=255)
    fa = np.asarray(fill, np.float32) / 255
    dots = fa
    col = np.asarray(base, np.float32)
    yel = np.array([226, 186, 62], np.float32)
    col[..., :3] = col[..., :3] * (1 - dots[..., None] * 0.85) + yel * dots[..., None] * 0.85
    one = Image.new('L', (W, H), 0); ImageDraw.Draw(one).text((q(112), q(300)), '1', font=font('sansB', q(46)), fill=255)
    oa = np.asarray(one, np.float32) / 255
    col[..., :3] = col[..., :3] * (1 - oa[..., None]) + np.array([206, 112, 34]) * oa[..., None]
    col[..., :3] = col[..., :3] * (1 - a[..., None] * 0.92) + np.array(INK) * a[..., None] * 0.92
    img = Image.fromarray(np.clip(col, 0, 255).astype(np.uint8), 'RGBA')
    img = shade_multiply(img, 54, contrast=0.25).crop((0, 0, W, q(600)))
    return cutout(img.convert('RGB'), rough=5, seed=55), dict(one=[q(126), q(330)])
img, m = phone_clip(); save(img, 'phone', **m)

# ---------- notes / strips / headline clippings ----------
def note(text, seed, base=(236, 224, 170), px=64, ink=(30, 36, 58), rough=5, fk='gaegu', pad=(46, 34)):
    f = font(fk, px); bb = f.getbbox(text)
    w, h = bb[2] - bb[0] + 2 * pad[0], bb[3] - bb[1] + 2 * pad[1]
    bg = Image.fromarray(paper(w, h, seed, base=base, contrast=0.3, stains=0, edge=0.1, n=60, creases=3, scale=3)).convert('RGBA')
    bg.alpha_composite(text_layer((w, h), [((pad[0] - bb[0], pad[1] - bb[1]), text, fk, px, None)], seed, ink=ink))
    return cutout(bg, rough=rough, seed=seed)
save(note('바쁜가 보다~', 61, px=108), 'note_busy')
for i, t in enumerate(['프로필 사진 또 눌러 봄', '어제 대화 처음부터 다시 읽음', '그 농담, 별로였나?', '내가 너무 자주 연락했나?']):
    save(note(t, 70 + i, base=[(238, 230, 205), (236, 224, 170), (232, 214, 204), (226, 230, 214)][i], px=58), f'clue{i + 1}')
save(note('예민한 성격 탓?', 80, base=(238, 230, 205), px=72), 'note_sensitive')

def headline(text, seed, px=150, fk='hahmEB', pad=(56, 40)):
    f = font(fk, px); bb = f.getbbox(text)
    w, h = bb[2] - bb[0] + 2 * pad[0], bb[3] - bb[1] + 2 * pad[1]
    bg = Image.fromarray(newsprint(w, h, seed)).convert('RGBA')
    bg.alpha_composite(text_layer((w, h), [((pad[0] - bb[0], pad[1] - bb[1]), text, fk, px, None)], seed, ink=(24, 21, 18)))
    return cutout(bg, rough=5, seed=seed)
save(headline('30분째 답장 없음', 90, px=112), 'hl_30')
save(headline('머릿속에서 일어나는 일', 91, px=92), 'hl_head')
save(headline('마음의 경보 장치', 92, px=120), 'hl_alarm')

def typed_strip(text, seed, px=40, fk='codeB', pad=(28, 16), base=(240, 236, 226)):
    f = font(fk, px); bb = f.getbbox(text)
    w, h = bb[2] - bb[0] + pad[0] * 2, bb[3] - bb[1] + pad[1] * 2 + 6
    bg = Image.fromarray(paper(w, h, seed, base=base, contrast=0.4, stains=0, edge=0.1, n=30, creases=2, scale=2)).convert('RGBA')
    bg.alpha_composite(text_layer((w, h), [((pad[0] - bb[0], pad[1] - bb[1] + 3), text, fk, px, None)], seed, ink=(30, 27, 25)))
    return cutout(bg, rough=1.5, seed=seed, rim=False)
save(typed_strip("심리학에선 '애착'이라고 불러요", 101, px=42), 'lab_attach')
save(typed_strip('볼비 (1969) · 미쿨린서 & 셰이버 (2003)', 102, px=36), 'lab_cite7')
# blank ticket for the running clock (digits drawn live in HTML)
tk = Image.fromarray(paper(440, 110, 104, base=(240, 236, 226), contrast=0.4, stains=0, edge=0.1, n=30, creases=2, scale=2))
save(cutout(tk, rough=1.5, seed=104, rim=False), 'ticket')

# ---------- stamps (red ink, worn) ----------
def stamp(text, seed, px=86, fk='bhs', color=RED, pad=24, border=7, rot=0):
    f = font(fk, px); bb = f.getbbox(text)
    tw, th = bb[2] - bb[0], bb[3] - bb[1]
    W, H = tw + 2 * pad, th + 2 * pad
    m = Image.new('L', (W, H), 0); d = ImageDraw.Draw(m)
    d.rectangle([3, 3, W - 4, H - 4], outline=255, width=border)
    d.text((pad - bb[0], pad - bb[1]), text, font=f, fill=255)
    a = np.asarray(m, np.float32) / 255
    rng = np.random.default_rng(seed)
    n = gblur(rng.random((H, W)).astype(np.float32), 3)
    a = a * 0.95
    out = np.zeros((H, W, 4), np.uint8); out[..., :3] = color; out[..., 3] = (np.clip(a, 0, 1) * 255).astype(np.uint8)
    return Image.fromarray(out, 'RGBA').rotate(rot, expand=True, resample=Image.BICUBIC)
save(stamp('읽지 않음', 110, px=70, rot=-8), 'st_unread')
save(stamp('1시간째', 111, px=84, rot=6), 'st_1h')
save(stamp('끝에서 공개', 112, px=104, rot=-4), 'st_soon')

# ---------- tape, pin, marker ----------
def tape(w, h, seed, color=(222, 210, 178), alpha=0.8):
    rng = np.random.default_rng(seed)
    a = np.full((h, w), alpha, np.float32)
    for side in (0, 1):
        prof = (np.abs(gblur(rng.normal(0, 1, (h, 1)).astype(np.float32), 1)[:, 0]) * 9 + rng.random(h) * 4).astype(int) + 2
        for y in range(h):
            if side == 0: a[y, :prof[y]] = 0
            else: a[y, w - prof[y]:] = 0
    a *= 0.9 + 0.1 * rng.random((h, w))
    rgb = np.zeros((h, w, 3), np.float32); rgb[:] = color
    rgb += rng.normal(0, 4, (h, w))[..., None]
    for _ in range(3):
        x = rng.integers(10, w - 10); rgb[:, max(0, x - 1):x + 1] *= 0.93
    return Image.fromarray(np.dstack([np.clip(rgb, 0, 255), a * 255]).astype(np.uint8), 'RGBA')
for i in range(4): save(tape(230 + 30 * i, 62, 120 + i), f'tape{i + 1}')

def pin(size=70, color=(176, 30, 30)):
    img = Image.new('RGBA', (size, size), (0, 0, 0, 0)); d = ImageDraw.Draw(img)
    r = size * 0.36; c = size / 2
    for i in range(int(r), 0, -1):
        t = i / r; k = 0.5 + 0.5 * (1 - t)
        d.ellipse([c - i, c - i, c + i, c + i], fill=tuple(int(v * k) for v in color) + (255,))
    d.ellipse([c - r * 0.55, c - r * 0.62, c - r * 0.12, c - r * 0.22], fill=(255, 235, 230, 170))
    return img
save(pin(), 'pin')

# ---------- clock clipping + hands ----------
def clock(size=700):
    img = Image.fromarray(newsprint(size, size, 130, base=(236, 230, 214))).convert('RGBA')
    m = Image.new('L', (size, size), 0); d = ImageDraw.Draw(m)
    c = size / 2; R = size * 0.44
    d.ellipse([c - R, c - R, c + R, c + R], outline=255, width=12)
    d.ellipse([c - R * 0.92, c - R * 0.92, c + R * 0.92, c + R * 0.92], outline=255, width=3)
    for i in range(60):
        a = i / 60 * 2 * math.pi - math.pi / 2; r1 = R * (0.8 if i % 5 == 0 else 0.86)
        d.line([(c + math.cos(a) * r1, c + math.sin(a) * r1), (c + math.cos(a) * R * 0.9, c + math.sin(a) * R * 0.9)], fill=255, width=6 if i % 5 == 0 else 2)
    f = font('hahm', 54)
    for i in range(1, 13):
        a = i / 12 * 2 * math.pi - math.pi / 2; t = str(i); bb = f.getbbox(t)
        x = c + math.cos(a) * R * 0.66 - (bb[2] + bb[0]) / 2; y = c + math.sin(a) * R * 0.66 - (bb[3] + bb[1]) / 2
        d.text((x, y), t, font=f, fill=255)
    a = np.asarray(m, np.float32) / 255
    col = np.asarray(img, np.float32)
    yy, xx = np.mgrid[0:size, 0:size]; rr = np.sqrt((xx - c) ** 2 + (yy - c) ** 2) / R
    shade = halftone(1 - np.clip((rr - 0.55) * 0.6, 0, 0.35), cell=6, angle=30)
    col[..., :3] *= (1 - shade[..., None] * 0.35)
    col[..., :3] = col[..., :3] * (1 - a[..., None] * 0.9) + np.array(INK) * a[..., None] * 0.9
    img = Image.fromarray(np.clip(col, 0, 255).astype(np.uint8), 'RGBA')
    circ = Image.new('L', (size, size), 0)
    pts = [(c + math.cos(t) * (R * 1.06 + np.random.default_rng(132).normal(0, 2.5)), c + math.sin(t) * (R * 1.06 + np.random.default_rng(int(t * 1000)).normal(0, 2.5))) for t in np.linspace(0, 2 * math.pi, 180)]
    ImageDraw.Draw(circ).polygon(pts, fill=255)
    img.putalpha(circ)
    return img
save(clock(), 'clock')
def hand(length, width, seed):
    W, H = width * 3, length + width * 2
    m = Image.new('L', (W, H), 0); d = ImageDraw.Draw(m)
    cx = W / 2
    d.polygon([(cx, 4), (cx + width / 2, H - width * 1.6), (cx, H - width * 0.9), (cx - width / 2, H - width * 1.6)], fill=255)
    d.ellipse([cx - width * 0.7, H - width * 2.2, cx + width * 0.7, H - width * 0.8], fill=255)
    a = np.asarray(m, np.float32) / 255
    out = np.zeros((H, W, 4), np.uint8); out[..., :3] = INK; out[..., 3] = (a * 255).astype(np.uint8)
    return Image.fromarray(out, 'RGBA'), H - width * 1.5
img, piv = hand(262, 26, 133); save(img, 'hand_min', pivot=piv)
img, piv = hand(176, 32, 134); save(img, 'hand_hour', pivot=piv)

# ---------- "1" clipping for the evidence board ----------
def one_clip():
    W, H = 320, 330
    bg = Image.fromarray(newsprint(W, H, 140, base=(236, 230, 214))).convert('RGBA')
    bg.alpha_composite(text_layer((W, H), [((100, 14), '1', 'bhs', 230, None)], 141, ink=(206, 112, 34)))
    bg.alpha_composite(text_layer((W, H), [((50, 256), '읽지 않음', 'gaegu', 56, None)], 142))
    return cutout(bg, rough=4, seed=143)
save(one_clip(), 'one_clip')

# ---------- research cards (photocopy look) ----------
def card(lines, seed, hl=None, pad=(40, 32)):
    """lines: (text, fontkey, px, line_height). Card size follows the longest line."""
    ws = [font(fk, px).getbbox(t) for t, fk, px, g in lines]
    w = max(b[2] - b[0] for b in ws) + 2 * pad[0]; h = sum(g for _, _, _, g in lines) + 2 * pad[1] - 8
    bg = Image.fromarray(paper(w, h, seed, base=(244, 241, 233), contrast=0.25, stains=0, edge=0.06, n=70, creases=3, scale=3)).convert('RGBA')
    items = []; y = pad[1]; boxes = []
    for (t, fk, px, g), bb in zip(lines, ws):
        items.append(((pad[0] - bb[0], y - bb[1] + 4), t, fk, px, None))
        if hl is not None and t in hl: boxes.append([pad[0] - 10, y - 2, pad[0] + bb[2] - bb[0] + 10, y + bb[3] - bb[1] + 14])
        y += g
    bg.alpha_composite(text_layer((w, h), items, seed, ink=(26, 24, 22)))
    return cutout(bg.convert('RGB'), rough=1.6, seed=seed, rim=False), boxes
img, b = card([('헤이잔 & 셰이버, 1987', 'hahmEB', 42, 72), ("어른의 연애에도 '애착'이 있다", 'hahm', 42, 56)], 150)
save(img, 'card_hazan')
img, b = card([('미쿨린서 & 셰이버, 2003', 'hahmEB', 42, 72), ('불안할수록 위협을 더 크게 본다', 'hahm', 42, 56)], 151)
save(img, 'card_mik')
L1, L2 = '불안이 큰 사람일수록', '실제보다 더 자주 메시지를 바랐다'
img, b = card([('파텔 외, 2022 · 연애 중인 대학생 302명', 'hahmEB', 50, 98), (L1, 'hahm', 68, 92), (L2, 'hahm', 68, 88)], 152, hl=[L1, L2], pad=(50, 40))
save(img, 'card_patel', hl=b)

# ---------- index cards for the teaser ----------
def index_card(n, seed):
    w, h = 480, 300
    bg = Image.fromarray(paper(w, h, seed, base=(241, 235, 219), contrast=0.45, stains=0, edge=0.12, n=40, creases=2, scale=3)).convert('RGBA')
    d = ImageDraw.Draw(bg)
    d.line([(0, 72), (w, 72)], fill=(190, 70, 64, 200), width=3)
    for y in range(110, h - 20, 38): d.line([(0, y), (w, y)], fill=(120, 150, 190, 120), width=2)
    d.ellipse([w / 2 - 12, h - 34, w / 2 + 12, h - 10], fill=(90, 80, 70, 255))
    bg.alpha_composite(text_layer((w, h), [((26, 8), f'방법 {n}', 'hahmEB', 54, None)], seed))
    rng = np.random.default_rng(seed)
    for y in (90, 128, 166):
        x1 = 32 + rng.integers(0, 20); x2 = w - 44 - rng.integers(0, 130)
        d.rectangle([x1, y, x2, y + 26], fill=(22, 20, 19, 245))
    return cutout(bg.convert('RGB'), rough=1.4, seed=seed, rim=False)
for i in range(3): save(index_card(i + 1, 160 + i), f'icard{i + 1}')

# ---------- masthead ----------
def masthead():
    w, h = 1500, 640
    bg = Image.fromarray(paper(w, h, 170, base=(232, 222, 198), contrast=0.6, stains=1, edge=0.25, n=120, creases=5, scale=3)).convert('RGBA')
    items = [((0, 0), '', 'code', 20, None)]
    f = font('hahmEB', 170); t = 'F의 연애 레터'; bb = f.getbbox(t)
    items.append((((w - (bb[2] - bb[0])) // 2 - bb[0], 160 - bb[1]), t, 'hahmEB', 170, None))
    f2 = font('hahm', 46); t2 = '제1호  ·  2026년 10월  ·  근거로 풀어 주는 연애 심리'; bb2 = f2.getbbox(t2)
    items.append((((w - (bb2[2] - bb2[0])) // 2 - bb2[0], 446), t2, 'hahm', 46, None))
    bg.alpha_composite(text_layer((w, h), items, 171, ink=(26, 23, 20)))
    d = ImageDraw.Draw(bg)
    for y, wd in ((118, 6), (130, 2), (420, 2), (432, 6), (528, 2)):
        d.line([(70, y), (w - 70, y)], fill=(26, 23, 20, 220), width=wd)
    return cutout(bg.convert('RGB'), rough=6, seed=172)
save(masthead(), 'masthead')

# ---------- potato cut-out stickers (printed look) ----------
def potato_sticker(name, seed):
    src = Image.open(os.path.join(RAW, f'pot_{name}.png')).convert('RGBA')
    pad = 40
    W, H = src.size[0] + 2 * pad, src.size[1] + 2 * pad
    canvas = Image.new('RGBA', (W, H), (0, 0, 0, 0)); canvas.alpha_composite(src, (pad, pad))
    a = np.asarray(canvas, np.float32)
    al = a[..., 3] / 255
    yy, xx = np.mgrid[0:H, 0:W].astype(np.float32)
    # print shading: halftone dots darker toward lower-right of the body
    g = 1 - np.clip(((xx / W) * 0.6 + (yy / H) * 0.8 - 0.55) * 0.9, 0, 0.45)
    dots = halftone(g, cell=7, angle=45) * al
    a[..., :3] *= (1 - dots[..., None] * 0.30)
    rng = np.random.default_rng(seed)
    a[..., :3] *= (0.94 + 0.06 * gblur(rng.random((H, W)).astype(np.float32), 2))[..., None]
    body = Image.fromarray(np.clip(a, 0, 255).astype(np.uint8), 'RGBA')
    # paper sticker border (cut with scissors, slightly uneven)
    border = canvas.getchannel('A').filter(ImageFilter.MaxFilter(31)).filter(ImageFilter.GaussianBlur(2)).point(lambda v: 255 if v > 110 else 0)
    paperimg = Image.fromarray(paper(W, H, seed, base=(239, 233, 219), contrast=0.45, stains=0, edge=0.05, n=60, creases=3, scale=3)).convert('RGBA')
    paperimg.putalpha(border)
    paperimg.alpha_composite(body)
    return shade_multiply(paperimg, seed + 1, contrast=0.35, n=50, creases=3)
for i, nm in enumerate(['basic', 'anx', 'aha', 'smile', 'anx_siren', 'aha_siren']):
    save(potato_sticker(nm, 180 + i), f'pot_{nm}')
# red ink potato seal (logo): outline + face of the potato inside a round seal with the channel name
src = Image.open(os.path.join(RAW, 'pot_basic.png')).convert('RGBA')
src = src.resize((int(src.size[0] * 190 / src.size[1]), 190), Image.LANCZOS)
arr = np.asarray(src, np.float32); al = arr[..., 3] / 255; lum = arr[..., :3].mean(2)
pot_ink = np.clip((150 - lum) / 50, 0, 1) * al
S = 320
canvas = np.zeros((S, S), np.float32)
ox, oy = (S - src.size[0]) // 2, 62
canvas[oy:oy + src.size[1], ox:ox + src.size[0]] = np.maximum(canvas[oy:oy + src.size[1], ox:ox + src.size[0]], pot_ink)
ring = Image.new('L', (S, S), 0); d = ImageDraw.Draw(ring)
d.ellipse([8, 8, S - 9, S - 9], outline=255, width=10); d.ellipse([24, 24, S - 25, S - 25], outline=255, width=3)
canvas = np.maximum(canvas, np.asarray(ring, np.float32) / 255)
a = ink_texture(canvas, 190)
out = np.zeros((S, S, 4), np.uint8); out[..., :3] = RED; out[..., 3] = (a * 235).astype(np.uint8)
save(Image.fromarray(out, 'RGBA').rotate(-6, resample=Image.BICUBIC), 'potato_stamp')

json.dump(META, open(os.path.join(OUT, 'meta.json'), 'w'), indent=1)
print('assets:', len(META))
