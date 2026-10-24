# Cut one Short out of the finished episode's timeline: scenes and subtitles of the chosen stretch, moved to start at 0,
# plus an end card, and the matching soundtrack (narration + music, the music running on under the end card).
# usage: build_short.py <episode timeline.json> <short spec.json> <narration.wav> <bgm.wav> <out dir>
#   episode timeline: from scripts/build_timeline.py + fit_clips.py (credits.md 3장 8번); narration/bgm: the stems that
#   were mixed into it (mix_audio.py). Writes <out>/<id>_timeline.json and <out>/<id>_audio.wav.
# Spec keys (full/shorts/<id>.json): audio_start, end, end_card {text, dur, size (px or "fit"), lines_ok}, fade_out, scenes {id: {vcx}},
#   hi_res {dir}, one_line_times (chunk times from split_subs.py: every subtitle line becomes one-line chunks),
#   sub_style (passed to render_short.py), header {text, height, size, weight, y_center, gap} (title band on top), music {fade_in, fade_out_after, gain_db, track?, offset?}: with "track"
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
    if s["type"] == "video" and sp.get("hi_res"):
        hi = os.path.join(root, sp["hi_res"]["dir"], os.path.basename(s["src"]))
        if os.path.exists(hi):
            s["src"] = hi
        else:
            print("no hi-res file, using", s["src"])
    s.pop("why", None)
    scenes.append(s)
scenes.append({"id": "end", "type": "card", "start": main, "end": total})

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
                 "lines_ok": True, **{k: h[k] for k in ("height", "size", "weight", "y_center", "gap") if k in h}})
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
