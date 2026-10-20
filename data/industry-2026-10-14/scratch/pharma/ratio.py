import re, sys
LBL = re.compile(r'\s*\[(사실|귀납|연역|유추|추측)[^\]]*\]\s*\.?\s*$')
def r(s):
    s = LBL.sub('', s)
    m = re.findall(r'\{\{(.+?)\}\}', s); p = s.replace('{{','').replace('}}','')
    return sum(map(len, m)) / len(p)
for line in sys.stdin.read().split('\n@@\n'):
    line = line.strip()
    if line: print(f"{r(line):.0%}  {line[:50]}")
