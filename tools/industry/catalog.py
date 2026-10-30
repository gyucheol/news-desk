"""산업·노드 목록(nodes.md)을 만든다. 밸류체인 한 줄(vc)을 쓰는 에이전트와 mk_mix 검사가 이 목록을 기준으로 한다.
사용: python3 -I tools/industry/catalog.py <chains 폴더> [<chains 폴더> ...]  (뒤 폴더가 같은 id를 덮어씀)
결과: tools/industry/nodes.md, tools/industry/nodes.json({산업 id: [노드 id, ...]})"""
import json, glob, os, re, sys
H = os.path.dirname(os.path.abspath(__file__))
P = lambda s: re.sub(r'\s*\[(사실|귀납|연역|유추|추측)[^\]]*\]', '', re.sub(r'\{\{|\}\}', '', s or '')).strip()
pages = {}
for d in sys.argv[1:]:
    for f in glob.glob(os.path.join(d, '*.json')):
        c = json.load(open(f))
        pages[c.get('id') or os.path.basename(f)[:-5]] = c
order = sorted(pages.values(), key=lambda c: (c.get('order', 99), c['id']))
out = ['# 산업·노드 목록 (자동 생성: tools/industry/catalog.py — 손으로 고치지 않습니다)\n',
       '밸류체인 한 줄(vc)의 ind·node는 이 목록에 있는 것만 씁니다. 형식: 노드 id — 이름: 역할\n']
for c in order:
    out.append(f"\n## {c['id']} — {c.get('name', '')} ({c.get('short', '')})\n")
    for n in c.get('nodes', []):
        role = P(n.get('role', ''))
        out.append(f"- {n['id']} — {n.get('name', '')}: {role[:110]}{'…' if len(role) > 110 else ''}\n")
open(os.path.join(H, 'nodes.md'), 'w').write(''.join(out))
json.dump({c['id']: [n['id'] for n in c.get('nodes', [])] for c in order}, open(os.path.join(H, 'nodes.json'), 'w'), ensure_ascii=False, indent=0)
print(len(order), 'industries,', sum(len(c.get('nodes', [])) for c in order), 'nodes')
