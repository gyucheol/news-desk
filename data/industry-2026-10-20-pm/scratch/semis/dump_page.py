import json,sys
c=json.load(open(sys.argv[1]))
print('SUMMARY',c.get('summary'))
for n in c['nodes']:
  print('NODE',n['id'],n.get('name') or n.get('label'),'stage',n.get('stage'),n.get('stageNote',''))
  for s in (n.get('state') or [])[-4:]: print('   ',s.get('d'),s.get('t'))
print('IS'); [print('  ',s.get('d'),s.get('kind'),s.get('t')) for s in c.get('industryState') or []]
cy=c.get('cycle') or {};print('CYCLE',json.dumps({k:v for k,v in cy.items() if k!='flags'},ensure_ascii=False))
print('FLAGS',[f['t'] for f in cy.get('flags',[])][-4:])
for k,v in (c.get('insight') or {}).items():
  for a in v: print('INS',k,a['t'],[s.get('u') for s in a.get('src',[])])
print('GAPS',c.get('gaps'))
print('HIST',c.get('history')[-2:])
