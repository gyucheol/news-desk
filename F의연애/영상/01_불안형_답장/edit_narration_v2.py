# 01편 narration v2 (2026-10-24, owner feedback on v1). Input: the v1 narration (edit_narration.py: part1 whole, 0.15 s,
# part2 up to 247.22 s, part3 whole; one constant gain) and the v1 line times (lines_align.json, same clock).
# Changes, nothing else (no denoise, EQ, compression or speed change: the owner edited these recordings):
#  1. 0.20 s of silence before the first word (part1 starts with voice in its first 20 ms) and a 20 ms fade-in where
#     part2 starts: the owner's file begins on an edit cut at 18.6 ms, which was an audible click at 7:09 in v1.
#  2. Shorter pauses ("녹음 문장과 문장 사이의 빈 시간이 있다면 줄이되, 최대한 자연스럽게 줄여줘"): only the silent middle
#     of a pause is taken out (60 ms after the voice and 50 ms before the next voice stay; breaths stay), joined with
#     15 ms crossfades inside the silence. Silence = 10 ms frames under (speech level - 38 dB), the level of the
#     owner's gated pauses. Targets for the remaining silence: between sentences 0.22 s, before a new section 0.38 s,
#     at a comma or inside a line at most 0.16 s; shorter pauses are left as they are.
#  3. The end: the last word, then 3.0 s (HANDOFF_FEEDBACK.md 2장 10번).
#  4. One constant gain to -14 LUFS.
# Writes the new narration, timemap.json (old -> new, piecewise) and a log of every pause it changed.
# usage: edit_narration_v2.py narration_v1.wav lines.json lines_align.json out.wav timemap.json log.json
import json, re, subprocess, sys
import numpy as np

src, lines_p, align_p, outp, mapp, logp = sys.argv[1:7]
SR = 48000
x = np.frombuffer(subprocess.run(["ffmpeg", "-v", "error", "-i", src, "-ac", "1", "-ar", str(SR), "-f", "f32le", "-"],
                                 capture_output=True, check=True).stdout, np.float32).astype(np.float64)
lines = json.load(open(lines_p)); al = json.load(open(align_p))
assert [l["id"] for l in lines] == [a["id"] for a in al]
starts = np.array([a["start"] for a in al])
# a new section starts at these lines (the episode's parts, build_spec.py plan headers)
SECTION = ("지우는 2주째", "도대체 왜, 작은", "그 이유를 찾기 위해", "2004년", "도대체 왜 우리의 뇌는", "그런데 참 신기하죠",
           "하지만, 괜찮습니다", "자, 그렇다면", "첫째,", "둘째,", "셋째,", "생각해 보면", "어쩌면 답장 하나에", "여러분들만의")

# 1. fades at the edit points
P2 = 429.078                                             # part2 starts here in the v1 narration (edit_log.json)
i2 = int(P2 * SR); cut = int(0.0187 * SR); n15 = int(0.015 * SR)
x[i2:i2 + cut] = 0.0                                     # the fragment before the owner's edit cut at 18.6 ms
x[i2 + cut:i2 + cut + n15] *= np.linspace(0, 1, n15)
c1 = int(0.0121 * SR)                                    # part1 also starts on an edit cut (12 ms)
x[:c1] = 0.0
x[c1:c1 + n15] *= np.linspace(0, 1, n15)


def repair(t, before=0.0006, after=0.0010, order=24, ctx=0.03):
    """Single-sample clicks in the owner's files (found by scripts/jumps2.py): the 1.6 ms around the click are
    replaced by forward and backward linear prediction from 30 ms on each side, cross-faded."""
    g0, g1 = int((t - before) * SR), int((t + after) * SR)
    L_, R_ = x[g0 - int(ctx * SR):g0], x[g1:g1 + int(ctx * SR)]

    def coef(s):
        r = np.correlate(s, s, "full")[len(s) - 1:len(s) + order]
        from scipy.linalg import solve_toeplitz
        return solve_toeplitz(r[:order] * np.r_[1.0001, np.ones(order - 1)], r[1:order + 1])
    n = g1 - g0
    a, b = coef(L_), coef(R_[::-1])
    fw = list(L_[-order:]); bw = list(R_[:order][::-1])
    for _ in range(n):
        fw.append(float(np.dot(a, fw[-1:-order - 1:-1])))
        bw.append(float(np.dot(b, bw[-1:-order - 1:-1])))
    w = np.linspace(0, 1, n)
    x[g0:g1] = np.array(fw[order:]) * (1 - w) + np.array(bw[order:][::-1]) * w


for t in (227.2208, 355.0007):                           # v1 narration clock
    repair(t)

# 2. pauses
hop = 480
nf = len(x) // hop
db = 20 * np.log10(np.sqrt((x[:nf * hop].reshape(nf, hop) ** 2).mean(1)) + 1e-12)
level = np.percentile(db, 95)
quiet = db < level - 38
runs, i = [], 0
while i < nf:
    if quiet[i]:
        j = i
        while j < nf and quiet[j]:
            j += 1
        if j - i >= 8:
            runs.append((i * 0.01, j * 0.01))
        i = j
    else:
        i += 1
cuts, log = [], []                                       # (start, end) of removed audio, old clock
HEAD, TAIL, XF = 0.06, 0.05, 0.015
for a, b in runs:
    if b >= len(x) / SR - 0.02:                          # the end silence is handled below
        continue
    k = np.nonzero((starts >= a - 0.05) & (starts <= b + 0.15))[0]
    if len(k):
        nxt = lines[k[0]]["spoken"].strip()
        prev = re.sub(r"[\s'\"’”)\]]+$", "", lines[k[0] - 1]["spoken"]) if k[0] else ""
        if nxt.startswith(SECTION):
            kind, target = "section", 0.38
        elif prev.endswith((".", "?", "!")):
            kind, target = "sentence", 0.22
        else:
            kind, target = "comma", 0.16
    else:
        kind, target = "inside", 0.16
    dur = b - a
    if dur <= target + 0.01:
        continue
    c0, c1 = a + HEAD, b - TAIL                          # removable part
    remove = min(dur - target, c1 - c0)
    if remove < 0.02:
        continue
    mid = (c0 + c1) / 2
    cuts.append((round(mid - remove / 2, 4), round(mid + remove / 2, 4)))
    log.append({"at": round(a, 3), "kind": kind, "before": round(dur, 3), "after": round(dur - remove, 3),
                "next": lines[k[0]]["spoken"][:16] if len(k) else ""})
# 3. end: the last voice frame, then 3.0 s
voiced = np.nonzero(~quiet)[0]
end_voice = (voiced[-1] + 1) * 0.01
keep_end = end_voice + 3.0

# build the output: lead-in, then the kept pieces joined with equal-power crossfades inside silence
xf = int(XF * SR)
pieces, t = [], 0.0
bounds = [(0.0, cuts[0][0])] + [(cuts[k][1], cuts[k + 1][0]) for k in range(len(cuts) - 1)] + [(cuts[-1][1], keep_end)]
out = np.zeros(int(0.20 * SR))
tmap = [[0.0, 0.20]]                                     # (old time, new time) pairs at every piece start
for a, b in bounds:
    seg = x[int(a * SR):min(int(b * SR), len(x))]
    if b > len(x) / SR:
        seg = np.concatenate([seg, np.zeros(int((b - len(x) / SR) * SR))])
    if len(out) >= xf and len(seg) >= xf and a > 0:
        w = np.sin(np.linspace(0, np.pi / 2, xf)) ** 2
        tmap.append([a + XF / 2, (len(out) - xf / 2) / SR])
        out[-xf:] = out[-xf:] * (1 - w) + seg[:xf] * w
        out = np.concatenate([out, seg[xf:]])
    else:
        out = np.concatenate([out, seg])
fo = int(0.5 * SR)                                       # the end is silence already; keep it clean
out[-fo:] *= np.linspace(1, 0, fo) ** 2


# 4. constant gain to -14 LUFS
def lufs(y):
    r = subprocess.run(["ffmpeg", "-hide_banner", "-nostats", "-f", "f32le", "-ar", str(SR), "-ac", "1", "-i", "-",
                        "-af", "ebur128=peak=true", "-f", "null", "-"], input=y.astype(np.float32).tobytes(),
                       capture_output=True)
    return float(re.findall(r"I:\s+(-?[\d.]+) LUFS", r.stderr.decode())[-1])


l0 = lufs(out)
g = 10 ** ((-14.0 - l0) / 20)
out *= g
subprocess.run(["ffmpeg", "-v", "error", "-y", "-f", "f32le", "-ar", str(SR), "-ac", "1", "-i", "-", "-c:a", "pcm_f32le",
                outp], input=out.astype(np.float32).tobytes(), check=True)
json.dump({"pairs": tmap, "cuts": cuts, "lead_in": 0.20, "old_end": keep_end, "new_end": round(len(out) / SR, 3)},
          open(mapp, "w"), indent=1)
kinds = {}
for e in log:
    kinds.setdefault(e["kind"], [0, 0.0]); kinds[e["kind"]][0] += 1; kinds[e["kind"]][1] += e["before"] - e["after"]
json.dump({"pauses_changed": log, "by_kind": {k: {"n": v[0], "seconds_removed": round(v[1], 2)} for k, v in kinds.items()},
           "old_duration": round(len(x) / SR, 3), "new_duration": round(len(out) / SR, 3), "last_voice_old": round(end_voice, 3),
           "gain_db": round(20 * np.log10(g), 2), "lufs": lufs(out), "peak_dbfs": round(20 * np.log10(np.abs(out).max()), 2)},
          open(logp, "w"), ensure_ascii=False, indent=1)
print(f"{len(cuts)} pauses shortened, {sum(b - a for a, b in cuts):.2f} s removed | {len(x) / SR:.2f} s -> {len(out) / SR:.2f} s"
      f" | by kind {json.dumps({k: [v[0], round(v[1], 1)] for k, v in kinds.items()}, ensure_ascii=False)} | gain {20 * np.log10(g):+.2f} dB")
