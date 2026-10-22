#!/usr/bin/env python3
"""Non-intrusive DNSMOS P.835 scores (SIG, BAK, OVRL; 1..5) for audio files.

Follows microsoft/DNS-Challenge DNSMOS/dnsmos_local.py (non-personalised
polynomial mapping, 9.01 s windows, 1 s hop, 16 kHz input) but resamples with
ffmpeg/soxr instead of librosa.
Usage: dnsmos.py --model sig_bak_ovr.onnx FILE [FILE ...] [--json]
These are predicted MOS values from a neural network: a proxy, not a listening test.
"""
import argparse
import json
import subprocess
import sys

import numpy as np

SR = 16000
INPUT_LENGTH = 9.01
P_OVR = np.poly1d([-0.06766283, 1.11546468, 0.04602535])
P_SIG = np.poly1d([-0.08397278, 1.22083953, 0.0052439])
P_BAK = np.poly1d([-0.13166888, 1.60915514, -0.39604546])


def decode16k(path):
    cmd = ["ffmpeg", "-nostdin", "-v", "error", "-i", path, "-ac", "1",
           "-af", "aresample=16000:resampler=soxr", "-f", "f32le", "-"]
    raw = subprocess.run(cmd, check=True, stdout=subprocess.PIPE).stdout
    return np.frombuffer(raw, dtype="<f4").astype(np.float32)


def score(sess, audio):
    n = int(INPUT_LENGTH * SR)
    while len(audio) < n:
        audio = np.append(audio, audio)
    hops = int(np.floor(len(audio) / SR) - INPUT_LENGTH) + 1
    s, b, o = [], [], []
    name = sess.get_inputs()[0].name
    for i in range(hops):
        seg = audio[i * SR: i * SR + n]
        if len(seg) < n:
            continue
        sig, bak, ovr = sess.run(None, {name: seg[np.newaxis, :]})[0][0]
        s.append(P_SIG(sig))
        b.append(P_BAK(bak))
        o.append(P_OVR(ovr))
    return float(np.mean(s)), float(np.mean(b)), float(np.mean(o))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--model", required=True)
    ap.add_argument("files", nargs="+")
    ap.add_argument("--json", action="store_true")
    a = ap.parse_args()
    import onnxruntime as ort
    sess = ort.InferenceSession(a.model, providers=["CPUExecutionProvider"])
    rows = []
    for f in a.files:
        sig, bak, ovr = score(sess, decode16k(f))
        rows.append({"file": f, "SIG": sig, "BAK": bak, "OVRL": ovr})
        if not a.json:
            print(f"SIG {sig:4.2f}  BAK {bak:4.2f}  OVRL {ovr:4.2f}  {f}")
    if a.json:
        json.dump(rows, sys.stdout, indent=1)
        print()


if __name__ == "__main__":
    main()
