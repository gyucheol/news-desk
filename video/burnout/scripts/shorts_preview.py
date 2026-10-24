# Cuts preview clips of the Shorts/Reels candidates out of the finished landscape video, so the owner can watch them.
# usage: shorts_preview.py <shorts_candidates.json> <finished video> <out dir> [--series]
#   --series: S1 starts at its series_start (with the "첫 번째 신호" line).
# The audio starts in the silence just before the first word; until the first line's scene appears (video_start),
# the picture holds that scene's first frame, so no frame of the previous scene shows. The clip ends in the silence
# after the last word's tail. A 30 ms fade-in and 60 ms fade-out keep the music from clicking.
import json, math, os, subprocess, sys

spec, video, out = sys.argv[1:4]
series = "--series" in sys.argv
FPS = 30
os.makedirs(out, exist_ok=True)
for c in json.load(open(spec))["candidates"]:
    a0, v0, end = c["audio_start"], c["video_start"], c["end"]
    if series and "series_start" in c:
        a0, v0 = c["series_start"]["audio_start"], c["series_start"]["video_start"]
    first = math.ceil(v0 * FPS - 1e-6) / FPS          # first frame at or after the scene change
    lead, dur = first - a0, end - a0
    mmss = lambda t: f"{int(t // 60)}{int(t % 60):02d}"
    name = f"{out}/shorts_{c['id']}_{mmss(v0)}-{mmss(end)}.mp4"
    fc = (f"[0:v]trim=start={lead - 0.001:.3f},setpts=PTS-STARTPTS,"
          f"tpad=start_duration={lead:.3f}:start_mode=clone[v];"
          f"[0:a]afade=t=in:d=0.03,afade=t=out:st={dur - 0.06:.3f}:d=0.06[a]")
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-ss", f"{a0:.3f}", "-t", f"{dur:.3f}", "-i", video,
                    "-filter_complex", fc, "-map", "[v]", "-map", "[a]", "-t", f"{dur:.3f}",
                    "-c:v", "libx264", "-crf", "21", "-preset", "medium", "-pix_fmt", "yuv420p", "-r", str(FPS),
                    "-c:a", "aac", "-b:a", "192k", "-movflags", "+faststart", name], check=True)
    print(f"{c['id']} {a0:.2f}-{end:.2f} ({dur:.1f} s, picture held {lead:.2f} s) -> {name}")
