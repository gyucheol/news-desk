"""개편 시안(design/redesign-preview.html)의 도시바 HDD 예시(3~5단계)를 데스크의 blocks 형식으로 옮긴다."""
import json, sys, re
from bs4 import BeautifulSoup, NavigableString, Tag
soup = BeautifulSoup(open(sys.argv[1], encoding='utf-8').read(), 'html.parser')
def inl(node, skip_first_b=False):
    out = []; first = True
    for c in node.children:
        if isinstance(c, NavigableString): out.append(str(c)); continue
        cls = c.get('class') or []
        if c.name == 'span' and 'lb' in cls:
            k = [x for x in cls if x != 'lb'][0]; out.append(' {%s:%s}' % (k, c.get_text(strip=True)))
        elif c.name == 'a': out.append('[%s](%s)' % (c.get_text(strip=True), c['href']))
        elif c.name == 'br': out.append(' ')
        elif c.name == 'b' and skip_first_b and first: pass
        else: out.append(inl(c))
        if c.name == 'b': first = False
    s = re.sub(r'\s+', ' ', ''.join(out)).strip()
    return re.sub(r'\s+\{', ' {', s)
def blocks(parent):
    out = []
    for c in parent.children:
        if not isinstance(c, Tag): continue
        cls = c.get('class') or []
        if c.name == 'div' and 'block' in cls and 'verdict' in cls:
            out.append({'k': 'verdict', 'items': [{'tone': ' '.join(x for x in (v.get('class') or []) if x != 'v'), 'h': inl(v.h4), 't': inl(v.p)} for v in c.find_all('div', class_='v', recursive=False)]})
        elif c.name == 'div' and 'block' in cls: out += blocks(c)
        elif c.name == 'p' and 'legend' in cls: continue
        elif c.name == 'label': continue
        elif c.name in ('h3', 'h4'): out.append({'k': c.name, 't': inl(c)})
        elif c.name == 'p' and 'lead' in cls: out.append({'k': 'lead', 't': inl(c)})
        elif c.name == 'p' and 'chain' in cls: out.append({'k': 'chain', 'items': [inl(s) for s in c.find_all('span', recursive=False)]})
        elif c.name == 'p' and 'callout' in cls: out.append({'k': 'callout', 't': inl(c)})
        elif c.name == 'p' and 'dim' in cls: out.append({'k': 'dim', 't': inl(c)})
        elif c.name == 'p': out.append({'k': 'p', 't': inl(c)})
        elif c.name == 'span' and 'role' in cls: continue
        elif c.name == 'ul' and 'pts' in cls: out.append({'k': 'pts', 'items': [inl(l) for l in c.find_all('li', recursive=False)]})
        elif c.name == 'ol' and 'num' in cls: out.append({'k': 'num', 'items': [inl(l) for l in c.find_all('li', recursive=False)]})
        elif c.name == 'ul' and 'src' in cls: out.append({'k': 'src', 'items': [inl(l) for l in c.find_all('li', recursive=False)]})
        elif c.name == 'ul' and 'seg' in cls:
            out.append({'k': 'seg', 'items': [{'nm': inl(l.find(class_='nm')), 'stage': inl(l.find(class_='stage')), 'tone': [x for x in l.find(class_='stage')['class'] if x != 'stage'][0], 'why': inl(l.find(class_='why'))} for l in c.find_all('li', recursive=False)]})
        elif c.name == 'ul' and 'cmp' in cls:
            out.append({'k': 'cmp', 'items': [[inl(s) for s in l.find_all('span', recursive=False)] for l in c.find_all('li', recursive=False)]})
        elif c.name == 'div' and 'vc' in cls:
            cols = []
            for col in c.find_all('div', class_='col', recursive=False):
                items = [{'b': l.b.get_text(strip=True), 't': inl(l, True)} if l.b else inl(l) for l in col.ul.find_all('li', recursive=False)]
                d = {'h': inl(col.h4), 'items': items}
                if 'here' in col['class']: d['here'] = True; d['tag'] = col.find(class_='here-tag').get_text(strip=True)
                cols.append(d)
            out.append({'k': 'vc', 'label': c.get('aria-label', ''), 'cols': cols})
        elif c.name == 'div' and 'hyps' in cls:
            its = []
            for a in c.find_all('article', recursive=False):
                dts = a.dl.find_all('dt'); dds = a.dl.find_all('dd')
                its.append({'kicker': inl(a.find(class_='k')), 'h': inl(a.h4), 'kv': [[inl(x), inl(y)] for x, y in zip(dts, dds)]})
            out.append({'k': 'hyps', 'items': its})
        elif c.name == 'article' and 'co' in cls:
            role = c.find('span', class_='role')
            d = {'k': 'co', 'name': inl(c.find('h3')), 'tk': inl(c.find(class_='tk')), 'px': inl(c.find(class_='px')), 'role': inl(role), 'cond': 'cond' in role['class'],
                 'parts': [{'h': inl(dt.summary), 'blocks': blocks(dt.find('div', recursive=False))} for dt in c.find_all('details', recursive=False)]}
            out.append(d)
        elif c.name == 'dl' and 'series' in cls:
            out.append({'k': 'series', 'items': [[inl(r.dt), inl(r.dd)] for r in c.find_all('div', recursive=False)]})
        elif c.name == 'div' and 'picks' in cls:
            out.append({'k': 'picks', 'items': [{'k': inl(p.find(class_='k')), 'n': inl(p.find(class_='n')), 't': inl(p.p)} for p in c.find_all('div', class_='pick', recursive=False)]})
        else: raise SystemExit('모르는 요소: %s %s' % (c.name, cls))
    return out
def sec(i):
    s = soup.find(id=i); sh = s.find(class_='sh')
    return {'tag': sh.find(class_='tag').get_text(strip=True), 'title': inl(sh.h2), 'sub': inl(sh.find_all('p')[-1]) if len(sh.find_all('p')) > 1 else '', 'blocks': blocks(s.find(class_='panel'))}
d = sec('detail')
res = {'detail': {'updated': '2026-10-07', 'blocks': d['blocks']},
       'insight2': {'updated': '2026-10-07', 'parts': [dict(sec(i), id=n) for i, n in (('insight', 'structure'), ('flip', 'flip'), ('picks', 'picks'))]}}
for p in res['insight2']['parts']: p['tag'] = re.sub(r'^\d단계 · ', '', p['tag'])
json.dump(res, open(sys.argv[2], 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
txt = lambda h: re.sub(r'\s+', '', h)
# 대조: 변환한 글자 수와 원문 글자 수
src_chars = sum(len(txt(soup.find(id=i).find(class_='panel').get_text())) for i in ('detail', 'insight', 'flip', 'picks'))
out_chars = len(txt(re.sub(r'\{[fpaiu]:|\}|\]\(https?://[^)]+\)|\[', '', ' '.join(re.findall(r'"(?:t|h|nm|stage|why|kicker|name|tk|px|role|b|k|n)": "((?:[^"\\]|\\.)*)"', json.dumps(res, ensure_ascii=False))))))
print('blocks', len(res['detail']['blocks']), [len(p['blocks']) for p in res['insight2']['parts']], 'bytes', len(json.dumps(res, ensure_ascii=False).encode()), 'chars src/out', src_chars, out_chars)
