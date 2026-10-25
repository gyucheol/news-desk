# 01편 narration v6, step 2 (2026-10-25): the joined new recordings (join_narration_v6.py) edited by the same rules as
# the v2 narration (edit_narration_v2.py), so the new narration has the tempo the owner approved in v2-v5:
#  1. The sigh '하..' before '내가 연락을 너무 재촉하는 것처럼' is taken out (the owner, v4 list 10: "'하..' 숨소리
#     빼기"; CLAUDE.md rule 15). The span found on the new recording (sigh_v6.json, measured: see credits_v6.md) is set to
#     silence, so it becomes part of the pause before that line and is shortened with it (step 2).
#  2. Shorter pauses ("녹음 문장과 문장 사이의 빈 시간이 있다면 줄이되, 최대한 자연스럽게 줄여줘", v2): only the silent
#     middle of a pause is taken out (60 ms after the voice and 50 ms before the next voice stay; breaths stay), joined
#     with 15 ms crossfades inside the silence. Silence = 10 ms frames under (speech level - 38 dB). Remaining silence:
#     between sentences 0.22 s, before a new section 0.38 s, at a comma or inside a line at most 0.16 s; shorter pauses
#     are left as they are. The 0.20 s before the first word (join_narration_v6.py) is kept.
#  3. The end: the last word, then 3.0 s (HANDOFF_FEEDBACK.md 2장 10번), the last 0.5 s faded.
#  4. One constant gain to -14 LUFS.
# No denoise, EQ, compression or speed change (the owner recorded and edited these files).
# Writes the new narration, timemap.json (old -> new, piecewise, as edit_narration_v2.py) and a log of every pause.
# usage: edit_narration_v6.py joined.wav lines_v6.json align_rough.json sigh_v6.json out.wav timemap.json log.json
import json, re, subprocess, sys
import numpy as np

src, lines_p, align_p, sigh_p, outp, mapp, logp = sys.argv[1:8]
SR = 48000
x = np.frombuffer(subprocess.run(["ffmpeg", "-v", "error", "-i", src, "-ac", "1", "-ar", str(SR), "-f", "f32le", "-"],
                                 capture_output=True, check=True).stdout, np.float32).astype(np.float64)
lines = json.load(open(lines_p)); al = json.load(open(align_p))
assert [l["id"] for l in lines] == [a["id"] for a in al]
starts = np.array([a["start"] for a in al])
# a new section starts at these lines (the episode's parts, as in edit_narration_v2.py; the v2+ subtitles split some
# of v1's lines, so they are named by their whole text where a prefix would match other lines too)
SECTION_TEXT = ["지우는 2주째", "도대체 왜", "그 이유를 찾기 위해", "2004년", "도대체 왜 우리의 뇌는", "그런데 참 신기하죠",
                "하지만", "그렇다면", "첫째,", "둘째", "셋째", "생각해 보면", "어쩌면 답장 하나에", "여러분들만의"]
section_ids = set()
for t in SECTION_TEXT:
    hit = [o["id"] for o in lines if o["spoken"].strip() == t]
    if not hit:
        hit = [o["id"] for o in lines if o["spoken"].startswith(t)][:1]
    assert len(hit) >= 1, t
    section_ids.update(hit if t in ("도대체 왜",) else hit[:1])
assert len(section_ids) == 14, sorted(section_ids)
idx = {o["id"]: k for k, o in enumerate(lines)}

# 1. the sigh
sigh = json.load(open(sigh_p))
if sigh.get("cut"):
    a, b = sigh["cut"]
    ia, ib, f = int(a * SR), int(b * SR), int(0.005 * SR)
    x[ia - f:ia] *= np.linspace(1, 0, f)
    x[ia:ib] = 0.0

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
    if a <= 0.0 or b >= len(x) / SR - 0.02:              # the lead-in stays; the end is handled below
        continue
    k = np.nonzero((starts >= a - 0.05) & (starts <= b + 0.15))[0]
    if len(k):
        o = lines[k[0]]
        prev = re.sub(r"[\s'\"’”)\]]+$", "", lines[k[0] - 1]["spoken"]) if k[0] else ""
        if o["id"] in section_ids:
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

# build the output: the kept pieces joined with equal-power crossfades inside silence
xf = int(XF * SR)
bounds = [(0.0, cuts[0][0])] + [(cuts[k][1], cuts[k + 1][0]) for k in range(len(cuts) - 1)] + [(cuts[-1][1], keep_end)]
out = np.zeros(0)
tmap = [[0.0, 0.0]]                                      # (old time, new time) pairs at every piece start
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
json.dump({"pairs": tmap, "cuts": cuts, "lead_in": 0.0, "old_end": keep_end, "new_end": round(len(out) / SR, 3),
           "sigh": sigh.get("cut")}, open(mapp, "w"), indent=1)
kinds = {}
for e in log:
    kinds.setdefault(e["kind"], [0, 0.0]); kinds[e["kind"]][0] += 1; kinds[e["kind"]][1] += e["before"] - e["after"]
json.dump({"pauses_changed": log, "by_kind": {k: {"n": v[0], "seconds_removed": round(v[1], 2)} for k, v in kinds.items()},
           "sections": sorted(section_ids), "old_duration": round(len(x) / SR, 3), "new_duration": round(len(out) / SR, 3),
           "last_voice_old": round(end_voice, 3), "gain_db": round(20 * np.log10(g), 2), "lufs": lufs(out),
           "peak_dbfs": round(20 * np.log10(np.abs(out).max()), 2), "sigh": sigh},
          open(logp, "w"), ensure_ascii=False, indent=1)
print(f"{len(cuts)} pauses shortened, {sum(b - a for a, b in cuts):.2f} s removed | {len(x) / SR:.2f} s -> {len(out) / SR:.2f} s"
      f" | by kind {json.dumps({k: [v[0], round(v[1], 1)] for k, v in kinds.items()}, ensure_ascii=False)} | gain {20 * np.log10(g):+.2f} dB")
