# Polish the owner's narration recording (2026-10-22 request: clean it up, make breaths and gaps natural).
#   1) 75 Hz high-pass. FFT denoise (ffmpeg afftdn) only with --denoise: on 2026-10-22 the phone recording's
#      background was already about -50 dB (speech -11 dB) and afftdn changed nothing but added a 25 ms delay
#   2) breaths between phrases are turned down, not removed: loud ones to about noise floor + 10 dB (25 ms ramps)
#   3) long gaps are tightened by type, measured voiced-to-voiced: sentence end 0.65 s, comma 0.50 s, section 0.80 s.
#      Only the quietest part of a gap is cut (20 ms crossfades); a breath stays, right before the next phrase.
#   4) mouth clicks inside gaps only (spikes over 12x the level of the surrounding 20 ms) are turned down 20 dB for 4 ms.
#      ffmpeg adeclick was not used: on the whole file it also changed speech (65k samples, up to 0.68).
#   5) optional gentle de-esser, then the same loudness step as prep_audio.py (-14 LUFS, true peak -1.5 dB)
# Safety: the 80 ms around voiced speech is never touched. A "breath" right before a word starting with
# ㅎ/ㅅ/ㅆ/ㅊ/ㅋ/ㅌ/ㅍ is treated as that consonant (on 2026-10-22 the strongest "breath" was the ㅎ of 혹시).
# Gap types come from faster-whisper punctuation (word ending in . ? ! = sentence end); --section marks section breaks.
# usage: polish_voice.py IN(m4a/wav) OUT.wav [--section 20.6,...] [--denoise 12] [--deess 0.3] [--report r.json] [--words w.json]
#                        [--soft 0.4] [--breath-rel -22] [--tempo 1.3]
#   --tempo T: speed up first, pitch kept (Rubber Band R3 'finer' engine, `rubberband -3`; apt package rubberband-cli).
#             On 2026-10-22 R3 kept voicing clarity and consonants closer to the original than ffmpeg atempo.
#             --section and --words are given in the ORIGINAL file's time; they are divided by T.
#   --soft K: shorten a long gap only part of the way (target + K x the excess), so the speaker's own rhythm stays
#             (used for the ElevenLabs file on 2026-10-22: equal gaps everywhere sound machine-made)
#   --breath-rel D: judge breaths against the speech level instead of the noise floor (turn down only breaths
#             louder than speech p95 + D dB). Needed for AI/studio audio whose silence is digital (-61 dB floor)
#   If speech starts right at 0 s, 0.2 s of silence is put in front (a fade-in would eat the first consonant).
import json, os, re, subprocess, sys
import numpy as np

ROOT = os.environ.get("VIDEO_ROOT", os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
SR, HOP, WIN = 48000, 480, 1200                     # 10 ms frames
DIL, MIN_PAUSE = 8, 12                              # 80 ms around voiced frames, pauses >= 120 ms
TARGET_GAP = {"sentence": 0.65, "comma": 0.50, "section": 0.80}
PROTECT_INITIALS = {9, 10, 14, 15, 16, 17, 18}      # ㅅ ㅆ ㅊ ㅋ ㅌ ㅍ ㅎ (Hangul initial index)


def decode(path, af=None):
    cmd = ["ffmpeg", "-v", "error", "-i", path] + (["-af", af] if af else []) + ["-ac", "1", "-ar", str(SR), "-f", "f32le", "-"]
    return np.frombuffer(subprocess.run(cmd, capture_output=True, check=True).stdout, np.float32).astype(np.float64)


def frames_db(x):
    n = 1 + (len(x) - WIN) // HOP
    fr = np.lib.stride_tricks.as_strided(x, (n, WIN), (x.strides[0] * HOP, x.strides[0])) * np.hanning(WIN)
    return fr, 10 * np.log10((fr ** 2).mean(1) + 1e-12)


def runs(mask):
    out, i = [], 0
    while i < len(mask):
        if mask[i]:
            j = i
            while j < len(mask) and mask[j]:
                j += 1
            out.append([i, j]); i = j
        else:
            i += 1
    return out


def analyse(x):
    """Voiced frames (pitch 70-400 Hz), speech = voiced +-80 ms, pauses, breath candidates inside pauses."""
    fr, db = frames_db(x)
    floor = float(np.percentile(db, 10))
    y = fr[:, ::4]; y = y - y.mean(1, keepdims=True)
    ac = np.fft.irfft(np.abs(np.fft.rfft(y, 2 * y.shape[1])) ** 2)[:, :y.shape[1]]
    ac = ac / (ac[:, :1] + 1e-12)
    voiced = (ac[:, 30:171].max(1) > 0.45) & (db > floor + 15)
    sp = np.convolve(voiced.astype(int), np.ones(2 * DIL + 1), "same") > 0
    for a, b in runs(~sp):
        if b - a < MIN_PAUSE and a > 0 and b < len(sp):
            sp[a:b] = True
    pauses = []
    for a, b in runs(~sp):
        if b - a < MIN_PAUSE:
            continue
        cands = [[a + c, a + d, float(db[a + c:a + d].max() - floor)] for c, d in runs(db[a:b] > floor + 5) if d - c >= 10]
        pauses.append({"a": a, "b": b, "cands": cands})
    return db, floor, pauses


def initial_index(word):
    for ch in word:
        if "가" <= ch <= "힣":
            return (ord(ch) - 0xAC00) // 588
    return None


def transcribe(path):
    from faster_whisper import WhisperModel
    audio = decode(path)[::3].astype(np.float32)        # 16 kHz
    model = WhisperModel(f"{ROOT}/models/fw-large-v3", device="cpu", compute_type="int8")
    segs, _ = model.transcribe(audio, language="ko", beam_size=5, word_timestamps=True, vad_filter=False)
    return [{"w": w.word.strip(), "s": w.start, "e": w.end} for s in segs for w in s.words]


def main():
    a = sys.argv[1:]
    opt = lambda k, d=None: a[a.index(k) + 1] if k in a else d
    src, out = a[0], a[1]
    tempo = float(opt("--tempo", "1"))
    sections = [float(v) / tempo for v in opt("--section", "").split(",") if v]
    if tempo != 1:                                           # speed up first, then polish the faster audio
        wav_in, sped = out + ".in.wav", out + ".tempo.wav"
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", src, "-ac", "1", "-ar", str(SR), "-c:a", "pcm_f32le", wav_in], check=True)
        subprocess.run(["rubberband", "-q", "-3", f"-T{tempo}", wav_in, sped], check=True)
        os.remove(wav_in); src = sped
    deess = float(opt("--deess", "0"))
    soft = float(opt("--soft", "0"))
    breath_rel = opt("--breath-rel")
    x = decode(src, "highpass=f=75")
    db, floor, pauses = analyse(x)
    nr = float(opt("--denoise", "0"))
    if nr:                                                   # afftdn delays the signal by 1200 samples: undo it
        xd = decode(src, f"highpass=f=75,afftdn=nr={nr}:nf={max(-80, min(-20, round(floor)))}:rf=-60:tn=1")
        xd = np.concatenate([xd[1200:], np.zeros(1200)])
    else:
        xd = x
    words = ([{**w, "s": w["s"] / tempo, "e": w["e"] / tempo} for w in json.load(open(opt("--words")))]
             if opt("--words") else transcribe(src))
    n_fr = len(db)
    gain_db = np.zeros(len(x))
    speech_p95 = float(np.percentile(db, 95))
    keep_cuts, report = [], {"floor_db": round(floor, 1), "speech_p95_db": round(speech_p95, 1), "pauses": []}
    first, last = pauses[0], pauses[-1]
    lead_start = first["b"] if first["a"] == 0 else 0           # frame where the first speech region starts
    for p in pauses:
        A, B = p["a"] * 0.01, p["b"] * 0.01
        edge = p["a"] == 0 or p["b"] >= n_fr - 1
        # whisper word starts absorb the pause before them (혹시 was placed 0.5 s early), so find the word before
        # the pause by its end time and take the next word by order, not by time
        prv_i = min((i for i, w in enumerate(words) if w["e"] <= A + 0.3), key=lambda i: abs(words[i]["e"] - A), default=None)
        prv = words[prv_i] if prv_i is not None and abs(words[prv_i]["e"] - A) <= 0.6 else None
        nxt = words[0] if p["a"] == 0 else (words[prv_i + 1] if prv_i is not None and prv_i + 1 < len(words) else None)
        breaths, blocked = [], []                                # blocked: never cut (breaths, onsets, tails)
        for c, d, lv in p["cands"]:
            cs, ce = c * 0.01, d * 0.01
            if cs - A < 0.06 and p["a"] > 0:
                blocked.append((A, ce)); continue                # tail of the previous word
            if nxt and initial_index(nxt["w"]) in PROTECT_INITIALS and B - ce < 0.12:
                blocked.append((cs, B)); continue                # onset consonant, not a breath
            cs, ce = max(A + 0.06, cs - 0.07), min(B - 0.04, ce + 0.07)
            blocked.append((cs, ce))                             # a breath stays (natural), only loud ones go down
            att = float(np.clip((floor + lv) - (speech_p95 + float(breath_rel)) if breath_rel else lv - 10, 0, 12))
            if att >= 3:
                breaths.append([cs, ce, att])
                s0, s1, r = int(cs * SR), int(ce * SR), int(0.025 * SR)
                env = np.full(s1 - s0, -att)
                ramp = np.linspace(0, -att, min(r, (s1 - s0) // 2))
                env[:len(ramp)] = ramp; env[len(env) - len(ramp):] = ramp[::-1]
                gain_db[s0:s1] = np.minimum(gain_db[s0:s1], env)
        # mouth clicks: only between the protected tail/onset parts, never on speech
        clicks = []
        za = max([A + 0.03] + [v for u, v in blocked if u <= A + 0.001]) if p["a"] > 0 else A
        zb = min([B - 0.03] + [u for u, v in blocked if v >= B - 0.001])   # plosive bursts can start here
        i0, i1 = int(za * SR), int(zb * SR)
        if i1 - i0 > int(0.05 * SR):
            h = np.abs(np.diff(x[i0:i1], 2)); n = len(h)
            c2 = np.concatenate([[0.0], np.cumsum(h ** 2)])
            k = np.arange(n)
            o0, o1 = np.maximum(0, k - 960), np.minimum(n, k + 960)      # +-20 ms around ...
            c0_, c1_ = np.maximum(0, k - 96), np.minimum(n, k + 96)      # ... minus the middle +-2 ms
            ring = np.sqrt(np.maximum((c2[o1] - c2[o0]) - (c2[c1_] - c2[c0_]), 0) /
                           np.maximum((o1 - o0) - (c1_ - c0_), 1))
            hits = np.where((h > 12 * ring) & (h > 1e-4))[0]
            for kk in hits:                                              # a click sticks out of its surroundings
                t = (i0 + kk + 1) / SR
                if not clicks or t - clicks[-1] >= 0.004:
                    clicks.append(t)
            if len(clicks) > 6:                                          # many hits = not isolated clicks
                clicks = []
            for t in clicks:
                c0, c1, r = int((t - 0.002) * SR), int((t + 0.002) * SR), int(0.001 * SR)
                env = np.full(c1 - c0, -20.0); ramp = np.linspace(0, -20, r)
                env[:r] = ramp; env[-r:] = ramp[::-1]
                gain_db[c0:c1] = np.minimum(gain_db[c0:c1], env)
        entry = {"start": round(A, 2), "end": round(B, 2), "gap": round(B - A + 0.16, 2),
                 "clicks_turned_down": [round(float(t), 3) for t in clicks],
                 "breaths_turned_down": [[round(u, 2), round(v, 2), round(g, 1)] for u, v, g in breaths]}
        if not edge:
            kind = ("section" if any(abs(A - t) < 0.3 for t in sections) else
                    "sentence" if prv and re.search(r"[.?!]$", prv["w"]) else "comma")
            need = ((B - A + 0.16) - TARGET_GAP[kind]) * (1 - soft)
            entry["type"] = kind
            if need > 0.05:
                lo, hi = A + 0.10, B - 0.06
                blocked = [(u - 0.05, v + 0.05) for u, v in blocked]
                free, cur = [], lo                               # allowed intervals between protected parts
                for u, v in sorted(blocked):
                    if u > cur: free.append((cur, min(u, hi)))
                    cur = max(cur, v)
                if cur < hi: free.append((cur, hi))
                best = None
                for u, v in free:
                    L = min(need, v - u)
                    if L < 0.08: continue
                    for s in np.arange(u, v - L + 1e-9, 0.01):
                        e = float(np.mean(db[int(s * 100):max(int(s * 100) + 1, int((s + L) * 100))]))
                        if best is None or (L, -e) > (best[1] - best[0], -best[2]):
                            best = (s, s + L, e)
                if best:
                    keep_cuts.append((float(best[0]), float(best[1])))
                    entry["cut"] = [round(float(best[0]), 2), round(float(best[1]), 2)]
                    entry["gap_after"] = round(entry["gap"] - float(best[1] - best[0]), 2)
        report["pauses"].append(entry)
    # timeline: lead-in 0.25 s before the first speech, tail 0.35 s after the last
    t_start = max(0.0, lead_start * 0.01 + 0.08 - 0.25)
    t_end = min(len(x) / SR, (last["a"] * 0.01 - 0.08 + 0.35) if last["b"] >= n_fr - 1 else len(x) / SR)
    y = xd[:len(gain_db)] * 10 ** (gain_db[:len(xd)] / 20)
    pieces, cur = [], t_start
    for s, e in sorted(keep_cuts):
        pieces.append((cur, s)); cur = e
    pieces.append((cur, t_end))
    xf = int(0.02 * SR); fade = np.sin(np.linspace(0, np.pi / 2, xf)) ** 2
    outbuf = y[int(pieces[0][0] * SR):int(pieces[0][1] * SR)].copy()
    for s, e in pieces[1:]:
        seg = y[int(s * SR) - xf // 2:int(e * SR)].copy()
        tail = outbuf[-xf:] * fade[::-1] + seg[:xf] * fade       # equal-power crossfade inside silence
        outbuf = np.concatenate([outbuf[:-xf], tail, seg[xf:]])
    fi, fo = int(0.03 * SR), int(0.06 * SR)
    pad = 0.0
    if first["a"] != 0 or first["b"] * 0.01 < 0.15:              # speech starts at once: put silence in front
        pad = 0.2
        outbuf = np.concatenate([np.zeros(int(pad * SR)), outbuf])
    outbuf[:fi] *= np.linspace(0, 1, fi); outbuf[-fo:] *= np.linspace(1, 0, fo)
    tmp = out + ".tmp.wav"
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-f", "f32le", "-ar", str(SR), "-ac", "1", "-i", "-"]
                   + (["-af", f"deesser=i={deess}"] if deess else []) + ["-c:a", "pcm_f32le", tmp],
                   input=outbuf.astype(np.float32).tobytes(), check=True)
    subprocess.run([sys.executable, os.path.join(os.path.dirname(os.path.abspath(__file__)), "prep_audio.py"), tmp, out], check=True)
    os.remove(tmp)
    if tempo != 1:
        os.remove(src)
    report.update({"tempo": tempo, "in_sec": round(len(x) * tempo / SR, 2), "out_sec": round(len(outbuf) / SR, 2),
                   "lead_in_trim": round(t_start, 2), "lead_in_pad": pad, "cuts": [[round(s, 2), round(e, 2)] for s, e in sorted(keep_cuts)]})
    if opt("--report"):
        json.dump(report, open(opt("--report"), "w"), ensure_ascii=False, indent=1)
    for p in report["pauses"]:
        print(p)
    print(f"{src} {report['in_sec']}s -> {out} {report['out_sec']}s")


if __name__ == "__main__":
    main()
