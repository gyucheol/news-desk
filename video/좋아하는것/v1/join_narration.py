# 녹음 1편 전체 + 쉼 0.20초 + 녹음 2편 처음~44.20초(50번 사진 문장 '나중에 예상하지 못한 상을 줬습니다.'의 끝, 다음 문장 앞 쉼 안)
# + 끝 무음 2.0초. 자르거나 속도를 바꾸지 않고, 1편 끝의 쉼(0.17초)과 2편 앞의 쉼(0.10초)은 녹음 그대로 둠.
# 이어 붙인 자리의 쉼은 모두 약 0.47초: 이 녹음에서 가장 긴 쉼(1편 0.40초, 2편 0.49초)과 비슷하게, 단락이 바뀌는 자리라서.
# usage: join_narration.py  (ep4/v1에서) -> rec.wav, join.json
import json, subprocess
import numpy as np
SR = 48000
def load(p):
    return np.frombuffer(subprocess.run(['ffmpeg', '-v', 'error', '-i', p, '-ac', '1', '-ar', str(SR), '-f', 's16le', '-'],
                                        capture_output=True, check=True).stdout, np.int16)
a = load('../rec/part1.m4a'); b = load('../rec/part2.m4a')
GAP, CUT2, TAIL = 0.20, 44.20, 2.0
seg_b = b[:int(round(CUT2 * SR))]
out = np.concatenate([a, np.zeros(int(round(GAP * SR)), np.int16), seg_b, np.zeros(int(round(TAIL * SR)), np.int16)])
subprocess.run(['ffmpeg', '-v', 'error', '-y', '-f', 's16le', '-ar', str(SR), '-ac', '1', '-i', '-', '-c:a', 'pcm_s16le', 'rec.wav'],
               input=out.tobytes(), check=True)
off2 = len(a) / SR + GAP
info = {'part1_len': len(a) / SR, 'gap': GAP, 'part2_offset': off2, 'part2_cut': CUT2, 'voice_end': off2 + CUT2,
        'tail': TAIL, 'total': len(out) / SR}
json.dump(info, open('join.json', 'w'), indent=1)
print(info)
