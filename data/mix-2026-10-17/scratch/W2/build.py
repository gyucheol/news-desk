import json, re, sys

def it(t, o, d, u, s=None):
    x = {"t": t, "o": o, "d": d, "u": u}
    if s is not None:
        x["s"] = s
    return x

def vc(ind, node, f, dr, k, t):
    return {"ind": ind, "node": node, "f": f, "dir": dr, "k": k, "t": t}

B = "블룸버그"; R = "로이터"
items = []

# G1-002
items.append({
 "cid": "G1-002", "attachTo": "n-rtr-0025",
 "title": "AI·반도체주 투매 속 젠슨 황 '모두 지나갈 것'…반도체지수 8일 연속 하락",
 "one": "헤지펀드의 AI주 청산 속에 필라델피아 반도체지수가 2008년 이후 최장인 8거래일 연속 떨어지고 메모리 ETF에서 8주째 자금이 빠지면서, 젠슨 황의 '결국 지나갈 것'이라는 반박에도 AI·반도체주 수급 부담이 이어지고 있다",
 "facts": [
  "무엇이: 필라델피아 반도체지수가 16일까지 8거래일 연속 떨어져 2008년 이후 최장 하락을 기록했고 이번 주 11.4% 내렸으며, 나스닥은 주간 약 4.5% 하락해 6월 이후 최악이었다 [사실]",
  "젠슨 황: 엔비디아 CEO 젠슨 황은 16일 베를린 블룸버그 행사에서 지금의 혼란은 결국 지나갈 것이고 AI는 초기 단계라 펀더멘털은 바뀌지 않는다고 말했다 [사실]",
  "자금 유출: 메모리 ETF 'DRAM'은 이번 주 19% 떨어져 4월 상장 이후 최대 주간 낙폭을 냈고, 8주 연속 자금이 빠졌다 [채널]",
  "신용·매출: 채널은 앤트로픽 ARR 순증 둔화와 오픈AI 9월 런레이트의 기대 하회, 코어위브 가산금리 1,023bp를 들어 차입 의존 AI 기업의 상환 능력이 재평가됐다고 봤다 [채널]",
  "금리: 워시 의장 발언 뒤 10월 FOMC 금리 인상 확률은 약 27%에서 15% 아래로 내려갔다 [사실]"
 ],
 "basis": "verified",
 "check": "젠슨 황 발언·반도체지수 8일 연속 하락·주간 낙폭·워시 발언 뒤 인상 확률은 검색 결과 요약으로 확인, DRAM ETF 수치와 AI 매출·신용 수치는 채널 전언. 엔비디아 신규 주문 글(t.me/HANAchina/70558)은 AI 칩 대량 구매 내용이라 사용자 기준으로 뺐다",
 "src": [
  {"o": "CNN", "d": "2026-10-16", "u": "https://www.cnn.com/2026/10/16/investing/tech-stocks-ai-coreweave"},
  {"o": "CBS News", "d": "2026-10-16", "u": "https://www.cbsnews.com/news/tech-stocks-slide-ai-debt-concerns/"},
  {"o": "Asianet Newsable", "d": "2026-10-16", "u": "https://newsable.asianetnews.com/markets/nasdaq-100-records-worst-week-in-18-months-as-investors-steer-clear-of-chipmakers-aapl-mstr-uber-soxx-in-focus-articleshow-xcdkcz2"}
 ],
 "inds": ["macro"], "nodes": ["macro/semis", "macro/cb"],
 "vc": [
  vc("macro", "semis", "가격", "down", "실제", "필라델피아 반도체지수 8거래일 연속 하락"),
  vc("macro", "liquidity", "공급", "down", "실제", "메모리 ETF DRAM 8주 연속 자금 유출"),
  vc("macro", "cb", "-", "flat", "예상", "워시 발언 뒤 10월 금리 인상 확률 하락")
 ],
 "fed": [
  {"k": "", "who": "연준", "role": "워시 발언 뒤 시장 반응", "kind": "관련 뉴스", "stance": "중립",
   "t": "워시 의장 발언 뒤 10월 금리 인상 확률이 15% 아래로 내려갔다", "d": "2026-10-16",
   "u": "https://www.bloomberg.com/news/articles/2026-10-16/s-p-500-steady-as-warsh-boosts-expectations-of-rate-hold"}
 ],
 "added": "이번 블룸버그 3건과 텔레그램 7건으로 반도체지수 8거래일 연속 하락과 젠슨 황의 '결국 지나갈 것' 발언, 메모리 ETF 'DRAM'의 주간 19% 급락과 8주 연속 자금 유출이 추가됐다",
 "items": [
  it("엔비디아 황과 브로드컴 탄, AI 붐을 조금씩 다른 자리에서 본다", B, "2026-10-16", "https://www.bloomberg.com/news/newsletters/2026-10-16/nvidia-s-huang-and-broadcom-s-tan-see-the-ai-boom-from-slightly-different-places",
     "엔비디아 젠슨 황과 브로드컴 혹 탄 CEO가 AI 붐을 서로 조금 다른 자리에서 바라본다는 분석이 나오면서 두 칩 업체 수장의 시각차가 비교됐다 (제목 기준)"),
  it("헤지펀드 5거래일 연속 AI주 순매도…숏 스퀴즈 조건 무르익나", "텔레그램 하나증권 중국전략", "2026-10-16", "https://t.me/HANAchina/70530",
     "헤지펀드들이 5거래일 연속 AI주를 순매도해 2025년 이후 쌓은 순매수를 모두 청산하면서, 공매도가 몰린 반도체·한국 증시에 반등 조건이 생기고 있다는 분석이 나왔다"),
  it("AI 우려에 반도체주 급락…S&P500 6월 이후 최악의 한 주", B, "2026-10-16", "https://www.bloomberg.com/news/articles/2026-10-16/s-p-500-steady-as-warsh-boosts-expectations-of-rate-hold",
     "AI 우려로 반도체주가 무너지면서 S&P500이 6월 이후 최악의 한 주를 보냈고, 워시 의장 발언 뒤 10월 금리 인상 확률은 15% 아래로 내려갔다"),
  it("엔비디아 CEO, AI 시장 혼란에 '이 모든 것은 지나갈 것'", B, "2026-10-17", "https://www.bloomberg.com/news/articles/2026-10-16/nvidia-ceo-on-ai-market-turmoil-all-of-this-is-going-to-pass",
     "젠슨 황 엔비디아 CEO가 AI 시장 혼란은 결국 지나갈 것이라고 말하면서, 기술 발전은 계속되고 산업은 이제 시작 단계라며 투매에 반박했다"),
  it("젠슨 황 'AI 변동성 결국 진정…하드웨어 투자가 수익 낼 것'", "텔레그램 미국 주식 인사이더", "2026-10-17", "https://t.me/insidertracking/66500",
     "젠슨 황이 베를린 행사에서 차입 비용 상승에 따른 AI 지출 우려에도 대규모 하드웨어 투자가 결국 수익을 내 시장 불안을 누그러뜨릴 것이라고 전망했다"),
  it("AI 인프라주 급락은 지수 붕괴 아닌 업종 로테이션…AI 매출 둔화가 계기", "텔레그램 나쁜양파", "2026-10-17", "https://t.me/Badonions/7876",
     "앤트로픽 ARR 순증 둔화와 오픈AI 런레이트 기대 하회로 코어위브 등 차입 의존 기업의 상환 능력이 재평가되면서, 반도체가 14.7% 빠지고 자금이 필수소비재·에너지로 옮겨 갔다"),
  it("필라델피아 반도체지수 8일 연속 하락, 2008년 이후 최장", "텔레그램 하나증권 중국전략", "2026-10-17", "https://t.me/HANAchina/70539",
     "필라델피아 반도체지수가 2008년 이후 최장인 8거래일 연속 하락하고 코어위브가 한 주에 25% 넘게 폭락하면서 AI 인프라 투자 열풍이 신뢰 위기를 맞았다"),
  it("바클레이즈 'AI 트레이딩 황금기 지나…반도체 급락은 포지션 청산 탓'", "텔레그램 하나증권 중국전략", "2026-10-17", "https://t.me/HANAchina/70543",
     "바클레이즈가 반도체주 폭락은 수요 붕괴가 아닌 포지션 청산 때문이지만 밸류에이션·자금조달·매출 지연이 AI주를 누른다고 보면서, 현금흐름과 매출 가시성을 따지라고 권했다"),
  it("메모리 ETF 'DRAM' 이번 주 19% 급락…8주 연속 자금 유출", "텔레그램 TNBfolio", "2026-10-17", "https://t.me/TNBfolio/71586",
     "삼성전자·SK하이닉스를 담은 메모리 ETF 'DRAM'이 상장 이후 최대인 주간 19% 급락하고 8주 연속 자금이 빠지면서, 메모리 랠리를 떠받친 자금이 이탈하고 있다"),
  it("씨티 '2027년 글로벌 이익 증가의 약 70%를 기술주가 기여할 전망'", "텔레그램 하나증권 중국전략", "2026-10-17", "https://t.me/HANAchina/70553",
     "씨티가 2027년 글로벌 이익 증가의 약 70%를 기술주가 차지하고 전체 EPS 증가율은 35%에서 16%로 둔화한다고 보면서, AI 열기가 식으면 증시가 흔들릴 수 있다고 짚었다")
 ]})

# G1-011
items.append({
 "cid": "G1-011", "attachTo": "",
 "title": "美 2026회계연도 재정적자 1.99조 달러로 5년 만에 최대…총이자 지출 사상 최고",
 "one": "미국 2026회계연도 재정적자가 12% 늘어난 1조 9,900억 달러로 5년 만에 가장 커지고 총이자 지출도 1조 3,600억 달러로 사상 최고를 기록하면서, 40조 달러를 넘은 국가부채의 조달 비용 부담이 재정을 더 압박할 전망이다",
 "facts": [
  "무엇이: 미국 2026회계연도 재정적자는 전년보다 2,170억 달러 늘어난 1조 9,900억 달러로 2021년 이후 가장 컸다 [사실]",
  "이자: 총이자 지출은 12% 늘어난 1조 3,600억 달러로 사상 최고였고, 이자는 사회보장에 이어 두 번째로 큰 지출 항목이 됐다 [사실]",
  "세입·세출: 지출은 6% 늘어난 7조 4,000억 달러, 수입은 3% 늘어난 5조 4,000억 달러였고 감세로 법인세 수입은 약 700억 달러 줄었다 [채널]",
  "부채: 미국 국가부채는 8월 40조 달러를 넘었고, 대법원의 관세 위헌 판결에 따른 환급도 적자 확대 요인으로 꼽혔다 [사실]",
  "전망: 채널은 추세가 이어지면 2028년 말 이전 이자 지출이 사회보장 지출을 넘어 최대 단일 항목이 될 수 있다고 전했다 [채널]"
 ],
 "basis": "verified",
 "check": "적자 규모·증가액·총이자 1조 3,600억 달러·부채 40조 달러·관세 환급은 검색 결과 요약으로 확인. 세입·세출 세부와 2028년 전망은 채널 전언. 10월 9일 n-tg-0140은 CBO 추정치(1조 9,930억 달러)였고 이번은 재무부 확정치와 세부 항목이다",
 "src": [
  {"o": "CNBC", "d": "2026-10-16", "u": "https://www.cnbc.com/2026/10/16/us-budget-deficit-2026.html"},
  {"o": "Fox Business", "d": "2026-10-16", "u": "https://www.foxbusiness.com/politics/federal-budget-deficit-hits-2t-national-debt-costs-surge"},
  {"o": "NPR", "d": "2026-08-19", "u": "https://www.npr.org/2026/08/19/nx-s1-5937552/the-u-s-debt-tops-a-record-shattering-40-trillion-yes-with-a-t"}
 ],
 "inds": ["macro"], "nodes": ["macro/fiscal"],
 "vc": [
  vc("macro", "fiscal", "수요", "up", "실제", "지출 6% 늘며 적자 1조 9,900억 달러로 확대"),
  vc("macro", "rates", "가격", "up", "실제", "총이자 지출 1조 3,600억 달러로 사상 최고")
 ],
 "added": "이번 텔레그램 3건으로 총이자 지출 1조 3,600억 달러와 2028년 이자의 사회보장 추월 가능성, 부채 40조 달러 속 비트코인과 실질금리 상관 확대 분석이 추가됐다",
 "items": [
  it("미국, 지출 증가로 2026회계연도 재정적자 1조 9,900억 달러", B, "2026-10-17", "https://www.bloomberg.com/news/articles/2026-10-16/us-posts-1-99-trillion-budget-gap-for-2026-as-spending-climbs",
     "미국 정부가 지출 증가로 2026회계연도에 1조 9,900억 달러 적자를 내면서, 사회보장·메디케어·이자 지출이 세수 증가를 앞질렀다"),
  it("미 2026회계연도 재정적자 1조 9,900억 달러로 늘어 5년 만에 최대", R, "2026-10-17", "https://www.reuters.com/world/us/us-fiscal-2026-budget-deficit-rises-199-trillion-largest-5-years-2026-10-16/",
     "미국 재정적자가 2,170억 달러 늘어난 1조 9,900억 달러로 5년 만에 가장 커지면서, 관세 환급과 이자 비용 증가가 적자를 키운 것으로 나타났다"),
  it("美 재정적자 1조 9,920억 달러…순이자 1조 달러 돌파, 부채 40조", "텔레그램 TNBfolio", "2026-10-17", "https://t.me/TNBfolio/71585",
     "미국 적자가 전년 1조 7,750억 달러에서 약 12% 늘고 순이자 비용이 1조 달러를 넘으면서, 25년 연속 적자 속 감세로 법인세 수입은 약 700억 달러 줄었다"),
  it("美 총이자 지출 1조 3,600억 달러 사상 최고…2028년 사회보장 추월 가능성", "텔레그램 하나증권 중국전략", "2026-10-17", "https://t.me/HANAchina/70541",
     "미국 총이자 지출이 1조 3,600억 달러로 사상 최고를 경신하면서, 추세가 이어지면 2028년 말 이전 이자가 사회보장을 넘어 최대 단일 지출 항목이 될 전망이다"),
  it("美 부채 40조 달러 돌파 속 피델리티 '비트코인·실질금리 상관 사상 최고'", "텔레그램 미국 주식 인사이더", "2026-10-17", "https://t.me/insidertracking/66514",
     "미국 부채가 40조 달러를 넘고 10년물 금리가 오르는 가운데 피델리티가 비트코인과 실질금리의 상관계수가 0.6을 넘었다며, 비트코인의 헤지 매력이 커질 수 있다고 봤다")
 ]})

# G1-017
items.append({
 "cid": "G1-017", "attachTo": "",
 "title": "美 주식형 펀드에 한 주 391억 달러 유입…BofA는 '몇 주간 위험 회피'",
 "one": "미국 주식형 펀드에 10월 14일까지 한 주간 391억 달러가 들어오고 미 국채 펀드도 16주 연속 자금이 유입됐지만, BofA 하트넷 팀이 실질금리 3%와 AI주 약세를 들어 앞으로 3~4주는 위험 회피를 권하면서 주식 매수세가 꺾일 수 있다는 경계가 커졌다",
 "facts": [
  "무엇이: BofA는 10월 14일까지 한 주 미국 주식형 펀드에 391억 달러가 들어왔고, 연초 이후 유입은 사상 최대인 6,360억 달러라고 밝혔다 [사실]",
  "국채: 미 국채 펀드에는 36억 달러가 들어와 16주 연속 유입으로 2024년 8월 이후 최장 기록을 세웠다 [사실]",
  "글로벌: 글로벌 주식형 펀드에는 약 645억 달러가 들어와 올해 사상 최대인 1조 3,000억 달러 유입 속도를 보였다 [사실]",
  "경계: 하트넷 팀은 실질금리 3%, 지정학 위험, 중간선거 불확실성, AI 관련주 약세를 들어 앞으로 3~4주 위험 회피를 권했고, 연준이 10월 28일 인상해야 한다고 봤다 [사실]"
 ],
 "basis": "verified",
 "check": "BofA 주간 흐름 수치는 검색 결과 요약으로 확인. 채널은 국채 유입이 4년 만의 최장이라 했지만 검색 결과는 2024년 8월 이후 최장이라 검색 쪽을 따랐다. 로이터 국채 금리 진정 기사(LSEG 집계로 보임)는 제목만 근거",
 "src": [
  {"o": "Investing.com", "d": "2026-10-16", "u": "https://ca.investing.com/news/stock-market-news/stay-riskoff-as-higher-real-yields-and-ai-volatility-threaten-stocks-hartnett-4884777"},
  {"o": "BigGo Finance", "d": "2026-10-16", "u": "https://finance.biggo.com/news/89ffe182-6500-463e-b6e0-a38e5903ad59"}
 ],
 "inds": ["fin", "macro"], "nodes": ["macro/liquidity"],
 "vc": [
  vc("fin", "assetmgmt", "수요", "up", "실제", "미 주식형 펀드 한 주 391억 달러 유입"),
  vc("macro", "rates", "수요", "up", "실제", "미 국채 펀드 16주 연속 자금 유입")
 ],
 "added": "이번 로이터 1건으로 국채 금리가 진정되자 미국 주식형 펀드에 자금이 다시 들어오고 있다는 집계가 BofA 주간 흐름 자료에 더해 추가됐다 (제목 기준)",
 "items": [
  it("글로벌 시장 자금 흐름, BofA 주간 집계 긴급 보도", R, "2026-10-16", "https://www.reuters.com/business/global-markets-flows-bofa-urgent-2026-10-16/",
     "BofA가 주간 자금 흐름을 집계하면서 미국 주식형 펀드 391억 달러 유입과 미 국채 펀드 16주 연속 유입이 확인됐다"),
  it("그래픽으로 보는 글로벌 시장 자금 흐름(10월 16일)", R, "2026-10-16", "https://www.reuters.com/world/china/global-markets-flows-graphic-2026-10-16/",
     "로이터가 10월 16일 글로벌 시장 자금 흐름을 그래픽으로 정리하면서 주간 펀드 자금 이동을 한눈에 보여 줬다 (제목 기준)"),
  it("BofA 하트넷 '향후 몇 주 위험 회피'…미 국채 유입 최장 기록", "텔레그램 하나증권 중국전략", "2026-10-16", "https://t.me/HANAchina/70534",
     "BofA 하트넷이 미국 주식형 펀드 390억 달러 유입에도 실질금리 상승과 AI·은행주 흐름, 중간선거 변동성을 들어 몇 주간 위험 회피를 권하면서 위험자산 경계를 이어 갔다"),
  it("국채 금리 진정에 미 주식형 펀드로 다시 자금 유입", R, "2026-10-16", "https://www.reuters.com/business/us-equity-funds-draw-renewed-inflows-treasury-yields-ease-2026-10-16/",
     "미 국채 금리가 진정되면서 미국 주식형 펀드로 자금이 다시 들어와 주식 수급이 나아지는 흐름이 나타났다 (제목 기준)")
 ]})

# G1-023
items.append({
 "cid": "G1-023", "attachTo": "n-rtr-0024",
 "title": "브라질 8월 경제활동 0.3% 증가…보우소나루 랠리 뒤 커지는 부채 문제",
 "one": "플라비우 보우소나루의 결선 선두로 외국인 자금이 브라질 주식에 몰리는 사이 8월 경제활동지수가 예상대로 0.3% 늘었지만, 시장 열광이 급증하는 국가부채 문제를 가린다는 지적이 나오면서 결선 뒤 재정 계획이 자산 가격의 핵심 변수가 되고 있다",
 "facts": [
  "무엇이: 브라질 중앙은행 경제활동지수(IBC-Br)는 8월 전월보다 0.3%(반올림 전 0.34%) 늘어 로이터 예상과 같았고, 산업 0.9%·서비스 0.2% 증가, 농업 1.8% 감소였다 [사실]",
  "금리: 셀릭 금리는 9월 0.25%포인트 인하로 13.75%이며 다음 결정은 11월 초다 [사실]",
  "부채: 보우소나루 결선 기대에 따른 시장 열광이 급증하는 브라질 부채 문제를 가리고 있다는 분석이 나왔다 [제목]",
  "개혁: 브라질 장관은 세제·노동 개혁의 충격을 덜기 위해 신용 한도를 제공할 수 있다고 말했다 [제목]",
  "기존: 이코노미스트들은 연말 셀릭 전망을 13.25%로 낮췄고, 폴리마켓의 보우소나루 결선 승리 확률은 13일 86.4%였다 [사실]"
 ],
 "basis": "partial",
 "check": "IBC-Br 수치·셀릭 금리는 검색 결과 요약으로 확인. 부채 문제 분석과 신용 한도 발언은 확인 못 해 제목만 근거",
 "src": [
  {"o": "Investing.com", "d": "2026-10-16", "u": "https://au.investing.com/news/world-news/brazil-economic-activity-rises-034-in-august-amid-election-4695464"},
  {"o": "Rio Times", "d": "2026-10-16", "u": "https://www.riotimesonline.com/brazil-ibc-br-economic-activity-august-2026/"}
 ],
 "inds": ["macro"], "nodes": ["macro/growth", "macro/fiscal"],
 "vc": [
  vc("macro", "growth", "수요", "up", "실제", "브라질 8월 경제활동 0.3% 증가"),
  vc("macro", "fiscal", "공급", "up", "예상", "보우소나루 랠리 뒤 부채 급증 문제 지적")
 ],
 "added": "이번 로이터·블룸버그 4건으로 8월 경제활동 0.3% 증가와 시장 열광 뒤 급증하는 부채 문제 지적, 개혁 충격 완화용 신용 한도 검토가 추가됐다",
 "items": [
  it("브라질 8월 경제활동 0.3% 증가, 예상 부합", R, "2026-10-16", "https://www.reuters.com/world/americas/brazil-economic-activity-up-03-august-matching-forecasts-2026-10-16/",
     "브라질 경제활동지수가 8월 0.3% 늘어 예상에 부합하면서, 산업 0.9% 증가가 농업 1.8% 감소를 메워 성장세를 받쳤다"),
  it("시장 열광이 브라질의 급증하는 부채 문제를 가린다", B, "2026-10-16", "https://www.bloomberg.com/news/articles/2026-10-16/market-euphoria-distracts-from-brazil-s-mounting-debt-problem",
     "브라질 자산 시장의 열광이 커지면서 급증하는 국가부채 문제가 투자자들의 관심 밖으로 밀려나고 있다는 지적이 나왔다 (제목 기준)"),
  it("브라질, 플라비우 보우소나루 열광이 부채 위기를 가린다(스페인어판)", B, "2026-10-16", "https://www.bloomberg.com/news/articles/2026-10-16/brasil-euforia-por-flavio-bolsonaro-oculta-crisis-de-deuda-mvb38nf8",
     "플라비우 보우소나루를 향한 시장 열광이 브라질의 부채 위기를 가리고 있다는 분석이 스페인어판으로 실리면서, 결선 랠리 뒤 재정 위험이 부각됐다 (제목 기준)"),
  it("브라질, 세제·노동 개혁 충격 완화 위해 신용 한도 제공 검토…장관", R, "2026-10-17", "https://www.reuters.com/world/americas/brazil-may-offer-credit-lines-ease-impact-tax-labor-reforms-minister-says-2026-10-16/",
     "브라질 장관이 세제·노동 개혁의 충격을 덜기 위해 신용 한도를 제공할 수 있다고 밝히면서, 개혁 비용을 정부 금융 지원으로 완충하는 방안이 거론됐다 (제목 기준)")
 ]})

# G1-029
items.append({
 "cid": "G1-029", "attachTo": "n-rtr-0230",
 "title": "유럽 유통 사이버공격 확산…아홀드 온라인 5일째 중단, H&M도 장애에 주가 타격",
 "one": "프랑스 슈퍼마켓 약 700곳을 덮친 냉장 관리 소프트웨어 해킹에 이어 아홀드 델레이즈의 웹사이트·앱이 11일부터 닷새째 멈추고 H&M 장애가 주가를 끌어내리면서, 보험 보상이 어려운 유통업체의 손실과 식품 공급 불안이 커지고 있다",
 "facts": [
  "무엇이: 아홀드 델레이즈는 11일 시작된 사이버보안 사고로 알버트 하인·델레이즈·스톱앤숍·푸드라이언 등 유럽·미국 브랜드의 웹사이트와 앱을 닷새째 내렸고, 매장·약국·주유소는 문을 열었다 [사실]",
  "대응: 아홀드는 고객·직원 정보 유출 증거는 없다며 일부 시스템의 통제된 재가동을 시작했고, 미국 브랜드는 처리 못 한 온라인 주문을 환불하기로 했다 [사실]",
  "H&M: H&M은 시스템 장애로 주가가 떨어졌고, 잇단 사이버공격이 트레이더들을 불안하게 했다 [제목]",
  "식품 안보: 슈퍼마켓 사이버공격이 식품 안보 위협을 더한다는 분석이 나왔다 [제목]",
  "기존: 프랑스 슈퍼마켓 약 700곳이 냉장 관리 소프트웨어 공격 피해를 입었고, 보험사들은 식품 폐기 같은 물리적 손실은 대개 보상하지 않는다고 했다 [사실]"
 ],
 "basis": "partial",
 "check": "아홀드 온라인 중단·환불·재가동은 검색 결과 요약으로 확인. H&M 장애와 주가 영향, 식품 안보 분석은 확인 못 해 제목만 근거",
 "src": [
  {"o": "Grocery Dive", "d": "2026-10-16", "u": "https://www.grocerydive.com/news/ahold-delhaize-usa-sites-still-down/832900/"},
  {"o": "Supermarket News", "d": "2026-10-16", "u": "https://www.supermarketnews.com/grocery-technology/ahold-delhaize-s-web-shutdown-enters-fifth-day"},
  {"o": "BleepingComputer", "d": "2026-10-13", "u": "https://www.bleepingcomputer.com/news/security/retail-giant-ahold-delhaize-takes-systems-offline-after-cyberattack/"}
 ],
 "inds": ["consumer"], "nodes": [],
 "vc": [
  vc("consumer", "retail", "공급", "down", "실제", "아홀드 웹사이트·앱 닷새째 중단"),
  vc("consumer", "apparel", "가격", "down", "실제", "H&M 시스템 장애에 주가 하락")
 ],
 "added": "이번 블룸버그 2건과 로이터 1건으로 아홀드 웹사이트·앱 닷새째 중단과 H&M 장애에 따른 주가 하락, 슈퍼마켓 공격이 식품 안보를 위협한다는 분석이 추가됐다",
 "items": [
  it("H&M 시스템 장애에 주가 하락…사이버공격에 트레이더들 긴장", B, "2026-10-16", "https://www.bloomberg.com/news/newsletters/2026-10-16/h-m-outage-hits-stock-as-cyberattacks-spook-traders",
     "H&M의 시스템 장애가 주가를 끌어내리면서 잇단 사이버공격에 유통주 트레이더들의 경계가 커졌다 (제목 기준)"),
  it("슈퍼마켓 사이버공격, 식품 안보 위협을 키운다", B, "2026-10-16", "https://www.bloomberg.com/news/newsletters/2026-10-16/supermarket-cyberattacks-add-to-food-security-threats",
     "슈퍼마켓을 겨냥한 사이버공격이 이어지면서 이미 쌓여 있던 식품 안보 위협 요인이 하나 더 늘었다는 분석이 나왔다 (제목 기준)"),
  it("슈퍼마켓 운영사 아홀드, 사이버 사고 5일 지나도 웹사이트·앱 중단", R, "2026-10-16", "https://www.reuters.com/business/supermarket-operator-aholds-websites-app-remain-offline-5-days-after-cyber-2026-10-16/",
     "아홀드 델레이즈가 사이버 사고 뒤 닷새째 웹사이트와 앱을 열지 못하면서, 알버트 하인·스톱앤숍 등 유럽·미국 브랜드의 온라인 주문이 멈추고 환불이 이어졌다")
 ]})

# G1-035
items.append({
 "cid": "G1-035", "attachTo": "n-tg-0162",
 "title": "우크라 가스 비축 6년 만에 최대…러 드론 공습에 100만 명 넘게 정전",
 "one": "러시아가 우크라이나 전력망을 노린 겨울 공세를 이어 가며 드론 공습으로 수십만 가구 전기를 끊고 한때 100만 명 넘는 소비자가 정전을 겪는 가운데, 나프토가스가 가스 비축을 6년 만의 최대인 160억㎥로 쌓아 겨울 난방 연료 여유를 확보했다",
 "facts": [
  "무엇이: 나프토가스 대표대행은 우크라이나 지하 저장고 가스가 160억㎥로 2020년 이후 최대라고 했고, 정부의 겨울 최소 목표는 132억㎥, 지난 시즌 시작 때는 140억㎥ 미만이었다 [사실]",
  "공격: 나프토가스는 올해 자사 자산이 러시아 공격을 400회 넘게 받아 2025년의 두 배였고, 산업 수요 감소가 비축 확대를 도왔다고 했다 [사실]",
  "정전: 한때 100만 명 넘는 소비자가 정전을 겪었고, 러시아 드론 공격으로 3명이 숨지고 수십만 가구의 전력이 끊겼다 [제목]",
  "기존: 뉴욕타임스는 러시아가 미사일·드론 최대 1,000발로 발전설비 약 15GW를 없애려는 겨울 공격 계획 문서를 보도했다 [사실]",
  "철강: 잇단 공습 뒤 우크라이나 철강 생산의 약 90%가 멈춘 것으로 전해졌다 [사실]"
 ],
 "basis": "partial",
 "check": "가스 비축 160억㎥·목표 132억㎥·공격 400회 이상은 검색 결과 요약으로 확인. 100만 명 정전과 드론 공격 사상자·정전 규모는 확인 못 해 제목만 근거",
 "src": [
  {"o": "인터팩스-우크라이나(uazmi 전재)", "d": "2026-10-16", "u": "https://uazmi.org/news/post/adcb48ca3f1943e07aad31527040554d"},
  {"o": "UNIAN", "d": "2026-10-16", "u": "https://unian.ua/economics/energetics/ukrajina-nakopichila-rekordniy-obsyag-gazu-i-navit-prodala-yogo-za-kordon-13531224.html"}
 ],
 "inds": ["power", "gas"], "nodes": ["power/grid", "gas/regas"],
 "vc": [
  vc("gas", "regas", "공급", "up", "실제", "우크라 가스 저장량 160억㎥로 6년 만에 최대"),
  vc("power", "grid", "공급", "down", "실제", "러 드론 공습에 100만 명 넘게 정전")
 ],
 "added": "이번 로이터 3건으로 우크라이나 가스 비축 160억㎥의 6년 만 최대 기록과 러시아 드론 공습에 따른 100만 명 이상 정전, 3명 사망이 추가됐다",
 "items": [
  it("나프토가스 대표 '우크라 가스 비축, 겨울 앞두고 6년 만에 최대'", R, "2026-10-16", "https://www.reuters.com/business/energy/naftogaz-chief-says-ukraines-gas-reserves-hit-six-year-high-ahead-winter-2026-10-16/",
     "나프토가스가 겨울을 앞두고 우크라이나 가스 비축이 160억㎥로 6년 만에 최대라고 밝히면서, 러시아의 잇단 공격 속에서도 난방 가스 공급 여력이 커졌다"),
  it("우크라이나 소비자 100만 명 넘게 한때 정전 겪어…에너지 당국", R, "2026-10-16", "https://www.reuters.com/business/energy/over-1-million-consumers-were-facing-power-cuts-ukraine-some-point-energy-2026-10-16/",
     "우크라이나에서 한때 100만 명 넘는 소비자가 정전을 겪으면서, 겨울을 앞둔 전력 공급 차질이 넓게 번진 것으로 나타났다 (제목 기준)"),
  it("러시아 드론 공격에 우크라 3명 사망, 수십만 가구 정전", R, "2026-10-17", "https://www.reuters.com/world/europe/russian-drones-kill-3-people-ukraine-cut-power-hundreds-thousands-2026-10-16/",
     "러시아 드론 공격으로 우크라이나에서 3명이 숨지고 수십만 가구의 전력이 끊기면서, 전력망을 겨냥한 겨울 공세가 이어지고 있다 (제목 기준)")
 ]})

# G1-041
items.append({
 "cid": "G1-041", "attachTo": "n-tg-0166",
 "title": "후티 미사일, 아덴 공항 타격…사우디 연합군은 얀부行 탄도미사일 요격",
 "one": "후티가 사우디의 오만 회담 제안을 거부한 채 공격을 이어 가며 16일 아덴 국제공항에 미사일 2발을 떨어뜨리고 사우디 원유 수출항 얀부를 향해 탄도미사일까지 쏘면서, 호르무즈를 우회하는 사우디 홍해 수출로에 대한 위협이 커지고 있다",
 "facts": [
  "무엇이: 아덴 보안당국은 16일 미사일 2발이 아덴 국제공항 구내에 떨어졌다며 후티를 지목했고, 일주일도 안 돼 두 번째 공격이었으며 사상자는 없었다 [사실]",
  "얀부: 사우디 주도 연합군은 얀부로 향하던 탄도미사일을 요격했고, 홍해 상공 순항미사일 2발과 남부·리야드 지역 드론 3대도 격추했다고 밝혔다 [사실]",
  "의미: 얀부는 사우디가 호르무즈 해협을 거치지 않고 홍해로 원유를 내보내는 핵심 출구다 [사실]",
  "발사 지점: 채널은 미사일이 알달레주 담트·알후샤 지역에서 발사됐다고 전했다 [채널]",
  "기존: 후티는 사우디의 오만 무스카트 회담 제안을 거부했고, 10월에만 리야드 공항을 20차례 공격했다 [사실]"
 ],
 "basis": "verified",
 "check": "아덴 공항 미사일 2발·얀부행 미사일 요격·추가 격추는 검색 결과 요약으로 확인. 발사 지점은 채널 전언",
 "src": [
  {"o": "The New Arab", "d": "2026-10-16", "u": "https://www.newarab.com/news/missiles-hit-aden-airport-saudi-coalition-intercepts-missile"},
  {"o": "TRT World", "d": "2026-10-16", "u": "https://www.trtworld.com/article/2e5763e8ac93"},
  {"o": "신화통신", "d": "2026-10-17", "u": "https://english.news.cn/20261017/7ae57006048849aa849b5cb839f5cced/c.html"}
 ],
 "inds": ["macro", "oil"], "nodes": ["macro/geo"],
 "vc": [
  vc("oil", "transport", "공급", "down", "예상", "후티 미사일이 사우디 수출항 얀부 겨냥"),
  vc("aero", "airports", "공급", "down", "실제", "아덴 국제공항에 미사일 2발 낙하")
 ],
 "added": "이번 텔레그램·로이터 2건으로 아덴 공항 미사일 2발 낙하와 사우디 원유 수출항 얀부를 노린 탄도미사일 요격, 홍해 상공 순항미사일 격추가 추가됐다",
 "items": [
  it("후티 탄도미사일, 예멘 아덴 국제공항 인근 타격 영상 공개", "텔레그램 미국 주식 인사이더", "2026-10-17", "https://t.me/insidertracking/66491",
     "후티 반군이 알달레주에서 쏜 탄도미사일이 아덴 국제공항 인근을 때린 영상이 공개되면서, 예멘 정부 거점 공항에 대한 위협이 다시 드러났다"),
  it("미사일 아덴 공항 타격…사우디 연합군, 얀부行 미사일 요격", R, "2026-10-17", "https://www.reuters.com/world/middle-east/missiles-hit-aden-airport-saudi-led-coalition-intercepts-missile-headed-yanbu-2026-10-16/",
     "미사일 2발이 아덴 공항에 떨어지고 사우디 연합군이 원유 수출항 얀부로 향하던 탄도미사일을 요격하면서, 사우디 홍해 수출 거점까지 공격 대상이 됐다")
 ]})

# G1-046
items.append({
 "cid": "G1-046", "attachTo": "",
 "title": "美 9월 제조업 생산 0.3% 반등…반도체 2.1% 늘며 견인",
 "one": "연준 집계에서 미국 9월 제조업 생산이 반도체 2.1% 증가에 힘입어 0.3% 늘며 8월 감소를 되돌리고 전체 산업생산도 0.7% 뛰었지만, 자동차 생산이 3개월 연속 줄어 하이테크를 뺀 제조업 회복은 더딘 모습이다",
 "facts": [
  "무엇이: 연준에 따르면 9월 제조업 생산은 0.3% 늘어 수정된 8월 0.2% 감소를 되돌렸고, 블룸버그 조사 중간값과 같았다 [사실]",
  "반도체: 반도체·전자부품 생산은 9월 2.1% 늘어 1년 전보다 19.9% 많았고, 3분기에는 연율 28.4% 늘었다 [사실]",
  "자동차: 자동차·부품 생산은 3.0% 줄어 3개월 연속 감소했고, 하이테크를 뺀 제조업 생산은 전월 대비 0.2%, 전년 대비 0.7% 증가에 그쳤다 [사실]",
  "전체: 광업·유틸리티를 포함한 산업생산은 0.7% 늘어 5개월 만에 가장 많이 늘었고, 유틸리티 생산이 3.5% 증가했다 [사실]"
 ],
 "basis": "verified",
 "check": "연준 G.17 발표 수치를 검색 결과 요약으로 확인(연준 페이지는 열지 않음)",
 "src": [
  {"o": "연준 이사회 G.17", "d": "2026-10-16", "u": "https://www.federalreserve.gov/releases/g17/current/default.htm"},
  {"o": "investingLive", "d": "2026-10-16", "u": "https://investinglive.com/news/us-september-industrial-production-0-7-vs-0-4-expected/"},
  {"o": "Breitbart", "d": "2026-10-16", "u": "https://www.breitbart.com/economy/2026/10/16/u-s-machinery-metals-and-chip-production-climb-as-manufacturing-expands/"}
 ],
 "inds": ["macro"], "nodes": ["macro/growth", "macro/semis", "macro/cb"],
 "vc": [
  vc("macro", "growth", "공급", "up", "실제", "9월 제조업 생산 0.3% 반등"),
  vc("semis", "foundry", "공급", "up", "실제", "반도체·전자부품 생산 2.1% 증가"),
  vc("macro", "cb", "-", "flat", "실제", "연준 집계 9월 산업생산 0.7% 증가")
 ],
 "fed": [
  {"k": "", "who": "연준", "role": "산업생산 통계 발표", "kind": "조사·보고서", "stance": "",
   "t": "9월 제조업 생산이 반도체 덕에 0.3% 늘었다고 집계했다", "d": "2026-10-16",
   "u": "https://www.bloomberg.com/news/articles/2026-10-16/us-factory-output-increased-0-3-in-september-fed-data-show"}
 ],
 "added": "이번 로이터 1건으로 미국 9월 제조업 생산 증가가 다시 확인되고, 유틸리티 생산 3.5% 증가에 힘입은 전체 산업생산 0.7% 증가가 추가됐다",
 "items": [
  it("美 공장 생산, 반도체와 공급재 생산 덕에 반등", B, "2026-10-16", "https://www.bloomberg.com/news/articles/2026-10-16/us-factory-output-increased-0-3-in-september-fed-data-show",
     "반도체와 공급재 생산이 늘면서 미국 9월 공장 생산이 0.3% 반등해 8월 감소를 되돌리고, 반도체 생산은 1년 전보다 19.9% 많아졌다"),
  it("미국 제조업 생산량, 9월에 증가(연준 산업생산 통계)", R, "2026-10-16", "https://www.reuters.com/business/us-manufacturing-output-rises-september-2026-10-16/",
     "미국 9월 제조업 생산이 늘고 유틸리티 생산 3.5% 증가로 전체 산업생산이 0.7% 뛰면서, 자동차 생산 감소에도 공장 경기가 나아졌다")
 ]})

# G1-052
items.append({
 "cid": "G1-052", "attachTo": "n-bbg-0104",
 "title": "IMF 'ECB 연내 최소 한 차례 더 인상'…AI 붐 자금 쟁탈에 중앙은행 인상론",
 "one": "나겔 분데스방크 총재 등 ECB 인사들의 추가 인상론에 이어 IMF가 ECB가 연내 최소 한 차례 0.25%포인트 더 올릴 것으로 내다보고 AI 붐발 자금 쟁탈 속 중앙은행들이 금리 인상을 저울질하면서, 10월 29일 ECB 회의의 인상 가능성이 커지고 있다",
 "facts": [
  "무엇이: IMF는 유럽 전망에서 ECB가 높은 물가에 맞서 올해 최소 한 차례 더 0.25%포인트 올릴 가능성이 크다고 봤다 [사실]",
  "배경: ECB는 이란 전쟁발 에너지 가격 급등에 따른 물가 상승에 맞서 6월과 9월 0.25%포인트씩 올렸다 [사실]",
  "이후: IMF는 2028년 물가 목표 복귀를 위해 추가 긴축이 필요할 수 있고, 에너지 가격 보전용 재정 지원이 물가 억제를 방해할 수 있다고 경고했다 [사실]",
  "글로벌: AI 붐이 자금 쟁탈을 부추기면서 중앙은행들이 금리 인상을 검토하고 있다 [제목]",
  "기존: 나겔 총재는 추가 인상을 배제하지 않았고 렌·카작스 총재는 신중론을 폈으며, ECB 예금금리는 2.50%다 [사실]"
 ],
 "basis": "partial",
 "check": "IMF의 ECB 추가 인상 전망과 6·9월 인상은 검색 결과 요약으로 확인. AI 붐발 자금 쟁탈과 중앙은행 인상 검토 기사는 확인 못 해 제목만 근거(연준 인사 포함 여부 모름)",
 "src": [
  {"o": "IndexBox", "d": "2026-10-16", "u": "https://www.indexbox.io/blog/imf-ecb-may-need-at-least-one-more-25-basis-point-rate-hike-in-2026/"},
  {"o": "GuruFocus", "d": "2026-10-16", "u": "https://www.gurufocus.com/news/9127428/imf-predicts-ecb-rate-hikes-needed-to-combat-inflation"}
 ],
 "inds": ["macro"], "nodes": ["macro/cb", "macro/rates"],
 "vc": [
  vc("macro", "cb", "가격", "up", "예상", "IMF, ECB 연내 최소 한 차례 추가 인상 예상"),
  vc("macro", "rates", "가격", "up", "예상", "AI 붐 자금 쟁탈에 중앙은행 금리 인상 검토")
 ],
 "added": "이번 로이터 2건으로 IMF의 ECB 연내 최소 한 차례 추가 인상 전망과 AI 붐발 자금 쟁탈 속 각국 중앙은행의 금리 인상 검토가 추가됐다",
 "items": [
  it("IMF, 2026년 ECB 최소 한 차례 0.25%p 추가 인상 예상", R, "2026-10-16", "https://www.reuters.com/business/imf-expects-least-one-more-25-bps-ecb-rate-hike-2026-2026-10-16/",
     "IMF가 ECB가 높은 물가에 맞서 올해 최소 한 차례 0.25%포인트 더 올릴 것으로 보면서, 6월·9월에 이은 세 번째 인상 가능성이 커졌다"),
  it("AI 붐발 자금 쟁탈에 중앙은행들 금리 인상 저울질", R, "2026-10-17", "https://www.reuters.com/business/finance/central-bankers-eye-higher-rates-ai-boom-fuels-scramble-cash-2026-10-16/",
     "AI 붐이 자금 쟁탈을 부추기면서 각국 중앙은행이 금리 인상을 저울질해, 기업과 정부의 차입 비용이 더 오를 수 있다 (제목 기준)")
 ]})

# G1-058
items.append({
 "cid": "G1-058", "attachTo": "n-bbg-0116",
 "title": "사모신용 균열 확산…오크트리 A-Cap 보험사 인수 무산, BNY는 ABS 사각지대 겨냥",
 "one": "무디스가 PIK를 포함한 사모신용 부도율을 5.8%로 높여 잡고 은행들이 호주 사모신용 펀드 대출을 줄인 데 이어, 오크트리의 A-Cap 보험사 인수가 무산되고 BNY가 트라이컬러 사태 뒤 ABS 담보 사각지대 점검에 나서면서 사모신용 연계 시장의 신뢰 부담이 커지고 있다",
 "facts": [
  "무엇이: 오크트리의 A-Cap 보험사 인수 거래가 무산되면서 새로운 협상이 시작됐다 [제목]",
  "배경: 오크트리는 3월 A-Cap 계열 애틀랜틱코스트라이프 지배지분 인수에 합의했지만, 사우스캐롤라이나 보험 당국은 9월 777파트너스 노출을 이유로 이 보험사와 재보험 계열사의 회생절차를 추진했다 [사실]",
  "ABS: BNY는 약 1조 달러 ABS 시장의 사각지대를 겨냥해 소비자 대출·ABS 거래를 추적하는 디지털 등록부를 내년 자동차 대출부터 내놓을 계획이다 [미확인]",
  "트라이컬러: 트라이컬러 기록 검토에서 활성 대출 7만 건 중 약 2만 9,000건이 창고 대출과 증권화에 이중으로 담보 잡힌 것으로 전해졌다 [사실]",
  "기존: 무디스는 PIK 변경·만기 연장을 포함하면 사모신용 차입자 부도율이 4%에서 5.8%로 오른다고 밝혔다 [사실]"
 ],
 "basis": "partial",
 "check": "오크트리 3월 인수 합의·9월 회생절차 추진과 트라이컬러 이중 담보는 검색 결과 요약으로 확인. 인수 무산·새 협상은 독립 확인 못 함(제목 기준). BNY 등록부 내용은 블룸버그 전재 글 요약에만 있어 미확인",
 "src": [
  {"o": "Insurance Journal", "d": "2026-09-16", "u": "https://www.insurancejournal.com/news/southeast/2026/09/16/885325.htm"},
  {"o": "Alternative Credit Investor", "d": "2026-03-16", "u": "https://alternativecreditinvestor.com/2026/03/16/oaktree-deepens-insurance-push-with-atlantic-coast-life-takeover/"},
  {"o": "Credit Chronometer", "d": "", "u": "https://www.creditchronometer.com/double-trouble-in-tricolor-risks-in-collateral-misrepresentation"}
 ],
 "inds": ["fin"], "nodes": [],
 "vc": [
  vc("fin", "insurance", "수요", "down", "실제", "오크트리의 A-Cap 보험사 인수 무산"),
  vc("fin", "pcredit", "가격", "up", "실제", "PIK 포함 사모신용 부도율 5.8%로 상승")
 ],
 "added": "이번 블룸버그 2건으로 오크트리의 A-Cap 보험사 인수 무산과 새 협상, BNY의 트라이컬러 사태 뒤 ABS 시장 사각지대 점검이 추가됐다 (제목 기준)",
 "items": [
  it("BNY, 트라이컬러 사태로 흔들린 ABS 시장의 사각지대 겨냥", B, "2026-10-16", "https://www.bloomberg.com/news/articles/2026-10-16/bny-targets-blind-spots-in-abs-after-tricolor-mess-rocked-market",
     "BNY가 트라이컬러 사태로 드러난 ABS 시장의 사각지대를 겨냥하면서, 이중 담보 같은 증권화 위험을 걸러 낼 장치가 마련될 수 있다 (제목 기준)"),
  it("오크트리의 A-Cap 보험사 인수 무산…새 협상 시작", B, "2026-10-17", "https://www.bloomberg.com/news/articles/2026-10-16/oaktree-s-deal-to-buy-a-cap-insurer-crumbles-spawning-new-talks",
     "오크트리의 A-Cap 보험사 인수 거래가 무산되고 새 협상이 시작되면서, 사모신용과 얽힌 부실 보험사 정리 작업이 다시 불확실해졌다 (제목 기준)")
 ]})

# G1-066
items.append({
 "cid": "G1-066", "attachTo": "n-rtr-0317",
 "title": "세계은행, 베네수엘라에 2년간 최대 50억 달러 대출 검토…제재 해제 뒤 재건 지원",
 "one": "미국이 베네수엘라 국회의장 제재를 푼 데 이어 세계은행이 2년간 최대 50억 달러 대출을 검토하고 첫해 최대 20억 달러는 다른 다자은행 연체 해소를 조건으로 걸면서, 베네수엘라 채무 재조정과 재건 자금 유입의 길이 열릴 수 있다",
 "facts": [
  "무엇이: 세계은행 수사나 코르데이루 게하 중남미·카리브 부총재는 앞으로 2년간 공공·민간 부문을 합쳐 베네수엘라에 최대 50억 달러를 빌려줄 수 있다고 말했다 [사실]",
  "조건: 첫해 최대 20억 달러는 베네수엘라가 미주개발은행 20억 달러 넘는 연체 등 다른 다자은행 연체를 풀어야 하며, 모든 자금은 이사회 승인이 필요하다 [사실]",
  "첫 사업: 수도·전력 분야 5억 달러 사업이 이미 정해졌고, 세계은행의 베네수엘라 대출은 2005년이 마지막이었다 [사실]",
  "채무: 세계은행은 거시재정 체계와 채무 재조정 작업을 돕고 있으며, 민간 추산 채무는 약 1,700억 달러다 [사실]",
  "기존: 미국 재무부는 14일 호르헤 로드리게스 국회의장을 제재 명단에서 뺐다 [사실]"
 ],
 "basis": "verified",
 "check": "대출 규모·조건·첫 사업·연체·채무 추산은 검색 결과 요약(여러 매체)으로 확인",
 "src": [
  {"o": "La República", "d": "2026-10-16", "u": "https://www.larepublica.co/globoeconomia/el-banco-mundial-preve-posibles-prestamos-de-hasta-us-5-000-millones-a-venezuela-4504285"},
  {"o": "El Informador Venezuela", "d": "2026-10-16", "u": "https://elinformadorve.com/16/10/2026/actualidad/banco-mundial-evalua-prestamos-de-hasta-5-000-millones-de-dolares-para-venezuela-en-dos-anos/"},
  {"o": "InvestNews", "d": "2026-10-16", "u": "https://investnews.com.br/economia/banco-mundial-preve-emprestar-ate-us-5-bilhoes-a-venezuela/"}
 ],
 "inds": ["macro"], "nodes": ["macro/liquidity"],
 "vc": [
  vc("macro", "liquidity", "공급", "up", "예상", "세계은행, 베네수엘라에 최대 50억 달러 대출 검토")
 ],
 "added": "이번 블룸버그 1건으로 세계은행의 2년간 최대 50억 달러 대출 검토와 수도·전력 5억 달러 첫 사업, 다자은행 연체 해소 조건이 추가됐다",
 "items": [
  it("세계은행, 베네수엘라에 최대 50억 달러 대출 가능성", B, "2026-10-16", "https://www.bloomberg.com/news/articles/2026-10-16/world-bank-sees-up-to-5-billion-in-possible-loans-to-venezuela",
     "세계은행이 베네수엘라에 2년간 최대 50억 달러 대출을 검토하면서, 2005년 이후 끊긴 국제 개발 자금이 다시 들어갈 길이 열렸다")
 ]})

# G1-072
items.append({
 "cid": "G1-072", "attachTo": "n-bbg-0254",
 "title": "아시아 겨울 연료 쟁탈…카타르 8월 아시아 LNG 수출 '0', 수입가 32% 상승",
 "one": "러시아 최대 원료탄 광산 중단과 한국의 석탄·원전 발전 확대에 이어 카타르가 8월 아시아 6대 LNG 시장에 수출을 전혀 못 하고 북미산이 공백의 약 63%만 메우면서, 이들 시장의 LNG 평균 수입가가 31.8% 올라 겨울 연료 수급 부담이 커지고 있다",
 "facts": [
  "무엇이: 카타르는 8월 중국·일본·한국·대만·태국·싱가포르에 LNG를 전혀 수출하지 못했고, 1년 전에는 410만 톤이었다 [채널]",
  "대체: 미국산은 110만 톤에서 290만 톤으로 늘었고 캐나다산은 90만 톤으로, 북미가 카타르 물량의 약 63%를 대체했다 [채널]",
  "가격: 6개 시장 LNG 수입량은 12.5% 줄어든 1,690만 톤, 평균 수입가는 31.8% 오른 MMBtu당 14.1달러였다 [채널]",
  "배경: 카타르 LNG 수출은 3~8월 1년 전보다 96% 줄었고, 10월 수출은 약 60만 톤으로 줄어들 것이라는 케플러 집계가 나왔다 [사실]",
  "기존: 러시아 최대 원료탄 광산 라스파드스카야가 90일 조업 중단 명령을 받았고, 한국은 겨울 가스난에 석탄·원전 발전을 늘리기로 했다 [사실]"
 ],
 "basis": "partial",
 "check": "카타르 LNG 수출 급감(3~8월 96% 감소)과 미국산 대체는 검색 결과 요약으로 확인. 8월 아시아 6대 시장 수출 0, 63% 대체, 수입가 31.8% 상승 수치는 확인 못 해 채널 전언",
 "src": [
  {"o": "Hellenic Shipping News", "d": "", "u": "https://www.hellenicshippingnews.com/u-s-lng-fills-qatar-gap-as-south-korea-shifts-imports-and-boosts-profits/"},
  {"o": "Baird Maritime", "d": "", "u": "https://www.bairdmaritime.com/shipping/tankers/gas/opinion-the-iran-war-is-choking-middle-east-lng-with-no-end-in-sight"}
 ],
 "inds": ["gas", "coal"], "nodes": ["gas/liquefaction", "gas/trade", "coal/met"],
 "vc": [
  vc("gas", "liquefaction", "공급", "down", "실제", "카타르 8월 아시아 6대 시장 LNG 수출 0"),
  vc("gas", "trade", "가격", "up", "실제", "아시아 6대 시장 LNG 평균 수입가 31.8% 상승")
 ],
 "added": "이번 텔레그램 1건으로 카타르의 8월 아시아 6대 시장 LNG 수출 중단과 북미산의 약 63% 대체, 평균 수입가 31.8% 상승이 추가됐다",
 "items": [
  it("카타르, 8월 아시아 6대 시장 LNG 수출 '0'…북미가 63% 대체", "텔레그램 트릴리온", "2026-10-17", "https://t.me/Trillion_labs/10663",
     "카타르가 8월 아시아 6대 시장에 LNG를 전혀 보내지 못하고 북미산이 공백의 63%만 메우면서, 이들 시장의 평균 LNG 수입가가 31.8% 올랐다")
 ]})

# G1-078
items.append({
 "cid": "G1-078", "attachTo": "n-bbg-0252",
 "title": "템스워터, B급 채권단과 재자본화 합의…채권 약 10억 파운드 탕감",
 "one": "긴급 자금 한도를 54억 파운드로 늘려 달라고 요청한 템스워터가 B급 채권 60% 이상 보유자와 약 10억 파운드 탕감에 5.9% 회수 조건으로 합의하면서, 오프왓 협의와 2027년 3월 선순위 만기 전 재자본화 성사가 다음 관문이 됐다",
 "facts": [
  "무엇이: 템스워터는 16일 후순위 B급 채권 60% 이상 보유자가 약 10억 파운드 탕감안에 합의했다고 밝혔다 [사실]",
  "조건: 이들은 재편 회사 지분 등으로 약 5.9%를 회수하고 1억 5,000만 파운드 신규 지분 참여권을 받으며, 합의는 전체 재자본화 조건 합의와 오프왓의 공개 협의 개시를 전제로 한다 [사실]",
  "일정: 회사는 2027년 3월 선순위 채권 만기 전 구조조정 완료가 확실하지 않아 모회사가 일정을 늘리는 임시 거래를 계획하고 있다 [사실]",
  "이자: 템스워터는 재자본화가 끝날 때까지 A·B급 채권 이자를 전액 현금으로 낸다고 했다 [사실]",
  "기존: 템스워터는 긴급 자금 한도를 24억 파운드 늘린 54억 파운드로 키워 달라고 요청했고, 채권단은 10월 29일까지 투표한다 [사실]"
 ],
 "basis": "verified",
 "check": "B급 채권단 합의 비율·탕감액·회수율·조건·임시 거래 계획은 검색 결과 요약(회사 공시 포함)으로 확인",
 "src": [
  {"o": "Investing.com", "d": "2026-10-16", "u": "https://uk.investing.com/news/stock-market-news/thames-water-reaches-deal-with-class-b-creditors-on-debt-terms-93CH-4914968"},
  {"o": "ADVFN(템스워터 공시)", "d": "2026-10-16", "u": "https://uk.advfn.com/stock-market/london/2-62-gtd-sec-snr-cls-a-AW14/share-news/Thames-Water-Utilities-Limited-Recapitalisation-Up/99510599"},
  {"o": "Finimize", "d": "2026-10-16", "u": "https://finimize.com/content/thames-water-strikes-a-deal-with-class-b-creditors"}
 ],
 "inds": ["utilities"], "nodes": [],
 "vc": [
  vc("utilities", "capital", "공급", "down", "예상", "B급 채권 약 10억 파운드 탕감 합의")
 ],
 "added": "이번 로이터 1건으로 B급 채권 60% 이상 보유자의 약 10억 파운드 탕감 합의와 5.9% 회수 조건, 2027년 3월 만기를 늘리는 임시 거래 계획이 추가됐다",
 "items": [
  it("英 템스워터, 핵심 B급 채권단과 재자본화 합의", R, "2026-10-17", "https://www.reuters.com/world/uk/uks-thames-water-reaches-deal-with-key-class-b-creditors-recapitalisation-2026-10-16/",
     "템스워터가 핵심 B급 채권단과 재자본화에 합의하면서 약 10억 파운드 탕감과 5.9% 회수 조건으로 회생안의 한 고비를 넘었다")
 ]})

# G1-084
items.append({
 "cid": "G1-084", "attachTo": "n-tg-0226",
 "title": "北, AI 유도 초고속 정밀어뢰 시험…순항미사일 이어 수중 무기 과시",
 "one": "북한이 14일 잠수함발사 전략순항미사일 2종에 이어 15일 AI로 표적을 찾고 유도한다는 초고속 정밀유도 어뢰를 시험했다고 밝히면서, 한 주 새 잇따른 수중 무기 시험으로 한반도 지정학 위험이 다시 커지고 있다",
 "facts": [
  "무엇이: 조선중앙통신은 17일 북한이 15일 초고속 정밀유도 어뢰 무기체계 Zam-2.0을 시험해 기술 개량을 확인했다고 보도했다 [사실]",
  "AI: 북한은 AI가 표적 탐지와 유도를 맡는다고 했지만 사거리·속도·시험 장소나 근거는 밝히지 않았다 [사실]",
  "시험: 북한은 지난 5년간 180차례 넘는 관련 시험으로 추진 성능을 높였다고 했다 [사실]",
  "기존: 북한은 14일 잠수함에서 쏘는 전략순항미사일 2종을, 12일에는 전술탄도미사일을 쐈다 [사실]"
 ],
 "basis": "verified",
 "check": "어뢰 시험 날짜·AI 주장·180차례 시험은 검색 결과 요약으로 확인. 무기 이름 표기는 매체마다 달라 영문 Zam-2.0으로 적음",
 "src": [
  {"o": "코리아타임스", "d": "2026-10-17", "u": "https://www.koreatimes.co.kr/foreignaffairs/northkorea/20261017/n-korea-conducts-underwater-test-of-new-precision-guided-torpedo-using-ai-kcna"},
  {"o": "코리아헤럴드", "d": "2026-10-17", "u": "https://www.koreaherald.com/article/10905699"},
  {"o": "아주경제", "d": "2026-10-17", "u": "https://www.ajupress.com/view/20261017093741976"}
 ],
 "inds": ["macro"], "nodes": ["macro/geo"],
 "vc": [
  vc("macro", "geo", "-", "flat", "실제", "북한 수중 무기 시험 잇따라 지정학 위험 부각")
 ],
 "added": "이번 로이터 1건으로 15일 AI 유도 초고속 정밀어뢰 시험과 지난 5년간 180차례 넘는 관련 시험을 거쳤다는 북한 주장이 추가됐다",
 "items": [
  it("북한, AI 탑재 신형 어뢰 시험…조선중앙통신", R, "2026-10-17", "https://www.reuters.com/world/asia-pacific/north-korea-tests-new-ai-equipped-torpedo-kcna-says-2026-10-16/",
     "북한이 AI로 표적을 찾고 유도한다는 신형 초고속 어뢰를 시험했다고 밝히면서, 잠수함발사 순항미사일에 이은 수중 무기 과시가 이어졌다")
 ]})

out = {"agent": "W2", "searches_used": 16, "fetches_used": 0, "items": items, "skipped": []}
path = "/home/user/news-desk/data/mix-2026-10-17/out2/W2.json"
import os
os.makedirs(os.path.dirname(path), exist_ok=True)
json.dump(out, open(path, "w"), ensure_ascii=False, indent=1)

tail = re.compile(r' \((제목 기준|채널 전언)\)$')
bad = []
for x in items:
    L = lambda s: len(tail.sub('', s))
    n = len(x["items"])
    lo, hi = (80, 130) if (n == 1 and not x["attachTo"]) else (90, 160)
    if not (20 <= len(x["title"]) <= 50): bad.append((x["cid"], "title", len(x["title"])))
    if not (lo <= L(x["one"]) <= hi) or not x["one"].endswith("다"): bad.append((x["cid"], "one", L(x["one"])))
    if "added" in x and not (60 <= L(x["added"]) <= 140): bad.append((x["cid"], "added", L(x["added"])))
    if not (2 <= len(x["facts"]) <= 5): bad.append((x["cid"], "facts", len(x["facts"])))
    for f in x["facts"]:
        if "|" in f or "**" in f: bad.append((x["cid"], "factchar"))
    for i in x["items"]:
        if not (25 <= len(i["t"]) <= 60): bad.append((x["cid"], "t", len(i["t"]), i["t"]))
        if "s" in i and not (45 <= L(i["s"]) <= 110): bad.append((x["cid"], "s", L(i["s"]), i["s"][:30]))
    for v in x["vc"]:
        if not (12 <= len(v["t"]) <= 45): bad.append((x["cid"], "vc", len(v["t"])))
    for f in x.get("fed", []):
        if not (20 <= len(f["t"]) <= 70): bad.append((x["cid"], "fed", len(f["t"])))
    s = json.dumps(x, ensure_ascii=False)
    if "{{" in s or "**" in s: bad.append((x["cid"], "emph"))
for b in bad: print(b)
print("ok", len(items))
