# v2 narration edit (2026-10-23 owner feedback): cut U163-U164, replace U256-U260 / U292-U297 / U306-U311 with the
# owner's re-recordings, a breathing pause after U270, end 3 s after the last word. Cuts sit inside pauses; joints get
# 10 ms equal-power fades. Pauses are filled with the quietest 0.4 s of the old take (room tone, about -46 dB).
# Record of exactly what was done; it needs the owner's recordings, which are not in the repository.
# usage: edit_narration_v2.py <v1 narration.wav> <folder with re1_pol.wav re2_pol.wav re3_pol.wav> <out folder>
#   v1 narration.wav: polish_voice.py output of the first take (credits.md 3장 2번); re*_pol.wav: the re-recordings after
#   polish_voice.py (--words with recognised word times). Then: scripts/prep_audio.py <out>/narration_v2_raw.wav <out>/narration_v2.wav
# Writes <out>/narration_v2_raw.wav and <out>/edit_log_v2.json (piece list: where each stretch of the new file comes from).
import json, re, subprocess, sys
import numpy as np

# speech / silence analysis on a mono wav (10 ms frames)
SR = 48000
def load(p):
    return np.frombuffer(subprocess.run(["ffmpeg", "-v", "error", "-i", p, "-ac", "1", "-ar", str(SR), "-f", "f32le", "-"],
                                        capture_output=True, check=True).stdout, np.float32).copy()
def frames_db(x, hop=0.01, win=0.03):
    h, w = int(hop * SR), int(win * SR)
    n = max(1, (len(x) - w) // h + 1)
    idx = np.arange(w)[None, :] + h * np.arange(n)[:, None]
    e = np.sqrt(np.mean(x[idx] ** 2, axis=1) + 1e-12)
    return 20 * np.log10(e)
def threshold(db):
    return max(np.percentile(db, 10) + 10, np.percentile(db, 95) - 35)
def silences(db, thr, t0, t1, hop=0.01, min_len=0.06):
    """silence runs (start, end) in seconds inside [t0, t1]"""
    a, b = max(0, int(t0 / hop)), min(len(db), int(t1 / hop))
    out, s = [], None
    for i in range(a, b):
        q = db[i] < thr
        if q and s is None: s = i
        if not q and s is not None:
            if (i - s) * hop >= min_len: out.append((s * hop, i * hop))
            s = None
    if s is not None and (b - s) * hop >= min_len: out.append((s * hop, b * hop))
    return out
NARR, REC, V = sys.argv[1:4]
old = load(NARR)
def seg(t0, t1): return old[int(round(t0 * SR)):int(round(t1 * SR))].copy()
# room tone: the quietest 0.4 s inside a long pause of the old narration (kept as a loopable bed)
db = frames_db(old); thr = threshold(db)
# quietest 0.4 s window (10 ms steps) inside any pause of 0.5 s or longer
best = None
for a0, a1 in silences(db, thr, 0, len(old) / SR, min_len=0.5):
    for k in range(int(a0 / 0.01) + 3, int(a1 / 0.01) - 43):
        m = float(np.mean(db[k:k + 40]))
        if best is None or m < best[0]: best = (m, k * 0.01)
r0, r1 = best[1], best[1] + 0.4; tone = seg(r0, r1)
def room(d):
    n = int(d * SR); reps = int(np.ceil(n / len(tone))) + 1
    y = np.concatenate([tone] * reps)[:n].copy()
    return y
def lufs(x):
    p = f"{V}/_tmp.wav"
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-f", "f32le", "-ar", str(SR), "-ac", "1", "-i", "-", p], input=x.astype(np.float32).tobytes(), check=True)
    r = subprocess.run(["ffmpeg", "-hide_banner", "-i", p, "-af", "loudnorm=print_format=json", "-f", "null", "-"], capture_output=True, text=True)
    return float(json.loads(re.search(r"\{[^{}]*\"input_i\"[^{}]*\}", r.stderr).group(0))["input_i"])
def speech_only(p, pre=0.03, post=0.08):
    x = load(p); d = frames_db(x); t = threshold(d)
    on = np.where(d >= t)[0]
    a, b = max(0, on[0] * 0.01 - pre), min(len(x) / SR, on[-1] * 0.01 + 0.03 + post)
    return x[int(a * SR):int(b * SR)].copy(), (a, b)
log = {}
def matched(name, orig_t0, orig_t1):
    x, ab = speech_only(f"{REC}/{name}_pol.wav")
    g = lufs(seg(orig_t0, orig_t1)) - lufs(x)
    log[name] = {"trim": [round(ab[0], 3), round(ab[1], 3)], "gain_db": round(g, 2)}
    return x * (10 ** (g / 20))
pieces = [
    ("old 0-249.30 (through U162 + pause)", seg(0, 249.30), ("old", 0, 249.30)),
    ("room 0.13 (U163-U164 cut)", room(0.13), ("room", 0.13)),
    ("old 252.48-402.84 (U165..U255)", seg(252.48, 402.84), ("old", 252.48, 402.84)),
    ("old pause 402.84-403.15", seg(402.84, 403.15), ("old", 402.84, 403.15)),
    ("re1 (U256-U260)", matched("re1", 403.15, 410.59), ("new", "re1")),
    ("old pause 410.59-410.85", seg(410.59, 410.85), ("old", 410.59, 410.85)),
    ("old 410.85-424.45 (U261..U270 + half pause)", seg(410.85, 424.45), ("old", 410.85, 424.45)),
    ("room 0.45 (breath after U270)", room(0.45), ("room", 0.45)),
    ("old 424.45-455.61 (..U291)", seg(424.45, 455.61), ("old", 424.45, 455.61)),
    ("old pause 455.61-456.02", seg(455.61, 456.02), ("old", 455.61, 456.02)),
    ("re2 (U292-U297)", matched("re2", 456.02, 464.89), ("new", "re2")),
    ("room 0.45 (pause before U298)", room(0.45), ("room", 0.45)),
    ("old 464.97-476.86 (U298..U305)", seg(464.97, 476.86), ("old", 464.97, 476.86)),
    ("old pause 476.86-477.17", seg(476.86, 477.17), ("old", 476.86, 477.17)),
    ("re3 (U306-U311)", matched("re3", 477.17, 486.32), ("new", "re3")),
]
XF = int(0.01 * SR); fade = np.sin(np.linspace(0, np.pi / 2, XF)) ** 2
out = pieces[0][1]; marks = [(pieces[0][0], 0.0, pieces[0][2])]
for name, p, src in pieces[1:]:
    marks.append((name, len(out) / SR - 0.01, src))
    out = np.concatenate([out[:-XF], out[-XF:] * fade[::-1] + p[:XF] * fade, p[XF:]])
last_word_end = len(out) / SR - 0.08          # re3 speech_only keeps 80 ms after the last voiced frame
tail = room(0.6); tail *= np.linspace(1, 0, len(tail))
out = np.concatenate([out, tail, np.zeros(int((3.0 - 0.6 + 0.08) * SR), np.float32)])
raw = f"{V}/narration_v2_raw.wav"
subprocess.run(["ffmpeg", "-v", "error", "-y", "-f", "f32le", "-ar", str(SR), "-ac", "1", "-i", "-", "-c:a", "pcm_f32le", raw],
               input=out.astype(np.float32).tobytes(), check=True)
json.dump({"pieces": [[n, round(t, 3), src] for n, t, src in marks], "matched": log, "last_word_end": round(last_word_end, 3),
           "duration": round(len(out) / SR, 3), "room_tone_from": [round(r0, 2), round(r1, 2)], "room_tone_db": round(best[0], 1)},
          open(f"{V}/edit_log_v2.json", "w"), ensure_ascii=False, indent=1)
print(json.dumps(log), "last word end", round(last_word_end, 2), "duration", round(len(out) / SR, 2))
