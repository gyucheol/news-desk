# Render a timeline (JSON) to MP4: photo scenes with slow zoom, black cards,
# bottom subtitle boxes per the channel guide (9장 6절), narration audio.
# usage: render.py timeline.json out.mp4 [--frames-only N]
import json, math, os, subprocess, sys
import numpy as np
from PIL import Image, ImageDraw, ImageFont

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


def text_width(segs):
    return font.getlength("".join(s for s, _ in segs))


def draw_line(layer, segs, x_left, baseline):
    d = ImageDraw.Draw(layer)
    x = x_left
    for s, emph in segs:
        d.text((x, baseline), s, font=font, fill=YELLOW if emph else WHITE, anchor="ls")
        x += font.getlength(s)


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
        mid = H / 2
        first_base = mid - GLYPH_MID - (n - 1) * LINE_GAP / 2
        txt = Image.new("RGBA", (W, H), (0, 0, 0, 0))
        for i, (segs, w) in enumerate(zip(lines, widths)):
            base = first_base + i * LINE_GAP
            draw_line(txt, segs, (W - w) / 2, base)
        if sub.get("italic"):
            txt = slant(txt, H / 2)
        layer.alpha_composite(txt)
        return layer
    # bottom subtitle box (guide 6-1): bottom edge fixed at 92.8%, grows upward
    box_h = (BOX_BOTTOM - BOX_TOP_1) + (n - 1) * LINE_GAP
    box_top = BOX_BOTTOM - box_h
    box_w = max(widths) + 2 * PAD_X
    d = ImageDraw.Draw(layer)
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


def grade(im, g):
    """Common low-key look so all scenes match: mute colors, darker mids, vignette."""
    if not g:
        return im
    a = np.asarray(im, dtype=np.float32) / 255
    lum = a @ np.array([0.2126, 0.7152, 0.0722], np.float32)
    a = lum[..., None] + (a - lum[..., None]) * g.get("sat", 0.88)
    a = np.clip((a - g.get("black", 0.02)) / (1 - g.get("black", 0.02)), 0, 1) ** g.get("gamma", 1.12)
    h, w = lum.shape
    yy, xx = np.mgrid[0:h, 0:w].astype(np.float32)
    r = np.sqrt(((xx - w / 2) / (w / 2)) ** 2 + ((yy - h / 2) / (h / 2)) ** 2) / math.sqrt(2)
    u = np.clip((r - 0.35) / 0.65, 0, 1)
    a *= (1 - g.get("vignette", 0.35) * u * u * (3 - 2 * u))[..., None]
    return Image.fromarray((np.clip(a, 0, 1) * 255).round().astype(np.uint8))


DEFAULT_GRADE = {"sat": 0.88, "black": 0.02, "gamma": 1.12, "vignette": 0.35}


def prep_image(path, crop=None, g=DEFAULT_GRADE):
    """Crop to 16:9, grade, and upscale so that MAX_ZOOM maps 1:1 to output pixels."""
    im = Image.open(path).convert("RGB")
    w, h = im.size
    if crop:  # [x0, y0, x1, y1] in source pixels
        im = im.crop(crop); w, h = im.size
    tw = w; th = round(w * 9 / 16)
    if th > h:
        th = h; tw = round(h * 16 / 9)
    x0 = (w - tw) // 2; y0 = (h - th) // 2
    im = grade(im.crop((x0, y0, x0 + tw, y0 + th)), g)   # grade after crop: vignette stays centered
    return im.resize((round(W * MAX_ZOOM), round(H * MAX_ZOOM)), Image.LANCZOS)


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
    srcs = {}
    for sc in tl["scenes"]:
        if sc["type"] == "photo" and sc["image"] not in srcs:
            srcs[sc["image"]] = prep_image(sc["image"], sc.get("crop"), sc.get("grade", DEFAULT_GRADE))
    layers = [(s["start"], s["end"], render_text_layer(s)) for s in tl["subs"]]
    black = Image.new("RGB", (W, H), (0, 0, 0))

    def frame_at(t):
        sc = next((s for s in tl["scenes"] if s["start"] <= t < s["end"]), tl["scenes"][-1])
        if sc["type"] == "photo":
            u = min(max((t - sc["start"]) / (sc["end"] - sc["start"]), 0), 1)
            # exponential zoom = constant perceived speed
            z = sc.get("z0", 1.0) * (sc.get("z1", 1.04) / sc.get("z0", 1.0)) ** u
            cx = lerp(sc.get("cx0", 0.5), sc.get("cx1", 0.5), u)
            cy = lerp(sc.get("cy0", 0.5), sc.get("cy1", 0.5), u)
            img = kenburns(srcs[sc["image"]], z, cx, cy).convert("RGBA")
        else:
            img = black.convert("RGBA")
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
    print("wrote", out, nfr, "frames")


if __name__ == "__main__":
    main()
