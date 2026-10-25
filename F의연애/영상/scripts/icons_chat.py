# F의 연애 chat screens (2026-10-24): the dark-theme chat look of the 01 thumbnail (bubble colours measured on the owner's
# Galaxy KakaoTalk screen, F의연애/썸네일/thumb_chat.py), drawn on black like the other icon screens. No app name or logo.
# A bubble appears when its line is spoken (at = voice onsets of the listed lines, seconds from the scene start);
# v2 (2026-10-24, owner): no pop, scale or fade on the bubbles, the unread 1 or the times.
import math
from PIL import Image, ImageDraw, ImageFilter, ImageChops
from fy_common import *

THEIR = (58, 58, 62)            # the other person's bubble (dark gray, as in dark mode)
THEIR_TEXT = (238, 238, 238)
TIME = (150, 152, 156)
BH = 118                        # bubble height at output scale (px); text = 0.37 h like the thumbnail


def _bubble(img, x0, y, text, me, k, h, f, lines=None, lh=None):
    """One chat bubble with its text, drawn at full size (v2: no pop-in; the owner asked for no entrance effect).
    k is kept for the colour (always 1 in v2). lines/lh: several text rows (panels3). Returns (x0, x1)."""
    d = ImageDraw.Draw(img)
    rows = lines or [text]
    lh = lh or h
    wmax = max(f.getlength(r) for r in rows)
    bw = wmax + 0.68 * (h if lines is None else 0.9 * lh)
    bh = h if lines is None else lh * len(rows) + 0.55 * lh
    cx, cy = x0 + bw / 2, y + bh / 2
    w2, h2 = bw / 2, bh / 2
    fill = mix((0, 0, 0), KAKAO if me else THEIR, k)
    r = 0.40 * (h if lines is None else 1.15 * lh)
    d.rounded_rectangle([cx - w2, cy - h2, cx + w2, cy + h2], radius=r, fill=fill)
    tail = h if lines is None else 1.1 * lh
    if me:   # tail at the top right, as on the real screen
        x1 = cx + w2
        d.polygon([(x1 - 0.30 * tail, cy - h2), (x1 + 0.13 * tail, cy - h2 + 0.02 * tail), (x1 - 0.02 * tail, cy - h2 + 0.26 * tail)], fill=fill)
    else:
        xa = cx - w2
        d.polygon([(xa + 0.30 * tail, cy - h2), (xa - 0.13 * tail, cy - h2 + 0.02 * tail), (xa + 0.02 * tail, cy - h2 + 0.26 * tail)], fill=fill)
    tc = mix(fill, KAKAO_TEXT if me else THEIR_TEXT, k)
    for i, row in enumerate(rows):
        ry = cy - (len(rows) - 1) * lh / 2 + i * lh
        d.text((cx - wmax / 2, ry), row, font=f, fill=tc, anchor="lm")
    return cx - bw / 2, cx + bw / 2


def kakao(t, dur, args, at):
    """Chat screen. args: msgs=[{me, text, time, show, read}], show/read = index into at (None = from the start /
    never read), title (label at the top). v2 (2026-10-24, owner): no entrance effect (a message is simply there from
    the moment its line is spoken), the title is white and larger, and no yellow glow behind the unread 1
    (glow_one is ignored)."""
    img, d = canvas()
    h = BH * SS
    f = noto(BH * 0.37, 450)
    f1 = noto(46, 700)
    fm = noto(36, 400)
    msgs = args.get("msgs", [])
    gap = 0.30 * h
    title = args.get("title")
    top_pad = 130 * SS if title else 0
    # v4 (2026-10-25, owner: "첫번째, 두번째, 세번째에 나오는 카톡 위치와 자막 위치가 동일하게"): "slots" lays the
    # screen out as if it had that many messages, so a screen with one message puts its title and bubble where the
    # two-message screens put theirs
    n = max(len(msgs), int(args.get("slots", 0)))
    total = n * h + (n - 1) * gap
    y = CY - total / 2 + top_pad / 2
    if title:
        text(d, (CX, y - 135 * SS), title, 76, WHITE, weight="ExtraBold")
    right, left = CX + 560 * SS, CX - 560 * SS
    for m in msgs:
        t_show = 0.0 if m.get("show") is None else at_or(at, m["show"], 0.0)
        if t < t_show:
            y += h + gap
            continue
        me = m.get("me", True)
        bb = f.getbbox(m["text"])
        bw = (bb[2] - bb[0]) + 0.68 * h
        if me:
            x0 = right - bw
        else:
            av = 0.86 * h                               # round avatar (no photo) left of the bubble
            ax = left + av / 2
            d.ellipse([ax - av / 2, y, ax + av / 2, y + av], fill=(90, 90, 96))
            hr = av * 0.2
            d.ellipse([ax - hr, y + av * 0.22, ax + hr, y + av * 0.22 + 2 * hr], fill=(150, 150, 156))
            d.chord([ax - av * 0.34, y + av * 0.58, ax + av * 0.34, y + av * 1.2], 180, 360, fill=(150, 150, 156))
            x0 = left + av + 0.18 * h
        bx0, bx1 = _bubble(img, x0, y, m["text"], me, 1.0, h, f)
        d = ImageDraw.Draw(img)
        # unread 1 and time: left of my bubble, right of theirs
        read = me and m.get("read") is not None and t >= at_or(at, m["read"], 1e9)
        if me:
            xr = bx0 - 0.12 * h
            if not read:
                d.text((xr, y + h - (0.42 if m.get("time") else 0.10) * h), "1", font=f1, fill=KAKAO_ONE, anchor="rs")
            if m.get("time"):
                d.text((xr, y + h - 0.06 * h), m["time"], font=fm, fill=TIME, anchor="rs")
        elif m.get("time"):
            d.text((bx1 + 0.12 * h, y + h - 0.06 * h), m["time"], font=fm, fill=TIME, anchor="ls")
        y += h + gap
    return finish(img)


def _wrap_rows(s, f, maxw):
    """Split chat text into rows no wider than maxw (at spaces when possible)."""
    rows, cur = [], ""
    for word in s.split(" "):
        cand = (cur + " " + word).strip()
        if f.getlength(cand) <= maxw or not cur:
            cur = cand
        else:
            rows.append(cur); cur = word
    rows.append(cur)
    out = []
    for r in rows:                                   # a single word wider than maxw: cut by characters
        while f.getlength(r) > maxw and len(r) > 1:
            k = len(r)
            while k > 1 and f.getlength(r[:k]) > maxw:
                k -= 1
            out.append(r[:k]); r = r[k:]
        out.append(r)
    return out


PANEL_CHATS = [   # v2 (owner): the panels show the real messages of the three situations
    {"reply": "뭐 할껀 없어, 같이 저녁 먹을까?", "label": "5분 만에 답장"},
    {"reply": "헉 미안해..ㅜ회식 와서 연락을 이제 봤네", "label": "3시간 뒤 답장"},
    {"reply": None, "label": ""},                  # owner: no "3시간째 1" under the third panel
]
MY_MSG = "오늘 퇴근하고 뭐할꺼야?"


def _panel_chat(img, x0, y0, w, hh, i, chat, focus, my_msg):
    """One panel of panels3: outline, my message (unread 1 only when there is no reply) and the reply, readable."""
    d = ImageDraw.Draw(img)
    d.rounded_rectangle([x0, y0, x0 + w, y0 + hh], radius=34 * SS, outline=YEL if focus else (150, 150, 150),
                        width=(10 if focus else 6) * SS)
    f = noto(38, 500)
    lh = 50 * SS
    pad = 30 * SS
    my_rows = _wrap_rows(my_msg, f, w * 0.55)
    bw_me = max(f.getlength(r) for r in my_rows) + 0.68 * 0.9 * lh
    bx0 = x0 + w - pad - bw_me
    by = y0 + 44 * SS
    _bubble(img, bx0, by, my_msg, True, 1.0, lh, f, lines=my_rows, lh=lh)
    my_h = lh * len(my_rows) + 0.55 * lh
    d = ImageDraw.Draw(img)
    if not chat["reply"]:
        d.text((bx0 - 14 * SS, by + my_h - 4 * SS), "1", font=noto(56, 700), fill=KAKAO_ONE, anchor="rs")
        return
    av = 64 * SS                                    # the other person: round avatar + gray bubble
    ry = by + my_h + 40 * SS
    ax = x0 + pad
    d.ellipse([ax, ry, ax + av, ry + av], fill=(90, 90, 96))
    hr = av * 0.2
    d.ellipse([ax + av / 2 - hr, ry + av * 0.22, ax + av / 2 + hr, ry + av * 0.22 + 2 * hr], fill=(150, 150, 156))
    d.chord([ax + av / 2 - av * 0.34, ry + av * 0.58, ax + av / 2 + av * 0.34, ry + av * 1.2], 180, 360, fill=(150, 150, 156))
    rx0 = ax + av + 14 * SS
    rows = _wrap_rows(chat["reply"], f, (x0 + w - pad) - rx0 - 0.68 * 0.9 * lh)
    _bubble(img, rx0, ry, chat["reply"], False, 1.0, lh, f, lines=rows, lh=lh)


def panels3(t, dur, args, at):
    """Three situations side by side with their real messages (v2): replied in 5 min / replied after 3 h / still 1.
    args.focus=[[at_index, panel], ...] outlines one panel in yellow. No entrance effect; labels white and larger."""
    img, d = canvas()
    w, hh, gap = 520 * SS, 390 * SS, 40 * SS              # panels span x 140..1780 px
    x = CX - (3 * w + 2 * gap) / 2
    y0 = 270 * SS
    cur = None
    for ai, p in args.get("focus", []):
        if t >= at_or(at, ai, 1e9):
            cur = p
    chats = args.get("chats", PANEL_CHATS)
    my_msg = args.get("my_msg", MY_MSG)
    # v4 (2026-10-25, owner: "5분 만에 답장, 3시간 뒤 답장 이라는 자막 지워줘. 첫번째, 두번째, 세번째도 지워줘"):
    # "titles": False / "labels": False leave out the words above and under the panels
    for i in range(3):
        focus = cur == i
        xi = x + i * (w + gap)
        _panel_chat(img, xi, y0, w, hh, i, chats[i], focus, my_msg)
        d = ImageDraw.Draw(img)
        col = YEL if focus else WHITE
        if args.get("titles", True):
            text(d, (xi + w / 2, y0 - 62 * SS), ["첫 번째", "두 번째", "세 번째"][i], 66, col, weight="ExtraBold")
        if chats[i].get("label") and args.get("labels", True):
            text(d, (xi + w / 2, y0 + hh + 66 * SS), chats[i]["label"], 54, col, weight="Bold")
    return finish(img)


_CACHE = {}


def _outline(key, size, draw_fn, k):
    """Cached outline mask (width k) of a filled shape drawn by draw_fn: shape minus its erosion."""
    if key not in _CACHE:
        m = Image.new("L", size, 0)
        draw_fn(ImageDraw.Draw(m))
        inner = m
        for _ in range(k):
            inner = inner.filter(ImageFilter.MinFilter(3))
        _CACHE[key] = ImageChops.subtract(m, inner)
    return _CACHE[key]


def chat1(t, dur, args, at):
    """F의 연애 sample icon (render_icons.patch, 2026-10-22): my message bubble and the unread yellow 1 that stays."""
    img, d = canvas()
    cx, cy, lw = CX, CY, LW
    bw, bh, rad = 620 * SS, 250 * SS, 72 * SS
    x1 = cx + bw / 2 + 70 * SS; x0 = x1 - bw
    y0 = cy - bh / 2; y1 = y0 + bh

    def shape(dd):
        dd.rounded_rectangle([x0, y0, x1, y1], radius=rad, fill=255)
        dd.polygon([(x1 - 60 * SS, y0 + 10 * SS), (x1 + 44 * SS, y0 - 2 * SS), (x1 - 2 * SS, y0 + 84 * SS)], fill=255)
    mask = _outline(("chat", SS), img.size, shape, lw)
    a = sm(min(t / 0.3, 1))
    img.paste((255, 255, 255), (0, 0), mask.point(lambda v: round(v * a)))
    d = ImageDraw.Draw(img)
    col = mix((0, 0, 0), (255, 255, 255), a)
    for i, frac in enumerate((0.64, 0.40)):                  # two lines of 'text' (not readable on purpose)
        ly = cy - 34 * SS + i * 68 * SS
        d.rounded_rectangle([x0 + 70 * SS, ly - 13 * SS, x0 + 70 * SS + bw * frac, ly + 13 * SS], radius=13 * SS, fill=col)
    if t >= 0.45:
        k = sm(min((t - 0.45) / 0.2, 1))
        f = font(round(150 + 40 * (1 - k)), "ExtraBold")
        d.text((x0 - 34 * SS, y1 + 4 * SS), "1", font=f, fill=mix((0, 0, 0), YEL, k), anchor="rs")
    return finish(img)


def siren(t, dur, args, at):
    """F의 연애 sample icon (render_icons.patch): a warning lamp that keeps going off (smooth pulse, not a flicker)."""
    img, d = canvas()
    cx, cy, lw = CX, CY, LW
    on = sm(min(t / 0.25, 1))
    p = 0.5 - 0.5 * math.cos(2 * math.pi * 1.25 * max(t - 0.25, 0))
    lit = on * (0.3 + 0.7 * p)
    r = 125 * SS
    top, base_y = cy - r * 1.05, cy + 85 * SS
    g = Image.new("L", img.size, 0)
    ImageDraw.Draw(g).ellipse([cx - r * 1.9, top - r * 0.5, cx + r * 1.9, base_y + r * 0.5], fill=round(190 * lit))
    g = g.filter(ImageFilter.GaussianBlur(85 * SS))
    img = Image.composite(Image.new("RGB", img.size, RED), img, g)
    d = ImageDraw.Draw(img)
    d.rounded_rectangle([cx - r, top, cx + r, base_y], radius=r, corners=(True, True, False, False),
                        fill=mix((60, 8, 10), RED, lit), outline=(255, 255, 255), width=lw)
    d.arc([cx - r * 0.66, top + r * 0.32, cx + r * 0.30, top + r * 1.30], start=195, end=250,
          fill=mix((150, 150, 150), (255, 255, 255), lit), width=round(lw * 0.8))
    d.rounded_rectangle([cx - r * 1.42, base_y + 4 * SS, cx + r * 1.42, base_y + 64 * SS], radius=16 * SS, fill=(255, 255, 255))
    rc = (cx, top + r * 0.95)
    for sx in (-1, 1):
        for dy in (-0.42, 0.0, 0.42):
            vx, vy = sx * math.sqrt(1 - dy * dy), dy
            r1, r2 = r * 1.5, r * (1.5 + 0.22 + 0.30 * p)
            d.line([(rc[0] + vx * r1, rc[1] + vy * r1), (rc[0] + vx * r2, rc[1] + vy * r2)],
                   fill=mix((0, 0, 0), RED, on * (0.45 + 0.55 * p)), width=lw)
    return finish(img)


KINDS = {"kakao": kakao, "panels3": panels3, "chat1": chat1, "siren": siren}


def blank_bubble(t, dur, args, at):
    """그 빈칸을 채우기 시작합니다: an empty speech bubble; at at[0] question marks fill it one by one, turning red."""
    img, d = canvas()
    bw, bh = 760 * SS, 360 * SS
    x0, y0 = CX - bw / 2, CY - bh / 2
    k = fade(t, 0.0, 0.3)
    col = mix((0, 0, 0), WHITE, k)
    d.rounded_rectangle([x0, y0, x0 + bw, y0 + bh], radius=110 * SS, outline=col, width=LW)
    d.polygon([(x0 + 150 * SS, y0 + bh - 6 * SS), (x0 + 120 * SS, y0 + bh + 90 * SS), (x0 + 250 * SS, y0 + bh - 6 * SS)],
              fill=(0, 0, 0))
    d.line([(x0 + 150 * SS, y0 + bh - 2 * SS), (x0 + 120 * SS, y0 + bh + 90 * SS), (x0 + 250 * SS, y0 + bh - 2 * SS)],
           fill=col, width=LW, joint="curve")
    t0 = at_or(at, 0, 1.2)
    dots = 1 - fade(t, t0, 0.3)
    for i in range(3):                                   # empty: three quiet dots
        cx = CX + (i - 1) * 90 * SS
        d.ellipse([cx - 18 * SS, CY - 18 * SS, cx + 18 * SS, CY + 18 * SS], fill=mix((0, 0, 0), GRAY, k * dots))
    for i in range(3):                                   # then the blank fills with guesses
        q = fade(t, t0 + 0.25 + 0.3 * i, 0.3)
        if q > 0:
            c = mix(LIGHT, RED, fade(t, t0 + 1.2, 0.6))
            d.text((CX + (i - 1) * 190 * SS, CY + 6 * SS), "?", font=font(170, "ExtraBold"), fill=mix((0, 0, 0), c, q),
                   anchor="mm")
    return finish(img)


KINDS["blank_bubble"] = blank_bubble


def door_closed(t, dur, args, at):
    """부모의 면회를 엄격하게 금지했습니다: a closed ward door (small window, handle) with a red no-entry sign."""
    img, d = canvas()
    w, h = 420 * SS, 640 * SS
    x0, y0 = CX - 300 * SS, CY - h / 2 + 30 * SS
    k = fade(t, 0.0, 0.3)
    col = mix((0, 0, 0), WHITE, k)
    d.rectangle([x0 - 40 * SS, y0 - 40 * SS, x0 + w + 40 * SS, y0 + h], outline=mix((0, 0, 0), GRAY, k), width=LW)
    d.rectangle([x0, y0, x0 + w, y0 + h], outline=col, width=LW)
    d.ellipse([x0 + w / 2 - 70 * SS, y0 + 80 * SS, x0 + w / 2 + 70 * SS, y0 + 220 * SS], outline=col, width=LW // 2 + SS)
    d.rounded_rectangle([x0 + w - 90 * SS, y0 + h / 2, x0 + w - 40 * SS, y0 + h / 2 + 22 * SS], radius=10 * SS, fill=col)
    q = fade(t, at_or(at, 0, 0.6), 0.35)
    if q > 0:
        cx, cy, r = CX + 330 * SS, CY - 20 * SS, 150 * SS
        c = mix((0, 0, 0), RED, q)
        d.ellipse([cx - r, cy - r, cx + r, cy + r], outline=c, width=LW + 4 * SS)
        d.rounded_rectangle([cx - r * 0.62, cy - 20 * SS, cx + r * 0.62, cy + 20 * SS], radius=10 * SS, fill=c)
    return finish(img)


def film_camera(t, dur, args, at):
    """카메라에 담았습니다: an old movie camera (two film reels on top, lens) on a tripod, line art; the reels turn."""
    img, d = canvas()
    k = fade(t, 0.0, 0.3)
    col = mix((0, 0, 0), WHITE, k)
    bx0, by0, bw, bh = CX - 260 * SS, CY - 80 * SS, 440 * SS, 240 * SS      # v2: raised, tripod ends at y 804 px
    d.rounded_rectangle([bx0, by0, bx0 + bw, by0 + bh], radius=28 * SS, outline=col, width=LW)
    d.polygon([(bx0 + bw, by0 + 70 * SS), (bx0 + bw + 150 * SS, by0 + 20 * SS), (bx0 + bw + 150 * SS, by0 + bh - 20 * SS),
               (bx0 + bw, by0 + bh - 70 * SS)], outline=col, width=LW)
    ang = t * 90
    for cx in (bx0 + 110 * SS, bx0 + 330 * SS):
        r, cy = 105 * SS, by0 - 110 * SS
        d.ellipse([cx - r, cy - r, cx + r, cy + r], outline=col, width=LW)
        d.ellipse([cx - 16 * SS, cy - 16 * SS, cx + 16 * SS, cy + 16 * SS], fill=col)
        for j in range(3):                                   # three spokes turning slowly (the film runs)
            a = math.radians(ang + j * 120)
            d.line([(cx + 30 * SS * math.cos(a), cy + 30 * SS * math.sin(a)),
                    (cx + 82 * SS * math.cos(a), cy + 82 * SS * math.sin(a))], fill=col, width=LW // 2 + 2 * SS)
    lx = bx0 + bw / 2
    for dx in (-150, 0, 150):                                # tripod
        d.line([(lx, by0 + bh), (lx + dx * SS, by0 + bh + 190 * SS)], fill=mix((0, 0, 0), GRAY, k), width=LW)
    return finish(img)


KINDS["door_closed"] = door_closed
KINDS["film_camera"] = film_camera
