# F의 연애 01편 icon screens for the psychology experiments (2026-10-24): the rock-and-snake task (rocks, shock, measures,
# uncertainty curve), the drop in belonging, the alarm in 1 of 5 adults, attachment anxiety by age, the spider study and
# affect labelling. Same look as icons.py: black background, white line art (LW, rounded joints), gray = off,
# yellow (#F2C94C) = the key element, red only for warning. Drawn at 2x (SS) and downsampled; every drawing stays above
# y 860 px and inside x 120..1800 px. Every kind: fn(t, dur, args, at) -> 1920x1080 RGB image (see fy_common.py).
# v2 (2026-10-24, owner): text white (yellow only for the key item) and larger (50-80 px), in the graphic font of
# fy_common.font() (Gmarket Sans); the 320 counter keeps its digits in equal cells (tab_text).
import math
from PIL import Image, ImageDraw, ImageFilter
from fy_common import *

BLACK = (0, 0, 0)
UNLIT = (72, 72, 72)                                   # an unlit lamp


# --- small drawing helpers ------------------------------------------------------------------------------------------
def _k(col, k):
    """Colour faded in from the black background (k = 0..1)."""
    return mix(BLACK, col, k)


def _line(d, pts, col, w=LW, closed=False, caps=True):
    """Polyline with round joints; round ends unless caps=False; closed=True draws a loop."""
    pts = [tuple(p) for p in pts]
    if closed:
        pts = pts + pts[:2]
    d.line(pts, fill=col, width=max(1, round(w)), joint="curve")
    if caps and not closed:
        r = w / 2
        for x, y in (pts[0], pts[-1]):
            d.ellipse([x - r, y - r, x + r, y + r], fill=col)


def _txt(d, xy, s, px, col, weight="SemiBold", anchor="mm"):
    """Graphic text (fy_common.font); anchor-'m' text is moved to its true middle (mm_dy)."""
    x, y = xy
    if anchor[1] == "m":
        y += mm_dy(px)
    d.text((x, y), s, font=font(px, weight), fill=col, anchor=anchor)


def _times(at, defaults):
    """Voice times for items shown one after another; a missing one follows the previous with the default spacing."""
    out = []
    for i, dv in enumerate(defaults):
        v = at_or(at, i, None)
        out.append(v if v is not None else (dv if i == 0 else out[-1] + dv - defaults[i - 1]))
    return out


def _rot(pts, cx, cy, ang):
    c, s = math.cos(ang), math.sin(ang)
    return [(cx + (x - cx) * c - (y - cy) * s, cy + (x - cx) * s + (y - cy) * c) for x, y in pts]


def _chaikin(pts, n=2):
    """Corner-cut a closed polygon n times (soft corners)."""
    for _ in range(n):
        out = []
        for i in range(len(pts)):
            (x0, y0), (x1, y1) = pts[i], pts[(i + 1) % len(pts)]
            out += [(0.75 * x0 + 0.25 * x1, 0.75 * y0 + 0.25 * y1), (0.25 * x0 + 0.75 * x1, 0.25 * y0 + 0.75 * y1)]
        pts = out
    return pts


def _bez(p0, p1, p2, p3, n=32):
    return [((1 - u) ** 3 * p0[0] + 3 * (1 - u) ** 2 * u * p1[0] + 3 * (1 - u) * u * u * p2[0] + u ** 3 * p3[0],
             (1 - u) ** 3 * p0[1] + 3 * (1 - u) ** 2 * u * p1[1] + 3 * (1 - u) * u * u * p2[1] + u ** 3 * p3[1])
            for u in (i / n for i in range(n + 1))]


def _ell(cx, cy, rx, ry, a0, a1, n=48):
    """Points on an ellipse from angle a0 to a1 (radians, PIL orientation: 90 deg points down)."""
    return [(cx + rx * math.cos(a0 + (a1 - a0) * i / n), cy + ry * math.sin(a0 + (a1 - a0) * i / n)) for i in range(n + 1)]


def _dot(d, x, y, r, col):
    d.ellipse([x - r, y - r, x + r, y + r], fill=col)


def _thick(d, pts, col, w, closed=False, caps=True):
    """Wide stroke drawn segment by segment with a disc at every point (no gaps on tight curves)."""
    pts = list(pts) + ([pts[0]] if closed else [])
    for a, b in zip(pts, pts[1:]):
        d.line([a, b], fill=col, width=max(1, round(w)))
    for i, (x, y) in enumerate(pts):
        if caps or closed or 0 < i < len(pts) - 1:
            _dot(d, x, y, w / 2, col)


def _snap(p, poly):
    """Nearest point to p on the closed polygon poly."""
    best, bd = p, 1e18
    for (x0, y0), (x1, y1) in zip(poly, poly[1:] + poly[:1]):
        dx, dy = x1 - x0, y1 - y0
        u = max(0.0, min(1.0, ((p[0] - x0) * dx + (p[1] - y0) * dy) / max(dx * dx + dy * dy, 1e-9)))
        q = (x0 + u * dx, y0 + u * dy)
        dd = (q[0] - p[0]) ** 2 + (q[1] - p[1]) ** 2
        if dd < bd:
            best, bd = q, dd
    return best


# --- outline of a union of simple shapes (hands, bubbles, the seated person) ---------------------------------------
# shapes: ("circle", x, y, r), ("capsule", x0, y0, x1, y1, r), ("rrect", x0, y0, x1, y1, radius), ("poly", pts).
# The union grown by w/2 is painted in the line colour, then the union shrunk by w/2 is painted black: an outline of
# even width w around the whole union, with no lines where the shapes overlap.
def _grow(d, s, delta, col):
    kind = s[0]
    if kind == "circle":
        _, x, y, r = s
        if r + delta > 0:
            _dot(d, x, y, r + delta, col)
    elif kind == "capsule":
        _, x0, y0, x1, y1, r = s
        r += delta
        if r > 0:
            d.line([(x0, y0), (x1, y1)], fill=col, width=max(1, round(2 * r)))
            _dot(d, x0, y0, r, col)
            _dot(d, x1, y1, r, col)
    elif kind == "rrect":
        _, x0, y0, x1, y1, rad = s
        x0, y0, x1, y1 = x0 - delta, y0 - delta, x1 + delta, y1 + delta
        if x1 - x0 > 1 and y1 - y0 > 1:
            d.rounded_rectangle([x0, y0, x1, y1], radius=max(0, min(rad + delta, (x1 - x0) / 2, (y1 - y0) / 2)), fill=col)
    elif kind == "poly":
        d.polygon(s[1], fill=col)
        if delta > 0:
            _line(d, s[1], col, 2 * delta, closed=True)


def _shrink_poly(img, pts, delta, col):
    x0, y0 = int(min(p[0] for p in pts)) - 2, int(min(p[1] for p in pts)) - 2
    x1, y1 = int(max(p[0] for p in pts)) + 3, int(max(p[1] for p in pts)) + 3
    m = Image.new("L", (x1 - x0, y1 - y0), 0)
    md = ImageDraw.Draw(m)
    q = [(x - x0, y - y0) for x, y in pts]
    md.polygon(q, fill=255)
    _line(md, q, 0, 2 * delta, closed=True)
    img.paste(col, (x0, y0), m)


def _outline_union(img, shapes, col, w=LW, inside=BLACK):
    d = ImageDraw.Draw(img)
    for s in shapes:
        _grow(d, s, w / 2, col)
    for s in shapes:
        if s[0] == "poly":
            _shrink_poly(img, s[1], w / 2, inside)
        else:
            _grow(d, s, -w / 2, inside)


# --- rocks, snake, hand, bolt ---------------------------------------------------------------------------------------
# outline (x from -0.5 to 0.5 of the width, y from -1 = top to 0 = ground, in units of the height) and facet lines
# (low-poly boulders: the facet lines split each rock into planes and end on the outline or the ground)
ROCKS = {
    "a": ([(-0.50, 0.00), (-0.48, -0.34), (-0.34, -0.70), (-0.08, -0.94), (0.20, -1.00), (0.42, -0.78), (0.50, -0.40),
           (0.46, 0.00)], [[(-0.34, -0.70), (0.00, -0.56), (0.42, -0.78)], [(0.00, -0.56), (0.08, 0.00)]]),
    "b": ([(-0.50, 0.00), (-0.47, -0.32), (-0.36, -0.62), (-0.10, -0.80), (0.16, -0.76), (0.36, -0.92), (0.49, -0.60),
           (0.50, 0.00)], [[(-0.36, -0.62), (0.20, -0.46), (0.49, -0.60)], [(0.20, -0.46), (0.24, 0.00)]]),
}


def _rock(d, x, yb, w, h, kind, col, ang=0.0):
    """Line-art rock standing on (x, yb), black inside; ang tilts it around its middle."""
    outline, facets = ROCKS[kind]
    P = lambda pts: [(x + u * w, yb + v * h) for u, v in pts]
    poly = _chaikin(P(outline), 1)
    lines = []
    for f in facets:
        pts = P(f)
        pts[0], pts[-1] = _snap(pts[0], poly), _snap(pts[-1], poly)     # ends sit exactly on the outline
        lines.append(pts)
    if ang:
        poly = _rot(poly, x, yb - h / 2, ang)
        lines = [_rot(l, x, yb - h / 2, ang) for l in lines]
    d.polygon(poly, fill=BLACK)
    _line(d, poly, col, LW, closed=True)
    for l in lines:
        _line(d, l, col, LW * 0.7)


def _tube(d, pts, col, bw, lw, closed=False, caps=True):
    """A body bw wide drawn as two parallel lines lw wide (a wide stroke, then a black stroke inside it)."""
    _thick(d, pts, col, bw, closed, caps)
    _thick(d, pts, BLACK, bw - 2 * lw, closed, caps)


def _snake(d, x, yg, s=1.0, col=WHITE):
    """Coiled line-art snake on the ground line yg (x = middle of the coils): two coils, the head raised to the right
    with an eye and a small red forked tongue; s = scale (1 = about 410 px wide with the tail, 185 px tall)."""
    u = SS * s
    bw, lw = 38 * u, 10 * SS
    cxb, cyb, rxb, ryb = x, yg - 19 * u - 22 * u, 130 * u, 22 * u               # lower coil
    cxt, cyt, rxt, ryt = x + 6 * u, cyb - 42 * u, 98 * u, 20 * u                 # upper coil
    tl = _bez((cxb - 70 * u, cyb + 14 * u), (cxb - 128 * u, cyb + 24 * u), (cxb - 168 * u, cyb + 16 * u),
              (cxb - 186 * u, cyb - 4 * u), 20)                                   # tail: tapering out to the left
    left, right = [], []
    for i, (px, py) in enumerate(tl):
        a, b = tl[max(i - 1, 0)], tl[min(i + 1, len(tl) - 1)]
        n = math.hypot(b[0] - a[0], b[1] - a[1])
        nx, ny = -(b[1] - a[1]) / n, (b[0] - a[0]) / n
        hw = (bw / 2) * (1 - i / (len(tl) - 1)) + 2
        left.append((px + nx * hw, py + ny * hw))
        right.append((px - nx * hw, py - ny * hw))
    tail = left + right[::-1]
    d.polygon(tail, fill=BLACK)
    _line(d, tail, col, lw, closed=True)
    _tube(d, _ell(cxb, cyb, rxb, ryb, 0, 2 * math.pi, 90), col, bw, lw, closed=True)
    _tube(d, _ell(cxt, cyt, rxt, ryt, 0, 2 * math.pi, 90), col, bw, lw, closed=True)
    hx, hy = cxt + 108 * u, cyt - 72 * u
    neck = _bez((cxt + 14 * u, cyt + 12 * u), (cxt + 16 * u, cyt - 50 * u), (cxt + 50 * u, cyt - 78 * u),
                (hx - 26 * u, hy + 2 * u), 30)
    _tube(d, neck, col, bw, lw)                                     # rises from behind the front of the upper coil
    _tube(d, _ell(cxt, cyt, rxt, ryt, -0.35, math.pi + 0.35, 60), col, bw, lw, caps=False)
    tx = hx + 40 * u                                                # tongue: short line and a fork
    _line(d, [(tx - 6 * u, hy + 6 * u), (tx + 32 * u, hy + 6 * u)], RED, 7 * SS)
    for sy in (-1, 1):
        _line(d, [(tx + 32 * u, hy + 6 * u), (tx + 48 * u, hy + 6 * u + sy * 11 * u)], RED, 7 * SS)
    d.ellipse([hx - 44 * u, hy - 28 * u, hx + 44 * u, hy + 28 * u], fill=BLACK, outline=col, width=round(lw))
    _dot(d, hx + 14 * u, hy - 7 * u, 7 * u, col)


HAND_PALM = [(-150, -148), (-128, -168), (128, -168), (150, -148), (156, 20), (136, 130), (118, 200), (118, 330),
             (-118, 330), (-118, 200), (-134, 130), (-152, 20)]
HAND_FINGERS = [((-112, -110), (-142, -292), 33), ((-40, -118), (-54, -366), 36), ((34, -118), (38, -396), 37),
                ((108, -112), (126, -350), 35), ((124, 56), (262, -84), 40)]      # little, ring, middle, index, thumb
HAND_CUT, HAND_WRIST = 262, 118


def _hand(img, hx, hy, s, col):
    """Back of a LEFT hand, fingers up, thumb on the right; (hx, hy) = middle of the back of the hand, s = scale
    (1 = about 650 px tall). The wrist ends open at the bottom."""
    u = s * SS
    P = lambda x, y: (hx + x * u, hy + y * u)
    shapes = [("poly", _chaikin([P(x, y) for x, y in HAND_PALM], 2))]
    for b, tip, r in HAND_FINGERS:
        shapes.append(("capsule",) + P(*b) + P(*tip) + (r * u,))
    _outline_union(img, shapes, col)
    d = ImageDraw.Draw(img)
    yc = hy + HAND_CUT * u
    d.rectangle([hx - 150 * u, yc, hx + 150 * u, hy + 340 * u + LW], fill=BLACK)
    for sx in (-1, 1):
        _dot(d, hx + sx * HAND_WRIST * u, yc, LW / 2, col)


BOLT = [(18, -70), (-30, 8), (2, 8), (-14, 70), (34, -10), (2, -10)]


def _bolt(d, x, y, s, col, ang=0.0):
    """Lightning bolt centred on (x, y), s = scale (1 = 140 px tall)."""
    pts = _rot([(x + px * s * SS, y + py * s * SS) for px, py in BOLT], x, y, ang)
    d.polygon(pts, fill=col)
    _line(d, pts, col, 6 * SS, closed=True)


# --- 1. rocks on a screen ---------------------------------------------------------------------------------------------
def rocks2(t, dur, args, at):
    """Two different rocks on a big screen, each under a white '?'; the left rock turns yellow (chosen) at at[0]."""
    img, d = canvas()
    k0, kr, ks = fade(t, 0, 0.3), fade(t, 0.2), fade(t, at_or(at, 0, 1.6))
    sw, sh = 1100 * SS, 560 * SS
    x0, y0 = CX - sw / 2, CY - sh / 2
    col = _k(WHITE, k0)
    d.rounded_rectangle([x0, y0, x0 + sw, y0 + sh], radius=36 * SS, outline=col, width=LW)
    d.rectangle([CX - 36 * SS, y0 + sh, CX + 36 * SS, y0 + sh + 50 * SS], fill=col)          # stand
    _line(d, [(CX - 150 * SS, y0 + sh + 56 * SS), (CX + 150 * SS, y0 + sh + 56 * SS)], col)
    yg = CY + 196 * SS
    for x, kind, w, h, sel in ((CX - 255 * SS, "a", 320 * SS, 260 * SS, True),
                               (CX + 255 * SS, "b", 380 * SS, 215 * SS, False)):
        _line(d, [(x - w / 2 - 40 * SS, yg), (x + w / 2 + 40 * SS, yg)], _k(GRAY, kr), 8 * SS)
        _rock(d, x, yg, w, h, kind, _k(mix(WHITE, YEL, ks) if sel else WHITE, kr))
        _txt(d, (x, yg - h - 80 * SS), "?", 120, _k(WHITE, kr), "Bold")
    return finish(img)


# --- 2. the rock lifts: a snake, then a shock -----------------------------------------------------------------------
def rock_snake(t, dur, args, at):
    """The rock lifts and tilts at at[0], showing a coiled snake; at at[1] a yellow bolt next to the back of a hand."""
    img, d = canvas()
    t1 = at_or(at, 0, 0.5)
    t2 = at_or(at, 1, t1 + 0.7)
    k0, lift, slide = fade(t, 0, 0.3), sm((t - t1) / 0.6), sm((t - t2) / 0.5)
    gx, yg = CX - 290 * SS * slide, CY + 200 * SS
    _line(d, [(gx - 320 * SS, yg), (gx + 320 * SS, yg)], _k(GRAY, k0), 8 * SS)
    if lift > 0:
        _snake(d, gx - 10 * SS, yg, 0.85)                          # under the rock: hidden until it lifts
    _rock(d, gx, yg - 155 * SS * lift, 480 * SS, 300 * SS, "a", _k(WHITE, k0), ang=math.radians(-8) * lift)
    kh = fade(t, t2, 0.4)
    if kh > 0:
        hx, hy = CX + 390 * SS, CY + 30 * SS
        _hand(img, hx, hy, 0.6, _k(WHITE, kh))
        d = ImageDraw.Draw(img)
        kb = fade(t, t2 + 0.15, 0.3)
        if kb > 0:
            _bolt(d, hx - 170 * SS, hy - 60 * SS, 0.95 + 0.25 * kb, _k(YEL, kb), math.radians(-20))
    return finish(img)


# --- 3. electrode on the back of the left hand ------------------------------------------------------------------------
def hand_electrode(t, dur, args, at):
    """The back of a left hand with a gray electrode patch and its wire; small yellow sparks appear at at[0]."""
    img, d = canvas()
    k = fade(t, 0, 0.35)
    sc = 0.92
    hx, hy = CX - 58 * SS, CY + 79 * SS
    _hand(img, hx, hy, sc, _k(WHITE, k))
    d = ImageDraw.Draw(img)
    u = sc * SS
    px, py = hx, hy - 30 * u
    # the wire crosses the little-finger side of the hand and runs up out of the frame
    wire = _bez((px, py), (px - 130 * u, py + 10 * u), (px - 200 * u, py - 10 * u), (px - 240 * u, py - 80 * u), 24)
    wire += _bez(wire[-1], (px - 270 * u, py - 140 * u), (px - 280 * u, py - 240 * u), (px - 286 * u, py - 350 * u), 30)[1:]
    wire += _bez(wire[-1], (px - 290 * u, py - 440 * u), (px - 292 * u, py - 520 * u), (px - 292 * u, -40 * SS), 30)[1:]
    _line(d, wire, _k(WHITE, k), 6 * SS)
    s = 56 * SS
    d.rounded_rectangle([px - s, py - s, px + s, py + s], radius=16 * SS, fill=_k(GRAY, k), outline=_k(WHITE, k),
                        width=round(LW * 0.8))
    d.ellipse([px - 16 * SS, py - 16 * SS, px + 16 * SS, py + 16 * SS], outline=_k(WHITE, k), width=6 * SS)
    ks = fade(t, at_or(at, 0, 1.2), 0.35)
    if ks > 0:
        for a in (210, 246, 292, 330, 30, 72, 114, 150):            # not at 180: the wire leaves to the left
            c, sn = math.cos(math.radians(a)), math.sin(math.radians(a))
            r1, r2 = 84 * SS, 120 * SS
            _line(d, [(px + r1 * c, py + r1 * sn), (px + r2 * c, py + r2 * sn)], _k(YEL, ks), 10 * SS)
    return finish(img)


# --- 4. 320 times ---------------------------------------------------------------------------------------------------
def counter320(t, dur, args, at):
    """A big count from 1 to 320 over the first 75% of the scene (ease-out); it turns yellow when it reaches 320."""
    img, d = canvas()
    T = max(0.75 * dur, 0.5)
    u = min(max(t / T, 0.0), 1.0)
    n = 1 + round(319 * (1 - (1 - u) ** 3))
    t320 = T * (1 - (0.5 / 319) ** (1 / 3))                 # the moment the rounded count first shows 320
    k0, kd = fade(t, 0, 0.3), fade(t, t320, 0.3)
    fn, fb = font(220, "ExtraBold"), font(96, "Bold")
    wn = tab_len("320", fn)                                 # digits in equal cells: the count does not wobble
    gap = 22 * SS
    total = wn + gap + d.textlength("번", font=fb)
    xr = CX - total / 2 + wn
    top = fn.getbbox("320", anchor="ls")[1]
    yb = CY - top / 2
    tab_text(d, (xr, yb), str(n), fn, _k(mix(WHITE, YEL, kd), k0), "rs")
    d.text((xr + gap, yb), "번", font=fb, fill=_k(WHITE, k0), anchor="ls")
    return finish(img)


# --- 5. what was measured -------------------------------------------------------------------------------------------
def _eye(d, x, y, k, grow):
    col = _k(WHITE, k)
    up = [(x + 172 * SS * v, y - 102 * SS * (1 - v * v)) for v in (i / 24 - 1 for i in range(49))]
    lo = [(x + 172 * SS * v, y + 92 * SS * (1 - v * v)) for v in (i / 24 - 1 for i in range(49))]
    _line(d, up + lo[::-1][1:], col, LW, closed=True)
    r = 76 * SS
    d.ellipse([x - r, y - r, x + r, y + r], outline=col, width=round(LW * 0.8))
    _dot(d, x, y, (20 + 34 * grow) * SS, _k(YEL, k))                # the pupil (yellow) widens


def _fingertip(d, x, y, k, kd):
    col = _k(WHITE, k)
    w, top, bot = 74 * SS, y - 130 * SS, y + 140 * SS
    _line(d, [(x - w, bot)] + _ell(x, top + w, w, w, math.pi, 2 * math.pi, 30) + [(x + w, bot)], col)
    for r in (20, 38, 56):                                         # fingerprint on the pad
        rr = r * SS
        _line(d, _ell(x, top + 118 * SS, rr * 0.92, rr, math.radians(195), math.radians(345), 20),
              _k(GRAY, k), 6 * SS)
    for dy in (0, 22):                                             # joint crease
        yy = top + 196 * SS + dy * SS
        _line(d, [(x - 34 * SS, yy), (x + 34 * SS, yy)], _k(GRAY, k), 6 * SS)
    if kd > 0:                                                     # a small drop of sweat
        cx, cy, r = x + 118 * SS, top + 66 * SS, 22 * SS
        b = math.acos(1 / 1.9)
        pts = [(cx, cy - 1.9 * r)] + _ell(cx, cy, r, r, -math.pi / 2 + b, 1.5 * math.pi - b, 30)
        d.polygon(pts, fill=_k(YEL, kd))


def _scale10(d, x, y, k, pos):
    col = _k(WHITE, k)
    x0, x1 = x - 200 * SS, x + 200 * SS
    _line(d, [(x0, y), (x1, y)], col)
    for i in range(11):
        xx = x0 + (x1 - x0) * i / 10
        h = (26 if i in (0, 5, 10) else 16) * SS
        _line(d, [(xx, y - h), (xx, y + h)], col, 6 * SS)
    _txt(d, (x0, y + 72 * SS), "0", 52, _k(WHITE, k))
    _txt(d, (x1, y + 72 * SS), "10", 52, _k(WHITE, k))
    xm = x0 + (x1 - x0) * pos
    d.polygon([(xm - 28 * SS, y - 92 * SS), (xm + 28 * SS, y - 92 * SS), (xm, y - 40 * SS)], fill=_k(YEL, k))
    _line(d, [(xm - 28 * SS, y - 92 * SS), (xm + 28 * SS, y - 92 * SS), (xm, y - 40 * SS)], _k(YEL, k), 8 * SS,
          closed=True)


def measures3(t, dur, args, at):
    """Pupil size, sweat on the fingertip, a 0-10 stress score: each with its label, fading in at at[0], at[1], at[2]."""
    img, d = canvas()
    ts = _times(at, (0.3, 1.9, 3.5))
    labels = ("동공 크기", "땀 반응", "스트레스 점수")
    y, ly = CY - 20 * SS, CY + 236 * SS
    for i, t0 in enumerate(ts):
        k = fade(t, t0)
        if k <= 0:
            continue
        x = CX + (i - 1) * 560 * SS
        if i == 0:
            _eye(d, x, y, k, sm((t - t0 - 0.1) / 1.1))
        elif i == 1:
            _fingertip(d, x, y, k, fade(t, t0 + 0.3))
        else:
            _scale10(d, x, y + 20 * SS, k, 0.15 + 0.55 * sm((t - t0 - 0.1) / 0.9))
        _txt(d, (x, ly), labels[i], 60, _k(WHITE, k), "Bold")
    return finish(img)


# --- 6. 100% or 50:50 -----------------------------------------------------------------------------------------------
def choice2(t, dur, args, at):
    """Two boxes, '100%' (확실할 때) and '50 : 50' (반반일 때); args answer=True: the right box turns yellow at at[0]."""
    img, d = canvas()
    answer = bool((args or {}).get("answer"))
    if answer:                                 # follows the question screen: both boxes already there, no fade-in
        ka = kb = 1.0
        hl = fade(t, at_or(at, 0, 0.4))
    else:
        ka, kb, hl = fade(t, 0.2), fade(t, at_or(at, 0, 1.6)), 0.0
    bw, bh = 560 * SS, 400 * SS
    for i, (big, cap, k) in enumerate((("100%", "확실할 때", ka), ("50 : 50", "반반일 때", kb))):
        if k <= 0:
            continue
        x = CX + (i * 2 - 1) * 330 * SS
        if i == 0:
            line_c, big_c, cap_c = mix(WHITE, GRAY, hl), mix(WHITE, GRAY, hl), mix(WHITE, GRAY, hl)
        else:
            line_c, big_c, cap_c = mix(WHITE, YEL, hl), mix(WHITE, YEL, hl), mix(WHITE, YEL, hl)
        d.rounded_rectangle([x - bw / 2, CY - bh / 2, x + bw / 2, CY + bh / 2], radius=40 * SS, outline=_k(line_c, k),
                            width=LW)
        _txt(d, (x, CY - 46 * SS), big, 120, _k(big_c, k), "ExtraBold")
        _txt(d, (x, CY + 110 * SS), cap, 60, _k(cap_c, k), "Bold")
    return finish(img)


# --- 7. tension by probability (inverted U) -------------------------------------------------------------------------
def _axes(d, x0, x1, yt, yb, k, ytitle):
    col = _k(GRAY, k)
    _line(d, [(x0, yt), (x0, yb), (x1, yb)], col, 7 * SS)
    _txt(d, (x0, yt - 56 * SS), ytitle, 56, _k(WHITE, k), "Bold")


def _partial(pts, q):
    """The first fraction q (0..1) of a polyline, by point count."""
    if q <= 0:
        return []
    n = (len(pts) - 1) * min(q, 1.0)
    i = int(n)
    out = pts[:i + 1]
    if i < len(pts) - 1 and n > i:
        (xa, ya), (xb, yb) = pts[i], pts[i + 1]
        out = out + [(xa + (xb - xa) * (n - i), ya + (yb - ya) * (n - i))]
    return out


def curve(t, dur, args, at):
    """Inverted-U curve of tension over the chance of a snake: yellow dot on the peak at 50%, white dot at 100% at at[0]."""
    img, d = canvas()
    k = fade(t, 0, 0.3)
    x0, x1, yt, yb = CX - 560 * SS, CX + 560 * SS, CY - 250 * SS, CY + 200 * SS
    _axes(d, x0, x1, yt, yb, k, "긴장도")
    xa, xb = x0 + 70 * SS, x1 - 70 * SS
    for p, lab in ((0, "0%"), (0.5, "50%"), (1, "100%")):
        xx = xa + (xb - xa) * p
        _line(d, [(xx, yb), (xx, yb + 18 * SS)], _k(GRAY, k), 7 * SS)
        _txt(d, (xx, yb + 58 * SS), lab, 50, _k(WHITE, k))
    _txt(d, (CX, yb + 140 * SS), "뱀이 나올 확률", 58, _k(WHITE, k), "Bold")
    lo, hi = yb - 0.25 * (yb - yt), yb - 0.92 * (yb - yt)
    pts = [(xa + (xb - xa) * i / 80, lo + (hi - lo) * math.sin(math.pi * i / 80)) for i in range(81)]
    q = sm((t - 0.3) / 1.5)
    seg = _partial(pts, q)
    if len(seg) > 1:
        _line(d, seg, WHITE)
    kp = fade(t, 1.05, 0.3)                                        # the drawing passes the peak at 1.05 s
    if kp > 0:
        _dot(d, CX, hi, 32 * SS, BLACK)
        _dot(d, CX, hi, (16 + 8 * kp) * SS, _k(YEL, kp))
    ke = fade(t, max(at_or(at, 0, 2.6), 1.9))
    if ke > 0:
        _dot(d, xb, lo, 28 * SS, BLACK)
        _dot(d, xb, lo, 18 * SS, _k(WHITE, ke))
    return finish(img)


# --- 8. three scores drop -------------------------------------------------------------------------------------------
def _down_arrow(d, x, top, col, s=1.0):
    """A thick down arrow from top; s scales it (v4, 2026-10-25: smaller over a photo with centre subtitles)."""
    sw, L, hw, hh = 64 * SS * s, 140 * SS * s, 160 * SS * s, 110 * SS * s
    pts = [(x - sw / 2, top), (x + sw / 2, top), (x + sw / 2, top + L), (x + hw / 2, top + L), (x, top + L + hh),
           (x - hw / 2, top + L), (x - sw / 2, top + L)]
    d.polygon(pts, fill=col)
    _line(d, pts, col, round(10 * SS * s), closed=True)


def drops3(t, dur, args, at):
    """소속감 / 통제감 / 자존감, each getting a thick down arrow that slides down at at[0..2]; '절반 이하' under the first."""
    img, d = canvas()
    k0 = fade(t, 0, 0.3)
    ts = _times(at, (0.4, 2.4, 4.0))
    # v4 (2026-10-25): over a photo with the subtitles in the middle (render.py "icon_overlay"), "lift" (output px)
    # moves the words and arrows up, "drop" (output px) shortens the arrows' slide and "arrow" scales the arrows, so
    # nothing is drawn where the centre subtitles are; "note": False leaves out '절반 이하' ("note_y", output px, moves it)
    lift, drop = args.get("lift", 0) * SS, args.get("drop", 96) * SS
    for i, (lab, t0) in enumerate(zip(("소속감", "통제감", "자존감"), ts)):
        x = CX + (i - 1) * 500 * SS
        _txt(d, (x, CY - 230 * SS - lift), lab, 72, _k(WHITE, k0), "ExtraBold")
        ka = fade(t, t0)
        if ka > 0:
            _down_arrow(d, x, CY - 150 * SS - lift + drop * sm((t - t0) / 0.7), _k(WHITE, ka), args.get("arrow", 1.0))
        if i == 0 and args.get("note", True):
            kc = fade(t, t0 + 0.55)
            if kc > 0:
                ny = args["note_y"] * SS if "note_y" in args else CY + 266 * SS
                _txt(d, (x, ny), "절반 이하", 60, _k(YEL, kc), "Bold")
    return finish(img)


# --- 9. one in five -------------------------------------------------------------------------------------------------
def _person(d, x, y, col, lw=LW):
    """Head circle and shoulder arc; (x, y) = centre of the head."""
    r = 58 * SS
    d.ellipse([x - r, y - r, x + r, y + r], outline=col, width=lw)
    _line(d, _ell(x, y + 210 * SS, 112 * SS, 128 * SS, math.radians(192), math.radians(348), 40), col, lw)


def _alarm_lamp(d, x, yb, k):
    """Small red alarm lamp standing on yb: a dome on a base with three short rays."""
    r = 40 * SS
    top = yb - 16 * SS - 52 * SS
    d.rounded_rectangle([x - r, top, x + r, yb - 16 * SS], radius=r, corners=(True, True, False, False),
                        fill=_k(RED, k), outline=_k(WHITE, k), width=7 * SS)
    d.rounded_rectangle([x - 56 * SS, yb - 16 * SS, x + 56 * SS, yb], radius=7 * SS, fill=_k(WHITE, k))
    cy = top + r
    for a in (-135, -90, -45):
        c, s = math.cos(math.radians(a)), math.sin(math.radians(a))
        _line(d, [(x + 62 * SS * c, cy + 62 * SS * s), (x + 90 * SS * c, cy + 90 * SS * s)], _k(RED, k), 8 * SS)


def people5(t, dur, args, at):
    """Five people; at at[0] the 4th turns yellow under a small red alarm lamp and '5명 중 1명' fades in."""
    img, d = canvas()
    k0, k1 = fade(t, 0, 0.35), fade(t, at_or(at, 0, 1.0))
    y, sp = CY - 64 * SS, 272 * SS
    for i in range(5):
        x = CX + (i - 2) * sp
        _person(d, x, y, _k(mix(WHITE, YEL, k1) if i == 3 else WHITE, k0))
    if k1 > 0:
        _alarm_lamp(d, CX + sp, y - 58 * SS - 26 * SS + 14 * SS * (1 - k1), k1)
        if args.get("caption", True):       # v4 (2026-10-25, owner): "5명 중 1명이라는 자막 없애줘"
            _txt(d, (CX, CY + 254 * SS), "5명 중 1명", 72, _k(WHITE, k1), "ExtraBold")
    return finish(img)


# --- 10. attachment anxiety by age ------------------------------------------------------------------------------------
def graph_down(t, dur, args, at):
    """Attachment anxiety over age (10대 to 70대): a gently falling line drawn from 0.3 s to 2.0 s, ending in a yellow dot."""
    img, d = canvas()
    k = fade(t, 0, 0.3)
    x0, x1, yt, yb = CX - 560 * SS, CX + 560 * SS, CY - 250 * SS, CY + 200 * SS
    _axes(d, x0, x1, yt, yb, k, "애착 불안")
    xa, xb = x0 + 70 * SS, x1 - 70 * SS
    for xx, lab in ((xa, "10대"), (xb, "70대")):
        _line(d, [(xx, yb), (xx, yb + 18 * SS)], _k(GRAY, k), 7 * SS)
        _txt(d, (xx, yb + 58 * SS), lab, 50, _k(WHITE, k))
    _txt(d, (CX, yb + 140 * SS), "나이", 58, _k(WHITE, k), "Bold")
    hi, lo = yb - 0.84 * (yb - yt), yb - 0.24 * (yb - yt)

    def yv(p):
        return hi + (lo - hi) * (1 - (1 - p) ** 1.35)
    pts = [(xa + (xb - xa) * i / 80, yv(i / 80)) for i in range(81)]
    seg = _partial(pts, sm((t - 0.3) / 1.7))
    if len(seg) > 1:
        _line(d, seg, WHITE)
    ke = fade(t, 2.0, 0.3)
    if ke > 0:
        _dot(d, xb, lo, 32 * SS, BLACK)
        _dot(d, xb, lo, (16 + 8 * ke) * SS, _k(YEL, ke))
    return finish(img)


# --- 11-12. the spider study ----------------------------------------------------------------------------------------
# right-side legs in body radii: start (inside the body), knee, foot; each leg is a smooth arch through the knee
SPIDER_LEGS = [((0.55, -0.75), (1.20, -1.42), (2.00, -1.15)), ((0.85, -0.35), (1.70, -0.80), (2.40, -0.10)),
               ((0.90, 0.15), (1.85, -0.10), (2.45, 0.80)), ((0.65, 0.65), (1.55, 0.50), (2.00, 1.40))]


def _spider(d, x, y, s, col):
    """Simple friendly spider: round body with two eyes and 8 arched legs; (x, y) = body centre, s = 1: ~320 px wide."""
    R = 64 * s * SS
    for sx in (-1, 1):
        for leg in SPIDER_LEGS:
            (x0, y0), (xk, yk), (x2, y2) = [(x + sx * R * a, y + R * b) for a, b in leg]
            cx, cy = 2 * xk - (x0 + x2) / 2, 2 * yk - (y0 + y2) / 2      # quadratic curve through the knee
            _line(d, [((1 - u) ** 2 * x0 + 2 * (1 - u) * u * cx + u * u * x2, (1 - u) ** 2 * y0 + 2 * (1 - u) * u * cy + u * u * y2)
                      for u in (i / 20 for i in range(21))], col)
    d.ellipse([x - R, y - R, x + R, y + R], fill=BLACK, outline=col, width=LW)
    for sx in (-1, 1):
        _dot(d, x + sx * R * 0.34, y - R * 0.12, R * 0.13, col)


def spider_title(t, dur, args, at):
    """Spider icon on the left; '2012년' (yellow) at 0.2 s and '거미를 무서워하는 88명' at at[0] on the right."""
    img, d = canvas()
    _spider(d, CX - 400 * SS, CY, 1.0, _k(WHITE, fade(t, 0, 0.45)))
    tx = CX - 150 * SS
    _txt(d, (tx, CY - 10 * SS), "2012년", 150, _k(YEL, fade(t, 0.2, 0.45)), "ExtraBold", "ls")
    _txt(d, (tx + 6 * SS, CY + 92 * SS), "거미를 무서워하는 88명", 64, _k(WHITE, fade(t, at_or(at, 0, 1.0), 0.45)),
         "ExtraBold", "ls")
    return finish(img)


def _seated(img, x, ys, col):
    """Side view of a person sitting on a chair, facing left; x = middle of the seat, ys = seat height."""
    d = ImageDraw.Draw(img)
    u = SS
    sl, sr, fl = x - 120 * u, x + 92 * u, ys + 172 * u                                   # chair
    _line(d, [(sr + 8 * u, ys - 236 * u), (sr, ys), (sl, ys)], col)
    _line(d, [(sl + 14 * u, ys), (sl + 14 * u, fl)], col)
    _line(d, [(sr - 6 * u, ys), (sr - 6 * u, fl)], col)
    hip, knee, ankle = (x + 44 * u, ys - 46 * u), (x - 128 * u, ys - 50 * u), (x - 150 * u, ys + 150 * u)
    shapes = [("capsule", hip[0], hip[1], x + 62 * u, ys - 228 * u, 46 * u),
              ("capsule", hip[0], hip[1], knee[0], knee[1], 42 * u),
              ("capsule", knee[0], knee[1], ankle[0], ankle[1], 34 * u),
              ("capsule", ankle[0] + 8 * u, ankle[1], ankle[0] - 52 * u, ankle[1] + 8 * u, 24 * u)]
    _outline_union(img, shapes, col)
    d = ImageDraw.Draw(img)
    r = 56 * u
    hx, hy = x + 48 * u, ys - 336 * u
    d.ellipse([hx - r, hy - r, hx + r, hy + r], fill=BLACK, outline=col, width=LW)
    return x - 150 * u - 34 * u - 6 * u                                 # front of the knee (leftmost body point at knee height)


def spider_60(t, dur, args, at):
    """Spider on the left, a seated person on the right, and a '60cm' dimension line between them at at[0]."""
    img, d = canvas()
    k = fade(t, 0, 0.4)
    sx, sy = CX - 470 * SS, CY + 30 * SS
    _spider(d, sx, sy, 0.95, _k(WHITE, k))
    front = _seated(img, CX + 470 * SS, CY + 70 * SS, _k(WHITE, k))
    d = ImageDraw.Draw(img)
    km = fade(t, at_or(at, 0, 0.8), 0.4)
    if km > 0:
        xa, xb, y = sx + 190 * SS, front - 40 * SS, sy
        g = sm((t - at_or(at, 0, 0.8)) / 0.4)
        xm, half = (xa + xb) / 2, (xb - xa) / 2 * (0.3 + 0.7 * g)
        col = _k(WHITE, km)
        _line(d, [(xm - half, y), (xm + half, y)], col, 7 * SS)
        for xx in (xm - half, xm + half):
            _line(d, [(xx, y - 30 * SS), (xx, y + 30 * SS)], col, 7 * SS)
        _txt(d, (xm, y - 84 * SS), "60cm", 80, _k(YEL, km), "ExtraBold")
    return finish(img)


# --- 13. three groups -----------------------------------------------------------------------------------------------
GROUPS = ("이름 붙이기", "달래기", "딴생각")


def _bubble(img, x, y, w, h, col):
    """Speech bubble outline centred on (x, y) with a tail at the bottom left."""
    x0, y0, x1, y1 = x - w / 2, y - h / 2, x + w / 2, y + h / 2
    tail = [(x - w * 0.30, y1 - 60 * SS), (x - w * 0.08, y1 - 60 * SS), (x - w * 0.34, y1 + 66 * SS)]
    _outline_union(img, [("rrect", x0, y0, x1, y1, 64 * SS), ("poly", tail)], col)


def groups3(t, dur, args, at):
    """Three numbered speech bubbles (이름 붙이기 / 달래기 / 딴생각); args mode intro | focus (i) | answer (at[0])."""
    img, d = canvas()
    args = args or {}
    mode = args.get("mode", "intro")
    w, h, y = 440 * SS, 210 * SS, CY + 30 * SS
    for i, lab in enumerate(GROUPS):
        x = CX + (i - 1) * 520 * SS
        k, col = 1.0, WHITE
        if mode == "intro":
            k = fade(t, (0.2, 0.6, 1.0)[i])
        elif mode == "focus":
            col = YEL if i == int(args.get("i", 0)) else GRAY
        elif mode == "answer":
            u = fade(t, at_or(at, 0, 0.6))
            col = mix(WHITE, YEL if i == 0 else GRAY, u)
        if k <= 0:
            continue
        c = _k(col, k)
        _bubble(img, x, y, w, h, c)
        d = ImageDraw.Draw(img)
        _txt(d, (x, y), lab, 52, c, "Bold")
        _txt(d, (x, y - h / 2 - 62 * SS), str(i + 1), 60, c, "ExtraBold")
    return finish(img)


# --- 14. the alarm calms down ---------------------------------------------------------------------------------------
_GLOW = {}


def siren_calm(t, dur, args, at):
    """Red warning lamp pulsing slowly (about 1 Hz); from at[0] the pulse slows and within 1.2 s the lamp goes unlit gray."""
    img, d = canvas()
    ta, T, f0, f1 = at_or(at, 0, 1.4), 1.2, 1.0, 0.35
    if t <= ta:
        ph = f0 * t
    else:                                     # the phase is the integral of a frequency easing from f0 to f1
        u = min((t - ta) / T, 1.0)
        ph = f0 * ta + T * (f0 * u + (f1 - f0) * (u ** 3 - u ** 4 / 2)) + f1 * max(t - ta - T, 0)
    p = 0.5 - 0.5 * math.cos(2 * math.pi * ph)
    on, calm = fade(t, 0, 0.3), sm((t - ta) / T)
    lit = on * (0.3 + 0.7 * p) * (1 - calm)
    r = 125 * SS
    top, base_y = CY - r * 1.05, CY + 85 * SS
    if lit > 0.005:
        if "g" not in _GLOW:
            g = Image.new("L", img.size, 0)
            ImageDraw.Draw(g).ellipse([CX - r * 1.9, top - r * 0.5, CX + r * 1.9, base_y + r * 0.5], fill=190)
            _GLOW["g"] = g.filter(ImageFilter.GaussianBlur(85 * SS))
        img = Image.composite(Image.new("RGB", img.size, RED), img, _GLOW["g"].point(lambda v: round(v * lit)))
        d = ImageDraw.Draw(img)
    fill = mix(mix((60, 8, 10), RED, on * (0.3 + 0.7 * p)), UNLIT, calm)
    d.rounded_rectangle([CX - r, top, CX + r, base_y], radius=r, corners=(True, True, False, False),
                        fill=_k(fill, on), outline=_k(WHITE, on), width=LW)
    d.arc([CX - r * 0.66, top + r * 0.32, CX + r * 0.30, top + r * 1.30], start=195, end=250,
          fill=_k(mix(mix((150, 150, 150), WHITE, p), (150, 150, 150), calm), on), width=round(LW * 0.8))
    d.rounded_rectangle([CX - r * 1.42, base_y + 4 * SS, CX + r * 1.42, base_y + 64 * SS], radius=16 * SS,
                        fill=_k(WHITE, on))
    kr = on * (0.45 + 0.55 * p) * (1 - calm)
    if kr > 0.01:
        rc = (CX, top + r * 0.95)
        for sx in (-1, 1):
            for dy in (-0.42, 0.0, 0.42):
                vx, vy = sx * math.sqrt(1 - dy * dy), dy
                r1, r2 = r * 1.5, r * (1.5 + (0.22 + 0.30 * p) * (1 - calm))
                if r2 - r1 > 2:
                    d.line([(rc[0] + vx * r1, rc[1] + vy * r1), (rc[0] + vx * r2, rc[1] + vy * r2)],
                           fill=_k(RED, kr), width=LW)
    return finish(img)


KINDS = {
    "rocks2": rocks2, "rock_snake": rock_snake, "hand_electrode": hand_electrode, "counter320": counter320,
    "measures3": measures3, "choice2": choice2, "curve": curve, "drops3": drops3, "people5": people5,
    "graph_down": graph_down, "spider_title": spider_title, "spider_60": spider_60, "groups3": groups3,
    "siren_calm": siren_calm,
}
