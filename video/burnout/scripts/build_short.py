# Cut one Short out of the finished episode's timeline: scenes and subtitles of the chosen stretch, moved to start at 0,
# plus an end card, and the matching soundtrack (narration + music, the music running on under the end card).
# usage: build_short.py <episode timeline.json> <short spec.json> <narration.wav> <bgm.wav> <out dir>
#   episode timeline: from scripts/build_timeline.py + fit_clips.py (credits.md 3장 8번); narration/bgm: the stems that
#   were mixed into it (mix_audio.py). Writes <out>/<id>_timeline.json and <out>/<id>_audio.wav.
# Spec keys (full/shorts/<id>.json): audio_start, end, end_card {text, dur, size (px or "fit"), lines_ok}, fade_out, scenes {id: {vcx}},
#   hi_res {dir}, one_line_times (chunk times from split_subs.py: every subtitle line becomes one-line chunks),
#   split {until_line, band_top, gap, grade, top/bottom {src, in, speed, zoom, vcx, vcy}, bottom.appear_line},
#   sub_style (passed to render_short.py), header {text, height, size (px or "fit"), weight, leading, bottom or y_center} (title band on top), music {fade_in, fade_out_after, gain_db, track?, offset?}: with "track"
#   the music is that file from "offset", brought to the loudness the episode's music has over the same stretch.
import json, os, re, subprocess, sys

tl_path, spec_path, nar, bgm, out = sys.argv[1:6]
tl, sp = json.load(open(tl_path)), json.load(open(spec_path))
root = os.environ.get("VIDEO_ROOT", os.path.dirname(os.path.dirname(os.path.abspath(__file__))))  # holds work/
a0, a1 = sp["audio_start"], sp["end"]
main, card = a1 - a0, sp["end_card"]["dur"]
total = main + card
os.makedirs(out, exist_ok=True)
MIN = 0.2   # a scene or subtitle that is on screen for less than this inside the stretch belongs to its neighbour
            # (the audio starts 0.07 s before the first word, while the previous scene and line are still up)


def inside(x):
    return min(x["end"], a1) - max(x["start"], a0) >= MIN


scenes = []
for sc in tl["scenes"]:
    if not inside(sc):
        continue
    s = dict(sc)
    s["start"], s["end"] = max(sc["start"], a0) - a0, min(sc["end"], a1) - a0
    if sc["start"] < a0 and s["type"] == "video":        # the stretch starts inside this shot: start the shot earlier
        s["in"] = sc.get("in", 0) + (a0 - sc["start"]) * sc.get("speed", 1.0)
    elif sc["start"] > a0 and not scenes:                # audio starts a moment before the first scene: show it already
        s["start"] = 0.0
        if s["type"] == "video":
            s["in"] = sc.get("in", 0) - (sc["start"] - a0) * sc.get("speed", 1.0)
    s.update(sp["scenes"].get(sc["id"], {}))
    if s.get("src") and not os.path.isabs(s["src"]):      # a replacement clip named in the spec (relative to root)
        s["src"] = os.path.join(root, s["src"])
    if s["type"] == "video" and sp.get("hi_res"):
        hi = os.path.join(root, sp["hi_res"]["dir"], os.path.basename(s["src"]))
        if os.path.exists(hi):
            s["src"] = hi
        else:
            print("no hi-res file, using", s["src"])
    s.pop("why", None)
    scenes.append(s)
scenes.append({"id": "end", "type": "card", "start": main, "end": total})


def probe(path):
    r = subprocess.run(["ffprobe", "-v", "error", "-select_streams", "v", "-show_entries", "stream=width,height",
                        "-of", "csv=p=0", path], capture_output=True, text=True, check=True)
    return tuple(int(v) for v in r.stdout.strip().split(","))


def fit(part, w, h):
    """ffmpeg filters that speed up a clip, fill w x h (zoom > 1 goes closer) and keep (vcx, vcy) of it in view."""
    iw, ih = probe(os.path.join(root, part["src"]))
    k = max(w / iw, h / ih) * part.get("zoom", 1.0)
    sw, sh = max(w, round(iw * k / 2) * 2), max(h, round(ih * k / 2) * 2)
    x = min(max(part.get("vcx", 0.5) * sw - w / 2, 0), sw - w)
    y = min(max(part.get("vcy", 0.5) * sh - h / 2, 0), sh - h)
    return (f"setpts=(PTS-STARTPTS)/{part.get('speed', 1.0)},fps=30,scale={sw}:{sh}:flags=lanczos,"
            f"crop={w}:{h}:{round(x)}:{round(y)},setsar=1")


if sp.get("split"):     # owner's hook (S1 v6): the frame below the title band split in two, top first, bottom later
    c = sp["split"]
    starts = {su["line"]: su["start"] for su in tl["subs"]}
    t_end = starts[c["until_line"]] - a0                     # back to one picture when this line is spoken
    t_app = starts[c["bottom"]["appear_line"]] - a0          # the lower half appears when this line is spoken
    band, gap = c.get("band_top", 384), c.get("gap", 6)
    half = (1920 - band) // 2
    clip = f"{out}/{sp['id']}_split.mp4"
    fc = (f"[0:v]{fit(c['top'], 1080, half)}[t];"
          f"[1:v]{fit(c['bottom'], 1080, half)},tpad=start_duration={t_app:.3f}:color=black[b];"
          f"[t][b]vstack=inputs=2,drawbox=x=0:y={half - gap // 2}:w=1080:h={gap}:color=black:t=fill,"
          f"pad=1080:1920:0:{band}:color=black,format=yuv420p[v]")
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-ss", str(c["top"]["in"]), "-i", os.path.join(root, c["top"]["src"]),
                    "-ss", str(c["bottom"]["in"]), "-i", os.path.join(root, c["bottom"]["src"]), "-filter_complex", fc,
                    "-map", "[v]", "-t", f"{t_end:.3f}", "-r", "30", "-c:v", "libx264", "-crf", "10", "-preset", "veryfast",
                    clip], check=True)
    kept = []
    for s in scenes:
        if s["id"] != "end" and s["end"] <= t_end:
            continue                                         # wholly under the split
        if s["start"] < t_end:
            moved, s["start"] = t_end - s["start"], t_end
            if s["type"] == "video":
                s["in"] = s.get("in_after_split", s.get("in", 0) + moved * s.get("speed", 1.0))
        s.pop("in_after_split", None)
        kept.append(s)
    scenes = [{"id": "split", "type": "video", "src": clip, "in": 0.0, "start": 0.0, "end": t_end,
               "grade": c.get("grade", {}), "note": "split screen (build_short.py)"}] + kept
    print(f"split screen 0-{t_end:.2f} s, lower half from {t_app:.2f} s -> {clip}")

chunks = {}
if sp.get("one_line_times"):
    for c in json.load(open(os.path.join(os.path.dirname(os.path.abspath(spec_path)), sp["one_line_times"]))):
        chunks.setdefault(c["line"], []).append(c)
subs = []
for su in tl["subs"]:
    if not inside(su):
        continue
    parts = chunks.get(su["line"]) or [{"chunk": 0, "start": su["start"], "text": su["text"]}]
    for i, c in enumerate(parts):
        s = dict(su)
        s.pop("steps", None)
        end = parts[i + 1]["start"] if i + 1 < len(parts) else su["end"]
        s["start"], s["end"] = max(c["start"], a0) - a0, min(end, a1) - a0
        s["text"] = c["text"]
        if len(parts) > 1:
            s["line"] = f"{su['line']}.{c['chunk']}"
        subs.append(s)
ec = sp["end_card"]
if sp.get("header"):                      # a black band over the top with the title, for the whole Short
    h = sp["header"]
    subs.append({"line": "header", "unit": "header", "pos": "header", "text": h["text"], "start": 0.0, "end": total,
                 "lines_ok": True, **{k: h[k] for k in ("height", "size", "weight", "y_center", "gap", "leading", "bottom", "max_width", "max_size") if k in h}})
subs.append({"line": "end", "unit": "end", "text": ec["text"], "pos": "center", "start": main, "end": total,
             **({"size": ec["size"]} if ec.get("size") else {}), **({"lines_ok": True} if ec.get("lines_ok") else {})})


def lufs(path, ss, t):
    r = subprocess.run(["ffmpeg", "-hide_banner", "-nostats", "-ss", f"{ss:.3f}", "-t", f"{t:.3f}", "-i", path,
                        "-af", "ebur128", "-f", "null", "-"], capture_output=True, text=True)
    return float(re.findall(r"I:\s+(-?[\d.]+) LUFS", r.stderr)[-1])


audio = f"{out}/{sp['id']}_audio.wav"
m = sp["music"]
music, mss, mgain = bgm, a0, 0.0
if m.get("track"):
    music, mss = os.path.join(root, m["track"]), m.get("offset", 0.0)
    mgain = lufs(bgm, a0, total) - lufs(music, mss, total)
    print(f"music {os.path.basename(music)} from {mss} s, {mgain:+.2f} dB to the episode music's loudness here")
fc = (f"[0:a]aformat=channel_layouts=stereo,aresample=48000,afade=t=out:st={main - 0.06:.3f}:d=0.06,"
      f"apad=whole_dur={total:.3f}[n];"
      f"[1:a]aformat=channel_layouts=stereo,aresample=48000,volume={mgain:.3f}dB,afade=t=in:d={m['fade_in']},"
      f"afade=t=out:st={main + m['fade_out_after']:.3f}:d={card - m['fade_out_after']:.3f}[b];"
      f"[n][b]amix=inputs=2:duration=longest:normalize=0,volume={m['gain_db']}dB,"
      f"alimiter=limit={10 ** (-1.5 / 20):.5f}:attack=5:release=80:level=false:latency=true[m]")
subprocess.run(["ffmpeg", "-v", "error", "-y", "-ss", f"{a0:.3f}", "-t", f"{main:.3f}", "-i", nar,
                "-ss", f"{mss:.3f}", "-t", f"{total:.3f}", "-i", music, "-filter_complex", fc, "-map", "[m]",
                "-t", f"{total:.3f}", "-ar", "48000", "-ac", "2", "-c:a", "pcm_s16le", audio], check=True)

short = {"duration": round(total, 3), "audio": audio, "fade_in": 0.0, "fade_out": sp.get("fade_out", 0.0),
         "sub_style": sp.get("sub_style", {}), "scenes": scenes, "subs": subs, "unit_start": {}}
p = f"{out}/{sp['id']}_timeline.json"
json.dump(short, open(p, "w"), ensure_ascii=False, indent=1)
print(f"{p}: {len(scenes)} scenes, {len(subs)} subtitles, {total:.2f} s (speech {main:.2f} s + end card {card} s)")
