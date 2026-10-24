# F의 연애 01 (2026-10-24): makes work/rec/part{1,2,3}_words.json for align_words.py (run_align.sh).
# Whisper words with timestamps for one recording (same settings as align.py: large-v3 int8, beam 5, no prompt, no VAD).
# usage: transcribe.py audio out.json [threads]
import json, os, subprocess, sys, time
import numpy as np
from faster_whisper import WhisperModel
ROOT = os.environ["VIDEO_ROOT"]
audio, outp = sys.argv[1], sys.argv[2]
threads = int(sys.argv[3]) if len(sys.argv) > 3 else 4
t0 = time.time()
model = WhisperModel(f"{ROOT}/models/fw-large-v3", device="cpu", compute_type="int8", cpu_threads=threads)
pcm = subprocess.run(["ffmpeg", "-v", "error", "-i", audio, "-ac", "1", "-ar", "16000", "-f", "s16le", "-"],
                     capture_output=True, check=True).stdout
x = np.frombuffer(pcm, np.int16).astype(np.float32) / 32768
segs, info = model.transcribe(x, language="ko", word_timestamps=True, beam_size=5, vad_filter=False)
out = []
for s in segs:
    out.append({"start": s.start, "end": s.end, "text": s.text,
                "words": [[round(w.start, 3), round(w.end, 3), w.word, round(w.probability, 3)] for w in s.words]})
    print(f"{s.start:7.2f} {s.end:7.2f} {s.text}", flush=True)
json.dump(out, open(outp, "w"), ensure_ascii=False, indent=1)
print(f"done {time.time() - t0:.0f}s", flush=True)
