"""Validate an industry page JSON written per tools/industry/BUILD.md.
usage: python3 check.py <out.json> [<other out.json> ...]"""
import json, re, sys, os, glob

CHAINS = '/home/user/news-desk/work/live14/chains'
OUT = '/home/user/news-desk/data/industry-2026-10-14/out'
DATE = re.compile(r'^\d{4}-\d{2}-\d{2}$')
TAGS = ('[사실]', '[귀납]', '[유추]', '[추측]', '[연역]')

def known_nodes():
    k = {}
    for f in glob.glob(CHAINS + '/*.json') + glob.glob(OUT + '/*.json'):
        try:
            d = json.load(open(f))
            k[d['id']] = {n['id'] for n in d.get('nodes', [])}
        except Exception:
            pass
    return k

def emph(s):
    """return (ratio incl spaces, ratio excl spaces, problems)"""
    probs = []
    if s.count('{{') != s.count('}}'):
        probs.append('unbalanced braces')
    plain = s.replace('{{', '').replace('}}', '')
    chunks = re.findall(r'\{\{(.*?)\}\}', s)
    for c in chunks:
        if '{' in c or '}' in c:
            probs.append('nested: ' + c)
        if c != c.strip():
            probs.append('space edge: [' + c + ']')
        if len(c) > 30:
            probs.append('long chunk(%d): %s' % (len(c), c))
        if c and c[-1] in ',.:;':
            probs.append('punct end: ' + c)
        if any(t in c for t in TAGS):
            probs.append('tag inside: ' + c)
    tot = len(plain)
    em = sum(len(c) for c in chunks)
    tot_ns = len(plain.replace(' ', ''))
    em_ns = sum(len(c.replace(' ', '')) for c in chunks)
    return (em / tot if tot else 0, em_ns / tot_ns if tot_ns else 0, probs)

def main(paths):
    known = known_nodes()
    bad = 0
    def err(m):
        nonlocal bad
        bad += 1
        print('  ERROR:', m)
    for p in paths:
        print('==', p)
        d = json.load(open(p))
        for k in ['id','name','short','icon','order','asOf','rev','summary','intro','nodes','cycle','industryState','insight','flows','gaps','history']:
            if k not in d: err('missing top key ' + k)
        if len(d['short']) > 6: err('top short > 6: ' + d['short'])
        if d.get('insight') != {} or d.get('flows') != []: err('insight/flows must be {} / []')
        ids = [n['id'] for n in d['nodes']]
        if len(ids) != len(set(ids)): err('duplicate node ids')
        if not 5 <= len(ids) <= 9: err('node count %d' % len(ids))
        names = [n['name'] for n in d['nodes']]
        emph_fields = []  # (label, text, strict)
        emph_fields.append(('summary', d['summary'], True))
        it = d['intro']
        for k in ['what','money','drivers']:
            emph_fields.append(('intro.'+k, it[k], True))
        if not 3 <= len(it['watch']) <= 5: err('watch count')
        if not 5 <= len(it['players']) <= 8: err('players count')
        if not 3 <= len(it['reading']) <= 5: err('reading count')
        if not 3 <= len(it['terms']) <= 6: err('terms count')
        for w in it['watch']:
            if set(w) != {'n','why','where'}: err('watch keys %s' % w)
            if '{{' in json.dumps(w, ensure_ascii=False): err('emphasis in watch')
        for pl in it['players']:
            if set(pl) != {'n','t','m','role'}: err('player keys %s' % pl)
            if '{{' in json.dumps(pl, ensure_ascii=False): err('emphasis in players')
        for t in it['terms']:
            if set(t) != {'k','v'}: err('terms keys')
            if '{{' in json.dumps(t, ensure_ascii=False): err('emphasis in terms')
        for i, r in enumerate(it['reading']):
            if set(r) != {'news','means'}: err('reading keys')
            if '{{' in r['news']: err('emphasis in reading.news')
            if not any(nm in r['means'].replace('{{','').replace('}}','') for nm in names):
                err('reading[%d].means has no node name' % i)
            emph_fields.append(('reading[%d].means' % i, r['means'], True))
        for n in d['nodes']:
            nid = n['id']
            if not re.match(r'^[a-z]{2,12}$', nid): err('bad node id ' + nid)
            for k in ['id','name','short','role','bottleneck','indicators','companies','state']:
                if k not in n: err('%s missing %s' % (nid, k))
            if len(n['short']) > 6: err('%s short > 6: %s' % (nid, n['short']))
            if 'stage' in n and not (isinstance(n['stage'], int) and 1 <= n['stage'] <= 8): err(nid + ' bad stage')
            if not 2 <= len(n['indicators']) <= 3: err(nid + ' indicators count')
            if not 2 <= len(n['companies']) <= 5: err(nid + ' companies count %d' % len(n['companies']))
            if len(n['state']) > 3: err(nid + ' state > 3')
            emph_fields.append((nid+'.role', n['role'], True))
            emph_fields.append((nid+'.bottleneck', n['bottleneck'], False))
            if not any(t in n['bottleneck'] for t in TAGS): print('  note: %s bottleneck has no tag' % nid)
            for c in n['companies']:
                if set(c) - {'n','t','m','note'} or not {'n','t','m','note'} <= set(c): err('%s company keys %s' % (nid, c))
                emph_fields.append((nid+'.co.'+c['n'][:12], c['note'], False))
            for ind in n['indicators']:
                if set(ind) != {'n','src'}: err(nid + ' indicator keys')
            for l in n.get('links', []):
                to = l.get('to', '')
                if '/' not in to: err('%s bad link %s' % (nid, to)); continue
                ind_, node_ = to.split('/', 1)
                if ind_ not in known: print('  note: link target industry not built yet: ' + to)
                elif node_ not in known[ind_]: err('%s link target missing: %s' % (nid, to))
                if '{{' in l.get('why',''): err('emphasis in link why')
            for s in n['state']:
                for k in ['d','o','t','u']:
                    if not s.get(k): err('%s state missing %s' % (nid, k))
                if not DATE.match(s.get('d','')): err('%s state date %s' % (nid, s.get('d')))
                if not any(t in s['t'] for t in TAGS): err(nid + ' state no tag')
                emph_fields.append((nid+'.state', s['t'], False))
        c = d['cycle']
        if not (isinstance(c['stage'], int) and 1 <= c['stage'] <= 8): err('cycle.stage')
        if c['conf'] not in ('높음','중간','낮음'): err('cycle.conf')
        if not 2 <= len(c['why']) <= 4: err('why count')
        for w in c['why']:
            if not w.get('src'): err('why without src')
            for s in w.get('src', []):
                if not s.get('o') or not s.get('u'): err('why src missing o/u')
                if not DATE.match(s.get('d','')): err('why src date %s' % s.get('d'))
            if not any(t in w['t'] for t in TAGS): err('why no tag')
            emph_fields.append(('cycle.why', w['t'], False))
        emph_fields.append(('cycle.next', c['next'], False))
        if not any(t in c['next'] for t in TAGS): err('next no tag')
        if not 3 <= len(c['watch']) <= 5: err('cycle.watch count')
        for sp in c.get('split', []):
            if not 1 <= sp['stage'] <= 8: err('split stage')
            for x in sp['nodes']:
                if x not in ids: err('split node missing ' + x)
        if not 2 <= len(d['industryState']) <= 5: err('industryState count')
        for s in d['industryState']:
            for k in ['d','kind','o','t','u']:
                if not s.get(k): err('industryState missing ' + k)
            if s.get('kind') not in ('price','supply','demand','capex','policy'): err('industryState kind ' + str(s.get('kind')))
            if not DATE.match(s.get('d','')): err('industryState date ' + s.get('d',''))
            if '{{' in s['t']: print('  note: emphasis in industryState')
        # all src-like items: o and u
        def walk(x):
            if isinstance(x, dict):
                if 'src' in x and isinstance(x['src'], list):
                    for s in x['src']:
                        if not (s.get('o') and s.get('u')): err('src item missing o/u: %s' % s)
                for v in x.values(): walk(v)
            elif isinstance(x, list):
                for v in x: walk(v)
        walk(d)
        print('  emphasis ratios (incl spaces / excl spaces):')
        for lab, txt, strict in emph_fields:
            r1, r2, probs = emph(txt)
            flag = ''
            if strict and not (0.50 <= r1 <= 0.65): flag = '  <-- outside 50-65%'
            if not strict and '{{' in txt and not (0.40 <= r1 <= 0.75): flag = '  <-- check'
            print('   %-28s %4.0f%% %4.0f%%%s' % (lab, r1*100, r2*100, flag))
            for pr in probs: err('%s: %s' % (lab, pr))
        print('  nodes:', ids)
    print('ERRORS:', bad)

if __name__ == '__main__':
    main(sys.argv[1:])
