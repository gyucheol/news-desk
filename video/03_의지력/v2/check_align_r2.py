# 03편 v2 자막 시각 점검: 새로 맞춘 onsets_r2.json을 v1(onsets_v3.json)과 비교합니다.
# - 새 녹음 앞(V001~V202): v1과 같아야 함 / 뒤(V406~V450): v1 + delta와 같아야 함
# - 새 녹음 구간(V203~V405): 시작이 차례대로 늘어나는지, 줄 길이, 받아쓴 낱말 시작과의 차이
# usage: check_align_r2.py onsets_v3.json onsets_r2.json splice_r2.json new_words.json lines_r2.json
import json, re, sys
O1 = json.load(open(sys.argv[1], encoding='utf-8')); O2 = json.load(open(sys.argv[2], encoding='utf-8'))
sp = json.load(open(sys.argv[3])); W = json.load(open(sys.argv[4], encoding='utf-8')); L = json.load(open(sys.argv[5], encoding='utf-8'))
d, n0 = sp['delta_after'], sp['new_start']
assert [o['id'] for o in O1] == [o['id'] for o in O2]
idx = {o['id']: i for i, o in enumerate(O2)}
i203, i405 = idx['V203'], idx['V405']
def stat(xs):
    xs = sorted(abs(x) for x in xs)
    return f"max {xs[-1]*1000:.0f} ms, median {xs[len(xs)//2]*1000:.0f} ms, over 20 ms: {sum(x > 0.02 for x in xs)}"
pre = [O2[i]['start'] - O1[i]['start'] for i in range(i203)]
post = [O2[i]['start'] - (O1[i]['start'] + d) for i in range(i405 + 1, len(O2))]
print('before the new part (V001-V202) vs v1:', stat(pre))
print('after the new part (V406-V450) vs v1+delta:', stat(post))
for i in range(len(O2)):
    if (i < i203 and abs(pre[i]) > 0.02) or (i > i405 and abs(post[i - i405 - 1]) > 0.02):
        print('   moved', O2[i]['id'], round(O1[i]['start'], 3), '->', round(O2[i]['start'], 3), L[i]['text'])
# new part: monotonic, durations
bad = [O2[i]['id'] for i in range(i203, i405 + 1) if not (O2[i]['start'] > O2[i - 1]['start'])]
print('new part: lines', i405 - i203 + 1, '| first', O2[i203]['id'], round(O2[i203]['start'], 3), '| last', O2[i405]['id'],
      round(O2[i405]['start'], 3), '-', O2[i405].get('end'), '| not increasing:', bad)
gaps = sorted(((O2[i + 1]['start'] - O2[i]['start']), O2[i]['id'], L[i]['text']) for i in range(i203, i405 + 1))
print('shortest lines:', [(round(g, 2), a, t) for g, a, t in gaps[:5]])
print('longest lines:', [(round(g, 2), a, t) for g, a, t in gaps[-5:]])
# compare with recognised word starts (first word of each line) in the new recording
words = [(a + n0, re.sub(r'[^가-힣0-9A-Za-z]', '', w)) for s in W for a, b, w, p in s['words']]
diffs = []
for i in range(i203, i405 + 1):
    t = O2[i]['start']
    first = re.sub(r'[^가-힣0-9A-Za-z]', '', L[i]['say'].split()[0]) if L[i]['say'].split() else ''
    near = [a for a, w in words if abs(a - t) < 1.5 and first[:2] and w.startswith(first[:2])]
    if near:
        diffs.append((min(near, key=lambda a: abs(a - t)) - t, O2[i]['id'], L[i]['text']))
print('vs recognised first word (matched', len(diffs), 'of', i405 - i203 + 1, '):', stat([x for x, _, _ in diffs]))
for x, a, t in sorted(diffs, key=lambda z: -abs(z[0]))[:8]:
    print(f'   {a} {x*1000:+.0f} ms {t}')
