#!/usr/bin/env python3
"""DeepFilterNet3 noise suppression: 48 kHz WAV in -> 48 kHz float WAV out.

Same length as the input and delay-compensated. Long inputs are processed in
chunks (with pre-roll context and a short cross-fade) to bound memory.
Run with the Python 3.11 venv that has deepfilternet + CPU torch:
  venv311/bin/python -I dfn_enhance.py IN.wav OUT.wav --model-dir DIR [--atten-lim 24]
"""
import argparse
import sys
import time
import warnings


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("inp")
    ap.add_argument("out")
    ap.add_argument("--model-dir", required=True, help="dir with config.ini + checkpoints/")
    ap.add_argument("--atten-lim", type=float, default=None,
                    help="limit noise attenuation to this many dB (default: unlimited)")
    ap.add_argument("--post-filter", action="store_true")
    ap.add_argument("--threads", type=int, default=0)
    ap.add_argument("--chunk-s", type=float, default=120.0)
    ap.add_argument("--preroll-s", type=float, default=3.0)
    a = ap.parse_args()

    warnings.filterwarnings("ignore")
    import numpy as np
    import soundfile as sf
    import torch

    # Never unpickle arbitrary objects from the checkpoint file.
    _orig_load = torch.load

    def _safe_load(*args, **kw):
        kw["weights_only"] = True
        return _orig_load(*args, **kw)

    torch.load = _safe_load
    if a.threads > 0:
        torch.set_num_threads(a.threads)

    from df.enhance import enhance, init_df

    model, df_state, _ = init_df(model_base_dir=a.model_dir, post_filter=a.post_filter,
                                 log_level="ERROR", log_file=None)
    x, sr = sf.read(a.inp, dtype="float32", always_2d=True)  # [T, C]
    if sr != df_state.sr():
        sys.exit(f"dfn_enhance: expected {df_state.sr()} Hz input, got {sr}")
    x = np.ascontiguousarray(x.T)  # [C, T]
    n = x.shape[1]
    chunk = int(a.chunk_s * sr)
    pre = int(a.preroll_s * sr)
    xf = int(0.05 * sr)  # 50 ms cross-fade
    t0 = time.time()
    out = np.zeros_like(x)

    def run(seg):
        with torch.inference_mode():
            return enhance(model, df_state, torch.from_numpy(np.ascontiguousarray(seg)),
                           pad=True, atten_lim_db=a.atten_lim).numpy()

    if n <= chunk + pre:
        out[:] = run(x)
    else:
        ramp = np.linspace(0.0, 1.0, xf, dtype=np.float32)
        s = 0
        while s < n:
            e = min(n, s + chunk)
            a0 = max(0, s - pre)
            e1 = min(n, e + xf)
            y = run(x[:, a0:e1])[:, s - a0:]
            if s == 0:
                out[:, s:e1] = y
            else:
                # cross-fade the first xf samples with the previous chunk's tail
                out[:, s:s + xf] = out[:, s:s + xf] * (1 - ramp) + y[:, :xf] * ramp
                out[:, s + xf:e1] = y[:, xf:]
            s = e
    el = time.time() - t0
    sf.write(a.out, out.T, sr, subtype="FLOAT")
    dur = n / sr
    print(f"[dfn] {dur:.1f}s audio, {el:.1f}s compute "
          f"({el / dur * 60:.1f}s per audio-minute)", file=sys.stderr)


if __name__ == "__main__":
    main()
