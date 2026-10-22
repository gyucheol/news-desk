#!/usr/bin/env python3
"""Helpers for polish_voice.sh.

  vt_util.py lag A.wav B.wav          -> lag of B relative to A in samples
  vt_util.py trim-bounds X.wav [--pad-start 0.3 --pad-end 0.5]
                                      -> "START END" seconds, or "none"
Trim bounds only locate the first and last sustained speech activity, so
nothing inside the speech is ever removed.
"""
import argparse
import sys

import numpy as np
import soundfile as sf
from scipy.signal import correlate


def load_mono(path):
    x, sr = sf.read(path, dtype="float32", always_2d=True)
    return x.astype(np.float64), sr


def cmd_lag(a):
    x, sr = load_mono(a.a)
    y, _ = load_mono(a.b)
    x = x.mean(axis=1)
    y = y.mean(axis=1)
    n = min(len(x), len(y), sr * 30)
    max_lag = int(0.1 * sr)
    c = correlate(y[:n], x[:n], mode="full", method="fft")
    mid = n - 1
    seg = c[mid - max_lag: mid + max_lag + 1]
    print(int(np.argmax(np.abs(seg)) - max_lag))


def cmd_trim(a):
    x, sr = load_mono(a.file)
    env = np.max(np.abs(x), axis=1)  # use loudest channel
    w = int(0.02 * sr)
    n = len(env) // w
    if n < 10:
        print("none")
        return
    fr = x[: n * w].reshape(n, w, -1)
    db = 10 * np.log10(np.max(np.mean(fr ** 2, axis=1), axis=1) + 1e-20)
    floor = np.percentile(db, 10)
    loud = np.percentile(db, 95)
    span = loud - floor
    if span < 15:  # speech not clearly above the background: do not trim
        print("none")
        return
    thr = floor + max(6.0, min(15.0, 0.3 * span))
    act = db > thr
    run = 3  # 60 ms sustained activity
    ok = np.convolve(act.astype(int), np.ones(run, dtype=int), mode="valid") == run
    idx = np.flatnonzero(ok)
    if idx.size == 0:
        print("none")
        return
    # extend outwards over soft onsets/decays: keep going while frames stay
    # above floor + 4 dB (gaps of up to 3 frames = 60 ms tolerated)
    soft = db > floor + 4.0
    i0 = idx[0]
    gap = 0
    j = i0 - 1
    while j >= 0 and gap <= 3:
        if soft[j]:
            i0, gap = j, 0
        else:
            gap += 1
        j -= 1
    i1 = idx[-1] + run - 1
    gap = 0
    j = i1 + 1
    while j < n and gap <= 3:
        if soft[j]:
            i1, gap = j, 0
        else:
            gap += 1
        j += 1
    first = i0 * w / sr
    last = (i1 + 1) * w / sr
    dur = len(x) / sr
    start = max(0.0, first - a.pad_start)
    end = min(dur, last + a.pad_end)
    if start < 0.05 and end > dur - 0.05:
        print("none")
        return
    print(f"{start:.3f} {end:.3f}")


def main():
    ap = argparse.ArgumentParser()
    sub = ap.add_subparsers(dest="cmd", required=True)
    p = sub.add_parser("lag")
    p.add_argument("a")
    p.add_argument("b")
    p.set_defaults(fn=cmd_lag)
    p = sub.add_parser("trim-bounds")
    p.add_argument("file")
    p.add_argument("--pad-start", type=float, default=0.3)
    p.add_argument("--pad-end", type=float, default=0.5)
    p.set_defaults(fn=cmd_trim)
    a = ap.parse_args()
    a.fn(a)


if __name__ == "__main__":
    sys.exit(main())
