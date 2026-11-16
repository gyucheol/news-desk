import json, sys
base='/home/user/news-desk/work/live52/news/'
full = '-v' in sys.argv
for i in [a for a in sys.argv[1:] if not a.startswith('-')]:
    try:
        d=json.load(open(base+i+'.json'))
    except Exception as e:
        print(i,'ERR',e); continue
    its=d.get('items',[])
    ds=sorted(x.get('d','') for x in its)
    print(f"== {i} | n={len(its)} range={ds[0] if ds else ''}~{ds[-1] if ds else ''}")
    print('  T:',d.get('title'))
    if full:
        print('  ONE:',(d.get('one') or '').replace('\n',' / ')[:600])
        for x in its[-8:]:
            print('   -',x.get('d'),'|',(x.get('t') or '')[:110])
