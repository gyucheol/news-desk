import json, os
HERE = os.path.dirname(os.path.abspath(__file__))
t1 = json.load(open(os.path.join(HERE, 'tune/t1.json')))
t2 = json.load(open(os.path.join(HERE, 'tune/t2.json')))
t2['housing.s2'] = '{{30년 고정 모기지 금리}}는 {{10월 8일}} {{7.40%}}로 전주 7.28%와 {{1년 전 6.30%}}보다 {{올랐}}습니다 [사실]'

U = {
    'nar': 'https://www.nar.realtor/newsroom/existing-home-sales-increased-1-5-in-september-according-to-nar-report',
    'pmms': 'https://www.globenewswire.com/news-release/2026/10/08/3377537/0/en/mortgage-rates-average-7-40.html',
    'fn': 'https://www.fnnews.com/news/202610081400476102',
    'lennar': 'https://newsroom.lennar.com/2026-09-16-Lennar-Reports-Third-Quarter-2026-Results',
    'nahb': 'https://www.nahb.org/news-and-economics/press-releases/2026/09/builder-sentiment-falls-on-higher-interest-rates-and-costs',
    'gs': 'https://www.greenstreet.com/waiting-for-price-clarity/',
    'yp': 'https://yieldpro.com/2026/10/multifamily-cmbs-delinquency-rate-leads-overall-rate-higher-in-september',
    'mba': 'https://www.mba.org/news-and-research/newsroom/news/2026/02/09/17-percent-of-commercial-and-multifamily-mortgage-balances-to-mature-in-2026',
    'cbre': 'https://www.cbre.com/press-releases/north-american-data-center-demand-continues-to-outpace-supply-despite-record-construction-activity',
    'credaily': 'https://www.credaily.com/briefs/rising-yields-stall-reit-ma-as-buyers-and-sellers-split/',
    'xinhua': 'https://english.news.cn/20260915/bf34999008cd4d42ac9a5beaeec35aea/c.html',
    'caixin': 'https://www.caixinglobal.com/2026-07-23/vanke-wins-new-funding-as-it-completes-extensions-on-2026-public-bonds-102467124.html',
    'molit': 'https://www.molit.go.kr/USR/NEWS/m_71/dtl.jsp?lcmspage=1&id=95091185',
    'nate': 'https://m.news.nate.com/view/20260109n20267',
}
NA = '이며 최근 실적은 {{확인 못 함}}'

def st(d, o, key, u):
    return {'d': d, 'o': o, 't': t2[key], 'u': U[u]}

d = {
    'id': 'realestate', 'name': '부동산', 'short': '부동산', 'icon': '🏢', 'order': 19,
    'asOf': '2026-10-14', 'rev': '2026-10-14',
    'summary': t1['summary'],
    'intro': {
        'what': t2['what'], 'money': t1['money'], 'drivers': t1['drivers'],
        'watch': [
            {'n': '미국 30년 고정 모기지 금리', 'why': '주택 구매 능력, 곧 주택 수요를 가장 먼저 움직입니다', 'where': '프레디맥 PMMS(매주 목요일)'},
            {'n': '기존주택 판매·재고·중위가격', 'why': '매물이 쌓이는지, 가격이 꺾이는지를 보여 줍니다', 'where': '전미부동산중개인협회(NAR) 월간 발표'},
            {'n': 'CMBS 연체율(오피스·멀티패밀리)', 'why': '상업용 부동산 부실이 어느 부문까지 번졌는지 보여 줍니다', 'where': 'Trepp 월간 CMBS 연체율'},
            {'n': '상업용 부동산 가격지수', 'why': '금리 변화가 건물 가격에 반영되는 속도를 봅니다', 'where': '그린스트리트 CPPI(월간)'},
            {'n': '중국 70개 도시 신규주택 가격', 'why': '중국 부동산 바닥 여부와 개발사 부실의 방향을 가늠합니다', 'where': '중국 국가통계국(매월 중순)'},
        ],
        'players': [
            {'n': 'D.R.호튼(D.R. Horton)', 't': 'DHI', 'm': 'NYSE', 'role': '미국 최대 주택 건설사. 미국 신규 주택 공급을 대표합니다'},
            {'n': '프롤로지스(Prologis)', 't': 'PLD', 'm': 'NYSE', 'role': '세계 최대 물류창고 리츠'},
            {'n': '에퀴닉스(Equinix)', 't': 'EQIX', 'm': 'NASDAQ', 'role': '세계 최대 데이터센터 리츠'},
            {'n': '블랙스톤(Blackstone)', 't': 'BX', 'm': 'NYSE', 'role': '사모 부동산 펀드와 부동산 대출을 운용하는 대형 대체투자사'},
            {'n': '선홍카이프로퍼티(Sun Hung Kai Properties)', 't': '0016', 'm': 'HKEX', 'role': '홍콩 최대 개발사'},
            {'n': '차이나반커(China Vanke)', 't': '2202', 'm': 'HKEX', 'role': '중국 대형 개발사. 국유 대주주(선전메트로) 지원으로 채권 만기를 연장하고 있습니다'},
            {'n': '미쓰이부동산(Mitsui Fudosan)', 't': '8801', 'm': 'TSE', 'role': '일본 최대 종합 부동산 회사(오피스·상업시설·주택)'},
            {'n': '현대건설(Hyundai Engineering & Construction)', 't': '000720', 'm': 'KRX', 'role': '한국 대형 건설사(주택·플랜트·인프라)'},
        ],
        'reading': [
            {'news': '모기지 금리 상승 속 주택 판매·건설사 예약 둔화(미국 9월 기존주택 판매, 영국 벨웨이)', 'means': t1['r0']},
            {'news': '대출 만기 차환 난항·대주단의 대출 매각 타진(몰 오브 베를린, 프랑크푸르트 코메르츠방크 타워)', 'means': t1['r1']},
            {'news': '리츠 매각·분할 매각·행동주의 압박(빅옐로, H&R 리츠, 서비스프로퍼티 호텔)', 'means': t1['r2']},
            {'news': '중국·홍콩 개발사 자산 매각·구조조정과 연휴 주택 거래(헝다물업 지분 매각, 뉴월드 사업 이관)', 'means': t1['r3']},
            {'news': '개발사 대규모 투자·토지 매입(인도 브리게이드 40억 달러, 마이애미 윈우드 부지)', 'means': t1['r4']},
        ],
        'terms': [
            {'k': '캡레이트(자본환원율)', 'v': '순임대수익을 건물 가격으로 나눈 비율. 금리가 오르면 대개 따라 오르고, 캡레이트가 오르면 같은 임대료라도 건물 가치가 내려갑니다'},
            {'k': 'CMBS', 'v': '상업용 부동산 담보대출을 묶어 만든 채권. 연체율이 상업용 부동산 부실의 대표 지표입니다'},
            {'k': 'NAV 할인', 'v': '리츠 주가가 보유 부동산의 시장가치에서 부채를 뺀 순자산가치(NAV)보다 낮게 거래되는 정도'},
            {'k': '선임대(Pre-leasing)', 'v': '완공 전에 임차인과 임대 계약을 맺어 두는 것. 비율이 높을수록 공급 과잉 위험이 작습니다'},
            {'k': '차환(Refinancing)', 'v': '만기가 된 대출을 새 대출로 갚는 것. 금리가 오르거나 건물 가치가 떨어지면 어려워집니다'},
            {'k': 'PF(프로젝트 파이낸싱)', 'v': '땅값·공사비를 사업의 미래 분양 수익을 담보로 빌리는 대출. 한국 시행사의 주된 자금 조달 방식입니다'},
        ],
    },
    'nodes': [
        {
            'id': 'develop', 'name': '개발·시행·건설', 'short': '개발·건설',
            'role': t2['develop.role'], 'bottleneck': t2['develop.bottleneck'],
            'stage': 3, 'stageNote': '미국 주택 건설: 가격 인하·인센티브 확대',
            'indicators': [
                {'n': '주택 착공·인허가', 'src': '미 인구조사국(Census) 신규주택 착공, 국토교통부 주택건설실적'},
                {'n': '건설사 체감지수와 가격 인하 비율', 'src': 'NAHB/웰스파고 주택시장지수(HMI)'},
                {'n': '건설사 매출총이익률·인센티브 비율', 'src': '레나·D.R.호튼 분기 실적'},
            ],
            'companies': [
                {'n': 'D.R.호튼(D.R. Horton)', 't': 'DHI', 'm': 'NYSE', 'note': '{{미국 최대 주택 건설사}}' + NA},
                {'n': '레나(Lennar)', 't': 'LEN', 'm': 'NYSE',
                 'note': '3분기 {{신규 주문 2만 879채(-9%)}}, 주택 {{매출총이익률 15.8%}}, 평균 판매가 {{37만 2,000달러}}에 {{인센티브 약 12%}}'},
                {'n': '벨웨이(Bellway)', 't': 'BWY', 'm': 'London Stock Exchange',
                 'note': '{{80% LTV 모기지 금리}}가 {{5%를 넘자}} {{주간 예약}}이 {{5.8% 줄었}}고 {{2027 회계연도 완공 목표}}를 {{9,000~9,400채}}로 {{낮췄}}습니다(10월 13일 데스크 뉴스)'},
                {'n': '브리게이드 엔터프라이즈(Brigade Enterprises)', 't': 'BRIGADE', 'm': 'National Stock Exchange of India',
                 'note': '{{3년간 40억 달러 넘게}} {{개발 사업에 투자}}하겠다고 밝혔습니다(10월 8일 데스크 뉴스)'},
                {'n': '현대건설(Hyundai Engineering & Construction)', 't': '000720', 'm': 'KRX', 'note': '{{한국 대형 건설사}}' + NA},
            ],
            'links': [
                {'to': 'macro/rates', 'why': '모기지·PF 금리가 분양 수요와 개발 자금 비용을 함께 정합니다'},
            ],
            'state': [
                st('2026-09-16', 'NAHB(전미주택건설협회) 보도자료', 'develop.s1', 'nahb'),
                st('2026-09-16', '레나 3분기 실적 보도자료', 'develop.s2', 'lennar'),
            ],
        },
        {
            'id': 'housing', 'name': '주택 매매·임대·모기지', 'short': '주택',
            'role': t2['housing.role'], 'bottleneck': t2['housing.bottleneck'],
            'stage': 3, 'stageNote': '미국 재고 증가(서울은 상승 지속)',
            'indicators': [
                {'n': '30년 고정 모기지 금리', 'src': '프레디맥 PMMS(주간)'},
                {'n': '기존주택 판매·재고·중위가격', 'src': 'NAR 월간 기존주택 판매'},
                {'n': '서울 아파트 주간 매매·전세 가격', 'src': '한국부동산원 주간 아파트 가격 동향'},
            ],
            'companies': [
                {'n': '프레디맥(Freddie Mac)', 't': 'FMCC', 'm': 'OTC',
                 'note': '{{미국 모기지를 사들여 증권화하는 정부 후원 기업}}으로 {{주간 모기지 금리 조사(PMMS)}}를 {{발표}}합니다'},
                {'n': '로켓컴퍼니즈(Rocket Companies)', 't': 'RKT', 'm': 'NYSE', 'note': '{{미국 대형 모기지 대출사}}' + NA},
                {'n': '질로우그룹(Zillow Group)', 't': 'Z', 'm': 'NASDAQ', 'note': '{{미국 대형 부동산 정보·중개 플랫폼}}' + NA},
                {'n': '유니슨(Unison)', 't': '', 'm': 'private',
                 'note': '{{주택 지분을 사들이는}} {{대안 주택금융 업체}}로 {{최대 5억 달러 미국 상장}}을 {{준비}}합니다(10월 13일 데스크 뉴스)'},
            ],
            'links': [
                {'to': 'macro/rates', 'why': '장기 국채 금리가 모기지 금리를 끌어올려 주택 구매 수요를 줄입니다'},
                {'to': 'macro/growth', 'why': '고용과 소득이 주택 구매·임대 수요를 받칩니다'},
            ],
            'state': [
                st('2026-10-13', '전미부동산중개인협회(NAR)', 'housing.s1', 'nar'),
                st('2026-10-08', '프레디맥 PMMS 보도자료', 'housing.s2', 'pmms'),
                st('2026-10-08', '파이낸셜뉴스(한국부동산원 주간 통계)', 'housing.s3', 'fn'),
            ],
        },
        {
            'id': 'commercial', 'name': '상업용 부동산(오피스·리테일·물류·호텔)', 'short': '상업용',
            'role': t2['commercial.role'], 'bottleneck': t2['commercial.bottleneck'],
            'stage': 6, 'stageNote': '오피스 공실 정점 통과, 부실 정리 중',
            'indicators': [
                {'n': '오피스 공실률·순흡수', 'src': '뉴마크·CBRE·쿠시먼앤웨이크필드 분기 보고서'},
                {'n': '상업용 부동산 가격지수', 'src': '그린스트리트 CPPI, MSCI RCA CPPI'},
                {'n': '부문별 CMBS 연체율', 'src': 'Trepp 월간 보고서'},
            ],
            'companies': [
                {'n': '프롤로지스(Prologis)', 't': 'PLD', 'm': 'NYSE', 'note': '{{세계 최대 물류창고 리츠}}' + NA},
                {'n': '보네이도(Vornado Realty Trust)', 't': 'VNO', 'm': 'NYSE',
                 'note': '{{뉴욕 오피스 중심 리츠}}로 {{순자산가치 대비 30% 이상 할인}}된 대형 리츠에 {{꼽혔}}습니다(호야캐피털, CRE Daily 인용)'},
                {'n': '킬로이 리얼티(Kilroy Realty)', 't': 'KRC', 'm': 'NYSE',
                 'note': '{{미국 서부 오피스 리츠}}로 {{30% 이상 할인}}된 대형 리츠에 {{꼽혔}}습니다(호야캐피털, CRE Daily 인용)'},
                {'n': '미쓰이부동산(Mitsui Fudosan)', 't': '8801', 'm': 'TSE', 'note': '{{일본 최대 종합 부동산 회사}}(오피스·상업시설)' + NA},
            ],
            'links': [
                {'to': 'macro/rates', 'why': '국채 금리가 캡레이트와 건물 가치를 움직입니다'},
                {'to': 'macro/growth', 'why': '고용과 기업 실적이 오피스·상가 임차 수요를 정합니다'},
            ],
            'state': [
                st('2026-10-06', '그린스트리트 보도자료', 'commercial.s1', 'gs'),
                st('2026-10-04', 'Yield PRO(Trepp 집계 인용)', 'commercial.s2', 'yp'),
            ],
        },
        {
            'id': 'datacenter', 'name': '데이터센터', 'short': '데이터센터',
            'role': t2['datacenter.role'], 'bottleneck': t2['datacenter.bottleneck'],
            'stage': 2, 'stageNote': '착공 사상 최대, 공실 1.4%',
            'indicators': [
                {'n': '주요 시장 공실률·선임대 비율', 'src': 'CBRE North America Data Center Trends(반기)'},
                {'n': '건설 중 용량(MW)과 임대료', 'src': 'CBRE·JLL 데이터센터 보고서'},
                {'n': '빅테크 설비투자', 'src': '마이크로소프트·알파벳·아마존·메타 분기 실적'},
            ],
            'companies': [
                {'n': '에퀴닉스(Equinix)', 't': 'EQIX', 'm': 'NASDAQ', 'note': '{{세계 최대 데이터센터 리츠}}' + NA},
                {'n': '디지털 리얼티(Digital Realty Trust)', 't': 'DLR', 'm': 'NYSE', 'note': '{{대형 데이터센터 리츠}}' + NA},
                {'n': '블랙스톤(Blackstone)', 't': 'BX', 'm': 'NYSE',
                 'note': '{{QTS}}·{{에어트렁크(AirTrunk)}} 등 {{데이터센터 사업자}}를 {{인수}}한 {{대형 사모 부동산 투자자}}입니다'},
            ],
            'links': [
                {'to': 'power/demand', 'why': '데이터센터 착공이 전력 수요와 계통 연결 대기열을 늘리고, 전력 연결이 늦으면 데이터센터 공급도 늦어집니다'},
                {'to': 'macro/rates', 'why': '장기 임대 자산이라 금리가 개발 자금 비용과 자산 가치를 좌우합니다'},
            ],
            'state': [
                st('2026-08-27', 'CBRE 보도자료(북미 데이터센터 동향 2026년 상반기)', 'datacenter.s1', 'cbre'),
                st('2026-08-27', 'CBRE 보도자료(북미 데이터센터 동향 2026년 상반기)', 'datacenter.s2', 'cbre'),
            ],
        },
        {
            'id': 'reits', 'name': '리츠·상장 부동산', 'short': '리츠',
            'role': t2['reits.role'], 'bottleneck': t2['reits.bottleneck'],
            'stage': 6, 'stageNote': '합병·인수로 통합 진행',
            'indicators': [
                {'n': '리츠 주가의 순자산가치(NAV) 대비 할인·할증', 'src': '그린스트리트·호야캐피털·S&P Global'},
                {'n': '리츠 인수합병·비상장 전환 건수', 'src': 'S&P Global Market Intelligence, Nareit'},
                {'n': '리츠 배당수익률과 10년 국채 금리 차이', 'src': 'Nareit, 미 재무부'},
            ],
            'companies': [
                {'n': '퍼블릭스토리지(Public Storage)', 't': 'PSA', 'm': 'NYSE',
                 'note': '{{내셔널스토리지어필리에이츠}}를 {{105억 달러 주식 교환}}으로 {{인수}}하기로 {{합의}}했습니다(CRE Daily)'},
                {'n': '웰타워(Welltower)', 't': 'WELL', 'm': 'NYSE',
                 'note': '{{시니어 주거·헬스케어 리츠}}로 {{순자산가치 대비 약 97% 할증}}에 {{거래}}됩니다(호야캐피털, CRE Daily 인용)'},
                {'n': '빅옐로(Big Yellow Group)', 't': 'BYG', 'm': 'London Stock Exchange',
                 'note': '{{영국 셀프스토리지 리츠}}로 {{행동주의 앵코라}}가 {{매각 검토}}를 {{요구}}했습니다(순자산 대비 약 40% 할인, 10월 14일 데스크 뉴스)'},
                {'n': '서비스프로퍼티트러스트(Service Properties Trust)', 't': 'SVC', 'm': 'NASDAQ',
                 'note': '{{TKO}}가 {{호텔 포트폴리오 전체}}를 {{20억 달러 현금}}에 {{사겠다고 제안}}했습니다(10월 10일 데스크 뉴스)'},
                {'n': 'H&R 리츠(H&R REIT)', 't': 'HR.UN', 'm': 'Toronto Stock Exchange',
                 'note': '{{블랙스톤 등이 참여한 분할 인수안}}에 {{RBC자산운용·밀폰드}}가 {{반대}}해 {{11월 13일 주총}} {{통과}}가 {{불투명}}합니다(10월 8일 데스크 뉴스)'},
            ],
            'links': [
                {'to': 'macro/rates', 'why': '배당수익률이 국채 금리와 경쟁해 금리가 오르면 리츠 주가와 증자 여력이 줄어듭니다'},
                {'to': 'macro/liquidity', 'why': '리츠 자금 흐름과 사모펀드의 인수 자금이 할인 해소 속도를 정합니다'},
            ],
            'state': [
                st('2026-10-07', 'CRE Daily(호야캐피털 인용)', 'reits.s1', 'credaily'),
                st('2026-10-07', 'CRE Daily', 'reits.s2', 'credaily'),
            ],
        },
        {
            'id': 'finance', 'name': '부동산 금융', 'short': '부동산금융',
            'role': t2['finance.role'], 'bottleneck': t2['finance.bottleneck'],
            'stage': 6, 'stageNote': '만기 벽·연체율 상승, 대출 매각',
            'indicators': [
                {'n': 'CMBS 연체율(전체·오피스·멀티패밀리)', 'src': 'Trepp 월간 보고서'},
                {'n': '상업용 부동산 대출 만기 규모', 'src': '미국 모기지은행협회(MBA) 연간 만기 조사'},
                {'n': '은행 상업용 부동산 대출 연체·무수익 비율', 'src': 'FDIC Quarterly Banking Profile'},
            ],
            'companies': [
                {'n': '스타우드 프로퍼티 트러스트(Starwood Property Trust)', 't': 'STWD', 'm': 'NYSE', 'note': '{{대형 상업용 부동산 대출 리츠}}' + NA},
                {'n': '블랙스톤 모기지 트러스트(Blackstone Mortgage Trust)', 't': 'BXMT', 'm': 'NYSE', 'note': '{{상업용 부동산 대출 리츠}}' + NA},
                {'n': '웰스파고(Wells Fargo)', 't': 'WFC', 'm': 'NYSE', 'note': '{{상업용 부동산 대출이 많은}} {{미국 대형 은행}}' + NA},
                {'n': '우니크레디트(UniCredit)', 't': 'UCG', 'm': 'Euronext Milan',
                 'note': '{{몰 오브 베를린}} {{대출 차환}}을 {{주도}}하는 {{협상}}이 {{막바지}}입니다(10월 12일 데스크 뉴스)'},
                {'n': '삼성SRA자산운용', 't': '', 'm': 'private',
                 'note': '{{프랑크푸르트 코메르츠방크 타워}} 소유주로 {{3억 6,000만 유로 차환}}과 {{리모델링 자금}} {{조달}}이 {{더딥니다}}(10월 8일 데스크 뉴스)'},
            ],
            'links': [
                {'to': 'fin/banks', 'why': '은행이 상업용 부동산 대출과 CMBS의 큰 보유자라 차환 실패가 은행 대손비용으로 이어집니다'},
                {'to': 'fin/pcredit', 'why': '은행이 줄인 부동산 대출을 사모 신용 펀드가 메우고, 부동산 부실이 사모 신용 부도율을 끌어올립니다'},
                {'to': 'macro/liquidity', 'why': '신용 스프레드와 채권시장 자금이 CMBS 발행과 차환 가능성을 정합니다'},
            ],
            'state': [
                st('2026-10-04', 'Yield PRO(Trepp 집계 인용)', 'finance.s1', 'yp'),
                st('2026-02-09', '미국 모기지은행협회(MBA)', 'finance.s2', 'mba'),
            ],
        },
        {
            'id': 'china', 'name': '중국·홍콩 개발사', 'short': '중국개발사',
            'role': t2['china.role'], 'bottleneck': t2['china.bottleneck'],
            'stage': 6, 'stageNote': '개발사 퇴출·구조조정(바닥 미확인)',
            'indicators': [
                {'n': '70개 도시 신규·기존주택 가격', 'src': '중국 국가통계국(매월 중순)'},
                {'n': '상위 100개 개발사 월간 판매액', 'src': 'CRIC(커얼루이)'},
                {'n': '미분양 면적·토지 판매 수입', 'src': '중국 국가통계국·재정부'},
            ],
            'companies': [
                {'n': '차이나반커(China Vanke)', 't': '2202', 'm': 'HKEX',
                 'note': '{{선전메트로}}에서 올해 {{다섯 번째 지원}}(누적 약 45억 위안)을 받아 {{2026년 공모채}}를 {{모두 연장}}했습니다(차이신)'},
                {'n': '헝다물업(Evergrande Property Services)', 't': '6666', 'm': 'HKEX',
                 'note': '{{사모펀드 PAG}}가 {{헝다 청산인}}과 {{지배지분 인수}}를 {{독점 협상}} 중입니다(10월 9일 데스크 뉴스)'},
                {'n': '뉴월드개발(New World Development)', 't': '0017', 'm': 'HKEX',
                 'note': '{{홍콩 공항청}}이 {{11 스카이즈 사업(180억 홍콩달러)}}을 {{넘겨받는}} {{구제안}}으로 {{2029년 말까지}} {{자본구조 조정 시간}}을 {{벌었}}습니다(10월 13일 데스크 뉴스)'},
                {'n': '선홍카이프로퍼티(Sun Hung Kai Properties)', 't': '0016', 'm': 'HKEX', 'note': '{{홍콩 최대 개발사}}' + NA},
                {'n': '중국해외발전(China Overseas Land & Investment)', 't': '0688', 'm': 'HKEX', 'note': '{{국유 대형 개발사}}' + NA},
            ],
            'links': [
                {'to': 'macro/growth', 'why': '중국 부동산 투자 감소가 중국 성장과 철강·원자재 수요를 끌어내립니다'},
            ],
            'state': [
                st('2026-09-15', '신화통신(국가통계국 발표)', 'china.s1', 'xinhua'),
                st('2026-07-23', '차이신 글로벌', 'china.s2', 'caixin'),
            ],
        },
        {
            'id': 'policy', 'name': '부동산 정책(금리·세제·공급)', 'short': '정책',
            'role': t2['policy.role'], 'bottleneck': t2['policy.bottleneck'],
            'indicators': [
                {'n': '기준금리와 모기지 금리', 'src': '연준·한국은행 통화정책 결정, 프레디맥 PMMS'},
                {'n': '대출 규제(LTV·DSR)와 가계대출 증가액', 'src': '금융위원회·한국은행 가계대출 동향'},
                {'n': '주택 공급 계획과 착공 실적', 'src': '국토교통부 발표, 미 인구조사국'},
            ],
            'companies': [
                {'n': '한국토지주택공사(LH)', 't': '', 'm': 'private',
                 'note': '{{9·7 대책}}에서 {{공공택지 주택사업 직접 시행}}을 {{맡았}}습니다(국토교통부)'},
                {'n': '패니메이(Fannie Mae)', 't': 'FNMA', 'm': 'OTC', 'note': '{{미국 정부 후원 모기지 기관}}이며 최근 정책 변화는 {{확인 못 함}}'},
            ],
            'links': [
                {'to': 'macro/rates', 'why': '중앙은행 금리와 국채 금리가 모기지·PF 금리를 거쳐 주택 수요를 움직입니다'},
            ],
            'state': [
                st('2025-09-07', '국토교통부(9·7 주택공급 확대방안)', 'policy.s1', 'molit'),
                st('2026-01-09', '네이트 뉴스(2026 성장전략 보도)', 'policy.s2', 'nate'),
            ],
        },
    ],
    'cycle': {
        'stage': 6, 'conf': '낮음', 'rev': '2026-10-14',
        'why': [
            {'t': t2['why1'], 'src': [{'o': 'CRE Daily', 'd': '2026-10-07', 'u': U['credaily']}]},
            {'t': t2['why2'], 'src': [{'o': 'Yield PRO(Trepp 집계 인용)', 'd': '2026-10-04', 'u': U['yp']},
                                      {'o': '미국 모기지은행협회(MBA)', 'd': '2026-02-09', 'u': U['mba']}]},
            {'t': t2['why3'], 'src': [{'o': '그린스트리트 보도자료', 'd': '2026-10-06', 'u': U['gs']},
                                      {'o': 'CRE Daily', 'd': '2026-10-07', 'u': U['credaily']}]},
            {'t': t2['why4'], 'src': [{'o': 'CBRE 보도자료', 'd': '2026-08-27', 'u': U['cbre']},
                                      {'o': '전미부동산중개인협회(NAR)', 'd': '2026-10-13', 'u': U['nar']},
                                      {'o': 'NAHB(전미주택건설협회) 보도자료', 'd': '2026-09-16', 'u': U['nahb']}]},
        ],
        'next': t2['next'],
        'watch': ['CMBS 연체율(Trepp)', '미 30년 모기지 금리(Freddie Mac)', '기존주택 재고·판매(NAR)', '리츠 NAV 할인율', '중국 70개 도시 신규주택 가격'],
        'split': [
            {'stage': 2, 'label': '증설(데이터센터)', 'nodes': ['datacenter']},
            {'stage': 3, 'label': '공급 과잉(미국 주택)', 'nodes': ['develop', 'housing']},
            {'stage': 6, 'label': '부실 정리·통합(오피스·리츠·금융·중국)', 'nodes': ['commercial', 'reits', 'finance', 'china']},
        ],
    },
    'industryState': [
        {'d': '2026-10-13', 'kind': 'demand', 'o': '전미부동산중개인협회(NAR)',
         't': '미국 9월 기존주택 판매는 연율 399만 채(전월 대비 +1.5%, 전년 대비 -2.2%)였고 재고는 160만 채로 2019년 11월 이후 최대, 중위가격은 41만 7,500달러(+1.3%)였습니다 [사실]', 'u': U['nar']},
        {'d': '2026-10-08', 'kind': 'price', 'o': '프레디맥 PMMS 보도자료',
         't': '미국 30년 고정 모기지 금리는 10월 8일 7.40%로 전주(7.28%)와 1년 전(6.30%)보다 높았습니다 [사실]', 'u': U['pmms']},
        {'d': '2026-08-27', 'kind': 'capex', 'o': 'CBRE 보도자료',
         't': '북미 주요 시장 데이터센터 공실률은 2026년 상반기 1.4%였고 건설 중 용량은 7,481MW(+24.8%)로 사상 최대이며 80% 넘게 선임대됐습니다 [사실]', 'u': U['cbre']},
        {'d': '2026-10-06', 'kind': 'price', 'o': '그린스트리트 보도자료',
         't': '미국 상업용 부동산 가격지수(CPPI)는 9월 0.1% 내렸고 1년 상승률은 4.7%였습니다 [사실]', 'u': U['gs']},
        {'d': '2026-09-15', 'kind': 'price', 'o': '신화통신(국가통계국 발표)',
         't': '중국 70개 도시 중 8월 신규주택 가격이 전월보다 오르거나 보합인 곳은 21곳이었고 1선 도시 신규주택 가격은 전년보다 0.9% 낮았습니다 [사실]', 'u': U['xinhua']},
    ],
    'insight': {}, 'flows': [],
    'gaps': ('웹 검색 14회, 열람 5회(1회는 접속 차단) 안에서 확인했고 다음은 확인하지 못했습니다. '
             '(1) 미국 3분기 전국 오피스 공실률과 오피스 착공·용도 전환·철거 물량. 뉴마크 2분기 말 19.9%(정점 20.5%)는 검색 요약 기준이며 원문은 접속이 막혀 열지 못했습니다. '
             '(2) 미국 8월 주택 착공(2차 자료만 있어 쓰지 않음)과 10월 NAHB 지수(10월 19일 발표 예정). '
             '(3) 2026년 하반기 한국 대출 규제·공급 대책 발표, 한국 PF 부실 현황과 건설사 실적. 9·7 대책 페이지의 게시일은 대책 이름(9월 7일) 기준으로 적었습니다. '
             '(4) 중국 9월 70개 도시 가격(10월 중순 발표)과 상위 100개 개발사 9월 판매(CRIC), 비구이위안 등 다른 개발사의 구조조정 현황. '
             '(5) 사모 부동산 펀드(BREIT 등)의 환매·수익률, 유럽·일본 상업용 부동산 가격, 리츠 3분기 실적. '
             '(6) 리츠 평균 할인 약 10%는 호야캐피털 수치를 인용한 CRE Daily 기준이며, S&P Global의 1분기 말 중간 할인 19.3%는 게재일을 확인 못 해 쓰지 않았습니다. '
             '(7) 데이터센터 상장사(에퀴닉스·디지털 리얼티) 실적과 빅테크 설비투자 수치. '
             '(8) 회사 메모에 데스크 뉴스로 표시한 내용은 데스크 뉴스 목록의 요약 기준이며 원문(블룸버그·로이터)은 열지 않았습니다.'),
    'history': [{'rev': '2026-10-14', 'note': '새 산업 페이지 첫 작성: 노드 8개(개발·건설, 주택, 상업용, 데이터센터, 리츠, 부동산 금융, 중국·홍콩 개발사, 정책), 국면 ⑥ 공급 파괴·통합(확신도 낮음; 데이터센터 ②, 미국 주택 ③), 부동산 금융 노드를 fin/banks·fin/pcredit과 연결, 웹 검색 14회·열람 5회'}],
}

out = '/home/user/news-desk/data/industry-2026-10-14/out/realestate.json'
with open(out, 'w', encoding='utf-8') as f:
    json.dump(d, f, ensure_ascii=False, indent=1)
print('wrote', out)
