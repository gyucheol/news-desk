import json,sys
d=json.load(open('/home/user/news-desk/data/rebundle-2026-10-20/win/W02.json'))
i=int(sys.argv[1])
c=d['clusters'][i]
print('==',c['c'],c['theme']); print('core:',c['core']); print('docs:',c['docs'])
for it in c['items']: print('-',it['d'],it['o'],'|',it['t'],'|S:',it['s'],'|',it['u'])
for k in c['docs']:
    x=d['docs'][k]; print('## DOC',k,x['title']); print(' one:',x['one']); 
    for f in x['facts']: print(' f:',f)
    print(' check:',x.get('check')); print(' basis:',x.get('basis'))
    for s in x.get('src',[]): print(' src:',s)
    print(' vc:',x.get('vc'),'inds',x.get('inds'),x.get('nodes')); 
    if x.get('fed'): print(' fed:',x['fed'])
    print(' other keys', [k2 for k2 in x if k2 not in ('title','one','facts','check','basis','src','vc','fed')])
