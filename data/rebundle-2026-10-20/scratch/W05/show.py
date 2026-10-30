import json,sys
d=json.load(open('/home/user/news-desk/data/rebundle-2026-10-20/win/W05.json'))
for c in d['clusters'][int(sys.argv[1]):int(sys.argv[2])]:
    print('#####',c['c'],c['theme']); print('CORE:',c['core'])
    for it in c['items']: print(' -',it['o'],it['d'],'|',it['t'],'|S:',it.get('s'),'|',it['u'])
    for k in c['docs']:
        x=d['docs'][k]; print('  DOC',k,'basis',x.get('basis'),'|',x['title']); print('   one:',x['one'])
        for f in x['facts']: print('   f:',f)
        print('   check:',x.get('check'))
        for s in x.get('src',[]): print('   src:',json.dumps(s,ensure_ascii=False)[:250])
        print('   vc:',json.dumps(x.get('vc'),ensure_ascii=False)[:300])
        if x.get('fed'): print('   fed:',json.dumps(x['fed'],ensure_ascii=False))
