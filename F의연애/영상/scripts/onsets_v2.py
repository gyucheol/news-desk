# Subtitle starts on the first audible sound of each line's first shown syllable (F의 연애 01 v2, 2026-10-24).
# Owner feedback on v1: "녹음본 목소리가 나오기 전에 자막이 나오거나, 녹음본이 나오고 좀 있다가 자막이 나오는 경우가 좀
# 많아보여. 녹음본의 목소리가 해당 자막을 읽을 때 자막이 같이 딱 나올 수 있게". Checked on spectrograms: v1 took an
# energy onset after a pause when it found one, and that pause was sometimes inside the previous line (the subtitle
# came 0.3 s early, during "라고" of "불안해라고") or the onset was found 0.5 s late after a pause inside the line.
# Here the anchor is always the CTC frame of the line's first shown syllable (ctc_align.py "syl"; hidden leading words
# such as "(하며)" are skipped), which was consistent with the sound in every case looked at, and the sound only
# fine-tunes it, never back across the previous syllable and never more than 10 ms after the anchor:
#   - a pause (band energy under speech level - 30 dB for >= 40 ms) that ends between the previous syllable and the
#     anchor: the start is where the sound comes back (the first consonant). How far before the anchor depends on the
#     first consonant (measured here: a vowel starts within 0.05 s of its anchor, ㄴ ㅁ ㄹ and stops within 0.085 s):
#     vowel 0.06 s, ㄴ ㅁ ㄹ and ㄱ ㄷ ㅂ ㄲ ㄸ ㅃ 0.10 s, ㅎ 0.12 s, noisy consonants 0.15 s. Farther back it is a breath
#     (이미, 이런, 알림: 0.12-0.15 s of breath noise between the pause and the voice);
#   - a first syllable starting with a noisy consonant (ㅅ ㅆ ㅈ ㅉ ㅊ ㅋ ㅌ ㅍ): CTC marks the vowel, 50-120 ms after
#     the hiss or the burst is heard (슬슬, 심리학, 스스로, 생각해, 사람들), so the start goes back to where the noise
#     above 3 kHz begins (unvoiced: louder than the voicing band, within 15 dB of its own peak), at most 0.30 s;
#   - else the energy valley of the consonant just before the anchor (>= 6 dB deep on both sides, within 0.10 s):
#     the start is where the energy rises again (the release of ㅈ ㅊ ㅌ ㅍ; for ㅅ the hiss is earlier and wins);
#   - else the anchor minus the CTC lead measured on clean pause onsets in this recording.
# The previous syllable: the last syllable of the previous line, but CTC puts a line's last syllable late, inside
# the following pause, when that line ends an alignment chunk (니 665.86, 다 666.28, next line 666.37), so it is
# taken as at most 0.30 s after the syllable before it. A sound that starts more than 0.15 s before the anchor after a
# pause (a breath, a lip noise) is not the start, except the hiss of a noisy consonant.
# usage: onsets_v2.py audio.wav align_ctc.json lines.json out.json
import json, re, subprocess, sys
import numpy as np
import scipy.signal as ss

audio, ctcp, linesp, outp = sys.argv[1:5]
SR = 48000
x = np.frombuffer(subprocess.run(["ffmpeg", "-v", "error", "-i", audio, "-ac", "1", "-ar", str(SR), "-f", "f32le", "-"],
                                 capture_output=True, check=True).stdout, np.float32).astype(np.float64)
HOP = 0.002
h = int(HOP * SR)


def env(lo, hi, win):
    b = ss.sosfiltfilt(ss.butter(4, [lo, hi], "bandpass", fs=SR, output="sos"), x)
    w = int(win * SR)
    return 20 * np.log10(np.sqrt(np.convolve(b ** 2, np.ones(w) / w, mode="same")[::h] + 1e-14))


E = env(150, 7000, 0.006)                      # speech band
H = env(3000, 10000, 0.008)                    # hiss of ㅅ, ㅈ, aspiration
Lv = env(80, 900, 0.008)                       # voicing
units = json.load(open(ctcp)); lines = {o["id"]: o for o in json.load(open(linesp))}
fr = lambda t: min(max(int(round(t / HOP)), 0), len(E) - 1)
tt = lambda i: i * HOP
INI = "ㄱㄲㄴㄷㄸㄹㅁㅂㅃㅅㅆㅇㅈㅉㅊㅋㅌㅍㅎ"
NOISY = set("ㅅㅆㅈㅉㅊㅋㅌㅍ")
WIN = lambda c: 0.15 if c in NOISY else 0.06 if c == "ㅇ" else 0.12 if c == "ㅎ" else 0.10


def level_at(t):
    return np.percentile(E[fr(t - 1.0):fr(t + 1.0)], 90)


def quiet_end(t0, t1, lev):
    """End of the last quiet stretch (>= 40 ms in full, under lev - 30 dB) that ends inside (t0, t1]; None if none."""
    a, b = fr(t0), fr(t1)
    q = E < lev - 30
    end = None
    for j in range(a + 1, b + 1):              # j: first loud frame after a quiet run
        if q[j - 1] and not q[j]:
            i = j - 1
            while i > 0 and q[i - 1]:
                i -= 1
            if (j - i) * HOP >= 0.04:
                end = j
    return end


def hiss_start(A, lo):
    """Where the unvoiced noise of a noisy first consonant begins, walking back from 10 ms before the anchor."""
    a = fr(A) - 5
    stop = fr(max(lo, A - 0.30))
    pk = H[stop:fr(A) + 1].max()
    k = a
    while k > stop and H[k] > pk - 15 and H[k] > Lv[k] - 3:
        k -= 1
    return tt(k + 1) if (a - k) * HOP >= 0.015 else None


def prev_syllable(k):
    """The previous line's last syllable time, capped at 0.30 s after the syllable before it (see above)."""
    s = units[k - 1].get("syl") or []
    if not s:
        return None
    return min(s[-1][1], s[-2][1] + 0.30) if len(s) >= 2 else s[-1][1]


# anchors and the syllable before each anchor (the previous line's last syllable or this line's hidden lead)
seq = []
for k, u in enumerate(units):
    n_lead = len(re.findall(r"[가-힣]", lines[u["id"]].get("lead", "")))
    syl = u.get("syl") or []
    A = syl[n_lead][1] if len(syl) > n_lead else (u.get("start_ctc") or u["start"])
    first = syl[n_lead][0] if len(syl) > n_lead else ""
    P = syl[n_lead - 1][1] if n_lead and len(syl) >= n_lead else (prev_syllable(k) if k else None)
    seq.append((A, A - 1.0 if P is None else P, INI[(ord(first) - 0xAC00) // 588] if first else ""))
leads = []
for A, P, ini in seq:
    q = quiet_end(max(P + 0.05, A - WIN(ini)), A + 0.03, level_at(A))
    if q is not None and A - tt(q) >= -0.02:
        leads.append(A - tt(q))
lead = float(np.clip(np.median(leads), 0.0, 0.06)) if leads else 0.02
out, prev, kinds = [], -1.0, {}
for k, u in enumerate(units):
    A, P, ini = seq[k]
    lo = max(P + 0.05, prev + 0.10)
    lev = level_at(A)
    t, how = A - lead, "ctc - lead"
    q = quiet_end(max(lo, A - WIN(ini)), A + 0.03, lev)
    if q is not None:
        t, how = tt(q) - 0.004, "after pause"
    else:
        a, b = fr(max(lo, A - 0.10)), fr(A + 0.02)
        if b - a > 5:
            seg = E[a:b]
            m = int(np.argmin(seg))
            left = E[max(a + m - 40, 0):a + m + 1].max(); right = E[a + m:min(a + m + 40, len(E))].max()
            if left - seg[m] >= 6 and right - seg[m] >= 6:
                j = a + m
                while j < len(E) - 1 and E[j] < seg[m] + 6:
                    j += 1
                t, how = min(tt(j) - 0.004, A + 0.01), "valley"
    hs = hiss_start(A, lo) if ini in NOISY else None
    if hs is not None and hs < t - 0.01:
        t, how = hs - 0.004, "hiss"
    t = min(max(t, lo - 0.05 if how == "ctc - lead" else lo), A + 0.01)
    prev = t
    kinds[how] = kinds.get(how, 0) + 1
    out.append(dict(u, start_v1=u.get("start"), start=round(t, 3), anchor=round(A, 3), onset_v2=how, first_consonant=ini))
json.dump(out, open(outp, "w"), ensure_ascii=False, indent=1)
d = np.array([o["start"] - o["start_v1"] for o in out]); da = np.array([o["start"] - o["anchor"] for o in out])
print(f"{len(out)} lines | CTC lead {lead * 1000:.0f} ms (from {len(leads)} pause onsets) | {kinds} | start - anchor: "
      f"p5 {np.percentile(da, 5) * 1000:+.0f} ms, median {np.median(da) * 1000:+.0f}, p95 {np.percentile(da, 95) * 1000:+.0f} | "
      f"vs ctc_align start: |diff| > 80 ms in {int((np.abs(d) > 0.08).sum())} lines")
