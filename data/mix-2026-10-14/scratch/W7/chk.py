import json,re,sys
d=json.load(open(sys.argv[1]))
tail=re.compile(r' \((제목 기준|채널 전언)\)$')
def L(x): return len(tail.sub('',x).replace('{{','').replace('}}',''))
def R(x):
    x=tail.sub('',x); plain=x.replace('{{','').replace('}}','')
    em=sum(len(m) for m in re.findall(r'\{\{(.*?)\}\}',x))
    bad=[m for m in re.findall(r'\{\{(.*?)\}\}',x) if len(m)>30 or m!=m.strip()]
    nest='{{{' in x or re.search(r'\{\{[^}]*\{\{',x)
    return f"{em/len(plain):.2f}"+(' BAD'+str(bad) if bad else '')+(' NEST' if nest else '')
for c in d['items']:
    multi=len(c['items'])>1 or c['attachTo']
    lo,hi=(90,160) if multi else (80,130)
    print(c['cid'],'title',L(c['title']),R(c['title']),'one',L(c['one']),f'[{lo}-{hi}]',R(c['one']),'facts',len(c['facts']))
    if 'added' in c: print('   added',L(c['added']),R(c['added']))
    for it in c['items']:
        print('   t',len(it['t']), ('s %d %s'%(L(it['s']),R(it['s']))) if 's' in it else '')
    for f in c['facts']:
        if '|' in f or '**' in f or '{{' in f: print('BADFACT',f)
