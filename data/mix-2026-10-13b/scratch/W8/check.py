import json,re,sys
d=json.load(open(sys.argv[1]))
def L(x): return len(re.sub(r' \((제목 기준|채널 전언)\)$','',x).replace('{{','').replace('}}',''))
def spans(x): return re.findall(r'\{\{(.*?)\}\}',x)
for it in d['items']:
    multi = len(it['items'])>1 or it['attachTo']
    p=[]
    t=L(it['title']); o=L(it['one'])
    if not 20<=t<=50: p.append(f'title{t}')
    lo,hi=(90,160) if multi else (80,130)
    if not lo<=o<=hi: p.append(f'one{o}')
    if not 1<=it['title'].count('{{')<=2: p.append('tb')
    if not 2<=it['one'].count('{{')<=4: p.append('ob')
    for s in spans(it['title'])+spans(it['one'])+spans(it.get('added','')):
        if not 2<=len(s)<=20: p.append('span:'+s)
    if not 2<=len(it['facts'])<=5: p.append('facts')
    if not it['facts'][0].startswith('무엇이:'): p.append('f0')
    for f in it['facts']:
        if '|' in f or '**' in f or '{{' in f: p.append('fchar')
    if not it['one'].endswith('다') and not re.search(r'\((제목 기준|채널 전언)\)$',it['one']): p.append('oend')
    if multi:
        a=it.get('added','')
        if not 60<=L(a)<=140: p.append(f'added{L(a)}')
        if not 1<=a.count('{{')<=3: p.append('ab')
        for x in it['items']:
            s=x.get('s','')
            if not 45<=L(s)<=110: p.append(f"s{L(s)}:{s[:15]}")
            if not 1<=s.count('{{')<=2: p.append('sb')
            for sp in spans(s):
                if not 2<=len(sp)<=20: p.append('sspan:'+sp)
    else:
        if 'added' in it or any('s' in x for x in it['items']): p.append('extra s/added')
    for x in it['items']:
        if not 25<=len(x['t'])<=60: p.append(f"t{len(x['t'])}:{x['t'][:15]}")
    ds=[x['d'] for x in it['items']]
    if ds!=sorted(ds): p.append('order')
    print(it['cid'],t,o,p)
print('skipped',d['skipped'])
