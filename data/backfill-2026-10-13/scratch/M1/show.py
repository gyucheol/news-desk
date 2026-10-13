import json,sys
d=json.load(open(sys.argv[1]))
for x in d[int(sys.argv[2]):int(sys.argv[3])]:
    print('=====',x['id']); print('T:',x['title']); print('O:',x['one'])
    for f in x['facts']: print('F:',f)
    for k,i in enumerate(x.get('items',[])):
        print(f"  [{k}]{'*NEW*' if i['new'] else ''} {i['o']} {i['d']} | {i['t']}")
        if i.get('text'): print('     TEXT:',i['text'][:1200].replace('\n',' '))
