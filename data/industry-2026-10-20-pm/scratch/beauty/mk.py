import json
D='/home/user/news-desk/data/industry-2026-10-20-pm'
ids=[json.loads(l)['id'] for l in open(f'{D}/news/beauty.jsonl')]
BC='https://www.bloomberg.com/news/articles/2026-08-25/us-canada-cosmetic-tariffs-threaten-the-10-beauty-impulse-buy'
x={"id":"beauty","summary":"",
"state":{
 "exports":[
  {"d":"2026-09-08","o":"블룸버그","u":BC,"nid":"n-bbg-0010","t":"미국이 캐나다산 화장품에 매긴 50% 관세가 8월 22일 발효됐고 캐나다도 9월 8일부터 미국산 향수·메이크업 등에 50% 맞관세를 물려, 연 42억 달러 규모인 미국 화장품의 캐나다 수출이 타격을 받게 됐습니다 [사실]"},
  {"d":"2026-10-14","o":"로이터","u":"https://www.reuters.com/business/retail-consumer/french-cosmetics-facing-delays-clearing-china-customs-says-industry-association-2026-10-14/","nid":"n-rtr-0579","t":"프랑스 화장품 업계 단체가 10월 14일 자국 화장품이 중국 세관 통관에서 지연을 겪고 있다고 밝혀, 유럽 경쟁 브랜드의 중국 수출에 차질이 생기고 있습니다 [제목]"}],
 "brands":[
  {"d":"2026-10-15","o":"로이터","u":"https://www.reuters.com/legal/transactional/galderma-buy-us-firm-zo-skin-health-15-billion-2026-10-14/","nid":"n-rtr-0606","t":"갈더마는 10월 15일 블랙스톤이 가진 미국 스킨케어 업체 ZO스킨헬스를 기업가치 15억 달러에 인수한다고 발표해 미국 스킨케어 시장에서 몸집을 키웁니다 [사실]"}]
},
"industryState":[
 {"d":"2026-09-08","kind":"policy","o":"블룸버그","u":BC,"nid":"n-bbg-0010","t":"캐나다의 대미 맞관세 50%는 미국산 수입품 276억 캐나다달러, 약 700개 품목에 걸리고, 미국 화장품의 캐나다 수출은 연 42억 달러로 미국 업계 수출의 4분의 1이 넘습니다 [사실]"},
 {"d":"2026-10-15","kind":"capex","o":"로이터","u":"https://www.reuters.com/legal/transactional/galderma-buy-us-firm-zo-skin-health-15-billion-2026-10-14/","nid":"n-rtr-0606","t":"갈더마가 블랙스톤 소유의 미국 ZO스킨헬스를 기업가치 15억 달러에 사들이기로 해, 사모펀드가 피부관리 자산을 전략적 인수자에게 넘겼습니다 [사실]"}
],
"flags":[],"insight":{},"cycle":None,"nodeStage":{},"gaps":"",
"note":"뉴스 4건 반영: 미국·캐나다 화장품 50% 맞관세 규모(276억 캐나다달러·미국 화장품 대캐나다 수출 42억 달러), 프랑스 화장품 중국 통관 지연, 갈더마의 ZO스킨헬스 15억 달러 인수; K뷰티 M&A 몸값·육성법은 이미 반영. 국면 ② 그대로, 근거 3줄, 수치 2줄, 재검토 신호 0건, 검색 0회",
"applied":ids,"searches":0,"fetches":0}
json.dump(x,open(f'{D}/out/beauty.json','w'),ensure_ascii=False,indent=1)
