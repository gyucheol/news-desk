import json
B = '/home/user/news-desk/data/industry-2026-10-17'
ids = [json.loads(l)['id'] for l in open(f'{B}/news/fin.jsonl')]

R = 'https://www.reuters.com/'
U = {
 'bofa': R + 'legal/government/bank-america-says-it-has-completed-lot-work-consent-order-2026-10-14/',
 'regions': R + 'markets/us/us-regional-banks-join-bigger-peers-signaling-resilient-economy-lending-holds-2026-10-16/',
 'carlyle': 'https://www.bloomberg.com/news/articles/2026-10-16/carlyle-buys-7-7-billion-in-consumer-loans-as-truist-revamps',
 'cw': R + 'business/coreweave-shares-bonds-headed-steep-weekly-losses-ai-borrowing-concerns-mount-2026-10-16/',
 'dc': R + 'business/finance/market-selloff-rising-rates-test-ai-data-centre-deal-boom-2026-10-15/',
 'vwap': R + 'world/india/indias-derivatives-trading-volumes-may-recover-after-settlement-rule-changes-2026-10-16/',
 'lseg': R + 'business/lseg-talks-buy-octus-about-35-billion-2026-10-13/',
 'man': R + 'business/man-groups-assets-under-management-hit-record-2709-billion-volatility-drives-2026-10-16/',
 'blk': R + 'business/blackrock-profit-jumps-resilient-markets-boost-fees-2026-10-14/',
 'bx': 'https://www.bloomberg.com/news/newsletters/2026-10-13/blackstone-hits-6-billion-european-exit-record',
 'isaias': R + 'legal/litigation/insured-losses-hurricane-isaias-could-reach-2-billion-verisk-says-2026-10-13/',
 'acap': 'https://www.bloomberg.com/news/articles/2026-10-16/oaktree-s-deal-to-buy-a-cap-insurer-crumbles-spawning-new-talks',
 'ramp': R + 'technology/fintech-firm-ramp-raises-185-billion-60-billion-valuation-2026-10-15/',
 'upi': R + 'world/india/india-postpones-upi-payment-fee-rollout-after-diwali-festival-2026-10-13/',
 'ubs': R + 'legal/transactional/ubs-exploring-options-abroad-case-swiss-rules-prove-intolerable-sources-say-2026-10-15/',
 'sfc': R + 'legal/government/baicha-baidao-notes-hong-kong-regulators-trading-suspension-over-ipo-rigging-2026-10-14/',
 'flows': R + 'business/us-equity-funds-draw-renewed-inflows-treasury-yields-ease-2026-10-16/',
 'hf': R + 'business/finance/hedge-funds-are-top-draw-asia-investors-look-beyond-bonds-2026-10-13/',
 'fed': R + 'markets/us/feds-hammack-warns-inflation-expectations-deterioration-could-require-fed-2026-10-15/',
 'ey': 'https://www.ey.com/en_ch/newsroom/2026/10/fewer-ipos-more-capital-global-market-remains-robust-initial-signs-of-an-upturn-in-switzerland',
 'ms': 'https://www.cnbc.com/2026/10/14/morgan-stanley-ms-q3-2026-earnings.html',
 'bac8k': 'https://www.sec.gov/Archives/edgar/data/0000070858/000007085826000481/bac-09302026ex993.htm',
 'moodys': 'https://www.privateequitywire.co.uk/pik-amendments-mask-us-private-credit-stress-moodys-warns/',
 'marsh': 'https://www.insurancejournal.com/news/national/2026/07/23/878716.htm',
 'tricolor': 'https://www.bloomberg.com/news/articles/2026-10-16/bny-targets-blind-spots-in-abs-after-tricolor-mess-rocked-market',
 'srt': 'https://www.bloomberg.com/news/articles/2026-10-13/pension-pggm-agrees-to-back-srt-tied-to-5-billion-of-ing-loans',
 'semi': 'https://t.me/HANAchina/70543',
 'italy': R + 'business/italy-raise-044-gdp-financial-sector-through-2029-fund-budget-2026-10-15/',
 'ukbank': R + 'world/uk/raising-bank-tax-is-not-best-choice-uk-budget-imf-says-2026-10-16/',
}
def S(o, d, k): return {'o': o, 'd': d, 'u': U[k]}

state = {
 'banks': [
  {'d': '2026-10-14', 'o': '로이터', 'u': U['bofa'], 'nid': 'n-rtr-0300',
   't': '뱅크오브아메리카는 12억 달러 자금세탁 방지 위반 벌금으로 3분기 순이익이 17% 줄었고, 벌금 발표 뒤 주가가 장 초반 8% 떨어져 5월 이후 최저로 밀렸습니다 [사실]'},
  {'d': '2026-10-16', 'o': '로이터', 'u': U['regions'], 'nid': 'n-rtr-0043',
   't': '미국 지역은행 리전스의 3분기 평균 대출은 전 분기보다 0.5% 늘었고 기업·산업 대출이 이끌었으며, 순상각률은 평균 대출의 0.29%로 내렸습니다 [사실]'},
 ],
 'pcredit': [
  {'d': '2026-10-16', 'o': '블룸버그', 'u': U['carlyle'], 'nid': 'n-rtr-0326',
   't': '칼라일이 트루이스트의 무담보 개인대출 77억 달러를 사기로 했고, 트루이스트는 지난달 아폴로에도 자동차대출 55억 달러를 팔아 은행 대출이 사모 신용으로 옮겨 가고 있습니다 [사실]'},
  {'d': '2026-10-16', 'o': '로이터', 'u': U['cw'], 'nid': 'n-bbg-0049',
   't': '코어위브 2031년물 수익률이 한때 16%를 넘었고, 메타·블루아울 하이페리온 데이터센터 채권은 1달러당 92센트, 블랙스톤 QTS 엑스칼리버 채권은 88센트 밑으로 내려갔습니다 [사실]'},
 ],
 'ib': [
  {'d': '2026-10-15', 'o': '로이터', 'u': U['dc'], 'nid': 'n-tg-0295',
   't': '최근 일주일 새 에어트렁크 리츠·퍼머스·SB에너지 등 데이터센터 관련 상장이 철회되거나 연기됐고, 코어위브 주가는 10월 14일 약 15.5% 급락했습니다 [채널]'},
 ],
 'markets': [
  {'d': '2026-10-16', 'o': '로이터', 'u': U['vwap'], 'nid': 'n-bbg-0231',
   't': '인도 NSE의 8월 파생 총거래대금은 종가 경매 도입 뒤 34조 4,800억 루피로 19.2% 줄었고, SEBI는 12월 7일부터 VWAP 결제로 되돌립니다 [사실]'},
 ],
 'assetmgmt': [
  {'d': '2026-10-16', 'o': '로이터', 'u': U['man'], 'nid': 'n-rtr-0328',
   't': '맨그룹 운용자산은 9월 말 사상 최대 2,709억 달러, 3분기 순유입은 101억 달러였고, 블랙록은 3분기 말 약 15조 5,000억 달러에 분기 순유입 2,050억 달러였습니다 [사실]'},
  {'d': '2026-10-13', 'o': '블룸버그', 'u': U['bx'], 'nid': 'n-bbg-0205',
   't': '블랙스톤은 올해 유럽 투자 기업 7곳을 팔아 약 60억 달러로 연간 회수 기록을 세웠지만, 퍼미라는 AI 초대형 IPO가 사모펀드 상장 회수를 밀어낸다고 했습니다 [사실]'},
 ],
 'insurance': [
  {'d': '2026-10-13', 'o': '로이터', 'u': U['isaias'], 'nid': 'n-tg-0187',
   't': '허리케인 이사야스의 육상 재산 보험 손실을 베리스크는 10억~20억 달러, 코탈리티는 20억~30억 달러로 추산했습니다 [사실]'},
  {'d': '2026-10-16', 'o': '블룸버그', 'u': U['acap'], 'nid': 'n-bbg-0116',
   't': '오크트리의 A-Cap 계열 보험사 인수가 무산돼 새 협상이 시작됐고, 이 보험사는 777파트너스 노출로 9월 당국이 회생절차를 추진한 곳입니다 [사실]'},
 ],
 'payments': [
  {'d': '2026-10-15', 'o': '로이터', 'u': U['ramp'], 'nid': 'n-bbg-0321',
   't': '지출관리 핀테크 램프가 18억 5,000만 달러를 조달하며 기업가치 600억 달러를 인정받아 4개월 전 440억 달러에서 약 36% 올랐고, 연환산 매출은 20억 달러를 넘었습니다 [사실]'},
  {'d': '2026-10-13', 'o': '로이터', 'u': U['upi'], 'nid': 'n-rtr-0119',
   't': '인도 NPCI가 10월 15일 시행하려던 UPI 가맹점 수수료 0.4% 부과를 디왈리 뒤로 미뤄 페이티엠·파인랩스 등 결제사의 수수료 수익도 늦춰지게 됐습니다 [사실]'},
 ],
 'regulation': [
  {'d': '2026-10-15', 'o': '로이터', 'u': U['ubs'], 'nid': 'n-rtr-0193',
   't': '스위스 정부안은 UBS 해외 자회사를 CET1 자본으로 100% 뒷받침하게 해 약 160억 달러 추가 자본이 필요하고, UBS는 본사 해외 이전 비상 계획을 검토 중입니다 [사실]'},
  {'d': '2026-10-13', 'o': '로이터', 'u': U['sfc'], 'nid': 'n-bbg-0320',
   't': '홍콩 SFC가 IPO 수요 조작 의혹으로 바이차바이다오 거래를 정지하고 브로커 6곳의 고객자산 최대 43억 7,946만 홍콩달러 처분을 제한했습니다 [사실]'},
 ],
}

industryState = [
 {'d': '2026-10-14', 'kind': 'demand', 'o': '로이터(BofA 주간 자금흐름)', 'u': U['flows'], 'nid': 'n-rtr-0356',
  't': '10월 14일까지 한 주 미국 주식형 펀드에 391억 달러가 들어와 연초 이후 유입이 사상 최대 6,360억 달러가 됐고, 미 국채 펀드는 16주 연속 유입이었습니다 [사실]'},
 {'d': '2026-10-13', 'kind': 'demand', 'o': '로이터(HFR 집계)', 'u': U['hf'], 'nid': 'n-rtr-0310',
  't': '세계 헤지펀드 자산은 2026년 2분기에 4,090억 달러 늘어 사상 최대 5조 6,000억 달러가 됐습니다 [사실]'},
 {'d': '2026-10-15', 'kind': 'price', 'o': '로이터', 'u': U['cw'], 'nid': 'n-bbg-0049',
  't': '코어위브 2031년 10월 만기 달러채 수익률이 10월 15일 한때 16%를 넘고 부도보험료가 1,000bp를 넘어 사상 최고였습니다 [사실]'},
 {'d': '2026-10-15', 'kind': 'policy', 'o': '로이터', 'u': U['fed'], 'nid': 'n-fed-0001',
  't': '미국 9월 소비자물가가 전년 대비 3.7% 올라 예상(3.6%)을 웃돌았고, 이후 연준의 10월 금리 인상 확률이 33%로 높아졌습니다 [사실]'},
]

summary = ('금융은 예금·보험료·연금·펀드 자금을 모아 가계·기업·정부에 빌려주거나(은행·사모 신용) 주식·채권 발행을 주선하고(투자은행) '
 '거래·운용·결제를 대신해 주며 이자와 수수료를 받는 사슬입니다. 2026년 3분기에도 주식 거래와 발행이 붐이라 JP모건 순이자이익은 271억 달러(+13%), '
 '골드만삭스 주식 매출은 +72%, 모건스탠리 주식 매출은 58억 달러(+41%)였고 미국 주식형 펀드 유입은 연초 이후 사상 최대 6,360억 달러입니다. '
 '다만 채권 트레이딩은 줄었고(JP모건 -4%, 모건스탠리 -7%), 뱅크오브아메리카는 12억 달러 벌금으로 순이익이 17% 줄었습니다. '
 '빠듯해지는 곳은 차입 쪽입니다: 무디스가 PIK 전환·만기 연장을 넣어 다시 잰 사모 신용 부도율은 5.8%였고, 코어위브 채권 수익률은 16%를 넘었으며 데이터센터 상장은 철회·연기가 이어졌습니다. '
 '은행은 대출을 사모 신용에 넘기고(트루이스트 77억 달러→칼라일), 9월 물가 3.7%로 금리 인상 기대가 커져 보유 채권 평가손실 부담도 남아 있습니다.')

cycle = {
 'stage': 2, 'conf': '중간',
 'why': [
  {'t': '돈은 여전히 자본시장으로 몰립니다. 2026년 1~9월 글로벌 IPO 조달액은 사상 최대 2,875억 달러였고, 미국 주식형 펀드 유입은 연초 이후 사상 최대 6,360억 달러입니다 [사실]',
   'src': [S('EY(스위스 IPO 바로미터)', '2026-10-01', 'ey'), S('로이터(BofA 주간 자금흐름)', '2026-10-16', 'flows')]},
  {'t': '은행·투자은행은 아직 고수익입니다. 모건스탠리 3분기 주식 매출은 58억 달러(+41%), 뱅크오브아메리카 순이자이익은 164억 달러(+8%)였지만 채권 트레이딩은 모건스탠리 -7%로 줄었습니다 [사실]',
   'src': [S('CNBC(모건스탠리 3분기 실적)', '2026-10-14', 'ms'), S('뱅크오브아메리카 3분기 실적(SEC 8-K)', '2026-10-14', 'bac8k')]},
  {'t': '차입 쪽에서 과잉의 대가가 커집니다. 무디스는 PIK 전환·만기 연장을 넣으면 중견기업 사모 대출 부도율이 4%에서 5.8%가 된다고 했고, 코어위브 채권 수익률은 16%를 넘었습니다 [사실]',
   'src': [S('Private Equity Wire(무디스 보고서)', '2026-10-14', 'moodys'), S('로이터', '2026-10-16', 'cw')]},
  {'t': '손해보험은 자본이 남아 상업보험 요율이 8분기 연속 내려 이미 ③ 공급 과잉에 들어섰습니다 [귀납]',
   'src': [S('Insurance Journal(마시 글로벌 보험시장 지수)', '2026-07-23', 'marsh')]},
 ],
 'next': '금리 인상 기대 속에 AI 인프라 채권 약세와 데이터센터 상장 철회가 대형 IPO와 사모 신용 모금으로 번져 발행 창구가 닫히면 ③ 공급 과잉으로 넘어갑니다. 은행이 넘긴 대출의 부실이 펀드 대출·창고 대출로 되돌아오면 ④ 수익 악화가 앞당겨질 수 있습니다 [유추]',
 'watch': ['사모 신용 부도율(Fitch·무디스 PIK 포함)', 'AI 인프라 채권 가격(코어위브·데이터센터 프로젝트채)', '비상장 BDC 환매 요청 비율',
           '미국 은행 순이자마진·평가손실(FDIC)', '글로벌 IPO 조달액과 상장 철회 건수(EY)'],
 'split': [
  {'stage': 1, 'label': '고수익(은행·IB·거래소)', 'nodes': ['banks', 'ib', 'markets']},
  {'stage': 3, 'label': '공급 과잉(사모 신용·손보)', 'nodes': ['pcredit', 'insurance']},
 ],
}

flags = [
 {'nid': 'n-bbg-0049', 't': '재검토 필요: 코어위브 채권 수익률 16%와 데이터센터 프로젝트채 88~92센트는 AI 인프라 차입이 ③ 공급 과잉(빌려준 돈이 남는 국면)으로 가고 있음을 가리키며, 금리 인상 기대에 차입 여건이 빠르게 조여지기 때문입니다 [유추]'},
 {'nid': 'n-tg-0295', 't': '재검토 필요: 일주일 새 데이터센터 관련 상장 철회·연기가 이어진 것은 발행 창구가 일부 닫히는 ③ 공급 과잉 신호를 가리키며, 사상 최대 IPO 흐름과 엇갈리기 때문입니다 [유추]'},
]

insight = {
 'a': [{'t': '은행이 대출을 사모 신용·연기금에 넘기는 일이 잦아졌습니다. 트루이스트는 개인대출 77억 달러를 칼라일에, 자동차대출 55억 달러를 아폴로에 팔았고 ING는 대출 50억 유로 연계 위험이전거래를 PGGM과 맺었습니다 [귀납]',
        'src': [S('블룸버그', '2026-10-16', 'carlyle'), S('블룸버그', '2026-10-13', 'srt')]}],
 'a1': [{'t': '은행은 자본이 덜 드는 수수료 사업(주식 트레이딩·자산관리)에 기대고, 신용 위험은 사모 신용·보험 자본 쪽에 쌓여 다음 부실은 은행 밖에서 먼저 드러날 가능성이 큽니다 [유추]',
         'src': [S('블룸버그', '2026-10-16', 'acap'), S('CNBC(모건스탠리 3분기 실적)', '2026-10-14', 'ms')]}],
 'a2': [{'t': '반대로 사모 신용 부실이 은행의 창고 대출·펀드 대출로 되돌아오면 위험은 다시 은행에 실립니다. 트라이컬러는 활성 대출 7만 건 중 약 2만 9,000건이 창고 대출과 증권화에 이중 담보로 잡힌 것으로 전해졌습니다 [사실]',
         'src': [S('블룸버그', '2026-10-16', 'tricolor')]}],
 'b': [{'t': '투자자 돈이 채권 대신 주식·헤지펀드로 옮겨 갑니다. 2024년 말 이후 MSCI 세계지수는 약 36% 올랐고 FTSE 세계국채 지수는 7% 내렸으며, 세계 헤지펀드 자산은 사상 최대 5조 6,000억 달러입니다 [사실]',
        'src': [S('로이터', '2026-10-13', 'hf')]},
       {'t': '맨그룹 운용자산은 사상 최대 2,709억 달러, 블랙록 3분기 순유입은 2,050억 달러로 운용사로 돈이 계속 들어옵니다 [사실]',
        'src': [S('로이터', '2026-10-16', 'man'), S('로이터', '2026-10-14', 'blk')]}],
 'b1': [{'t': '주식 거래·운용 수수료는 계속 늘고 채권 쪽은 덜 벌 가능성이 큽니다. 모건스탠리 주식 매출은 +41%였지만 채권 트레이딩은 -7%였습니다 [유추]',
         'src': [S('CNBC(모건스탠리 3분기 실적)', '2026-10-14', 'ms')]}],
 'b2': [{'t': '반대로 연준이 10월 28일 금리를 올리고 AI주 투매가 이어지면 주식 유입이 되돌 수 있습니다. 반도체지수는 8거래일 연속 내렸고 BofA는 3~4주 위험 회피를 권했습니다 [유추]',
         'src': [S('로이터(BofA 주간 자금흐름)', '2026-10-16', 'flows'), S('텔레그램 하나증권 중국전략', '2026-10-17', 'semi')]}],
 'c': [{'t': 'AI 인프라 차입에 금이 갔습니다. 코어위브 채권 수익률은 16%를 넘고 부도보험료는 1,000bp를 넘었으며, 데이터센터 관련 상장이 일주일 새 잇달아 철회·연기됐습니다 [사실]',
        'src': [S('로이터', '2026-10-16', 'cw'), S('로이터', '2026-10-15', 'dc')]}],
 'c1': [{'t': '아직 덮을 만큼 크지는 않습니다. 코어위브 빚은 약 500억 달러로 올해 미국 주식형 펀드 유입 6,360억 달러에 견줘 작지만, 블루아울·블랙스톤 관련 데이터센터 채권으로 번지는 중이라 크기보다 번지는 경로가 관건입니다 [유추]',
         'src': [S('로이터', '2026-10-16', 'cw'), S('로이터(BofA 주간 자금흐름)', '2026-10-16', 'flows')]}],
 'd': [{'t': '정치·규제가 은행의 높은 이익을 거둬 가는 흐름으로 볼 수도 있습니다. 이탈리아는 3년간 금융권에서 107억 유로를 걷고, 영국은 은행 추가세율을 3%에서 8%로 되돌리는 안을 검토하며, 스위스는 UBS에 약 160억 달러 추가 자본을 요구합니다 [귀납]',
        'src': [S('로이터', '2026-10-15', 'italy'), S('로이터', '2026-10-16', 'ukbank'), S('로이터', '2026-10-15', 'ubs')]}],
}

gaps = ('웹 검색 누적 17회(이번 3회), 열람 5회 안에서 확인했고 다음은 확인하지 못했습니다. (1) 씨티·웰스파고 3분기 수치는 2차 매체 요약만 봤고, 모건스탠리 수치는 CNBC 검색 요약 기준입니다. '
 '(2) 한국 4대 금융지주 3분기 실적(10월 23~29일 발표 예정), 일본 3대 은행 4~9월 실적(11월), DBS·OCBC 실적(11월 5~6일). '
 '(3) 사모 신용 부도율은 무디스(중견기업 CLO 차입자 607곳, 6월까지 12개월) 5.8%를 2차 매체로 봤고, 피치 8월 6.3%와 직접대출 1~9월 모금 1,291억 달러는 블로그 요약뿐이라 쓰지 않았습니다. '
 '(4) 코어위브 외 데이터센터 상장 철회 건(에어트렁크·퍼머스·SB에너지)은 텔레그램 전언이며 원문을 열지 않았습니다. '
 '(5) 2026년 재보험 갱신 요율, 이사야스 최종 보험 손실, 생명보험·연금 위험 이전 시장 규모. (6) 비자·마스터카드 최근 분기 결제액, 스테이블코인 공급(2차 매체). '
 '(7) 데스크 뉴스로 표시한 내용은 데스크 뉴스 요약 기준이며 원문(로이터·블룸버그)은 열지 않았습니다.')

note = ('뉴스 93건 반영: BofA 벌금·은행 대출의 사모 신용 이전, 코어위브 채권 16%·데이터센터 상장 철회, 주식형 펀드·헤지펀드 자금 사상 최대. '
        '국면 ② 그대로(why 근거 교체), 근거 14줄, 수치 4줄, 재검토 신호 2건, 검색 3회')

out = {'id': 'fin', 'summary': summary, 'state': state, 'industryState': industryState, 'flags': flags,
       'insight': insight, 'cycle': cycle, 'nodeStage': {}, 'gaps': gaps, 'note': note,
       'applied': ids, 'searches': 3, 'fetches': 0}
json.dump(out, open(f'{B}/out/fin.json', 'w'), ensure_ascii=False, indent=1)
print(len(ids), sum(len(v) for v in state.values()))
