import json
c=json.load(open('/home/user/news-desk/work/nightly-2026-10-20/chains/gas.json'))
a1=[{"t":a["t"],"src":a["src"]} for a in c['insight']['a1'][:2]]
Q='https://www.bloomberg.com/news/articles/2026-09-21/pakistan-secures-latest-qatar-lng-shipment-after-deal-with-iran'
Q2='https://t.me/Trillion_labs/10845'
G='https://www.bloomberg.com/news/articles/2026-09-15/lng-buyers-look-to-us-to-hedge-future-risk-of-hormuz-disruption'
P='https://t.me/PipeBeom/6577'
SH='https://www.bloomberg.com/news/articles/2026-10-07/shell-sees-strong-oil-and-gas-trading-as-war-drives-price-swings'
OR='https://www.bloomberg.com/news/articles/2026-10-13/oracle-asks-regulators-to-expedite-gas-pipeline-for-data-center'
CP='https://www.bloomberg.com/news/articles/2026-10-19/us-taps-wartime-funds-to-help-build-stalled-new-york-pipeline'
ARC='https://www.reuters.com/business/energy/russias-second-new-ice-class-lng-carrier-heads-via-northern-sea-route-lseg-data-2026-08-14/'
DE='https://www.reuters.com/business/energy/germany-fund-new-emergency-gas-reserve-via-consumer-levy-draft-says-2026-10-13/'
DE2='https://www.reuters.com/business/energy/germany-gas-storage-low-no-supply-risk-regulator-says-2026-10-15/'
JP='https://www.bloomberg.com/news/articles/2026-10-19/japan-power-price-at-four-year-high-with-rising-coal-lng-costs'
VG='https://t.me/Onionfarmer/18117'
KS='https://t.me/Trillion_labs/9825'
A1=a1+[{"t":"알래스카 LNG(사업비 445억~545억 달러)와 탄자니아 420억 달러 협정에 이어 YPF가 연 1,200만 톤(사업비 약 240억 달러) 수출 사업의 11월 FID를 노려 2030년대 공급 후보가 더 늘었습니다. 과잉이 오면 그 폭이 커질 가능성이 큽니다 [유추]",
 "src":c['insight']['a1'][2]['src']+[{"o":"블룸버그","d":"2026-09-15","u":G}]}]
x={"id":"gas","summary":"",
"state":{
 "liquefaction":[
  {"d":"2026-09-21","o":"블룸버그","u":Q,"nid":"n-bbg-0016","t":"카타르는 라스라판 완전 가동까지 최소 3년이 걸린다고 밝혔고, 전쟁 첫 6개월 수출은 18척으로 1년 전 509척에 크게 못 미쳤습니다 [사실]"},
  {"d":"2026-09-14","o":"블룸버그","u":G,"nid":"n-bbg-0017","t":"YPF는 연 1,200만 톤·사업비 약 240억 달러 수출 사업의 판매 계약 2~3건이 임박했다고 했지만 아직 서명은 없고, 최종 투자 결정은 11월이 목표입니다 [사실]"}],
 "trade":[
  {"d":"2026-09-15","o":"블룸버그","u":G,"nid":"n-bbg-0017","t":"방콕 가스텍 2026 사흘째까지 발표된 거래가 약 400억 달러로 추산됐고, 차이나가스는 벤처글로벌에서 2030년부터 20년간 연 50만 톤을 사기로 했습니다 [사실]"}],
 "upstream":[
  {"d":"2026-10-07","o":"블룸버그","u":SH,"nid":"n-bbg-0395","t":"셸은 3분기 통합가스 생산 전망을 하루 74만~78만 배럴로 제시해 2분기 63만 1,000배럴보다 높였습니다 [사실]"},
  {"d":"2026-09-14","o":"텔레그램","u":P,"nid":"n-bbg-0017","t":"포스코인터내셔널이 셰니에르 헨리허브 연동 도입계약의 원가 위험을 메우려 미국 마셀러스 셰일가스 자산(LNG 환산 연 약 100만 톤)을 5.5억 달러에 샀습니다 [사실]"}],
 "midstream":[
  {"d":"2026-10-14","o":"블룸버그","u":OR,"nid":"n-bbg-0416","t":"오라클이 뉴멕시코 데이터센터용 가스관 완공이 2027년 2월로 밀려 데이터센터 가동이 늦을 수 있다며 FERC에 신속 승인을 요청했고, 12개 주가 분쟁에 가세했습니다 [사실]"},
  {"d":"2026-10-19","o":"블룸버그","u":CP,"nid":"n-bbg-0425","t":"미 에너지부가 국방물자법 자금 최대 4,200만 달러를 뉴욕주 반대로 멈춘 약 125마일 컨스티튜션 가스관 인허가 작업에 대기로 했지만, 주 수질 인증이 여전히 관건입니다 [사실]"}],
 "shipping":[
  {"d":"2026-08-30","o":"로이터","u":ARC,"nid":"n-rtr-0007","t":"러시아가 두 번째 자국산 Arc7 쇄빙 LNG선을 제재 대상 북극 LNG 2에 투입해 7만 톤 넘는 첫 화물을 실었고, 겨울 전 Arc7 선대가 4척이 될 전망입니다 [사실]"}],
 "regas":[
  {"d":"2026-10-13","o":"로이터","u":DE,"nid":"n-rtr-0432","t":"독일이 새 비상 가스 비축 재원을 소비자 부담금으로 마련하는 초안을 만들어, 가구가 2027년 10월부터 연 최대 7.20유로를 낼 수 있습니다 [사실]"},
  {"d":"2026-10-16","o":"로이터","u":DE2,"nid":"n-rtr-0435","t":"독일 규제당국은 가스 저장량이 낮지만 공급 위험은 없다고 밝혀 겨울 부족 우려를 누그러뜨리려 했습니다 [제목]"}],
 "demand":[
  {"d":"2026-10-19","o":"블룸버그","u":JP,"nid":"n-bbg-0413","t":"일본 전국 익일 현물 전력값이 LNG·석탄값 상승과 정기 보수로 한 주 새 25% 넘게 올라 19일 kWh당 31.15엔, 약 4년 만의 최고를 기록했습니다 [사실]"},
  {"d":"2026-10-15","o":"텔레그램 양파농장","u":VG,"nid":"n-tg-0016","t":"벤처글로벌이 GE 베르노바·베이커휴즈와 720MW급 독립형 가스복합 발전 설비 최대 16기 계약을 맺어 데이터센터 전력 사업에 나섰습니다 [사실]"},
  {"d":"2026-10-01","o":"텔레그램","u":KS,"nid":"n-bbg-0002","t":"한국 대미 투자 1호 사업인 텍사스 가스발전 프로젝트 스타(223억 달러)는 넥스트에라가 6.47GW를 짓고 전력 대부분을 옆 5GW 데이터센터에 댑니다 [사실]"}]},
"industryState":[
  {"d":"2026-10-19","kind":"price","o":"블룸버그","u":JP,"nid":"n-bbg-0413","t":"일본전력거래소 전국 익일 현물 가격은 19일 kWh당 31.15엔으로 한 주 새 25% 넘게 올라 약 4년 만의 최고였습니다 [사실]"},
  {"d":"2026-09-21","kind":"supply","o":"블룸버그","u":Q,"nid":"n-bbg-0016","t":"카타르 생산능력은 라스라판 손상으로 약 17% 줄었고 완전 가동까지 최소 3년이 걸리며, 전쟁 첫 6개월 수출은 18척으로 1년 전 509척에 못 미쳤습니다 [사실]"},
  {"d":"2026-09-14","kind":"capex","o":"블룸버그","u":G,"nid":"n-bbg-0017","t":"YPF는 연 1,200만 톤·사업비 약 240억 달러 LNG 수출 사업의 최종 투자 결정을 2026년 11월에 내리는 것을 목표로 합니다 [사실]"},
  {"d":"2026-10-01","kind":"demand","o":"텔레그램","u":KS,"nid":"n-bbg-0002","t":"텍사스 프로젝트 스타는 223억 달러로 6.47GW 가스발전을 지어 5GW 데이터센터 캠퍼스에 공급하며 첫 발전은 이르면 2029년입니다 [사실]"}],
"flags":[],
"insight":{"a1":A1},
"cycle":None,"nodeStage":{},"gaps":"",
"note":"뉴스 27건 반영: 카타르 완전 가동 최소 3년·6개월 수출 18척, 가스텍 거래 400억 달러·YPF 11월 FID 목표, 일본 전력값 4년 최고·오라클 가스관 지연. 국면 ② 그대로, 근거 13줄, 수치 4줄, 인사이트 a1 고침, 재검토 신호 0건, 검색 0회",
"applied":[json.loads(l)['id'] for l in open('news/gas.jsonl')],"searches":0,"fetches":0}
json.dump(x,open('out/gas.json','w'),ensure_ascii=False,indent=1)
