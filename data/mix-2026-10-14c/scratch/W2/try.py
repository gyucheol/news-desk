import re, sys
TAIL = re.compile(r' \((제목 기준|채널 전언)\)$')
for line in open(sys.argv[1], encoding='utf-8'):
    line=line.rstrip('\n')
    if not line.strip() or line.startswith('#'):
        continue
    body=TAIL.sub('', line)
    chunks=re.findall(r'\{\{(.*?)\}\}', body)
    total=len(body.replace('{{','').replace('}}',''))
    em=sum(len(c) for c in chunks)
    big=[c for c in chunks if len(c)>30]
    print('%3d %3.0f%% %s | %s' % (total, 100*em/total, ('BIG '+str(big)) if big else '', body[:60]))
