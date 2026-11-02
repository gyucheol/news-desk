import json
O='/home/user/news-desk/data/industry-2026-11-02-pm/out/'
ETG='https://www.bloomberg.com/news/articles/2026-10-29/etg-group-plans-2-billion-mozambique-urea-plant-as-iran-war-lifts-prices'
SW='https://www.bloomberg.com/news/articles/2026-10-30/us-won-t-halt-mexican-cattle-imports-despite-screwworm-surge'
CH='https://www.bloomberg.com/news/newsletters/2026-10-30/this-year-s-halloween-is-a-spooky-time-for-the-chocolate-industry'
x={"id":"agri","summary":"",
"state":{
 "inputs":[{"d":"2026-10-29","o":"블룸버그","u":ETG,"nid":"n-bbg-0869","t":"아프리카 최대 비료 무역상 ETG가 호르무즈발 비료값 상승을 계기로 모잠비크 북부에 연 150만 톤 요소 공장(15억~20억 달러)을 검토하며, 결정은 약 1년 뒤입니다 [사실]"}],
 "livestock":[{"d":"2026-10-30","o":"블룸버그","u":SW,"nid":"n-bbg-0870","t":"미 농무부는 6월 초 이후 국내 가축 나선구더기 감염이 73건(활성 21건)으로 늘었는데도 멕시코산 소 수입을 유지하고, 노갈레스 통관은 11월 30일 재개를 계획합니다 [사실]"}],
 "softs":[{"d":"2026-10-30","o":"블룸버그","u":CH,"nid":"n-bbg-0871","t":"코코아는 톤당 3,000달러 아래로 내렸지만 초콜릿 값은 지난 할로윈보다 약 8% 비싸, 할로윈 초콜릿 판매가 9주간 3,310만 달러 줄어 최소 3년 새 최대 감소였습니다 [사실]"}]},
"industryState":[
 {"d":"2026-10-29","kind":"capex","o":"블룸버그","u":ETG,"nid":"n-bbg-0869","t":"ETG의 모잠비크 요소 공장 계획은 연 150만 톤, 투자비 15억~20억 달러 규모이고, 원료 가스를 댈 모잠비크 LNG의 첫 수출 목표는 2029년입니다 [사실]"},
 {"d":"2026-10-30","kind":"demand","o":"블룸버그","u":CH,"nid":"n-bbg-0871","t":"NIQ 자료로 10월 17일까지 9주간 할로윈 초콜릿 판매는 3,310만 달러 줄었고, 9월 편의점 캔디 판매는 5% 줄었습니다 [사실]"}],
"flags":[],"insight":{},"cycle":None,"nodeStage":{},"gaps":"",
"note":"뉴스 3건 반영: ETG 모잠비크 요소 공장 15억~20억 달러 검토, 나선구더기 73건에도 멕시코산 소 수입 유지, 할로윈 초콜릿 판매 3,310만 달러 감소. 국면 ④(분할) 그대로, 근거 3줄, 수치 2줄, 재검토 신호 0건, 검색 0회",
"applied":["n-bbg-0869","n-bbg-0870","n-bbg-0871"],"searches":0,"fetches":0}
json.dump(x,open(O+'agri.json','w'),ensure_ascii=False,indent=1)
