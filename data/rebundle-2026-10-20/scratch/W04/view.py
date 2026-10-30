import json,sys
d=json.load(open('/home/user/news-desk/data/rebundle-2026-10-20/win/W04.json'))
a,b=int(sys.argv[1]),int(sys.argv[2])
for c in d['clusters'][a:b]:
    print('=====',c['c'],'|',c['theme'],'| docs',c['docs'])
    for x in c['core']: print('  core:',x)
    for it in c['items']: print('  -',it['d'],it['o'],'|',it['t'],'|| s:',it['s'],'|',it['u'])
