import json,re,sys
d=json.load(open(sys.argv[1]))
T=re.compile(r' \((제목 기준|채널 전언)\)$')
def st(x):
    x=T.sub('',x); plain=x.replace('{{','').replace('}}','')
    em=sum(len(m) for m in re.findall(r'\{\{(.*?)\}\}',x))
    big=[m for m in re.findall(r'\{\{(.*?)\}\}',x) if len(m)>30 or m!=m.strip()]
    return len(plain), round(em/max(1,len(plain))*100), big
for it in d['items']:
    multi = len(it['items'])>1 or it['attachTo']
    print(it['cid'],'T',st(it['title']),'O',st(it['one']),'range', '90-160' if multi else '80-130')
    if 'added' in it: print('   A',st(it['added']))
    for s in it['items']:
        if 's' in s: print('   s',st(s['s']), len(s['t']))
        else: print('   t',len(s['t']))
