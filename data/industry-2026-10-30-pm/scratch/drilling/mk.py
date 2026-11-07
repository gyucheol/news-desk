import json
P='/home/user/news-desk/'
def load(i): return json.load(open(P+'work/nightly-2026-10-30/chains/'+i+'.json'))
def save(o): json.dump(o,open(P+'data/industry-2026-10-30-pm/out/'+o['id']+'.json','w'),ensure_ascii=False,indent=1)
EQ='https://t.me/PipeBeom/6921'; TR='https://t.me/Trillion_labs/11425'; VR='https://t.me/verteinsight/5'
SH='https://www.bloomberg.com/news/newsletters/2026-10-29/shell-ceo-faces-test-of-turning-a-cash-windfall-into-durable-growth'
# drilling
o=load('drilling')
save({"id":"drilling","summary":"",
"state":{
 "capex":[
  {"d":"2026-10-30","o":"텔레그램 상상인 김진범","u":EQ,"nid":"n-tg-0803","t":"셰브론은 미개발 지역 탐사를 다시 늘려 탐사 투자 중 이 지역 비중을 약 20%에서 50%로 높이고, 연간 최대 20개 탐사정 중 절반을 신규 지역에 배정한다는 WSJ 전언입니다 [채널]"},
  {"d":"2026-10-30","o":"텔레그램 트릴리온","u":TR,"nid":"n-tg-0837","t":"중국 국가에너지국은 10월 21일 회의 뒤 3대 국영 석유사에 생산능력·투자 확대를 주문했지만, 페트로차이나의 1~9월 설비투자는 1,594억 위안으로 줄었습니다 [사실]"}],
 "subsea":[
  {"d":"2026-10-30","o":"텔레그램 Verte Research","u":VR,"nid":"n-tg-0837","t":"에퀴노르는 6월 자본시장설명회에서 손익분기 배럴당 35달러 미만 투자 기회와 2035년까지 매년 타이백 6~8개 개발 계획을 제시했다는 전언입니다 [채널]"}]},
"industryState":[
  {"d":"2026-10-30","kind":"capex","o":"텔레그램 상상인 김진범","u":EQ,"nid":"n-tg-0803","t":"셰브론의 탐사 투자 가운데 미개발 지역 비중은 수년 전 약 20%에서 50%로 올랐다는 WSJ 전언입니다 [채널]"},
  {"d":"2026-10-30","kind":"capex","o":"텔레그램 Verte Research","u":VR,"nid":"n-tg-0837","t":"Verte 리서치는 IEA를 인용해 2019년 이후 업스트림 투자의 약 90%가 기존 유전의 생산 감소를 메우는 데 쓰였다고 짚었습니다 [채널]"},
  {"d":"2026-10-30","kind":"capex","o":"텔레그램 트릴리온","u":TR,"nid":"n-tg-0837","t":"페트로차이나 3분기 순이익은 518억 4,000만 위안으로 21.6% 늘었지만 1~9월 설비투자는 1,594억 위안으로 줄었습니다 [사실]"}],
"flags":[],"insight":{},"cycle":None,"nodeStage":{},
"gaps":o['gaps']+" 10월 30일 저녁 업데이트는 검색·열람 없이 입력 뉴스 2건으로만 반영했습니다. 셰브론 탐사 비중과 Verte 리서치의 IEA 인용 90%, 에퀴노르 타이백 계획은 채널 전언이고, 페트로차이나 설비투자의 감소 폭과 중국 국영사 자금 여력 확대의 규모(기사 제목만 봄), 엑손·셰브론 경영진의 ADIPEC 불참이 계약 일정에 미칠 영향은 확인하지 못했습니다.",
"note":"뉴스 2건 반영: 셰브론 미개발지 탐사 비중 20%→50% 전언, 상류 투자 90%가 감산 메우기라는 분석, 에퀴노르 타이백 계획. 국면 ⑧ 그대로, 근거 3줄, 수치 3줄, 재검토 신호 0건, 검색 0회",
"applied":["n-tg-0803","n-tg-0837"],"searches":0,"fetches":0})
# uranium
o=load('uranium')
save({"id":"uranium","summary":"",
"state":{"build":[
  {"d":"2026-10-29","o":"텔레그램 TNBfolio","u":"https://t.me/TNBfolio/71753","nid":"n-tg-0808","t":"두산에너빌리티가 10월 29일 뉴스케일파워와 NRC 설계승인 SMR의 첫 상업용 원자로 압력용기 상부 모듈 제작 계약을 맺었지만, 금액은 공개되지 않았고 뉴스케일은 확정 고객 주문이 없습니다 [사실]"}]},
"industryState":[],"flags":[],"insight":{},"cycle":None,"nodeStage":{},
"gaps":o['gaps']+" 10월 30일 저녁 업데이트는 검색·열람 없이 입력 뉴스 1건으로만 반영했습니다. 두산–뉴스케일 본제작 계약 금액과 납기, 뉴스케일의 확정 고객 여부, 로사톰과 미국의 데이터센터용 SMR 논의(채널 전언)의 실체는 확인하지 못했습니다.",
"note":"뉴스 1건 반영: 두산에너빌리티–뉴스케일 SMR 첫 상업용 모듈 본제작 계약. 국면 ⑧ 그대로, 근거 1줄, 수치 0줄, 재검토 신호 0건, 검색 0회",
"applied":["n-tg-0808"],"searches":0,"fetches":0})
# petchem
o=load('petchem')
save({"id":"petchem","summary":"",
"state":{"cracker":[
  {"d":"2026-10-29","o":"블룸버그","u":SH,"nid":"n-bbg-0395","t":"셸의 3분기 화학 마진 지표는 톤당 270달러에서 208달러로 떨어져, 정제 마진 지표가 배럴당 24달러에서 42달러로 뛴 것과 엇갈렸습니다 [사실]"}]},
"industryState":[
  {"d":"2026-10-29","kind":"price","o":"블룸버그","u":SH,"nid":"n-bbg-0395","t":"셸의 3분기 화학 마진 지표는 톤당 208달러로 직전 270달러보다 약 23% 낮아졌습니다 [사실]"}],
"flags":[],"insight":{},"cycle":None,"nodeStage":{},
"gaps":o['gaps']+" 10월 30일 저녁 업데이트는 검색·열람 없이 입력 뉴스 1건으로만 반영했습니다. 셸 화학 마진 하락의 지역·제품별 원인과 시노펙 화학 부문의 3분기 손익은 확인하지 못했습니다.",
"note":"뉴스 1건 반영: 셸 3분기 화학 마진 톤당 270→208달러(정제 마진과 엇갈림). 국면 ⑥ 그대로, 근거 1줄, 수치 1줄, 재검토 신호 0건, 검색 0회",
"applied":["n-bbg-0395"],"searches":0,"fetches":0})
