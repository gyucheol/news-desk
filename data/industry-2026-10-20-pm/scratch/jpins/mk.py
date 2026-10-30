import json
D='/home/user/news-desk/data/industry-2026-10-20-pm'
ids=[json.loads(l)['id'] for l in open(f'{D}/news/jpins.jsonl')]
UE='https://www.reuters.com/world/asia-pacific/boj-governor-ueda-says-underlying-inflation-quite-close-2-target-2026-10-19/'
TK='https://www.reuters.com/world/asia-pacific/japan-pm-says-wont-rule-out-debt-issuance-fund-tax-cut-2026-10-19/'
IMF='https://www.reuters.com/world/asia-pacific/boj-may-need-tighten-faster-if-inflation-beats-forecast-imf-says-2026-10-17/'
DL='https://www.bloomberg.com/news/articles/2026-10-18/daiichi-life-offers-to-buy-remainder-of-australia-s-challenger'
x={"id":"jpins","summary":"",
"state":{
 "rates":[
  {"d":"2026-10-17","o":"로이터","u":IMF,"nid":"n-rtr-0497","t":"IMF는 10월 17일 물가가 전망을 웃돌면 일본은행이 더 빨리 긴축해야 할 수 있다고 했고, 닛케이는 이번 국면의 최종 기준금리를 1.75~2%로 내다봤습니다 [사실]"},
  {"d":"2026-10-19","o":"로이터","u":UE,"nid":"n-bbg-0082","t":"우에다 총재는 19일 국회에서 기조물가가 2%에 꽤 가까워져 그 근처에 안착시키는 것이 더 중요해졌다며, 정책금리를 적절히 조정하지 못하면 장기금리가 오를 수 있다고 경고했습니다 [사실]"},
  {"d":"2026-10-19","o":"로이터","u":TK,"nid":"n-bbg-0082","t":"다카이치 총리는 내년 4월 시작될 2년간 식품 소비세 감세(감세·급부 2년간 약 10조 엔)의 재원으로 국채 발행을 배제하지 않겠다고 했습니다 [사실]"}],
 "capital":[
  {"d":"2026-10-19","o":"블룸버그","u":DL,"nid":"n-bbg-0360","t":"다이이치생명 호주 자회사는 지분 20.36%를 가진 연금 운용사 챌린저의 나머지 79.5%를 주당 11.80호주달러(약 44억 달러, 약 20% 할증)에 사겠다는 구속력 없는 제안을 했습니다 [사실]"}]
},
"industryState":[
 {"d":"2026-10-19","kind":"capex","o":"블룸버그","u":DL,"nid":"n-bbg-0360","t":"다이이치생명의 챌린저 잔여 지분 인수 제안은 주당 11.80호주달러, 블룸버그 계산 약 44억 달러이며 챌린저 주가는 2018년 이후 최고로 뛰었습니다 [사실]"},
 {"d":"2026-10-19","kind":"policy","o":"로이터","u":TK,"nid":"n-bbg-0082","t":"일본 정부의 2년간 식품 소비세 감세·급부 규모는 약 10조 엔이며, 다카이치 총리는 재원으로 국채 발행을 배제하지 않았습니다 [사실]"}
],
"flags":[{"nid":"n-bbg-0360","t":"재검토 필요: 도쿄해상의 호주 손보 검토에 이어 다이이치생명이 약 44억 달러로 챌린저 인수를 제안한 것은 해외 인수가 잇따르는 ② 자본 유입·증설 국면 조건을 가리키며, 넘치는 자본이 해외 확장으로 향하고 있기 때문입니다 [유추]"}],
"insight":{"a1":[
 {"t":"우에다 총재가 10월 19일 기조물가가 2%에 꽤 가까워졌다고 했고 10월 인상 가능성은 낮아져 추가 인상은 12월 쪽으로 옮겨 갔습니다. 인상이 이어지면 생보의 신규 운용 수익률이 오르고 손보 요율 인상이 2027년까지 이익에 반영될 가능성이 큽니다 [유추]","src":[{"o":"로이터","d":"2026-10-19","u":UE},{"o":"블룸버그","d":"2026-10-19","u":"https://www.bloomberg.com/news/articles/2026-10-19/japan-pm-takaichi-denies-she-s-driving-weak-yen-high-rates"}]},
 {"t":"닛케이가 이번 국면 최종 기준금리를 1.75~2%로 보고 IMF도 물가가 전망을 웃돌면 더 빨리 긴축해야 할 수 있다고 해, 생보의 신규 채권 수익률이 지금보다 더 오를 여지가 있습니다 [유추]","src":[{"o":"로이터","d":"2026-10-17","u":IMF},{"o":"텔레그램","d":"2026-08-23","u":"https://t.me/The_MariTimes/62259"}]},
 {"t":"MUFG가 일본 국채 매수를 재개하고 보험사들이 해외 자금을 서서히 국내로 들일 채비를 해, 초장기 국채 수요가 받쳐지면서 생보의 평가손실 부담이 줄어드는 흐름이 가능합니다 [유추]","src":[{"o":"블룸버그","d":"2026-10-15","u":"https://www.bloomberg.com/news/articles/2026-10-14/mufg-wades-back-into-japanese-bonds-with-eye-on-policy-risks"},{"o":"로이터","d":"2026-10-15","u":"https://www.reuters.com/business/finance/japanese-insurers-are-poised-bring-money-back-home-gradually-2026-10-15/"}]}
]},
"cycle":None,"nodeStage":{},"gaps":"",
"note":"뉴스 3건 반영: 다이이치생명의 챌린저 약 44억 달러 인수 제안, 우에다 총재 '기조물가 2% 근접'과 12월 인상론, 다카이치 총리의 감세 재원 국채 발행 여지(약 10조 엔)·IMF 긴축 가속 언급; 8월 10년물 2.93%는 이미 반영. 국면 ① 그대로, 근거 4줄, 수치 2줄, 재검토 신호 1건, 검색 0회",
"applied":ids,"searches":0,"fetches":0}
json.dump(x,open(f'{D}/out/jpins.json','w'),ensure_ascii=False,indent=1)
