import json,re
d=json.load(open('/home/user/news-desk/data/mix-2026-10-15/out2/W3.json'))
nodes=open('/home/user/news-desk/tools/industry/nodes.md').read()
valid={}
cur=None
for l in nodes.splitlines():
    m=re.match(r'^## (\w+) ',l)
    if m: cur=m.group(1); valid[cur]=set(); continue
    m=re.match(r'^- (\w+) —',l)
    if m and cur: valid[cur].add(m.group(1))
tail=lambda s: re.sub(r' \((제목 기준|채널 전언)\)$','',s)
def rng(name,s,a,b):
    n=len(tail(s))
    if not a<=n<=b: print('  BAD',name,n,'(',a,b,')',s[:40])
for x in d['items']:
    multi=len(x['items'])>1 or x['attachTo']
    print(x['cid'],len(x['title']),len(tail(x['one'])))
    rng('title',x['title'],20,50)
    rng('one',x['one'],90 if multi else 80,160 if multi else 130)
    if not x['one'].endswith('다'): print('  one ending')
    if not 2<=len(x['facts'])<=5: print('  facts n')
    for f in x['facts']:
        if '|' in f or '**' in f or '{{' in f: print('  bad char')
    if multi: rng('added',x.get('added',''),60,140)
    for it in x['items']:
        rng('t',it['t'],25,60)
        if multi: rng('s',it['s'],45,110)
    for v in x['vc']:
        rng('vc',v['t'],12,45)
        if v['ind'] not in valid or (v['node'] and v['node'] not in valid[v['ind']]): print('  bad vc node',v)
    for n in x['nodes']:
        i,nn=n.split('/'); 
        if i not in x['inds']: print('  inds missing',i)
    for f in x.get('fed',[]): rng('fed',f['t'],20,70)
