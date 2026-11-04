# 수면 편 v2 (2026-11-04): 다시 녹음한 조각(rec151, "참가자들은 14일 동안" ~ "비슷한 수준까지 떨어졌습니다.")을 원래 녹음에 이음.
# 자르는 곳은 원래 녹음의 디지털 무음 속(앞: 72.55초, 이전 문장 끝과 '참가자들은' 사이 / 뒤: 100.90초, '떨어졌습니다' 끝과
# '그런데' 사이). 새 조각은 처음부터 끝까지 그대로 씀(꼬리를 자르지 않음, 끝 10ms만 줄여 이음매 잡음을 막음).
# 쉼: 앞 약 0.11초(원래 0.14초), 뒤 약 0.44초(원래 0.39초). 새 조각은 음색과 크기를 앞뒤 녹음에 맞춘 것(rec2/match_tone.py).
import json, subprocess
import numpy as np
SR = 48000
A, B = 72.55, 100.90
def load(p):
    return np.frombuffer(subprocess.run(['ffmpeg','-v','error','-i',p,'-ac','1','-ar',str(SR),'-f','f32le','-'],capture_output=True,check=True).stdout,np.float32)
old = load('rec/rec.wav'); new = load('rec2/rec151_matched.wav').copy()
f = int(0.010 * SR); new[-f:] *= np.linspace(1, 0, f)
out = np.concatenate([old[:int(A * SR)], new, old[int(B * SR):]])
subprocess.run(['ffmpeg','-v','error','-y','-f','f32le','-ar',str(SR),'-ac','1','-i','-','-c:a','pcm_f32le','rec/rec_v2.wav'],input=out.astype(np.float32).tobytes(),check=True)
delta = len(new) / SR - (B - A)
info = {'cut_a': A, 'cut_b': B, 'new_len': round(len(new) / SR, 4), 'delta': round(delta, 4), 'total': round(len(out) / SR, 4),
        'new_file': '85b05928-151.m4a (2026-11-04)', 'tone': 'rec2/match_tone.json'}
json.dump(info, open('rec/splice_v2.json', 'w'), indent=1)
# 받아쓰기 낱말도 같은 자리에서 이음
w_old = json.load(open('rec/rec_words.json', encoding='utf-8')); w_new = json.load(open('rec2/rec151_words.json', encoding='utf-8'))
words = [x for x in w_old if x[1] < A] + [[x[0], round(x[1] + A, 3), round(x[2] + A, 3), x[3]] for x in w_new] + \
        [[x[0], round(x[1] + delta, 3), round(x[2] + delta, 3), x[3]] for x in w_old if x[1] >= B]
json.dump(words, open('rec/rec_v2_words.json', 'w', encoding='utf-8'), ensure_ascii=False)
segs = [{'start': words[0][1], 'end': words[-1][2], 'text': ' '.join(x[0] for x in words), 'words': [[x[1], x[2], ' ' + x[0], x[3]] for x in words]}]
json.dump(segs, open('rec/rec_v2_words_seg.json', 'w', encoding='utf-8'), ensure_ascii=False)
print(info, len(words), 'words')
