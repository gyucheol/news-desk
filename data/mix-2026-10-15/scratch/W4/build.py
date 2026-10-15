import json, re

OUT = '/home/user/news-desk/data/mix-2026-10-15/out2/W4.json'
TB = ' (제목 기준)'

def it(t, o, d, u, s=None):
    x = {"t": t, "o": o, "d": d, "u": u}
    if s is not None:
        x["s"] = s
    return x

items = []

# G1-016
items.append({
 "cid": "G1-016", "attachTo": "n-rtr-0287",
 "title": "中 9월 수출 36.3% 급증, 예상 25.5% 크게 웃돌아…무역흑자 1,335억 달러",
 "one": "중국 9월 수출이 반도체·자동차 등 첨단 제품 호조로 전년 대비 36.3% 늘어 예상치 25.5%를 크게 웃돌고 무역흑자가 1,335억 달러로 불어나면서, 1~9월 흑자가 9,381억 달러에 이르러 EU 등 교역국의 무역 불균형 압박이 커질 수 있다",
 "facts": [
  "무엇이: 중국 9월 수출은 달러 기준 전년 대비 36.3% 늘어 4,471억 8,000만 달러로, 이코노미스트 예상 25.5%와 8월 25%를 크게 웃돌았다 [사실]",
  "수입·흑자: 수입은 31% 늘었고 9월 무역흑자는 1,335억 달러로 8월 1,191억 달러보다 커졌으며, 1~9월 누적 흑자는 9,381억 달러였다 [사실]",
  "반도체: 집적회로 수출액은 136% 늘었지만 수출 물량은 1% 증가에 그쳐 가격 효과가 컸다 [사실]",
  "품목·지역: 반도체·컴퓨팅 장비가 수출 증가율에 13%p 넘게 기여했고 자동차 출하는 56.3%, 동남아향 수출은 52.3%, 미국향은 40.0% 늘었으며 EU향 증가율은 25.3%로 뛰었다 [채널]",
  "내수: 9월 소비자물가는 0.9% 올라 예상 1.0%를 밑돌았고, 3분기 성장률은 4.4%로 예상된다 [채널]"
 ],
 "basis": "verified",
 "check": "검색 결과 요약으로 확인(AP·Fortune·IndexBox): 수출 36.3%, 수입 31%, 9월 흑자 1,335억 달러, 1~9월 9,381억 달러, 집적회로 금액 136%·물량 1%. 품목·지역별 기여도와 9월 CPI는 텔레그램(WSJ 인용) 전언으로만 확인",
 "src": [
  {"o": "IndexBox", "d": "2026-10-14", "u": "https://www.indexbox.io/blog/chinas-september-exports-surge-363-as-trade-surplus-hits-1335-billion/"},
  {"o": "Fortune", "d": "2026-10-14", "u": "https://fortune.com/2026/10/14/chinas-trade-surplus-eu-rebalance/"},
  {"o": "ABC News(AP)", "d": "2026-10-14", "u": "https://abcnews.com/Business/wireStory/chinas-exports-surge-363-september-pressure-ramps-rebalance-137246052"}
 ],
 "inds": ["macro"], "nodes": ["macro/growth", "macro/semis"],
 "vc": [
  {"ind": "macro", "node": "growth", "f": "수요", "dir": "up", "k": "실제", "t": "중국 9월 수출 36.3% 급증, 예상 크게 상회"},
  {"ind": "macro", "node": "semis", "f": "가격", "dir": "up", "k": "실제", "t": "중국 집적회로 수출액 136% 증가, 물량은 1% 증가"}
 ],
 "added": "이번 블룸버그·로이터 5건과 텔레그램 2건으로 실제 9월 수출이 36.3% 늘어 예상 25.5%를 크게 웃돌고 무역흑자가 1,335억 달러로 불었다는 결과가 추가됐다",
 "items": [
  it("中 수출 급증에 무역흑자 사상 최대 기록 근접", "블룸버그", "2026-10-14", "https://www.bloomberg.com/news/articles/2026-10-14/china-s-trade-surplus-nears-940-billion-as-export-growth-surges",
     "중국 수출이 급증하면서 1~9월 무역흑자가 9,381억 달러로 불어나 연간 사상 최대 기록을 새로 쓸 수 있는 수준에 다가섰다"),
  it("中 9월 수출 36.3%·수입 31% 서프라이즈, 수출입 첫 월 5조 위안 돌파", "텔레그램 하나증권 중국전략", "2026-10-14", "https://t.me/HANAchina/70394",
     "중국 9월 수출입이 모두 예상을 웃돌아 수출입 총액이 처음 월 5조 위안을 넘으면서, 집적회로 수출이 136% 늘고 한국·대만향 수출이 크게 늘었다"),
  it("치솟는 中 수출, 교역 상대국 반발 키울 수도", "블룸버그", "2026-10-14", "https://www.bloomberg.com/news/newsletters/2026-10-14/china-s-soaring-exports-may-mean-more-pushback-from-trade-partners",
     "중국 수출이 치솟으면서 교역 상대국들이 중국산 제품에 맞서 반발을 키울 수 있다는 분석이 나왔다" + TB),
  it("中 9월 수출 전년 대비 36.3% 급증, 수입은 31% 증가", "로이터", "2026-10-14", "https://www.reuters.com/world/asia-pacific/chinas-exports-surge-363-yy-september-imports-up-31-2026-10-14/",
     "중국 9월 수출이 전년 대비 36.3%, 수입이 31% 늘면서 두 지표 모두 시장 예상을 크게 웃돌았다"),
  it("WSJ \"中 수출 가속, 반도체 기여 13%p…EU 무역 마찰 우려\"", "텔레그램 상상인 김진범", "2026-10-15", "https://t.me/PipeBeom/6707",
     "WSJ 인용으로 반도체·컴퓨팅 장비가 수출 증가율에 13%p 넘게 기여하고 EU향 수출 증가율이 25.3%로 뛰면서, 중·EU 무역 마찰 우려가 커졌다"),
  it("이번 中 수출 호황은 정말로 지속될 동력이 있다", "로이터", "2026-10-15", "https://www.reuters.com/world/china/this-chinese-export-boom-really-has-legs-wings-2026-10-15/",
     "로이터 칼럼이 이번 중국 수출 호황은 일시적이지 않고 오래 이어질 힘이 있다고 진단하면서, 교역국의 대응 부담이 길어질 수 있다" + TB),
  it("이번 中 수출 호황은 정말로 지속될 동력이 있다(소비재 면 재게재)", "로이터", "2026-10-15", "https://www.reuters.com/business/retail-consumer/this-chinese-export-boom-really-has-legs-wings-2026-10-15/",
     "로이터가 같은 칼럼을 소비재 면에 다시 실으며 중국 수출 호황이 계속될 동력이 있다고 봐, 교역국 압박 논의가 이어질 수 있다" + TB),
 ]
})

# G1-019
items.append({
 "cid": "G1-019", "attachTo": "n-tg-0277",
 "title": "IMF \"성장만으론 부채 못 줄여\"…국채 금리 상승에 재정 긴축 촉구",
 "one": "IMF가 재정점검보고서에서 선진국 재정적자가 올해 GDP의 5.2%에 이르고 국채 금리 상승이 재정 압박을 키운다며 긴축을 촉구하고 게오르기에바 총재도 성장만으로는 미국 부채를 줄일 수 없다고 하면서, 선진국 재정 건전화 압박이 커지고 있다",
 "facts": [
  "무엇이: IMF는 10월 14일 재정점검보고서에서 재정 위험이 커지고 있다며 선진국 재정적자가 2026년 GDP의 5.2%에 이를 것으로 봤다 [사실]",
  "미국: IMF는 미국 일반정부 적자를 2026년 GDP의 8.5%로 전망했고, 게오르기에바 총재는 성장만으로는 조정을 충분히 빨리 해낼 수 없다며 적자를 줄이는 긴축 쪽으로 가야 한다고 했다 [사실]",
  "금리: IMF는 국채 금리 상승이 재정 압박을 더한다고 했고, 미국 10년물 금리는 5.2% 안팎으로 2002년 이후 최고권이었다 [사실]",
  "국가별: 미국 2027년 적자 비율이 6.1%로 5대 선진국 중 가장 크고 독일 4.1%, 일본 2.5%, 프랑스 5.2%로 커지며 영국만 3.1%로 줄 것이라는 전망이 전해졌다 [채널]",
  "드라기: 드라기는 의회가 적자를 억제하면 AI가 미국 부채 안정에 도움이 될 수 있다고 했다 [제목]"
 ],
 "basis": "partial",
 "check": "검색 결과 요약으로 확인(CNBC·Fortune·IMF 미디어센터): 선진국 적자 5.2%, 미국 8.5%(2차 보도 기준), 게오르기에바 발언, 미 10년물 5.2%. 텔레그램의 국가별 2027년 적자 비율과 드라기 발언은 확인 못 함",
 "src": [
  {"o": "CNBC", "d": "2026-10-14", "u": "https://cnbc.com/2026/10/14/bond-yields-debt-deficit-treasury.html"},
  {"o": "Fortune", "d": "2026-10-14", "u": "https://fortune.com/2026/10/14/imf-us-nations-global-debt-economic-growth"},
  {"o": "IMF 미디어센터", "d": "2026-10-14", "u": "https://mediacenter.imf.org/news/imf---fiscal-monitor-report-annual-meetings--2026/s/1b05cec6-cde8-4b75-80ec-2b29f9fb5d19"}
 ],
 "inds": ["macro"], "nodes": ["macro/fiscal", "macro/rates"],
 "vc": [
  {"ind": "macro", "node": "fiscal", "f": "공급", "dir": "up", "k": "예상", "t": "선진국 적자 GDP 5.2%로 국채 공급 부담 확대"},
  {"ind": "macro", "node": "rates", "f": "가격", "dir": "up", "k": "실제", "t": "미 10년물 5.2% 안팎, 2002년 이후 최고권"}
 ],
 "added": "이번 블룸버그 3건·로이터 2건·텔레그램 1건으로 게오르기에바 총재의 성장만으론 미국 부채를 못 줄인다는 발언과 금리 상승이 긴축을 시급하게 만든다는 경고가 추가됐다",
 "items": [
  it("美 2027년 재정적자 비율 6.1% 전망…5대 선진국 중 최대", "텔레그램 하나증권 중국전략", "2026-10-14", "https://t.me/HANAchina/70386",
     "미국 재정적자가 2027년 GDP의 6.1%로 5대 선진국 중 가장 크고 독일·일본·프랑스도 커지면서, 영국만 적자 비율이 줄 것이라는 전망이 전해졌다"),
  it("IMF \"美 성장만으로는 높은 부채·적자 대응 못 해\"", "블룸버그", "2026-10-14", "https://www.bloomberg.com/news/articles/2026-10-14/imf-says-us-growth-not-enough-to-fight-high-debt-deficit-levels",
     "IMF가 미국 경제 성장만으로는 높은 부채와 적자를 줄이기에 충분하지 않다고 하면서, 적자 감축 압박이 커졌다"),
  it("IMF \"높은 부채·금리의 악순환에 갇힌 정부들\"", "블룸버그", "2026-10-14", "https://www.bloomberg.com/news/newsletters/2026-10-14/feedback-loop-ensnares-governments-with-debt-and-yields-high-imf-says",
     "IMF가 높은 부채와 국채 금리가 서로를 키우는 악순환에 정부들이 갇혔다고 경고하면서, 재정 여력이 더 좁아질 수 있다" + TB),
  it("게오르기에바 IMF 총재 \"美 성장만으론 부채 축소 불충분\"", "로이터", "2026-10-14", "https://www.reuters.com/world/us/imfs-georgieva-says-us-growth-will-not-be-enough-shrink-debt-2026-10-14/",
     "게오르기에바 총재가 성장은 도움이 되지만 조정을 충분히 빨리 해낼 수 없다며 적자를 줄이는 긴축 쪽으로 가야 한다고 했다"),
  it("IMF \"국채 금리 상승, 재정 건전화 시급성 부각\"", "로이터", "2026-10-14", "https://www.reuters.com/world/china/imf-says-higher-bond-yields-underscore-urgency-fiscal-consolidation-2026-10-14/",
     "IMF가 국채 금리 상승이 재정 압박을 더한다며 재정 건전화를 미룰수록 필요한 조정 폭이 커진다고 경고했다"),
  it("드라기 \"의회가 적자 억제하면 AI가 美 부채 안정 도울 수 있어\"", "블룸버그", "2026-10-15", "https://www.bloomberg.com/news/articles/2026-10-15/draghi-says-ai-can-help-us-steady-debt-if-congress-curbs-deficit",
     "드라기가 미국 의회가 적자를 억제한다면 AI에 따른 성장이 미국 부채 안정에 도움이 될 수 있다고 했다" + TB),
 ]
})

# G1-028
items.append({
 "cid": "G1-028", "attachTo": "",
 "title": "연준 베이지북 \"전 지역서 유가 상승 영향\"…경유값 공급망 전가, 4곳 물가 가속",
 "one": "연준 베이지북이 12개 지역 모두에서 유가 상승 영향이 나타나고 경유 유류할증료가 공급망 전반으로 전가되며 4개 지역은 물가 상승 속도가 빨라졌다고 밝히면서, 10월 말 FOMC를 앞두고 금리 인상 압력이 커질 수 있다",
 "facts": [
  "무엇이: 연준은 10월 14일 베이지북에서 모든 지역 보고에 유가 상승 영향이 나타났고, 기업들이 높은 경유 가격과 유류할증료로 오른 비용을 공급망 전반에 넘기고 있다고 밝혔다 [사실]",
  "물가: 3개 지역은 물가 상승이 강하다고, 8개 지역은 완만하다고 했고 4개 지역은 직전 보고 이후 상승 속도가 빨라졌으며, 여러 지역 기업은 계약·헤지 만료 뒤 가격이 더 오를 것으로 봤다 [사실]",
  "경기·고용: 경제활동은 지역별로 엇갈린 가운데 제조업이 버팀목이었고 고용은 대체로 변화가 없었으며, 5개 지역은 AI 투자로 생산성을 높인 뒤 채용을 늦추거나 줄인 기업이 있다고 했다 [사실]",
  "경유값: 미국 경유 평균 소매가는 지난달 갤런당 6.5달러를 넘어 사상 최고였다 [채널]",
  "시장: 10월 27~28일 FOMC의 금리 인상 확률은 보도 시점에 따라 37~44%로 전해졌다 [사실]"
 ],
 "basis": "verified",
 "check": "연준 이사회 베이지북 요약 페이지 열람으로 유가·경유 전가, 지역별 물가·고용 평가 확인. 인상 확률은 검색 결과 요약(2차 보도, 수치 엇갈림)으로 확인. 경유 평균 소매가 6.5달러는 텔레그램(서울경제) 전언",
 "src": [
  {"o": "연준 이사회 베이지북 요약", "d": "2026-10-14", "u": "https://www.federalreserve.gov/monetarypolicy/beigebook202610-summary.htm"},
  {"o": "BigGo Finance", "d": "2026-10-15", "u": "https://finance.biggo.com/news/77bebbc7-01ab-4847-802d-62928c39c2e7"}
 ],
 "inds": ["macro"], "nodes": ["macro/cb", "macro/inflation"],
 "vc": [
  {"ind": "macro", "node": "cb", "f": "가격", "dir": "up", "k": "예상", "t": "물가 압력 심화로 10월 FOMC 인상 확률 상승"},
  {"ind": "macro", "node": "inflation", "f": "가격", "dir": "up", "k": "실제", "t": "전 지역서 유가 상승 영향, 경유 할증료 전가"}
 ],
 "fed": [
  {"k": "", "who": "연준", "role": "연방준비제도", "kind": "조사·보고서", "stance": "",
   "t": "베이지북에서 12개 지역 모두 유가 상승 영향과 4개 지역 물가 가속을 보고했다", "d": "2026-10-15",
   "u": "https://www.bloomberg.com/news/articles/2026-10-14/fed-s-beige-book-shows-intensifying-price-growth-in-some-areas"}
 ],
 "added": "이번 텔레그램 2건으로 절반가량 지역의 물가 압력 심화와 미국 경유 평균 소매가가 지난달 갤런당 6.5달러를 넘어 사상 최고였다는 점이 추가됐다",
 "items": [
  it("연준 베이지북, 일부 지역에서 물가 상승세 심화", "블룸버그", "2026-10-15", "https://www.bloomberg.com/news/articles/2026-10-14/fed-s-beige-book-shows-intensifying-price-growth-in-some-areas",
     "연준 베이지북이 3개 지역은 물가 상승이 강하고 4개 지역은 속도가 빨라졌다고 보고하면서, 일부 지역의 물가 압력이 커졌다"),
  it("연준 조사, 연료비 상승 속에 물가 압력 심화", "로이터", "2026-10-15", "https://www.reuters.com/business/fed-survey-shows-price-pressures-intensifying-amid-rise-fuel-costs-2026-10-14/",
     "연준 조사에서 높은 경유값과 유류할증료가 공급망 전반으로 전가되면서, 기업들이 앞으로 가격이 더 오를 것으로 내다봤다"),
  it("베이지북, 유가 급격한 충격 경고…절반 지역 물가 압력 강화", "텔레그램 하나증권 중국전략", "2026-10-15", "https://t.me/HANAchina/70436",
     "베이지북이 절반가량 지역에서 물가 압력이 강하거나 심해졌다고 전하면서, 기업들이 가격 인상과 이익률 압박에 동시에 맞닥뜨렸다"),
  it("베이지북 \"美 전역 유가 상승…경유값 공급망 비용 전가\"", "텔레그램 부의 나침반", "2026-10-15", "https://t.me/w_compass/7330",
     "베이지북이 모든 지역에서 유가 상승 영향을 확인한 가운데 미국 경유 평균 소매가가 갤런당 6.5달러를 넘어 사상 최고를 기록해 물류비 부담이 커졌다"),
 ]
})

# G1-032
items.append({
 "cid": "G1-032", "attachTo": "n-bbg-0117",
 "title": "미 실업수당 청구 19만9000건 소폭 증가…5주째 20만 건 아래 '저해고' 지속",
 "one": "미국 신규 실업수당 청구가 10월 10일로 끝난 주 19만9000건으로 1000건 늘었지만 5주 연속 20만 건 아래에 머물고 계속 청구도 171만 건으로 줄면서, 9월 일자리 증가가 2만9000개에 그친 저채용·저해고 노동시장이 이어지고 있다",
 "facts": [
  "무엇이: 10월 10일로 끝난 주 신규 실업수당 청구는 19만9000건으로 수정치 19만8000건보다 1000건 늘었고 예상치 20만 건을 밑돌았다 [사실]",
  "추세: 청구는 5주 연속 20만 건 아래였고 4주 평균은 19만8500건으로 올랐다 [사실]",
  "계속 청구: 10월 3일로 끝난 주 계속 청구는 4000건 줄어 171만 건이었다 [사실]",
  "기존: 9월 비농업 일자리는 2만9000개 증가에 그쳤다 [사실]",
  "재고·채용: 8월 기업재고는 완만하게 늘었고, 신입 채용이 되살아나고 있을 수 있다는 분석이 나왔다 [제목]"
 ],
 "basis": "verified",
 "check": "검색 결과 요약으로 확인(미 노동부 보도자료·IndexBox·FXStreet): 청구 19만9000건, 4주 평균, 계속 청구 171만 건. 8월 기업재고와 신입 채용 분석은 제목 기준",
 "src": [
  {"o": "미 노동부 보도자료", "d": "2026-10-15", "u": "https://www.dol.gov/sites/dolgov/files/OPA/newsreleases/ui-claims/20261599.pdf"},
  {"o": "IndexBox", "d": "2026-10-15", "u": "https://www.indexbox.io/blog/us-jobless-claims-edge-up-to-199000-as-layoffs-stay-historically-low/"}
 ],
 "inds": ["macro"], "nodes": ["macro/growth"],
 "vc": [
  {"ind": "macro", "node": "growth", "f": "수요", "dir": "flat", "k": "실제", "t": "주간 실업수당 청구 19만9000건, 해고 낮은 수준 유지"}
 ],
 "added": "이번 로이터·블룸버그 3건으로 10월 둘째 주 청구가 19만9000건으로 소폭 늘었지만 5주째 20만 건 아래이고 계속 청구는 171만 건으로 줄었다는 점이 추가됐다",
 "items": [
  it("美 주간 실업수당 청구 소폭 증가…해고는 낮은 수준", "로이터", "2026-10-15", "https://www.reuters.com/world/us/us-weekly-jobless-claims-rise-marginally-amid-low-layoffs-2026-10-15/",
     "미국 신규 실업수당 청구가 19만9000건으로 1000건 늘었지만 5주째 20만 건 아래에 머물러 해고가 낮은 수준을 이어 갔다"),
  it("美 8월 기업재고, 완만한 증가세 기록", "로이터", "2026-10-15", "https://www.reuters.com/business/us-business-inventories-rise-moderately-august-2026-10-15/",
     "미국 기업재고가 8월에 완만하게 늘면서, 기업들의 재고 쌓기가 3분기 성장에 보탬이 될 수 있다" + TB),
  it("미국 신입 채용, 다시 되살아나고 있을 수도", "블룸버그", "2026-10-16", "https://www.bloomberg.com/news/newsletters/2026-10-15/entry-level-hiring-may-be-making-a-comeback",
     "얼어붙었던 신입 채용이 다시 살아나고 있을 수 있다는 분석이 나오면서, 저채용 노동시장에 변화 신호가 될 수 있다" + TB),
 ]
})

# G2-006
items.append({
 "cid": "G2-006", "attachTo": "n-rtr-0038",
 "title": "스페이스X, 우크라 스타실드 속도 제한…美 '지시 안 해'·유럽 위성 대안 모색",
 "one": "스페이스X가 우크라이나군 스타실드 단말기에 시속 160km 속도 제한을 걸어 드론 작전이 차질을 빚자 머스크는 미군과 대통령이 정한다고 했지만 백악관은 지시하지 않았다고 하면서, 유럽이 스페이스X 의존을 줄일 위성 대안을 서두르고 있다",
 "facts": [
  "무엇이: 스페이스X가 군용 스타실드 단말기가 시속 160km를 넘으면 연결이 끊기도록 제한해, 우크라이나는 사전 경고 없이 드론 작전 등이 차질을 빚었다고 밝혔다 [사실]",
  "책임 공방: 머스크는 스타실드를 미국 정부가 소유·통제하며 속도·사용 제한은 미군과 최종적으로 대통령이 정한다고 했고, 백악관 관계자들은 스페이스X를 통제하지 않으며 제한을 지시하지 않았다고 우크라이나에 전했다 [사실]",
  "복구: 페도로프 전 국방장관은 시속 160km까지의 연결이 복구됐다며 제한을 완전히 없애야 한다고 했고, 국방부는 제한 자체는 남아 있다고 했다 [사실]",
  "유럽: 시코르스키 폴란드 외무장관이 머스크를 비판했고 유텔샛 주가가 뛰었으며, EU 집행위는 스페이스X 대항 위성망을 신속 추진할 준비가 됐다 [제목]",
  "기존: 앞서 트럼프 행정부는 러시아 정유시설 공격을 이유로 우크라이나에 정보 공유·스타링크 차단을 거론하며 압박했다 [사실]"
 ],
 "basis": "verified",
 "check": "검색 결과 요약으로 확인(CNBC·Kyiv Independent·The Record·Fox News): 시속 160km 제한과 작전 차질, 머스크 발언, 백악관 부인(악시오스 보도), 일부 복구. EU 대항 위성망·유텔샛·영국 스트리팅 발언은 제목 기준",
 "src": [
  {"o": "CNBC", "d": "2026-10-15", "u": "https://www.cnbc.com/2026/10/15/elon-musk-starlink-ukraine-trump-energy-ceasefire.html"},
  {"o": "The Record", "d": "2026-10-15", "u": "https://therecord.media/ukraine-says-starshield-working-again-after-disruption"},
  {"o": "Kyiv Independent", "d": "2026-10-14", "u": "https://kyivindependent.com/this-cannot-be-a-coincidence-ukraines-starlink-access-restricted-without-warning-zelensky-adviser-says/"}
 ],
 "inds": ["macro", "tech", "aero"], "nodes": ["macro/geo"],
 "vc": [
  {"ind": "tech", "node": "telecom", "f": "공급", "dir": "down", "k": "실제", "t": "스타실드 시속 160km 넘으면 연결 차단"},
  {"ind": "aero", "node": "space", "f": "수요", "dir": "up", "k": "예상", "t": "EU, 스페이스X 대항 위성망 신속 추진 검토"}
 ],
 "added": "이번 블룸버그 5건·로이터 6건·텔레그램 7건으로 스타실드 시속 160km 속도 제한과 작전 차질, 머스크·백악관의 책임 공방, 일부 복구와 EU의 대항 위성망 추진이 추가됐다",
 "items": [
  it("스타링크, 우크라 단말기 이동 속도 제한…고속 이동 시 연결 끊겨", "텔레그램 미국 주식 인사이더", "2026-10-14", "https://t.me/insidertracking/66199",
     "스타링크가 우크라이나 내 단말기에 사용 제한을 걸어 시속 60km를 넘게 움직이면 연결이 끊기는 현상이 나타났다는 전언이 나왔다"),
  it("젤렌스키, 트럼프·머스크가 위성 사용을 제한했다고 비판", "블룸버그", "2026-10-14", "https://www.bloomberg.com/news/articles/2026-10-14/russia-hits-ukraine-energy-plants-in-blow-to-trump-s-truce-claim",
     "젤렌스키가 트럼프와 머스크가 위성 통신 사용을 조였다고 비판하면서, 미·우크라이나 갈등이 위성 서비스로 번졌다" + TB),
  it("스페이스X, 우크라 스타링크 운영 제한…군사 작전 차질", "로이터", "2026-10-14", "https://www.reuters.com/world/europe/spacex-limits-starlink-operations-ukraine-disrupting-military-missions-2026-10-14/",
     "스페이스X가 우크라이나의 스타링크 운영을 제한하면서 고속 이동 중인 드론·차량의 통신이 끊겨 군사 작전에 차질이 생겼다"),
  it("폴란드 시코르스키, 머스크에 '스타링크로 정치하나' 비판", "로이터", "2026-10-14", "https://www.reuters.com/business/media-telecom/polands-sikorski-asks-big-man-musk-if-he-is-playing-politics-with-starlink-2026-10-14/",
     "시코르스키 폴란드 외무장관이 머스크에게 스타링크로 정치를 하느냐고 따지면서, 유럽의 스타링크 신뢰 문제가 다시 불거졌다" + TB),
  it("스페이스X, 스타실드 시속 160km 제한…우크라 작전 차질", "텔레그램 트릴리온", "2026-10-14", "https://t.me/Trillion_labs/10478",
     "스페이스X가 군용 스타실드에 시속 160km 속도 제한을 걸어 고속 차량·드론 통신이 막히자, 우크라이나 국방부는 경고 없이 여러 작전이 차질을 빚었다고 했다"),
  it("시코르스키, 스타실드 제한 두고 머스크와 재충돌", "텔레그램 미국 주식 인사이더", "2026-10-14", "https://t.me/insidertracking/66240",
     "시코르스키 장관이 스타실드 속도 제한을 두고 머스크가 또 제품으로 정치를 한다고 비판하면서, 연간 약 720억 원의 이용료를 내는 폴란드가 대안을 언급해 왔다"),
  it("우크라 스타링크 군용 서비스 제한에 유텔샛 주가 급등", "로이터", "2026-10-15", "https://www.reuters.com/business/eutelsat-shares-jump-ukraine-flags-curbs-starlink-military-grade-service-2026-10-14/",
     "우크라이나가 스타링크 군용 서비스 제한을 알리자 유럽 위성 업체 유텔샛 주가가 뛰면서, 대체 위성망 수요 기대가 커졌다" + TB),
  it("美 초당파 우크라 코커스, 스타링크 제한·정보 중단 우려", "텔레그램 미국 주식 인사이더", "2026-10-15", "https://t.me/insidertracking/66291",
     "미 의회 초당파 우크라이나 코커스 의원들이 스타링크 제한과 정보 공유 중단이 우크라이나 민간인과 체류 미국인을 위험에 빠뜨릴 수 있다고 경고했다"),
  it("머스크 \"스타실드는 美 정부 소유·통제, 최종 결정은 대통령\"", "텔레그램 미국 주식 인사이더", "2026-10-15", "https://t.me/insidertracking/66293",
     "머스크가 스타실드는 미국 정부가 소유·통제하며 속도·사용 제한은 미군이 정하고 최종 결정권은 대통령에게 있다고 해 책임을 정부로 돌렸다"),
  it("머스크, 스타실드 제한 결정권은 미군·대통령에 있다고 거듭 설명", "텔레그램 미국 주식 인사이더", "2026-10-15", "https://t.me/insidertracking/66296",
     "같은 채널이 머스크의 스타실드 정부 통제 설명을 다시 전하면서, 속도 제한을 누가 결정했는지를 둘러싼 혼선이 이어졌다"),
  it("악시오스 \"백악관, 스페이스X 통제 못 하고 제한과 무관하다고 우크라에 전달\"", "텔레그램 미국 주식 인사이더", "2026-10-15", "https://t.me/insidertracking/66307",
     "젤렌스키 보좌관이 백악관에 차단 결정 여부를 묻자 백악관은 스페이스X를 통제할 수 없고 제한과 무관하다고 답해, 머스크 설명과 엇갈렸다"),
  it("우크라, 스페이스X가 드론 작전 마비시켰다고 비판…대미 관계 악화", "로이터", "2026-10-15", "https://www.reuters.com/business/media-telecom/ukraine-accuses-spacex-crippling-drone-missions-ties-with-us-worsen-2026-10-14/",
     "우크라이나가 스페이스X의 제한이 드론 작전을 마비시켰다고 비판하면서, 미국과의 관계가 더 나빠지고 있다" + TB),
  it("스타링크·美 위성정보에 매인 우크라, 유럽엔 빠른 대안 없어", "로이터", "2026-10-15", "https://www.reuters.com/business/media-telecom/ukraine-struggles-with-starlink-us-satellite-data-europe-has-no-quick-fix-2026-10-14/",
     "우크라이나가 스타링크와 미국 위성정보 문제로 어려움을 겪지만 유럽에는 이를 곧바로 대신할 수단이 없다는 분석이 나왔다" + TB),
  it("EU 집행위, 스페이스X 대항 위성망 신속 추진 준비", "블룸버그", "2026-10-16", "https://www.bloomberg.com/news/articles/2026-10-15/eu-commission-is-ready-to-fast-track-satellite-rival-to-spacex",
     "EU 집행위원회가 스페이스X에 맞설 위성망을 신속히 추진할 준비가 됐다고 하면서, 유럽 위성 산업에 새 수요가 생길 수 있다" + TB),
  it("머스크 게시글, 우크라 스타실드 차질 두고 혼란 키워", "블룸버그", "2026-10-16", "https://www.bloomberg.com/news/articles/2026-10-15/musk-comments-sow-confusion-over-ukraine-starshield-disruption",
     "머스크의 게시글이 스타실드 차질의 책임 소재를 두고 혼란을 키우면서, 누가 제한을 결정했는지 불분명해졌다" + TB),
  it("美 정부 \"트럼프, 우크라 스페이스X 접속 제한 지시 안 해\"", "블룸버그", "2026-10-16", "https://www.bloomberg.com/news/articles/2026-10-15/trump-didn-t-order-limits-on-kyiv-s-spacex-access-us-says",
     "미국 정부가 트럼프는 우크라이나의 스페이스X 접속 제한을 지시하지 않았다고 밝혀, 머스크의 대통령 결정 설명을 부인했다"),
  it("우크라 통신 장애, 머스크 스페이스X 의존 우려 재점화", "블룸버그", "2026-10-16", "https://www.bloomberg.com/news/newsletters/2026-10-15/ukraine-outage-revives-concerns-over-relying-on-musk-s-spacex",
     "우크라이나의 위성 통신 장애가 머스크의 스페이스X 한 곳에 의존하는 위험을 다시 드러내면서, 대체 공급원 논의가 커졌다" + TB),
  it("英 스트리팅 \"헤그세스와 우크라 스타링크 복구 환영\"", "로이터", "2026-10-16", "https://www.reuters.com/business/media-telecom/uks-streeting-says-he-hegseth-welcomed-starlink-restoration-ukraine-2026-10-15/",
     "영국 스트리팅이 헤그세스 미 국방장관과 함께 우크라이나 스타링크 복구를 환영했다고 밝혀, 서비스가 정상화 쪽으로 움직였다" + TB),
 ]
})

# G2-010
items.append({
 "cid": "G2-010", "attachTo": "",
 "title": "후티 공세에 사우디 흔들…EU-걸프 정상회의 연기, 프랑스 방공 배치",
 "one": "후티 반군의 사우디 공격이 이어져 리야드 킹칼리드 공항이 폐쇄되고 10월 24일 예정이던 EU-걸프 정상회의가 연기된 데다 프랑스가 석유시설 방어용 방공 시스템 배치를 시작하면서, 사우디 석유 공급과 현지 금융 업무에 차질 우려가 커지고 있다",
 "facts": [
  "무엇이: EU와 걸프협력회의(GCC)는 10월 24일 리야드에서 열려던 두 번째 정상회의를 연기했고 새 날짜는 정하지 않았다 [사실]",
  "이유: GCC는 계속되는 후티 위협과 킹칼리드 국제공항의 폐쇄 연장을 이유로 들었다 [사실]",
  "방어: 프랑스가 방위협력협정에 따라 사우디 석유시설을 지키려 병력과 방공 시스템 배치를 시작했다 [채널]",
  "여파: 사우디 공격으로 금융회사들이 직원 재택근무를 허용했고 순례객들도 공격에 휘말렸다 [제목]",
  "무기·중재: 후티가 중국산 부품으로 첨단 미사일을 만든다는 WSJ 보도와 오만·러시아·중국이 휴전 협상을 중재한다는 AP 보도가 전해졌다 [채널]"
 ],
 "basis": "verified",
 "check": "검색 결과 요약으로 확인(The National·Saudi Gazette·The New Arab): 10월 24일 리야드 정상회의 연기, 공항 폐쇄 연장. 프랑스 방공 배치는 The National이 프랑스·이탈리아의 사우디 방공 지원을 언급한 수준이라 세부는 채널 전언",
 "src": [
  {"o": "The National", "d": "2026-10-15", "u": "https://www.thenationalnews.com/news/mena/2026/10/15/gulf-eu-summit-in-riyadh-postponed-amid-houthi-attacks-on-saudi-arabia/"},
  {"o": "Saudi Gazette", "d": "2026-10-15", "u": "https://saudigazette.com.sa/article/665445/saudi-arabia/gcc-eu-summit-in-riyadh-postponed-over-houthi-attacks-and-airport-suspension"}
 ],
 "inds": ["macro", "oil", "aero"], "nodes": ["macro/geo"],
 "vc": [
  {"ind": "oil", "node": "opec", "f": "공급", "dir": "down", "k": "예상", "t": "후티 공세에 사우디 석유시설 방어 비상"},
  {"ind": "aero", "node": "defspend", "f": "수요", "dir": "up", "k": "실제", "t": "프랑스, 사우디에 병력·방공 시스템 배치 시작"}
 ],
 "added": "이번 텔레그램 1건으로 프랑스가 방위협력협정에 따라 사우디 석유시설을 지키려 병력과 방공 시스템 배치를 시작했다는 점이 추가됐다",
 "items": [
  it("WSJ \"후티, 중국산 부품으로 첨단 미사일 제작\"", "텔레그램 미국 주식 인사이더", "2026-10-14", "https://t.me/insidertracking/66183",
     "후티가 중국산 부품으로 첨단 미사일을 만들고 있다는 WSJ 보도가 전해지면서, 사우디를 향한 공격 능력이 커질 수 있다는 우려가 나왔다"),
  it("AP \"오만·러시아·중국, 후티 휴전 협상 중재 중\"", "텔레그램 트릴리온", "2026-10-14", "https://t.me/Trillion_labs/10480",
     "오만·러시아·중국이 후티 반군과의 휴전 협상을 중재하고 있다는 AP 보도가 전해지면서, 공세 완화 가능성이 거론됐다"),
  it("빈 살만, 후티 위협에 최대 위기 중 하나 직면", "블룸버그", "2026-10-14", "https://www.bloomberg.com/news/articles/2026-10-14/mbs-faces-houthi-menace-in-one-of-saudi-prince-s-biggest-crises",
     "후티의 위협이 커지면서 무함마드 빈 살만 사우디 왕세자가 집권 이후 가장 큰 위기 가운데 하나에 몰렸다" + TB),
  it("후티 공격 격화로 빈 살만 왕세자 중대 위기 맞아", "블룸버그", "2026-10-15", "https://www.bloomberg.com/news/newsletters/2026-10-14/houthi-attacks-escalate-leaving-mbs-facing-a-major-crisis",
     "후티의 공격이 격화하면서 빈 살만 왕세자가 안보와 경제 계획 모두에서 중대한 위기를 맞고 있다" + TB),
  it("사우디아라비아에서 후티 공격에 순례객들 휘말려", "로이터", "2026-10-15", "https://www.reuters.com/world/middle-east/pilgrims-caught-up-houthi-strikes-saudi-arabia-2026-10-14/",
     "후티의 사우디 공격에 순례객들까지 휘말리면서, 종교 관광 등 민간 활동으로 피해가 번지고 있다" + TB),
  it("EU·걸프, 후티 공격에 사우디 정상회의 연기", "블룸버그", "2026-10-15", "https://www.bloomberg.com/news/articles/2026-10-15/eu-gulf-states-expected-to-postpone-saudi-summit-over-attacks",
     "EU와 걸프 국가들이 후티 공격을 이유로 10월 24일 리야드 정상회의를 미루면서, 사우디의 외교 일정이 흔들렸다"),
  it("후티의 사우디 공격, 군사력 격차 무색하게 해", "블룸버그", "2026-10-15", "https://www.bloomberg.com/news/articles/2026-10-15/houthi-attacks-on-saudi-arabia-defy-difference-in-military-power",
     "후티의 사우디 공격이 두 세력 간 큰 군사력 격차에도 효과를 내면서, 사우디 방어 체계의 취약점이 드러났다" + TB),
  it("EU·걸프 국가, 사우디 개최 예정 정상회의 연기", "로이터", "2026-10-15", "https://www.reuters.com/world/middle-east/eu-gulf-states-postpone-summit-due-saudi-arabia-2026-10-15/",
     "GCC가 후티 위협과 킹칼리드 공항 폐쇄 연장을 들어 EU와의 정상회의를 미루고 새 날짜는 추후 정하기로 했다"),
  it("사우디 공격에 금융회사들, 직원 재택근무 허용", "로이터", "2026-10-15", "https://www.reuters.com/business/world-at-work/attacks-saudi-arabia-prompt-finance-firms-let-staff-work-home-sources-say-2026-10-15/",
     "사우디 공격이 이어지자 현지 금융회사들이 직원 재택근무를 허용하면서, 리야드 금융 업무가 위축될 수 있다" + TB),
  it("프랑스, 사우디 석유시설 보호 위해 병력·방공 시스템 배치", "텔레그램 미국 주식 인사이더", "2026-10-16", "https://t.me/insidertracking/66407",
     "프랑스가 방위협력협정에 따라 후티 드론·미사일로부터 사우디 석유시설을 지키려 병력과 방공 시스템을 배치하기 시작했다"),
 ]
})

# G2-026
items.append({
 "cid": "G2-026", "attachTo": "n-rtr-0284",
 "title": "신흥국 연료·전력난 확산…발리 연료 부족·PLN CEO 교체, 케냐 휘발유값 인상",
 "one": "에너지 비용 급등 속에 말라위·몰디브에 이어 인도네시아 발리가 연료 부족으로 사흘 재택근무를 명령하고 국영 전력사 PLN이 대정전 뒤 CEO를 바꿨으며 케냐도 휘발유 상한가를 올리면서, 연료 수입 신흥국의 물가·재정 압박이 커지고 있다",
 "facts": [
  "무엇이: 인도네시아 발리주는 연료 부족이 심해지자 10월 15~17일 재택근무와 온라인 수업을 명령했고, 에너지부 장관은 연료 재고가 20일분이라며 수요 이동과 보조 연료 오용을 탓했다 [사실]",
  "전력: 인도네시아 국영 전력사 PLN은 바탐에서 41만 1,000여 고객이 피해를 본 정전 뒤 다르마완 프라소조 CEO를 수로소 이스난다르로 교체했다 [사실]",
  "케냐: 에너지규제청(EPRA)은 10월 15일부터 나이로비 휘발유 상한가를 리터당 12.93실링 올린 226.96실링으로 정했고, 수입 휘발유 도착 원가는 11.81% 올랐다 [사실]",
  "기존: 말라위는 외화 부족으로 연료가 바닥나 주유소 밤샘 줄이 이어졌고, 몰디브는 에너지 비용 완충 재원 지원을 요청했다 [사실]",
  "식량: 인도네시아가 연료 공급을 확보하려 식량·삼림을 희생하고 있으며 팜유값 상승이 저소득 가구에 전가된다는 분석이 전해졌다 [채널]"
 ],
 "basis": "verified",
 "check": "검색 결과 요약으로 확인(Jakarta Globe·The Star·Tempo·The Star Kenya·EPRA): 발리 재택근무 명령, PLN CEO 교체와 바탐 정전, 케냐 휘발유 12.93실링 인상. 팜유·식량 분석은 채널 전언",
 "src": [
  {"o": "Jakarta Globe", "d": "2026-10-15", "u": "https://jakartaglobe.id/news/bali-orders-three-days-of-remote-work-online-classes-amid-fuel-shortage"},
  {"o": "The Star(말레이시아)", "d": "2026-10-15", "u": "https://www.thestar.com.my/aseanplus/aseanplus-news/2026/10/15/indonesia-replaces-state-electricity-chief-after-16-hour-blackout-in-batam"},
  {"o": "The Star(케냐)", "d": "2026-10-14", "u": "https://www.the-star.co.ke/news/2026-10-14-epra-raises-petrol-by-sh1293"}
 ],
 "inds": ["oil", "power"], "nodes": ["power/market"],
 "vc": [
  {"ind": "oil", "node": "products", "f": "공급", "dir": "down", "k": "실제", "t": "발리 연료 부족에 사흘 재택근무 명령"},
  {"ind": "oil", "node": "products", "f": "가격", "dir": "up", "k": "실제", "t": "케냐 휘발유 상한가 리터당 12.93실링 인상"},
  {"ind": "power", "node": "market", "f": "공급", "dir": "down", "k": "실제", "t": "바탐 대정전 뒤 PLN CEO 교체"}
 ],
 "added": "이번 블룸버그·로이터 3건과 텔레그램 1건으로 인도네시아 발리 연료 부족과 PLN CEO 교체, 케냐의 휘발유 상한가 인상이 추가됐다",
 "items": [
  it("인니 곳곳 연료 부족에 발리 운전자들 주유 행렬", "블룸버그", "2026-10-14", "https://www.bloomberg.com/news/articles/2026-10-14/bali-motorists-line-up-as-fuel-shortages-hit-parts-of-indonesia",
     "인도네시아 일부 지역에 연료 부족이 번져 발리 운전자들이 주유소에 줄을 서면서, 주정부가 사흘 재택근무를 명령했다"),
  it("인니 국영 전력사, 대규모 정전 속 CEO 교체", "로이터", "2026-10-15", "https://www.reuters.com/business/energy/indonesia-state-utility-firm-replaces-ceo-amid-widespread-power-outages-2026-10-15/",
     "인도네시아 PLN이 바탐 등 잇단 대규모 정전 뒤 다르마완 CEO를 수로소 이스난다르로 바꾸면서, 전력 공급 차질이 경영진 교체로 번졌다"),
  it("인도네시아, 식량·삼림 희생하며 연료 공급 확보", "텔레그램 트릴리온", "2026-10-15", "https://t.me/Trillion_labs/10544",
     "인도네시아가 식량과 삼림을 희생해 연료를 확보하면서 팜유값 상승이 노점·식당을 거쳐 저소득 가구의 식비 부담으로 번지고 있다는 분석이 전해졌다"),
  it("케냐, 중동 분쟁發 수입 비용 상승에 연료값 인상", "로이터", "2026-10-15", "https://www.reuters.com/world/africa/kenya-raises-fuel-prices-middle-east-conflict-lifts-import-costs-2026-10-15/",
     "케냐가 중동 분쟁으로 수입 원가가 오르자 나이로비 휘발유 상한가를 리터당 12.93실링 올리면서, 소비자 연료비 부담이 커졌다"),
 ]
})

# G2-049
items.append({
 "cid": "G2-049", "attachTo": "n-rtr-0275",
 "title": "한미 관계, 정보 공유 갈등에 최저점…美, 북한 정보 접근 일부 제한",
 "one": "미국이 정동영 통일부 장관의 북한 구성 우라늄 농축시설 공개 뒤 한국의 북한 관련 정보 접근을 일부 제한하고 핵추진 잠수함 협의도 멈춰 한미 관계가 최저점으로 떨어졌다는 평가가 나오면서, 대북 대응 공조에 부담이 커지고 있다",
 "facts": [
  "무엇이: 미국과 한국의 관계가 정보 공유 갈등으로 최저점에 이르렀다는 보도가 나왔다 [제목]",
  "발단: 정동영 통일부 장관이 3월 북한 구성의 우라늄 농축시설을 공개한 뒤 미국은 한국의 북한 관련 정보 접근을 일부 제한했다 [사실]",
  "현황: 강경화 주미대사는 10월 12일 진전이 있었다면서도 백악관과의 고위급 소통에 한계가 있다고 인정했고, 군 당국자는 원자료 공유는 계속되지만 일부 분석 정보는 제한된다고 했다 [사실]",
  "다른 마찰: 3,500억 달러 투자 합의에도 핵추진 잠수함 안보 협의가 멈춰 있다 [사실]"
 ],
 "basis": "partial",
 "check": "검색 결과 요약으로 확인(코리아헤럴드·코리아타임스·코리아중앙데일리): 정보 접근 제한 경위, 강경화 대사 발언, 잠수함 협의 정체. '최저점' 평가는 블룸버그 제목에만 있고 동맹 전반 균열로 보기 어렵다는 전문가 의견도 있음",
 "src": [
  {"o": "코리아헤럴드", "d": "2026-10-14", "u": "https://www.koreaherald.com/article/10901291"},
  {"o": "코리아중앙데일리", "d": "2026-10-14", "u": "https://www.koreajoongangdaily.com/korea/seoulwashington-intelligence-ties-appear-strained-as-security-talks-continue-to-stall/12913275"},
  {"o": "코리아타임스", "d": "2026-10-13", "u": "https://www.koreatimes.co.kr/foreignaffairs/20261013/s-korean-envoy-says-progress-made-in-intelligence-cooperation-with-us-amid-friction-concerns"}
 ],
 "inds": ["macro"], "nodes": ["macro/geo"],
 "vc": [
  {"ind": "macro", "node": "geo", "f": "-", "dir": "flat", "k": "실제", "t": "한미 정보 공유 갈등은 수급과 직접 무관한 동맹 마찰"}
 ],
 "added": "이번 블룸버그 1건으로 한미 관계가 정보 공유 갈등으로 최저점에 이르렀다는 평가와 미국의 북한 정보 일부 제한 경위가 추가됐다",
 "items": [
  it("미국과 한국의 관계, 정보 갈등으로 최저점", "블룸버그", "2026-10-16", "https://www.bloomberg.com/news/articles/2026-10-15/south-korea-us-ties-hit-lowest-ebb-in-years-on-intelligence-row",
     "미국과 한국의 관계가 정보 공유를 둘러싼 갈등으로 최저점에 떨어지면서, 동맹 공조에 부담이 커졌다는 보도가 나왔다" + TB),
 ]
})

# G3-018
items.append({
 "cid": "G3-018", "attachTo": "",
 "title": "英 힐리 재무장관, 이달 예산안서 은행세 인상 추진…추가세율 8% 환원 거론",
 "one": "존 힐리 영국 재무장관이 10월 28일 예산안에서 은행 과세를 높일 계획인 가운데 현재 3%인 은행 추가세율을 8%로 되돌리는 안이 거론되면서, 영국 은행들의 세 부담이 연 22억 5,000만 파운드가량 늘어날 수 있다",
 "facts": [
  "무엇이: 힐리 재무장관은 10월 28일 예산안에서 은행 세금을 올릴 계획이다 [사실]",
  "방안: 업계는 현재 3%인 은행 추가세율이 8%로 환원될 가능성이 크다고 보며, 영국노총(TUC)은 이 경우 연 22억 5,000만 파운드가 걷힐 것으로 추산했다 [사실]",
  "발언: 힐리는 은행이 영국 경제의 보석 가운데 하나라며 폭넓은 기여를 강조했지만, 예산안에서 결정을 내리겠다며 과세 여지를 남겼다 [사실]",
  "업계: 업계는 추가세율 인상을 받아들이는 분위기이고, 일부 은행은 추가세 적용 기준을 1억 파운드에서 5억 파운드로 올려 달라고 요청했다 [사실]"
 ],
 "basis": "verified",
 "check": "검색 결과 요약으로 확인(AOL·Yahoo·The British Eye): 10월 28일 예산안 은행세 인상 검토, 3%→8% 환원안, TUC 추산. 최종 결정은 아직 발표되지 않음",
 "src": [
  {"o": "AOL", "d": "2026-10-15", "u": "https://www.aol.co.uk/articles/john-healey-poised-raise-taxes-160035000.html"},
  {"o": "The British Eye", "d": "2026-10-15", "u": "https://thebritisheye.com/2026/10/15/uk-banks-potential-tax-rise-in-budget/"}
 ],
 "inds": ["fin", "macro"], "nodes": ["macro/fiscal"],
 "vc": [
  {"ind": "fin", "node": "banks", "f": "가격", "dir": "up", "k": "예상", "t": "영국 은행 추가세율 3%에서 8% 환원 거론"}
 ],
 "added": "이번 로이터·블룸버그 2건으로 힐리가 은행세 질문에 은행의 폭넓은 기여를 강조하면서도 이달 예산안에서 은행 과세를 올릴 계획이라는 점이 추가됐다",
 "items": [
  it("힐리 \"은행은 영국 경제 왕관의 보석 중 하나\"", "블룸버그", "2026-10-15", "https://www.bloomberg.com/news/articles/2026-10-15/banks-are-part-of-jewel-in-uk-economic-crown-healey-says",
     "힐리 재무장관이 은행을 영국 경제의 보석 가운데 하나로 치켜세우면서, 은행세 인상 폭을 두고 업계 관심이 커졌다" + TB),
  it("은행세 질문에 힐리, 업계의 폭넓은 기여 강조", "로이터", "2026-10-16", "https://www.reuters.com/business/finance/asked-bank-tax-uks-healey-stresses-sectors-broader-contribution-2026-10-15/",
     "힐리가 은행세 질문에 업계의 폭넓은 기여를 강조하면서도 예산안에서 결정을 내리겠다고 해 은행 과세 여지를 남겼다"),
  it("힐리 재무장관, 이달 예산안서 은행 세금 인상 계획", "블룸버그", "2026-10-16", "https://www.bloomberg.com/news/articles/2026-10-15/healey-plans-to-raise-uk-taxes-on-banks-at-budget-this-month",
     "힐리가 10월 28일 예산안에서 은행 세금을 올릴 계획이어서, 3%인 은행 추가세율이 8%로 환원될 수 있다"),
 ]
})

# G3-027
items.append({
 "cid": "G3-027", "attachTo": "n-rtr-0230",
 "title": "유럽 유통 사이버공격 여파…佛 슈퍼마켓 식품 손실, 사이버보험 보상 어려워",
 "one": "냉장 관리 소프트웨어 해킹으로 프랑스 슈퍼마켓 약 700곳이 피해를 입은 데 이어 보험사들이 사이버보험은 식품 같은 물리적 손실을 대개 보상하지 않는다고 밝히고 네덜란드 알버트 하인도 물류센터 차질을 겪으면서, 유통업체가 손실을 떠안을 가능성이 커졌다",
 "facts": [
  "무엇이: 보험사들은 프랑스 슈퍼마켓의 사이버보험이 조사·홍보 비용 일부는 보상해도 식품 폐기 같은 물리적 손실은 대개 보상하지 않는다고 밝혔다 [사실]",
  "피해: 앵테르마르셰 CEO는 하루 만에 전국 손실이 수천만 유로에 이른다고 했고, 자사 보험도 이런 사고를 보상하지 않는다고 했다 [사실]",
  "국가 배후 변수: 보험사들은 국가 행위자 소행이면 전쟁 면책 조항 때문에 보상이 더 어려울 수 있다고 했다 [사실]",
  "기존: 냉장 관리 소프트웨어를 노린 공격으로 프랑스 슈퍼마켓 약 700곳이 영향을 받았고, 대형 매장은 최대 20만 유로 손실이 추정됐다 [사실]",
  "네덜란드: 알버트 하인은 사이버 사고 뒤 물류센터가 곧 정상 가동될 것으로 예상했다 [제목]"
 ],
 "basis": "partial",
 "check": "검색 결과 요약으로 확인(Insurance Journal·NBC·알자지라): 사이버보험 미보상, 앵테르마르셰 손실 추정, 전쟁 면책 우려. 알버트 하인 물류센터 건은 확인 못 함",
 "src": [
  {"o": "Insurance Journal", "d": "2026-10-15", "u": "https://www.insurancejournal.com/news/international/2026/10/15/889037.htm"},
  {"o": "NBC News", "d": "2026-10-14", "u": "https://www.nbcnews.com/world/europe/hackers-heat-french-supermarket-fridges-sparking-fires-spoiling-food-rcna603151"}
 ],
 "inds": ["consumer", "fin"], "nodes": [],
 "vc": [
  {"ind": "consumer", "node": "retail", "f": "공급", "dir": "down", "k": "실제", "t": "佛 슈퍼마켓 약 700곳 냉장 시스템 해킹 피해"}
 ],
 "added": "이번 로이터 2건으로 사이버보험이 식품 손실을 대개 보상하지 않는다는 보험사 판단과 네덜란드 알버트 하인의 물류센터 차질이 추가됐다",
 "items": [
  it("알버트 하인, 사이버 사고 뒤 물류센터 곧 정상화 예상", "로이터", "2026-10-14", "https://www.reuters.com/business/albert-heijn-expects-distribution-centres-be-operational-soon-after-cyber-2026-10-14/",
     "네덜란드 알버트 하인이 사이버 사고로 멈춘 물류센터가 곧 정상 가동될 것으로 예상하면서, 매장 공급 차질이 조만간 풀릴 수 있다" + TB),
  it("보험사 \"佛 슈퍼마켓 사이버보험, 식품 손실 보상 어려워\"", "로이터", "2026-10-16", "https://www.reuters.com/legal/litigation/french-supermarkets-cyber-insurance-unlikely-cover-food-losses-insurers-say-2026-10-15/",
     "보험사들이 사이버보험은 식품 폐기 같은 물리적 손실을 대개 보상하지 않는다고 밝히면서, 프랑스 슈퍼마켓이 손실을 떠안게 될 수 있다"),
 ]
})

# G3-045
items.append({
 "cid": "G3-045", "attachTo": "n-bbg-0269",
 "title": "뉴월드, 채권 교환 조기 응모에 새 채권 1억 8,910만 달러 발행 예정",
 "one": "홍콩 공항청 구제안으로 시간을 번 뉴월드개발이 2027~2028년 만기 달러채 약 9억 9,100만 달러를 2032년 만기 담보채로 바꾸는 교환에서 조기 응모를 받아 새 채권 1억 8,910만 달러를 발행할 예정이어서, 단기 부채 만기 부담을 일부 늦추게 됐다",
 "facts": [
  "무엇이: 뉴월드개발은 10월 15일 채권 교환 조기 응모 결과 약 1억 8,910만 달러의 새 채권을 발행할 것으로 예상한다고 밝혔다 [사실]",
  "조건: 대상은 2027·2028년 만기 달러채 3종 약 9억 9,100만 달러로, 액면 1,000달러당 2032년 만기 새 담보채 950달러와 현금 35달러를 주고 조기 응모자에게 17.5달러를 더 준다 [사실]",
  "일정: 조기 응모분 결제는 10월 20일로 예정됐다 [사실]",
  "기존: 홍콩 공항청이 180억 홍콩달러 규모 11 스카이즈 사업을 넘겨받는 구제안으로 정씨 일가는 2029년 말까지 자본구조를 손볼 시간을 벌었고, 이르면 내년 약 110억 달러 부채 만기가 돌아온다 [사실]"
 ],
 "basis": "verified",
 "check": "검색 결과 요약으로 확인(The Standard·BigGo Finance): 새 채권 1억 8,910만 달러, 대상 채권 3종 약 9억 9,100만 달러, 교환 조건, 10월 20일 결제",
 "src": [
  {"o": "The Standard", "d": "2026-10-15", "u": "https://www.thestandard.com.hk/finance/article/345531/New-World-expects-to-issue-US189-million-of-new-notes-after-early-debt-exchange-results"},
  {"o": "BigGo Finance", "d": "2026-10-15", "u": "https://finance.biggo.com/news/5b0735a8-a706-4b7a-a269-6f2a035d998e"}
 ],
 "inds": ["realestate"], "nodes": [],
 "vc": [
  {"ind": "realestate", "node": "china", "f": "가격", "dir": "down", "k": "실제", "t": "액면 1천 달러당 새 채권 950달러·현금 35달러로 교환"}
 ],
 "added": "이번 로이터 1건으로 뉴월드가 2027~2028년 만기 달러채 교환 조기 응모 결과 2032년 만기 새 채권 1억 8,910만 달러를 발행할 예정이라는 점이 추가됐다",
 "items": [
  it("뉴월드, 채권 교환 조기 결과 뒤 새 채권 1억 8,900만 달러 발행 예정", "로이터", "2026-10-15", "https://www.reuters.com/world/asia-pacific/new-world-expects-issue-189-million-new-notes-after-early-debt-exchange-results-2026-10-14/",
     "뉴월드가 채권 교환 조기 응모 결과 2032년 만기 새 채권 1억 8,910만 달러를 발행할 예정이라고 밝혀, 일부 부채 만기가 뒤로 밀리게 됐다"),
 ]
})

# G4-018
items.append({
 "cid": "G4-018", "attachTo": "n-tg-0225",
 "title": "中 완성차 유럽 공략 가속…체리 '아이카' 영국 진출, 중-EU 무역 합의",
 "one": "영국 점유율 7%로 중국 업체 1위인 체리가 오프로드 브랜드 아이카의 전기 SUV를 2027년 초 영국에 내놓고 중국 자동차 단체가 중-EU 무역 합의가 산업 안정을 돕는다고 하면서, BYD·샤오펑에 이어 중국 완성차의 유럽 공세가 넓어지고 있다",
 "facts": [
  "무엇이: 체리는 오프로드 브랜드 아이카(iCAUR)를 2027년 초 영국에 출시하며 첫 모델로 박스형 전기 SUV V27을 내놓는다 [사실]",
  "체리 영국: 체리 계열 브랜드는 올해 9월까지 영국 시장 점유율 7%로 중국 자동차 업체 중 가장 많이 팔렸다 [사실]",
  "중-EU: 중국 자동차 단체는 중-EU 무역 합의가 산업 안정에 도움이 된다고 했고, 이탈리아 장관은 중국 업체가 살 수 있는 자동차 공장이 없다고 했다 [제목]",
  "기존: BYD는 유럽 인력을 2030년 4만 명 넘게 늘리고, 덴자는 이르면 2027년 유럽 자동차금융 법인 설립을 검토한다 [사실]"
 ],
 "basis": "partial",
 "check": "검색 결과 요약으로 확인(Electrifying·Card Dealer Magazine·Global Banking and Finance): 아이카 2027년 초 영국 출시, V27, 체리 영국 점유율 7%. 중-EU 합의 평가와 이탈리아 장관 발언은 제목 기준",
 "src": [
  {"o": "Electrifying", "d": "2026-10-15", "u": "https://www.electrifying.com/blog/article/icaur-v27-uk-launch-2027"},
  {"o": "Card Dealer Magazine", "d": "2026-10-15", "u": "https://cardealermagazine.co.uk/chery-to-launch-another-uk-car-brand-as-icaur-confirms-2027-arrival/328255"},
  {"o": "Global Banking and Finance", "d": "2026-10-15", "u": "https://www.globalbankingandfinance.com/chinese-automaker-chery-launch-new-ev-model-uk-early-2027/"}
 ],
 "inds": ["auto"], "nodes": [],
 "vc": [
  {"ind": "auto", "node": "chinaoem", "f": "공급", "dir": "up", "k": "예상", "t": "체리 아이카, 2027년 초 영국에 전기 SUV 출시"}
 ],
 "added": "이번 로이터 5건·블룸버그 1건으로 체리 아이카의 2027년 초 영국 출시와 중-EU 무역 합의 평가, 이탈리아의 중국 업체 공장 매각 불가 입장이 추가됐다",
 "items": [
  it("中 자동차 단체 \"중-EU 무역 합의, 산업 안정에 도움\"", "로이터", "2026-10-14", "https://www.reuters.com/business/retail-consumer/china-auto-group-says-china-eu-trade-consensus-aids-industry-stability-2026-10-14/",
     "중국 자동차 단체가 중-EU 무역 합의가 산업 안정에 도움이 된다고 하면서, 중국차의 유럽 수출 불확실성이 줄 수 있다" + TB),
  it("伊 장관 \"중국 업체가 살 수 있는 자동차 공장 없다\"", "로이터", "2026-10-14", "https://www.reuters.com/world/china/no-auto-plants-available-italy-chinese-purchase-italian-minister-says-2026-10-14/",
     "이탈리아 장관이 중국 업체가 인수할 수 있는 자동차 공장이 없다고 하면서, 중국차의 이탈리아 현지 생산 길이 좁아졌다" + TB),
  it("센강까지 번진 중국과 EU의 자동차 전쟁", "로이터", "2026-10-15", "https://www.reuters.com/podcasts/viewsroom/china-eu-auto-wars-drive-in-seine-level-2026-10-15/",
     "로이터 팟캐스트가 중국과 유럽 완성차의 경쟁이 한층 격해졌다고 짚으면서, 유럽 업체의 안방 시장 부담이 커지고 있다" + TB),
  it("체리 새 브랜드, 랜드로버 닮은꼴로 영국 상륙", "블룸버그", "2026-10-15", "https://www.bloomberg.com/news/articles/2026-10-15/chery-s-latest-brand-comes-to-the-uk-with-land-rover-lookalike",
     "체리가 랜드로버를 닮은 박스형 SUV를 앞세운 새 브랜드 아이카로 영국에 들어오면서, 영국 SUV 시장 경쟁이 거세질 수 있다"),
  it("中 체리, 2027년 초 영국에 새 전기차 출시", "로이터", "2026-10-15", "https://www.reuters.com/world/china/chinese-automaker-chery-launch-new-ev-model-uk-early-2027-2026-10-15/",
     "체리가 2027년 초 영국에 아이카 브랜드의 5인승 전기 SUV를 내놓으면서, 오모다에 이어 영국 내 브랜드를 늘린다"),
  it("중국 완성차 업체들의 생존 길은 유럽을 지난다", "로이터", "2026-10-15", "https://www.reuters.com/business/autos-transportation/chinese-automakers-road-survival-runs-through-europe-2026-10-15/",
     "내수 경쟁에 몰린 중국 완성차들이 살아남으려면 유럽 진출이 필수라는 분석이 나오면서, 유럽 시장 공세가 이어질 전망이다" + TB),
 ]
})

# G4-035
items.append({
 "cid": "G4-035", "attachTo": "",
 "title": "우크라, 러 공군기지 미사일 타격 Su-34M 6대 피해…도네츠크 영토 탈환 주장",
 "one": "우크라이나가 넵튠 미사일로 러시아 보로네시주 보리소글렙스크 비행장을 타격해 Su-34M 전폭기 6대에 피해를 줬다고 밝히고 도네츠크에서 영토를 더 되찾았다고 하면서, 러시아의 대규모 드론 공세와 맞물려 양측 공방이 거세지고 있다",
 "facts": [
  "무엇이: 우크라이나 총참모부는 10월 14~15일 밤 보로네시주 보리소글렙스크 비행장을 공격해 Su-34M 6대에 정도가 다른 피해를 확인했다고 밝혔다 [사실]",
  "무기·검증: 해군은 넵튠 해안 미사일 체계를 썼다고 했고, 피해는 독립적으로 확인되지 않았다 [사실]",
  "반격: 우크라이나는 도네츠크주 반격에서 영토를 더 해방했다고 밝혔다 [제목]",
  "피해: 우크라이나 중부 지역이 대규모 드론 공격을 받아 3명이 숨졌다 [제목]"
 ],
 "basis": "verified",
 "check": "검색 결과 요약으로 확인(TVP World·Al Arabiya·Eurasia Review): Su-34M 6대 피해 주장, 넵튠 사용, 독립 확인 안 됨. 도네츠크 반격과 중부 드론 공격은 제목 기준",
 "src": [
  {"o": "TVP World", "d": "2026-10-15", "u": "https://tvpworld.com/95941085/ukraine-says-it-damaged-six-russian-military-jets-in-missile-strike-on-airfield"},
  {"o": "Eurasia Review", "d": "2026-10-15", "u": "https://www.eurasiareview.com/15102026-ukraine-takes-out-six-russian-fighter-jets-in-one-strike/"}
 ],
 "inds": ["aero", "macro"], "nodes": ["macro/geo"],
 "vc": [
  {"ind": "aero", "node": "platforms", "f": "공급", "dir": "down", "k": "실제", "t": "러 Su-34M 6대 피해 주장, 독립 확인 안 됨"}
 ],
 "added": "이번 로이터 1건으로 우크라이나가 넵튠 미사일로 러시아 비행장을 타격해 Su-34M 6대에 피해를 줬다는 주장이 추가됐다",
 "items": [
  it("우크라이나 중부, 대규모 드론 공격에 3명 사망", "로이터", "2026-10-15", "https://www.reuters.com/business/aerospace-defense/central-ukrainian-region-hit-by-vast-drone-attack-killing-three-2026-10-15/",
     "러시아의 대규모 드론 공격이 우크라이나 중부 지역을 덮쳐 3명이 숨지면서, 민간 피해가 다시 커졌다" + TB),
  it("우크라이나 \"도네츠크 반격으로 영토 추가 해방\"", "로이터", "2026-10-15", "https://www.reuters.com/business/aerospace-defense/ukraine-says-it-frees-more-territory-donetsk-region-counteroffensive-2026-10-14/",
     "우크라이나가 도네츠크주 반격에서 영토를 더 되찾았다고 밝히면서, 동부 전선의 공방이 거세지고 있다" + TB),
  it("우크라 \"비행장 미사일 타격으로 러 군용기 6대 손상\"", "로이터", "2026-10-15", "https://www.reuters.com/business/aerospace-defense/ukraine-says-it-damaged-six-russian-military-jets-missile-strike-airfield-2026-10-15/",
     "우크라이나가 넵튠 미사일로 보리소글렙스크 비행장을 타격해 Su-34M 6대에 피해를 줬다고 밝혀, 러시아 공군 전력에 타격이 될 수 있다"),
 ]
})

# G4-049
items.append({
 "cid": "G4-049", "attachTo": "",
 "title": "테슬라, 9년 지연 차세대 로드스터 공개…'플라잉카' 시연으로 부진 만회 노려",
 "one": "테슬라가 9년 가까이 미뤄 온 차세대 로드스터를 10월 15일 텍사스 스페이스X 시험장에서 공개하며 플라잉카 시연을 준비하면서, 부진한 자동차 사업에 관심을 되살리려 하지만 양산은 2027~2028년으로 잡혀 있다",
 "facts": [
  "무엇이: 테슬라는 10월 15일 오후 7시 55분(미 중부 시간) 텍사스 맥그레거의 스페이스X 시험장에서 차세대 로드스터 공개 행사를 생중계한다 [사실]",
  "지연: 행사는 날씨를 이유로 10월 1일에서 미뤄졌고, 로드스터는 거의 9년 지연됐다 [사실]",
  "시연: 테슬라는 부진한 자동차 사업을 띄우려 플라잉카 시연을 준비한다 [제목]",
  "축소: 일렉트렉은 시연이 비행에서 짧은 공중 부양으로 줄었고 양산은 2027년 또는 2028년으로 안내돼 있다고 전했다 [사실]"
 ],
 "basis": "verified",
 "check": "검색 결과 요약으로 확인(Electrek·CNBC·Tesla Oracle): 10월 15일 공개 일정, 10월 1일에서 연기, 공중 부양 축소 보도, 양산 2027~2028년. 행사 결과는 검색 시점에 나오지 않음",
 "src": [
  {"o": "Electrek", "d": "2026-10-13", "u": "https://electrek.co/2026/10/13/tesla-roadster-event-thursday-nine-years-delays/"},
  {"o": "CNBC", "d": "2026-10-15", "u": "https://www.cnbc.com/2026/10/15/tesla-roadster-reveal-what-to-know-about-the-delayed-ev.html"}
 ],
 "inds": ["auto"], "nodes": [],
 "vc": [
  {"ind": "auto", "node": "oem", "f": "공급", "dir": "up", "k": "예상", "t": "테슬라 차세대 로드스터 공개, 양산은 2027~2028년"},
  {"ind": "auto", "node": "sales", "f": "수요", "dir": "down", "k": "실제", "t": "테슬라 자동차 사업 부진에 시연으로 관심 끌기"}
 ],
 "added": "이번 블룸버그 1건으로 테슬라가 부진한 자동차 사업을 띄우려 로드스터 공개에 맞춰 플라잉카 시연을 준비한다는 점이 추가됐다 (제목 기준)",
 "items": [
  it("테슬라, 수년 지연 끝 차세대 로드스터 공개 예정", "로이터", "2026-10-15", "https://www.reuters.com/business/autos-transportation/tesla-set-unveil-next-generation-roadster-sports-ev-after-years-delay-2026-10-15/",
     "테슬라가 수년간 미뤄 온 차세대 로드스터 스포츠 전기차를 10월 15일 공개하기로 하면서, 양산 일정과 가격에 관심이 쏠렸다"),
  it("테슬라, 부진한 자동차 사업 띄우려 플라잉카 시연 준비", "블룸버그", "2026-10-15", "https://www.bloomberg.com/news/articles/2026-10-15/tesla-readies-flying-car-demo-to-pump-up-sluggish-auto-business",
     "테슬라가 부진한 자동차 사업에 활력을 주려고 플라잉카 시연을 준비하면서, 판매 둔화를 화제성으로 만회하려 한다" + TB),
 ]
})

# G4-062
items.append({
 "cid": "G4-062", "attachTo": "",
 "title": "佛·獨, 차 배출가스 규제 완화·영국 '메이드 인 EU' 편입 합의 근접",
 "one": "프랑스와 독일이 2035년 차 CO2 감축 목표를 90%로 낮추고 조건부로 영국을 '메이드 인 유럽' 자동차 정의에 넣는 안에 합의를 앞두면서, EU 승인을 거치면 유럽 완성차의 2035년 배출 규제 부담이 줄 수 있다",
 "facts": [
  "무엇이: 프랑스와 독일이 자동차 배출가스와 영국의 '메이드 인 EU' 지위에 관한 합의에 근접했다 [사실]",
  "배출: 안은 2035년 차 CO2 감축 목표를 추가 상쇄 없이 90%로 정하는 것이다 [사실]",
  "영국: 영국 편입은 완전한 상호주의와 제3국 투자 조건·EU 무역보호 조치에 대한 동적 정렬이 조건이어서, 영국이 중국산 하이브리드·전기차 수입 제한을 따라야 할 수 있다 [사실]",
  "절차: 시행되려면 다른 EU 회원국과 유럽의회를 설득해야 한다 [사실]"
 ],
 "basis": "verified",
 "check": "검색 결과 요약으로 확인(France24·KFGO·Global Banking and Finance): 2035년 목표 90%, 영국 편입 조건, EU 승인 필요. 로이터는 '근접', AFP는 독일 최종 승인 전 합의로 표현",
 "src": [
  {"o": "France24(AFP)", "d": "2026-10-15", "u": "https://www.france24.com/en/live-news/20261015-france-germany-reach-deal-on-future-of-car-industry-1"},
  {"o": "Global Banking and Finance", "d": "2026-10-15", "u": "https://www.globalbankingandfinance.com/france-germany-near-deal-car-emissions-britain-made-eu/"}
 ],
 "inds": ["auto"], "nodes": [],
 "vc": [
  {"ind": "auto", "node": "policy", "f": "공급", "dir": "up", "k": "예상", "t": "佛·獨, 2035년 차 CO2 감축 목표 90%로 완화 추진"}
 ],
 "items": [
  it("佛·獨, 차 배출가스·영국 '메이드 인 EU' 지위 합의 근접", "로이터", "2026-10-16", "https://www.reuters.com/business/environment/france-germany-near-deal-car-emissions-britain-made-eu-status-2026-10-15/"),
 ]
})

doc = {"agent": "W4", "searches_used": 16, "fetches_used": 2, "items": items, "skipped": []}
json.dump(doc, open(OUT, 'w'), ensure_ascii=False, indent=1)

# checks
strip = lambda s: re.sub(r' \((제목 기준|채널 전언)\)$', '', s)
for x in items:
    single = len(x['items']) == 1 and not x['attachTo']
    lo, hi = (80, 130) if single else (90, 160)
    L = len(strip(x['one']))
    pr = []
    if not (lo <= L <= hi): pr.append(f"one {L}")
    if not (20 <= len(x['title']) <= 50): pr.append(f"title {len(x['title'])}")
    if 'added' in x:
        a = len(strip(x['added']))
        if not (60 <= a <= 140): pr.append(f"added {a}")
    for i in x['items']:
        if not (25 <= len(i['t']) <= 60): pr.append(f"t {len(i['t'])} {i['t']}")
        if 's' in i:
            s = len(strip(i['s']))
            if not (45 <= s <= 110): pr.append(f"s {s} {i['s'][:20]}")
    for v in x['vc']:
        if not (12 <= len(v['t']) <= 45): pr.append(f"vc {len(v['t'])} {v['t']}")
    for f in x.get('fed', []):
        if not (20 <= len(f['t']) <= 70): pr.append(f"fed {len(f['t'])}")
    if not (2 <= len(x['facts']) <= 5): pr.append('facts n')
    for f in x['facts']:
        if '|' in f or '**' in f: pr.append('bad char')
    s_all = json.dumps(x, ensure_ascii=False)
    if '{{' in s_all or '**' in s_all: pr.append('emph')
    print(x['cid'], L, pr)
