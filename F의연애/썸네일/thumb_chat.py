# 「F의 연애」 썸네일: 채팅 확대판 (2026-10-22)
# 휴대폰 몸체 없이 카톡 대화 내용만 크게 보여 준다. 썸네일을 작게 봐도 노란 말풍선과 읽지 않은 '1'이 눈에 들어오게.
# 말풍선 모양·색·비율과 '1'·시간 위치는 사용자가 보내 준 갤럭시 카톡 화면에서 잰 값이다(2026-10-22).
# 갤럭시 기본 글꼴은 기기 전용이라 쓸 수 없어서, 같은 높이로 맞춰 비교했을 때 너비·굵기가 가장 가까운
# Noto Sans KR(OFL) 굵기 450을 쓴다(너비 98.9%, 획 굵기 102.8%).
# 말풍선은 기울이지 않고 똑바로 둔다. 아래에 주제 단어(thumb.py와 같은 글꼴·위치, 기본 흰색).
#
# usage: thumb_chat.py OUT.jpg [--theme dark|light] [--word 불안] [--color white|red]   (기본: dark, white)
#                              [--msgs "a|b|c"] [--times "오후 6:12|오후 8:43|오후 11:50"] [--size 262]
#   --size : 주제 단어 글자 크기(px, 기본 262). 01편 '불안형'은 259(2026-10-26 사용자: "3p만 줄이자").
#   --times: 메시지마다 보낸 시각. 분이 다르면 카톡은 말풍선마다 꼬리를 새로 달고, 왼쪽에 '1'과 시간을 위아래로 둔다.
#   light: 카톡 기본 테마(하늘색 배경) 화면 조각을 검은 배경 위에 둔다
#   dark : 카톡 다크 테마처럼 검은 화면에 노란 말풍선만
import os, sys
import numpy as np
from PIL import Image, ImageDraw, ImageFilter, ImageFont

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from thumb import W, H, FONT_DIR, WORD_SIZE, bottom_fade, put_word   # noqa: E402

S = 2                                   # draw at 2x, then downsample
BUBBLE = (253, 229, 0)                  # measured on the Galaxy screenshot
TEXT = (24, 24, 24)
ONE = (246, 222, 18)
THEMES = {"light": dict(bg=(171, 192, 209), time=(84, 96, 106)),   # bg measured; time from the darkest time pixels
          "dark": dict(bg=(22, 22, 24), time=(150, 152, 156))}     # dark-mode values are approximate (no reference)
# proportions relative to the bubble height h (Galaxy screenshot: h = 105 px)
R_RADIUS, R_TEXT, R_PADL, R_PADR, R_GAP = 0.40, 0.37, 0.32, 0.36, 0.22
R_ONE = 0.28        # real '1' is about 0.22 h tall; a little larger so it still shows on a small thumbnail
R_TIME = 0.24


def noto(weight, px_height, sample="원하는거 올릴수있게변함"):
    """Noto Sans KR at the size whose glyph box for `sample` is px_height tall."""
    path = f"{FONT_DIR}/NotoSansKR-VF.ttf"
    size = max(8, round(px_height * 1.08))
    for _ in range(6):
        f = ImageFont.truetype(path, size)
        f.set_variation_by_axes([weight])
        bb = f.getbbox(sample)
        size = max(8, round(size * px_height / max(1, bb[3] - bb[1])))
    f = ImageFont.truetype(path, size)
    f.set_variation_by_axes([weight])
    return f


def draw_chat(d, msgs, right, top, h, theme, times):
    """My messages, Galaxy KakaoTalk style: yellow pill bubbles right-aligned at x=right, '1' on the left of each.
    times: one entry per message (None = no time shown). A message with a time closes its minute group, so the next
    bubble starts a new group and gets the tail again, as on the real screen. Returns the bounding box drawn."""
    ft, f1, fm = noto(450, R_TEXT * h), noto(700, R_ONE * h, "1"), noto(400, R_TIME * h, "오후 11:52")
    y, box = top, [right, top, right, top]
    new_group = True
    for i, m in enumerate(msgs):
        time = times[i] if i < len(times) else None
        bb = ft.getbbox(m)
        bw = (bb[2] - bb[0]) + (R_PADL + R_PADR) * h
        x1, x0 = right, right - bw
        d.rounded_rectangle([x0, y, x1, y + h], radius=R_RADIUS * h, fill=BUBBLE)
        if new_group:   # tail on the first bubble of each group (top right)
            d.polygon([(x1 - 0.30 * h, y), (x1 + 0.13 * h, y + 0.02 * h), (x1 - 0.02 * h, y + 0.26 * h)], fill=BUBBLE)
        d.text((x0 + R_PADL * h - bb[0], y + h / 2), m, font=ft, fill=TEXT, anchor="lm")
        one_bottom = y + h - (0.46 if time else 0.12) * h
        d.text((x0 - 0.10 * h, one_bottom), "1", font=f1, fill=ONE, anchor="rs")
        if time:
            d.text((x0 - 0.10 * h, y + h - 0.10 * h), time, font=fm, fill=THEMES[theme]["time"], anchor="rs")
            box[0] = min(box[0], x0 - 0.10 * h - fm.getlength(time))
        box[0] = min(box[0], x0 - 0.10 * h - f1.getlength("1"))
        new_group = bool(time)
        y += h + R_GAP * h
    box[3] = y - R_GAP * h
    return box


def make_light(msgs, times, h=100):
    """A crop of the default-theme chat screen (light blue) floating on black, softly lit."""
    CW, CH = W * S, H * S
    hh = h * S
    # measure the chat block first, then size the screen crop around it
    probe = Image.new("RGB", (CW, CH)); bx = draw_chat(ImageDraw.Draw(probe), msgs, CW, 0, hh, "light", times)
    bw, bh = CW - bx[0], bx[3] - bx[1]
    pad_l, pad_r, pad_v = 70 * S, 34 * S, 40 * S
    cw, ch = round(bw + pad_l + pad_r), round(bh + 2 * pad_v)
    cx0, cy0 = (CW - cw) // 2, 24 * S                 # crop ends well above the title
    card = Image.new("RGB", (cw, ch), THEMES["light"]["bg"])
    draw_chat(ImageDraw.Draw(card), msgs, cw - pad_r, pad_v, hh, "light", times)
    img = Image.new("RGB", (CW, CH), (0, 0, 0))
    glow = Image.new("L", (CW, CH), 0)          # screen light spilling into the dark around the crop
    ImageDraw.Draw(glow).rounded_rectangle([cx0 - 20 * S, cy0 - 10 * S, cx0 + cw + 20 * S, cy0 + ch + 30 * S], radius=60 * S, fill=110)
    glow = glow.filter(ImageFilter.GaussianBlur(60 * S))
    img = Image.composite(Image.new("RGB", (CW, CH), (60, 72, 84)), img, glow)
    m = Image.new("L", (cw, ch), 0)
    ImageDraw.Draw(m).rounded_rectangle([0, 0, cw - 1, ch - 1], radius=26 * S, fill=255)
    img.paste(card, (cx0, cy0), m)
    return finish(img)


def make_dark(msgs, times, h=100):
    """Dark-theme chat: black screen, only my yellow bubbles, a soft glow like a lit screen in a dark room."""
    CW, CH = W * S, H * S
    hh = h * S
    probe = Image.new("RGB", (CW, CH)); bx = draw_chat(ImageDraw.Draw(probe), msgs, CW, 0, hh, "dark", times)
    bw = CW - bx[0]
    right = (CW + bw) / 2
    img = Image.new("RGB", (CW, CH), THEMES["dark"]["bg"])
    draw_chat(ImageDraw.Draw(img), msgs, right, 34 * S, hh, "dark", times)
    a = np.asarray(img, np.float32)
    lum = a.mean(2)
    bright = Image.fromarray(np.clip((lum - 120) * 2, 0, 255).astype(np.uint8)).filter(ImageFilter.GaussianBlur(26 * S))
    a += (np.asarray(bright, np.float32) / 255)[..., None] * np.array([60, 50, 12], np.float32)
    return finish(Image.fromarray(np.clip(a, 0, 255).astype(np.uint8)))


def finish(img):
    """Edges fall off to black (dark room), faint noise, downsample to 1280x720."""
    CW, CH = img.size
    a = np.asarray(img, np.float32)
    yy, xx = np.mgrid[0:CH, 0:CW].astype(np.float32)
    r = np.sqrt(((xx - 0.50 * CW) / (0.64 * CW)) ** 2 + ((yy - 0.38 * CH) / (0.64 * CH)) ** 2)
    v = np.clip(1 - (r - 0.62) / 0.45, 0, 1)
    a *= (v * v * (3 - 2 * v))[..., None]
    a += np.random.default_rng(3).normal(0, 1.2, a.shape)
    return Image.fromarray(np.clip(a, 0, 255).astype(np.uint8)).resize((W, H), Image.LANCZOS)


if __name__ == "__main__":
    a = sys.argv[1:]
    opt = lambda k, dflt: a[a.index(k) + 1] if k in a else dflt
    msgs = opt("--msgs", "오늘 하루 어땠어요?|바빠요? ㅎㅎ|자요..?").split("|")
    if "--times" in a:
        times = [t.strip() or None for t in opt("--times", "").split("|")]
    elif "--time" in a:                      # one time under the last message only
        times = [None] * (len(msgs) - 1) + [opt("--time", "")]
    else:                                    # 01편: 저녁 6:12, 8:43, 밤 11:50에 하나씩 보냄(2026-10-22 사용자 지정)
        times = ["오후 6:12", "오후 8:43", "오후 11:50"]
    img = (make_light if opt("--theme", "dark") == "light" else make_dark)(msgs, times)   # 기본 다크(2026-10-22 사용자 결정)
    img = bottom_fade(img, 405, 520)
    put_word(img, opt("--word", "불안"), opt("--color", "white"), int(opt("--size", WORD_SIZE))).save(a[0], quality=93)
    print(a[0])
