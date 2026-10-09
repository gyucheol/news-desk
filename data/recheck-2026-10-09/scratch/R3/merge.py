import json,glob,sys
base='/home/user/news-desk/data/recheck-2026-10-09/'
inp=json.load(open(base+'in/R3.json'))
done={}
for f in sorted(glob.glob(base+'scratch/R3/b*.json')):
    for d in json.load(open(f)): done[d['id']]=d
docs=[done.get(x['id'],{"id":x['id'],"changed":False,"basis":"title","note":"아직 확인 전"}) for x in inp]
json.dump({"agent":"R3","searches_used":int(sys.argv[1]),"fetches_used":0,"docs":docs},open(base+'out/R3.json','w'),ensure_ascii=False,indent=1)
print(len(docs),sum(1 for d in docs if d['changed']))
