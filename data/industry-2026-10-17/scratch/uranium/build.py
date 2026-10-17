import json
N='/home/user/news-desk/data/industry-2026-10-17/news/uranium.jsonl'
ids=[json.loads(l)['id'] for l in open(N)]
def S(o,d,u): return {'o':o,'d':d,'u':u}
B_UP='https://www.bloomberg.com/news/newsletters/2026-10-13/us-nuclear-s-low-hanging-fruit-is-being-gobbled-up'
R_EDF='https://www.reuters.com/business/energy/record-summer-nuclear-disruptions-push-edf-fast-track-climate-measures-2026-10-13/'
R_MO='https://www.reuters.com/business/energy/slovakia-connect-mochovce-nuclear-power-plants-fourth-unit-ramp-up-continues-2026-10-13/'
B_KA='https://www.bloomberg.com/news/articles/2026-10-14/nuclear-startup-kairos-raises-643-million-for-tennessee-project'
R_CA='https://www.reuters.com/business/energy/constellation-amazon-sign-20-year-power-deal-support-maryland-nuclear-plant-2026-09-30/'
state={
 'operators':[
  {'d':'2026-10-13','o':'블룸버그','u':B_UP,'nid':'n-bbg-0072','t':'구글 890MW·비스트라 433MW 증강 계약 뒤 제프리스는 미국 원전의 남은 출력 증강 여력을 3~5GW로 봤고, 2024년 에너지부 추정은 최대 8GW였습니다 [사실]'},
  {'d':'2026-10-13','o':'로이터','u':R_EDF,'nid':'n-rtr-0285','t':'EDF는 6월 말 폭염으로 강물 온도가 오르자 원전 출력을 약 6.2~6.5GW(약 10%) 줄였고, 기후 적응 예산을 15년 안에 연 6억 유로로 늘리는 계획을 앞당깁니다 [사실]'}],
 'build':[
  {'d':'2026-10-14','o':'블룸버그','u':B_KA,'nid':'n-bbg-0071','t':'카이로스 파워는 민간 3억 6,800만 달러와 에너지부 2억 7,500만 달러 등 6억 4,300만 달러를 확보해 2030년 가동 예정인 50MW 시범로 헤르메스 2에 씁니다 [사실]'},
  {'d':'2026-10-13','o':'로이터','u':R_MO,'nid':'n-rtr-0285','t':'슬로바키아 모호프체 4호기(471MW)는 기술 시험을 반복하느라 계통 연결이 며칠 늦어졌고, 연말 완전 가동이 목표입니다 [사실]'}],
}
industryState=[
 {'d':'2026-10-13','kind':'supply','o':'블룸버그','u':B_UP,'nid':'n-bbg-0072','t':'제프리스는 미국 원전 출력 증강 여력을 3~5GW로 추정했고, 2024년 에너지부 추정은 최대 8GW였습니다 [사실]'},
 {'d':'2026-10-13','kind':'policy','o':'블룸버그','u':B_UP,'nid':'n-bbg-0072','t':'미 에너지부 UPRISE 계획은 원전 설비를 2027년까지 2.5GW, 2029년까지 모두 5GW 늘리는 것을 목표로 합니다 [사실]'},
]
insight={
 'b1':[
  {'t':'수요가 계약으로 확정되는 속도가 공급 증가보다 빠를 가능성이 큽니다. 데이터센터 사업자가 기존 원전의 출력 증강·수명 연장 투자까지 받쳐 주는 구조가 생겼기 때문입니다 [유추]','src':[S('로이터','2026-10-01',R_CA)]},
  {'t':'다만 출력 증강으로 빨리 잡히는 수요는 바닥이 보입니다. 제프리스는 구글·비스트라 계약 뒤 남은 미국 증강 여력을 3~5GW로 봐, 그 뒤 연료 수요 증가는 재가동과 신규 건설 속도에 달립니다 [유추]','src':[S('블룸버그','2026-10-13',B_UP)]}],
}
out={'id':'uranium','summary':'','state':state,'industryState':industryState,'flags':[],'insight':insight,
 'cycle':None,'nodeStage':{},'gaps':'',
 'note':'뉴스 4건 반영: 미국 원전 출력 증강 여력 3~5GW로 소진, 카이로스 6억 4,300만 달러 확보, EDF 폭염 출력 감축·모호프체 4호기 지연. 국면 그대로(⑧ 회복 초기), 근거 4줄, 수치 2줄, 인사이트 b1 고침, 재검토 신호 0건, 검색 0회',
 'applied':ids,'searches':0,'fetches':0}
json.dump(out,open('/home/user/news-desk/data/industry-2026-10-17/out/uranium.json','w'),ensure_ascii=False,indent=1)
