import json,re,sys
d=json.load(open(sys.argv[1]))
def L(x):
    x=re.sub(r' \((제목 기준|채널 전언)\)$','',x); return len(x.replace('{{','').replace('}}',''))
def R(x):
    x=re.sub(r' \((제목 기준|채널 전언)\)$','',x); p=x.replace('{{','').replace('}}','')
    e=sum(len(m) for m in re.findall(r'\{\{(.*?)\}\}',x)); big=max([len(m) for m in re.findall(r'\{\{(.*?)\}\}',x)]+[0])
    return f"{L(x)}c {e*100//max(1,len(p))}% max{big}"
for it in d['items']:
    print(it['cid'],'T',R(it['title']),'O',R(it['one']))
    if it.get('added'): print('   A',R(it['added']))
    for s in it['items']:
        print('   t',len(s['t']), 'S',R(s['s']) if s.get('s') else '')
    for f in it['facts']:
        if '|' in f or '**' in f: print('BAD',f)
