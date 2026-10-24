# Find when each subtitle unit is spoken in a narration recording.
# 1) faster-whisper large-v3 word timestamps  2) character-level alignment of the known script
# to the recognized text (difflib), so recognition typos do not matter.
# Run refine.py afterwards: recognized word starts after a pause usually include the pause.
# usage: align.py audio units.json out.json [threads]
#   units.json: [{"id": "U1", "text": "주말 내내 분명 푹 잤는데,"}, ...] in script order
# Do not pass the script as initial_prompt: in testing that made Whisper skip the first sentence.
import os, sys, json, re, difflib, time, subprocess
import numpy as np
from faster_whisper import WhisperModel

ROOT = os.environ.get("VIDEO_ROOT", os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
audio, units_path, out_path = sys.argv[1], sys.argv[2], sys.argv[3]
threads = int(sys.argv[4]) if len(sys.argv) > 4 else (os.cpu_count() or 4)
units = json.load(open(units_path))
norm = lambda s: re.sub(r"[^0-9A-Za-z가-힣]", "", s)

t0 = time.time()
model = WhisperModel(f"{ROOT}/models/fw-large-v3", device="cpu", compute_type="int8", cpu_threads=threads)
pcm = subprocess.run(["ffmpeg", "-v", "error", "-i", audio, "-ac", "1", "-ar", "16000", "-f", "s16le", "-"],
                     capture_output=True, check=True).stdout
samples = np.frombuffer(pcm, np.int16).astype(np.float32) / 32768
segs, info = model.transcribe(samples, language="ko", word_timestamps=True, beam_size=5, vad_filter=False)
words = [(w.start, w.end, w.word) for s in segs for w in s.words]
print(f"asr {time.time()-t0:.1f}s:", "".join(w for _, _, w in words), flush=True)

asr_chars, asr_t, asr_w = [], [], []
for wi, (a, b, w) in enumerate(words):
    cs = norm(w)
    for i, c in enumerate(cs):  # spread a word's time evenly over its characters
        asr_chars.append(c); asr_t.append((a + (b - a) * i / len(cs), a + (b - a) * (i + 1) / len(cs)))
        asr_w.append(wi)
sc_chars, sc_unit = [], []
for k, u in enumerate(units):
    for c in norm(u["text"]):
        sc_chars.append(c); sc_unit.append(k)
sm = difflib.SequenceMatcher(None, sc_chars, asr_chars, autojunk=False)
m = {}
for blk in sm.get_matching_blocks():
    for j in range(blk.size):
        m[blk.a + j] = blk.b + j
res = []
for k, u in enumerate(units):
    hit = [m[i] for i, uu in enumerate(sc_unit) if uu == k and i in m]
    n = sum(1 for uu in sc_unit if uu == k)
    res.append({"id": u["id"], "text": u["text"],
                "start": float(asr_t[min(hit)][0]) if hit else None,
                "end": float(asr_t[max(hit)][1]) if hit else None,
                "first_word_end": float(words[asr_w[min(hit)]][1]) if hit else None,
                "match": round(len(hit) / max(n, 1), 2)})
# units the recognizer missed: interpolate between neighbours so nothing is dropped silently
for k, r in enumerate(res):
    if r["start"] is None:
        prev = next((res[j]["end"] for j in range(k - 1, -1, -1) if res[j]["end"] is not None), 0.0)
        r["start"] = r["end"] = r["first_word_end"] = prev
        r["warning"] = "not recognized - check by ear"
json.dump(res, open(out_path, "w"), ensure_ascii=False, indent=1)
for r in res:
    print(r["id"], round(r["start"], 2), round(r["end"], 2), "match", r["match"], r.get("warning", ""))
