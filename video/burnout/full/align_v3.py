# v3 subtitle units + rough times (2026-10-23), the step before scripts/onsets.py and scripts/ctc_align.py.
# The owner changed one line near the start and re-recorded it (edit_narration_v3.py): U012-U013 become three units
# (U012 / U012b / U013). Those are recognised again (faster-whisper large-v3) in a short window of the v3 narration;
# every other unit keeps its v2 rough times (align_v2_mapped.json), moved by the length change after the new line.
# usage: align_v3.py <root with models/fw-large-v3> <v2 folder with align_v2_mapped.json> <v3 folder with edit_log_v3.json
#        and narration_v3.wav>
# Writes <v3>/align_v3_mapped.json and <v3>/units_v3.json (= full/units.json). Next:
#   scripts/onsets.py <v3>/narration_v3.wav <v3>/align_v3_mapped.json <v3>/onsets.json
#   scripts/ctc_align.py <v3>/narration_v3.wav <v3>/onsets.json models/w2v_ko full/align_refined.json
import difflib, json, re, subprocess, sys
import numpy as np
from faster_whisper import WhisperModel

S, V2, V3 = sys.argv[1:4]
old = json.load(open(f"{V2}/align_v2_mapped.json"))
pieces = {p[0].split(" ")[0] + " " + p[0].split(" ")[1]: p for p in json.load(open(f"{V3}/edit_log_v3.json"))["pieces"]}
# v2 kept the first take unchanged up to 249.30 s, so v2 time = take time there; v3 replaced 15.33-18.20 of it
cut0, cut1 = 15.33, 18.20
shift = round(pieces["old 18.20-249.30"][1] - cut1, 3)          # the new line is this much longer than the old one
mp = lambda t: round(t if t <= cut0 else t + shift, 3)
NEW = [("U012", "그렇다면 오늘 이야기가"), ("U012b", "그 질문의 답을 찾는 데"), ("U013", "작은 힌트가 될지도 모르겠습니다.")]
units = []
for u in old:
    if u["id"] == "U012":
        units += [{"id": i, "text": t, "atext": t} for i, t in NEW]
    elif u["id"] != "U013":
        v = dict(u)
        for k in ("start_asr", "first_word_end", "end", "start"):
            v[k] = mp(u[k])
        units.append(v)
byid = {u["id"]: u for u in units}
w0, w1 = 14.90, 19.95                       # v3 time: the pause after U011 to just before U014
model = WhisperModel(f"{S}/models/fw-large-v3", device="cpu", compute_type="int8", cpu_threads=4)
norm = lambda s: re.sub(r"[^0-9A-Za-z가-힣]", "", s)
pcm = subprocess.run(["ffmpeg", "-v", "error", "-ss", f"{w0}", "-t", f"{w1 - w0}", "-i", f"{V3}/narration_v3.wav",
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
for uid, _ in NEW:
    for c in norm(byid[uid]["atext"]):
        sc.append(c); owner.append(uid)
m = {}
for blk in difflib.SequenceMatcher(None, sc, ac, autojunk=False).get_matching_blocks():
    for k in range(blk.size):
        m[blk.a + k] = blk.b + k
for uid, _ in NEW:
    idx = [i for i, o in enumerate(owner) if o == uid]
    hit = [m[i] for i in idx if i in m]
    u = byid[uid]
    u["start_asr"] = round(at[hit[0]], 3); u["first_word_end"] = round(words[aw[hit[0]]][1], 3)
    u["end"] = round(words[aw[hit[-1]]][1], 3); u["match"] = round(len(hit) / len(idx), 2); u["src"] = f"window {w0:.1f}"
    u["start"] = u["start_asr"]
    print(uid, u["start_asr"], u["first_word_end"], u["end"], u["match"])
json.dump(units, open(f"{V3}/align_v3_mapped.json", "w"), ensure_ascii=False, indent=1)
json.dump([{"id": u["id"], "text": u["text"]} for u in units], open(f"{V3}/units_v3.json", "w"), ensure_ascii=False, indent=1)
print(len(units), "units, shift", shift)
