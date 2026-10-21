# Snap subtitle-unit start times to the real speech onset.
# Recognized word starts after a pause tend to absorb the pause (0.3-0.7 s early in testing).
# Inside [asr_start - 0.1, end of the unit's first word] we take the longest quiet gap (>= 60 ms)
# and move the start to its end. A pause is expected only at the very start or after punctuation
# in the script; mid-phrase units accept only a gap right at the recognized boundary.
# usage: refine.py audio align.json out.json
import sys, json, subprocess
import numpy as np

audio, inp, outp = sys.argv[1:4]
pcm = subprocess.run(["ffmpeg", "-v", "error", "-i", audio, "-ac", "1", "-ar", "16000", "-f", "s16le", "-"],
                     capture_output=True, check=True).stdout
x = np.frombuffer(pcm, np.int16).astype(np.float32) / 32768
rms = np.sqrt(np.convolve(x ** 2, np.ones(400) / 400, mode="same")[::160] + 1e-12)  # 25 ms window, 10 ms hop
db = 20 * np.log10(rms)
peak = np.percentile(db, 95)
th = peak - 35          # relative to the speech level, so it adapts to a real microphone recording
quiet = db < th


def gaps(a, b):
    out, i = [], max(int(a / 0.01), 0)
    b = min(int(b / 0.01), len(quiet))
    while i < b:
        if quiet[i]:
            j = i
            while j < len(quiet) and quiet[j]:
                j += 1
            out.append((i * 0.01, j * 0.01)); i = j
        else:
            i += 1
    return out


PUNCT = tuple(",.?!'\"…”’")
units = json.load(open(inp))
for k, u in enumerate(units):
    s, fwe = u["start"], u.get("first_word_end") or u["start"] + 0.6
    expect_pause = k == 0 or units[k - 1]["text"].rstrip().endswith(PUNCT)
    g = [(a, b) for a, b in gaps(s - 0.1, fwe) if b - a >= 0.06]
    if not expect_pause:
        g = [(a, b) for a, b in g if a <= s + 0.1]
    u["start_asr"], u["pause_expected"] = s, expect_pause
    if g:
        a, b = max(g, key=lambda ab: ab[1] - ab[0])
        u["start"] = round(b, 3)
json.dump(units, open(outp, "w"), ensure_ascii=False, indent=1)
print(f"speech level {peak:.1f} dB, quiet below {th:.1f} dB")
for u in units:
    print(u["id"], "asr", round(u["start_asr"], 2), "-> start", u["start"])
