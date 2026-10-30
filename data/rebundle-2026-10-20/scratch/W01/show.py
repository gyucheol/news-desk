import json,sys
d=json.load(open('/home/user/news-desk/data/rebundle-2026-10-20/win/W01.json'))
a,b=int(sys.argv[1]),int(sys.argv[2])
seen=set()
for c in d['clusters'][a:b]:
    print('=====',c['c'],c['theme']); print('CORE:',c['core'])
    for it in c['items']: print(' -',it['o'],it['d'],'|',it['t'],'|S:',it['s'],'|',it['u'])
    for di in c['docs']:
        x=d['docs'][di]
        print(' DOC',di,'basis',x.get('basis'),'|',x.get('title'))
        print('   one:',x.get('one'))
        for f in x.get('facts',[]): print('   f:',f)
        print('   check:',x.get('check'))
        for s in x.get('src',[]): print('   src:',json.dumps(s,ensure_ascii=False)[:300])
        print('   vc:',json.dumps(x.get('vc'),ensure_ascii=False))
        if x.get('fed'): print('   fed:',json.dumps(x.get('fed'),ensure_ascii=False))
