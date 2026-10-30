"""데스크 뉴스 문서의 '자세한 정리(detail) + 투자 인사이트(insight2)'를 마크다운 파일로 옮긴다.
사용: python3 -I tools/insight/to_md.py <출력 폴더> <뉴스 json> [<뉴스 json> ...]
강조 {{ }}는 떼고(2026-10-15 사용자 지시), 꼬리표 {f:사실} 등은 [사실] 꼴로, 링크는 그대로 둔다. 굵은 글씨는 쓰지 않는다."""
import json, os, re, sys
TAG = {'f': '사실', 'p': '회사 발표', 'a': '증권사', 'i': '추론', 'u': '미확인'}
def t(s):
    s = re.sub(r'\{\{|\}\}', '', str(s or ''))
    s = re.sub(r'\s*\{([fpaiu]):([^{}]+)\}', lambda m: ' [' + m.group(2) + ']', s)
    return s.strip()
def blocks(bs, lv=2):
    out = []
    H = lambda n: '#' * min(n, 6) + ' '
    for b in bs or []:
        k = b.get('k')
        if k == 'h3': out += ['', H(lv) + t(b['t']), '']
        elif k == 'h4': out += ['', H(lv + 1) + t(b['t']), '']
        elif k in ('lead', 'p', 'dim'): out += [t(b['t']), '']
        elif k == 'callout': out += ['> ' + t(b['t']), '']
        elif k == 'legend': out += ['꼬리표: [사실] 보도·공시로 확인, [회사 발표] 회사 계획·발언, [증권사] 분석 기관 견해, [추론] Claude의 판단, [미확인] 원문 확인 못 함', '']
        elif k in ('pts', 'src'): out += ['- ' + t(x) for x in b.get('items', [])] + ['']
        elif k == 'num': out += [f'{i}. ' + t(x) for i, x in enumerate(b.get('items', []), 1)] + ['']
        elif k == 'chain': out += [' → '.join(t(x) for x in b.get('items', [])), '']
        elif k == 'vc':
            if b.get('label'): out += [t(b['label']), '']
            for c in b.get('cols', []):
                out.append('- ' + t(c.get('h')) + (' (' + t(c.get('tag') or '이번 변화') + ')' if c.get('here') else ''))
                for x in c.get('items', []):
                    out.append('  - ' + (t(x) if isinstance(x, str) else ((t(x.get('b')) + ' ') if x.get('b') else '') + t(x.get('t'))))
            out.append('')
        elif k == 'seg': out += ['- ' + t(x.get('nm')) + ' — ' + t(x.get('stage')) + ': ' + t(x.get('why')) for x in b.get('items', [])] + ['']
        elif k == 'hyps':
            for x in b.get('items', []):
                out += ['', H(lv + 1) + t(x.get('kicker')) + ' — ' + t(x.get('h')), '']
                out += ['- ' + t(p[0]) + ': ' + t(p[1]) for p in x.get('kv', [])] + ['']
        elif k == 'verdict': out += ['- ' + t(x.get('h')) + ': ' + t(x.get('t')) for x in b.get('items', [])] + ['']
        elif k in ('cmp', 'series'): out += ['- ' + t(p[0]) + ': ' + t(p[1]) for p in b.get('items', [])] + ['']
        elif k == 'picks': out += ['- ' + t(x.get('k')) + ' · ' + t(x.get('n')) + ': ' + t(x.get('t')) for x in b.get('items', [])] + ['']
        elif k == 'co':
            out += ['', H(lv + 1) + t(b.get('name')) + (' (' + t(b.get('tk')) + ')' if b.get('tk') else ''), '']
            if b.get('px'): out += [t(b['px']), '']
            if b.get('role'): out += ['역할: ' + t(b['role']), '']
            for p in b.get('parts', []):
                out += ['', H(lv + 2) + t(p.get('h')), ''] + blocks(p.get('blocks'), lv + 3)
        elif b.get('t'): out += [t(b['t']), '']
    return out
OUT = sys.argv[1]
for p in sys.argv[2:]:
    n = json.load(open(p)); n = n.get('data', n) if isinstance(n.get('data'), dict) else n
    d, ins = n.get('detail') or {}, n.get('insight2') or {}
    upd = (n.get('updatedAt') or '')[:10]
    L = ['# ' + t(n.get('title')), '',
         f"뉴스 id {n['id']} · 자세한 정리 작성 {d.get('updated', '')} · 투자 인사이트 작성 {ins.get('updated', '')}", '',
         '한줄 요약: ' + t(n.get('one')), '']
    if upd and d.get('updated') and upd > d['updated']:
        L += [f"> 이 문서에는 {upd}에 새 기사가 더해졌습니다. 아래 정리와 인사이트는 {d['updated']} 기준이라 그 뒤 더해진 기사는 반영되지 않았습니다.", '']
    L += ['', '# 자세한 정리', ''] + blocks(d.get('blocks'))
    for part in ins.get('parts', []):
        L += ['', '# ' + t(part.get('tag')) + ' — ' + t(part.get('title')), '']
        if part.get('sub'): L += [t(part['sub']), '']
        L += blocks(part.get('blocks'))
    its = n.get('items') or []
    if its:
        L += ['', '# 원문 목록', ''] + [f"- {x.get('d', '')} {x.get('o', '')} — [{t(x.get('t'))}]({x.get('u')})" for x in its]
    L += ['', '---', '투자 권유가 아닌 관찰 기록입니다. 블룸버그·로이터 원문은 직접 읽지 못해 독립 매체와 1차 출처로 확인했습니다.', '']
    txt = re.sub(r'\n{3,}', '\n\n', '\n'.join(L))
    f = os.path.join(OUT, n['id'] + '.md'); open(f, 'w').write(txt)
    print(f, len(txt), txt.count('{{'), txt.count('**'))
