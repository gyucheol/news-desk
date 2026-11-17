# 전체 영상 v2: 녹음 1편 + 쉼 0.20초 + 2편 전체 + 쉼 0.27초 + 3편 전체 + 끝 무음 3초 -> rec_full.wav, join_full.json
# 자르거나 속도를 바꾸지 않음. 이은 자리의 쉼은 둘 다 약 0.47초(앞 녹음 끝의 쉼 + 넣은 무음 + 뒤 녹음 앞의 쉼):
#  1편 끝 0.17 + 0.20 + 2편 앞 0.10 / 2편 끝 0.17 + 0.27 + 3편 앞 0.03. 이 녹음에서 가장 긴 쉼(0.40~0.49초)과 비슷함.
import json, subprocess
import numpy as np
SR = 48000
def load(p):
    return np.frombuffer(subprocess.run(['ffmpeg', '-v', 'error', '-i', p, '-ac', '1', '-ar', str(SR), '-f', 's16le', '-'],
                                        capture_output=True, check=True).stdout, np.int16)
a, b, c = (load(f'../rec/part{i}.m4a') for i in (1, 2, 3))
G1, G2, TAIL = 0.20, 0.27, 3.0
z = lambda s: np.zeros(int(round(s * SR)), np.int16)
out = np.concatenate([a, z(G1), b, z(G2), c, z(TAIL)])
subprocess.run(['ffmpeg', '-v', 'error', '-y', '-f', 's16le', '-ar', str(SR), '-ac', '1', '-i', '-', '-c:a', 'pcm_s16le', 'rec_full.wav'],
               input=out.tobytes(), check=True)
off2 = len(a) / SR + G1
off3 = off2 + len(b) / SR + G2
info = {'part1_len': len(a) / SR, 'gap1': G1, 'part2_offset': off2, 'part2_len': len(b) / SR, 'gap2': G2, 'part3_offset': off3,
        'part3_len': len(c) / SR, 'voice_end': off3 + 239.34, 'tail': TAIL, 'total': len(out) / SR}
json.dump(info, open('join_full.json', 'w'), indent=1)
print(info)
