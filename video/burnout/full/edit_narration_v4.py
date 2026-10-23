# v4 narration edit (2026-10-23 owner feedback on v3: the end of the new line was cut off; U156-U162 re-recorded because
# the sentence ends sounded strange; "don't let the recording get cut or get quieter towards the end").
# Causes found and fixed: polish_voice.py cut the dying last syllable of re1, re2 and re4 and treated soft 다/죠 endings
# and missed word starts as breaths (turned down up to 12 dB, 56 places in the first take); loudnorm ran in its
# gain-riding dynamic mode; the old rule here (last frame over the speech threshold + 0.11 s) cut re4 again.
# Now: the first take and re1-re4 are polished again with their old gap cuts (same timing; one cut that ate 0.15 s of
# "...거죠." is left out) and no breath or click edits (--keep-levels), re5 the same without any cut; every recording is
# used to the end of its polished file; all gains are constant (prep_audio.py, mix_audio.py).
# Pieces: re4 for U012-U013 (new line), re5 for U156-U162, cut U163-U164, re1-re3 for U256-U260 / U292-U297 / U306-U311,
# a breathing pause after U270, end about 3 s after the last word. Cuts sit inside pauses; joints get 10 ms equal-power
# fades. Pauses are filled with the quietest 0.4 s of the first take.
# Record of exactly what was done; it needs the owner's recordings, which are not in the repository.
# usage: edit_narration_v4.py <polished first take> <folder with re1_pol.wav .. re5_pol.wav> <out folder>
#   Then: scripts/prep_audio.py <out>/narration_v4_raw.wav <out>/narration_v4.wav
# Writes <out>/narration_v4_raw.wav and <out>/edit_log_v4.json (piece list: where each stretch of the new file comes from).
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
# room tone: the 0.2 s stretch of the first take whose loudest 10 ms frame is the quietest (after the silent lead-in);
# longer fills loop it with 20 ms crossfades. v4: no 0.4 s stretch of this tightly paced take is free of tails and
# breaths, and the old pick (quietest mean) put an 80 ms, -33 dB bit of a tail into every fill
db = frames_db(old)
m, k0 = min((float(np.max(db[k:k + 20])), k) for k in range(30, len(db) - 20))
r0, r1 = k0 * 0.01, k0 * 0.01 + 0.2; tone = seg(r0, r1); best = (m, r0)
def room(d):
    n = int(round(d * SR)); xf = int(0.02 * SR); f = np.sin(np.linspace(0, np.pi / 2, xf)) ** 2
    y = tone.copy()
    while len(y) < n:
        y = np.concatenate([y[:-xf], y[-xf:] * f[::-1] + tone[:xf] * f, tone[xf:]])
    return y[:n].copy()
def lufs(x):
    p = f"{V}/_tmp.wav"
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-f", "f32le", "-ar", str(SR), "-ac", "1", "-i", "-", p], input=x.astype(np.float32).tobytes(), check=True)
    r = subprocess.run(["ffmpeg", "-hide_banner", "-i", p, "-af", "loudnorm=print_format=json", "-f", "null", "-"], capture_output=True, text=True)
    return float(json.loads(re.search(r"\{[^{}]*\"input_i\"[^{}]*\}", r.stderr).group(0))["input_i"])
def speech_only(p, pre=0.03):
    # from 30 ms before the first frame over the speech threshold to the end of the polished file (v4: the old end,
    # last such frame + 0.11 s, cut soft endings); also returns where the last frame over the threshold ends
    x = load(p); d = frames_db(x); t = threshold(d)
    on = np.where(d >= t)[0]
    a, b = max(0, on[0] * 0.01 - pre), len(x) / SR
    return x[int(a * SR):].copy(), (a, b), on[-1] * 0.01 + 0.03 - a
log = {}
# loudness of a re-recording is matched to the stretch it replaces, measured on its speech only (to the v3 trim end for
# re1-re4, to the last word + 0.08 s for re5), so the kept ending does not change the level of the speech
SPEECH_END = {"re1": 8.12, "re2": 9.68, "re3": 10.51, "re4": 4.70, "re5": 13.00}
def matched(name, orig_t0, orig_t1):
    x, ab, last_voiced = speech_only(f"{REC}/{name}_pol.wav")
    g = lufs(seg(orig_t0, orig_t1)) - lufs(x[:int(round((SPEECH_END[name] - ab[0]) * SR))])
    log[name] = {"trim": [round(ab[0], 3), round(ab[1], 3)], "gain_db": round(g, 2), "last_voiced": round(last_voiced, 3)}
    return x * (10 ** (g / 20))
# the first take keeps its old timing except after the left-out cut: from 445.43 s on it runs 0.2076 s later
T = lambda t: round(t + 0.2076 if t > 445.43 else t, 4)
def take(t0, t1, what):
    return (f"old {T(t0):.2f}-{T(t1):.2f} ({what})", seg(T(t0), T(t1)), ("old", T(t0), T(t1)))
pieces = [
    take(0, 15.33, "through U011 + pause"),
    ("re4 (U012-U013, new line)", matched("re4", 15.36, 18.10), ("new", "re4")),
    # each re-recording keeps 0.1 s after its ending dies away, so the old pause after it starts 0.1 s later than in v3
    take(18.30, 237.84, "rest of pause, U014..U155"),
    ("re5 (U156-U162, re-recorded by the owner)", matched("re5", 237.84, 249.30), ("new", "re5")),
    ("room 0.08 (U163-U164 cut; about 0.3 s quiet before U165)", room(0.08), ("room", 0.08)),
    take(252.48, 402.84, "U165..U255"),
    take(402.84, 403.15, "pause"),
    ("re1 (U256-U260)", matched("re1", 403.15, 410.59), ("new", "re1")),
    take(410.69, 410.85, "pause"),
    take(410.85, 424.45, "U261..U270 + half pause"),
    ("room 0.45 (breath after U270)", room(0.45), ("room", 0.45)),
    take(424.45, 455.61, "..U291"),
    take(455.61, 456.02, "pause"),
    ("re2 (U292-U297)", matched("re2", T(456.02), T(464.89)), ("new", "re2")),
    ("room 0.35 (pause before U298)", room(0.35), ("room", 0.35)),
    take(464.97, 476.86, "U298..U305"),
    take(476.86, 477.17, "pause"),
    ("re3 (U306-U311)", matched("re3", T(477.17), T(486.32)), ("new", "re3")),
]
XF = int(0.01 * SR); fade = np.sin(np.linspace(0, np.pi / 2, XF)) ** 2
out = pieces[0][1]; marks = [(pieces[0][0], 0.0, pieces[0][2])]
for name, p, src in pieces[1:]:
    marks.append((name, len(out) / SR - 0.01, src))
    out = np.concatenate([out[:-XF], out[-XF:] * fade[::-1] + p[:XF] * fade, p[XF:]])
# end: as v2/v3, 3.16 s after the end of the last frame over the speech threshold in re3 (the last word)
last_word_end = next(t for n, t, src in marks if src == ("new", "re3")) + log["re3"]["last_voiced"]   # piece starts at its mark
pad = last_word_end + 3.16 - len(out) / SR
tail = room(0.6); tail *= np.linspace(1, 0, len(tail))
out = np.concatenate([out, tail, np.zeros(int(round((pad - 0.6) * SR)), np.float32)])
raw = f"{V}/narration_v4_raw.wav"
subprocess.run(["ffmpeg", "-v", "error", "-y", "-f", "f32le", "-ar", str(SR), "-ac", "1", "-i", "-", "-c:a", "pcm_f32le", raw],
               input=out.astype(np.float32).tobytes(), check=True)
json.dump({"pieces": [[n, round(t, 3), src] for n, t, src in marks], "matched": log, "last_word_end": round(last_word_end, 3),
           "duration": round(len(out) / SR, 3), "room_tone_from": [round(r0, 2), round(r1, 2)], "room_tone_db": round(best[0], 1)},
          open(f"{V}/edit_log_v4.json", "w"), ensure_ascii=False, indent=1)
print(json.dumps(log), "last word end", round(last_word_end, 2), "duration", round(len(out) / SR, 2))
