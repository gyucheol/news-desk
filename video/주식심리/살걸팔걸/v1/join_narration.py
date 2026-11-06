# 녹음 세 개(1_1, 2_1, 3_1)를 순서대로 이어 rec/rec.wav를 만듦(자르거나 속도를 바꾸지 않음).
# 세 파일 모두 말이 0.05초 안에 시작하고 끝에서 약 0.2초 안에 끝나서, 이음매에 무음을 넣어 쉼을 맞춤.
#   1 -> 2: 원인 2로 넘어가는 자리(질문 뒤 새 장면) -> 실제 쉼 0.70초
#   2 -> 3: 같은 문단 안('사후 확신 편향이라고 부릅니다' -> '그래서 결과를 알기 전에') -> 실제 쉼 0.50초
# 녹음 안의 문장 사이 쉼은 0.25~0.59초(1번 파일, 중앙값 0.34초).
import json, wave
import numpy as np
SR = 48000
parts, info = [], []
for n in (1, 2, 3):
    w = wave.open(f'rec/part{n}.wav'); assert w.getframerate() == SR and w.getnchannels() == 1
    x = np.frombuffer(w.readframes(w.getnframes()), np.int16).astype(np.float32)
    parts.append(x)
def edges(x):
    hop = SR // 100; win = SR // 50
    r = np.sqrt(np.convolve(x.astype(np.float64) ** 2, np.ones(win) / win, 'same')[::hop] + 1e-9) / 32768
    db = 20 * np.log10(r + 1e-12); v = np.nonzero(db > np.percentile(db, 95) - 22)[0]
    return v[0] * 0.01, len(x) / SR - v[-1] * 0.01
WANT = [0.70, 0.50]
out = []; t = 0.0; offs = []
for k, x in enumerate(parts):
    head, tail = edges(x)
    f = int(0.005 * SR); x = x.copy(); x[:f] *= np.linspace(0, 1, f); x[-f:] *= np.linspace(1, 0, f)
    if k:
        prev_tail = info[-1]['tail']
        gap = max(WANT[k - 1] - prev_tail - head, 0.0)
        out.append(np.zeros(int(round(gap * SR)), np.float32)); t += int(round(gap * SR)) / SR
        info[-1]['gap_after'] = round(gap, 3)
    offs.append(round(t, 4)); out.append(x); t += len(x) / SR
    info.append({'part': k + 1, 'offset': round(offs[-1], 4), 'len': round(len(x) / SR, 4), 'head': round(head, 2), 'tail': round(tail, 2)})
y = np.concatenate(out)
w = wave.open('rec/rec.wav', 'wb'); w.setnchannels(1); w.setsampwidth(2); w.setframerate(SR)
w.writeframes(np.clip(y, -32768, 32767).astype(np.int16).tobytes()); w.close()
json.dump({'parts': info, 'total': round(len(y) / SR, 4)}, open('rec/join.json', 'w'), indent=1)
print(json.dumps(info), 'total', round(len(y) / SR, 3))
