# v5 narration edit (2026-10-23 owner feedback): U233-U235 re-recorded with the new age (작년 십이월, 한 언론 기사에
# 서른한 살 직장인 박 모 씨의 이야기가 실렸습니다; re6) and U238-U241 re-recorded with new wording (출근하면 일할 의욕이
# 없고, 퇴근해서 취미를 하나 만들어보려고 해도 너무 피곤해서 잠만 자는 날이 계속 이어졌다고 합니다; re7), with the
# request that the end of each new line is not cut off and does not suddenly get quieter.
# How: both recordings are polished like re5 (polish_voice.py --keep-levels, no cuts) and used whole, from 30 ms before
# the voice to the end of the polished file, with one constant gain matched on their speech to the stretch they replace
# (integrated loudness, ffmpeg ebur128).
# The recording app ends each file with its own fade below the room noise (the last 60-90 ms, after the voice has died
# away to the noise); a new line is used up to where that fade starts and joins the take's room tone with a 20 ms
# equal-power fade, so the background never drops out (an overlap of the fade itself left a 50 ms dip to -69 dB). The silences around the
# new lines keep the take's own lengths (0.175 s before re6, 0.195 s after it, 0.170 s before re7); after re7 0.19 s
# instead of the take's 0.11 s before 그리고. Everything else is v4 (edit_narration_v4.py): same pieces, same room tone.
# Record of exactly what was done; it needs the owner's recordings, which are not in the repository.
# usage: edit_narration_v5.py <polished first take> <folder with re1_pol.wav .. re7_pol.wav, re6/re7_polish.json> <out>
#   Then: scripts/prep_audio.py <out>/narration_v5_raw.wav <out>/narration_v5.wav
# Writes <out>/narration_v5_raw.wav and <out>/edit_log_v5.json (piece list: where each stretch of the new file comes from).
import json, re, subprocess, sys
import numpy as np

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
NARR, REC, V = sys.argv[1:4]
old = load(NARR)
def seg(t0, t1): return old[int(round(t0 * SR)):int(round(t1 * SR))].copy()
# room tone as v4: the 0.2 s stretch of the first take whose loudest 10 ms frame is the quietest, looped with 20 ms
# crossfades for longer fills
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
def lufs_eb(x):
    # ffmpeg ebur128 (BS.1770 integrated). v5: loudnorm's input_i read up to 0.8 dB low on these 5-7 s clips, so the
    # two new lines are matched with ebur128; re1-re5 keep their v4 gains (within 0.55 dB of an ebur128 match)
    p = f"{V}/_tmp.wav"
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-f", "f32le", "-ar", str(SR), "-ac", "1", "-i", "-", p], input=x.astype(np.float32).tobytes(), check=True)
    r = subprocess.run(["ffmpeg", "-hide_banner", "-nostats", "-i", p, "-af", "ebur128", "-f", "null", "-"], capture_output=True, text=True)
    return float(re.findall(r"I:\s+(-?[\d.]+) LUFS", r.stderr)[-1])
def speech_only(p, pre=0.03):
    # v4 rule for re1-re5: from 30 ms before the first frame over the speech threshold to the end of the polished file
    x = load(p); d = frames_db(x); t = threshold(d)
    on = np.where(d >= t)[0]
    a, b = max(0, on[0] * 0.01 - pre), len(x) / SR
    return x[int(a * SR):].copy(), (a, b), on[-1] * 0.01 + 0.03 - a
log = {}
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

# --- v5: the two new lines ---------------------------------------------------------------------------------------
def fine_db(x, hop=0.005, win=0.01):
    h, w = int(hop * SR), int(win * SR); n = max(1, (len(x) - w) // h + 1)
    idx = np.arange(w)[None, :] + h * np.arange(n)[:, None]
    return 20 * np.log10(np.sqrt(np.mean(x[idx] ** 2, axis=1)) + 1e-12)
def quiet_run(guess, thr=-46.0):
    """the silence of the take (10 ms level under thr) around guess: (end of the voice before, start of the voice after)"""
    t0 = guess - 0.4; d = fine_db(seg(t0, guess + 0.4)); k = int(0.4 / 0.005)
    assert d[k] < thr, f"no silence at {guess}"
    a = k
    while a > 0 and d[a - 1] < thr: a -= 1
    b = k
    while b < len(d) - 1 and d[b + 1] < thr: b += 1
    return round(t0 + a * 0.005, 3), round(t0 + (b + 1) * 0.005 + 0.005, 3)
LEAD = 0.03                    # a new line starts 30 ms before its voice
XF_END = 0.02                  # joint from the end of a new line (where the app's fade starts) to the take's room tone
def new_line(name, orig_t0, orig_t1):
    x = load(f"{REC}/{name}_pol.wav"); floor = json.load(open(f"{REC}/{name}_polish.json"))["floor_db"]
    d = fine_db(x)
    on = int(np.argmax(d >= floor + 6)) * 0.005                     # first 10 ms over the room noise + 6 dB
    vend = (len(d) - 1 - int(np.argmax(d[::-1] >= floor + 3))) * 0.005 + 0.01   # last 10 ms over noise + 3 dB
    fade = (len(d) - 1 - int(np.argmax(d[::-1] >= floor - 2))) * 0.005 + 0.01   # after this only the app's fade is left
    a = max(0.0, on - LEAD); y = x[int(round(a * SR)):int(round(fade * SR))].copy()
    g = lufs_eb(seg(orig_t0, orig_t1)) - lufs_eb(x[int(round(on * SR)):int(round(vend * SR))])
    info = {"from": round(a, 3), "voice": [round(on, 3), round(vend, 3)], "to": round(fade, 3),
            "file_end": round(len(x) / SR, 3), "floor_db": floor, "gain_db": round(g, 2), "after_voice": round(fade - vend, 3)}
    log[name] = info
    return y * (10 ** (g / 20)), info
# silences of the take (take time = v4 time - 0.265 in this stretch; guesses from the v4 level plot)
e1, o1 = quiet_run(366.74)     # 들려드릴게요. | 작년 십이월 (old U233)
e2, o2 = quiet_run(371.45)     # 실렸습니다. (old U235) | 그는 처음엔
e3, o3 = quiet_run(374.63)     # 몰랐다고 해요. | 폭식을 (old U238)
e4, o4 = quiet_run(380.985)    # 이어졌다고 합니다. (old U241) | 그리고 기사에서
re6, i6 = new_line("re6", o1, e2)
re7, i7 = new_line("re7", o3, e4)
joints = {}
def after_new(info, e_old, o_next, target, key):
    """take start after a new line so that the silence after its voice is `target`; room tone if the old line's
    ending would come back in (the take is used from 30 ms after the old voice ends at the earliest)"""
    tail = info["after_voice"] - XF_END                              # silence the new file itself brings
    b = o_next - (target - tail)
    fill = 0.0
    if b < e_old + 0.03:
        fill = (e_old + 0.03) - b + 0.01; b = e_old + 0.03                # + the 10 ms joint after the fill
    joints[key] = {"silence": round(target, 3), "take_from": round(b, 3), "room_fill": round(fill, 3)}
    return round(b, 3), fill
b1, f1 = after_new(i6, e2, o2, o2 - e2, "after re6")
b2, f2 = after_new(i7, e4, o4, 0.19, "after re7")
a1, a2 = round(o1 - 0.02, 3), round(o3 - 0.02, 3)                   # silence before = the take's own (10 ms joint)
joints["before re6"] = {"silence": round(a1 - e1 + LEAD - 0.01, 3), "take_to": a1}
joints["before re7"] = {"silence": round(a2 - e3 + LEAD - 0.01, 3), "take_to": a2}

pieces = [
    take(0, 15.33, "through U011 + pause"),
    ("re4 (U012-U013, new line)", matched("re4", 15.36, 18.10), ("new", "re4")),
    take(18.30, 237.84, "rest of pause, U014..U155"),
    ("re5 (U156-U162, re-recorded by the owner)", matched("re5", 237.84, 249.30), ("new", "re5")),
    ("room 0.08 (U163-U164 cut; about 0.3 s quiet before U165)", room(0.08), ("room", 0.08)),
    take(252.48, a1, "U165..U232b + pause"),
    ("re6 (U233-U235, 서른한 살, re-recorded by the owner)", re6, ("new", "re6")),
] + ([(f"room {f1:.2f} (pause after re6)", room(f1), ("room", round(f1, 3)))] if f1 > 0.005 else []) + [
    take(b1, a2, "pause + U236..U237 + pause"),
    ("re7 (U238-U241b, new wording, re-recorded by the owner)", re7, ("new", "re7")),
] + ([(f"room {f2:.2f} (pause after re7)", room(f2), ("room", round(f2, 3)))] if f2 > 0.005 else []) + [
    take(b2, 402.84, "pause + U242..U255"),
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
XF = int(0.01 * SR)
def fade(n): return np.sin(np.linspace(0, np.pi / 2, n)) ** 2
out = pieces[0][1]; marks = [(pieces[0][0], 0.0, pieces[0][2])]; prev = pieces[0][2]
for name, p, src in pieces[1:]:
    n = int(round(XF_END * SR)) if prev in (("new", "re6"), ("new", "re7")) else XF   # 20 ms after a new line
    f = fade(n)
    marks.append((name, len(out) / SR - n / SR, src))
    out = np.concatenate([out[:-n], out[-n:] * f[::-1] + p[:n] * f, p[n:]])
    prev = src
# end: as v2-v4, 3.16 s after the end of the last frame over the speech threshold in re3 (the last word)
last_word_end = next(t for n, t, src in marks if src == ("new", "re3")) + log["re3"]["last_voiced"]
pad = last_word_end + 3.16 - len(out) / SR
tail = room(0.6); tail *= np.linspace(1, 0, len(tail))
out = np.concatenate([out, tail, np.zeros(int(round((pad - 0.6) * SR)), np.float32)])
raw = f"{V}/narration_v5_raw.wav"
subprocess.run(["ffmpeg", "-v", "error", "-y", "-f", "f32le", "-ar", str(SR), "-ac", "1", "-i", "-", "-c:a", "pcm_f32le", raw],
               input=out.astype(np.float32).tobytes(), check=True)
json.dump({"pieces": [[n, round(t, 3), src] for n, t, src in marks], "matched": log, "joints": joints,
           "take_silences": {"before re6": [e1, o1], "after re6": [e2, o2], "before re7": [e3, o3], "after re7": [e4, o4]},
           "last_word_end": round(last_word_end, 3), "duration": round(len(out) / SR, 3),
           "room_tone_from": [round(r0, 2), round(r1, 2)], "room_tone_db": round(best[0], 1)},
          open(f"{V}/edit_log_v5.json", "w"), ensure_ascii=False, indent=1)
print(json.dumps({k: log[k] for k in ("re6", "re7")}, ensure_ascii=False))
print(json.dumps(joints, ensure_ascii=False))
print("last word end", round(last_word_end, 2), "duration", round(len(out) / SR, 2))
