import json, glob, os, re
BASE = '/home/user/news-desk/data/backfill-2026-10-13'
SRC = os.path.join(BASE, 'in', 'S1.json')
SCR = os.path.join(BASE, 'scratch', 'S1')
OUT = os.path.join(BASE, 'out', 'S1.json')
src_list = json.load(open(SRC, encoding='utf-8'))
src = {d['id']: d for d in src_list}
order = {d['id']: k for k, d in enumerate(src_list)}

def mark(text, phrases, lo, hi, label, errs):
    if not lo <= len(phrases) <= hi:
        errs.append(f'{label}: {len(phrases)} spans'); return text
    spans = []
    for p in phrases:
        n = text.count(p)
        if n != 1:
            errs.append(f'{label}: "{p}" found {n}x'); return text
        if not 2 <= len(p) <= 20:
            errs.append(f'{label}: "{p}" len {len(p)}'); return text
        if '(제목 기준)' in p or '(채널 전언)' in p:
            errs.append(f'{label}: tail in span'); return text
        i = text.index(p)
        spans.append((i, i + len(p), p))
    spans.sort()
    for a, b in zip(spans, spans[1:]):
        if a[1] > b[0]:
            errs.append(f'{label}: overlap'); return text
    out, last = [], 0
    for s, e, _ in spans:
        out.append(text[last:s]); out.append('{{' + text[s:e] + '}}'); last = e
    out.append(text[last:])
    return ''.join(out)

specs = []
for f in sorted(glob.glob(os.path.join(SCR, 'spec_*.json'))):
    specs += json.load(open(f, encoding='utf-8'))
errs, docs = [], {}
for e in specs:
    i = e['id']
    if i not in src: errs.append(f'{i}: not in input'); continue
    if i in docs: errs.append(f'{i}: duplicate'); continue
    s = src[i]
    docs[i] = {'id': i,
               'title': mark(s['title'], e['title'], 1, 2, i + '.title', errs),
               'one': mark(s['one'], e['one'], 2, 4, i + '.one', errs)}
    for f in ('title', 'one'):
        if docs[i][f].replace('{{', '').replace('}}', '') != s[f]:
            errs.append(f'{i}.{f}: plain text changed')
out = [docs[i] for i in sorted(docs, key=lambda k: order[k])]
os.makedirs(os.path.dirname(OUT), exist_ok=True)
json.dump({'docs': out}, open(OUT, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('saved', len(out), 'docs; errors:', len(errs))
for x in errs[:60]: print(' -', x)
