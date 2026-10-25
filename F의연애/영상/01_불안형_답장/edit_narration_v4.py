# 01편 v4 narration (2026-10-25): the v2 narration (work/v2/narration.wav) with the sigh before '내가 연락을 너무 재촉하는
# 것처럼' cut out. The owner: "' 내가 연락을 너무 재촉하는 것처럼 보이면 어떡하지.'에서 하.. 하는 녹음본은 빼주고".
# Where (measured on the loudness envelope, 10 ms and 2 ms steps): '후회가 밀려옵니다.' fades out by 117.04 s, room tone
# (-65 dB) until 117.20 s, the sigh 117.21-117.77 s (peak -18 dB), '내가' starts at 117.780 s (the nasal rises in the
# 80-900 Hz band). The cut is 117.205-117.776 s. The pause left between the two sentences is then the room tone
# 117.04-117.205 s plus 0.05 s more room tone (taken from 117.06-117.11 s): 0.21 s of silence, as at the other sentence
# breaks of this narration (v2 shortened them; measured median 0.15 s, 90% at most 0.20 s; 0.22 s before '9시 반이 되자').
# The joins are 3 ms cross-fades. Every moment after the cut moves earlier by the same amount (cut_v4.json "removed").
# usage: edit_narration_v4.py narration.wav out.wav cut.json
import json, subprocess, sys
import numpy as np

src, out, cutp = sys.argv[1:4]
SR = 48000
x = np.frombuffer(subprocess.run(["ffmpeg", "-v", "error", "-i", src, "-ac", "1", "-ar", str(SR), "-f", "f32le", "-"],
                                 capture_output=True, check=True).stdout, np.float32).astype(np.float64)
A, B = round(117.205 * SR), round(117.776 * SR)          # cut [A, B)
F0, FN = round(117.06 * SR), round(0.05 * SR)            # room tone to put back
CF = round(0.003 * SR)                                   # cross-fade length
fill = x[F0:F0 + FN].copy()
ramp = np.linspace(0.0, 1.0, CF)


def join(a, b):
    """a then b, the last CF samples of a cross-faded into the first CF samples of b."""
    return np.concatenate([a[:-CF], a[-CF:] * (1 - ramp) + b[:CF] * ramp, b[CF:]])


y = join(join(x[:A], fill), x[B:])
removed = len(x) - len(y)
subprocess.run(["ffmpeg", "-v", "error", "-y", "-f", "f32le", "-ar", str(SR), "-ac", "1", "-i", "-", "-c:a", "pcm_f32le", out],
               input=y.astype(np.float32).tobytes(), check=True)
# a time t of the old narration is t (t <= keep_until) or t - removed (t >= moved_from); times in between were cut.
# The old sample B is the first of the kept tail (faded in over the 3 ms join), new index B - removed.
info = {"source": src, "cut": [A / SR, B / SR], "fill_seconds": FN / SR, "crossfade_seconds": CF / SR,
        "removed": removed / SR, "keep_until": A / SR, "moved_from": B / SR,
        "old_seconds": len(x) / SR, "new_seconds": len(y) / SR}
json.dump(info, open(cutp, "w"), indent=1)
print(json.dumps(info))
