# v4 subtitle units + rough times (2026-10-23), the step before scripts/onsets.py and scripts/ctc_align.py.
# Units are those of v3. Every unit outside the new recording keeps its v3 rough times, carried through the edit pieces:
# old-take stretches by their take time (the first take now runs 0.2076 s later from 445.43 s on, where one old gap cut
# was left out), re-recordings by their place inside the recording. U156-U162 (re5, the owner's new recording) are
# recognised again (faster-whisper large-v3) in a window of the v4 narration.
# usage: align_v4.py <root with models/fw-large-v3> <v3 folder with align_v3_mapped.json, edit_log_v3.json>
#        <v4 folder with edit_log_v4.json, narration_v4.wav>
# Writes <v4>/align_v4_mapped.json. Next:
#   scripts/onsets.py <v4>/narration_v4.wav <v4>/align_v4_mapped.json <v4>/onsets.json
#   scripts/ctc_align.py <v4>/narration_v4.wav <v4>/onsets.json models/w2v_ko full/align_refined.json
import difflib, json, re, subprocess, sys
import numpy as np
from faster_whisper import WhisperModel

S, V3, V4 = sys.argv[1:4]
units = json.load(open(f"{V3}/align_v3_mapped.json"))
p3 = json.load(open(f"{V3}/edit_log_v3.json"))["pieces"]
p4 = json.load(open(f"{V4}/edit_log_v4.json"))["pieces"]
TAKE = lambda t: t + 0.2076 if t > 445.43 else t               # v3 take time -> v4 take time


def piece_at(pieces, t):
    return max((p for p in pieces if p[1] <= t + 1e-6), key=lambda p: p[1])


def mp(t):
    name, m3, src = piece_at(p3, t)
    if src[0] == "old":
        s = TAKE(src[1] + (t - m3))                              # time in the (v4) first take
        q = next((p for p in p4 if p[2][0] == "old" and p[2][1] - 1e-4 <= s <= p[2][2] + 1e-4), None)
        if q is None:                                            # in a stretch v4 leaves out (a shortened pause):
            q = min((p for p in p4 if p[2][0] == "old" and p[2][1] > s), key=lambda p: p[2][1])   # snap to the next joint
            snapped.append((round(t, 3), round(s, 3), q[0])); s = q[2][1]
        return round(q[1] + (s - q[2][1]), 3)
    if src[0] == "new":
        q = next(p for p in p4 if p[2] == src)
        return round(q[1] + (t - m3), 3)
    raise ValueError(f"unit time {t} inside {name}")


snapped = []
NEW = ["U156", "U157", "U158", "U159", "U160", "U161", "U162"]
out = []
for u in units:
    v = dict(u)
    if u["id"] not in NEW:
        for k in ("start_asr", "first_word_end", "end", "start"):
            v[k] = mp(u[k])
    out.append(v)
byid = {u["id"]: u for u in out}
r5 = next(p for p in p4 if p[2] == ["new", "re5"])
nxt = p4[p4.index(r5) + 1]
w0, w1 = r5[1] - 0.05, nxt[1] + 0.05                             # the re5 piece
model = WhisperModel(f"{S}/models/fw-large-v3", device="cpu", compute_type="int8", cpu_threads=4)
norm = lambda s: re.sub(r"[^0-9A-Za-z가-힣]", "", s)
pcm = subprocess.run(["ffmpeg", "-v", "error", "-ss", f"{w0}", "-t", f"{w1 - w0}", "-i", f"{V4}/narration_v4.wav",
                      "-ac", "1", "-ar", "16000", "-f", "s16le", "-"], capture_output=True, check=True).stdout
a = np.frombuffer(pcm, np.int16).astype(np.float32) / 32768
segs, _ = model.transcribe(a, language="ko", word_timestamps=True, beam_size=5, vad_filter=False)
words = [(w.start + w0, w.end + w0, w.word) for s in segs for w in s.words]
print("window:", " ".join(w for _, _, w in words))
ac, at, aw = [], [], []
for wi, (s0, s1, t) in enumerate(words):
    cs = norm(t)
    for i, c in enumerate(cs):
        ac.append(c); at.append(s0 + (s1 - s0) * i / max(len(cs), 1)); aw.append(wi)
sc, owner = [], []
for uid in NEW:
    for c in norm(byid[uid]["atext"]):
        sc.append(c); owner.append(uid)
m = {}
for blk in difflib.SequenceMatcher(None, sc, ac, autojunk=False).get_matching_blocks():
    for k in range(blk.size):
        m[blk.a + k] = blk.b + k
for uid in NEW:
    idx = [i for i, o in enumerate(owner) if o == uid]
    hit = [m[i] for i in idx if i in m]
    u = byid[uid]
    u["start_asr"] = round(at[hit[0]], 3); u["first_word_end"] = round(words[aw[hit[0]]][1], 3)
    u["end"] = round(words[aw[hit[-1]]][1], 3); u["match"] = round(len(hit) / len(idx), 2); u["src"] = f"window {w0:.1f}"
    u["start"] = u["start_asr"]
    print(uid, u["start_asr"], u["first_word_end"], u["end"], u["match"], u["text"])
for k in ("onset", "start_ctc", "timing"):                      # v3 results of the next two steps are not carried over
    for u in out:
        u.pop(k, None)
json.dump(out, open(f"{V4}/align_v4_mapped.json", "w"), ensure_ascii=False, indent=1)
print("rough times snapped to the next joint:", snapped)
print(len(out), "units")
