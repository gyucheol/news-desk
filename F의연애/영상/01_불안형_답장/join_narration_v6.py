# 01편 narration v6, step 1 (2026-10-25): the owner's new recordings 1-8 joined in order. The owner: "녹음본 1~8번까지
# 내가 속도를 약간 올려서 녹음해왔음. 이 녹음본으로 적용해줘." The files are used as they came (the owner recorded and
# edited them; no speed change, denoise, EQ or compression here, as for v1/v2).
# Measured on the files (2026-10-25): AAC 48 kHz, the same sound in both channels (taken as mono), each already at
# -14.1 LUFS with peaks at -2.1 dBFS, nothing clipped, the spectrum cut at 15.6 kHz (an earlier lossy step, as in the
# v1 files), quiet parts gated near -70 dB. Each file starts 10-50 ms before its first word and ends 0.1-0.2 s after
# its last one.
#  - 0.20 s of silence before the first word (as v2);
#  - every file gets a 15 ms fade-in and a 20 ms fade-out (recording 7 ends on sound at -41 dB: no click at the join);
#  - 0.50 s of silence between files, so each join is a pause that edit_narration_v6.py then sets like any other pause
#    (0.22 s between sentences, 0.38 s before a new section);
#  - no end silence here (edit_narration_v6.py ends the narration 3.0 s after the last word).
# Writes 48 kHz mono float WAV and join_log.json (where each recording starts in the joined narration).
# usage: join_narration_v6.py <folder with part1.wav .. part8.wav> out.wav join_log.json
import json, subprocess, sys
import numpy as np

src, outp, logp = sys.argv[1:4]
SR = 48000
LEAD, GAP, FI, FO = 0.20, 0.50, 0.015, 0.020


def load(p):
    return np.frombuffer(subprocess.run(["ffmpeg", "-v", "error", "-i", p, "-ac", "1", "-ar", str(SR), "-f", "f32le", "-"],
                                        capture_output=True, check=True).stdout, np.float32).astype(np.float64)


out = [np.zeros(int(LEAD * SR))]
pos = len(out[0])
log = []
for i in range(1, 9):
    x = load(f"{src}/part{i}.wav")
    fi, fo = int(FI * SR), int(FO * SR)
    x[:fi] *= np.linspace(0, 1, fi)
    x[-fo:] *= np.linspace(1, 0, fo)
    log.append({"part": i, "start": round(pos / SR, 6), "seconds": round(len(x) / SR, 6)})
    out.append(x); pos += len(x)
    if i < 8:
        out.append(np.zeros(int(GAP * SR))); pos += int(GAP * SR)
y = np.concatenate(out)
subprocess.run(["ffmpeg", "-v", "error", "-y", "-f", "f32le", "-ar", str(SR), "-ac", "1", "-i", "-", "-c:a", "pcm_f32le",
                outp], input=y.astype(np.float32).tobytes(), check=True)
json.dump({"lead_in": LEAD, "gap": GAP, "parts": log, "duration": round(len(y) / SR, 6)}, open(logp, "w"), indent=1)
print(f"{len(y) / SR:.2f} s; parts start at " + ", ".join(f"{p['start']:.3f}" for p in log))
