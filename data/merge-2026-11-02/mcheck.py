"""합치기 2단계 출력 검사(여러 줄 요약 형식). 사용: python3 -I mcheck.py <출력 json>"""
import json, re, sys
d = json.load(open(sys.argv[1])); P = []
G = {g['gid']: g for g in json.load(open('/home/user/news-desk/data/merge-2026-11-02/groups.json'))}
for x in d:
    g = x.get('gid', '?')
    if g not in G: P.append(f'{g} groups.json에 없음'); continue
    if x.get('keep') != G[g]['keep'] or sorted(x.get('absorb', [])) != sorted(G[g]['absorb']): P.append(f'{g} keep·absorb가 groups.json과 다름')
    t = x.get('title', '')
    if not 20 <= len(t) <= 70: P.append(f'{g} 제목 {len(t)}자')
    L = x.get('one', '').split('\n')
    if not 4 <= len(L) <= 7: P.append(f'{g} 요약 {len(L)}줄')
    tail = re.compile(r' \((제목 기준|채널 전언)\)$')
    for i, l in enumerate(L):
        s = tail.sub('', l)
        if i == 0:
            if s.startswith('·') or not 40 <= len(s) <= 90: P.append(f'{g} 첫 줄 {len(s)}자')
        else:
            if not s.startswith('· '): P.append(f'{g} {i+1}째 줄 · 없음')
            elif not 25 <= len(s) - 2 <= 90: P.append(f'{g} {i+1}째 줄 {len(s)-2}자')
        if not s.rstrip().endswith('다'): P.append(f'{g} {i+1}째 줄 끝맺음')
        if '{{' in s or '**' in s: P.append(f'{g} 강조 기호')
    if tail.search(L[-1]) and x.get('basis') not in ('title', 'channel'): P.append(f'{g} 꼬리와 basis 불일치')
    if x.get('basis') == 'title' and not L[-1].endswith(' (제목 기준)'): P.append(f'{g} 제목 기준 꼬리 없음')
    if x.get('basis') == 'channel' and not L[-1].endswith(' (채널 전언)'): P.append(f'{g} 채널 전언 꼬리 없음')
    if x.get('basis') not in ('verified', 'partial', 'channel', 'title'): P.append(f'{g} basis')
    f = x.get('facts', [])
    if not 3 <= len(f) <= 6 or not f[0].startswith('무엇이:'): P.append(f'{g} facts 형식')
    if any('|' in s or '**' in s for s in f): P.append(f'{g} facts 기호')
    if not x.get('check'): P.append(f'{g} check 없음')
    if not 40 <= len(x.get('added', '')) <= 140: P.append(f'{g} added {len(x.get("added",""))}자')
print('묶음', len(d), '문제', len(P)); [print(' -', p) for p in P]
