# onsets_v3.json에 줄마다 끝 시각(end)을 더합니다(build_timeline.py가 씀). 끝 시각은 2판 음절 맞춤(../align/align_ctc.json)의
# 그 줄 끝입니다. 사진 4장에 맞춰 나눈 [69](2판 L206, L207)는 다음 줄의 시작, 마지막 조각 '돌아와야 합니다.'는 L207의 끝입니다.
# usage: add_line_ends.py   (ep3/v3 폴더에서, onsets_v2.py 다음에)
import json
A = json.load(open('../align/align_ctc.json', encoding='utf-8'))
L = json.load(open('lines_v3.json', encoding='utf-8'))
O = json.load(open('onsets_v3.json', encoding='utf-8'))
src_end = {a['id']: a.get('end') for a in A}
for i, (l, o) in enumerate(zip(L, O)):
    e = src_end.get(l['src'])
    if l['src'] in ('L206', 'L207'):
        e = O[i + 1]['start'] if i + 1 < len(O) else e
        if l['text'] == '돌아와야 합니다.':
            e = src_end['L207']
    o['end'] = e
json.dump(O, open('onsets_v3.json', 'w'), ensure_ascii=False, indent=1)
print(O[-1]['id'], O[-1]['text'], O[-1]['start'], O[-1]['end'])
