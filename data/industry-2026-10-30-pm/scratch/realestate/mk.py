import json
P='/home/user/news-desk/'
old=json.load(open(P+'work/nightly-2026-10-30/chains/realestate.json'))
EQX='https://www.bloomberg.com/news/articles/2026-10-28/equinix-says-data-project-barriers-could-boost-its-pricing-power'
UK='https://www.bloomberg.com/news/articles/2026-10-29/uk-mortgage-approvals-fall-more-than-forecast-as-loan-costs-bite'
DC1='https://t.me/PipeBeom/6927'; DC2='https://t.me/The_MariTimes/64105'
HF='https://www.bloomberg.com/news/articles/2026-10-29/chinese-conglomerate-zhuhai-huafa-repays-overdue-trust-product'
HF0='https://www.bloomberg.com/news/articles/2026-10-27/china-property-woes-crisis-zhuhai-huafa-62-billion-debt-zhuhai-tower-guangdong'
ob=old['insight']['b']
out={"id":"realestate","summary":"",
"state":{
 "datacenter":[
  {"d":"2026-10-28","o":"블룸버그","u":EQX,"nid":"n-bbg-0795","t":"에퀴닉스의 3분기 신규 계약 가격은 12% 올랐고 연환산 총예약은 5억 3,300만 달러(35%↑)로 사상 최대였으며, 경영진은 수요를 채울 용량이 부족하다고 했습니다 [사실]"},
  {"d":"2026-10-30","o":"텔레그램 Polaristimes","u":DC2,"nid":"n-tg-0646","t":"미국 10개 주 38개 지자체에서 최소 41개 데이터센터 제한 안건이 투표에 부쳐지고, 오하이오 선버리 25MW 이상 금지안이 통과되면 아마존 20억 달러 사업이 차질을 빚을 수 있습니다 [채널]"}],
 "housing":[
  {"d":"2026-10-29","o":"블룸버그","u":UK,"nid":"n-bbg-0804","t":"영국 9월 주택 구입용 모기지 승인은 5만 3,443건으로 2023년 12월 이후 최저였고, 신규 모기지 실효금리는 4.60%에서 4.63%로 올랐습니다 [사실]"}],
 "china":[
  {"d":"2026-10-29","o":"블룸버그","u":HF,"nid":"n-tg-0765","t":"주하이 화파는 연체 신탁 상품 1건의 일부 투자자에게 상환했지만, 2027년 만기 위안화 역외채는 한 주 새 약 38% 떨어져 액면가 60센트 안팎에 거래됐습니다 [사실]"}]},
"industryState":[
  {"d":"2026-10-28","kind":"price","o":"블룸버그","u":EQX,"nid":"n-bbg-0795","t":"에퀴닉스 3분기 신규 계약 가격은 12% 올랐고 연환산 총예약은 사상 최대인 5억 3,300만 달러로 35% 늘었습니다 [사실]"},
  {"d":"2026-10-29","kind":"demand","o":"블룸버그","u":UK,"nid":"n-bbg-0804","t":"영국 9월 주택 구입용 모기지 승인은 5만 3,443건(8월 5만 4,800건)으로 33개월 만의 최저였고, 리모기지 승인은 4만 2,600건으로 늘었습니다 [사실]"},
  {"d":"2026-10-30","kind":"policy","o":"텔레그램 Polaristimes","u":DC2,"nid":"n-tg-0646","t":"미국 10개 주 38개 지자체에서 최소 41개 데이터센터 제한 안건이 투표에 부쳐지며, 그중 21개가 오하이오에 몰렸습니다 [채널]"},
  {"d":"2026-10-29","kind":"price","o":"블룸버그","u":HF,"nid":"n-tg-0765","t":"주하이 화파의 2027년 만기 위안화 역외채는 한 주 새 약 38% 떨어져 액면가 60센트 안팎이었고, 이자부 부채는 4,130억 위안입니다 [사실]"}],
"flags":[],
"insight":{"b":[
  {"t":ob[0]['t']+" 영국 9월 주택 구입용 모기지 승인은 5만 3,443건으로 33개월 만의 최저였습니다 [사실]","src":ob[0]['src']+[{"o":"블룸버그","d":"2026-10-29","u":UK}]},
  {"t":"데이터센터는 공실 1.4%로 수요가 빠듯해 에퀴닉스 신규 계약 가격이 3분기 12% 올랐지만, 샌프란시스코·뉴욕주·시카고의 승인 중단과 10개 주 41개 제한 안건 투표, 전력 지연(호주 대형 사업 중 전력 연결 확인 23%)이 공급을 막고 있습니다 [귀납]","src":ob[1]['src']+[{"o":"블룸버그","d":"2026-10-28","u":EQX},{"o":"텔레그램 Polaristimes","d":"2026-10-30","u":DC2}]}]},
"cycle":None,"nodeStage":{},
"gaps":old['gaps']+" (11) 10월 30일 저녁 업데이트는 검색·열람 없이 입력 뉴스 4건으로만 반영했습니다. 미국 지자체 41개 제한 안건과 뉴욕주·시카고 행정명령은 텔레그램 전언(로이터 인용)이고 투표 결과는 확인하지 못했습니다. 에퀴닉스의 '건설 장벽이 가격결정력을 키운다'는 평가는 기사 제목 기준이며, 화파가 상환한 신탁의 금액과 나머지 연체 상품 처리도 확인하지 못했습니다.",
"note":"뉴스 4건 반영: 에퀴닉스 신규 계약 가격 12%↑, 미 데이터센터 제한 안건 41개 투표 확산, 영국 9월 모기지 승인 33개월 최저, 화파 역외채 38% 급락. 국면 ⑥(분할) 그대로, 근거 4줄, 수치 4줄, 재검토 신호 0건, 검색 0회",
"applied":["n-bbg-0795","n-bbg-0804","n-tg-0646","n-tg-0765"],"searches":0,"fetches":0}
json.dump(out,open(P+'data/industry-2026-10-30-pm/out/realestate.json','w'),ensure_ascii=False,indent=1)
