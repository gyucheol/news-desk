import json, re, sys
p = sys.argv[1]
d = json.load(open(p))
TAIL = re.compile(r' \((제목 기준|채널 전언)\)$')
def plain(s): return s.replace('{{','').replace('}}','')
def strip_tail(s): return TAIL.sub('', s)
def ratio(s):
    s2 = strip_tail(s)
    tot = len(plain(s2)); emp = sum(len(m) for m in re.findall(r'\{\{(.*?)\}\}', s2))
    return round(emp / tot * 100) if tot else 0
def chunk_issues(s, label):
    out = []
    if re.search(r'\{\{[^}]*\{\{', s): out.append(label+': nested')
    if s.count('{{') != s.count('}}'): out.append(label+': unbalanced')
    for m in re.findall(r'\{\{(.*?)\}\}', s):
        if len(m) > 30: out.append(label+': chunk>30 [%s]' % m)
        if m != m.strip(): out.append(label+': chunk space [%s]' % m)
        if m and (m[0] in ",.'\"‘’“”" or m[-1] in ",.'\"‘’“”"): out.append(label+': chunk punct [%s]' % m)
    if re.search(r'\{\{[^}]*\((제목 기준|채널 전언)\)', s): out.append(label+': tail inside')
    return out
for x in d['items']:
    multi = len(x['items']) >= 2 or bool(x['attachTo'])
    lo, hi = (90, 160) if multi else (80, 130)
    tl = len(plain(x['title'])); ol = len(plain(strip_tail(x['one'])))
    iss = []
    if not 20 <= tl <= 50: iss.append('title len %d' % tl)
    if not lo <= ol <= hi: iss.append('one len %d (%d-%d)' % (ol, lo, hi))
    if not strip_tail(x['one']).endswith('다'): iss.append('one not ~다')
    if x['basis'] == 'title' and not x['one'].endswith(' (제목 기준)'): iss.append('one missing title tail')
    if x['basis'] == 'channel' and not x['one'].endswith(' (채널 전언)'): iss.append('one missing channel tail')
    if x['basis'] in ('verified','partial') and TAIL.search(x['one']): iss.append('one has tail but basis %s' % x['basis'])
    iss += chunk_issues(x['title'], 'title') + chunk_issues(x['one'], 'one')
    if not 2 <= len(x['facts']) <= 5: iss.append('facts count %d' % len(x['facts']))
    if not x['facts'][0].startswith('무엇이:'): iss.append('facts[0] not 무엇이')
    for f in x['facts']:
        if '|' in f or '**' in f or '{{' in f: iss.append('bad char in fact')
        if not re.search(r'\[(사실|채널|제목|추론|미확인)\]$', f): iss.append('fact tag missing: ' + f[-12:])
    if '{{' in x['check']: iss.append('braces in check')
    for k in ('inds','nodes'):
        if not isinstance(x[k], list): iss.append(k+' not list')
    for n in x['nodes']:
        if n.split('/')[0] not in x['inds']: iss.append('node ind missing ' + n)
    rs = [ratio(x['title']), ratio(x['one'])]
    if multi:
        a = x.get('added','')
        al = len(plain(strip_tail(a)))
        if not a.startswith('이번 '): iss.append('added not 이번')
        if not 60 <= al <= 140: iss.append('added len %d' % al)
        if not strip_tail(a).endswith('다'): iss.append('added not ~다')
        iss += chunk_issues(a, 'added'); rs.append(ratio(a))
    else:
        if x.get('added'): iss.append('added should be absent')
    prev = ''
    for it in x['items']:
        if '{{' in it['t']: iss.append('braces in t')
        if not 25 <= len(it['t']) <= 60: iss.append('t len %d: %s' % (len(it['t']), it['t']))
        if not re.match(r'^2026-\d\d-\d\d$', it['d']): iss.append('bad d')
        if it['d'] < prev: iss.append('items not sorted')
        prev = it['d']
        if multi:
            s = it.get('s','')
            sl = len(plain(strip_tail(s)))
            if not 45 <= sl <= 110: iss.append('s len %d: %s' % (sl, plain(s)[:30]))
            if not strip_tail(s).endswith('다'): iss.append('s not ~다')
            iss += chunk_issues(s, 's'); rs.append(ratio(s))
        elif it.get('s'): iss.append('s should be absent')
    print(x['cid'], x['basis'], 'T%d O%d' % (tl, ol), 'emph%', rs, '; '.join(iss) if iss else 'OK')
print('items', len(d['items']), 'skipped', len(d['skipped']), 'searches', d['searches_used'], 'fetches', d['fetches_used'])
