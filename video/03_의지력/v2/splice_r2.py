# 03편 v2 녹음 잇기 (2026-10-30 사용자 요청: "헬스장에 가는 일도 ~ 활동을 배치한 시간도 바꿔 볼 수 있습니다." 구간을
# 다시 녹음한 파일로 갈아 끼우기). 새 녹음은 처음부터 끝까지 그대로 씁니다(앞뒤를 자르지 않음, 속도·쉼 그대로).
# 옛 녹음(10월 28일 rec.wav)은 문장 사이 쉼의 무음 구간에서 자릅니다:
#   - 앞: "힘이 듭니다."의 끝소리가 사라진 뒤(247.98 s) 무음 속 248.08 s까지 옛 녹음, 그다음 무음 0.06 s, 새 녹음.
#     옛 녹음에서 "듭니다" 목소리 끝(247.85)부터 "헬스장" 목소리 시작(248.18)까지 0.33 s였던 쉼을 그대로 맞춤
#     (새 녹음은 목소리가 0.04 s에 시작).
#   - 뒤: 새 녹음 끝(마지막 "다"의 목소리 247.76 s, 끝소리는 파일 끝 247.89 s까지 그대로), 무음 0.03 s, 그다음
#     옛 녹음 494.03 s부터(무음 속; "평일에" 목소리는 494.12 s). 옛 녹음의 같은 쉼(0.22 s)과 비슷한 0.25 s.
#   - 이음매마다 5 ms 페이드(무음 속이라 들리는 소리는 바뀌지 않음). 두 녹음의 말소리 크기는 거의 같아(상위 5% -8.2 dB,
#     -8.0 dB) 크기는 맞추지 않음. 이어 붙인 뒤 prep_audio.py가 v1과 같이 한 번에 -14 LUFS로 맞춤.
# usage: splice_r2.py old.wav new.wav out.wav offsets.json
import json, subprocess, sys
import numpy as np
SR = 48000
OLD_CUT_IN, GAP1, GAP2, OLD_CUT_OUT = 248.08, 0.06, 0.03, 494.03
old_p, new_p, out_p, off_p = sys.argv[1:5]


def load(p):
    r = subprocess.run(["ffmpeg", "-v", "error", "-i", p, "-ac", "2", "-ar", str(SR), "-f", "f32le", "-"], capture_output=True, check=True)
    return np.frombuffer(r.stdout, np.float32).reshape(-1, 2).astype(np.float64)


old, new = load(old_p), load(new_p)
f = int(0.005 * SR); ramp = np.linspace(0, 1, f)[:, None]
a = old[:round(OLD_CUT_IN * SR)].copy(); a[-f:] *= ramp[::-1]
b = new.copy(); b[:f] *= ramp; b[-f:] *= ramp[::-1]
c = old[round(OLD_CUT_OUT * SR):].copy(); c[:f] *= ramp
z1, z2 = np.zeros((round(GAP1 * SR), 2)), np.zeros((round(GAP2 * SR), 2))
y = np.concatenate([a, z1, b, z2, c])
subprocess.run(["ffmpeg", "-v", "error", "-y", "-f", "f32le", "-ar", str(SR), "-ac", "2", "-i", "-", "-c:a", "pcm_f32le", out_p],
               input=y.astype(np.float32).tobytes(), check=True)
new0 = (len(a) + len(z1)) / SR
new1 = new0 + len(b) / SR
old1 = (len(a) + len(z1) + len(b) + len(z2)) / SR
info = {"old_cut_in": OLD_CUT_IN, "gap1": GAP1, "new_start": round(new0, 6), "new_len": round(len(b) / SR, 6), "new_end": round(new1, 6),
        "gap2": GAP2, "old_cut_out": OLD_CUT_OUT, "old_resume_at": round(old1, 6), "delta_after": round(old1 - OLD_CUT_OUT, 6),
        "total": round(len(y) / SR, 6), "old_total": round(len(old) / SR, 6)}
json.dump(info, open(off_p, "w"), indent=1)
print(info)
