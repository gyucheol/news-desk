# v2 줄 시작 시각: 이은 자리 앞(V001~V051)은 v1 그대로, 새 녹음(V052~V070)은 새로 맞춘 시각, 뒤(V071~)는 v1 + 길이 차이.
# (뒤쪽 소리는 v1과 같고 자리만 밀림. 새로 맞추면 3줄이 30ms 넘게 달라졌는데, V071은 이은 자리 앞으로 당겨져 틀림)
import json
D = json.load(open('rec/splice_v2.json'))['delta']
A = json.load(open('v1_keep/onsets_v2.json', encoding='utf-8')); B = {o['id']: o for o in json.load(open('onsets_v2.json', encoding='utf-8'))}
TIME = ('start', 'end', 'first_word_end', 'start_asr', 'start_ctc', 'start_v1', 'anchor')
out = []
for o in A:
    n = int(o['id'][1:])
    if n < 52:
        out.append(o)
    elif n <= 70:
        out.append(B[o['id']])
    else:
        x = dict(o)
        for k in TIME:
            if isinstance(x.get(k), (int, float)):
                x[k] = round(x[k] + D, 3)
        if isinstance(x.get('syl'), list):
            x['syl'] = [[s, round(t + D, 3)] if isinstance(t, (int, float)) else [s, t] for s, t in x['syl']]
        out.append(x)
json.dump(out, open('onsets_v2.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(out), 'lines, delta', D)
