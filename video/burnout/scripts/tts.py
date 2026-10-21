# Temporary guide narration for previews only (NOT for upload; the real video uses the owner's voice).
# Synthesizes each sentence with edge-tts, trims silence, joins with fixed pauses.
# usage: tts.py sentences.json out_raw.wav
#   sentences.json: {"voice": "ko-KR-SunHiNeural", "lead": 0.25, "gap": 0.30, "tail": 0.70,
#                    "sentences": [{"id": "s1", "text": "...", "rate": "+0%"}, ...]}
import asyncio, json, os, ssl, subprocess, sys, wave
import numpy as np
import edge_tts
import edge_tts.communicate as cm

ROOT = os.environ.get("VIDEO_ROOT", os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
CA = "/root/.ccr/ca-bundle.crt"   # cloud-session proxy CA; edge-tts pins certifi otherwise
if os.path.exists(CA):
    cm._SSL_CTX = ssl.create_default_context(cafile=CA)
SR = 48000
cfg = json.load(open(sys.argv[1])); out = sys.argv[2]
tmp = f"{ROOT}/work/tts"; os.makedirs(tmp, exist_ok=True)


async def synth(s):
    c = edge_tts.Communicate(s["text"], voice=cfg.get("voice", "ko-KR-SunHiNeural"), rate=s.get("rate", "+0%"))
    with open(f"{tmp}/{s['id']}.mp3", "wb") as f:
        async for ch in c.stream():
            if ch["type"] == "audio":
                f.write(ch["data"])


def load(sid):
    pcm = subprocess.run(["ffmpeg", "-v", "error", "-i", f"{tmp}/{sid}.mp3", "-ac", "1", "-ar", str(SR),
                          "-f", "s16le", "-"], capture_output=True, check=True).stdout
    return np.frombuffer(pcm, np.int16).astype(np.float32) / 32768


def trim(x):
    hop = SR // 100
    db = 20 * np.log10(np.sqrt(np.convolve(x ** 2, np.ones(hop) / hop, mode="same")[::hop] + 1e-12))
    act = np.where(db > -45)[0]
    a = max(act[0] * hop - int(0.05 * SR), 0); b = min((act[-1] + 1) * hop + int(0.15 * SR), len(x))
    y = x[a:b].copy(); f = int(0.01 * SR)
    y[:f] *= np.linspace(0, 1, f); y[-f:] *= np.linspace(1, 0, f)
    return y


async def main():
    for s in cfg["sentences"]:
        await synth(s)
    parts = [np.zeros(int(cfg.get("lead", 0.25) * SR), np.float32)]
    for i, s in enumerate(cfg["sentences"]):
        parts.append(trim(load(s["id"])))
        last = i == len(cfg["sentences"]) - 1
        parts.append(np.zeros(int(cfg.get("tail" if last else "gap", 0.3) * SR), np.float32))
    y = np.concatenate(parts)
    w = wave.open(out, "wb"); w.setnchannels(1); w.setsampwidth(2); w.setframerate(SR)
    w.writeframes((np.clip(y, -1, 1) * 32767).astype(np.int16).tobytes()); w.close()
    print(out, round(len(y) / SR, 2), "s")

asyncio.run(main())
