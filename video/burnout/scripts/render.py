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


def render_text_layer(sub):
    """Return a full-frame RGBA overlay for one subtitle unit."""
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


def kenburns(src, z, cx, cy):
    """z: 1.0 (full source) .. MAX_ZOOM; (cx, cy): focus as 0..1 of source."""
    sw, sh = src.size
    vw, vh = sw / z, sh / z
    # keep the view window inside the source
    x0 = min(max(cx * sw - vw / 2, 0), sw - vw)
    y0 = min(max(cy * sh - vh / 2, 0), sh - vh)
    a = vw / W; e = vh / H
    return src.transform((W, H), Image.AFFINE, (a, 0, x0, 0, e, y0), resample=Image.BICUBIC)


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
        if sc["type"] == "photo" and photo_key(sc) not in srcs:
            srcs[photo_key(sc)] = prep_image(sc["image"], sc.get("crop"), sc.get("grade", DEFAULT_GRADE), sc.get("blur", 0))
        elif sc["type"] == "video":
            vids[i] = VideoSource(sc)
    layers = [(s["start"], s["end"], render_text_layer(s)) for s in tl["subs"]]
    sub_start = {s["unit"]: s["start"] for s in tl["subs"]}
    black = Image.new("RGB", (W, H), (0, 0, 0))
    labels, label_font, titles = {}, ImageFont.truetype(FONT_PATH, 44), {}

    def frame_at(t):
        si = next((i for i, s in enumerate(tl["scenes"]) if s["start"] <= t < s["end"]), len(tl["scenes"]) - 1)
        sc = tl["scenes"][si]
        for j, v in vids.items():          # free decoders of scenes already passed
            if j < si and not frames_only:
                v.close()
        if sc["type"] == "video":
            u = min(max((t - sc["start"]) / (sc["end"] - sc["start"]), 0), 1)
            arr = grade_arr(vids[si].frame(int(round((t - sc["start"]) * FPS))), sc.get("grade", DEFAULT_GRADE))
            im = Image.fromarray(arr)
            if vids[si].zoom:
                z = sc.get("z0", 1.0) * (sc.get("z1", 1.0) / sc.get("z0", 1.0)) ** u
                im = kenburns(im, z, lerp(sc.get("cx0", 0.5), sc.get("cx1", 0.5), u),
                              lerp(sc.get("cy0", 0.5), sc.get("cy1", 0.5), u))
            img = im.convert("RGBA")
        elif sc["type"] == "icon":
            img = icon_frame(sc["icon"], t - sc["start"], sc["end"] - sc["start"]).convert("RGBA")
        elif sc["type"] == "photo":
            u = min(max((t - sc["start"]) / (sc["end"] - sc["start"]), 0), 1)
            # exponential zoom = constant perceived speed
            z = sc.get("z0", 1.0) * (sc.get("z1", 1.04) / sc.get("z0", 1.0)) ** u
            cx = lerp(sc.get("cx0", 0.5), sc.get("cx1", 0.5), u)
            cy = lerp(sc.get("cy0", 0.5), sc.get("cy1", 0.5), u)
            img = kenburns(srcs[photo_key(sc)], z, cx, cy).convert("RGBA")
            if sc.get("overlay"):              # text drawn over the photo (icons.py OVERLAYS), lines timed to units
                import icons
                ov = sc["overlay"]
                at = [sub_start[u] - sc["start"] for u in ov.get("at", []) if u in sub_start]
                img.alpha_composite(icons.overlay(ov["kind"], t - sc["start"], sc["end"] - sc["start"], at))
        elif sc.get("label"):                  # item card: small "1 / 3" above the centred line (scene table 항목카드)
            if sc["label"] not in labels:
                lab = black.copy()
                ImageDraw.Draw(lab).text((W / 2, H * 0.33), sc["label"], font=label_font, fill=(150, 150, 150), anchor="mm")
                labels[sc["label"]] = lab.convert("RGBA")
            img = labels[sc["label"]].copy()
        else:
            img = black.convert("RGBA")
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
