import json
B='/home/user/news-desk'
p=json.load(open(f'{B}/work/nightly-2026-11-17/chains/aero.json'))
ids=[json.loads(l)['id'] for l in open(f'{B}/data/industry-2026-11-17-pm/news/aero.jsonl')]
def S(d,o,u,nid,t): return dict(d=d,o=o,u=u,nid=nid,t=t)
FAA1='https://www.bloomberg.com/news/articles/2026-11-16/us-airlines-brace-for-billion-dollar-hit-after-faa-ground-stop'
FAA2='https://www.bloomberg.com/news/articles/2026-11-16/senate-gop-leader-tempers-duffy-s-50-billion-air-traffic-push'
ULA='https://www.bloomberg.com/news/articles/2026-11-15/ula-vulcan-rocket-launches-with-its-first-amazon-leo-payload'
ULA2='https://www.bloomberg.com/news/articles/2026-11-15/pentagon-rocket-provider-hit-by-failure-while-spacex-soars'
JB='https://www.bloomberg.com/news/features/2026-11-16/faa-flight-chaos-isn-t-jetblue-ceo-s-only-concern-amid-airline-bankruptcy-fears'
JB0='https://www.bloomberg.com/news/articles/2026-10-26/jetblue-s-outlook-worsens-as-operating-loss-margin-drops'
IND='https://www.bloomberg.com/news/articles/2026-11-16/airbus-boeing-supply-chain-shift-boosts-india-aerospace-stocks'
HW='https://t.me/habit4117/88035'; HD='https://t.me/habit4117/88034'
HDR='https://www.reuters.com/world/asia-pacific/hd-hyundai-build-us-shipyard-with-kiewit-create-3000-jobs-2026-10-23/'
CB='https://www.bloomberg.com/news/articles/2026-11-16/ukraine-hits-crimean-bridge-in-record-drone-strike-on-russia'
CB2='https://www.bloomberg.com/news/newsletters/2026-11-16/ukraine-s-crimea-bridge-barrage-highlights-global-drone-race'
EST='https://www.bloomberg.com/news/articles/2026-11-15/estonia-says-russia-behind-failed-arson-attempt-on-drone-maker'
HU='https://t.me/Trillion_labs/12165'
CD='https://www.bloomberg.com/news/features/2026-11-15/us-military-tests-new-counter-drone-weapons-in-race-to-catch-up'
state={
 'parts':[S('2026-11-16','블룸버그',IND,'n-bbg-0905','에어버스·보잉이 공급망을 인도로 옮기면서 인도 증시의 항공우주 관련주가 강세를 보였습니다 [제목]')],
 'airlines':[
  S('2026-11-13','블룸버그',FAA1,'n-bbg-0894','FAA 관제 통신망 장애로 11월 13일 미 전역 지상정지가 내려져 그날 1만 2,462편이 결항했고, 16일 새벽까지 누적 결항은 1만 8,520편, 지연은 2만 8,300편을 넘었습니다 [사실]'),
  S('2026-11-16','블룸버그',JB,'n-rtr-0667','제트블루는 3분기 순손실 2억 5,700만 달러를 냈고 9월 말 부채가 약 84억 달러이며, 선순위 채권자들이 구조조정 자문사를 고용했다는 보도가 나왔지만 CEO는 파산 계획이 없다고 했습니다 [사실]')],
 'airports':[
  S('2026-11-16','블룸버그',FAA2,'n-bbg-0894','FAA 예비 조사는 아칸소·텍사스 관제 시설 라우터를 원인으로 지목했고, 더피 교통장관은 구리선 교체가 끝나는 2028년 말까지 장애가 더 날 수 있다며 500억 달러를 요구했지만 상원 공화당 원내대표가 제동을 걸었습니다 [사실]'),
  S('2026-11-16','텔레그램 트릴리온',HU,'n-rtr-0372','후티는 11월 13일과 16일 리야드 킹칼리드 공항을 드론으로 공격했다고 주장했고, 16일에는 공항과 리야드 금융센터를 모두 파괴했다고 주장했습니다 [채널]')],
 'platforms':[
  S('2026-11-16','텔레그램 습관이 부자를 만든다',HD,'n-rtr-0692','HD현대와 안두릴이 공동 개발한 600t급 자율수상함을 띄웠고, 승조원 0명으로 승조원 50명이 쓰던 공간을 없애 무장·연료 적재를 늘렸습니다 [채널]'),
  S('2026-10-23','로이터',HDR,'n-rtr-0692','HD현대와 키위트가 합작사를 세워 2027년 착공, 2029년 완전 가동할 미국 조선소를 짓기로 했고, 한화는 10월 미 해군·해병대 중형상륙함 2억 6,900만 달러 건조 계약을 따냈습니다 [사실]')],
 'munitions':[
  S('2026-11-16','텔레그램 습관이 부자를 만든다',HW,'n-rtr-0692','한화는 아칸소에 7년간 22억 달러를 들여 155mm 포탄 구성품·추진장약 공장을 짓고, 방산 3사가 올해 미국 법인에 출자했거나 출자하기로 한 금액은 1조 5,060억 원입니다 [사실]'),
  S('2026-11-16','블룸버그',CB,'n-tg-0121','러시아 국방부는 11월 16일 밤 16개 지역에서 우크라이나 드론 1,336대를 요격했다며 10월 29일의 1,254대를 넘는 최대 기록이라고 주장했고, 같은 날 크림대교가 피격됐습니다 [사실]')],
 'defspend':[
  S('2026-11-15','블룸버그',EST,'n-tg-0162','에스토니아는 러시아 군정보총국이 지시했다고 본 드론업체 트레오드 시스템스 방화 미수로 라트비아인 8명을 붙잡고, 12월 1일부터 대러 도로 국경 검문소를 닫기로 했습니다 [사실]')],
 'space':[
  S('2026-11-15','블룸버그',ULA,'n-bbg-0895','ULA 벌컨이 11월 15일 비행 중 실패해 아마존 레오 위성 40기가 궤도에 오르지 못했고, 2006년 ULA 출범 뒤 첫 완전한 실패로 원인은 조사 중입니다 [사실]')],
}
IS=[
 dict(d='2026-11-16',kind='supply',o='블룸버그',u=FAA1,nid='n-bbg-0894',t='FAA 지상정지로 11월 13일 하루 결항은 1만 2,462편(대형 항공사 9,082편), 16일 새벽까지 누적 결항 1만 8,520편, 지연 2만 8,300편 이상이었습니다 [사실]'),
 dict(d='2026-11-16',kind='policy',o='블룸버그',u=FAA2,nid='n-bbg-0894',t='더피 교통장관은 관제 개선에 500억 달러를 요구했고, 상원 공화당 원내대표가 이 요구에 제동을 걸었습니다 [제목]'),
 dict(d='2026-11-16',kind='capex',o='텔레그램 습관이 부자를 만든다',u=HW,nid='n-rtr-0692',t='한화는 아칸소 155mm 포탄 구성품·추진장약 공장에 7년간 22억 달러를 쓰고, 방산 3사의 올해 미국 법인 출자는 1조 5,060억 원(에어로스페이스 1조 89억 원)입니다 [사실]'),
 dict(d='2026-11-15',kind='supply',o='블룸버그',u=ULA,nid='n-bbg-0895',t='벌컨 실패로 아마존 레오 위성 40기를 잃었고, 아마존은 레오용 벌컨 발사 38회를 샀으며 같은 BE-4 엔진의 뉴글렌도 5월 실패 뒤 멈춰 있습니다 [사실]'),
]
flags=[dict(nid='n-rtr-0667',t='재검토 필요: 제트블루 채권자들의 구조조정 자문사 고용 보도는 항공사 노드가 ④ 수익 악화에서 ⑥ 공급 파괴·통합(파산·인수) 쪽으로 가고 있음을 가리키며, 부채 84억 달러에 연료비와 FAA 혼란이 겹치기 때문입니다 [유추]')]
old=p['insight']
b2=[dict(t='항공사가 연료비를 버티지 못하면 반대로 흐를 수 있습니다. 아메리칸항공은 올해 조정 주당손실 1.00~1.60달러를 예상했고, 제트블루는 부채 약 84억 달러에 채권자들이 구조조정 자문사를 고용했다는 보도가 나왔으며, 비엣젯은 미인도 에어버스 주문까지 묶인 자산 동결을 맞았습니다. 이런 항공사가 늘면 인도 연기·주문 축소가 나올 수 있습니다 [유추]',
   src=[dict(o='블룸버그',d='2026-11-17',u=JB),dict(o='블룸버그',d='2026-10-27',u=JB0)]+[s for s in old['b2'][0]['src'] if 'vietjet' in s['u']]),
   {k:v for k,v in old['b2'][1].items() if k!='rev'},
   dict(t='공급 쪽 충격도 항공사 이익을 깎습니다. 11월 13일 FAA 관제 장애로 사흘 새 1만 8,520편이 결항해 항공사들은 10억 달러대 타격에 대비하고, 교통장관은 구리선 교체가 끝나는 2028년 말까지 장애가 더 날 수 있다고 했습니다 [유추]',
   src=[dict(o='블룸버그',d='2026-11-17',u=FAA1)])]
c0=old['c'][0]
c=[dict(t='돈은 들어오는데 실행이 못 따라간다는 정보가 쌓입니다. ULA 벌컨이 11월 15일 첫 완전한 실패로 아마존 레오 위성 40기를 잃었고, 같은 BE-4 엔진의 뉴글렌도 5월 실패 뒤 멈춰 있으며, 로켓랩 뉴트론은 2027년으로 밀렸습니다 [사실]',
   src=[dict(o='블룸버그',d='2026-11-16',u=ULA),dict(o='블룸버그',d='2026-11-16',u=ULA2)]+[s for s in c0['src'] if 'rocket-lab' in s['u']]),
   {k:v for k,v in old['c'][1].items() if k!='rev'},{k:v for k,v in old['c'][2].items() if k!='rev'}]
gaps=p['gaps']+' 11월 17일 저녁 업데이트도 검색·열람 없이 입력 뉴스 9건으로만 반영했습니다. 벌컨 실패 원인(BE-4 엔진인지 센타우르 상단인지)과 FAA 장애의 최종 원인·항공사별 손실액, 제트블루 채권자 협상 내용, 후티의 킹칼리드 공항·금융센터 파괴 주장, HD현대·안두릴 무인함 제원은 확인하지 못했고, 인도 항공우주주 강세는 기사 제목뿐입니다.'
out=dict(id='aero',summary='',state=state,industryState=IS,flags=flags,insight=dict(b2=b2,c=c),cycle=None,nodeStage={},gaps=gaps,
 note='뉴스 9건 반영: FAA 관제 장애로 결항 1만 8,520편, ULA 벌컨 실패로 아마존 레오 위성 40기 손실, 제트블루 채권자 구조조정 자문 고용·한화 아칸소 포탄 공장 22억 달러. 국면 ② 그대로, 근거 11줄, 수치 4줄, 재검토 신호 1건, 인사이트 b2·c 갱신, 검색 0회',
 applied=ids,searches=0,fetches=0)
json.dump(out,open(f'{B}/data/industry-2026-11-17-pm/out/aero.json','w'),ensure_ascii=False,indent=1)
