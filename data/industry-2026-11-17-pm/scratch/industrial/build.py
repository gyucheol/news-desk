import json
B='/home/user/news-desk'
p=json.load(open(f'{B}/work/nightly-2026-11-17/chains/industrial.json'))
ids=[json.loads(l)['id'] for l in open(f'{B}/data/industry-2026-11-17-pm/news/industrial.jsonl')]
def S(d,o,u,nid,t): return dict(d=d,o=o,u=u,nid=nid,t=t)
PA='https://www.bloomberg.com/news/newsletters/2026-11-14/paper-makers-are-starting-to-crumple-as-rising-costs-bite'
CN='https://www.bloomberg.com/news/features/2026-11-16/china-bets-on-zero-carbon-industrial-parks'
HW='https://t.me/habit4117/88035'
HS='https://t.me/sunstudy1111/139396'
state={
 'materials':[S('2026-11-14','블룸버그',PA,'n-bbg-0902','이란 관련 분쟁에 따른 에너지 비용 상승과 톤당 10~30달러의 펄프 해상운송 할증료로 제지업체들이 흔들리기 시작했고, 북미·유럽에서는 펄프·판지 공장 폐쇄·가동 중단이 잇따릅니다 [사실]'),
              S('2026-11-16','텔레그램 선진짱 주식공부방',HS,'n-tg-0862','반도체 특수가스·전해질 소재를 만드는 불소화학 업체 후성의 3분기 연결 영업이익은 361억 원으로 1년 전보다 522.1% 늘고 컨센서스를 48.5% 웃돌았다는 전언입니다 [채널]')],
 'shipbuild':[S('2026-11-16','텔레그램 습관이 부자를 만든다',HW,'n-rtr-0692','한화디펜스USA는 한화시스템이 가진 필리조선소 지분 60%를 1,684억 원에 사들이고, 한화는 10월 필리조선소 인수 뒤 첫 해군 신조인 중형상륙함 2억 6,900만 달러 계약을 따냈습니다 [사실]')],
 'construction':[S('2026-11-16','블룸버그',CN,'n-bbg-0907','중국은 2025년 12월 국가급 무탄소 산업단지 1차 52곳을 지정했고 2030년까지 약 100곳으로 늘릴 계획이며, 52곳 가운데 24곳이 주요 무탄소 사업을 추진 중입니다 [사실]')],
}
IS=[
 dict(d='2026-11-14',kind='price',o='블룸버그',u=PA,nid='n-bbg-0902',t='펄프 해상운송 할증료는 톤당 10~30달러에 이르렀고, 알리안츠는 제지 업황 회복이 수요보다 공급 축소에 기대 수익성이 과거 수준을 밑돈다고 봤습니다 [사실]'),
 dict(d='2026-11-16',kind='policy',o='블룸버그',u=CN,nid='n-bbg-0907',t='중국 국가급 무탄소 산업단지는 1차 52곳(추진 24곳·준비 24곳·청사진 확정 4곳)이고, 2030년까지 약 100곳이 목표입니다 [사실]'),
]
gaps=p['gaps']+' 11월 17일 저녁 업데이트도 검색·열람 없이 입력 뉴스 4건으로만 반영했습니다. 제지업체 원가 압박 기사는 제목과 업계 보도 수준이라 폐쇄된 공장 이름과 능력은 확인하지 못했고, 후성 실적은 텔레그램 전언이며, 중국 무탄소 산업단지의 투자 규모와 장비 발주는 확인하지 못했습니다. HD 키위트 조선소의 투자 규모·부지는 여전히 공개되지 않았습니다.'
out=dict(id='industrial',summary='',state=state,industryState=IS,flags=[],insight={},cycle=None,nodeStage={},gaps=gaps,
 note='뉴스 4건 반영: 제지업체 에너지·운송 원가 압박과 북미·유럽 공장 폐쇄, 후성 3분기 영업익 361억 원, 중국 무탄소 산업단지 52곳·2030년 100곳 목표. 국면 ② 그대로, 근거 4줄, 수치 2줄, 재검토 신호 0건, 검색 0회',
 applied=ids,searches=0,fetches=0)
json.dump(out,open(f'{B}/data/industry-2026-11-17-pm/out/industrial.json','w'),ensure_ascii=False,indent=1)
