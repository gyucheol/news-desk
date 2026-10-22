# 「F의 연애」 썸네일 틀 (초안, 2026-10-22)
# 검은 배경 + 가운데 핵심 물체 하나(VOX 느낌) + 아래에 주제 단어를 크게(흰색 또는 빨간색). 1280x720.
#
# usage:
#   thumb.py phone OUT.jpg --word 불안 --color white|red [--msgs "메시지1|메시지2|메시지3"] [--name "그 사람"]
#       나만 보내고 답이 없는 채팅 화면의 휴대폰을 직접 그린다(앱 로고·상표 없음).
#   thumb.py photo OUT.jpg IMAGE --word 불안 --color red [--crop x0,y0,x1,y1] [--gamma 1.3]
#       사진(스톡 영상의 한 장면 등)을 가운데에 두고 가장자리를 검게 감싼다.
# env FONT_DIR: Pretendard-Bold/SemiBold.otf(OFL)와 NotoSansKR-VF.ttf(Noto Sans KR 가변 글꼴, OFL)가 있는 폴더
# 주제 단어 글꼴(2026-10-22 갱신): Noto Sans KR 800(ExtraBold). Pretendard Black은 사용자가 촌스럽다고 해서 바꿈.
import math, os, sys
import numpy as np
from PIL import Image, ImageDraw, ImageFilter, ImageFont

W, H = 1280, 720
FONT_DIR = os.environ.get("FONT_DIR", os.path.join(os.path.dirname(os.path.abspath(__file__)), "fonts"))
COLORS = {"white": (255, 255, 255), "red": (230, 40, 48)}   # 맑은 빨강(채도 높고 분홍기 없음)
YEL = (242, 201, 76)                                       # #F2C94C, 채널 강조색
WORD_SIZE, WORD_BASE, WORD_WEIGHT = 236, 680, 800          # 주제 단어 크기, 글자 바닥선(y), 굵기 (2026-10-22: 186 → 236, 사용자 요청)


def font(weight, size):
    return ImageFont.truetype(f"{FONT_DIR}/Pretendard-{weight}.otf", size)


def vgrad(w, h, c0, c1):
    g = np.linspace(0, 1, h)[:, None, None]
    a = np.array(c0, np.float32) * (1 - g) + np.array(c1, np.float32) * g
    return Image.fromarray(np.repeat(a, w, axis=1).astype(np.uint8), "RGB")


def phone(msgs, name="그 사람", width=425, S=3):
    """Drawn phone (dark mode chat): only my yellow bubbles, each with the unread '1'. Returns RGBA, `width` px wide."""
    pw, ph, r = 340 * S, 700 * S, 56 * S
    body = Image.new("RGBA", (pw, ph), (0, 0, 0, 0))
    outer = Image.new("L", (pw, ph), 0)
    ImageDraw.Draw(outer).rounded_rectangle([0, 0, pw - 1, ph - 1], radius=r, fill=255)
    body.paste(vgrad(pw, ph, (112, 112, 118), (34, 34, 38)), (0, 0), outer)          # metal rim
    d = ImageDraw.Draw(body)
    b = 5 * S
    d.rounded_rectangle([b, b, pw - 1 - b, ph - 1 - b], radius=r - b, fill=(6, 6, 7, 255))  # black glass bezel
    sb = 15 * S
    sw, sh, sr = pw - 2 * sb, ph - 2 * sb, r - sb + 5 * S
    scr = Image.new("RGBA", (sw, sh), (22, 24, 30, 255))
    sd = ImageDraw.Draw(scr)
    # header: back chevron, round avatar, name
    hy = 84 * S
    sd.line([(30 * S, hy - 12 * S), (20 * S, hy), (30 * S, hy + 12 * S)], fill=(225, 225, 230), width=3 * S, joint="curve")
    sd.ellipse([46 * S, hy - 18 * S, 82 * S, hy + 18 * S], fill=(92, 98, 112))
    sd.text((94 * S, hy), name, font=font("SemiBold", 22 * S), fill=(235, 235, 240), anchor="lm")
    sd.line([(0, 118 * S), (sw, 118 * S)], fill=(44, 47, 56), width=S)
    # my bubbles on the right, with the unread "1" on their left
    fb, f1 = font("SemiBold", 23 * S), font("Bold", 25 * S)
    y = 140 * S
    for i, m in enumerate(msgs):
        tw = fb.getlength(m)
        bw, bh = tw + 32 * S, 50 * S
        x1 = sw - 18 * S
        x0 = x1 - bw
        sd.rounded_rectangle([x0, y, x1, y + bh], radius=17 * S, fill=YEL)
        if i == 0:   # tail on the first bubble of the run
            sd.polygon([(x1 - 22 * S, y), (x1 + 9 * S, y + 4 * S), (x1 - 2 * S, y + 20 * S)], fill=YEL)
        sd.text(((x0 + x1) / 2, y + bh / 2 + S), m, font=fb, fill=(30, 26, 18), anchor="mm")
        sd.text((x0 - 8 * S, y + bh - 3 * S), "1", font=f1, fill=YEL, anchor="rs")
        y += bh + 14 * S
    smask = Image.new("L", (sw, sh), 0)
    ImageDraw.Draw(smask).rounded_rectangle([0, 0, sw - 1, sh - 1], radius=sr, fill=255)
    body.paste(scr, (sb, sb), smask)
    d.rounded_rectangle([pw / 2 - 52 * S, sb + 14 * S, pw / 2 + 52 * S, sb + 46 * S], radius=16 * S, fill=(0, 0, 0, 255))
    # faint diagonal glass reflection, screen only
    refl = Image.new("L", (pw, ph), 0)
    ImageDraw.Draw(refl).polygon([(pw * 0.62, 0), (pw * 1.0, 0), (pw * 0.30, ph), (-pw * 0.08, ph)], fill=13)
    sm = Image.new("L", (pw, ph), 0)
    sm.paste(smask, (sb, sb))
    refl = Image.fromarray((np.asarray(refl, np.float32) * np.asarray(sm, np.float32) / 255).astype(np.uint8))
    body.alpha_composite(Image.merge("RGBA", (*Image.new("RGB", (pw, ph), (255, 255, 255)).split(), refl)))
    return body.resize((width, round(width * ph / pw)), Image.LANCZOS)


def bottom_fade(img, y0, y1):
    """Fade the picture to black from y0 to y1 so the word sits on black."""
    a = np.asarray(img, np.float32)
    g = np.clip((np.arange(H, dtype=np.float32) - y0) / (y1 - y0), 0, 1)
    g = g * g * (3 - 2 * g)
    a *= (1 - g)[:, None, None]
    return Image.fromarray(a.round().astype(np.uint8), "RGB")


def word_font(size=WORD_SIZE, weight=WORD_WEIGHT):
    f = ImageFont.truetype(f"{FONT_DIR}/NotoSansKR-VF.ttf", size)
    f.set_variation_by_axes([weight])
    return f


def put_word(img, word, color):
    """Topic word: clean heavy gothic, centered, with a soft dark shadow underneath for depth."""
    f = word_font()
    sh = Image.new("L", (W, H), 0)
    ImageDraw.Draw(sh).text((W / 2, WORD_BASE + 6), word, font=f, fill=235, anchor="ms")
    sh = sh.filter(ImageFilter.GaussianBlur(14))
    img = Image.composite(Image.new("RGB", (W, H), (0, 0, 0)), img, sh)
    ImageDraw.Draw(img).text((W / 2, WORD_BASE), word, font=f, fill=COLORS.get(color, color), anchor="ms")
    return img


def make_phone(out, word, color, msgs, name):
    canvas = Image.new("RGB", (W, H), (0, 0, 0))
    ph = phone(msgs, name)
    x, y = (W - ph.width) // 2, 24
    glow = Image.new("L", (W, H), 0)   # light spill from the screen so the phone separates from black
    ImageDraw.Draw(glow).rounded_rectangle([x - 20, y + 30, x + ph.width + 20, y + 500], radius=120, fill=80)
    glow = glow.filter(ImageFilter.GaussianBlur(70))
    canvas = Image.composite(Image.new("RGB", (W, H), (38, 44, 58)), canvas, glow)
    canvas.paste(ph, (x, y), ph)
    canvas = bottom_fade(canvas, 450, 590)
    put_word(canvas, word, color).save(out, quality=92)


def make_photo(out, src, word, color, crop=None, gamma=1.3):
    im = Image.open(src).convert("RGB")
    if crop:
        im = im.crop(crop)
    im = im.resize((W, H), Image.LANCZOS)
    a = np.asarray(im, np.float32) / 255
    lum = a @ np.array([0.2126, 0.7152, 0.0722], np.float32)
    a = lum[..., None] + (a - lum[..., None]) * 0.85            # mute colors a little
    a = np.clip(a, 0, 1) ** gamma                               # darker mids
    yy, xx = np.mgrid[0:H, 0:W].astype(np.float32)
    rr = np.sqrt(((xx - W / 2) / (W * 0.46)) ** 2 + ((yy - H * 0.40) / (H * 0.52)) ** 2)
    v = np.clip(1 - (rr - 0.55) / 0.55, 0, 1)                   # strong vignette into black
    a *= (v * v * (3 - 2 * v))[..., None]
    canvas = Image.fromarray((np.clip(a, 0, 1) * 255).round().astype(np.uint8), "RGB")
    canvas = bottom_fade(canvas, 430, 580)
    put_word(canvas, word, color).save(out, quality=92)


if __name__ == "__main__":
    a = sys.argv[1:]
    opt = lambda k, dflt: a[a.index(k) + 1] if k in a else dflt
    mode, out = a[0], a[1]
    word, color = opt("--word", "불안"), opt("--color", "white")
    if mode == "phone":
        msgs = opt("--msgs", "오늘 하루 어땠어요?|바빠요? ㅎㅎ|자요..?").split("|")
        make_phone(out, word, color, msgs, opt("--name", "그 사람"))
    else:
        crop = tuple(int(v) for v in opt("--crop", "").split(",")) if "--crop" in a else None
        make_photo(out, a[2], word, color, crop, float(opt("--gamma", "1.3")))
    print(out)
