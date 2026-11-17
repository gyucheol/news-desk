import json
O='/home/user/news-desk/data/industry-2026-11-02-pm/out/'
U='https://t.me/stockhasoo/17160'
x={"id":"uranium","summary":"",
"state":{"build":[{"d":"2026-10-29","o":"텔레그램 재야의 괴수들","u":U,"nid":"n-tg-0843","t":"한수원은 10월 29일 체코 두코바니 원전 시공계약 협상을 대우건설·두산에너빌리티 컨소시엄과 종료하고 시공사 재선정에 들어갔으며, 총액확정과 단가 정산 방식이 맞섰습니다 [사실]"}]},
"industryState":[],"flags":[],"insight":{},"cycle":None,"nodeStage":{},"gaps":"",
"note":"뉴스 1건 반영: 체코 두코바니 원전 한수원-시공 컨소시엄 협상 결렬·시공사 재선정(해외 원전 시공 수익성 의문). 국면 ⑧ 그대로, 근거 1줄, 수치 0줄, 재검토 신호 0건, 검색 0회",
"applied":["n-tg-0843"],"searches":0,"fetches":0}
json.dump(x,open(O+'uranium.json','w'),ensure_ascii=False,indent=1)
