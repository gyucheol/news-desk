# v5 subtitle units + rough times (2026-10-23), the step before scripts/onsets.py and scripts/ctc_align.py.
# Units (v5 units.json): v4 units with U233-U235 re-recorded (U234 now 서른한 살 직장인), U238-U241 replaced by the new
# wording in five units (출근하면 일할 의욕이 없고, / 퇴근해서 취미를 하나 / 만들어보려고 해도 / 너무 피곤해서 잠만 자는
# 날이 / 계속 이어졌다고 합니다.) and U249-U250 split as the owner marked (저는 이 말 중에서 / '열심히 살고 있는데도' /
# 라는 부분이 / 유독 마음에 오래 남더라고요.; the spoken 이 말 중에서 stays, owner: "녹음된 걸 기준으로").
# Every other unit keeps its v4 rough times, carried through the edit pieces (the take itself is unchanged; from re6 on
# it runs later by the new lines' extra length). The re6 / re7 units are recognised again (faster-whisper large-v3) in
# their windows of the v5 narration. The split units get rough starts in proportion to syllables (CTC places them).
# usage: align_v5.py <root with models/fw-large-v3> <v4 folder with align_v4_mapped.json, edit_log_v4.json>
#        <v5 folder with edit_log_v5.json, narration_v5.wav, units.json>
# Writes <v5>/align_v5_mapped.json. Next:
#   scripts/onsets.py <v5>/narration_v5.wav <v5>/align_v5_mapped.json <v5>/onsets_v5.json
#   scripts/ctc_align.py <v5>/narration_v5.wav <v5>/onsets_v5.json models/w2v_ko <v5>/align_v5_final.json
import difflib, json, re, subprocess, sys
import numpy as np
from faster_whisper import WhisperModel

S, V4, V5 = sys.argv[1:4]
units5 = json.load(open(f"{V5}/units.json"))
old = {u["id"]: u for u in json.load(open(f"{V4}/align_v4_mapped.json"))}
p4 = json.load(open(f"{V4}/edit_log_v4.json"))["pieces"]
p5 = json.load(open(f"{V5}/edit_log_v5.json"))["pieces"]
NEW = {"re6": ["U233", "U234", "U235"], "re7": ["U238", "U239", "U240", "U241", "U241b"]}
ATEXT = {"U233": "작년 12월, 한 언론 기사에", "U234": "31살 직장인"}     # as Whisper writes numbers


def piece_at(pieces, t):
    return max((p for p in pieces if p[1] <= t + 1e-6), key=lambda p: p[1])


snapped = []
def mp(t):
    """v4 narration time -> v5 narration time"""
    name, m4, src = piece_at(p4, t)
    if src[0] == "old":
        s = src[1] + (t - m4)                                    # time in the first take
        q = next((p for p in p5 if p[2][0] == "old" and p[2][1] - 1e-4 <= s <= p[2][2] + 1e-4), None)
        if q is None:                                            # in a stretch v5 replaces: snap to the next joint
            q = min((p for p in p5 if p[2][0] == "old" and p[2][1] > s), key=lambda p: p[2][1])
            snapped.append((round(t, 3), round(s, 3), q[0])); s = q[2][1]
        return round(q[1] + (s - q[2][1]), 3)
    if src[0] == "new":
        q = next(p for p in p5 if p[2] == src)
        return round(q[1] + (t - m4), 3)
    raise ValueError(f"unit time {t} inside {name}")


syl = lambda s: len(re.findall(r"[가-힣]", s))
o249, o250 = old["U249"], old["U250"]                           # v4: '열심히 살고 있는데도'라는 | 부분이 유독 ...
d249, d250 = o249["end"] - o249["start_asr"], o250["end"] - o250["start_asr"]
k9 = syl("열심히살고있는데도") / syl("열심히살고있는데도라는")
k3 = syl("부분이") / syl("부분이유독마음에오래남더라고요")
SPLIT = {
    "U249": (o249["start_asr"], o249["first_word_end"], o249["start_asr"] + d249 * k9),
    "U250": (o249["start_asr"] + d249 * k9, o249["end"], o250["start_asr"] + d250 * k3),
    "U250b": (o250["start_asr"] + d250 * k3, o250["start_asr"] + d250 * (k3 + 2 / 15), o250["end"]),
}
out = []
for u in units5:
    uid = u["id"]
    v = {"id": uid, "text": u["text"]}
    if uid in SPLIT:
        a, f, e = SPLIT[uid]
        v.update({"atext": u["text"], "start_asr": mp(a), "first_word_end": mp(f), "end": mp(e), "match": 1.0,
                  "src": "split (syllables)"})
        v["start"] = v["start_asr"]
    elif any(uid in ids for ids in NEW.values()):
        v["atext"] = ATEXT.get(uid, u["text"])
    else:
        o = old[uid]
        assert o["text"] == u["text"], (uid, o["text"], u["text"])
        v.update({k: o[k] for k in ("atext", "match", "src") if k in o})
        for k in ("start_asr", "first_word_end", "end", "start"):
            v[k] = mp(o[k])
    out.append(v)
byid = {u["id"]: u for u in out}
model = WhisperModel(f"{S}/models/fw-large-v3", device="cpu", compute_type="int8", cpu_threads=4)
norm = lambda s: re.sub(r"[^0-9A-Za-z가-힣]", "", s)
for rec, ids in NEW.items():
    r = next(p for p in p5 if p[2] == ["new", rec])
    nxt = p5[p5.index(r) + 1]
    w0, w1 = r[1] - 0.05, nxt[1] + 0.05
    pcm = subprocess.run(["ffmpeg", "-v", "error", "-ss", f"{w0}", "-t", f"{w1 - w0}", "-i", f"{V5}/narration_v5.wav",
                          "-ac", "1", "-ar", "16000", "-f", "s16le", "-"], capture_output=True, check=True).stdout
    a = np.frombuffer(pcm, np.int16).astype(np.float32) / 32768
    segs, _ = model.transcribe(a, language="ko", word_timestamps=True, beam_size=5, vad_filter=False)
    words = [(w.start + w0, w.end + w0, w.word) for s in segs for w in s.words]
    print(rec, "window:", " ".join(w for _, _, w in words))
    ac, at, aw = [], [], []
    for wi, (s0, s1, t) in enumerate(words):
        cs = norm(t)
        for i, c in enumerate(cs):
            ac.append(c); at.append(s0 + (s1 - s0) * i / max(len(cs), 1)); aw.append(wi)
    sc, owner = [], []
    for uid in ids:
        for c in norm(byid[uid]["atext"]):
            sc.append(c); owner.append(uid)
    m = {}
    for blk in difflib.SequenceMatcher(None, sc, ac, autojunk=False).get_matching_blocks():
        for k in range(blk.size):
            m[blk.a + k] = blk.b + k
    for uid in ids:
        idx = [i for i, o in enumerate(owner) if o == uid]
        hit = [m[i] for i in idx if i in m]
        u = byid[uid]
        u["start_asr"] = round(at[hit[0]], 3); u["first_word_end"] = round(words[aw[hit[0]]][1], 3)
        u["end"] = round(words[aw[hit[-1]]][1], 3); u["match"] = round(len(hit) / len(idx), 2); u["src"] = f"window {w0:.1f}"
        u["start"] = u["start_asr"]
        print(" ", uid, u["start_asr"], u["first_word_end"], u["end"], u["match"], u["text"])
json.dump(out, open(f"{V5}/align_v5_mapped.json", "w"), ensure_ascii=False, indent=1)
for uid in SPLIT:
    print(uid, {k: byid[uid][k] for k in ("start_asr", "first_word_end", "end")}, byid[uid]["text"])
print("rough times snapped to the next joint:", snapped)
print(len(out), "units")
