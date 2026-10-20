import json,re,sys
d=json.load(open(sys.argv[1]))
tail=re.compile(r' \((제목 기준|채널 전언)\)$')
L=lambda s: len(tail.sub('',s))
for x in d['items']:
    multi = len(x['items'])>1 or x['attachTo']
    lo,hi = (90,160) if multi else (80,130)
    p=[]
    t=len(x['title']); 
    if not 20<=t<=50: p.append(f"title {t}")
    o=L(x['one'])
    if not lo<=o<=hi: p.append(f"one {o}")
    if not x['one'].endswith('다'): p.append('one end')
    if not 2<=len(x['facts'])<=5: p.append('facts n')
    for f in x['facts']:
        if '|' in f or '**' in f or '{{' in f: p.append('bad char')
    if multi:
        a=L(x.get('added',''))
        if not 60<=a<=140: p.append(f"added {a}")
    for it in x['items']:
        if not 25<=len(it['t'])<=60: p.append(f"t {len(it['t'])} {it['t']}")
        if multi:
            s=L(it.get('s',''))
            if not 45<=s<=110: p.append(f"s {s} {it['s'][:30]}")
        elif 's' in it: p.append('s present single')
    ds=[it['d'] for it in x['items']]
    if ds!=sorted(ds): p.append('order')
    for v in x['vc']:
        if not 12<=len(v['t'])<=45: p.append(f"vc t {len(v['t'])}")
    print(x['cid'], t, o, p)
