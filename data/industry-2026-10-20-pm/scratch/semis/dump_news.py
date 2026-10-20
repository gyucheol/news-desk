import json,sys
for l in open(sys.argv[1]):
    x=json.loads(l)
    print('=== ',x['id'],x['d'],'upd' if x.get('upd') else '')
    print('T:',x['title']); print('1:',x.get('one'))
    if x.get('added'): print('ADD:',x['added'])
    print('F:',x.get('facts')); print('VC:',x.get('vc'))
    print('S:',[(s.get('o'),s.get('d'),s.get('u')) for s in x.get('src') or []])
