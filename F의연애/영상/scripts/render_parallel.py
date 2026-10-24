# Render a long timeline with several render.py processes (F의 연애, 2026-10-24): the frames are split at scene starts
# into N parts of about the same length, each part is encoded video-only (same x264 settings as render.py), then the
# parts are joined without re-encoding and the soundtrack is added once (AAC 192 kbps, 48 kHz, stereo, faststart).
# usage: render_parallel.py timeline.json out.mp4 [parts=3]
import json, os, subprocess, sys
here = os.path.dirname(os.path.abspath(__file__))
tl_path, out = sys.argv[1], sys.argv[2]
n = int(sys.argv[3]) if len(sys.argv) > 3 else 3
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
subprocess.run(["ffmpeg", "-v", "error", "-y", "-f", "concat", "-safe", "0", "-i", lst, "-i", tl["audio"],
                "-map", "0:v", "-map", "1:a", "-c:v", "copy", "-c:a", "aac", "-b:a", "192k", "-ar", "48000", "-ac", "2",
                "-shortest", "-movflags", "+faststart", out], check=True)
for p in parts + [lst]:
    os.remove(p)
print("wrote", out, nfr, "frames in", len(parts), "parts:", bounds)
