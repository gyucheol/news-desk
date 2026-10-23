# v2 subtitle units + rough times (2026-10-23), the step before scripts/onsets.py and scripts/ctc_align.py.
# Unchanged units are mapped from the v1 alignment through the edit pieces (edit_log_v2.json); the re-recorded sentences
# and the units the owner asked to split on screen (U105-U107, U229-U232) are recognised again (faster-whisper large-v3)
# in short windows of the v2 narration. Record of what was done: the v1 inputs are units.json and align_refined.json of
# commit 7220ef9 plus work/units_align.json (unit text spelled the way the recogniser writes numbers, not committed).
# usage: align_v2.py <root with models/fw-large-v3> <v1 folder> <v2 folder with edit_log_v2.json and narration_v2.wav>
# Writes <v2>/align_v2_mapped.json and <v2>/units_v2.json (= full/units.json). Next:
#   scripts/onsets.py <v2>/narration_v2.wav <v2>/align_v2_mapped.json <v2>/onsets.json
#   scripts/ctc_align.py <v2>/narration_v2.wav <v2>/onsets.json models/w2v_ko full/align_refined.json
import difflib, json, re, subprocess, sys
import numpy as np
from faster_whisper import WhisperModel
S, F, V = sys.argv[1:4]
units = json.load(open(f"{F}/units.json")); ua = {u["id"]: u["text"] for u in json.load(open(f"{F}/units_align.json"))}
old = {u["id"]: u for u in json.load(open(f"{F}/align_refined.json"))}
pieces = json.load(open(f"{V}/edit_log_v2.json"))["pieces"]
def mp(t):
    for name, new0, src in pieces:
        if src and src[0] == "old" and src[1] - 1e-6 <= t <= src[2] + 1e-6:
            return round(new0 + t - src[1], 3)
    nxt = [(src[1], new0) for name, new0, src in pieces if src and src[0] == "old" and src[1] > t]
    return round(min(nxt)[1], 3)          # inside a removed stretch: snap to the joint after it
SPLIT = {"U105": [("U105", "'제대로 관리되지 않은"), ("U106", "만성적인 직장 스트레스에서 생기는 증후군'"), ("U107", "이라고 정의했습니다.")],
         "U229": [("U229", "바로 이 때문에"), ("U229b", "번아웃을"), ("U230", "개인의 의지만의 문제로 보기는"), ("U230b", "어렵습니다.")],
         "U231": [("U231", "이쯤에서"), ("U231b", "한 사람의"), ("U232", "실제 이야기를"), ("U232b", "들려드릴게요.")]}
DROP = {"U163", "U164", "U106", "U107", "U230", "U232"}
new = []
for u in units:
    if u["id"] in SPLIT:
        new += [{"id": i, "text": t, "atext": t} for i, t in SPLIT[u["id"]]]
    elif u["id"] not in DROP:
        new.append({"id": u["id"], "text": u["text"], "atext": ua[u["id"]]})
# windows (v2 time) and the units recognised in each; neighbours with no pause between are included for context
WIN = [(mp(159.40), mp(165.90), ["U104", "U105", "U106", "U107"]),
       (mp(360.02), mp(366.50), ["U229", "U229b", "U230", "U230b", "U231", "U231b", "U232", "U232b"]),
       (400.00, 408.00, ["U256", "U257", "U258", "U259", "U260"]),
       (453.70, 463.30, ["U292", "U293", "U294", "U295", "U296", "U297"]),
       (475.80, 486.40, ["U306", "U307", "U308", "U309", "U310", "U311"])]
model = WhisperModel(f"{S}/models/fw-large-v3", device="cpu", compute_type="int8", cpu_threads=4)
norm = lambda s: re.sub(r"[^0-9A-Za-z가-힣]", "", s)
byid = {u["id"]: u for u in new}
for w0, w1, ids in WIN:
    pcm = subprocess.run(["ffmpeg", "-v", "error", "-ss", f"{w0}", "-t", f"{w1 - w0}", "-i", f"{V}/narration_v2.wav",
                          "-ac", "1", "-ar", "16000", "-f", "s16le", "-"], capture_output=True, check=True).stdout
    a = np.frombuffer(pcm, np.int16).astype(np.float32) / 32768
    segs, _ = model.transcribe(a, language="ko", word_timestamps=True, beam_size=5, vad_filter=False)
    words = [(w.start + w0, w.end + w0, w.word) for s in segs for w in s.words]
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
        if not hit:
            print("NO MATCH", uid); continue
        first, last = hit[0], hit[-1]
        u = byid[uid]
        u["start_asr"] = round(at[first], 3); u["first_word_end"] = round(words[aw[first]][1], 3)
        u["end"] = round(words[aw[last]][1], 3); u["match"] = round(len(hit) / len(idx), 2); u["src"] = f"window {w0:.1f}"
    print(f"window {w0:.1f}-{w1:.1f}:", " ".join(w for _, _, w in words))
for u in new:
    if "start_asr" not in u:
        o = old[u["id"]]
        u["start_asr"] = mp(o["start_asr"]); u["first_word_end"] = mp(o["first_word_end"]); u["end"] = mp(o["end"])
        u["match"] = o.get("match"); u["src"] = "mapped"
    u["start"] = u["start_asr"]
json.dump(new, open(f"{V}/align_v2_mapped.json", "w"), ensure_ascii=False, indent=1)
json.dump([{"id": u["id"], "text": u["text"]} for u in new], open(f"{V}/units_v2.json", "w"), ensure_ascii=False, indent=1)
bad = [(u["id"], u["match"]) for u in new if u.get("match") is not None and u["match"] < 0.8]
print(len(new), "units; low match:", bad)
