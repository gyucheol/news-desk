# Render a long timeline with several render.py processes (F의 연애, 2026-10-24): the frames are split at scene starts
# into N parts of about the same length, each part is encoded video-only (same x264 settings as render.py), then the
# parts are joined without re-encoding and the soundtrack is added once (AAC, 48 kHz, stereo, faststart).
# AAC 320 kbps since 01 v2 (2026-10-24): at 192 kbps ffmpeg's AAC encoder left audible artefacts in the
# 4-15 kHz band of the owner's voice (error/signal median -21 dB, 48 bad frames; at 320 kbps -32 dB, 2 frames).
# --video-only (F의 연애 01 v3, 2026-10-25): join the parts without sound, so the picture can be made while the music is
# still being chosen (the frames do not depend on the sound); add the sound later with the same AAC settings:
#   ffmpeg -i video.mp4 -i final_audio.wav -map 0:v -map 1:a -c:v copy -c:a aac -b:a 320k -ar 48000 -ac 2
#          -movflags +faststart out.mp4
# (no -shortest there: the sound ends a few ms before the last frame does, and -shortest dropped that frame in 01 v3)
# usage: render_parallel.py timeline.json out.mp4 [parts=3] [--video-only]
import json, os, subprocess, sys
here = os.path.dirname(os.path.abspath(__file__))
video_only = "--video-only" in sys.argv
args = [a for a in sys.argv[1:] if a != "--video-only"]
tl_path, out = args[0], args[1]
n = int(args[2]) if len(args) > 2 else 3
tl = json.load(open(tl_path))
FPS = 30
nfr = round(tl["duration"] * FPS)
cuts = sorted({round(sc["start"] * FPS) for sc in tl["scenes"]} | {0})
bounds = [0]
for k in range(1, n):
    target = nfr * k / n
    bounds.append(min(cuts, key=lambda c: abs(c - target)))
bounds = sorted(set(bounds)) + [nfr]
parts, procs = [], []
for a, b in zip(bounds, bounds[1:]):
    p = out.replace(".mp4", f"_part{a:06d}.mp4")
    parts.append(p)
    procs.append(subprocess.Popen([sys.executable, f"{here}/render.py", tl_path, p, "--range", f"{a},{b}"]))
codes = [q.wait() for q in procs]
assert all(c == 0 for c in codes), codes
lst = out.replace(".mp4", "_parts.txt")
open(lst, "w").write("".join(f"file '{os.path.abspath(p)}'\n" for p in parts))
if video_only:
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-f", "concat", "-safe", "0", "-i", lst, "-map", "0:v", "-c:v", "copy",
                    "-movflags", "+faststart", out], check=True)
else:
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-f", "concat", "-safe", "0", "-i", lst, "-i", tl["audio"],
                    "-map", "0:v", "-map", "1:a", "-c:v", "copy", "-c:a", "aac", "-b:a", "320k", "-ar", "48000", "-ac", "2",
                    "-shortest", "-movflags", "+faststart", out], check=True)
for p in parts + [lst]:
    os.remove(p)
print("wrote", out, nfr, "frames in", len(parts), "parts:", bounds)
