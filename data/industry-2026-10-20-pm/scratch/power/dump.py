import json,sys
for l in open(sys.argv[1]):
    r=json.loads(l)
    print('##',r['id'],r['d'],'upd' if r.get('upd') else '', '|',r['title'])
    print(' one:',r.get('one'))
    if r.get('added'): print(' added:',str(r['added'])[:600])
    f=r.get('facts');
    if f: print(' facts:',(' / '.join(f) if isinstance(f,list) else str(f))[:900])
    print(' vc:',r.get('vc'))
    print(' src:',' ; '.join(f"{s.get('o')}|{s.get('d')}|{s.get('u')}" for s in r.get('src',[])))
