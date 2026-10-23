# Put every subtitle unit's start on the real voice onset (2026-10-23 user feedback: subtitles, cuts and centre text
# changed before the next voice started). Replaces refine.py, whose quiet threshold (speech level - 35 dB) sat below
# this microphone's noise floor and whose "longest gap" rule stopped at a breath inside the pause.
# Method: frames above (speech level - 22 dB) count as voice; breaths and room noise stay below. Between 0.3 s before
# the recognised start and the end of the first recognised word, the longest stretch without voice (60 ms or more) is
# the pause; the onset is the first voice frame after it. A walk back from the first word (first try) stopped at the
# closure of a stop consonant inside the word (가볍게: 0.28 s late), so the longest stretch is used instead.
# Continuous speech with no such stretch keeps the recognised start.
# usage: onsets.py audio align.json out.json      (align.json from align.py: start, end, first_word_end)
import json, subprocess, sys
import numpy as np

audio, inp, outp = sys.argv[1:4]
SR, HOP = 16000, 0.01
x = np.frombuffer(subprocess.run(["ffmpeg", "-v", "error", "-i", audio, "-ac", "1", "-ar", str(SR), "-f", "s16le", "-"],
                                 capture_output=True, check=True).stdout, np.int16).astype(np.float32) / 32768
w = int(0.02 * SR)
rms = np.sqrt(np.convolve(x ** 2, np.ones(w) / w, mode="same")[::int(HOP * SR)] + 1e-12)
db = 20 * np.log10(rms)
level = np.percentile(db, 95)
voice = db > level - 22
# a pause can hold tiny blips (a click, a breath peak); voice shorter than 40 ms between quiet frames is not speech
i = 0
while i < len(voice):
    if voice[i]:
        j = i
        while j < len(voice) and voice[j]:
            j += 1
        if j - i < 4 and i > 0 and j < len(voice):
            voice[i:j] = False
        i = j
    else:
        i += 1
MIN_GAP = 6                     # frames: 60 ms without voice can be a pause; the longest one wins


def fr(t):
    return min(max(int(round(t / HOP)), 0), len(voice) - 1)


units = json.load(open(inp))
out = []
for k, u in enumerate(units):
    asr = u.get("start_asr", u["start"])
    fwe = u.get("first_word_end") or asr + 0.5
    if k == 0:
        out.append(dict(u, start_asr=asr, start=round(np.argmax(voice) * HOP, 3), onset="first voice")); continue
    prev = out[-1]
    e = fr(fwe - 0.03)
    while e < fr(fwe + 0.6) and not voice[e]:       # recognised word end can fall before the voice: move to it
        e += 1
    a = fr(max(asr - 0.3, prev["start"] + 0.15))
    runs, r0 = [], None                               # stretches without voice inside [asr - 0.3, first word end]
    for i in range(a, e + 1):
        if not voice[i] and r0 is None:
            r0 = i
        if voice[i] and r0 is not None:
            if i - r0 >= MIN_GAP:
                runs.append((r0, i))
            r0 = None
    # a short dip well before the recognised start is a closure inside the previous word, not the pause
    runs = [r for r in runs if r[1] * HOP >= asr - 0.08 or (r[1] - r[0]) * HOP >= 0.12]
    r = max(runs, key=lambda r: r[1] - r[0]) if runs else None     # the pause is the longest stretch
    punct = units[k - 1]["text"].rstrip().endswith(tuple(",.?!'\"…”’"))
    # a dip under 120 ms in mid-phrase is usually a stop closure or a glottal catch, not a pause (바로 | 이 때문에)
    if r and ((r[1] - r[0]) * HOP >= 0.12 or punct):
        onset, how = r[1] * HOP, "after pause"
    else:
        onset, how = asr, "kept"
    onset = max(onset, prev["start"] + 0.15)
    out.append(dict(u, start_asr=asr, start=round(onset, 3), onset=how))
# Pass 2: units that start inside continuous speech (no pause found). Recognised word times are unreliable there
# (바로 이 때문에 | 번아웃을: 0.5 s early). Between two reliable pause onsets, the voiced stretch is shared out by
# syllable count, and each estimate snaps to the deepest nearby energy dip (word-initial stop closures are silent:
# 번아웃을 | 개인의) within 0.3 s; the start is where the energy rises again after that dip.
import re
H5 = 80                                                    # 5 ms hop at 16 kHz
e5 = np.array([np.sqrt(np.mean(x[i:i + 480] ** 2) + 1e-12) for i in range(0, len(x) - 480, H5)])
d5 = np.convolve(20 * np.log10(e5), np.ones(5) / 5, mode="same")
syl = lambda t: max(1, len(re.findall(r"[가-힣A-Za-z0-9]", t)))


def snap(est):
    """Deepest nearby dip: score = dip level (dB) + 30 dB per second away from the estimate, within 0.3 s."""
    a0, a1 = int((est - 0.3) / 0.005), int((est + 0.3) / 0.005)
    best, bs = None, None
    for i in range(max(a0, 16), min(a1, len(d5) - 16)):
        if d5[i] == d5[i - 6:i + 7].min():
            depth = min(d5[i - 16:i].max(), d5[i + 1:i + 17].max()) - d5[i]
            sc = d5[i] + 30 * abs(i * 0.005 - est)
            if depth >= 10 and (bs is None or sc < bs):
                best, bs = i, sc
    if best is None:
        return None
    j = best
    while j < len(d5) - 1 and d5[j] < d5[best] + 6:        # release: energy back up 6 dB
        j += 1
    return j * 0.005


anchors = [k for k, u in enumerate(out) if u["onset"] != "kept"] + [len(out)]
for ai in range(len(anchors) - 1):
    a, b = anchors[ai], anchors[ai + 1]
    if b - a < 2:
        continue
    t0 = out[a]["start"]
    if b < len(out):                                       # voiced stretch ends before the pause that leads into b
        i = fr(out[b]["start"]) - 1
        while i > fr(t0) and not voice[i]:
            i -= 1
        t1 = i * HOP + 0.02
    else:
        t1 = out[b - 1].get("end", t0 + 1.0)
    counts = [syl(units[k]["text"]) for k in range(a, b)]
    tot = sum(counts)
    acc = 0
    for k in range(a + 1, b):
        acc += counts[k - a - 1]
        est = t0 + (t1 - t0) * acc / tot
        sn = snap(est)
        on = sn if sn is not None else est
        on = max(on, out[k - 1]["start"] + 0.15)
        out[k]["start_kept"] = out[k]["start"]
        out[k]["start"] = round(on, 3)
        out[k]["onset"] = "syllables+dip" if sn is not None else "syllables"
json.dump(out, open(outp, "w"), ensure_ascii=False, indent=1)
d = np.array([u["start"] - u["start_asr"] for u in out[1:]])
print(f"voice level {level:.1f} dB, voice above {level - 22:.1f} dB | onset - recognised start: "
      f"median {np.median(d):+.2f}s, later than recognised in {np.sum(d > 0.05)} of {len(d)} units, "
      f"earlier in {np.sum(d < -0.05)}; inside continuous speech: {sum(u['onset'].startswith('syllables') for u in out)} "
      f"({sum(u['onset'] == 'syllables+dip' for u in out)} snapped to a dip)")
