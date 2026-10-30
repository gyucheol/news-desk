import re, sys, json
def r(s):
    plain = s.replace('{{','').replace('}}','')
    ch = re.findall(r'\{\{(.*?)\}\}', s)
    return sum(len(c) for c in ch)/len(plain)
texts = json.load(open(sys.argv[1]))
for k, v in texts.items():
    print('%-14s %4.0f%%' % (k, r(v)*100))
