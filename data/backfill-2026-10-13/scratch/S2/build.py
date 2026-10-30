import glob, json, os, sys

BASE = '/home/user/news-desk/data/backfill-2026-10-13'
src = json.load(open(f'{BASE}/in/S2.json', encoding='utf-8'))
ids = {d['id'] for d in src}
spec = {}
for p in sorted(glob.glob(f'{BASE}/scratch/S2/spec_*.json')):
    for k, v in json.load(open(p, encoding='utf-8')).items():
        if k not in ids:
            sys.exit(f'unknown id {k} in {p}')
        if k in spec:
            sys.exit(f'duplicate id {k} in {p}')
        spec[k] = v
docs = []
for d in src:
    s = spec.get(d['id'])
    if s is None:
        continue
    o = {'id': d['id']}
    for f in ('title', 'one'):
        text = d[f]
        spans = []
        for ph in s[f]:
            n = text.count(ph)
            if n != 1:
                sys.exit(f"{d['id']}.{f}: {ph!r} occurs {n} times")
            i = text.index(ph)
            spans.append((i, i + len(ph)))
        spans.sort()
        for (a1, b1), (a2, b2) in zip(spans, spans[1:]):
            if a2 < b1:
                sys.exit(f"{d['id']}.{f}: overlapping highlights")
        out, last = [], 0
        for a, b in spans:
            out.append(text[last:a])
            out.append('{{' + text[a:b] + '}}')
            last = b
        out.append(text[last:])
        o[f] = ''.join(out)
    docs.append(o)
os.makedirs(f'{BASE}/out', exist_ok=True)
with open(f'{BASE}/out/S2.json', 'w', encoding='utf-8') as fh:
    json.dump({'docs': docs}, fh, ensure_ascii=False, indent=1)
print('wrote', len(docs), 'docs')
