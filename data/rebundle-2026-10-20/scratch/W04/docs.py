import json,sys
d=json.load(open('/home/user/news-desk/data/rebundle-2026-10-20/win/W04.json'))
cl=d['clusters']
for i in range(int(sys.argv[1]),int(sys.argv[2])):
    c=cl[i]; print('#####',c['c'])
    for k in c['docs']:
        x=d['docs'][k]
        print('--',k,'basis',x.get('basis'),'|',x.get('title'))
        print('  one:',x.get('one'))
        for f in x.get('facts',[]): print('  f:',f)
        print('  check:',x.get('check'))
        for s in x.get('src',[]): print('  src:',s.get('k'),'|',{kk:v for kk,v in s.items() if kk!='k'})
        print('  vc:',json.dumps(x.get('vc'),ensure_ascii=False))
        if x.get('fed'): print('  fed:',json.dumps(x.get('fed'),ensure_ascii=False))
