# Drawings over the owner's photos for F의 연애 01 v3 (2026-10-25), used by render.py photo scenes ("overlay").
# Every function: fn(t, dur, args, at, view) -> RGBA 1920x1080 (transparent where nothing is drawn).
#   t = seconds since the scene started, dur = scene length, args = dict from the spec (may be {}),
#   at = voice onsets of the listed subtitle lines in seconds from the scene start (may be shorter: defaults are used),
#   view = the part of the photo on screen (x0, y0, w, h) in 0..1 of the photo, so a drawing stays on the photo's
#   subject while the photo slowly zooms.
# Same rules as the icon screens: text in the graphic font (fy_common, Gmarket Sans), red only for a warning, no shake,
# flicker or blinking, only smooth fades and slow growth.
from fy_common import FAMILIES, FAMILY, RED, ROOT, W, H, WHITE, mix
from PIL import Image, ImageDraw, ImageFilter, ImageFont

_fonts = {}


def _font(px):
    """The graphic font (bold) at px output pixels (drawn at 1x: the glyph edges are anti-aliased by FreeType)."""
    if px not in _fonts:
        _fonts[px] = ImageFont.truetype(f"{ROOT}/fonts/{FAMILIES[FAMILY]['ExtraBold']}", px)
    return _fonts[px]


def _sm(u):
    u = min(max(u, 0.0), 1.0)
    return u * u * (3 - 2 * u)


def _lerp(a, b, u):
    return a + (b - a) * u


def _screen(view, u, v):
    x0, y0, w, h = view
    return (u - x0) / w * W, (v - y0) / h * H


def brain_unknown(t, dur, args, at, view):
    """Photo 4 (brain on a plinth under a spotlight) for '원래 인간의 뇌는 / 알 수 없는 상태를 / 우리가 생각하는 것보다 /
    훨씬 더 무겁고 / 위협적으로 받아들이도록 / 설계되어 있거든요'. The owner: "이 사진을 활용해서 … 를 잘 설명할 수 있게".
    at[0] '알 수 없는 상태를': a white '?' fades in above the brain, in the light.
    at[1] '훨씬 더 무겁고': the '?' grows and settles down onto the top of the brain (no bounce); its shadow darkens the
          top of the brain, so it reads as a weight pressing on it.
    at[2] '위협적으로': the '?' turns red while the photo turns the brain red (render.py "mix" to 04_red.png).
    Positions are in 0..1 of the photo (measured: brain x 0.33-0.67, top of the brain at y 0.290 in the middle)."""
    at = list(at) + [1.2, 3.5, 4.6][len(at):]
    k_in, k_grow, k_red = _sm((t - at[0]) / 0.4), _sm((t - at[1]) / 0.9), _sm((t - at[2]) / 0.6)
    layer = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    if k_in <= 0:
        return layer
    zoom = 1 / view[3]                                    # screen px per photo-height unit / H
    h_ink = _lerp(0.18, 0.25, k_grow)                     # height of the '?' (photo heights)
    bottom = _lerp(0.25, 0.293, k_grow)                   # its lowest point; 0.293 = resting on the brain
    cx, cy = _screen(view, 0.5, bottom - h_ink / 2)
    px = round(h_ink * H * zoom / 0.74)                   # Gmarket Sans Bold '?': ink height about 0.74 of the size
    f = _font(px)
    l, tp, r, b = f.getbbox("?", anchor="ls")
    pos = (cx - (l + r) / 2, cy - (tp + b) / 2)
    # contact shadow on the top of the brain, growing with the weight
    if k_grow > 0:
        sx, sy = _screen(view, 0.5, 0.300)
        rx, ry = 0.065 * H * zoom, 0.020 * H * zoom
        sh = Image.new("L", (W, H), 0)
        ImageDraw.Draw(sh).ellipse([sx - rx, sy - ry, sx + rx, sy + ry], fill=round(190 * k_grow * k_in))
        sh = sh.filter(ImageFilter.GaussianBlur(12 * zoom))
        layer.putalpha(sh)                                # black, alpha = the shadow
    # the '?' with a soft dark halo so it reads on the lit wall
    q = Image.new("L", (W, H), 0)
    ImageDraw.Draw(q).text(pos, "?", font=f, fill=255, anchor="ls")
    halo = q.filter(ImageFilter.GaussianBlur(10)).point(lambda v: round(min(255, v * 1.4) * 0.55 * k_in))
    dark = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    dark.putalpha(halo)
    layer.alpha_composite(dark)
    col = mix(WHITE, RED, k_red)
    glyph = Image.new("RGBA", (W, H), col + (0,))
    glyph.putalpha(q.point(lambda v: round(v * k_in)))
    layer.alpha_composite(glyph)
    return layer


OVERLAYS = {"brain_unknown": brain_unknown}
