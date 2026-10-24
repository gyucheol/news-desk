# Cut one Short out of the finished episode's timeline: scenes and subtitles of the chosen stretch, moved to start at 0,
# plus an end card, and the matching soundtrack (narration + music, the music running on under the end card).
# usage: build_short.py <episode timeline.json> <short spec.json> <narration.wav> <bgm.wav> <out dir>
#   episode timeline: from scripts/build_timeline.py + fit_clips.py (credits.md 3장 8번); narration/bgm: the stems that
#   were mixed into it (mix_audio.py). Writes <out>/<id>_timeline.json and <out>/<id>_audio.wav.
import json, os, subprocess, sys

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

subs = []
for su in tl["subs"]:
    if not inside(su):
        continue
    s = dict(su)
    s["start"], s["end"] = max(su["start"], a0) - a0, min(su["end"], a1) - a0
    if su["line"] in sp["subs"]:
        s["text"] = sp["subs"][su["line"]]
    s.pop("steps", None)
    subs.append(s)
subs.append({"line": "end", "unit": "end", "text": sp["end_card"]["text"], "pos": "center", "start": main, "end": total})

audio = f"{out}/{sp['id']}_audio.wav"
m = sp["music"]
fc = (f"[0:a]aformat=channel_layouts=stereo,aresample=48000,afade=t=out:st={main - 0.06:.3f}:d=0.06,"
      f"apad=whole_dur={total:.3f}[n];"
      f"[1:a]aresample=48000,afade=t=in:d={m['fade_in']},"
      f"afade=t=out:st={main + m['fade_out_after']:.3f}:d={card - m['fade_out_after']:.3f}[b];"
      f"[n][b]amix=inputs=2:duration=longest:normalize=0,volume={m['gain_db']}dB,"
      f"alimiter=limit={10 ** (-1.5 / 20):.5f}:attack=5:release=80:level=false:latency=true[m]")
subprocess.run(["ffmpeg", "-v", "error", "-y", "-ss", f"{a0:.3f}", "-t", f"{main:.3f}", "-i", nar,
                "-ss", f"{a0:.3f}", "-t", f"{total:.3f}", "-i", bgm, "-filter_complex", fc, "-map", "[m]",
                "-t", f"{total:.3f}", "-ar", "48000", "-ac", "2", "-c:a", "pcm_s16le", audio], check=True)

short = {"duration": round(total, 3), "audio": audio, "fade_in": 0.0, "fade_out": sp.get("fade_out", 0.0),
         "scenes": scenes, "subs": subs, "unit_start": {}}
p = f"{out}/{sp['id']}_timeline.json"
json.dump(short, open(p, "w"), ensure_ascii=False, indent=1)
print(f"{p}: {len(scenes)} scenes, {len(subs)} subtitles, {total:.2f} s (speech {main:.2f} s + end card {card} s)")
