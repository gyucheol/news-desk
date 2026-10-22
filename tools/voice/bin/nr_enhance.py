#!/usr/bin/env python3
"""Spectral-gating noise reduction with the 'noisereduce' package.

Usage: nr_enhance.py IN.wav OUT.wav [--prop 0.9] [--stationary]
Output is float WAV, same length and alignment as the input.
"""
import argparse
import sys
import time


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("inp")
    ap.add_argument("out")
    ap.add_argument("--prop", type=float, default=0.9, help="prop_decrease 0..1")
    ap.add_argument("--stationary", action="store_true")
    ap.add_argument("--time-constant-s", type=float, default=2.0,
                    help="noise-estimate time constant (non-stationary mode)")
    a = ap.parse_args()
    import noisereduce as nr
    import numpy as np
    import soundfile as sf

    x, sr = sf.read(a.inp, dtype="float32", always_2d=True)  # [T, C]
    t0 = time.time()
    y = nr.reduce_noise(y=np.ascontiguousarray(x.T), sr=sr, stationary=a.stationary,
                        prop_decrease=a.prop, time_constant_s=a.time_constant_s,
                        n_jobs=1)
    y = np.atleast_2d(y)
    el = time.time() - t0
    sf.write(a.out, y.T.astype(np.float32), sr, subtype="FLOAT")
    dur = x.shape[0] / sr
    print(f"[nr] {dur:.1f}s audio, {el:.1f}s compute ({el / dur * 60:.1f}s per audio-minute)",
          file=sys.stderr)


if __name__ == "__main__":
    main()
