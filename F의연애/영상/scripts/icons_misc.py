# Misc icon screens for F의 연애 01 (2026-10-24): same look as icons.py (black background, white line art, gray = off,
# yellow #F2C94C = the key element, red = warning only), drawn at 2x on canvas() and downsampled by finish().
# Every function: fn(t, dur, args, at) -> 1920x1080 RGB image. t = seconds since the scene started, dur = scene length,
# args = dict from the scene spec (may be {}), at = voice start times in seconds from the scene start (may be []).
# Rules kept here: text >= 40 px, everything inside x 120..1800 and above y 860 (output px), no shake/flicker/blinking,
# only smooth fades, pops and growth; schematic charts carry no numbers.
from fy_common import *
import math
from PIL import Image, ImageDraw, ImageFilter

BLACK = (0, 0, 0)
LCD_BG, LCD_FG = (150, 170, 140), (34, 44, 34)          # monochrome phone screen and its dark text


# --- small helpers ----------------------------------------------------------------------------------------------
def _args(args):
    return args if isinstance(args, dict) else {}


def _c(col, k):
    """Colour faded in from the black background (k 0..1)."""
    return mix(BLACK, col, k)


def _px(v):
    """Font size rounded to half output pixels (keeps the font cache small during pops)."""
    return round(v * 2) / 2


def _ctext(d, xy, s, px, fill, weight="SemiBold", ha="m", f=None, features=None):
    """Text whose Hangul body is vertically centred on y (ha = l/m/r horizontal anchor)."""
    f = f or font(px, weight)
    _, top, _, bot = f.getbbox("한", anchor="ls")
    d.text((xy[0], xy[1] - (top + bot) / 2), s, font=f, fill=fill, anchor=ha + "s", features=features)


def _ink(d, xy, s, f, fill, features=None):
    """Text whose ink box is centred exactly on xy (single glyphs such as '?' or a digit)."""
    l, t_, r_, b = f.getbbox(s, anchor="ls", features=features)
    d.text((xy[0] - (l + r_) / 2, xy[1] - (t_ + b) / 2), s, font=f, fill=fill, anchor="ls", features=features)


def _cap_line(d, a, b, col, w):
    """Straight line with round caps."""
    w = max(1, round(w))
    d.line([a, b], fill=col, width=w)
    r = w / 2
    for x, y in (a, b):
        d.ellipse([x - r, y - r, x + r, y + r], fill=col)


def _poly(d, pts, col, w, closed=False, caps=True):
    """Polyline with rounded joints (and round caps when open). A round brush is stamped on every vertex, which also
    fills the hairline notches PIL leaves between short segments of a wide curved line."""
    if len(pts) < 2:
        return
    w = max(1, round(w))
    if closed:
        pts = list(pts) + [pts[0], pts[1]]
    d.line(pts, fill=col, width=w, joint="curve")
    r = w / 2
    for x, y in (pts if (caps or closed) else pts[1:-1]):
        d.ellipse([x - r, y - r, x + r, y + r], fill=col)


def _bez(p0, p1, p2, p3, n=28):
    out = []
    for i in range(n + 1):
        u = i / n
        a, b, c, e = (1 - u) ** 3, 3 * (1 - u) ** 2 * u, 3 * (1 - u) * u * u, u ** 3
        out.append((a * p0[0] + b * p1[0] + c * p2[0] + e * p3[0], a * p0[1] + b * p1[1] + c * p2[1] + e * p3[1]))
    return out


def _partial(pts, q):
    """The first fraction q (0..1) of a polyline, by length (for strokes that draw themselves)."""
    if q <= 0 or len(pts) < 2:
        return []
    segs = [math.dist(a, b) for a, b in zip(pts, pts[1:])]
    goal = sum(segs) * min(q, 1.0)
    out = [pts[0]]
    for (a, b), L in zip(zip(pts, pts[1:]), segs):
        if goal >= L:
            out.append(b)
            goal -= L
        else:
            f = goal / L if L else 0
            out.append((a[0] + (b[0] - a[0]) * f, a[1] + (b[1] - a[1]) * f))
            break
    return out


def _arrow(d, x0, y, x1, col, q=1.0, w=12 * SS, head=30 * SS):
    """Horizontal arrow from x0 to x1 that grows with q (0..1)."""
    if q <= 0:
        return
    xe = x0 + (x1 - x0) * q
    if xe - head * 0.9 > x0:
        _cap_line(d, (x0, y), (xe - head * 0.9, y), col, w)
    d.polygon([(xe, y), (xe - head * 1.25, y - head * 0.85), (xe - head * 1.25, y + head * 0.85)], fill=col)


def _wrap(s, f, maxw):
    """Word wrap (spaces; long words broken by characters). Returns (lines, seps): seps[i] = characters of the
    source dropped after line i (the space or newline at the break), so typing can count them."""
    lines, seps = [], []
    paras = str(s).split("\n")
    for pi, para in enumerate(paras):
        cur = None
        for word in para.split(" "):
            trial = word if cur is None else cur + " " + word
            if f.getlength(trial) <= maxw:
                cur = trial
                continue
            if cur is not None:
                lines.append(cur)
                seps.append(1)
            while f.getlength(word) > maxw and len(word) > 1:
                i = len(word) - 1
                while i > 1 and f.getlength(word[:i]) > maxw:
                    i -= 1
                lines.append(word[:i])
                seps.append(0)
                word = word[i:]
            cur = word
        lines.append(cur or "")
        seps.append(1 if pi < len(paras) - 1 else 0)
    return lines, seps


def _fit(s, px, weight, maxw, max_lines=2, min_px=46):
    """Largest font size (from px down to min_px) at which s wraps into max_lines lines."""
    size = px
    while True:
        f = font(size, weight)
        lines, _ = _wrap(s, f, maxw)
        if len(lines) <= max_lines or size <= min_px:
            return f, size, lines
        size -= 2


_glows = {}


def _glow(img, box, colour, strength, blur=60):
    """fy_common.glow with the blurred mask cached (the box is static in these screens, only strength changes)."""
    if strength <= 0:
        return img
    key = (tuple(round(v) for v in box), blur)
    if key not in _glows:
        m = Image.new("L", img.size, 0)
        ImageDraw.Draw(m).ellipse(box, fill=150)
        _glows[key] = m.filter(ImageFilter.GaussianBlur(blur * SS))
    m = _glows[key]
    if strength < 1:
        m = m.point(lambda v: round(v * strength))
    return Image.composite(Image.new("RGB", img.size, colour), img, m)


def _phone(d, x, y, pw, ph, col):
    """Same phone outline as icons.phone_shape, in a given colour."""
    d.rounded_rectangle([x - pw / 2, y - ph / 2, x + pw / 2, y + ph / 2], radius=pw * 0.16, outline=col, width=LW)
    d.rounded_rectangle([x - pw * 0.12, y - ph / 2 + 26 * SS, x + pw * 0.12, y - ph / 2 + 40 * SS], radius=6 * SS,
                        fill=col)


def _bell_outline(x, y, s):
    """Closed outline of a bell; (x, y) = body centre, s = canvas px per output px of the 380 px tall master."""
    P = lambda u, v: (x + u * s, y + v * s)
    left = _bez((-176, 112), (-130, 88), (-118, 30), (-118, -46))
    dome = [(118 * math.cos(math.radians(a)), -46 - 118 * math.sin(math.radians(a))) for a in range(180, -1, -6)]
    right = [(-u, v) for u, v in reversed(left)]
    return [P(u, v) for u, v in left + dome[1:] + right[1:]]


# --- 1. brain ---------------------------------------------------------------------------------------------------
def _brain(d, cx, cy, A, B, col, w):
    """Brain seen from above: scalloped outline, the split between the two halves, three folds on each side."""
    m, amp = 7, 0.065
    step = math.pi / m

    def edge(th, f=1.0):                        # contour point (normalised), lobes meet in cusps every pi/m
        r = (1 - amp + amp * abs(math.sin(m * (th + math.pi / 2))) ** 0.8) * f
        return r * math.cos(th), r * math.sin(th)

    for k in range(2 * m):                      # each lobe its own round-capped stroke: clean cusps, no spikes
        a0 = -math.pi / 2 + k * step
        _poly(d, [(cx + A * u, cy + B * v) for u, v in (edge(a0 + step * i / 40) for i in range(41))], col, w)
    _cap_line(d, (cx, cy - B * (1 - amp)), (cx, cy - B * 0.60), col, w)       # split between the halves
    _cap_line(d, (cx, cy + B * (1 - amp)), (cx, cy + B * 0.66), col, w)
    folds = [(11, (-0.70, -0.30), (-0.52, -0.42), (-0.44, -0.66)),        # (cusp index, two controls, end)
             (10, (-0.74, 0.04), (-0.66, 0.30), (-0.44, 0.16)),
             (9, (-0.60, 0.44), (-0.46, 0.50), (-0.36, 0.34))]
    for k, c1, c2, e in folds:
        s0 = edge(-math.pi / 2 + k * step, 0.985)
        for sx in (1, -1):
            q = [(cx + sx * A * u, cy + B * v) for u, v in (s0, c1, c2, e)]
            _poly(d, _bez(*q), col, w)


def brain_q(t, dur, args, at):
    """Brain with a big gray '?'; at at[0] (1.2 s) a soft red glow, the '?' turns red and a warning triangle appears."""
    img, d = canvas()
    t1 = at_or(at, 0, 1.2)
    k0, k1, k2 = fade(t, 0, 0.35), fade(t, t1, 0.4), fade(t, t1 + 0.1, 0.35)
    cx, cy = CX - 40 * SS, CY + 10 * SS
    A, B = 370 * SS, 300 * SS
    img = _glow(img, [cx - A * 0.85, cy - B * 0.78, cx + A * 0.85, cy + B * 0.78], RED, 0.55 * k1, blur=60)
    d = ImageDraw.Draw(img)
    _brain(d, cx, cy, A, B, _c(WHITE, k0), LW)
    _ink(d, (cx, cy + 6 * SS), "?", font(300, "ExtraBold"), _c(mix(GRAY, RED, k1), k0))
    if k2 > 0:                                                    # warning triangle, upper right
        s = (0.8 + 0.2 * k2) * 190 * SS
        tx, ty = cx + A + 110 * SS, cy - B * 0.80
        tri = [(tx, ty - s * 0.58), (tx + s / 2, ty + s * 0.29), (tx - s / 2, ty + s * 0.29)]
        d.polygon(tri, fill=BLACK)
        _poly(d, tri, _c(RED, k2), LW, closed=True)
        _ink(d, (tx, ty + s * 0.07), "!", font(_px(100 * s / (190 * SS)), "ExtraBold"), _c(RED, k2))
    return finish(img)


# --- 2. running clock ---------------------------------------------------------------------------------------------
def _time_label(minutes, night=False):
    mins = int(round(minutes)) % (24 * 60)
    hh, mm = divmod(mins, 60)
    word = "오전" if hh < 12 else ("밤" if night and hh >= 21 else "오후")
    return f"{word} {hh % 12 or 12}:{mm:02d}"


def clock_run(t, dur, args, at):
    """Clock running args['from'] -> args['to'] (24 h, 19.0 -> 23.0) with a '오후 7:00' label; the rim turns red."""
    args = _args(args)
    h0, h1 = float(args.get("from", 19.0)), float(args.get("to", 23.0))
    p = min(max(t / max(0.85 * dur, 0.5), 0.0), 1.0)
    h = h0 + (h1 - h0) * sm(p)
    img, d = canvas()
    k0 = fade(t, 0, 0.3)
    w = _c(WHITE, k0)
    r, cx, cy = 220 * SS, CX, CY - 40 * SS
    d.ellipse([cx - r, cy - r, cx + r, cy + r], outline=_c(mix(WHITE, RED, sm((p - 0.6) / 0.4)), k0), width=LW)
    for k in range(12):
        a = math.radians(k * 30 - 90)
        r1 = r * (0.78 if k % 3 == 0 else 0.86)
        d.line([(cx + r1 * math.cos(a), cy + r1 * math.sin(a)), (cx + r * 0.93 * math.cos(a), cy + r * 0.93 * math.sin(a))],
               fill=w, width=(9 if k % 3 == 0 else 6) * SS)
    ah, am = math.radians(-90 + (h % 12) * 30), math.radians(-90 + (h % 1) * 360)
    _cap_line(d, (cx, cy), (cx + r * 0.5 * math.cos(ah), cy + r * 0.5 * math.sin(ah)), w, 16 * SS)
    _cap_line(d, (cx, cy), (cx + r * 0.75 * math.cos(am), cy + r * 0.75 * math.sin(am)), w, 10 * SS)
    d.ellipse([cx - 16 * SS, cy - 16 * SS, cx + 16 * SS, cy + 16 * SS], fill=w)
    step = 5 if abs(h1 - h0) <= 3 else 10                        # label ticks in 5- or 10-minute steps
    q = (h - h0) * 60 / step
    q = math.floor(q + 1e-6) if q >= 0 else math.ceil(q - 1e-6)
    shown = h1 * 60 if p >= 1 else h0 * 60 + q * step
    _ctext(d, (cx, cy + r + 92 * SS), _time_label(shown, bool(args.get("night_word"))), 64, w, weight="Bold",
           features=["tnum"])
    return finish(img)


# --- 3. three ways ------------------------------------------------------------------------------------------------
def three(t, dur, args, at):
    """Caption (args['label'], default '3가지 방법') and three numbered circles popping in at 0.2, 0.55, 0.9 s."""
    args = _args(args)
    img, d = canvas()
    _ctext(d, (CX, 250 * SS), str(args.get("label", "3가지 방법")), 64, _c(WHITE, fade(t, 0.1, 0.35)), weight="Bold")
    for i, t0 in enumerate((0.2, 0.55, 0.9)):
        k = fade(t, t0, 0.35)
        if k <= 0:
            continue
        s = 0.8 + 0.2 * k
        x, y, r = CX + (i - 1) * 380 * SS, 540 * SS, 130 * SS * s
        d.ellipse([x - r, y - r, x + r, y + r], outline=_c(WHITE, k), width=LW)
        _ink(d, (x, y), str(i + 1), font(_px(120 * s), "ExtraBold"), _c(YEL, k))
    return finish(img)


# --- 4. notifications off -------------------------------------------------------------------------------------------
def bell_off(t, dur, args, at):
    """Notification bell with a badge; at at[0] (0.8 s) a red slash draws across it and '알림 끄기' fades in."""
    img, d = canvas()
    t1 = at_or(at, 0, 0.8)
    k0, ks = fade(t, 0, 0.3), fade(t, t1, 0.35)
    w = _c(WHITE, k0)
    bx, by, s = CX, CY - 40 * SS, 1.2 * SS
    _poly(d, _bell_outline(bx, by, s), w, LW, closed=True)
    _poly(d, [(bx - 196 * s, by + 112 * s), (bx + 196 * s, by + 112 * s)], w, LW)            # rim
    d.arc([bx - 44 * s, by + 112 * s - 44 * s, bx + 44 * s, by + 112 * s + 44 * s], start=0, end=180, fill=w, width=LW)
    d.ellipse([bx - 22 * s, by - 186 * s, bx + 22 * s, by - 142 * s], fill=w)                   # knob
    ex, ey, er = bx + 120 * s, by - 150 * s, 44 * s                                             # badge
    d.ellipse([ex - er - 11 * s, ey - er - 11 * s, ex + er + 11 * s, ey + er + 11 * s], fill=BLACK)
    d.ellipse([ex - er, ey - er, ex + er, ey + er], fill=_c(mix(YEL, GRAY, ks), k0))
    if ks > 0:                                                                                  # the slash
        a, b = (bx - 215 * s, by - 225 * s), (bx + 215 * s, by + 205 * s)
        e = (a[0] + (b[0] - a[0]) * ks, a[1] + (b[1] - a[1]) * ks)
        _cap_line(d, a, e, BLACK, 60 * SS)
        _cap_line(d, a, e, RED, 28 * SS)
        _ctext(d, (bx, by + 335 * SS), "알림 끄기", 56, _c(WHITE, ks), weight="Bold")
    return finish(img)


# --- 5. three clocks with notification times --------------------------------------------------------------------------
def _mini_clock(d, x, y, r, hour, col):
    d.ellipse([x - r, y - r, x + r, y + r], outline=col, width=10 * SS)
    for j in range(12):
        a = math.radians(j * 30 - 90)
        r1 = r * (0.76 if j % 3 == 0 else 0.85)
        d.line([(x + r1 * math.cos(a), y + r1 * math.sin(a)), (x + r * 0.92 * math.cos(a), y + r * 0.92 * math.sin(a))],
               fill=col, width=(7 if j % 3 == 0 else 4) * SS)
    ah = math.radians(-90 + (hour % 12) * 30)
    _cap_line(d, (x, y), (x + r * 0.5 * math.cos(ah), y + r * 0.5 * math.sin(ah)), col, 13 * SS)
    _cap_line(d, (x, y), (x, y - r * 0.72), col, 9 * SS)
    d.ellipse([x - 12 * SS, y - 12 * SS, x + 12 * SS, y + 12 * SS], fill=col)


def _bell_badge(d, x, y, r, col):
    """Yellow round badge with a small black bell in it."""
    d.ellipse([x - r - 10 * SS, y - r - 10 * SS, x + r + 10 * SS, y + r + 10 * SS], fill=BLACK)
    d.ellipse([x - r, y - r, x + r, y + r], fill=col)
    s = r / (300 * SS) * SS
    bb = _bell_outline(x, y + 12 * s, s)
    d.polygon(bb, fill=BLACK)
    d.rounded_rectangle([x - 190 * s, y + 104 * s, x + 190 * s, y + 140 * s], radius=18 * s, fill=BLACK)
    d.ellipse([x - 44 * s, y + 112 * s, x + 44 * s, y + 200 * s], fill=BLACK)
    d.ellipse([x - 26 * s, y - 196 * s, x + 26 * s, y - 144 * s], fill=BLACK)


def clocks3(t, dur, args, at):
    """Three clocks at 9:00, 3:00 and 9:00 (오전 9시 / 오후 3시 / 밤 9시) with yellow bell badges, in at at[0..2]."""
    img, d = canvas()
    for i, (hour, label) in enumerate([(9, "오전 9시"), (3, "오후 3시"), (9, "밤 9시")]):
        k = fade(t, at_or(at, i, (0.2, 0.9, 1.6)[i]), 0.35)
        if k <= 0:
            continue
        s = 0.85 + 0.15 * k
        x, y, r = CX + (i - 1) * 500 * SS, CY - 30 * SS, 150 * SS * s
        _mini_clock(d, x, y, r, hour, _c(WHITE, k))
        _bell_badge(d, x + r * 0.76, y - r * 0.76, 48 * SS * s, _c(YEL, k))
        _ctext(d, (x, CY - 30 * SS + 150 * SS + 82 * SS), label, 52, _c(WHITE, k), weight="Bold")
    return finish(img)


# --- 6. if-then rule ------------------------------------------------------------------------------------------------
def _rule_box(d, x, y, bw, bh, tag, body, col, tagcol, k):
    if k <= 0:
        return
    d.rounded_rectangle([x - bw / 2, y - bh / 2, x + bw / 2, y + bh / 2], radius=36 * SS, outline=_c(col, k), width=10 * SS)
    f, size, lines = _fit(body, 56, "Bold", bw - 96 * SS)
    lh = size * 1.32 * SS
    y0 = y + 14 * SS - (len(lines) - 1) * lh / 2
    for i, ln in enumerate(lines):
        _ctext(d, (x, y0 + i * lh), ln, size, _c(WHITE, k), f=f)
    tf = font(44, "Bold")
    tw = tf.getlength(tag) + 56 * SS
    d.rounded_rectangle([x - tw / 2, y - bh / 2 - 36 * SS, x + tw / 2, y - bh / 2 + 36 * SS], radius=36 * SS,
                        fill=BLACK, outline=_c(tagcol, k), width=6 * SS)
    _ctext(d, (x, y - bh / 2), tag, 44, _c(tagcol, k), f=tf)


def ifthen(t, dur, args, at):
    """'만약' box (args['if']) -> arrow -> yellow '그러면' box (args['then']); left at 0.2 s, the rest at at[0] (1.0 s)."""
    args = _args(args)
    img, d = canvas()
    t1 = at_or(at, 0, 1.0)
    bw, bh, y = 600 * SS, 300 * SS, CY + 10 * SS
    xl, xr = CX - 440 * SS, CX + 440 * SS
    _rule_box(d, xl, y, bw, bh, "만약", str(args.get("if", "1이 그대로면")), WHITE, LIGHT, fade(t, 0.2, 0.35))
    _arrow(d, xl + bw / 2 + 34 * SS, y, xr - bw / 2 - 34 * SS, _c(WHITE, fade(t, t1, 0.25)), sm((t - t1) / 0.3))
    _rule_box(d, xr, y, bw, bh, "그러면", str(args.get("then", "휴대폰을 서랍에")), YEL, YEL, fade(t, t1 + 0.12, 0.35))
    return finish(img)


# --- 7. schematic bar chart -------------------------------------------------------------------------------------------
def bars_mood(t, dur, args, at):
    """Schematic '기분 회복' chart, no numbers: gray '다른 사람 사진' bar, yellow '어머니 사진' bar rising until at[0]."""
    img, d = canvas()
    t1 = max(at_or(at, 0, 1.6), 1.25)
    ka = fade(t, 0, 0.35)
    ax, yb, ytop = 500 * SS, 700 * SS, 190 * SS
    gx, yx, bw = 790 * SS, 1210 * SS, 230 * SS
    h1, h2 = 150 * SS, 420 * SS
    hg = h1 * sm((t - 0.3) / 0.8)
    hy = h1 * sm((t - 0.3) / 0.8) + (h2 - h1) * sm((t - 0.85) / (t1 - 0.85))
    for x, h, col in ((gx, hg, GRAY), (yx, hy, YEL)):
        if h > 1:
            d.rounded_rectangle([x - bw / 2, yb - h, x + bw / 2, yb + 30 * SS], radius=min(22 * SS, h / 2), fill=col)
    d.rectangle([ax + 4 * SS, yb, 1500 * SS, yb + 40 * SS], fill=BLACK)            # flat bottoms on the axis
    axis = _c(LIGHT, ka)
    _poly(d, [(ax, ytop + 20 * SS), (ax, yb), (1480 * SS, yb)], axis, 7 * SS)
    d.polygon([(ax, ytop - 6 * SS), (ax - 20 * SS, ytop + 30 * SS), (ax + 20 * SS, ytop + 30 * SS)], fill=axis)
    _ctext(d, (ax, ytop - 52 * SS), "기분 회복", 48, _c(WHITE, ka), weight="Bold")
    kl = fade(t, 0.2, 0.35)
    _ctext(d, (gx, yb + 62 * SS), "다른 사람 사진", 48, _c(LIGHT, kl))
    _ctext(d, (yx, yb + 62 * SS), "어머니 사진", 48, _c(YEL, kl), weight="Bold")
    return finish(img)


# --- 8. order matters --------------------------------------------------------------------------------------------------
def _chip(d, x, y, w, h, s, k, col=WHITE):
    d.rounded_rectangle([x - w / 2, y - h / 2, x + w / 2, y + h / 2], radius=h / 2, outline=_c(col, k), width=8 * SS)
    _ctext(d, (x, y), s, 52, _c(col, k))


def order2(t, dur, args, at):
    """Row 1 '속상한 기억 -> 사진' with a yellow check (0.2 s), row 2 '사진 -> 속상한 기억' with a gray X (at[0], 1.2 s)."""
    img, d = canvas()
    cw, ch = 380 * SS, 116 * SS
    xa, xb, xm = CX - 400 * SS, CX + 200 * SS, CX + 560 * SS
    rows = [(CY - 125 * SS, "속상한 기억", "사진", True, 0.2), (CY + 145 * SS, "사진", "속상한 기억", False, at_or(at, 0, 1.2))]
    for y, a, b, ok, t0 in rows:
        ka, kr, kb, km = (fade(t, t0 + o, 0.35) for o in (0.0, 0.15, 0.3, 0.5))
        if ka <= 0:
            continue
        _chip(d, xa, y, cw, ch, a, ka)
        _arrow(d, xa + cw / 2 + 36 * SS, y, xb - cw / 2 - 36 * SS, _c(WHITE, kr), sm((t - t0 - 0.15) / 0.3), w=10 * SS,
               head=26 * SS)
        _chip(d, xb, y, cw, ch, b, kb)
        q = sm((t - t0 - 0.5) / 0.35)
        if ok:
            pts = [(xm - 52 * SS, y + 2 * SS), (xm - 14 * SS, y + 40 * SS), (xm + 58 * SS, y - 46 * SS)]
            _poly(d, _partial(pts, q), YEL, 18 * SS)
        elif q > 0.02:                                            # both strokes of the X grow together
            m = 40 * SS
            _cap_line(d, (xm - m, y - m), (xm - m + 2 * m * q, y - m + 2 * m * q), GRAY, 16 * SS)
            _cap_line(d, (xm + m, y - m), (xm + m - 2 * m * q, y - m + 2 * m * q), GRAY, 16 * SS)
    return finish(img)


# --- 9. vaccine vs first aid ----------------------------------------------------------------------------------------
_syr = {}


def _syringe_mask():
    """Syringe line drawing (needle down-left) as an L mask, cached; centre of the mask = centre of the drawing."""
    if "m" in _syr:
        return _syr["m"]
    n = 760 * SS
    m = Image.new("L", (n, n), 0)
    d = ImageDraw.Draw(m)
    c = n / 2
    P = lambda u, v: (c + u * SS, c + v * SS)
    _cap_line(d, P(-275, 0), P(-180, 0), 255, 7 * SS)                                   # needle
    d.rounded_rectangle([*P(-190, -20), *P(-150, 20)], radius=6 * SS, fill=255)           # hub
    d.rounded_rectangle([*P(-150, -60), *P(110, 60)], radius=16 * SS, outline=255, width=LW)   # barrel
    for i, u in enumerate((-110, -75, -40, -5, 30)):                                        # scale marks
        _cap_line(d, P(u, -60), P(u, -60 + (36 if i % 2 == 0 else 22)), 255, 5 * SS)
    d.rounded_rectangle([*P(52, -46), *P(70, 46)], radius=6 * SS, fill=255)               # plunger seal
    _cap_line(d, P(70, 0), P(228, 0), 255, 15 * SS)                                     # rod
    d.rounded_rectangle([*P(110, -104), *P(132, 104)], radius=10 * SS, fill=255)          # finger flange
    d.rounded_rectangle([*P(226, -74), *P(248, 74)], radius=10 * SS, fill=255)            # thumb rest
    _syr["m"] = m.rotate(38, resample=Image.BICUBIC)
    return _syr["m"]


def medkit(t, dur, args, at):
    """Syringe '예방주사' (dims to gray at at[0], 0.8 s) and first-aid box '마음의 응급약' (yellow + glow at at[1], 2.2 s)."""
    img, d = canvas()
    t1, t2 = at_or(at, 0, 0.8), at_or(at, 1, 2.2)
    k0, kd, ky = fade(t, 0, 0.35), fade(t, t1, 0.4), fade(t, t2, 0.4)
    sx, kx, y = CX - 420 * SS, CX + 400 * SS, CY - 20 * SS
    img = _glow(img, [kx - 300 * SS, y - 250 * SS, kx + 300 * SS, y + 250 * SS], YEL, 0.6 * ky, blur=60)
    d = ImageDraw.Draw(img)
    m = _syringe_mask()                                                                     # left: syringe
    if k0 > 0:
        mm = m if k0 >= 1 else m.point(lambda v: round(v * k0))
        img.paste(Image.new("RGB", m.size, mix(WHITE, GRAY, kd)), (round(sx - m.width / 2), round(y - m.height / 2)), mm)
    sc = _c(mix(WHITE, GRAY, kd), k0)
    _ctext(d, (sx, 735 * SS), "예방주사", 56, sc, weight="Bold")
    kc = _c(mix(WHITE, YEL, ky), k0)                                                        # right: first-aid box
    bw, bh = 420 * SS, 300 * SS
    d.rounded_rectangle([kx - 85 * SS, y - bh / 2 - 66 * SS, kx + 85 * SS, y - bh / 2 + 30 * SS], radius=26 * SS,
                        outline=kc, width=LW)
    d.rounded_rectangle([kx - bw / 2, y - bh / 2, kx + bw / 2, y + bh / 2], radius=44 * SS, outline=kc, width=LW, fill=BLACK)
    a, l, cy_ = 36 * SS, 96 * SS, y + 6 * SS
    plus = [(kx - a, cy_ - l), (kx + a, cy_ - l), (kx + a, cy_ - a), (kx + l, cy_ - a), (kx + l, cy_ + a), (kx + a, cy_ + a),
            (kx + a, cy_ + l), (kx - a, cy_ + l), (kx - a, cy_ + a), (kx - l, cy_ + a), (kx - l, cy_ - a), (kx - a, cy_ - a)]
    if ky > 0:
        d.polygon(plus, fill=_c(YEL, ky))
    _poly(d, plus, kc, 10 * SS, closed=True)
    _ctext(d, (kx, 735 * SS), "마음의 응급약", 56, kc, weight="Bold")
    return finish(img)


# --- 10. profile card ---------------------------------------------------------------------------------------------
def _bust(d, x, y, r, col, w, kid=False):
    """Line-art head and shoulders in a circle (as icons.bust); kid=True: bigger head, narrower shoulders."""
    d.ellipse([x - r, y - r, x + r, y + r], outline=col, width=w)
    if kid:
        hr, hy, sw, st, sb = r * 0.40, y - r * 0.24, 0.46, 0.30, 1.20
    else:
        hr, hy, sw, st, sb = r * 0.30, y - r * 0.52, 0.62, -0.02, 1.22
    d.ellipse([x - hr, hy - hr, x + hr, hy + hr], outline=col, width=w)
    d.arc([x - r * sw, y + r * st, x + r * sw, y + r * sb], start=200, end=340, fill=col, width=w)


def profile(t, dur, args, at):
    """Profile card: line-art bust (args['kid'] -> child) and name / line1 / line2 (args) fading in one after another."""
    args = _args(args)
    name, l1, l2 = (str(args.get(k, "")) for k in ("name", "line1", "line2"))
    img, d = canvas()
    fn, f1 = font(86, "ExtraBold"), font(44)
    r, gap = 170 * SS, 80 * SS
    tw = max([fn.getlength(name), f1.getlength(l1), f1.getlength(l2), 1])
    x = CX - (2 * r + gap + tw) / 2 + r
    tx, y = x + r + gap, CY
    _bust(d, x, y, r, _c(WHITE, fade(t, 0, 0.4)), LW, bool(args.get("kid")))
    d.text((tx, y - 64 * SS), name, font=fn, fill=_c(WHITE, fade(t, 0.25, 0.4)), anchor="ls")
    d.text((tx, y + 14 * SS), l1, font=f1, fill=_c(LIGHT, fade(t, 0.5, 0.4)), anchor="ls")
    d.text((tx, y + 88 * SS), l2, font=f1, fill=_c(LIGHT, fade(t, 0.75, 0.4)), anchor="ls")
    return finish(img)


# --- 11. notes app, typed ------------------------------------------------------------------------------------------
MEMO_TEXT = "6시 30분에 보낸 카톡이 아직 안 읽혀서, 지금 내가 많이 불안하구나."


def memo(t, dur, args, at):
    """Notes screen '메모' on a phone: args['text'] typed from at[0] (0.3 s) at 16 chars/s, steady (non-blinking) cursor."""
    args = _args(args)
    s = str(args.get("text") or MEMO_TEXT)
    t0, cps = at_or(at, 0, 0.3), float(args.get("cps", 16))
    img, d = canvas()
    k0 = fade(t, 0, 0.3)
    col = _c(WHITE, k0)
    pw, ph, x, y = 560 * SS, 760 * SS, CX, 452 * SS
    _phone(d, x, y, pw, ph, col)
    left, right = x - pw / 2 + 54 * SS, x + pw / 2 - 54 * SS
    top = y - ph / 2
    _ctext(d, (left, top + 112 * SS), "메모", 44, col, weight="Bold", ha="l")
    d.line([(left, top + 162 * SS), (right, top + 162 * SS)], fill=_c(DIM, k0), width=3 * SS)
    f = noto(44)
    lines, seps = _wrap(s, f, right - left)
    lh, base0 = 74 * SS, top + 252 * SS
    n = max(0, int((t - t0) * cps)) if t >= t0 else 0
    cur_line, cur_x = 0, left
    for i, (ln, sep) in enumerate(zip(lines, seps)):
        shown = ln[:min(n, len(ln))]
        if shown:
            d.text((left, base0 + i * lh), shown, font=f, fill=col, anchor="ls")
        if n <= len(ln) or i == len(lines) - 1:
            cur_line, cur_x = i, left + f.getlength(shown)
            break
        n -= len(ln) + sep
        if n <= 0 and i + 1 < len(lines):
            cur_line, cur_x = i + 1, left
            break
    cb = base0 + cur_line * lh
    d.rectangle([cur_x + 4 * SS, cb - 46 * SS, cur_x + 8 * SS, cb + 10 * SS], fill=_c(YEL, k0))     # steady cursor
    return finish(img)


# --- 12. early-2000s mobile phone ----------------------------------------------------------------------------------
def _timer_secs(v):
    if isinstance(v, (int, float)) and not isinstance(v, bool):
        return max(0, round(float(v) * 60))                      # a number = minutes
    s = str(v).strip()
    if ":" in s:
        m, sec = s.split(":", 1)
        return max(0, int(float(m or 0)) * 60 + int(float(sec or 0)))
    return max(0, round(float(s) * 60))


_lcd_mask = {}


def _sms(lcd, t, msgs, at, sw, sh):
    """Text messages stacked under the status row of the phone screen, message i fading in at at[i]. When a new one
    does not fit, the oldest fades out in place, the rest slide up, then the new one fades in (nothing half cut)."""
    if not msgs:
        return
    f = font(42, "SemiBold")
    lh, gap, top = 58 * SS, 18 * SS, 70 * SS
    area_h = sh - top - 12 * SS
    rows = [_wrap(s, f, sw - 52 * SS)[0] for s in msgs]
    hs = [len(r) * lh for r in rows]
    times = [at_or(at, i, 0.3 + 0.9 * i) for i in range(len(msgs))]

    def layout(n):                                    # y of each visible message once the first n have arrived
        start, total = n, 0
        while start > 0:
            h = hs[start - 1] + (gap if start < n else 0)
            if total + h > area_h and start < n:
                break
            total += h
            start -= 1
        ys, y = {}, 0
        for i in range(start, n):
            ys[i] = y
            y += hs[i] + gap
        return ys

    n = sum(1 for tt in times if tt <= t)
    if n == 0:
        return
    a = times[n - 1]
    old, new = layout(n - 1), layout(n)
    dropped = [i for i in old if i not in new]
    show = []                                         # (message index, y, opacity)
    for i in dropped:
        show.append((i, old[i], 1 - fade(t, a, 0.25)))
    u = sm((t - a - 0.2) / 0.35) if dropped else 1.0
    for i, y in new.items():
        if i == n - 1:
            show.append((i, y, fade(t, a + (0.45 if dropped else 0.0), 0.35)))
        else:
            show.append((i, old.get(i, y) + (y - old.get(i, y)) * u, 1.0))
    area = Image.new("RGB", (sw, round(area_h)), LCD_BG)
    ad = ImageDraw.Draw(area)
    for i, y, k in show:
        if k <= 0:
            continue
        for j, ln in enumerate(rows[i]):
            _ctext(ad, (26 * SS, y + j * lh + lh / 2), ln, 42, mix(LCD_BG, LCD_FG, k), f=f, ha="l")
    lcd.paste(area, (0, top))


def oldphone(t, dur, args, at):
    """Generic candy-bar phone: args['lines'] shown at at[i] (0.3, 1.2, ...), or args['timer'] counting up from 0:00."""
    args = _args(args)
    img, d = canvas()
    k0 = fade(t, 0, 0.3)
    col = _c(WHITE, k0)
    bx0, by0, bx1, by1 = 650 * SS, 34 * SS, 1270 * SS, 850 * SS
    d.rounded_rectangle([bx0, by0, bx1, by1], radius=118 * SS, outline=col, width=LW)
    d.rounded_rectangle([CX - 62 * SS, 72 * SS, CX + 62 * SS, 86 * SS], radius=7 * SS, fill=col)           # speaker
    sw, sh = 520 * SS, 300 * SS
    sx0, sy0 = round(CX - sw / 2), 116 * SS
    lcd = Image.new("RGB", (sw, sh), LCD_BG)
    ld = ImageDraw.Draw(lcd)
    for i in range(4):                                                                          # signal bars
        bx = (24 + i * 15) * SS
        ld.rectangle([bx, (46 - 8 - i * 6) * SS, bx + 9 * SS, 46 * SS], fill=LCD_FG)
    ld.rectangle([sw - 76 * SS, 24 * SS, sw - 30 * SS, 46 * SS], outline=LCD_FG, width=3 * SS)       # battery
    ld.rectangle([sw - 30 * SS, 30 * SS, sw - 25 * SS, 40 * SS], fill=LCD_FG)
    for i in range(3):
        ld.rectangle([sw - (71 - i * 14) * SS, 29 * SS, sw - (61 - i * 14) * SS, 41 * SS], fill=LCD_FG)
    if args.get("timer") not in (None, "", False):
        total = _timer_secs(args["timer"])
        u = sm(min(max(t / max(0.85 * dur, 0.5), 0.0), 1.0))
        secs = total if u >= 1 else int(total * u)
        _ctext(ld, (sw / 2, 150 * SS), f"{secs // 60}:{secs % 60:02d}", 120, LCD_FG, weight="Bold", features=["tnum"])
        _ctext(ld, (sw / 2, 252 * SS), "새 메시지 없음", 42, LCD_FG)
    else:
        _sms(lcd, t, [str(s) for s in (args.get("lines") or [])], at, sw, sh)
    if k0 < 1:
        lcd = Image.blend(Image.new("RGB", lcd.size, BLACK), lcd, k0)
    if "m" not in _lcd_mask:
        mk = Image.new("L", (sw, sh), 0)
        ImageDraw.Draw(mk).rounded_rectangle([0, 0, sw - 1, sh - 1], radius=16 * SS, fill=255)
        _lcd_mask["m"] = mk
    img.paste(lcd, (sx0, sy0), _lcd_mask["m"])
    kc = col
    d.rounded_rectangle([CX - 105 * SS, 452 * SS, CX + 105 * SS, 510 * SS], radius=29 * SS, outline=kc, width=7 * SS)
    for sxk in (-1, 1):                                                                        # soft keys
        d.rounded_rectangle([CX + sxk * 205 * SS - 48 * SS, 462 * SS, CX + sxk * 205 * SS + 48 * SS, 500 * SS],
                            radius=19 * SS, outline=kc, width=6 * SS)
    for rr in range(4):                                                                        # 4 x 3 keypad
        for cc in range(3):
            kx, ky = CX + (cc - 1) * 178 * SS, (570 + rr * 74) * SS
            d.rounded_rectangle([kx - 70 * SS, ky - 26 * SS, kx + 70 * SS, ky + 26 * SS], radius=26 * SS, outline=kc,
                                width=6 * SS)
    return finish(img)


KINDS = {
    "brain_q": brain_q, "clock_run": clock_run, "three": three, "bell_off": bell_off, "clocks3": clocks3,
    "ifthen": ifthen, "bars_mood": bars_mood, "order2": order2, "medkit": medkit, "profile": profile,
    "memo": memo, "oldphone": oldphone,
}
