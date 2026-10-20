import json,sys
d=json.load(open(sys.argv[1]))
for x in d:
    if x['id'] not in sys.argv[2:]: continue
    print('==',x['id']); print('T:',x['title']); print('O:',x['one']); print('F:',json.dumps(x['facts'],ensure_ascii=False)); print('B:',x.get('basis'))
    for k,i in enumerate(x['items']):
        print(f" [{k}]{'*NEW*' if i.get('new') else ''} {i.get('o')} {i.get('d')} | {i.get('t')}")
        if i.get('text'): print('    TEXT:', i['text'].replace('\n',' ')[:700])
