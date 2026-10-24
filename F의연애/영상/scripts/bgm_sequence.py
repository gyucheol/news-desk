# Background music that changes with the story (2026-10-22 request: change the music where the situation turns).
# Each segment: a track played from `offset` seconds, placed from `start` to `end` on the video timeline.
# Segments overlap by XF seconds and cross-fade (equal power). Each segment is evened out first (ffmpeg dynaudnorm,
# so a track that builds up does not climb over the narration) and set to the same loudness, then the whole bed
# gets fades at both ends and is normalised to the target LUFS (-32 under narration, mix_audio.py makes -14 overall).
# usage: bgm_sequence.py segments.json total_seconds out.wav [--lufs -32] [--fade-out 4]
# segments.json: [{"track": "work/stock/music/614.mp3", "start": 0, "end": 68.2, "offset": 0}, ...]
import json, re, subprocess, sys
import numpy as np

SR, XF = 48000, 3.0
a = sys.argv[1:]
segs, total, out = json.load(open(a[0])), float(a[1]), a[2]
lufs = a[a.index("--lufs") + 1] if "--lufs" in a else "-32"
fade_out = float(a[a.index("--fade-out") + 1]) if "--fade-out" in a else 4.0   # v2 ends 3 s after the last word


def render(seg, first):
    length = seg["end"] - seg["start"] + (0 if first else XF)       # later segments start XF early (overlap)
    cmd = ["ffmpeg", "-v", "error", "-ss", str(seg.get("offset", 0)), "-t", f"{length:.3f}", "-i", seg["track"],
           "-af", "dynaudnorm=f=500:g=31:m=8,loudnorm=I=-20:TP=-2:LRA=7", "-ac", "2", "-ar", str(SR), "-f", "f32le", "-"]
    x = np.frombuffer(subprocess.run(cmd, capture_output=True, check=True).stdout, np.float32).reshape(-1, 2).astype(np.float64)
    need = int(length * SR)
    if len(x) < need:                                   # track shorter than the segment: loop it with a cross-fade
        loops = [x]
        while sum(len(l) for l in loops) < need + SR * XF:
            loops.append(x)
        y = loops[0]
        n = int(XF * SR); f = np.sin(np.linspace(0, np.pi / 2, n))[:, None] ** 2
        for l in loops[1:]:
            y = np.concatenate([y[:-n], y[-n:] * f[::-1] + l[:n] * f, l[n:]])
        x = y
    return x[:need]


bed = np.zeros((int(total * SR) + SR, 2))
n = int(XF * SR)
fade = np.sin(np.linspace(0, np.pi / 2, n))[:, None] ** 2
for i, seg in enumerate(segs):
    x = render(seg, i == 0).copy()
    s0 = int(seg["start"] * SR) - (n if i > 0 else 0)
    if i > 0:
        x[:n] *= fade                                           # fade in during the overlap
    if i + 1 < len(segs):
        x[-n:] *= fade[::-1]                                    # fade out while the next one fades in
    a0, a1 = max(s0, 0), min(s0 + len(x), len(bed))
    if a1 > a0:
        bed[a0:a1] += x[a0 - s0:a1 - s0]
bed = bed[:int(total * SR)]
k1, k2 = int(1.0 * SR), int(fade_out * SR)
bed[:k1] *= np.linspace(0, 1, k1)[:, None]
bed[-k2:] *= np.linspace(1, 0, k2)[:, None]
tmp = out + ".tmp.wav"
subprocess.run(["ffmpeg", "-v", "error", "-y", "-f", "f32le", "-ar", str(SR), "-ac", "2", "-i", "-", "-c:a", "pcm_f32le", tmp],
               input=bed.astype(np.float32).tobytes(), check=True)
r = subprocess.run(["ffmpeg", "-hide_banner", "-i", tmp, "-af", f"loudnorm=I={lufs}:TP=-2:LRA=7:print_format=json", "-f", "null", "-"],
                   capture_output=True, text=True)
m = json.loads(re.search(r"\{[^{}]*\"input_i\"[^{}]*\}", r.stderr).group(0))
subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", tmp, "-af",
                f"loudnorm=I={lufs}:TP=-2:LRA=7:measured_I={m['input_i']}:measured_TP={m['input_tp']}:measured_LRA={m['input_lra']}"
                f":measured_thresh={m['input_thresh']}:offset={m['target_offset']}:linear=true", "-ar", str(SR), out], check=True)
subprocess.run(["rm", "-f", tmp])
print(out, f"{total:.1f}s", len(segs), "segments")
