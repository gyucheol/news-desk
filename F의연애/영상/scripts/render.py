# Render a timeline (JSON) to MP4: stock video scenes (in-point, speed), photo scenes with slow zoom,
# black cards, bottom subtitle boxes per the channel guide (9장 6절), and the audio track.
# All picture sources get the same grade so stock footage and AI images look like one piece.
# usage: render.py timeline.json out.mp4 [--frames-only N]
import json, math, os, subprocess, sys
import numpy as np
from PIL import Image, ImageDraw, ImageFilter, ImageFont

W, H, FPS = 1920, 1080, 30
ROOT = os.environ.get("VIDEO_ROOT", os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
FONT_PATH = f"{ROOT}/fonts/Pretendard-SemiBold.otf"
FONT_SIZE = 64                  # Hangul glyph height 56px = 5.2% of 1080 (guide: about 5%)
WHITE = (255, 255, 255, 255)
YELLOW = (242, 201, 76, 255)    # #F2C94C, guide 6-4
BOX_RGBA = (0, 0, 0, 224)       # nearly opaque black (guide 6-1)
BOX_BOTTOM = round(H * 0.928)   # 1002: box bottom edge at 92.8%
BOX_TOP_1 = round(H * 0.850)    # 918: one-line box top at 85.0%
LINE_GAP = 76                   # baseline distance for two-line subtitles
PAD_X = 28                      # narrow side padding
ITALIC_SLANT = math.tan(math.radians(12))
MAX_ZOOM = 1.05

font = ImageFont.truetype(FONT_PATH, FONT_SIZE)
# centre text (black cards, text over a dimmed photo): 70px since 2026-10-23 (owner: "1point씩 키워줘"; 64->65px would
# not be visible, so one step is taken as in a document going 10pt->11pt, about +9%). Bottom subtitles stay 64px.
CENTER_SIZE = 70
center_font = ImageFont.truetype(FONT_PATH, CENTER_SIZE)
TITLE_FONT_PATH = f"{ROOT}/fonts/Pretendard-ExtraBold.otf"
# Hangul glyph box relative to baseline (measured): top -51, bottom +5 -> visual center at -23
GLYPH_TOP, GLYPH_BOTTOM = -51, 5
GLYPH_MID = (GLYPH_TOP + GLYPH_BOTTOM) / 2


def parse_markup(text):
    """'[word]' marks the yellow emphasis word (one per subtitle)."""
    segs, buf, emph = [], "", False
    for ch in text:
        if ch == "[" and not emph:
            if buf: segs.append((buf, False)); buf = ""
            emph = True
        elif ch == "]" and emph:
            segs.append((buf, True)); buf = ""; emph = False
        else:
            buf += ch
    if buf: segs.append((buf, emph))
    return segs


def text_width(segs, f=None):
    return (f or font).getlength("".join(s for s, _ in segs))


def draw_line(layer, segs, x_left, baseline, f=None):
    f = f or font
    d = ImageDraw.Draw(layer)
    x = x_left
    for s, emph in segs:
        d.text((x, baseline), s, font=f, fill=YELLOW if emph else WHITE, anchor="ls")
        x += f.getlength(s)


def slant(layer, baseline):
    # synthetic oblique: tops lean right (Korean fonts have no true italic)
    k = ITALIC_SLANT
    return layer.transform(layer.size, Image.AFFINE, (1, k, -k * baseline, 0, 1, 0),
                           resample=Image.BICUBIC)


def render_text_layer(sub, upto=None):
    """Return a full-frame RGBA overlay for one subtitle unit. upto: centre text shows only its first `upto` rows,
    laid out as the whole sentence (v8 steps: the rows already shown never move)."""
    layer = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    lines = [parse_markup(l) for l in sub["text"].split("\n")]
    widths = [text_width(l) for l in lines]
    n = len(lines)
    if sub.get("pos", "bottom") == "center":
        # black card: centered, no box (guide 6-2)
        k = CENTER_SIZE / FONT_SIZE
        widths = [text_width(l, center_font) for l in lines]
        mid = H / 2
        first_base = mid - GLYPH_MID * k - (n - 1) * LINE_GAP * k / 2
        txt = Image.new("RGBA", (W, H), (0, 0, 0, 0))
        for i, (segs, w) in enumerate(zip(lines, widths)):
            if upto is not None and i >= upto:
                break
            base = first_base + i * LINE_GAP * k
            draw_line(txt, segs, (W - w) / 2, base, center_font)
        if sub.get("italic"):
            txt = slant(txt, H / 2)
        if sub.get("shadow"):                  # text over a dimmed photo: soft dark halo for legibility
            sh = Image.new("RGBA", (W, H), (0, 0, 0, 0))
            sh.putalpha(txt.getchannel("A").filter(ImageFilter.GaussianBlur(9)).point(lambda v: min(255, v * 2)))
            layer.alpha_composite(sh)
        layer.alpha_composite(txt)
        return layer
    # bottom subtitle box (guide 6-1): bottom edge fixed at 92.8%, grows upward
    box_h = (BOX_BOTTOM - BOX_TOP_1) + (n - 1) * LINE_GAP
    box_top = BOX_BOTTOM - box_h
    box_w = max(widths) + 2 * PAD_X
    d = ImageDraw.Draw(layer)
    if sub.get("box", True):   # black card / icon screens: text only (guide 6-1 #7)
        d.rectangle([round((W - box_w) / 2), box_top, round((W + box_w) / 2), BOX_BOTTOM], fill=BOX_RGBA)
    mid0 = box_top + (BOX_BOTTOM - BOX_TOP_1) / 2
    txt = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    for i, (segs, w) in enumerate(zip(lines, widths)):
        base = mid0 - GLYPH_MID + i * LINE_GAP
        draw_line(txt, segs, (W - w) / 2, base)
    if sub.get("italic"):
        txt = slant(txt, (box_top + BOX_BOTTOM) / 2)
    layer.alpha_composite(txt)
    return layer


_VIGNETTE = {}


def grade_arr(a8, g):
    """Common low-key look so all scenes match: mute colors, darker mids, vignette (uint8 HxWx3)."""
    if not g:
        return a8
    a = a8.astype(np.float32) / 255
    lum = a @ np.array([0.2126, 0.7152, 0.0722], np.float32)
    a = lum[..., None] + (a - lum[..., None]) * g.get("sat", 0.88)
    a = np.clip((a - g.get("black", 0.02)) / (1 - g.get("black", 0.02)), 0, 1) ** g.get("gamma", 1.12)
    h, w = lum.shape
    key = (h, w, g.get("vignette", 0.35))
    if key not in _VIGNETTE:
        yy, xx = np.mgrid[0:h, 0:w].astype(np.float32)
        r = np.sqrt(((xx - w / 2) / (w / 2)) ** 2 + ((yy - h / 2) / (h / 2)) ** 2) / math.sqrt(2)
        u = np.clip((r - 0.35) / 0.65, 0, 1)
        _VIGNETTE[key] = (1 - key[2] * u * u * (3 - 2 * u))[..., None].astype(np.float32)
    a *= _VIGNETTE[key]
    return (np.clip(a, 0, 1) * 255 + 0.5).astype(np.uint8)


def grade(im, g):
    return Image.fromarray(grade_arr(np.asarray(im.convert("RGB")), g))


def blur_box_filter(boxes, w, h):
    """F의 연애 01 (2026-10-24): "blur_box" [[x0, y0, x1, y1, sigma], ...] (0..1 of the output frame) blurs only that box,
    e.g. readable notification text on a phone lying still, so the rest of the shot stays sharp."""
    f = ""
    for i, (x0, y0, x1, y1, s) in enumerate(boxes):
        X, Y = 2 * round(x0 * w / 2), 2 * round(y0 * h / 2)
        bw, bh = 2 * round((x1 - x0) * w / 2), 2 * round((y1 - y0) * h / 2)
        f += f",split[bm{i}][bb{i}];[bb{i}]crop={bw}:{bh}:{X}:{Y},gblur=sigma={s}[bg{i}];[bm{i}][bg{i}]overlay={X}:{Y}"
    return f


class VideoSource:
    """Stock video scene: ffmpeg decodes from `in` (s) at `speed`, resampled to 30 fps and cropped to fill 16:9.
    Frames are read in order; if the clip runs out, the last frame is held."""

    def __init__(self, sc):
        self.sc, self.proc, self.k, self.last = sc, None, -1, None
        self.zoom = not (sc.get("z0", 1.0) == 1.0 and sc.get("z1", 1.0) == 1.0)
        self.size = (round(W * MAX_ZOOM), round(H * MAX_ZOOM)) if self.zoom else (W, H)

    def _start(self):
        w, h = self.size
        # optional per scene: "crop" [x0, y0, x1, y1] (0..1 of the source; keep it 16:9) cuts text or a logo off an edge,
        # "blur" (gaussian sigma in px) softens a shot whose readable text or face can't be cropped away
        c = self.sc.get("crop")
        pre = f"crop=iw*{c[2] - c[0]:.4f}:ih*{c[3] - c[1]:.4f}:iw*{c[0]:.4f}:ih*{c[1]:.4f}," if c else ""
        post = f",gblur=sigma={self.sc['blur']}" if self.sc.get("blur") else ""
        post += blur_box_filter(self.sc.get("blur_box", []), w, h)
        vf = (f"{pre}setpts=PTS/{self.sc.get('speed', 1.0)},fps={FPS},"
              f"scale={w}:{h}:force_original_aspect_ratio=increase:flags=lanczos,crop={w}:{h}{post}")
        self.proc = subprocess.Popen(["ffmpeg", "-v", "error", "-ss", str(self.sc.get("in", 0)), "-i", self.sc["src"],
                                      "-vf", vf, "-f", "rawvideo", "-pix_fmt", "rgb24", "-"],
                                     stdout=subprocess.PIPE, stderr=subprocess.DEVNULL)  # closing early is normal
        self.k = -1

    def frame(self, k):
        if self.proc is None or k < self.k:
            self.close(); self._start()
        n = self.size[0] * self.size[1] * 3
        while self.k < k:
            buf = self.proc.stdout.read(n)
            if len(buf) < n:
                break
            self.last = np.frombuffer(buf, np.uint8).reshape(self.size[1], self.size[0], 3)
            self.k += 1
        return self.last

    def close(self):
        if self.proc:
            self.proc.stdout.close(); self.proc.kill(); self.proc.wait(); self.proc = None


DEFAULT_GRADE = {"sat": 0.88, "black": 0.02, "gamma": 1.12, "vignette": 0.35}


def prep_image(path, crop=None, g=DEFAULT_GRADE, blur=0):
    """Crop to 16:9, grade, and upscale so that MAX_ZOOM maps 1:1 to output pixels (optional blur after)."""
    im = Image.open(path).convert("RGB")
    w, h = im.size
    if crop:  # [x0, y0, x1, y1] in source pixels
        im = im.crop(crop); w, h = im.size
    tw = w; th = round(w * 9 / 16)
    if th > h:
        th = h; tw = round(h * 16 / 9)
    x0 = (w - tw) // 2; y0 = (h - th) // 2
    im = grade(im.crop((x0, y0, x0 + tw, y0 + th)), g)   # grade after crop: vignette stays centered
    im = im.resize((round(W * MAX_ZOOM), round(H * MAX_ZOOM)), Image.LANCZOS)
    return im.filter(ImageFilter.GaussianBlur(blur)) if blur else im


def photo_key(sc):
    return json.dumps([sc["image"], sc.get("crop"), sc.get("grade", DEFAULT_GRADE), sc.get("blur", 0)], sort_keys=True)


def mix_source(sc):
    """F의 연애 01 v3 (2026-10-25): a photo scene's "mix" {"at": unit, "dur": s, and any of image/crop/grade/blur}
    cross-fades the photo into a second version of it from the voice onset of that unit, e.g. the brain turning red at
    '위협적으로', or a photo coming into focus when the centre text gives way to a bottom subtitle."""
    mx = sc["mix"]
    return {"image": mx.get("image", sc["image"]), "crop": mx.get("crop", sc.get("crop")),
            "grade": mx.get("grade", sc.get("grade", DEFAULT_GRADE)), "blur": mx.get("blur", sc.get("blur", 0))}


def mix_weight(mx, t, sub_start):
    """How far a scene's "mix" has gone at time t (0..1, smooth). It starts at the voice onset of mx["at"] (+ "shift"
    seconds, negative = earlier) and takes "dur" seconds; v4 (2026-10-25): with "until" (a unit) it goes back over the
    same time from that unit's onset (+ "until_shift"), e.g. a shot softened only under one centre line."""
    if mx["at"] not in sub_start:
        return 0.0
    d = mx.get("dur", 0.5)
    k = smooth(min(max((t - sub_start[mx["at"]] - mx.get("shift", 0.0)) / d, 0), 1))
    if mx.get("until") in sub_start:
        k *= 1 - smooth(min(max((t - sub_start[mx["until"]] - mx.get("until_shift", 0.0)) / d, 0), 1))
    return k


def luma_key(icon):
    """F의 연애 01 v4 (2026-10-25): an icon screen (white and coloured lines on black) as a transparent layer, so the
    drawing can sit on a picture: alpha = the brightest channel, colour = the pixel brought back to full strength."""
    a = np.asarray(icon.convert("RGB"), dtype=np.float32)
    al = a.max(axis=2)
    rgb = np.clip(a * (255.0 / np.maximum(al, 1.0))[..., None], 0, 255)
    return Image.fromarray(np.dstack([rgb, al]).round().astype(np.uint8), "RGBA")


SPLIT_GAP = 8                    # black line between the two halves of a split screen


def panel_size():
    return (W - SPLIT_GAP) // 2, H


def panel_key(p):
    return json.dumps(["panel", p["image"], p.get("crop"), p.get("grade", DEFAULT_GRADE)], sort_keys=True)


def prep_panel(p):
    """Split-screen panel (F의 연애 01 v3): "crop" [x0, y0, x1, y1] in source pixels with the panel's aspect (about
    956 x 1080), graded, scaled so that MAX_ZOOM maps 1:1 to output pixels."""
    im = Image.open(p["image"]).convert("RGB")
    if p.get("crop"):
        im = im.crop(p["crop"])
    pw, ph = panel_size()
    im = grade(im, p.get("grade", DEFAULT_GRADE))
    return im.resize((round(pw * MAX_ZOOM), round(ph * MAX_ZOOM)), Image.LANCZOS)


_FYO = None


def fy_overlays():
    """F의 연애 drawings over a photo (icons_photo.py OVERLAYS): fn(t, dur, args, at, view) -> RGBA 1920x1080; view =
    the visible window of the photo as (x0, y0, w, h) in 0..1 of the photo, so a drawing can stay on the photo's
    subject while the photo slowly zooms."""
    global _FYO
    if _FYO is None:
        import importlib
        try:
            _FYO = importlib.import_module("icons_photo").OVERLAYS
        except ImportError:
            _FYO = {}
    return _FYO


def title_layer(sc):
    """Big centred words over a scene (e.g. 번아웃, 1970년대) with a soft shadow; an optional smaller line below."""
    layer = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    d = ImageDraw.Draw(layer)
    size = sc.get("title_size", 170)
    f = ImageFont.truetype(TITLE_FONT_PATH, size)
    y = H * sc.get("title_y", 0.42)
    col = YELLOW if sc.get("title_color") == "yellow" else WHITE
    d.text((W / 2, y), sc["title"], font=f, fill=col, anchor="mm")
    if sc.get("title_sub"):
        d.text((W / 2, y + size * 0.78), sc["title_sub"], font=ImageFont.truetype(TITLE_FONT_PATH, round(size * 0.36)),
               fill=WHITE, anchor="mm")
    sh = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    sh.putalpha(layer.getchannel("A").filter(ImageFilter.GaussianBlur(14)).point(lambda v: min(255, round(v * 1.6))))
    sh.alpha_composite(layer)
    return sh


GRAY, RED = (110, 110, 110), (229, 72, 77)


def _mix(c1, c2, u):
    return tuple(round(a + (b - a) * u) for a, b in zip(c1, c2))


_FY = None


def fy_kinds():
    """F의 연애 icon screens (2026-10-24): kinds from icons_chat / icons_exp / icons_misc, fn(t, dur, args, at)."""
    global _FY
    if _FY is None:
        import importlib
        _FY = {}
        for m in ("icons_chat", "icons_exp", "icons_misc"):
            try:
                _FY.update(importlib.import_module(m).KINDS)
            except ImportError:
                pass
    return _FY


def icon_frame(kind, t, dur):
    """Icon screens (guide 6-3): black background, white line icon, drawn at 2x then downsampled."""
    if kind not in ("bulb", "battery"):                      # the other icons live in icons.py
        import icons
        return icons.draw(kind, t, dur)
    SS = 2
    img = Image.new("RGB", (W * SS, H * SS), (0, 0, 0))
    cx, cy = W * SS / 2, H * SS * 0.42
    lw = 12 * SS
    if kind == "bulb":
        on = smooth(min(max((t - 0.45) / 0.7, 0), 1))           # switches on, then stays lit
        on *= 1 - 0.06 * (1 - math.cos(max(t - 1.2, 0) * 2.4)) / 2  # faint flicker so it is alive
        r = 118 * SS
        if on > 0:
            glow = Image.new("L", img.size, 0)
            ImageDraw.Draw(glow).ellipse([cx - r * 1.5, cy - r * 1.5, cx + r * 1.5, cy + r * 1.5], fill=round(170 * on))
            glow = glow.filter(ImageFilter.GaussianBlur(70 * SS))
            img = Image.composite(Image.new("RGB", img.size, YELLOW[:3]), img, glow)
        d = ImageDraw.Draw(img)
        col = _mix(GRAY, (255, 255, 255), on)
        d.arc([cx - r, cy - r, cx + r, cy + r], start=135, end=405, fill=col, width=lw)
        a1, a2 = math.radians(135), math.radians(45)
        base_top, neck = cy + r * 1.28, r * 0.42
        d.line([(cx + r * math.cos(a1), cy + r * math.sin(a1)), (cx - neck, base_top)], fill=col, width=lw)
        d.line([(cx + r * math.cos(a2), cy + r * math.sin(a2)), (cx + neck, base_top)], fill=col, width=lw)
        for k in range(3):
            y = base_top + 10 * SS + k * 30 * SS
            w2 = neck - k * 10 * SS
            d.rounded_rectangle([cx - w2, y, cx + w2, y + 16 * SS], radius=8 * SS, fill=col)
        fil = _mix(GRAY, YELLOW[:3], on)
        pts = [(cx - 44 * SS, cy + 30 * SS), (cx - 22 * SS, cy - 18 * SS), (cx, cy + 22 * SS),
               (cx + 22 * SS, cy - 18 * SS), (cx + 44 * SS, cy + 30 * SS)]
        d.line(pts, fill=fil, width=8 * SS, joint="curve")
        if on > 0.05:                                          # short rays around the top
            for ang in range(-150, -20, 26):
                a = math.radians(ang)
                r1, r2 = r * 1.32, r * (1.32 + 0.30 * on)
                d.line([(cx + r1 * math.cos(a), cy + r1 * math.sin(a)), (cx + r2 * math.cos(a), cy + r2 * math.sin(a))],
                       fill=_mix((0, 0, 0), YELLOW[:3], on), width=9 * SS)
    elif kind == "battery":
        bw, bh = 420 * SS, 200 * SS
        x0, y0 = cx - bw / 2 - 14 * SS, cy - bh / 2
        d = ImageDraw.Draw(img)
        d.rounded_rectangle([x0, y0, x0 + bw, y0 + bh], radius=34 * SS, outline=(255, 255, 255), width=lw)
        d.rounded_rectangle([x0 + bw + 10 * SS, cy - 42 * SS, x0 + bw + 34 * SS, cy + 42 * SS], radius=10 * SS,
                            fill=(255, 255, 255))
        # level: plugged in, creeps up, then drains below where it started (charging but not filling)
        if t < 0.45:
            lvl = 0.12
        elif t < 1.55:
            lvl = 0.12 + 0.11 * smooth((t - 0.45) / 1.1)
        else:
            lvl = 0.23 - 0.16 * smooth(min((t - 1.55) / 0.9, 1))
        blink = 1.0 if t < 2.45 else (0.35 if int((t - 2.45) * 4) % 2 else 1.0)
        pad = 26 * SS
        inner_w = bw - 2 * pad
        d.rounded_rectangle([x0 + pad, y0 + pad, x0 + pad + max(inner_w * lvl, 18 * SS), y0 + bh - pad],
                            radius=14 * SS, fill=_mix((0, 0, 0), RED, blink))
        if t >= 0.4:                                           # charging bolt pops in
            k = min((t - 0.4) / 0.18, 1)
            sc = (0.6 + 0.4 * k) * SS
            bolt = [(18, -70), (-30, 8), (2, 8), (-14, 70), (34, -10), (2, -10), (18, -70)]
            d.polygon([(cx - 14 * SS + x * sc, cy + y * sc) for x, y in bolt], fill=_mix((0, 0, 0), YELLOW[:3], k))
    return img.resize((W, H), Image.LANCZOS)


def kenburns_view(src, z, cx, cy):
    """The window of the source seen at zoom z with focus (cx, cy): (x0, y0, vw, vh) in source pixels."""
    sw, sh = src.size
    vw, vh = sw / z, sh / z
    # keep the view window inside the source
    x0 = min(max(cx * sw - vw / 2, 0), sw - vw)
    y0 = min(max(cy * sh - vh / 2, 0), sh - vh)
    return x0, y0, vw, vh


def kenburns(src, z, cx, cy, size=(W, H)):
    """z: 1.0 (full source) .. MAX_ZOOM; (cx, cy): focus as 0..1 of source; size: output (split-screen panels)."""
    x0, y0, vw, vh = kenburns_view(src, z, cx, cy)
    a = vw / size[0]; e = vh / size[1]
    return src.transform(size, Image.AFFINE, (a, 0, x0, 0, e, y0), resample=Image.BICUBIC)


def lerp(a, b, u):
    return a + (b - a) * u


def smooth(u):
    return u * u * (3 - 2 * u)


def main():
    tl = json.load(open(sys.argv[1]))
    out = sys.argv[2]
    frames_only = None
    if "--frames-only" in sys.argv:
        frames_only = [float(x) for x in sys.argv[sys.argv.index("--frames-only") + 1].split(",")]
    dur = tl["duration"]
    nfr = round(dur * FPS)
    srcs, vids = {}, {}
    for i, sc in enumerate(tl["scenes"]):
        if sc["type"] == "photo":
            for ps in [sc] + ([mix_source(sc)] if sc.get("mix") else []):
                if photo_key(ps) not in srcs:
                    srcs[photo_key(ps)] = prep_image(ps["image"], ps.get("crop"), ps.get("grade", DEFAULT_GRADE),
                                                     ps.get("blur", 0))
        elif sc["type"] == "split":
            for p in sc["panels"]:
                if panel_key(p) not in srcs:
                    srcs[panel_key(p)] = prep_panel(p)
        elif sc["type"] == "video":
            vids[i] = VideoSource(sc)
    # F의 연애 (2026-10-24): a --range part or --frames-only builds only the subtitle layers it shows. Each layer is a
    # full-frame RGBA image (about 8 MB); all 460 of 01편 in each of 3 processes nearly filled the memory (3.9 GB each).
    want = None
    if "--range" in sys.argv:
        a_, b_ = [int(x) for x in sys.argv[sys.argv.index("--range") + 1].split(",")]
        want = lambda s: s["end"] >= a_ / FPS - 1.0 and s["start"] <= b_ / FPS + 1.0
    elif frames_only:
        want = lambda s: any(s["start"] - 1.0 <= t <= s["end"] + 1.0 for t in frames_only)
    layers = []
    for s in tl["subs"]:             # v8 steps: one layer per step, each adding the rows spoken by then
        if want and not want(s):
            continue
        st = s.get("steps", [])
        times = [s["start"]] + [x["start"] for x in st] + [s["end"]]
        rows = [x["row"] for x in st] + [None]
        for k in range(len(times) - 1):
            layers.append((times[k], times[k + 1], render_text_layer(s, rows[k])))
    # unit start times for overlays (v7 timelines carry them; subtitle lines no longer match the units)
    sub_start = tl.get("unit_start") or {s["unit"]: s["start"] for s in tl["subs"]}
    black = Image.new("RGB", (W, H), (0, 0, 0))
    # F의 연애 01 v2 (2026-10-24): the "1 / 3" item label is white and larger (owner on the grey 첫 번째 labels: "폰트를
    # 약간 더 키우고 흰색으로 만들어줘. 잘 안보임"; the same holds for this grey label)
    labels, label_font, titles = {}, ImageFont.truetype(FONT_PATH, 54), {}

    def frame_at(t):
        si = next((i for i, s in enumerate(tl["scenes"]) if s["start"] <= t < s["end"]), len(tl["scenes"]) - 1)
        sc = tl["scenes"][si]
        for j, v in vids.items():          # free decoders of scenes already passed
            if j < si and not frames_only:
                v.close()
        if sc["type"] == "video":
            u = min(max((t - sc["start"]) / (sc["end"] - sc["start"]), 0), 1)
            raw = vids[si].frame(int(round((t - sc["start"]) * FPS)))
            versions = [(Image.fromarray(grade_arr(raw, sc.get("grade", DEFAULT_GRADE))), 0)]
            # F의 연애 01 v4 (2026-10-25): "mix" on a stock shot = the same shot, graded and blurred as the background of
            # centre text, faded in at a line (and out again with "until"); the owner: "바로 앞 장면에서 사용한 사진을
            # 그대로 이어받아서 화면 중앙에 대본 적는 걸로"
            km = mix_weight(sc["mix"], t, sub_start) if sc.get("mix") else 0.0
            if km > 0:
                versions.append((Image.fromarray(grade_arr(raw, sc["mix"].get("grade", sc.get("grade", DEFAULT_GRADE)))),
                                 sc["mix"].get("blur", 0)))
            outs = []
            for im, bl in versions:
                if vids[si].zoom:
                    z = sc.get("z0", 1.0) * (sc.get("z1", 1.0) / sc.get("z0", 1.0)) ** u
                    im = kenburns(im, z, lerp(sc.get("cx0", 0.5), sc.get("cx1", 0.5), u),
                                  lerp(sc.get("cy0", 0.5), sc.get("cy1", 0.5), u))
                outs.append(im.filter(ImageFilter.GaussianBlur(bl)) if bl else im)
            im = outs[0] if km <= 0 else (outs[1] if km >= 1 else Image.blend(outs[0], outs[1], km))
            img = im.convert("RGBA")
        elif sc["type"] == "icon":
            if sc["icon"] in fy_kinds():
                # args from the spec; at = voice onsets of the listed lines, seconds from the scene start
                at = [sub_start[u] - sc["start"] if u in sub_start else None for u in sc.get("at", [])]
                at = [a + sh if a is not None else None for a, sh in
                      zip(at, sc.get("at_shift", []) + [0.0] * len(at))]      # e.g. a word inside the line
                img = fy_kinds()[sc["icon"]](t - sc["start"], sc["end"] - sc["start"], sc.get("args", {}), at).convert("RGBA")
            else:
                img = icon_frame(sc["icon"], t - sc["start"], sc["end"] - sc["start"]).convert("RGBA")
        elif sc["type"] == "photo":
            u = min(max((t - sc["start"]) / (sc["end"] - sc["start"]), 0), 1)
            # exponential zoom = constant perceived speed; zoom_rate (per second) gives every photo the same slow speed
            z0 = sc.get("z0", 1.0)
            z1 = min(MAX_ZOOM, z0 * (1 + sc["zoom_rate"] * (sc["end"] - sc["start"]))) if "zoom_rate" in sc else sc.get("z1", 1.04)
            z = z0 * (z1 / z0) ** u
            cx = lerp(sc.get("cx0", 0.5), sc.get("cx1", 0.5), u)
            cy = lerp(sc.get("cy0", 0.5), sc.get("cy1", 0.5), u)
            src = srcs[photo_key(sc)]
            if sc.get("mix") and sc["mix"]["at"] in sub_start:
                k = mix_weight(sc["mix"], t, sub_start)
                if k >= 1:
                    src = srcs[photo_key(mix_source(sc))]
                elif k > 0:
                    src = Image.blend(src, srcs[photo_key(mix_source(sc))], k)
            img = kenburns(src, z, cx, cy).convert("RGBA")
            if sc.get("overlay"):              # drawn over the photo, timed to units (icons_photo.py, then icons.py)
                ov = sc["overlay"]
                at = [sub_start[u] - sc["start"] for u in ov.get("at", []) if u in sub_start]
                if ov["kind"] in fy_overlays():
                    x0, y0, vw, vh = kenburns_view(src, z, cx, cy)
                    view = (x0 / src.width, y0 / src.height, vw / src.width, vh / src.height)
                    img.alpha_composite(fy_overlays()[ov["kind"]](t - sc["start"], sc["end"] - sc["start"],
                                                                  ov.get("args", {}), at, view))
                else:
                    import icons
                    img.alpha_composite(icons.overlay(ov["kind"], t - sc["start"], sc["end"] - sc["start"], at))
        elif sc["type"] == "split":
            # F의 연애 01 v3 (2026-10-25): two photos side by side, each appearing (fade) when its line is spoken; the
            # owner: "화면을 반으로 나누어서 … 오른쪽에 15번 사진이 먼저 나오고 … 13번 사진이 그 이후에 왼쪽에"
            pw, ph = panel_size()
            img = Image.new("RGBA", (W, H), (0, 0, 0, 255))
            for p in sc["panels"]:
                t_on = sub_start.get(p["at"], sc["start"]) if p.get("at") else sc["start"]
                k = smooth(min(max((t - t_on) / p.get("fade", 0.35), 0), 1))
                if k <= 0:
                    continue
                zp = min(MAX_ZOOM, p.get("z0", 1.0) * (1 + p.get("zoom_rate", 0.006) * max(t - t_on, 0)))
                pim = kenburns(srcs[panel_key(p)], zp, p.get("cx", 0.5), p.get("cy", 0.5), (pw, ph))
                if k < 1:
                    pim = Image.blend(Image.new("RGB", (pw, ph), (0, 0, 0)), pim, k)
                img.paste(pim, (0 if p["side"] == "left" else W - pw, 0))
        elif sc.get("label"):                  # item card: small "1 / 3" above the centred line (scene table 항목카드)
            if sc["label"] not in labels:
                lab = black.copy()
                ImageDraw.Draw(lab).text((W / 2, H * 0.33), sc["label"], font=label_font, fill=(255, 255, 255), anchor="mm")
                labels[sc["label"]] = lab.convert("RGBA")
            img = labels[sc["label"]].copy()
        else:
            img = black.convert("RGBA")
        if sc.get("icon_overlay"):
            # F의 연애 01 v4 (2026-10-25): an icon screen drawn over the picture (luma_key), from the voice onset of the
            # unit "from"; its "at" units are timed from there. The owner on 소속감/통제감/자존감: "바로 앞 장면에서 사용한
            # 사진을 그대로 이어받아서 화면 중앙에 대본 적는 걸로 편집. + ai자료도 그대로 중앙에 배치"
            ov = sc["icon_overlay"]
            t0 = sub_start.get(ov.get("from"), sc["start"])
            if t >= t0:
                at = [sub_start[u] - t0 for u in ov.get("at", []) if u in sub_start]
                img.alpha_composite(luma_key(fy_kinds()[ov["kind"]](t - t0, sc["end"] - t0, ov.get("args", {}), at)))
        if sc.get("title"):                     # big words over the scene, fading in at its start
            if si not in titles:
                titles[si] = title_layer(sc)
            a = smooth(min(max((t - sc["start"] - sc.get("title_delay", 0.0)) / 0.35, 0), 1))
            if a > 0:
                lay = titles[si] if a >= 1 else titles[si].copy()
                if a < 1:
                    lay.putalpha(lay.getchannel("A").point(lambda v: round(v * a)))
                img.alpha_composite(lay)
        for s0, s1, lay in layers:
            if s0 <= t < s1:
                a = 1.0
                if tl.get("text_fade_out") and t > s1 - tl["text_fade_out"] and s1 >= dur - 1e-6:
                    a = (s1 - t) / tl["text_fade_out"]
                if a < 1.0:
                    lay = lay.copy(); lay.putalpha(lay.getchannel("A").point(lambda v: round(v * a)))
                img.alpha_composite(lay)
        rgb = img.convert("RGB")
        fi, fo = tl.get("fade_in", 0), tl.get("fade_out", 0)
        g = 1.0
        if fi and t < fi: g = smooth(t / fi)
        if fo and t > dur - fo: g = min(g, smooth(max(dur - t, 0) / fo))
        if g < 1.0:
            rgb = Image.fromarray((np.asarray(rgb, dtype=np.float32) * g).round().astype(np.uint8))
        return rgb

    if frames_only:
        for t in frames_only:
            p = out.replace(".mp4", f"_t{t:05.2f}.png")
            frame_at(t).save(p); print(p)
        return
    # F의 연애 (2026-10-24): --range a,b renders frames a..b-1 as a video-only part (render_parallel.py joins the parts
    # and adds the sound once), so a long episode can use several processes
    rng = None
    if "--range" in sys.argv:
        rng = [int(x) for x in sys.argv[sys.argv.index("--range") + 1].split(",")]
    if rng:
        cmd = ["ffmpeg", "-v", "error", "-y", "-f", "rawvideo", "-pix_fmt", "rgb24", "-s", f"{W}x{H}",
               "-r", str(FPS), "-i", "-", "-map", "0:v",
               "-vf", "scale=out_color_matrix=bt709:out_range=tv",
               "-c:v", "libx264", "-preset", "slow", "-crf", "17", "-pix_fmt", "yuv420p",
               "-tune", "film", "-colorspace", "bt709", "-color_primaries", "bt709", "-color_trc", "bt709",
               "-threads", "2", out]
        p = subprocess.Popen(cmd, stdin=subprocess.PIPE)
        for i in range(rng[0], min(rng[1], nfr)):
            p.stdin.write(frame_at(i / FPS).tobytes())
        p.stdin.close(); p.wait()
        for v in vids.values():
            v.close()
        print("wrote", out, "frames", rng[0], "to", min(rng[1], nfr))
        return
    cmd = ["ffmpeg", "-v", "error", "-y", "-f", "rawvideo", "-pix_fmt", "rgb24", "-s", f"{W}x{H}",
           "-r", str(FPS), "-i", "-", "-i", tl["audio"], "-map", "0:v", "-map", "1:a",
           "-vf", "scale=out_color_matrix=bt709:out_range=tv",   # RGB->YUV with BT.709, matching the tags
           "-c:v", "libx264", "-preset", "slow", "-crf", "17", "-pix_fmt", "yuv420p",
           "-tune", "film", "-colorspace", "bt709", "-color_primaries", "bt709", "-color_trc", "bt709",
           "-c:a", "aac", "-b:a", "192k", "-ar", "48000", "-ac", "2", "-shortest",
           "-movflags", "+faststart", out]
    p = subprocess.Popen(cmd, stdin=subprocess.PIPE)
    for i in range(nfr):
        p.stdin.write(frame_at(i / FPS).tobytes())
    p.stdin.close(); p.wait()
    for v in vids.values():
        v.close()
    print("wrote", out, nfr, "frames")


if __name__ == "__main__":
    main()
