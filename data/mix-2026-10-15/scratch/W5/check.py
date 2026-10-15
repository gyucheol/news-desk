import json,re,sys
d=json.load(open(sys.argv[1])); b=open(sys.argv[2]).read()
burls=set(re.findall(r'https://\S+',b))
tail=lambda x: re.sub(r' \((제목 기준|채널 전언)\)$','',x)
for x in d['items']:
    multi=len(x['items'])>1 or x['attachTo']
    o=len(tail(x['one'])); lo,hi=(90,160) if multi else (80,130)
    p=[]
    if not(20<=len(x['title'])<=50): p.append(('title',len(x['title'])))
    if not(lo<=o<=hi): p.append(('one',o))
    if not(2<=len(x['facts'])<=5): p.append('facts n')
    if multi:
        a=len(tail(x['added']))
        if not(60<=a<=140): p.append(('added',a))
    for i in x['items']:
        if i['u'] not in burls: p.append(('url',i['u']))
        if not(25<=len(i['t'])<=60): p.append(('t',len(i['t']),i['t']))
        if multi:
            s=len(tail(i['s']))
            if not(45<=s<=110): p.append(('s',s,i['s'][:30]))
    for v in x['vc']:
        if not(12<=len(v['t'])<=45): p.append(('vc',len(v['t'])))
    if '{{' in json.dumps(x,ensure_ascii=False) or '**' in json.dumps(x,ensure_ascii=False): p.append('emph')
    print(x['cid'],len(x['items']),p)
print(len(burls), sum(len(x['items']) for x in d['items']))
