import json,sys
d=json.load(open(sys.argv[1]))
for n in sys.argv[2:]:
  x=d[int(n)]
  print('=====',n)
  for k in ('id','title','one','facts'): print(k, json.dumps(x[k],ensure_ascii=False))
  for i,y in enumerate(x['items']): print(i, json.dumps(y,ensure_ascii=False))
