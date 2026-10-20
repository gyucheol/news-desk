import json,sys
W=json.load(open('/home/user/news-desk/data/split-2026-10-20/win/W07.json'))
for did in sys.argv[1:]:
    d=W['docs'][did]
    print('#####',did)
    for k,v in d.items():
        if k in('facts','src','vc','fed'):
            print(k+':')
            for x in v: print('  ',json.dumps(x,ensure_ascii=False) if not isinstance(x,str) else x)
        else: print(k+':',v if isinstance(v,str) else json.dumps(v,ensure_ascii=False))
    for c in W['clusters']:
        if did in c['docs']:
            print('=== CL',c['c'],c['label'],c['docs'])
            for it in c['items']:
                print('  -',it['d'],it['o'],'|',it['t']); print('     s:',it['s']); print('     u:',it['u'])
