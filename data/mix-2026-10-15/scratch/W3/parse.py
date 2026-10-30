import re,json,sys
txt=open(sys.argv[1]).read()
out={}
cur=None
for line in txt.splitlines():
    m=re.match(r'^## (\S+) ',line)
    if m: cur=m.group(1); out[cur]=[]; continue
    m=re.match(r'^### (.+?) · (\d\d)-(\d\d) \d\d:\d\d KST · (\S+)',line)
    if m and cur:
        src=m.group(1).strip()
        o = src if src in ('블룸버그','로이터') else src
        out[cur].append({"o":o,"d":f"2026-{m.group(2)}-{m.group(3)}","u":m.group(4)})
json.dump(out,open(sys.argv[2],'w'),ensure_ascii=False,indent=0)
for k,v in out.items(): print(k,len(v),[x['o'] for x in v])
