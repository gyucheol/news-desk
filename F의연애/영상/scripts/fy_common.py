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
# Graphic text font (v2, 2026-10-24): the owner found the icon-screen lettering "too AI-like" (Pretendard, the subtitle
# font, everywhere). Chosen after a comparison sheet of three free fonts: Gmarket Sans (bold geometric, clearly
# different from the subtitle font, reads well at 1080p; free for commercial use, video included). Families below map
# our four weights to files in VIDEO_ROOT/fonts (setup.sh downloads them; FY_FONT=pretendard brings back the old look);
# "scale" evens out the Hangul glyph height against Pretendard, "dy" moves anchor-"mm" text to its true middle
# (fraction of the size; Gmarket Sans puts "mm" text 3% high). Gmarket Sans has no tabular digits: running numbers
# use tab_text(). The chat bubble text stays Noto Sans KR (noto()).
FAMILIES = {
    "pretendard": {"Medium": "Pretendard-Medium.otf", "SemiBold": "Pretendard-SemiBold.otf",
                   "Bold": "Pretendard-Bold.otf", "ExtraBold": "Pretendard-ExtraBold.otf", "scale": 1.0, "dy": 0.0},
    "gmarket": {"Medium": "GmarketSansMedium.otf", "SemiBold": "GmarketSansMedium.otf",
                "Bold": "GmarketSansBold.otf", "ExtraBold": "GmarketSansBold.otf", "scale": 1.0, "dy": 0.03},
    # the two below were only candidates on the comparison sheet; setup.sh does not download them
    "paperlogy": {"Medium": "Paperlogy-5Medium.otf", "SemiBold": "Paperlogy-6SemiBold.otf",
                  "Bold": "Paperlogy-7Bold.otf", "ExtraBold": "Paperlogy-8ExtraBold.otf", "scale": 1.0, "dy": 0.01},
    "nanumsquareround": {"Medium": "NanumSquareRoundR.ttf", "SemiBold": "NanumSquareRoundB.ttf",
                         "Bold": "NanumSquareRoundB.ttf", "ExtraBold": "NanumSquareRoundEB.ttf", "scale": 0.95, "dy": 0.01},
}
FAMILY = os.environ.get("FY_FONT", "gmarket")


def set_family(name):
    """Switch the graphic font (font comparison sheets); clears the font cache."""
    global FAMILY
    FAMILY = name
    _fonts.clear()


def font(px, weight="SemiBold"):
    """Graphic-text font of the current family at px output pixels; weight: Medium, SemiBold, Bold, ExtraBold."""
    key = (FAMILY, px, weight)
    if key not in _fonts:
        fam = FAMILIES[FAMILY]
        _fonts[key] = ImageFont.truetype(f"{ROOT}/fonts/{fam[weight]}", round(px * SS * fam["scale"]))
    return _fonts[key]


def mm_dy(px):
    """Pixels (drawing scale) to add to y for anchor-"mm" text of this size so the ink sits on the given middle."""
    return FAMILIES[FAMILY]["dy"] * px * SS


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
    x, y = xy
    if anchor[1] == "m":
        y += mm_dy(px)
    d.text((x, y), s, font=font(px, weight), fill=fill, anchor=anchor)


def tab_len(s, f):
    """Width of s when every digit sits in a cell as wide as the widest digit."""
    cell = max(f.getlength(c) for c in "0123456789")
    return sum(cell if c.isdigit() else f.getlength(c) for c in s)


def tab_text(d, xy, s, f, fill, anchor="ls"):
    """Text with tabular digits (each digit centred in a fixed cell), so a running count or clock does not wobble
    sideways (Gmarket Sans digits are proportional and the font has no tnum feature). anchor: l/m/r + PIL vertical."""
    cell = max(f.getlength(c) for c in "0123456789")
    parts, run = [], ""
    for c in s:
        if c.isdigit():
            if run:
                parts.append((run, f.getlength(run), False))
                run = ""
            parts.append((c, cell, True))
        else:
            run += c
    if run:
        parts.append((run, f.getlength(run), False))
    x, y = xy
    x -= {"l": 0.0, "m": 0.5, "r": 1.0}[anchor[0]] * sum(w for _, w, _ in parts)
    for p, w, dig in parts:
        d.text((x + ((w - f.getlength(p)) / 2 if dig else 0), y), p, font=f, fill=fill, anchor="l" + anchor[1])
        x += w


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
