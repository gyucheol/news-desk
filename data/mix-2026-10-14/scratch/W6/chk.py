import json,re,sys
d=json.load(open(sys.argv[1]))
def strip(x): return re.sub(r' \((제목 기준|채널 전언)\)$','',x)
def m(x):
    s=strip(x); plain=s.replace('{{','').replace('}}','')
    em=sum(len(a) for a in re.findall(r'\{\{(.*?)\}\}',s))
    big=[a for a in re.findall(r'\{\{(.*?)\}\}',s) if len(a)>30]
    return f"{len(plain)}/{em*100//max(1,len(plain))}%"+(f" BIG{big}" if big else "")
for x in d['items']:
    print(x['cid'],'T',m(x['title']),'O',m(x['one']),'A',m(x.get('added','')) if x.get('added') else '-')
    for i in x['items']:
        print('   t',len(i['t']),'s',m(i['s']) if i.get('s') else '-')
