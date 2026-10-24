# 01편 narration (2026-10-24): the owner's three edited recordings joined as the owner asked; nothing else is changed
# (speed, pauses and breaths stay as recorded: HANDOFF_FEEDBACK.md 1-1 2, 2장 2번).
#   1. 음성1 (part1.m4a, 428.92 s): whole file.
#   2. 0.15 s of silence: the two files meet at a paragraph boundary ("…울렸기 때문입니다." | "그런데 참 신기하죠.");
#      part1 ends 0.32 s after its last word and part2 starts at once, so the pause becomes about 0.5 s, the length of
#      the owner's own paragraph pauses in these recordings (0.4-0.55 s, measured).
#   3. 음성2 (part2.m4a) up to 247.22 s: the owner asked to delete the old ending, which starts at 247.28 s with
#      "마지막으로, 영상의 주제와 관련된 짧은 이야기를 …" (the echo story). The cut sits in the near-silent pause
#      (-64..-83 dB) between the end of "…꺼내 보시길 바랍니다." (tail fades out by 247.00 s) and that word.
#   4. 바뀜 (part3.m4a, 44.49 s): whole file, with one constant gain so its loudness equals the part it replaces
#      (ebur128 integrated, HANDOFF_FEEDBACK.md 2장 5번).
#   5. Silence after the last word so the video ends about 3 s after it (2장 10번).
# Then one constant gain brings the whole narration to -14 LUFS (prep_audio.py rule; no loudnorm, no limiter here).
# 10 ms fades at the joins (all inside silence). Output: 48 kHz mono 32-bit float WAV + edit_log.json.
# usage: edit_narration.py <rec folder with part1.wav part2.wav part3.wav (48 kHz mono)> out.wav log.json
import json, re, subprocess, sys
import numpy as np

rec, out, logp = sys.argv[1:4]
SR = 48000
CUT2 = 247.22
GAP12 = 0.15
TAIL = 3.0


def load(p):
    return np.frombuffer(subprocess.run(["ffmpeg", "-v", "error", "-i", p, "-ac", "1", "-ar", str(SR), "-f", "f32le", "-"],
                                        capture_output=True, check=True).stdout, np.float32).astype(np.float64)


def lufs(x):
    r = subprocess.run(["ffmpeg", "-hide_banner", "-nostats", "-f", "f32le", "-ar", str(SR), "-ac", "1", "-i", "-",
                        "-af", "ebur128=peak=true", "-f", "null", "-"], input=x.astype(np.float32).tobytes(),
                       capture_output=True)
    return float(re.findall(r"I:\s+(-?[\d.]+) LUFS", r.stderr.decode())[-1])


def last_voice(x, rel=-22.0):
    """End of the last stretch louder than (speech level + rel) dB, 10 ms frames."""
    h = SR // 100
    db = 20 * np.log10(np.sqrt(np.array([np.mean(x[i:i + h] ** 2) for i in range(0, len(x) - h, h)])) + 1e-12)
    lvl = np.percentile(db, 95)
    idx = np.where(db > lvl + rel)[0]
    return (idx[-1] + 1) * h / SR


p1, p2, p3 = load(f"{rec}/part1.wav"), load(f"{rec}/part2.wav"), load(f"{rec}/part3.wav")
k = int(CUT2 * SR)
kept2, old_end = p2[:k].copy(), p2[k:]
l_old, l3 = lufs(old_end), lufs(p3)
g3 = 10 ** ((l_old - l3) / 20)
f = int(0.01 * SR)
kept2[-f:] *= np.linspace(1, 0, f)
p3 = p3 * g3
p3[:f // 2] *= np.linspace(0, 1, f // 2)
lv3 = last_voice(p3)
tail = max(0.0, TAIL - (len(p3) / SR - lv3))
x = np.concatenate([p1, np.zeros(int(GAP12 * SR)), kept2, p3, np.zeros(int(tail * SR))])
l_all = lufs(x)
g = 10 ** ((-14.0 - l_all) / 20)
x = x * g
subprocess.run(["ffmpeg", "-v", "error", "-y", "-f", "f32le", "-ar", str(SR), "-ac", "1", "-i", "-", "-c:a", "pcm_f32le", out],
               input=x.astype(np.float32).tobytes(), check=True)
t1 = len(p1) / SR
t2 = t1 + GAP12
t3 = t2 + len(kept2) / SR
log = {"part1": {"from": 0.0, "to": round(t1, 3), "source": "part1 0..end"},
       "gap": {"from": round(t1, 3), "to": round(t2, 3), "seconds": GAP12},
       "part2": {"from": round(t2, 3), "to": round(t3, 3), "source": f"part2 0..{CUT2}"},
       "part3": {"from": round(t3, 3), "to": round(t3 + len(p3) / SR, 3), "source": "part3 0..end",
                 "gain_db": round(20 * np.log10(g3), 2), "old_end_lufs": l_old, "part3_lufs": l3},
       "last_word_end": round(t3 + lv3, 3), "silence_after": round(tail, 3), "total": round(len(x) / SR, 3),
       "final_gain_db": round(20 * np.log10(g), 2), "lufs_before_gain": l_all, "lufs": lufs(x),
       "peak_dbfs": round(20 * np.log10(np.abs(x).max()), 2)}
json.dump(log, open(logp, "w"), ensure_ascii=False, indent=1)
print(json.dumps(log, ensure_ascii=False))
