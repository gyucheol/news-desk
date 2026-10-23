# Extra icon screens for render.py (guide 6-3): black background, white line icons, one accent colour
# (yellow = attention, red = warning), drawn at 2x then downsampled. Used by the full burnout episode (2026-10-22).
# Each draw function gets t (seconds since the scene started) and dur (scene length).
import math, os
from PIL import Image, ImageDraw, ImageFilter, ImageFont

W, H, SS = 1920, 1080, 2
WHITE, GRAY, DIM = (255, 255, 255), (110, 110, 110), (55, 55, 55)
YEL, RED = (242, 201, 76), (229, 72, 77)
ROOT = os.environ.get("VIDEO_ROOT", os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
FONT = f"{ROOT}/fonts/Pretendard-SemiBold.otf"
CX, CY = W * SS / 2, H * SS * 0.42          # icon centre, above the subtitle area
LW = 12 * SS
_fonts = {}


def font(px):
    if px not in _fonts:
        _fonts[px] = ImageFont.truetype(FONT, px * SS)
    return _fonts[px]


def sm(u):
    u = min(max(u, 0.0), 1.0)
    return u * u * (3 - 2 * u)


def mix(c1, c2, u):
    u = min(max(u, 0.0), 1.0)
    return tuple(round(a + (b - a) * u) for a, b in zip(c1, c2))


def canvas():
    img = Image.new("RGB", (W * SS, H * SS), (0, 0, 0))
    return img, ImageDraw.Draw(img)


def text(d, xy, s, px, fill=WHITE, anchor="mm"):
    d.text(xy, s, font=font(px), fill=fill, anchor=anchor)


def glow(img, box, colour, strength):
    """Soft light behind an element (strength 0..1)."""
    if strength <= 0:
        return img
    m = Image.new("L", img.size, 0)
    ImageDraw.Draw(m).ellipse(box, fill=round(150 * strength))
    m = m.filter(ImageFilter.GaussianBlur(60 * SS))
    return Image.composite(Image.new("RGB", img.size, colour), img, m)


def page(d, x, y, s, col):
    """Document icon with a folded corner and three lines; (x, y) = centre, s = height."""
    w, h, f = s * 0.76, s, s * 0.22
    x0, y0 = x - w / 2, y - h / 2
    d.line([(x0, y0), (x0 + w - f, y0), (x0 + w, y0 + f), (x0 + w, y0 + h), (x0, y0 + h), (x0, y0)], fill=col,
           width=max(2, round(s * 0.07)), joint="curve")
    d.line([(x0 + w - f, y0), (x0 + w - f, y0 + f), (x0 + w, y0 + f)], fill=col, width=max(2, round(s * 0.05)))
    for k in range(3):
        yy = y0 + h * (0.42 + 0.17 * k)
        d.line([(x0 + w * 0.2, yy), (x0 + w * (0.8 if k < 2 else 0.55), yy)], fill=col, width=max(2, round(s * 0.05)))


# --- clocks -----------------------------------------------------------------------------------------------------
def clock(t, dur, hour):
    img, d = canvas()
    r = 230 * SS
    d.ellipse([CX - r, CY - r, CX + r, CY + r], outline=WHITE, width=LW)
    for k in range(12):
        a = math.radians(k * 30 - 90)
        r1 = r * (0.78 if k % 3 == 0 else 0.86)
        col = YEL if (k == hour % 12 and t > 1.0) else WHITE
        d.line([(CX + r1 * math.cos(a), CY + r1 * math.sin(a)), (CX + r * 0.93 * math.cos(a), CY + r * 0.93 * math.sin(a))],
               fill=col, width=(9 if k % 3 == 0 else 6) * SS)
    u = sm(t / 1.0)
    ah = math.radians(-90 + (hour % 12) * 30 * u)               # hour hand sweeps from 12 to the hour
    am = math.radians(-90 + 360 * u)                             # minute hand turns once and stops at 12
    d.line([(CX, CY), (CX + r * 0.5 * math.cos(ah), CY + r * 0.5 * math.sin(ah))], fill=WHITE, width=16 * SS)
    d.line([(CX, CY), (CX + r * 0.75 * math.cos(am), CY + r * 0.75 * math.sin(am))], fill=WHITE, width=10 * SS)
    d.ellipse([CX - 14 * SS, CY - 14 * SS, CX + 14 * SS, CY + 14 * SS], fill=WHITE)
    if hour in (1, 2, 3, 4):                                     # small moon for the small hours
        mx, my, mr = CX + r * 1.35, CY - r * 0.75, 46 * SS
        k = sm((t - 0.6) / 0.6)
        d.ellipse([mx - mr, my - mr, mx + mr, my + mr], fill=mix((0, 0, 0), YEL, k))
        d.ellipse([mx - mr + 26 * SS, my - mr - 10 * SS, mx + mr + 26 * SS, my + mr - 10 * SS], fill=(0, 0, 0))
    return img


# --- dials ------------------------------------------------------------------------------------------------------
def dial(d, r, ticks=10):
    cy = CY + r * 0.30                                           # dial centre low enough that the arc fits
    d.arc([CX - r, cy - r, CX + r, cy + r], start=180, end=360, fill=WHITE, width=LW)
    for k in range(ticks + 1):
        a = math.radians(180 + 180 * k / ticks)
        d.line([(CX + r * 0.82 * math.cos(a), cy + r * 0.82 * math.sin(a)),
                (CX + r * 0.94 * math.cos(a), cy + r * 0.94 * math.sin(a))], fill=WHITE, width=7 * SS)
    return cy


def needle(d, cy, r, frac, col=WHITE):
    a = math.radians(180 + 180 * frac)
    d.line([(CX, cy), (CX + r * 0.78 * math.cos(a), cy + r * 0.78 * math.sin(a))], fill=col, width=12 * SS)
    d.ellipse([CX - 22 * SS, cy - 22 * SS, CX + 22 * SS, cy + 22 * SS], fill=col)


def gauge(t, dur):
    """Pressure gauge: needle climbs into the red zone and trembles there (chronic stress)."""
    img, d = canvas()
    r = 300 * SS
    cy = dial(d, r)
    d.arc([CX - r, cy - r, CX + r, cy + r], start=324, end=360, fill=RED, width=LW + 10 * SS)
    frac = 0.08 + 0.84 * sm(t / 1.3) + (0.012 * math.sin(t * 23) if t > 1.3 else 0)
    needle(d, cy, r, frac, mix(WHITE, RED, sm((t - 0.9) / 0.5)))
    return img


def fuel(t, dur):
    """Fuel gauge: from half to E; E turns red."""
    img, d = canvas()
    r = 300 * SS
    cy = dial(d, r, ticks=8)
    k = sm((t - 0.3) / 1.4)
    needle(d, cy, r, 0.5 - 0.48 * k)
    text(d, (CX - r * 1.02, cy + 60 * SS), "E", 64, mix(WHITE, RED, k))
    text(d, (CX + r * 1.02, cy + 60 * SS), "F", 64, WHITE)
    px, py = CX, cy - r * 0.38                                    # fuel pump glyph
    d.rounded_rectangle([px - 34 * SS, py - 48 * SS, px + 22 * SS, py + 48 * SS], radius=8 * SS, outline=WHITE, width=8 * SS)
    d.rectangle([px - 22 * SS, py - 36 * SS, px + 10 * SS, py - 8 * SS], fill=WHITE)
    d.line([(px + 22 * SS, py - 20 * SS), (px + 46 * SS, py - 4 * SS), (px + 46 * SS, py + 30 * SS)], fill=WHITE, width=8 * SS)
    return img


# --- batteries and phones ----------------------------------------------------------------------------------------
def battery_shape(d, x, y, bw, bh, lvl, fill, bolt=0.0):
    d.rounded_rectangle([x - bw / 2, y - bh / 2, x + bw / 2, y + bh / 2], radius=bh * 0.17, outline=WHITE, width=LW)
    d.rounded_rectangle([x + bw / 2 + 8 * SS, y - bh * 0.2, x + bw / 2 + 26 * SS, y + bh * 0.2], radius=8 * SS, fill=WHITE)
    pad = bh * 0.13
    d.rounded_rectangle([x - bw / 2 + pad, y - bh / 2 + pad, x - bw / 2 + pad + max((bw - 2 * pad) * lvl, 14 * SS),
                         y + bh / 2 - pad], radius=bh * 0.07, fill=fill)
    if bolt > 0:
        sc = (0.45 + 0.25 * bolt) * SS * bh / (150 * SS)
        pts = [(18, -70), (-30, 8), (2, 8), (-14, 70), (34, -10), (2, -10), (18, -70)]
        d.polygon([(x + px * sc, y + py * sc) for px, py in pts], fill=mix((0, 0, 0), YEL, bolt))


def battery2(t, dur):
    """Ordinary tiredness refills; burnout stays near empty although it is charging."""
    img, d = canvas()
    bw, bh = 340 * SS, 160 * SS
    xl, xr, y = CX - 330 * SS, CX + 300 * SS, CY - 20 * SS
    k = sm((t - 0.3) / 2.2)
    battery_shape(d, xl, y, bw, bh, 0.18 + 0.8 * k, WHITE, bolt=sm(t / 0.3))
    blink = 1.0 if t < 1.5 else (0.4 if int(t * 3) % 2 else 1.0)
    battery_shape(d, xr, y, bw, bh, 0.1 + 0.03 * math.sin(t * 2), mix((0, 0, 0), RED, blink), bolt=sm(t / 0.3))
    text(d, (xl, y + bh * 0.95), "보통의 피로", 46, GRAY)
    text(d, (xr, y + bh * 0.95), "번아웃", 46, mix(GRAY, RED, sm((t - 1.2) / 0.6)))
    return img


def phone_shape(d, x, y, pw, ph):
    d.rounded_rectangle([x - pw / 2, y - ph / 2, x + pw / 2, y + ph / 2], radius=pw * 0.16, outline=WHITE, width=LW)
    d.rounded_rectangle([x - pw * 0.12, y - ph / 2 + 26 * SS, x + pw * 0.12, y - ph / 2 + 40 * SS], radius=6 * SS, fill=WHITE)


def apps(t, dur):
    """A phone whose app icons keep lighting up while its battery bar drains (something keeps running)."""
    img, d = canvas()
    pw, ph = 330 * SS, 600 * SS
    x, y = CX, CY - 10 * SS
    phone_shape(d, x, y, pw, ph)
    lvl = 0.62 - 0.5 * sm(t / max(dur - 0.5, 1.0))
    bx, by = x, y - ph / 2 + 92 * SS
    d.rounded_rectangle([bx - 70 * SS, by - 18 * SS, bx + 70 * SS, by + 18 * SS], radius=6 * SS, outline=WHITE, width=5 * SS)
    d.rectangle([bx - 64 * SS, by - 12 * SS, bx - 64 * SS + 128 * SS * lvl, by + 12 * SS], fill=RED if lvl < 0.25 else WHITE)
    s, gap = 70 * SS, 28 * SS
    x0, y0 = x - (3 * s + 2 * gap) / 2, y - 120 * SS
    for i in range(12):
        cx, cy = x0 + (i % 3) * (s + gap), y0 + (i // 3) * (s + gap)
        on = sm((t - 0.15 - i * 0.22) / 0.3)
        d.rounded_rectangle([cx, cy, cx + s, cy + s], radius=16 * SS, outline=mix(DIM, WHITE, on), width=5 * SS,
                            fill=mix((0, 0, 0), (70, 70, 70), on))
    return img


def phone_off(t, dur):
    """Phone on the charger whose screen stays dark: an empty battery blinks."""
    img, d = canvas()
    pw, ph = 330 * SS, 600 * SS
    phone_shape(d, CX, CY - 10 * SS, pw, ph)
    blink = 1.0 if int(t * 2) % 2 == 0 else 0.25
    battery_shape(d, CX - 10 * SS, CY - 10 * SS, 150 * SS, 72 * SS, 0.06, mix((0, 0, 0), RED, blink))
    d.line([(CX, CY + ph / 2 - 10 * SS), (CX, CY + ph / 2 + 70 * SS)], fill=GRAY, width=10 * SS)   # cable
    return img


# --- research ----------------------------------------------------------------------------------------------------
def docs(t, dur, n):
    img, d = canvas()
    if n <= 7:
        sp = 190 * SS
        for i in range(n):
            k = sm((t - 0.2 - i * 0.28) / 0.25)
            if k > 0:
                page(d, CX + (i - (n - 1) / 2) * sp, CY, 170 * SS, mix((0, 0, 0), WHITE, k))
    else:
        cols, rows = 12, 4
        sp = 120 * SS
        for i in range(cols * rows):
            k = sm((t - 0.1 - i * 0.035) / 0.2)
            c, r_ = i % cols, i // cols
            col = WHITE if i < 7 else GRAY
            if k > 0:
                page(d, CX + (c - (cols - 1) / 2) * sp, CY - 150 * SS + r_ * 110 * SS, 88 * SS, mix((0, 0, 0), col, k))
    return img


def graph(t, dur):
    """Wellbeing line rises during the holiday and falls back after returning to work."""
    img, d = canvas()
    x0, x1, yb, yt = CX - 640 * SS, CX + 640 * SS, CY + 190 * SS, CY - 230 * SS
    d.line([(x0, yt), (x0, yb), (x1, yb)], fill=GRAY, width=7 * SS)
    v0, v1 = x0 + 0.33 * (x1 - x0), x0 + 0.55 * (x1 - x0)
    d.rectangle([v0, yt, v1, yb - 4 * SS], fill=(40, 34, 14))
    text(d, ((v0 + v1) / 2, yt - 40 * SS), "휴가", 48, YEL)
    base, high = yb - 130 * SS, yt + 70 * SS

    def yv(x):
        if x < v0: return base
        if x < v0 + 120 * SS: return base + (high - base) * sm((x - v0) / (120 * SS))
        if x < v1: return high
        if x < v1 + 200 * SS: return high + (base - high) * sm((x - v1) / (200 * SS))
        return base
    prog = sm(t / max(min(dur - 0.6, 3.0), 1.0))
    xe = x0 + (x1 - x0) * prog
    pts = [(x, yv(x)) for x in [x0 + i * 8 * SS for i in range(int((xe - x0) / (8 * SS)) + 1)]]
    if len(pts) > 1:
        d.line(pts, fill=WHITE, width=12 * SS, joint="curve")
    d.line([(v1, yt), (v1, yb)], fill=mix((0, 0, 0), GRAY, prog), width=4 * SS)
    text(d, (v1 + 10 * SS, yb + 46 * SS), "복귀", 40, mix((0, 0, 0), GRAY, prog), anchor="lm")
    return img


def calendar(t, dur):
    """Two weeks of days: holiday days, then the line is back to the old level after the first week back."""
    img, d = canvas()
    n, s, gap = 14, 96 * SS, 14 * SS
    x0 = CX - (n * s + (n - 1) * gap) / 2
    y = CY + 120 * SS
    for i in range(n):
        x = x0 + i * (s + gap)
        hol = i < 4
        d.rounded_rectangle([x, y, x + s, y + s], radius=14 * SS, outline=YEL if hol else GRAY, width=6 * SS,
                            fill=(40, 34, 14) if hol else None)
    wk0, wk1 = x0 + 4 * (s + gap), x0 + 11 * (s + gap) - gap
    k = sm((t - 1.2) / 0.5)
    d.line([(wk0, y + s + 30 * SS), (wk1, y + s + 30 * SS)], fill=mix((0, 0, 0), YEL, k), width=8 * SS)
    text(d, ((wk0 + wk1) / 2, y + s + 80 * SS), "복귀 첫 주", 44, mix((0, 0, 0), YEL, k))
    base, high = y - 70 * SS, y - 330 * SS
    prog = sm(t / max(min(dur - 0.6, 2.6), 1.0))
    pts = []
    for i in range(n * 4 + 1):
        xx = x0 + i * (s + gap) / 4
        dd = i / 4
        yy = high if dd < 4 else (high + (base - high) * sm((dd - 4) / 7) if dd < 11 else base)
        if xx <= x0 + (n * (s + gap)) * prog:
            pts.append((xx + s / 2, yy))
    if len(pts) > 1:
        d.line(pts, fill=WHITE, width=12 * SS, joint="curve")
    d.line([(x0, base), (x0 + n * (s + gap), base)], fill=DIM, width=4 * SS)
    return img


def bars(t, dur):
    """Short and long holidays: different lengths, the same small lift afterwards."""
    img, d = canvas()
    for j, (label, length) in enumerate([("짧은 휴가", 220), ("긴 휴가", 620)]):
        y = CY - 150 * SS + j * 260 * SS
        x0 = CX - 520 * SS
        k = sm((t - 0.2 - j * 0.4) / 0.6)
        text(d, (x0 - 30 * SS, y), label, 48, GRAY, anchor="rm")
        d.rounded_rectangle([x0, y - 40 * SS, x0 + length * SS * k + 1, y + 40 * SS], radius=18 * SS, fill=mix((0, 0, 0), YEL, 0.85))
        e = sm((t - 1.4) / 0.5)                                   # effect marker: the same for both
        ex = x0 + 760 * SS
        d.line([(ex, y - 60 * SS), (ex, y + 60 * SS)], fill=mix((0, 0, 0), WHITE, e), width=10 * SS)
        d.polygon([(ex - 30 * SS, y - 60 * SS), (ex + 30 * SS, y - 60 * SS), (ex, y - 100 * SS)], fill=mix((0, 0, 0), WHITE, e))
    e = sm((t - 1.9) / 0.5)
    text(d, (CX + 240 * SS, CY + 260 * SS), "효과는 비슷", 44, mix((0, 0, 0), WHITE, e))
    return img


# --- the six areas of worklife (Maslach & Leiter) ---------------------------------------------------------------
SIX = ["업무량", "자율성", "보상", "관계", "공정함", "가치관"]


def six_pos(i):
    r_ = 330 * SS
    a = math.radians(-90 + 60 * i)
    return CX + r_ * math.cos(a), CY + 20 * SS + r_ * 0.78 * math.sin(a)


def six(t, dur, mode):
    img, d = canvas()
    R = 112 * SS
    for i, name in enumerate(SIX):
        x, y = six_pos(i)
        col, fill, k = WHITE, None, 1.0
        if mode == "appear":
            k = sm((t - 0.1 - i * dur / 7) / 0.35)
        elif mode == "off" and i in (0, 2, 4):
            m = sm((t - 0.5) / 0.7)
            x, y = x + (x - CX) * 0.22 * m, y + (y - CY) * 0.22 * m
            col = mix(WHITE, RED, m)
        elif mode == "seq":
            order = {0: 0, 2: 1, 3: 2}
            if i in order:
                on = sm((t - 0.2 - order[i] * 0.9) / 0.3)
                col, fill = mix(GRAY, YEL, on), mix((0, 0, 0), (60, 50, 18), on)
            else:
                col = GRAY
        elif mode == "pick":
            col = WHITE if i == 0 else GRAY
        if k <= 0:
            continue
        col = mix((0, 0, 0), col, k)
        d.ellipse([x - R, y - R, x + R, y + R], outline=col, width=9 * SS, fill=fill)
        text(d, (x, y), name, 44, col)
    if mode == "pick":                                            # a pen circle around one of them
        x, y = six_pos(0)
        p = sm((t - 0.4) / 0.9)
        rr = R * 1.32
        d.arc([x - rr, y - rr * 0.92, x + rr, y + rr * 0.92], start=-200, end=-200 + 380 * p, fill=YEL, width=12 * SS)
    return img


# --- tracking energy -------------------------------------------------------------------------------------------
DAYS = ["월", "화", "수", "목", "금", "토", "일"]
SCORES = [3, 6, 5, 6, 7, 8, 7]


def week(t, dur, mode):
    img, d = canvas()
    sp = 170 * SS
    x0 = CX - 3 * sp
    yb, unit = CY + 200 * SS, 42 * SS
    d.line([(x0 - 80 * SS, yb), (x0 + 6 * sp + 80 * SS, yb)], fill=DIM, width=5 * SS)
    for i, (day, sc) in enumerate(zip(DAYS, SCORES)):
        x = x0 + i * sp
        k = 1.0 if mode == "focus" else sm((t - 0.15 - i * 0.18) / 0.25)
        low = i == 0
        hl = sm((t - 0.3) / 0.5) if (mode == "focus" and low) else 0
        col = mix(WHITE, RED, 1.0 if low else 0) if mode != "focus" else (mix(GRAY, YEL, hl) if low else GRAY)
        text(d, (x, yb + 56 * SS), day, 46, mix((0, 0, 0), col if low else GRAY, k))
        if k > 0:
            y = yb - sc * unit
            d.line([(x, yb), (x, y)], fill=mix((0, 0, 0), DIM, k), width=6 * SS)
            rr = (26 + 8 * hl) * SS
            d.ellipse([x - rr, y - rr, x + rr, y + rr], fill=mix((0, 0, 0), col, k))
            if mode == "focus" and low:
                text(d, (x, y - 90 * SS), "3", 96, mix((0, 0, 0), YEL, hl))
    return img


def memo10(t, dur):
    """A small notebook: today's energy, out of 10."""
    img, d = canvas()
    w, h = 520 * SS, 400 * SS
    x0, y0 = CX - w / 2, CY - h / 2
    d.rounded_rectangle([x0, y0, x0 + w, y0 + h], radius=24 * SS, outline=WHITE, width=LW)
    for i in range(6):
        rx = x0 + 70 * SS + i * 76 * SS
        d.ellipse([rx - 14 * SS, y0 - 22 * SS, rx + 14 * SS, y0 + 22 * SS], outline=WHITE, width=6 * SS)
    text(d, (CX - 10 * SS, CY + 20 * SS), "/ 10", 96, WHITE, anchor="lm")
    k = sm((t - 0.5) / 0.4)
    text(d, (CX - 40 * SS, CY + 20 * SS), "6", 150, mix((0, 0, 0), YEL, k), anchor="rm")
    return img


def bulb_dim(t, dur):
    """A bulb that is not broken, only dim."""
    img, d = canvas()
    r = 118 * SS
    on = 0.28 + 0.06 * math.sin(t * 2.2)
    img = glow(img, [CX - r * 1.4, CY - r * 1.4, CX + r * 1.4, CY + r * 1.4], YEL, on * 0.6)
    d = ImageDraw.Draw(img)
    col = GRAY
    d.arc([CX - r, CY - r, CX + r, CY + r], start=135, end=405, fill=col, width=LW)
    a1, a2 = math.radians(135), math.radians(45)
    base_top, neck = CY + r * 1.28, r * 0.42
    d.line([(CX + r * math.cos(a1), CY + r * math.sin(a1)), (CX - neck, base_top)], fill=col, width=LW)
    d.line([(CX + r * math.cos(a2), CY + r * math.sin(a2)), (CX + neck, base_top)], fill=col, width=LW)
    for k in range(3):
        y = base_top + 10 * SS + k * 30 * SS
        w2 = neck - k * 10 * SS
        d.rounded_rectangle([CX - w2, y, CX + w2, y + 16 * SS], radius=8 * SS, fill=col)
    pts = [(CX - 44 * SS, CY + 30 * SS), (CX - 22 * SS, CY - 18 * SS), (CX, CY + 22 * SS),
           (CX + 22 * SS, CY - 18 * SS), (CX + 44 * SS, CY + 30 * SS)]
    d.line(pts, fill=mix(GRAY, YEL, on), width=8 * SS, joint="curve")
    return img



# --- v2 graphics (2026-10-23 user feedback: show the script literally) ------------------------------------------------
FONT_B = f"{ROOT}/fonts/Pretendard-ExtraBold.otf"
_fb = {}


def font_b(px):
    if px not in _fb:
        _fb[px] = ImageFont.truetype(FONT_B, px * SS)
    return _fb[px]


def bust(d, x, y, r, col, w):
    """Line-art head and shoulders inside a circle (a person whose photo we do not show)."""
    d.ellipse([x - r, y - r, x + r, y + r], outline=col, width=w)
    hr = r * 0.30
    d.ellipse([x - hr, y - r * 0.52 - hr, x + hr, y - r * 0.52 + hr], outline=col, width=w)
    d.arc([x - r * 0.62, y - r * 0.02, x + r * 0.62, y + r * 1.22], start=200, end=340, fill=col, width=w)


def freud_card(t, dur):
    """Profile card for Herbert Freudenberger: no freely licensed photo of him exists (checked 2026-10-23)."""
    img, d = canvas()
    k = sm(t / 0.45)
    x, y, r = CX - 420 * SS, CY, 170 * SS
    bust(d, x, y, r, mix((0, 0, 0), WHITE, k), LW)
    tx = CX - 180 * SS
    k2 = sm((t - 0.25) / 0.45)
    d.text((tx, y - 70 * SS), "허버트 프로이덴버거", font=font_b(86), fill=mix((0, 0, 0), WHITE, k2), anchor="ls")
    d.text((tx, y + 6 * SS), "Herbert J. Freudenberger", font=font(44), fill=mix((0, 0, 0), (170, 170, 170), k2), anchor="ls")
    d.text((tx, y + 80 * SS), "1926–1999 · 미국의 심리학자", font=font(44), fill=mix((0, 0, 0), (170, 170, 170), k2), anchor="ls")
    return img


def globe(d, x, y, r, col, w, k):
    d.ellipse([x - r, y - r, x + r, y + r], outline=col, width=w)
    for e in (0.36, 0.72):                                     # meridians
        d.ellipse([x - r * e, y - r, x + r * e, y + r], outline=col, width=max(2, w // 2))
    d.line([(x, y - r), (x, y + r)], fill=col, width=max(2, w // 2))
    for f in (-0.5, 0, 0.5):                                   # parallels
        yy = y + r * f; hw = r * math.sqrt(1 - f * f)
        d.line([(x - hw, yy), (x + hw, yy)], fill=col, width=max(2, w // 2))


def who2019(t, dur):
    """Year and organisation as text only: the WHO emblem needs WHO's written permission (checked 2026-10-23)."""
    img, d = canvas()
    k = sm(t / 0.5)
    globe(d, CX - 380 * SS, CY, 150 * SS, mix((0, 0, 0), WHITE, k), LW, k)
    k2 = sm((t - 0.2) / 0.5)
    tx = CX - 150 * SS
    d.text((tx, CY - 10 * SS), "2019년", font=font_b(150), fill=mix((0, 0, 0), YEL, k2), anchor="ls")
    k3 = sm((t - 0.45) / 0.5)
    d.text((tx + 6 * SS, CY + 92 * SS), "세계보건기구 (WHO)", font=font_b(64), fill=mix((0, 0, 0), WHITE, k3), anchor="ls")
    return img


def news(t, dur):
    """A newspaper and the person in the article (작년 12월, 26살 직장인 박 모 씨)."""
    img, d = canvas()
    k = sm(t / 0.45)
    col = mix((0, 0, 0), WHITE, k)
    x, y, w, h = CX - 420 * SS, CY, 300 * SS, 380 * SS
    x0, y0 = x - w / 2, y - h / 2
    d.rounded_rectangle([x0, y0, x0 + w, y0 + h], radius=14 * SS, outline=col, width=LW)
    d.text((x, y0 + 62 * SS), "뉴스", font=font_b(58), fill=col, anchor="mm")
    d.line([(x0 + 26 * SS, y0 + 104 * SS), (x0 + w - 26 * SS, y0 + 104 * SS)], fill=col, width=6 * SS)
    d.rectangle([x0 + 30 * SS, y0 + 130 * SS, x0 + w * 0.48, y0 + 250 * SS], outline=col, width=5 * SS)
    for i in range(7):
        yy = y0 + 140 * SS + i * 30 * SS
        xa = x0 + w * 0.56 if i < 4 else x0 + 30 * SS
        d.line([(xa, yy), (x0 + w - 30 * SS, yy)], fill=mix((0, 0, 0), GRAY, k), width=6 * SS)
    tx = CX - 160 * SS
    k2 = sm((t - 0.3) / 0.45)
    d.text((tx, CY - 70 * SS), "작년 12월", font=font(52), fill=mix((0, 0, 0), (170, 170, 170), k2), anchor="ls")
    k3 = sm((t - 0.9) / 0.45)
    d.text((tx, CY + 30 * SS), "26살 직장인", font=font_b(96), fill=mix((0, 0, 0), WHITE, k3), anchor="ls")
    d.text((tx, CY + 120 * SS), "박 모 씨", font=font_b(72), fill=mix((0, 0, 0), YEL, k3), anchor="ls")
    return img


def messenger(t, dur):
    """메신저에 팀장님 이름만 떠도: notifications from 팀장님 drop onto a phone screen."""
    img, d = canvas()
    pw, ph = 470 * SS, 640 * SS
    x, y = CX, CY - 10 * SS
    phone_shape(d, x, y, pw, ph)
    for i, (t0, line) in enumerate([(0.25, "확인 부탁드립니다"), (1.3, "잠깐 통화 가능할까요?")]):
        k = sm((t - t0) / 0.35)
        if k <= 0:
            continue
        by = y - ph / 2 + 110 * SS + i * 150 * SS - (1 - k) * 60 * SS
        bx0, bx1 = x - pw / 2 + 22 * SS, x + pw / 2 - 22 * SS
        d.rounded_rectangle([bx0, by, bx1, by + 126 * SS], radius=22 * SS, fill=mix((0, 0, 0), (58, 58, 58), k))
        d.ellipse([bx0 + 18 * SS, by + 30 * SS, bx0 + 84 * SS, by + 96 * SS], fill=mix((0, 0, 0), YEL, k))
        d.text((bx0 + 104 * SS, by + 52 * SS), "팀장님", font=font_b(40), fill=mix((0, 0, 0), WHITE, k), anchor="ls")
        d.text((bx0 + 104 * SS, by + 100 * SS), line, font=font(30), fill=mix((0, 0, 0), (190, 190, 190), k), anchor="ls")
    return img


def blank_doc(t, dur):
    """빈 파일을 열어 놓고 1시간째 첫 문장만: the first line is typed and erased again; a timer runs."""
    img, d = canvas()
    w, h = 560 * SS, 640 * SS
    x0, y0 = CX - w / 2, CY - h / 2 + 10 * SS
    d.rounded_rectangle([x0, y0, x0 + w, y0 + h], radius=18 * SS, outline=WHITE, width=LW)
    cyc = (t % 1.6) / 1.6
    frac = sm(cyc / 0.55) if cyc < 0.55 else (1 - sm((cyc - 0.65) / 0.3) if cyc > 0.65 else 1.0)
    lx0, ly = x0 + 60 * SS, y0 + 110 * SS
    lw = (w - 120 * SS) * 0.85 * frac
    if lw > 4 * SS:
        d.rounded_rectangle([lx0, ly - 14 * SS, lx0 + lw, ly + 14 * SS], radius=8 * SS, fill=(150, 150, 150))
    if int(t * 2.5) % 2 == 0:
        d.rectangle([lx0 + lw + 8 * SS, ly - 28 * SS, lx0 + lw + 16 * SS, ly + 28 * SS], fill=WHITE)
    for i in range(6):                                          # the rest of the page stays empty
        yy = ly + 90 * SS + i * 70 * SS
        d.line([(lx0, yy), (x0 + w - 60 * SS, yy)], fill=(40, 40, 40), width=4 * SS)
    secs = 3600 + int(t * 7)
    d.text((x0 + w + 40 * SS, y0 + 40 * SS), f"{secs // 3600}:{secs % 3600 // 60:02d}:{secs % 60:02d}",
           font=font_b(64), fill=YEL, anchor="ls")
    return img


def paper1974(t, dur):
    """그는 1974년 논문에서: a paper with the year."""
    img, d = canvas()
    k = sm(t / 0.4)
    page(d, CX - 400 * SS, CY, 330 * SS, mix((0, 0, 0), WHITE, k))
    k2 = sm((t - 0.2) / 0.4)
    tx = CX - 170 * SS
    d.text((tx, CY - 10 * SS), "1974년", font=font_b(150), fill=mix((0, 0, 0), YEL, k2), anchor="ls")
    d.text((tx + 6 * SS, CY + 92 * SS), "논문", font=font_b(64), fill=mix((0, 0, 0), WHITE, k2), anchor="ls")
    return img

KINDS = {
    "clock2": lambda t, d: clock(t, d, 2), "clock6": lambda t, d: clock(t, d, 6),
    "gauge": gauge, "fuel": fuel, "battery2": battery2, "apps": apps, "phone_off": phone_off,
    "docs7": lambda t, d: docs(t, d, 7), "docs_many": lambda t, d: docs(t, d, 48),
    "graph": graph, "calendar": calendar, "bars": bars,
    "six": lambda t, d: six(t, d, "appear"), "six_off": lambda t, d: six(t, d, "off"),
    "six_pick": lambda t, d: six(t, d, "pick"), "six_seq": lambda t, d: six(t, d, "seq"),
    "week": lambda t, d: week(t, d, "dots"), "week3": lambda t, d: week(t, d, "focus"),
    "memo10": memo10, "bulb_dim": bulb_dim,
    "freud_card": freud_card, "who2019": who2019, "news": news, "messenger": messenger, "blank_doc": blank_doc,
    "paper1974": paper1974,
}


def draw(kind, t, dur):
    return KINDS[kind](t, dur).resize((W, H), Image.LANCZOS)
