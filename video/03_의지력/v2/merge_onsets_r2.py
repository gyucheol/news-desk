# 03편 v2 줄 시각 합치기: 녹음이 그대로인 앞뒤 구간은 v1에서 확인한 시각을 쓰고(앞은 그대로, 뒤는 delta만큼 뒤로),
# 새 녹음 구간(V203~V405)만 새로 맞춘 시각(onsets_r2_raw.json)을 씁니다.
# - 새로 맞춘 값은 앞 구간에서 v1과 2 ms 안으로 같았고, 뒤 구간에서는 2줄이 달랐음: V418 '아니니까요.'(음절 맞춤이 깨져 0.79 s
#   늦음), V441(35 ms). 같은 소리이므로 v1 값을 씁니다.
# - V213 '그러니': 앞 줄 마지막 음절이 쉼 안으로 밀려 시작이 0.32 s 늦게 잡힘(260.388). 쉼이 끝나고 'ㄱ' 소리가 나는
#   260.07 s로 고침(소리 크기로 확인: 259.75~260.02 무음, 260.07부터 -33 dB 이상).
# usage: merge_onsets_r2.py onsets_v1.json onsets_r2_raw.json splice_r2.json out.json
import json, sys
O1 = json.load(open(sys.argv[1], encoding='utf-8')); O2 = json.load(open(sys.argv[2], encoding='utf-8'))
d = json.load(open(sys.argv[3]))['delta_after']
idx = {o['id']: i for i, o in enumerate(O2)}
i0, i1 = idx['V203'], idx['V405']
FIX = {'V213': 260.07}
TIME_KEYS = ('start', 'start_ctc', 'start_v1', 'anchor', 'end')
out = []
for i, (a, b) in enumerate(zip(O1, O2)):
    assert a['id'] == b['id']
    if i < i0:
        o = dict(a)
    elif i > i1:
        o = dict(a)
        for k in TIME_KEYS:
            if isinstance(o.get(k), (int, float)):
                o[k] = round(o[k] + d, 4)
        o['syl'] = [[c, round(t + d, 4)] for c, t in a.get('syl', [])]
    else:
        o = dict(b)
        if o['id'] in FIX:
            o['start'] = FIX[o['id']]; o['onset_v2'] = 'after pause (fixed by hand 2026-10-30)'
    out.append(o)
for i in range(1, len(out)):
    assert out[i]['start'] > out[i - 1]['start'], out[i]['id']
json.dump(out, open(sys.argv[4], 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(out), 'lines | new part', out[i0]['id'], out[i0]['start'], '-', out[i1]['id'], out[i1]['start'], '| last', out[-1]['id'], out[-1]['start'], out[-1]['end'])
