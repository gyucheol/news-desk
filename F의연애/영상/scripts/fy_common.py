# Shared drawing helpers for the F의 연애 icon screens (2026-10-24). Same look as icons.py (guide 6-3): black background,
# white line art, one accent colour (yellow = attention, red = warning), drawn at 2x (SS) then downsampled to 1920x1080.
# Every icon function has the signature  fn(t, dur, args, at) -> PIL RGB image, 1920x1080:
#   t    seconds since the scene started, dur = scene length (s)
#   args dict from the scene spec (may be {}), at = list of seconds (from the scene start) when the listed subtitle lines
#        start being spoken (may be shorter than expected or empty: then use sensible defaults)
import math, os
from PIL import Image, ImageDraw, ImageFilter, ImageFont

W, H, SS = 1920, 1080, 2
WHITE, GRAY, DIM, LIGHT = (255, 255, 255), (110, 110, 110), (55, 55, 55), (170, 170, 170)
YEL, RED = (242, 201, 76), (229, 72, 77)            # channel yellow #F2C94C, warning red
KAKAO, KAKAO_TEXT, KAKAO_ONE = (253, 229, 0), (24, 24, 24), (246, 222, 18)   # measured on the owner's Galaxy screen
ROOT = os.environ.get("VIDEO_ROOT", os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
CX, CY = W * SS / 2, H * SS * 0.42                 # icon centre, above the bottom subtitle area (box top y=918 px)
SAFE_BOTTOM = 860 * SS                             # keep drawings above this line (subtitle box starts at 918 px)
LW = 12 * SS
_fonts = {}


def font(px, weight="SemiBold"):
    """Pretendard (OFL) at px output pixels; weight: Medium, SemiBold, Bold, ExtraBold."""
    key = ("p", px, weight)
    if key not in _fonts:
        _fonts[key] = ImageFont.truetype(f"{ROOT}/fonts/Pretendard-{weight}.otf", round(px * SS))
    return _fonts[key]


def noto(px, weight=450):
    """Noto Sans KR variable font (chat text, as in the 01 thumbnail: weight 450 is closest to the Galaxy font)."""
    key = ("n", px, weight)
    if key not in _fonts:
        f = ImageFont.truetype(f"{ROOT}/fonts/NotoSansKR-VF.ttf", round(px * SS))
        f.set_variation_by_axes([weight])
        _fonts[key] = f
    return _fonts[key]


def sm(u):
    u = min(max(u, 0.0), 1.0)
    return u * u * (3 - 2 * u)


def mix(c1, c2, u):
    u = min(max(u, 0.0), 1.0)
    return tuple(round(a + (b - a) * u) for a, b in zip(c1, c2))


def fade(t, t0, d=0.35):
    """0 before t0, eases to 1 over d seconds."""
    return sm((t - t0) / d)


def canvas():
    img = Image.new("RGB", (W * SS, H * SS), (0, 0, 0))
    return img, ImageDraw.Draw(img)


def text(d, xy, s, px, fill=WHITE, anchor="mm", weight="SemiBold"):
    d.text(xy, s, font=font(px, weight), fill=fill, anchor=anchor)


def glow(img, box, colour, strength, blur=60):
    """Soft light behind an element (strength 0..1)."""
    if strength <= 0:
        return img
    m = Image.new("L", img.size, 0)
    ImageDraw.Draw(m).ellipse(box, fill=round(150 * strength))
    m = m.filter(ImageFilter.GaussianBlur(blur * SS))
    return Image.composite(Image.new("RGB", img.size, colour), img, m)


def at_or(at, i, default):
    """The i-th voice time if given, else default (seconds from the scene start)."""
    return at[i] if at is not None and i < len(at) and at[i] is not None else default


def finish(img):
    return img.resize((W, H), Image.LANCZOS)
