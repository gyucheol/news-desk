import json, collections
d = json.load(open('clusters_G2a.json'))
keep = [int(l.split('\t')[0]) for l in open('keep_G2a.tsv') if l.strip()]
ex = {l.split('\t')[1]: int(l.rstrip('\n').split('\t')[4]) for l in open('existing.tsv')}
used = [n for c in d['clusters'] for n in c['lines']] + [x['line'] for x in d['drop']]
cnt = collections.Counter(used)
print('keep lines', len(keep), 'used', len(used))
print('missing', sorted(set(keep) - set(used)))
print('extra', sorted(set(used) - set(keep)))
print('dup', [k for k, v in cnt.items() if v > 1])
cids = [c['cid'] for c in d['clusters']]
print('cids ok', cids == [f'G2a-{i:03d}' for i in range(1, len(cids) + 1)], 'size order ok', [len(c['lines']) for c in d['clusters']] == sorted([len(c['lines']) for c in d['clusters']], reverse=True))
for c in d['clusters']:
    a = c['attachTo']
    bad = [x for x in c['core'] if not 15 <= len(x) <= 45]
    print(c['cid'], c['field'], a or '""', ('n=%d' % ex[a]) if a else '', 'core', len(c['core']), 'ok' if 1 <= len(c['core']) <= 5 else 'BAD', 'len-out' if bad else '', bad, [len(x) for x in c['core']])
    assert not a or a in ex, a
print('clusters', len(d['clusters']), 'singles', sum(len(c['lines']) == 1 for c in d['clusters']),
      'attachTo', sum(bool(c['attachTo']) for c in d['clusters']), 'drop', len(d['drop']))
