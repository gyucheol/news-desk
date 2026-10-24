# Render a Short (1080x1920) from a timeline made by build_short.py, with render.py's look (grade, cards, icons),
# but the picture fills the vertical frame and all text stays inside the area that the Shorts/Reels buttons and
# captions do not cover.
# usage: render_short.py short_timeline.json out.mp4 [--frames-only t1,t2,...] [--guides]
#   --guides (with --frames-only): also draw the covered areas in red, to check the layout.
#
# Covered areas on a 1080x1920 frame (2026-10-24):
#   Google (vertical video ads on YouTube Shorts, the figures safe-zone tools quote from its help image): top 288,
#   bottom 672, left 48, right 192 px (right: like/dislike/comment/share/remix; bottom: channel, title, sound).
#   Meta (Reels ads): top 14% (270), bottom 35% (672), sides 6% (65 px).
#   Text is kept inside x 65..888, y 288..1248, the area clear on both.
# Subtitle style comes from the timeline's "sub_style" (full/shorts/<id>.json): without it, the episode's boxed
# subtitles sit above y 1220. S1 v2 (owner, 2026-10-24): no box, white text with a dark outline, one line only, its
# middle at y 1280 (the lower-third point the owner asked for; 32 px below the ad-guidance line 1248 above).
import json, math, os, subprocess, sys
import numpy as np
from PIL import Image, ImageDraw, ImageFilter

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import render as RD
import icons as IC

W, H = 1080, 1920
SAFE_L, SAFE_R, SAFE_T, SAFE_B = 65, W - 192, 288, H - 672
SUB_BOTTOM = 1220            # bottom edge of the subtitle box (28 px above the covered bottom area)
RD.W, RD.H = W, H
IC.W, IC.H = W, H
IC.CX, IC.CY = W * IC.SS / 2, H * IC.SS * 0.40
FONT, CFONT = RD.font, RD.center_font
FS, CS, GAP, PAD = RD.FONT_SIZE, RD.CENTER_SIZE, RD.LINE_GAP, RD.PAD_X
ONE_LINE_BOX = 84            # same as the episode (918..1002 at 1080p)
STYLE = {}                   # the timeline's sub_style, read in __main__
shifts = []
fitted = []
_fonts = {}


def sized_font(px):
    if px not in _fonts:
        _fonts[px] = RD.ImageFont.truetype(RD.FONT_PATH, px)
    return _fonts[px]


def draw_outlined(layer, lines, xs, bases, f, stroke):
    """Text with a dark outline and a soft shadow, for subtitles without a box: outlines first, then all the fills,
    so an outline never covers the letter next to it (the yellow word and its particle touch)."""
    out = Image.new("RGBA", layer.size, (0, 0, 0, 0))
    d = ImageDraw.Draw(out)
    for segs, x0, base in zip(lines, xs, bases):
        x = x0
        for s, _ in segs:
            d.text((x, base), s, font=f, fill=(0, 0, 0, 255), anchor="ls", stroke_width=stroke, stroke_fill=(0, 0, 0, 255))
            x += f.getlength(s)
    sh = Image.new("RGBA", layer.size, (0, 0, 0, 0))
    sh.putalpha(out.getchannel("A").filter(ImageFilter.GaussianBlur(6)).point(lambda v: round(v * 0.55)))
    layer.alpha_composite(sh)
    layer.alpha_composite(out)
    for segs, x0, base in zip(lines, xs, bases):
        RD.draw_line(layer, segs, x0, base, f)


def centre_x(w):
    """Centre the block on the frame; if it would reach the right-hand buttons, move it left just enough."""
    cx = min(W / 2, SAFE_R - w / 2)
    if cx - w / 2 < SAFE_L:
        raise SystemExit(f"text block {w:.0f}px is wider than the safe area; break the line")
    return cx


def text_layer(sub, upto=None):
    layer = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    lines = [RD.parse_markup(l) for l in sub["text"].split("\n")]
    n = len(lines)
    if STYLE.get("one_line") and n > 1 and not sub.get("lines_ok"):
        raise SystemExit(f"{sub['line']}: two lines on screen ({sub['text']!r}); the owner wants one line only")
    if sub.get("pos", "bottom") == "center":
        px = sub.get("size") or CS
        if px == "fit":                       # the largest size whose widest line fits centred, left of the buttons
            px = next(p for p in range(sub.get("max_size", CS), 10, -1)
                      if max(RD.text_width(l, sized_font(p)) for l in lines) <= 2 * (SAFE_R - W / 2))
            fitted.append((sub["line"], px))
        f = sized_font(px) if px != CS else CFONT
        k = px / FS
        widths = [RD.text_width(l, f) for l in lines]
        cx = centre_x(max(widths))
        if cx != W / 2:
            shifts.append((sub["line"], round(W / 2 - cx)))
        first = H / 2 - RD.GLYPH_MID * k - (n - 1) * GAP * k / 2
        txt = Image.new("RGBA", (W, H), (0, 0, 0, 0))
        for i, (segs, w) in enumerate(zip(lines, widths)):
            RD.draw_line(txt, segs, cx - w / 2, first + i * GAP * k, f)
        if sub.get("italic"):
            txt = RD.slant(txt, H / 2)
        if sub.get("shadow"):
            sh = Image.new("RGBA", (W, H), (0, 0, 0, 0))
            sh.putalpha(txt.getchannel("A").filter(ImageFilter.GaussianBlur(9)).point(lambda v: min(255, v * 2)))
            layer.alpha_composite(sh)
        layer.alpha_composite(txt)
        return layer
    widths = [RD.text_width(l) for l in lines]
    if STYLE.get("box") is False:             # no box: outlined text, middle of the (single) line at y_center
        stroke = STYLE.get("outline", 3)
        block = max(widths) + 2 * stroke
        cx = centre_x(block)
        if cx != W / 2:
            shifts.append((sub["line"], round(W / 2 - cx)))
        base0 = STYLE.get("y_center", SUB_BOTTOM - ONE_LINE_BOX / 2) - RD.GLYPH_MID - (n - 1) * GAP / 2
        txt = Image.new("RGBA", (W, H), (0, 0, 0, 0))
        draw_outlined(txt, lines, [cx - w / 2 for w in widths], [base0 + i * GAP for i in range(n)], FONT, stroke)
        if sub.get("italic"):
            txt = RD.slant(txt, STYLE.get("y_center", H / 2))
        layer.alpha_composite(txt)
        return layer
    boxed = sub.get("box", True)
    block = max(widths) + (2 * PAD if boxed else 0)
    cx = centre_x(block)
    if cx != W / 2:
        shifts.append((sub["line"], round(W / 2 - cx)))
    box_h = ONE_LINE_BOX + (n - 1) * GAP
    top = SUB_BOTTOM - box_h
    if boxed:
        ImageDraw.Draw(layer).rectangle([round(cx - block / 2), top, round(cx + block / 2), SUB_BOTTOM], fill=RD.BOX_RGBA)
    mid0 = top + ONE_LINE_BOX / 2
    txt = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    for i, (segs, w) in enumerate(zip(lines, widths)):
        RD.draw_line(txt, segs, cx - w / 2, mid0 - RD.GLYPH_MID + i * GAP)
    if sub.get("italic"):
        txt = RD.slant(txt, (top + SUB_BOTTOM) / 2)
    layer.alpha_composite(txt)
    return layer


_size = {}


def probe(path):
    if path not in _size:
        r = subprocess.run(["ffprobe", "-v", "error", "-select_streams", "v", "-show_entries", "stream=width,height",
                            "-of", "csv=p=0", path], capture_output=True, text=True, check=True)
        _size[path] = tuple(int(v) for v in r.stdout.strip().split(","))
    return _size[path]


class VideoSource(RD.VideoSource):
    """As in render.py, but the crop that fills the frame sits where the scene's 'vcx' says (0..1 of the width)."""

    def _start(self):
        w, h = self.size
        sc = self.sc
        iw, ih = probe(sc["src"])
        c = sc.get("crop") or [0.0, 0.0, 1.0, 1.0]
        cw, ch = iw * (c[2] - c[0]), ih * (c[3] - c[1])
        s = max(w / cw, h / ch)
        sw, sh = max(w, round(cw * s / 2) * 2), max(h, round(ch * s / 2) * 2)
        x = min(max(sc.get("vcx", 0.5) * sw - w / 2, 0), sw - w)
        pre = f"crop=iw*{c[2] - c[0]:.4f}:ih*{c[3] - c[1]:.4f}:iw*{c[0]:.4f}:ih*{c[1]:.4f}," if sc.get("crop") else ""
        post = f",gblur=sigma={sc['blur']}" if sc.get("blur") else ""
        vf = (f"{pre}setpts=PTS/{sc.get('speed', 1.0)},fps={RD.FPS},scale={sw}:{sh}:flags=lanczos,"
              f"crop={w}:{h}:{round(x)}:{(sh - h) // 2}{post}")
        self.proc = subprocess.Popen(["ffmpeg", "-v", "error", "-ss", str(sc.get("in", 0)), "-i", sc["src"],
                                      "-vf", vf, "-f", "rawvideo", "-pix_fmt", "rgb24", "-"],
                                     stdout=subprocess.PIPE, stderr=subprocess.DEVNULL)
        self.k = -1


def battery2_vertical(t, dur):
    """icons.battery2 for a tall frame: the two batteries one above the other (ordinary tiredness on top)."""
    img, d = IC.canvas()
    S = IC.SS
    bw, bh = 340 * S, 160 * S
    x = IC.CX - 9 * S                       # the terminal sticks out 26 px on the right; keep the whole shape centred
    yt, yb = 520 * S, 840 * S
    k = IC.sm((t - 0.3) / 2.2)
    IC.battery_shape(d, x, yt, bw, bh, 0.18 + 0.8 * k, IC.WHITE, bolt=IC.sm(t / 0.3))
    blink = 1.0 if t < 1.5 else (0.4 if int(t * 3) % 2 else 1.0)
    IC.battery_shape(d, x, yb, bw, bh, 0.1 + 0.03 * math.sin(t * 2), IC.mix((0, 0, 0), IC.RED, blink), bolt=IC.sm(t / 0.3))
    IC.text(d, (x, yt + bh * 0.95), "보통의 피로", 46, IC.GRAY)
    IC.text(d, (x, yb + bh * 0.95), "번아웃", 46, IC.mix(IC.GRAY, IC.RED, IC.sm((t - 1.2) / 0.6)))
    return img


IC.KINDS["battery2"] = battery2_vertical
RD.render_text_layer = text_layer
RD.VideoSource = VideoSource


def guides(im):
    """Red overlay on the areas the buttons and captions may cover (Google and Meta figures, whichever is larger)."""
    ov = Image.new("RGBA", im.size, (0, 0, 0, 0))
    d = ImageDraw.Draw(ov)
    red = (255, 40, 40, 110)
    d.rectangle([0, 0, W, SAFE_T], fill=red)
    d.rectangle([0, SAFE_B, W, H], fill=red)
    d.rectangle([0, SAFE_T, SAFE_L, SAFE_B], fill=red)
    d.rectangle([SAFE_R, SAFE_T, W, SAFE_B], fill=red)
    out = im.convert("RGBA")
    out.alpha_composite(ov)
    return out.convert("RGB")


if __name__ == "__main__":
    if "--guides" in sys.argv:
        sys.argv.remove("--guides")
        real = Image.Image.save

        def save(self, fp, *a, **k):
            return real(guides(self), fp, *a, **k)
        Image.Image.save = save
    STYLE.update(json.load(open(sys.argv[1])).get("sub_style", {}))
    RD.main()
    if shifts:
        print("moved left to clear the buttons:", sorted(set(shifts)))
    if fitted:
        print("font size fitted to the width:", sorted(set(fitted)))
