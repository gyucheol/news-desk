import json,sys
d=json.load(open('/home/user/news-desk/data/rebundle-2026-10-20/win/W03.json'))
for i in map(int,sys.argv[1:]):
    c=d['clusters'][i]
    print('=====',i,c['c'],c['theme']); print('CORE:',c['core'])
    for it in c['items']: print(' *',it['d'],it['o'],'|',it['t'],'|S:',it['s'],'|',it['u'])
    for k in c['docs']:
        x=d['docs'][k]; print(' --DOC',k,'basis=',x.get('basis'),'inds=',x.get('inds'),x.get('nodes'))
        print('   T:',x['title']); print('   O:',x.get('one'))
        for f in x.get('facts',[]): print('   F:',f)
        print('   C:',x.get('check'))
        for s in x.get('src',[]): print('   S:',s['k'],s['o'],s['d'],s['u'][:90])
        if x.get('vc'): print('   VC:',json.dumps(x['vc'],ensure_ascii=False))
        if x.get('fed'): print('   FED:',json.dumps(x['fed'],ensure_ascii=False))
