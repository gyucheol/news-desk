import json
O='/home/user/news-desk/data/industry-2026-11-02-pm/out/'
ETF='https://www.bloomberg.com/news/articles/2026-10-31/boj-faster-etf-sales-may-help-takaichi-spending-plan-non-tax-revenue'
PT='https://t.me/The_MariTimes/64153'
FX='https://www.bloomberg.com/news/articles/2026-11-02/japan-s-katayama-says-ready-to-take-steps-for-stable-fx-market'
x={"id":"jpins","summary":"",
"state":{
 "rates":[
  {"d":"2026-10-30","o":"텔레그램 Polaristimes","u":PT,"nid":"n-tg-0740","t":"일본은행은 10월 30일 정책금리를 1.25%로 8 대 1 동결했고, 다카타 하지메 위원은 1.5% 인상을 제안해 12월 인상 논의에 힘을 보탰습니다 [사실]"},
  {"d":"2026-11-02","o":"블룸버그","u":FX,"nid":"n-tg-0740","t":"가타야마 재무상은 11월 2일 무질서한 외환 움직임에 미국과 협력해 대응할 준비가 돼 있다고 했지만, 엔은 달러당 157.84엔 안팎에서 약세였습니다 [사실]"}],
 "securities":[
  {"d":"2026-10-30","o":"블룸버그","u":ETF,"nid":"n-tg-0740","t":"일본은행은 보유 주식 ETF 매각 목표를 장부가 기준 연 약 3,300억 엔에서 8,600억 엔으로 높여 2027년 1월부터 적용하며, 매각 종료 기간은 약 112년에서 약 43년으로 줄었습니다 [사실]"}]},
"industryState":[
 {"d":"2026-10-30","kind":"policy","o":"블룸버그","u":ETF,"nid":"n-tg-0740","t":"일본은행의 ETF 매각 목표는 장부가 기준 연 약 8,600억 엔(종전 약 3,300억 엔)으로 2027년 1월부터 적용되고, 정책금리는 1.25%로 동결됐습니다 [사실]"},
 {"d":"2026-11-02","kind":"price","o":"블룸버그","u":FX,"nid":"n-tg-0740","t":"엔은 11월 2일 도쿄 오전 달러당 157.84엔 안팎에서 약세였고, 스와프 시장은 10월 30일 12월 인상 확률을 약 80%로 반영했습니다 [사실]"}],
"flags":[],"insight":{},"cycle":None,"nodeStage":{},"gaps":"",
"note":"뉴스 2건 중 1건 반영: 일본은행 1.25% 동결(8 대 1, 다카타 1.5% 제안)·ETF 매각 연 8,600억 엔, 엔 157엔대와 가타야마 외환 대응 발언. 메모리·키옥시아 문서는 이 산업에 닿는 새 내용이 없어 applied만. 국면 ① 그대로, 근거 3줄, 수치 2줄, 재검토 신호 0건, 검색 0회",
"applied":["n-tg-0297","n-tg-0740"],"searches":0,"fetches":0}
json.dump(x,open(O+'jpins.json','w'),ensure_ascii=False,indent=1)
