import json,sys
for i in sys.argv[1:]:
    d=json.load(open(f'/home/user/news-desk/work/live42/news/{i}.json'))
    print('##',i,d.get('published','')[:10] if isinstance(d.get('published'),str) else '',d['title']); print('  one:',(d.get('one') or '')[:300].replace('\n',' / '))
    for it in d.get('items',[]): print('   -',(it.get('d'),it.get('o'),it.get('t')) if isinstance(it,dict) else str(it)[:120])
