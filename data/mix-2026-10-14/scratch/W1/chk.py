import json,re,sys
d=json.load(open(sys.argv[1]))
def L(x): return len(re.sub(r' \((제목 기준|채널 전언)\)$','',x).replace('{{','').replace('}}',''))
def R(x):
    x=re.sub(r' \((제목 기준|채널 전언)\)$','',x)
    em=sum(len(m) for m in re.findall(r'\{\{(.*?)\}\}',x)); tot=len(x.replace('{{','').replace('}}',''))
    mx=max([len(m) for m in re.findall(r'\{\{(.*?)\}\}',x)]+[0])
    return f"{em/tot:.2f} max{mx}"
for it in d['items']:
    print(it['cid'],'T',L(it['title']),R(it['title']),'O',L(it['one']),R(it['one']), 'A',(L(it['added']),R(it['added'])) if 'added' in it else '-')
    for s in it['items']:
        if 's' in s: print('   s',L(s['s']),R(s['s']),'t',len(s['t']))
        else: print('   t',len(s['t']))
