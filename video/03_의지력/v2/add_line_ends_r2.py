# onsets_v3.json에 줄마다 끝 시각(end)을 더합니다(build_timeline.py가 씀). 끝 시각은 2판 음절 맞춤(../align/align_ctc.json)의
# 그 줄 끝입니다. 사진 4장에 맞춰 나눈 [69](2판 L206, L207)는 다음 줄의 시작, 마지막 조각 '돌아와야 합니다.'는 L207의 끝입니다.
# 03편 v2: 입력을 인자로. usage: add_line_ends_r2.py align_ctc.json lines.json onsets.json (onsets.json을 고쳐 씀)
import json, sys
A = json.load(open(sys.argv[1], encoding='utf-8'))
L = json.load(open(sys.argv[2], encoding='utf-8'))
O = json.load(open(sys.argv[3], encoding='utf-8'))
src_end = {a['id']: a.get('end') for a in A}
for i, (l, o) in enumerate(zip(L, O)):
    e = src_end.get(l['src'])
    if l['src'] in ('L206', 'L207'):
        e = O[i + 1]['start'] if i + 1 < len(O) else e
        if l['text'] == '돌아와야 합니다.':
            e = src_end['L207']
    o['end'] = e
json.dump(O, open(sys.argv[3], 'w'), ensure_ascii=False, indent=1)
print(O[-1]['id'], O[-1]['text'], O[-1]['start'], O[-1]['end'])
