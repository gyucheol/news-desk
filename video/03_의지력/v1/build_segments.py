import json, sys
sys.path.insert(0, '.')
from seg_plan import SEG, K_SENTS
L = json.load(open('lines_v3.json', encoding='utf-8'))
O = json.load(open('onsets_v3.json', encoding='utf-8'))
END = 560.0
key2i = {(l['sent'], l['pi']): i for i, l in enumerate(L)}
starts = [key2i[s[0]] for s in SEG]
assert starts == sorted(starts) and starts[0] == 0, 'order'
segs = []
for j, s in enumerate(SEG):
    i0 = starts[j]; i1 = starts[j + 1] if j + 1 < len(SEG) else len(L)
    t0 = O[i0]['start']; t1 = O[i1]['start'] if i1 < len(L) else END
    lines = L[i0:i1]
    kind = s[1]
    d = {'n': j + 1, 'kind': kind, 'value': s[2], 'i0': i0, 'i1': i1, 't0': round(t0, 3), 't1': round(t1, 3),
         'dur': round(t1 - t0, 2), 'text': ' / '.join(l['text'] for l in lines),
         'pos': ''.join(l['pos'] for l in lines), 'sents': sorted({l['sent'] for l in lines})}
    if kind == 'S':
        d.update({'desc': s[3], 'kw': s[4], 'reuse': s[5]})
    if kind == 'K':
        assert all(l['sent'] in K_SENTS for l in lines), (j, lines[0]['text'])
    segs.append(d)
# K 문장이 다른 장면에 섞이지 않았는지
for d in segs:
    if d['kind'] != 'K':
        bad = [x for x in d['sents'] if x in K_SENTS]
        assert not bad, (d['n'], bad)
json.dump(segs, open('segments.json', 'w'), ensure_ascii=False, indent=1)
st = [d for d in segs if d['kind'] == 'S']
print('segments', len(segs), 'stock', len(st), 'stock time', round(sum(d['dur'] for d in st), 1),
      'photo time', round(sum(d['dur'] for d in segs if d['kind'] == 'P'), 1), 'K time', round(sum(d['dur'] for d in segs if d['kind'] == 'K'), 1))
print('avg seg', round(END / len(segs), 2), 'shortest', sorted((d['dur'], d['n'], d['kind'], d['value']) for d in segs)[:8])
print('longest stock', sorted(((d['dur'], d['value']) for d in st), reverse=True)[:8])
