import json
B='/home/user/news-desk'
p=json.load(open(f'{B}/work/nightly-2026-11-17/chains/metals.json'))
ids=[json.loads(l)['id'] for l in open(f'{B}/data/industry-2026-11-17-pm/news/metals.jsonl')]
def S(d,o,u,nid,t): return dict(d=d,o=o,u=u,nid=nid,t=t)
IO1='https://www.bloomberg.com/news/articles/2026-11-16/chinese-iron-ore-futures-hit-four-year-low-on-weak-steel-outlook'
IO2='https://www.bloomberg.com/news/articles/2026-11-16/china-s-iron-ore-clout-may-cost-australian-miners-8-billion-goldman-says'
IO3='https://www.bloomberg.com/news/newsletters/2026-11-16/china-s-steel-mills-brace-for-a-bitter-winter'
EN='https://www.bloomberg.com/news/articles/2026-10-22/chile-tormentas-de-el-nino-amenazan-el-cobre-y-los-cultivos-mvjo9iw8'
NI1='https://www.bloomberg.com/news/articles/2026-11-16/indonesia-says-70-of-benefits-from-mines-should-go-to-state'
NI0='https://www.bloomberg.com/news/articles/2026-10-20/chinese-nickel-firms-plan-to-discuss-cutting-indonesian-output'
NI2='https://t.me/The_MariTimes/64659'
NOV='https://www.bloomberg.com/news/articles/2026-11-15/novelis-cuts-china-exposure-with-265-million-sale'
AL1='https://www.bloomberg.com/news/articles/2026-11-16/giant-aluminum-squeeze-is-stress-test-for-lme-s-anti-abuse-rules'
AL2='https://www.bloomberg.com/news/articles/2026-11-16/chinese-aluminum-output-drops-but-still-on-course-for-record'
G1='https://t.me/Trillion_labs/12133'
G2='https://www.bloomberg.com/news/articles/2026-11-16/goldman-forecasts-gold-to-take-two-years-to-recapture-all-time-highs'
CU='https://www.bloomberg.com/news/articles/2026-11-16/copper-sinks-to-four-month-low-on-tech-rout-china-growth-woes'
CU0='https://t.me/PipeBeom/6929'
state={
 'ironore':[S('2026-11-16','블룸버그',IO1,'n-bbg-0124','중국 철광석 선물이 철강 전망 부진에 4년 만의 최저로 떨어졌고, 골드만삭스는 CMRG의 구매력에 호주 대형 광산들이 10년간 약 80억 달러의 이익을 잃을 수 있다고 봤습니다 [사실]'),
            S('2026-11-16','블룸버그',IO2,'n-bbg-0124','호주 정부는 철광석 교역 조작 가능성이 국제 규칙 위반이자 세수 위협이라고 경고했지만 CMRG와의 계약 협상에는 개입하지 않기로 했습니다 [사실]')],
 'steel':[S('2026-11-16','블룸버그',IO3,'n-bbg-0124','중국 제철소들이 철강 전망 부진 속에 혹독한 겨울에 대비하고 있다는 보도가 나와, 중국 철강 수요 약세가 철광석값을 끌어내리고 있습니다 [제목]')],
 'copper':[S('2026-11-16','블룸버그',CU,'n-tg-0791','LME 3개월물 구리는 11월 16일 0.9% 내린 톤당 1만 3,280달러로 장중 7월 8일 이후 최저까지 밀렸고, AI 관련 매도와 중국 10월 산업생산 증가율 4.8%(예상 5.3%)가 압박했습니다 [사실]'),
           S('2026-10-23','블룸버그',EN,'n-bbg-0350','엘니뇨 폭우가 멕시코에서 칠레까지 덮쳐 칠레 로스펠람브레스 구리광산이 멈췄다는 전언이고, 미 기후예측센터는 1~3월에도 강한 엘니뇨가 이어진다고 봤습니다 [채널]')],
 'aluminum':[S('2026-11-12','블룸버그',AL1,'n-bbg-0903','LME 알루미늄 현물·3개월물 백워데이션은 11월 12일 톤당 176.80달러로 1990년 11월 이후 가장 컸고, 두 주체가 가용 재고의 60~80%만큼 롱 포지션을 쥐었습니다 [사실]'),
             S('2026-11-14','블룸버그',NOV,'n-bbg-0898','노벨리스가 창저우 자동차 판재 공장을 포함한 중국 사업 2곳(2026 회계연도 순매출 3억 7,600만 달러)을 선전훙즈산업투자에 약 2억 6,500만 달러에 팔기로 했습니다 [사실]')],
 'battery':[S('2026-11-15','텔레그램 Polaristimes',NI2,'n-bbg-0622','인도네시아 주재 중국 대사관은 니켈 수출 통제와 생산 쿼터 강화가 전기차 배터리 채산성을 위협해 500억 달러 투자에 영향을 줄 수 있다고 했고, 2026년 니켈 광석 쿼터는 전년 3억 7,900만 톤에서 줄었습니다 [사실]')],
 'policy':[S('2026-11-16','블룸버그',NI1,'n-bbg-0622','프라보워 대통령은 11월 14일 광산 허가에서 나오는 이익의 최소 70%를 국가가 가져야 하고 모든 수출은 지정 기관 한 곳을 거쳐야 한다고 했지만, 기준과 시행 일정은 밝히지 않았습니다 [사실]')],
 'precious':[S('2026-11-16','텔레그램 트릴리온',G1,'n-tg-0124','중국 인민은행은 10월 금 약 25.8톤을 사들여 24개월 연속 매입했고 보유량은 약 2,435톤으로, 2024년 11월 매입 재개 이후 월간 최대였습니다 [사실]'),
             S('2026-11-17','블룸버그',G2,'n-tg-0124','골드만삭스는 연준 긴축 부담에 금값이 사상 최고를 되찾기까지 약 2년 걸려 2028년 말 5,600달러에 이를 것으로 봤습니다 [사실]')],
}
IS=[
 dict(d='2026-11-16',kind='price',o='블룸버그',u=CU,nid='n-tg-0791',t='LME 3개월물 구리는 11월 16일 톤당 1만 3,280달러(장중 1만 3,210.5달러)로 4개월 최저였지만, 상하이선물거래소 재고는 한 주 새 18% 줄고 양산항 프리미엄은 톤당 약 285~290달러로 사상 최고 부근입니다 [사실]'),
 dict(d='2026-11-12',kind='price',o='블룸버그',u=AL1,nid='n-bbg-0903',t='LME 알루미늄 현물·3개월물 백워데이션은 11월 12일 톤당 176.80달러로 1990년 11월 이후 최대였고, 16일에도 175달러를 넘었습니다 [사실]'),
 dict(d='2026-11-16',kind='supply',o='블룸버그',u=NI1,nid='n-bbg-0622',t='인도네시아의 2026년 니켈 광석 쿼터는 2억 6,000만~2억 7,000만 습톤으로 전년 3억 7,900만 톤에서 줄었고, 인도네시아는 지난해 세계 니켈의 약 3분의 2인 약 260만 톤을 캤습니다 [사실]'),
 dict(d='2026-11-16',kind='demand',o='텔레그램 트릴리온',u=G1,nid='n-tg-0124',t='중국 인민은행 금 보유량은 10월 말 7,830만 온스(약 2,435톤)로 83만 온스 늘었고, 1~10월 매입은 약 129톤입니다 [사실]'),
]
flags=[dict(nid='n-bbg-0124',t='재검토 필요: 중국 철광석 선물 4년 최저와 CMRG 구매력에 따른 호주 광산 80억 달러 이익 손실 추정은 철광석 노드가 ③ 공급 과잉에서 ④ 수익 악화 쪽으로 옮겨 감을 가리키며, 가격 결정력이 구매자에게 넘어가기 때문입니다 [유추]'),
       dict(nid='n-tg-0791',t='재검토 필요: LME 구리가 4개월 최저(1만 3,280달러)로 밀린 것은 구리 노드가 ① 호황에서 ③ 공급 과잉·조정 쪽으로 기울 수 있음을 가리키지만, 상하이 재고 감소와 양산항 프리미엄 최고는 실물이 아직 빠듯하다는 반대 신호입니다 [유추]')]
old=p['insight']
a=[dict(t='국가가 광산 이익과 지분을 직접 쥐려는 흐름이 넓어집니다. 세계은행의 핵심광물 금융 5배 목표, 프랑스 정부의 에라멧 지분 최대 49%에 이어, 인도네시아 프라보워 대통령은 광산 허가 이익의 최소 70%를 국가 몫으로 하고 수출을 지정 기관 한 곳으로 모으라고 했습니다 [귀납]',
   src=[s for s in old['a'][0]['src'][:2]]+[dict(o='블룸버그',d='2026-11-16',u=NI1)]),
   {k:v for k,v in old['a'][1].items() if k!='rev'},
   dict(t='중국은 구매자 쪽에서 가격 결정력을 모읍니다. 중국 제철소 절반 넘게의 구매를 맡는 CMRG의 협상력에 골드만삭스는 호주 대형 철광석 광산의 10년 이익 손실을 약 80억 달러로 봤고, 호주 정부는 경고만 하고 개입하지 않기로 했습니다 [사실]',
   src=[dict(o='블룸버그',d='2026-11-16',u=IO2)])]
c=[dict(t='구리 쪽 반대 신호가 커졌습니다. LME 3개월물은 11월 16일 톤당 1만 3,280달러로 4개월 최저였고, AI 관련 매도와 중국 10월 산업생산 둔화가 겹쳤으며, 맥쿼리는 구리값이 공급 여건을 넘어섰다고 봤습니다 [사실]',
   src=[dict(o='블룸버그',d='2026-11-16',u=CU),dict(o='텔레그램 상상인 김진범',d='2026-10-30',u=CU0)]),
   {k:v for k,v in old['c'][1].items() if k!='rev'},
   dict(t='철광석은 반대 신호가 더 짙어졌습니다. 중국 철광석 선물은 11월 16일 4년 만의 최저로 떨어졌고 중국 제철소들은 혹독한 겨울에 대비하며, 발레 분광 실현가격은 3분기 톤당 85.10달러로 10% 내렸습니다 [사실]',
   src=[dict(o='블룸버그',d='2026-11-16',u=IO1)]+[s for s in old['c'][2]['src'] if 'vale' in s['u']])]
summary=('금속·광물 산업은 광산에서 철광석·구리·리튬·금 같은 광석을 캐 제련·정련을 거쳐 철강·전기동·알루미늄·배터리 소재로 만들고 건설·전력망·자동차·배터리 업체에 파는 사슬이며, 가격은 거래소와 가격 지수가, 공급은 광산 리드타임과 자원국 정책이 정합니다. '
 '11월 중순 가장 빠듯한 곳은 실물 구리와 알루미늄입니다. 칠레 3분기 구리 생산이 20여 년 만의 최악이었고 상하이 구리 재고는 한 주 새 18% 줄어 양산항 프리미엄이 톤당 약 285~290달러로 사상 최고 부근이며, LME 알루미늄 백워데이션은 톤당 176.80달러로 1990년 이후 최대입니다. '
 '다만 LME 구리 선물은 기술주 급락과 중국 성장 둔화에 1만 3,280달러로 4개월 최저까지 밀려 선물과 실물이 엇갈립니다. '
 '남는 쪽은 철광석·철강으로, 중국 철광석 선물이 4년 만의 최저로 떨어졌고 CMRG의 구매력이 호주 광산 이익을 누릅니다. '
 '배터리 금속은 인도네시아가 니켈 쿼터를 줄이고 광산 이익의 70%를 국가 몫으로 요구해 공급 정책 위험이 커졌고, 금은 1년 최저 뒤 중국 인민은행이 10월 약 26톤을 사들였습니다.')
gaps=p['gaps']+' 11월 17일 저녁 업데이트도 검색·열람 없이 입력 뉴스 8건으로만 반영했습니다. 인도네시아 70% 국가 몫이 매출·이익 중 무엇 기준인지와 시행 일정, LME 알루미늄 롱 포지션 보유 주체, 중국 10월 알루미늄 생산량(기사 제목뿐), 로스펠람브레스 광산 중단 기간(채널 전언), 골드만의 호주 광산 손실 추정 범위(매체에 따라 90억~100억 달러)는 확인하지 못했습니다. 엘니뇨의 코코아·설탕·파나마운하 영향은 금속 사슬과 직접 닿지 않아 반영하지 않았고, 에스토니아 국경 폐쇄 뉴스도 금속 수급과 닿지 않아 반영하지 않았습니다.'
out=dict(id='metals',summary=summary,state=state,industryState=IS,flags=flags,insight=dict(a=a,c=c),cycle=None,nodeStage={},gaps=gaps,
 note='뉴스 8건 반영: LME 구리 4개월 최저 1만 3,280달러 대 양산항 프리미엄 최고, LME 알루미늄 백워데이션 1990년 이후 최대, 중국 철광석 선물 4년 최저·인니 광산 이익 70% 국가 몫. 국면 ② 그대로, 근거 11줄, 수치 4줄, 재검토 신호 2건, 인사이트 a·c 고침, 검색 0회',
 applied=ids,searches=0,fetches=0)
json.dump(out,open(f'{B}/data/industry-2026-11-17-pm/out/metals.json','w'),ensure_ascii=False,indent=1)
