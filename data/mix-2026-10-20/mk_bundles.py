"""clusters.json → bundle/W*.md (작성 에이전트 입력). 사용: python3 -I mk_bundles.py <DB 사본 폴더> <에이전트 수>"""
import json, sys
DB, N = sys.argv[1], int(sys.argv[2])
chan = json.load(open('chan.json'))['chan']
BANKS = json.load(open('/home/user/news-desk/tools/industry/fed_roster.json'))['banks']  # 연준 공식 출처(fed:<기관>) 표기
rows = {int(l.split('\t')[0]): l.rstrip('\n').split('\t') for l in open('all.tsv')}
cl = json.load(open('clusters.json'))['clusters']
# 글 수로 균형 있게 나눔(큰 묶음부터 가장 가벼운 에이전트에)
bins = [[] for _ in range(N)]; load = [0] * N
for c in sorted(cl, key=lambda c: -len(c['lines'])):
    i = load.index(min(load)); bins[i].append(c); load[i] += len(c['lines']) + 2
for i, b in enumerate(bins, 1):
    out = [f'# 묶음 파일 W{i} — 묶음 {len(b)}개\n']
    for c in sorted(b, key=lambda c: c['cid']):
        out.append(f"\n## {c['cid']} {c['theme']} (분야 {c['field']}) attachTo: \"{c.get('attachTo', '')}\"\n")
        if c.get('attachTo'):
            d = json.load(open(f"{DB}/news/{c['attachTo']}.json"))
            out.append(f"기존 문서 {d['id']} ({(d.get('published') or '')[:10]}, basis {d.get('basis', '')})\n- 제목: {d.get('title', '')}\n- 한줄: {d.get('one', '')}\n")
            for f in d.get('facts', []): out.append('- 사실: ' + f.replace('{{', '').replace('}}', '') + '\n')
            if d.get('added'): out.append(f"- 추가된 내용(직전): {d['added']}\n")
            its = d.get('items') or []
            if its:
                out.append(f'- 이미 묶인 원문 {len(its)}건(본문에 없는 핵심 내용이 있으면 사실·한줄에 반영):\n')
                cl = lambda x: (x or '').replace('{{', '').replace('}}', '')
                for it in its: out.append(f"  - {it.get('d', '')} {it.get('o', '')}: {cl(it.get('t'))}" + (f" — {cl(it['s'])}" if it.get('s') else '') + '\n')
        for ln in sorted(c['lines'], key=lambda n: rows[n][2]):
            r = rows[ln]; s = r[1]
            if s.startswith('tg:'):
                out.append(f"\n### 텔레그램 {chan.get(s[3:], s[3:])} · {r[2]} KST · {r[4]}\n{r[3][:1800]}\n")
            elif s.startswith('fed:'):
                out.append(f"\n### 연준 공식 {BANKS.get(s[4:], s[4:])} · {r[2]} KST · {r[4]}\n제목(발언자: 제목): {r[3]}\n")
            else:
                out.append(f"\n### {'블룸버그' if s == 'bbg' else '로이터'} · {r[2]} KST · {r[4]}\n제목: {r[3]}\n")
    open(f'bundle/W{i}.md', 'w').write(''.join(out))
    print(f'W{i}', len(b), '묶음', sum(len(c['lines']) for c in b), '글')
