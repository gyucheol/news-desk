"""Validate an industry page JSON against BUILD.md section 2/3 and GUIDE-short.md emphasis rules.
usage: python3 check.py <page.json> [other_page.json ...]  (other pages are used only to resolve cross links)
"""
import json, re, sys, glob, os

CHAINS = '/home/user/news-desk/work/live14/chains'
EMPH = re.compile(r'\{\{(.*?)\}\}')
TAGS = re.compile(r'\[(사실|귀납|연역|유추|추측)\]')
DATE = re.compile(r'^\d{4}-\d{2}(-\d{2})?$')
BLOCKED = ('bloomberg.com', 'reuters.com', 'bnnbloomberg', 'marketscreener', 'tradingview.com', 'investing.com', 'msn.com', 'yahoo.com', 'usnews.com')

def known_nodes(extra_pages):
    ids = {}
    for f in glob.glob(os.path.join(CHAINS, '*.json')):
        d = json.load(open(f, encoding='utf-8'))
        ids[d['id']] = {n['id'] for n in d['nodes']}
    for p in extra_pages:
        d = json.load(open(p, encoding='utf-8'))
        ids[d['id']] = {n['id'] for n in d['nodes']}
    return ids

def plain(s):
    return s.replace('{{', '').replace('}}', '')

def ratio(s):
    body = TAGS.sub('', s)
    tot = len(re.sub(r'\s', '', plain(body)))
    em = sum(len(re.sub(r'\s', '', m)) for m in EMPH.findall(body))
    return em / tot if tot else 0

def chunk_errors(s, where):
    errs = []
    if s.count('{{') != s.count('}}'):
        errs.append(f'{where}: unbalanced braces')
    depth = 0
    for i in range(len(s) - 1):
        if s[i:i+2] == '{{':
            depth += 1
            if depth > 1:
                errs.append(f'{where}: nested braces'); break
        elif s[i:i+2] == '}}':
            depth -= 1
    for m in EMPH.findall(s):
        if not m or m != m.strip():
            errs.append(f'{where}: chunk with edge space/empty: [{m}]')
        if len(m) > 30:
            errs.append(f'{where}: chunk >30 chars ({len(m)}): [{m}]')
        if m and m[-1] in ',.\'"':
            errs.append(f'{where}: punctuation at chunk end: [{m}]')
    return errs

def main(path, others):
    d = json.load(open(path, encoding='utf-8'))
    errs, warns = [], []
    nodes = known_nodes(others)
    my_ids = [n['id'] for n in d['nodes']]
    nodes[d['id']] = set(my_ids)
    for k in ['id', 'name', 'short', 'icon', 'order', 'asOf', 'rev', 'summary', 'intro', 'nodes', 'cycle', 'industryState', 'insight', 'flows', 'gaps', 'history']:
        if k not in d: errs.append(f'missing top key {k}')
    if len(d['short']) > 6: errs.append(f"top short >6: {d['short']}")
    if d.get('insight') != {} or d.get('flows') != []: errs.append('insight/flows must be {} / []')
    # intro
    it = d['intro']
    for k in ['what', 'money', 'drivers']:
        r = ratio(it[k]); print(f'ratio intro.{k}: {r:.2f}')
        if not 0.50 <= r <= 0.65: warns.append(f'intro.{k} ratio {r:.2f} outside 0.50-0.65')
        errs += chunk_errors(it[k], f'intro.{k}')
    for k, lo, hi in [('watch', 3, 5), ('players', 5, 8), ('reading', 3, 5), ('terms', 3, 6)]:
        if not lo <= len(it[k]) <= hi: errs.append(f'intro.{k} count {len(it[k])} not in {lo}-{hi}')
    for k in ['watch', 'players', 'terms']:
        if '{{' in json.dumps(it[k], ensure_ascii=False): errs.append(f'intro.{k} must not contain {{{{ }}}}')
    for i, w in enumerate(it['watch']):
        for f in ['n', 'why', 'where']:
            if not w.get(f): errs.append(f'watch[{i}] missing {f}')
    for i, p in enumerate(it['players']):
        for f in ['n', 't', 'm', 'role']:
            if f not in p: errs.append(f'players[{i}] missing {f}')
    for i, r in enumerate(it['reading']):
        rr = ratio(r['means']); print(f'ratio reading[{i}].means: {rr:.2f}')
        if not 0.50 <= rr <= 0.65: warns.append(f'reading[{i}].means ratio {rr:.2f}')
        errs += chunk_errors(r['means'], f'reading[{i}].means')
        if not any(n['short'] in r['means'] or n['name'].split('(')[0] in r['means'] for n in d['nodes']):
            warns.append(f'reading[{i}].means names no node')
    # summary
    print(f"ratio summary: {ratio(d['summary']):.2f}")
    errs += chunk_errors(d['summary'], 'summary')
    # nodes
    if not 5 <= len(d['nodes']) <= 9: errs.append(f'node count {len(d["nodes"])}')
    if len(set(my_ids)) != len(my_ids): errs.append('duplicate node ids')
    for n in d['nodes']:
        nid = n['id']
        if not re.fullmatch(r'[a-z]{2,12}', nid): errs.append(f'bad node id {nid}')
        if len(n['short']) > 6: errs.append(f'{nid} short >6: {n["short"]}')
        for f in ['name', 'short', 'role', 'bottleneck', 'indicators', 'companies']:
            if not n.get(f): errs.append(f'{nid} missing {f}')
        if 'stage' in n and n['stage'] is not None and not 1 <= n['stage'] <= 8: errs.append(f'{nid} stage out of range')
        if not 2 <= len(n['indicators']) <= 3: errs.append(f'{nid} indicators {len(n["indicators"])}')
        if not 2 <= len(n['companies']) <= 5: errs.append(f'{nid} companies {len(n["companies"])}')
        if len(n.get('state', [])) > 3: errs.append(f'{nid} state >3')
        for f in ['role', 'bottleneck']:
            errs += chunk_errors(n[f], f'{nid}.{f}')
        print(f'ratio {nid}.role {ratio(n["role"]):.2f} bottleneck {ratio(n["bottleneck"]):.2f}')
        for c in n['companies']:
            for f in ['n', 't', 'm', 'note']:
                if f not in c: errs.append(f'{nid} company missing {f}: {c}')
            errs += chunk_errors(c.get('note', ''), f'{nid}.company {c.get("n")}')
        for l in n.get('links', []):
            ind, _, node = l['to'].partition('/')
            if ind not in nodes or node not in nodes[ind]:
                errs.append(f'{nid} link target unknown: {l["to"]}')
            if not l.get('why'): errs.append(f'{nid} link without why')
        for s in n.get('state', []):
            for f in ['d', 'o', 't', 'u']:
                if not s.get(f): errs.append(f'{nid} state missing {f}')
            if s.get('d') and not DATE.match(s['d']): errs.append(f'{nid} state bad date {s["d"]}')
            if not TAGS.search(s.get('t', '')): warns.append(f'{nid} state without tag')
            errs += chunk_errors(s.get('t', ''), f'{nid}.state')
            if any(b in s.get('u', '') for b in BLOCKED): errs.append(f'{nid} state blocked url {s["u"]}')
    # cycle
    c = d['cycle']
    if not isinstance(c.get('stage'), int) or not 1 <= c['stage'] <= 8: errs.append('cycle.stage not 1..8')
    if c.get('conf') not in ('높음', '중간', '낮음'): errs.append('cycle.conf')
    if not 2 <= len(c['why']) <= 4: errs.append(f'cycle.why count {len(c["why"])}')
    for i, w in enumerate(c['why']):
        if not w.get('src'): errs.append(f'cycle.why[{i}] no src')
        for s in w.get('src', []):
            if not s.get('o') or not s.get('u'): errs.append(f'cycle.why[{i}] src missing o/u: {s}')
            if s.get('d') and not DATE.match(s['d']): errs.append(f'cycle.why[{i}] bad date')
            if any(b in s.get('u', '') for b in BLOCKED): errs.append(f'cycle.why[{i}] blocked url')
        if not TAGS.search(w['t']): errs.append(f'cycle.why[{i}] no tag')
        errs += chunk_errors(w['t'], f'cycle.why[{i}]')
    if not TAGS.search(c.get('next', '')): errs.append('cycle.next no tag')
    errs += chunk_errors(c.get('next', ''), 'cycle.next')
    if not 3 <= len(c.get('watch', [])) <= 5: errs.append('cycle.watch count')
    for sp in c.get('split', []):
        if not 1 <= sp['stage'] <= 8: errs.append('split stage')
        for nn in sp['nodes']:
            if nn not in my_ids: errs.append(f'split node unknown {nn}')
    # industryState
    if not 2 <= len(d['industryState']) <= 5: errs.append('industryState count')
    for s in d['industryState']:
        if s.get('kind') not in ('price', 'supply', 'demand', 'capex', 'policy'): errs.append(f'industryState kind {s.get("kind")}')
        for f in ['d', 'o', 't', 'u']:
            if not s.get(f): errs.append(f'industryState missing {f}')
        if any(b in s.get('u', '') for b in BLOCKED): errs.append('industryState blocked url')
    # soft check: every emphasized free-text field
    soft = [('summary', d['summary']), ('cycle.next', c.get('next', ''))]
    soft += [(f'cycle.why[{i}]', w['t']) for i, w in enumerate(c['why'])]
    for n in d['nodes']:
        soft += [(f"{n['id']}.role", n['role']), (f"{n['id']}.bottleneck", n['bottleneck'])]
        soft += [(f"{n['id']}.state[{i}]", s['t']) for i, s in enumerate(n.get('state', []))]
        soft += [(f"{n['id']}.co:{co['n'][:10]}", co['note']) for co in n['companies'] if '{{' in co.get('note', '')]
    hi = [(k, ratio(v)) for k, v in soft if v and ratio(v) > 0.68]
    lo = [(k, ratio(v)) for k, v in soft if v and '{{' in v and ratio(v) < 0.40]
    print('soft >0.68:', ', '.join(f'{k}={r:.2f}' for k, r in hi) or 'none')
    print('soft <0.40:', ', '.join(f'{k}={r:.2f}' for k, r in lo) or 'none')
    print('nodes:', my_ids)
    print('ERRORS:', len(errs)); [print('  E', e) for e in errs]
    print('WARNINGS:', len(warns)); [print('  W', w) for w in warns]

if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2:])
