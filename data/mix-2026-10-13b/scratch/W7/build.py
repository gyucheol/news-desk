import json, re

def I(t, o, d, u, s=None):
    x = {"t": t, "o": o, "d": d, "u": u}
    if s is not None:
        x["s"] = s
    return x

TR = "텔레그램 트릴리온"
HN = "텔레그램 하나증권 중국전략"
PO = "텔레그램 Polaristimes"
R = "로이터"
B = "블룸버그"

items = []

items.append({"cid": "C006", "attachTo": "n-bbg-0077",
 "title": "{{실물 브렌트}} 고공행진·세계 재고 바닥…中 연료 수출 재개에도 운송비 병목",
 "one": "{{OPEC}}이 올해 수요 증가 전망을 하루 40만 배럴로 낮췄지만, 세계 원유 재고가 2017년 이후 저점에 근접하고 {{VLCC 부족}}으로 운송비가 뛰면서 {{실물 브렌트}}가 선물을 크게 웃돌아 {{정유사 가동률}}이 낮아질 수 있다",
 "facts": [
  "무엇이: 골드만삭스는 걸프 원유 수출이 회복됐는데도 실물(데이티드) 브렌트가 배럴당 120달러 안팎으로 선물을 크게 웃돈다고 분석했고, 9월 브렌트 위험 프리미엄은 배럴당 22달러로 기록상 두 번째로 높았습니다 [사실]",
  "재고: 골드만은 세계 가시적 재고가 2017년 이후 저점에 근접했고 3월 이후 약 6억 6,000만 배럴 줄었다고 봤으며, 비톨은 호르무즈 운송이 끊기면 200달러도 가능하다고 했습니다 [채널]",
  "운송: JP모건은 9월 호르무즈 수송량이 하루 1,200만 배럴로 늘어 VLCC 923척 중 766척이 운항 중이고 이란 관련 124척은 제재로 쓸 수 없어, 운송비가 정유사 감당 범위를 넘어 가동률 감축이 나올 수 있다고 경고했습니다 [채널]",
  "중국: 중국이 연휴 뒤 10월 휘발유·경유·항공유 수출을 합계 약 370만 톤 규모로 승인했습니다 [사실]",
  "수요: OPEC은 10월 12일 2026년 원유 수요 증가 전망을 연초 하루 140만 배럴에서 40만 배럴로 낮췄습니다 [사실]"],
 "basis": "partial",
 "check": "골드만의 9월 위험 프리미엄 22달러·실물 브렌트의 선물 대비 큰 괴리, 중국 10월 연료 수출 약 370만 톤은 검색 결과 요약으로 확인. 실물 브렌트 130·150달러 수준, 중국행 VLCC 96척, JP모건 VLCC 수치는 확인 못 함",
 "src": [{"o": "investingLive", "d": "2026-10-10", "u": "https://investinglive.com/commodities/goldman-gulf-oil-exports-back-at-22-23-mb-d-but-dated-brent-stays-very-high/"},
         {"o": "ChemAnalyst", "d": "2026-10-09", "u": "https://www.chemanalyst.com/NewsAndDeals/NewsDetails/china-to-resume-october-fuel-exports-easing-global-diesel-44919"}],
 "inds": ["macro"], "nodes": ["macro/commodity", "macro/geo"],
 "added": "이번 텔레그램 8건·로이터 1건으로 {{골드만 위험 프리미엄 22달러}}, {{VLCC 부족에 따른 운송비 급등}}과 {{중국 연료 수출 370만 톤}} 재개가 추가됐다",
 "items": [
  I("골드만 '중동 공급 회복에도 낮은 재고·위험 프리미엄이 유가 지지'", HN, "2026-10-09", "https://t.me/HANAchina/70139",
    "{{골드만삭스}}가 페르시아만 수출 회복에도 세계 재고가 2017년 이후 저점에 가깝고 위험 프리미엄이 {{배럴당 22달러}}라고 분석하면서, 유가 하락이 제한될 수 있다"),
  I("중국, 10월 연료 수출 약 370만 톤 규모로 재개", TR, "2026-10-10", "https://t.me/Trillion_labs/10234",
    "{{중국}}이 10월 연료 수출을 9월보다 약 70만 톤 적은 {{370만 톤}} 규모로 재개하면서, 지금 크랙으로는 정제마진이 남지 않아 크랙이 올라야 한다는 시각이 나온다"),
  I("비OECD 육상 원유 재고 급감, 전략비축유 방출 여력도 한계", TR, "2026-10-10", "https://t.me/Trillion_labs/10253",
    "{{비OECD 국가 육상 원유 재고}}가 빠르게 줄고 각국 전략비축유가 더 풀기 어려운 수준에 이르면서, {{공급 완충 여력}}이 바닥나고 있다"),
  I("현물 브렌트 배럴당 130달러 넘어 고공 유지", TR, "2026-10-10", "https://t.me/Trillion_labs/10255",
    "{{현물 브렌트}}가 배럴당 {{130달러}}를 넘은 뒤 높은 수준을 이어가면서, 실물 원유 조달 비용이 계속 높게 유지되고 있다"),
  I("JP모건 '4월이 두 번 왔다'…VLCC 부족에 운송비 급등, 정유 감산 경고", TR, "2026-10-11", "https://t.me/Trillion_labs/10309",
    "{{JP모건}}이 호르무즈 수송 급증과 제재로 묶인 124척 탓에 {{VLCC}}가 모자라 운송비가 치솟는다고 분석하면서, 정유사들이 가동률을 낮출 수 있다고 경고했다"),
  I("중국행 초대형 유조선 약 96척, 미·이란 전쟁 이후 최대 규모", HN, "2026-10-11", "https://t.me/HANAchina/70199",
    "{{중국으로 향하는 VLCC}}가 약 {{96척}}으로 3주 연속 늘어 전쟁 이후 최대가 되면서, 중국 원유 수입 회복 여부가 유가를 좌우할 전망이다"),
  I("골드만 '세계 석유 재고 한계, 위험 프리미엄 역사적 고점 근접'", HN, "2026-10-11", "https://t.me/HANAchina/70207",
    "{{골드만삭스}}가 3월 이후 세계 석유 재고가 약 {{6억 6,000만 배럴}} 줄었다고 분석하면서, 시장의 충격 흡수력이 약해져 유가 상승 위험이 커졌다고 경고했다"),
  I("데이티드 브렌트 150달러, 4월 고점보다 비싸져", TR, "2026-10-13", "https://t.me/Trillion_labs/10391",
    "{{데이티드 브렌트}}가 배럴당 {{150달러}}로 4월보다 비싸지면서, 실물 원유 가격이 봄철 공급 위기 때 수준을 넘어선 것으로 전해졌다"),
  I("러시아 경유 공급 전망이 걸프 공급 위험 상쇄하며 유가 소폭 하락", R, "2026-10-13", "https://www.reuters.com/business/energy/oil-ticks-lower-russia-diesel-supply-prospects-counter-gulf-supply-risks-2026-10-13/",
    "13일 {{러시아산 경유}}의 공급 전망이 걸프 지역 공급 위험 우려를 상쇄하면서 {{국제 유가}}가 소폭 하락했다 (제목 기준)"),
 ]})

items.append({"cid": "C014", "attachTo": "n-tg-0187",
 "title": "이사야스發 美멕시코만 원유 {{최대 72% 중단}}…상륙 뒤 30%로 낮아져",
 "one": "{{허리케인 이사야스}}가 3등급으로 커지며 미 멕시코만 원유 생산의 {{약 72%}}와 가스 59%를 멈춰 세운 뒤 상륙 이후 중단 비율이 약 30%로 낮아졌지만, {{누적 손실 583만 배럴}}과 연안 정전 피해로 미 석유 공급 공백이 이어지고 있다",
 "facts": [
  "무엇이: 미 멕시코만 원유 생산 중단 비율이 10월 9일 약 71.5%까지 올랐고, 가스 생산은 약 59%가 멈췄습니다 [사실]",
  "대피: 유인 생산 플랫폼 371곳 가운데 129곳(35%)에서 인력이 대피했습니다 [사실]",
  "가격: 원유 중단량이 하루 146만 배럴에 이르면서 마스 원유가 WTI 대비 할인에서 배럴당 약 3달러 프리미엄으로 돌아섰습니다 [채널]",
  "이후: 상륙 뒤 원유 중단 비율은 약 30%로 낮아졌다는 보도가 나왔고, 누적 원유 생산 손실은 583만 배럴입니다 [채널]",
  "육상: 이사야스는 플로리다 데스틴 인근에 상륙해 플로리다·앨라배마에 대규모 정전과 인터넷 장애를 일으켰습니다 [채널]"],
 "basis": "verified",
 "check": "BOE Report·Marine Insight 검색 결과 요약으로 원유 71.5%·가스 59% 중단, 플랫폼 129곳 대피 확인. 하루 146만 배럴, 마스 원유 프리미엄, 상륙 뒤 정전은 확인 못 함",
 "src": [{"o": "BOE Report", "d": "2026-10-09", "u": "https://boereport.com/2026/10/09/about-71-5-of-us-gulf-oil-production-shut-in-ahead-of-hurricane-isaias/"},
         {"o": "Marine Insight", "d": "2026-10-10", "u": "https://marineinsight.com/129-gulf-of-mexico-oil-and-gas-platforms-evacuated-as-hurricane-isaias-forces-production-offline"}],
 "inds": ["macro", "gas"], "nodes": ["macro/commodity", "gas/upstream"],
 "added": "이번 텔레그램 4건·로이터 2건으로 원유 중단이 {{71.5%}}까지 늘었던 정점과 {{마스 원유 프리미엄}} 전환, {{플로리다·앨라배마 정전}}이 추가됐다",
 "items": [
  I("이사야스에 멕시코만 원유 하루 130만 배럴 중단, 생산의 3분의 2", TR, "2026-10-10", "https://t.me/Trillion_labs/10241",
    "{{해상 시추 시설}}이 원유 하루 {{130만 배럴}}과 가스 하루 11억 입방피트 생산을 멈추면서, 육상 홍수와 정유 시설 정전 피해가 실제 위험으로 꼽힌다"),
  I("이사야스 상륙 임박에 미 멕시코만 생산업체들 원유·가스 추가 중단", R, "2026-10-10", "https://www.reuters.com/business/energy/us-gulf-producers-shut-more-oil-gas-isaias-nears-landfall-2026-10-09/",
    "{{미 멕시코만 생산업체}}들이 이사야스 상륙을 앞두고 원유·가스 생산을 추가로 멈추면서, 원유 중단 비율이 {{약 72%}}까지 올라갔다"),
  I("미 멕시코만 원유 71.51%·가스 58.84% 생산 중단", TR, "2026-10-10", "https://t.me/Trillion_labs/10251",
    "미 멕시코만 {{원유 생산 71.51%}}와 가스 58.84%가 멈추면서, 1등급 예상을 깨고 {{3등급}}으로 커진 허리케인이 에너지 공급 불안을 키우고 있다"),
  I("대형 허리케인 미 걸프 연안 접근, 창문 막고 대피 행렬", R, "2026-10-10", "https://www.reuters.com/business/environment/boarded-windows-evacuations-major-hurricane-nears-us-gulf-coast-2026-10-09/",
    "{{대형 허리케인}}이 미 {{걸프 연안}}으로 다가오면서 연안 주민들이 창문을 판자로 막고 서둘러 대피에 나섰다 (제목 기준)"),
  I("이사야스 3등급 격상, 멕시코만 원유 72% 중단…마스 원유 프리미엄 전환", HN, "2026-10-10", "https://t.me/HANAchina/70154",
    "{{이사야스}}가 3등급으로 격상돼 하루 146만 배럴 원유 생산이 멈추면서, {{마스 원유}}가 WTI 대비 할인에서 약 3달러 프리미엄으로 돌아섰다"),
  I("이사야스, 플로리다·앨라배마에 대규모 정전·인터넷 장애", "텔레그램 미국 주식 인사이더", "2026-10-10", "https://t.me/insidertracking/65900",
    "{{이사야스}}가 플로리다 데스틴 인근에 상륙해 기반시설을 파손하면서, 플로리다·앨라배마 전역에 {{정전과 인터넷 장애}}가 번졌다"),
 ]})

items.append({"cid": "C031", "attachTo": "n-tg-0125",
 "title": "RBI, 루피 방어 이어 {{유동성 흡수}}…국채 매각·지준 강화에 인도 채권 이중고",
 "one": "{{인도중앙은행}}이 정유사 달러 수요를 떠맡고 파생상품 한도를 조인 데 이어 {{2,500억 루피}} 국채 매각과 일일 지준 유지 비율 상향으로 유동성을 거둬들이면서, 루피는 아시아 최대폭으로 올랐지만 {{인도 채권}}은 물가와 함께 이중 압박을 받고 있다",
 "facts": [
  "무엇이: RBI가 10월 13일 2,500억 루피 규모 국채를 공개시장에서 팔고, 10월 16일 시작 기간부터 은행이 법정 지급준비금의 최소 99%를 매일 유지하도록 했습니다(기존 90%) [사실]",
  "배경: RBI는 10월 7일 기준금리를 5.50%로 0.25%p 올렸고, 은행권 잉여 유동성은 9월 7조 7,800억 루피에서 10월 8일 3조 8,800억 루피로 줄었습니다 [사실]",
  "루피 방어: RBI가 국영 석유기업의 하루 2억 5,000만 달러 넘는 달러 매입 수요를 떠맡고, 실수요 없이 보유할 수 있는 외환파생상품 한도를 1억 달러에서 500만 달러로 낮췄습니다 [채널]",
  "물가: 9월 소비자물가 상승률은 5.54%로 2024년 말 이후 최고입니다 [채널]",
  "시장: 루피는 아시아 통화 중 가장 크게 올랐지만, 인도 채권은 루피 방어와 물가로 이중 타격을 받는다는 분석이 나왔습니다 [제목]"],
 "basis": "partial",
 "check": "BW Businessworld·NewsBytes 검색 결과 요약으로 2,500억 루피 국채 매각, 일일 지준 99% 유지, 기준금리 5.50% 확인. 파생상품 한도 축소와 정유사 달러 창구 세부 수치는 확인 못 함",
 "src": [{"o": "BW Businessworld", "d": "2026-10-09", "u": "https://www.businessworld.in/article/rbi-tightens-bank-cash-rules-plans-rs-25-000-cr-bond-sale-to-drain-liquidity-627902"},
         {"o": "NewsBytes", "d": "2026-10-09", "u": "https://www.newsbytesapp.com/news/business/rbi-to-sell-25000cr-bonds-raise-daily-crr-to-99/tldr"}],
 "inds": ["macro"], "nodes": ["macro/cb", "macro/fx", "macro/liquidity"],
 "added": "이번 로이터·블룸버그 7건과 텔레그램 1건으로 {{2,500억 루피 국채 매각}}과 {{일일 지준 99% 유지}}, 파생상품 한도 {{500만 달러 축소}}가 추가됐다",
 "items": [
  I("인도중앙은행, 26억 달러 국채 매각·지급준비 강화로 유동성 흡수", R, "2026-10-09", "https://www.reuters.com/world/india/india-central-bank-sell-26-bln-bonds-tighten-bank-reserve-need-squeeze-cash-2026-10-09/",
    "{{인도중앙은행}}이 {{26억 달러}} 규모 국채를 팔고 은행 지급준비 요건을 강화하면서, 은행권에 남아도는 현금이 줄어들게 됐다"),
  I("RBI, 국채 매각·은행 현금 규정 강화로 자금 흡수", B, "2026-10-09", "https://www.bloomberg.com/news/articles/2026-10-09/rbi-to-sell-bonds-tightens-bank-cash-rules-to-drain-liquidity",
    "{{RBI}}가 국채 매각과 함께 은행이 매일 지켜야 할 지준 유지 비율을 {{최소 99%}}로 높이면서, 단기 자금시장 금리에 상승 압력이 생길 수 있다"),
  I("인도 루피 방어전 재개…정유사 달러 매입 떠맡고 환투기 여지 95% 축소", HN, "2026-10-13", "https://t.me/HANAchina/70330",
    "{{RBI}}가 국영 석유기업 달러 매입을 대차대조표로 옮기고 파생상품 한도를 {{500만 달러}}로 낮추면서, 루피가 단기 1~2% 오를 수 있다는 전망이 나왔다"),
  I("인도 채권, 루피 방어와 인플레이션에 이중 타격", B, "2026-10-13", "https://www.bloomberg.com/news/newsletters/2026-10-13/indian-bonds-face-double-blow-from-rupee-defense-inflation",
    "{{루피 방어}} 조치와 높아진 인플레이션이 한꺼번에 겹치면서 {{인도 채권}}이 이중으로 타격을 받을 처지에 놓였다 (제목 기준)"),
  I("인도 루피 구출, 유가·물가·자금 유출의 시험대에 서", B, "2026-10-13", "https://www.bloomberg.com/news/articles/2026-10-13/india-s-rupee-rescue-faces-test-from-oil-inflation-and-outflows",
    "{{인도의 루피 구출}} 조치가 높은 유가와 물가, 해외 자금 유출이라는 세 가지 압력을 버텨야 하는 {{시험대}}에 올랐다 (제목 기준)"),
  I("RBI 통화 규제 확대에 루피, 아시아 통화 중 최대 상승", B, "2026-10-13", "https://www.bloomberg.com/news/articles/2026-10-13/india-s-rupee-gains-as-rbi-takes-more-steps-to-support-currency",
    "{{RBI}}가 통화 관련 규제를 더 넓히면서 {{루피}}가 13일 아시아 통화 가운데 가장 큰 폭으로 올랐다 (제목 기준)"),
  I("루피/달러: 인도 루피가 이렇게 약한 이유와 RBI의 대응", B, "2026-10-13", "https://www.bloomberg.com/news/articles/2026-10-13/inr-usd-why-india-s-rupee-is-so-weak-and-what-the-rbi-is-doing",
    "블룸버그가 {{루피 약세}}의 원인과 {{RBI의 대응}} 조치를 짚는 해설을 내면서, 방어책이 약세 흐름을 돌릴 수 있는지가 쟁점으로 정리됐다 (제목 기준)"),
  I("RBI가 압력 완화 추가 조치 내놓자 루피 회복세 이어갈 듯", R, "2026-10-13", "https://www.reuters.com/world/india/rupee-extend-recovery-rbi-takes-more-steps-ease-pressure-2026-10-13/",
    "{{RBI}}가 환율 압력을 덜기 위한 추가 조치를 내놓으면서 {{루피}}가 회복세를 이어갈 것으로 예상된다 (제목 기준)"),
 ]})

items.append({"cid": "C034", "attachTo": "n-bbg-0250",
 "title": "USDA 옥수수 생산 {{160억 부셸}}로 깜짝 상향…선물 장중 하한가, 대두도 약세",
 "one": "{{미 농무부}}가 옥수수 단수를 에이커당 181.2부셸로 올려 생산 전망을 {{160억 3,400만 부셸}}로 높이고 기말재고도 예상을 웃돌면서 옥수수 선물이 장중 하한가까지 밀렸고, {{대두}}도 중국 구매를 기다리며 약세를 보였다",
 "facts": [
  "무엇이: USDA가 10월 9일 수급 보고서(WASDE)에서 옥수수 단수를 에이커당 181.2부셸로, 생산 전망을 9월 158억 부셸에서 160억 3,400만 부셸로 올렸습니다 [사실]",
  "재고: 2026/27년 기말재고 전망은 18억 4,900만 부셸로 시장 예상 16억 7,700만 부셸을 크게 웃돌았습니다 [사실]",
  "가격: 옥수수 선물은 장중 한때 하한가까지 떨어졌고, 12월물은 20.5센트 내린 부셸당 4.7975달러에 마감했습니다 [사실]",
  "대두: 대두 단수 53.1부셸, 생산 45억 6,200만 부셸로 모두 사상 최대 전망이 나왔습니다 [사실]",
  "수요: 13일 대두 가격은 중국의 구매 확대를 기다리며 내렸습니다 [제목]"],
 "basis": "verified",
 "check": "DTN·High Plains Journal 검색 결과 요약으로 단수·생산·기말재고·12월물 종가 확인. 텔레그램의 '장중 6%, 약 3년 만의 최대 낙폭'은 확인 못 함",
 "src": [{"o": "DTN Progressive Farmer", "d": "2026-10-09", "u": "https://www.dtnpf.com/agriculture/web/ag/news/article/2026/10/09/october-wasdes-shocking-rise-corn"},
         {"o": "High Plains Journal", "d": "2026-10-12", "u": "https://hpj.com/2026/10/12/october-9-wasde-report/"}],
 "inds": ["agri"], "nodes": [],
 "added": "이번 텔레그램 2건과 로이터·블룸버그 각 1건으로 {{USDA 옥수수 생산 상향}}과 {{옥수수 선물 급락}}, 중국 구매를 기다리는 {{대두 약세}}가 추가됐다",
 "items": [
  I("옥수수 선물, WASDE 재고 발표 뒤 낙폭 5%로 확대", PO, "2026-10-10", "https://t.me/The_MariTimes/63635",
    "미 농무부의 {{WASDE}} 재고 발표 뒤 매도가 몰리면서 {{옥수수 선물}}의 하루 낙폭이 5%까지 커졌다"),
  I("늘어난 미 옥수수 재고, USDA 가축 사료 소비 자료에 의문 키워", R, "2026-10-10", "https://www.reuters.com/business/retail-consumer/bigger-us-corn-stocks-fuel-doubts-about-usda-livestock-feeding-data-2026-10-09/",
    "미 {{옥수수 재고}}가 예상보다 크게 나오면서 USDA의 {{가축 사료 소비}} 통계가 정확한지에 대한 의문이 커졌다 (제목 기준)"),
  I("USDA 옥수수 생산 전망 깜짝 상향…선물 장중 6% 급락", HN, "2026-10-10", "https://t.me/HANAchina/70155",
    "{{미 농무부}}가 옥수수 생산 전망을 약 {{160억 부셸}}로 올리면서 감산 기대가 뒤집혀 선물이 급락하고 농기계·종자·비료주도 약세를 보였다"),
  I("대두 가격, 트레이더들 중국의 구매 확대 기다리며 하락", B, "2026-10-13", "https://www.bloomberg.com/news/articles/2026-10-13/soybeans-decline-as-traders-wait-for-china-to-step-up-purchases",
    "트레이더들이 {{중국}}이 구매를 늘리기를 기다리며 관망하는 가운데 {{대두}} 가격이 13일 하락했다 (제목 기준)"),
 ]})

items.append({"cid": "C041", "attachTo": "n-bbg-0092",
 "title": "독일 비축유 {{최대 1,500만 배럴}} 방출…IEA는 {{경유 추가 방출}} 촉구",
 "one": "{{IEA}}가 3월 약속분 잔여 약 1억 배럴을 경유 위주로 서둘러 풀기로 한 데 이어 {{독일}}이 경유·난방유부터 최대 1,500만 배럴을 풀기로 했고, IEA가 경유 추가 방출을 촉구하면서 {{유럽 경유 부족}}이 일부 누그러질 수 있다",
 "facts": [
  "무엇이: 카테리나 라이헤 독일 경제장관이 10월 9일 G7 비축 협정 이행으로 최대 1,500만 배럴을 방출하며, 경유·난방유를 먼저 풀고 원유는 뒤에 푼다고 밝혔습니다 [사실]",
  "IEA: 회원국들은 10월 7일 3월 약속분 가운데 남은 약 1억 배럴을 경유 우선으로 서둘러 풀기로 했습니다 [사실]",
  "유럽 잔여: 독일은 3월 프로그램에서 1,950만 배럴, 프랑스는 1,000만 배럴을 약속했고, JP모건은 유럽의 미방출 약속분을 약 4,000만 배럴로 추정했습니다 [사실]",
  "추가 촉구: IEA가 세계 시장 경색에 경유 추가 방출을 촉구했습니다 [제목]"],
 "basis": "partial",
 "check": "OilPrice·우크라뉴스 검색 결과 요약으로 독일 방출 규모·순서와 유럽 잔여분 확인. IEA의 경유 추가 방출 촉구 발언은 확인 못 함, 독일 물량 배분·일정은 미공개",
 "src": [{"o": "OilPrice.com", "d": "2026-10-10", "u": "https://oilprice.com/Latest-Energy-News/World-News/Russia-Germany-Add-Diesel-Supply-as-Fuel-Market-Scrambles-for-Barrels.html"},
         {"o": "UkraNews", "d": "2026-10-09", "u": "https://ukranews.com/en/news/1180338-germany-will-release-up-to-15-million-barrels-of-oil-and-petroleum-products-from-its-emergency"}],
 "inds": ["macro"], "nodes": ["macro/commodity", "macro/geo"],
 "added": "이번 텔레그램·로이터·블룸버그 3건으로 {{독일 최대 1,500만 배럴}} 방출 계획과 IEA의 {{경유 추가 방출 촉구}}가 추가됐다",
 "items": [
  I("독일, 비상 석유 비축 최대 1,500만 배럴 방출 예정", TR, "2026-10-10", "https://t.me/Trillion_labs/10232",
    "{{독일}}이 G7 비축 협정 이행으로 {{최대 1,500만 배럴}}을 풀기로 하면서, 경유와 난방유가 원유보다 먼저 시장에 나오게 됐다"),
  I("독일, G7 계획에 따라 최대 1,500만 배럴 석유 방출", R, "2026-10-10", "https://www.reuters.com/business/energy/germany-release-up-15-million-barrels-oil-under-g7-plan-2026-10-09/",
    "{{독일 정부}}가 {{G7 계획}}의 일환으로 석유 방출을 결정했지만 품목별 배분과 일정은 밝히지 않아 실제 공급 시점은 불확실하다"),
  I("IEA, 세계 시장 경색에 경유 추가 방출 촉구", B, "2026-10-11", "https://www.bloomberg.com/news/articles/2026-10-11/iea-urges-more-diesel-releases-as-global-market-tightens",
    "{{IEA}}가 세계 석유 시장이 빠듯해지자 {{경유 추가 방출}}을 촉구하면서 비축 경유 공급이 더 늘어날 수 있다 (제목 기준)"),
 ]})

items.append({"cid": "C051", "attachTo": "n-rtr-0024",
 "title": "보베스파 {{사상 최고}}…브라질 대선發 랠리에 금융주 주도, 대미 무역도 변수",
 "one": "{{브라질 대선}} 1차 투표에서 플라비우 보우소나루가 선전한 뒤 재정 개혁 기대가 커지면서 {{보베스파}}가 10월 9일 20만 9,067로 사상 최고를 찍었고, 은행주가 랠리를 이끄는 가운데 {{해외 자금}}이 브라질로 몰리고 있다",
 "facts": [
  "무엇이: 보베스파 지수가 10월 9일 20만 9,067로 사상 최고로 마감했고, 10월 들어 약 11.7% 올랐습니다 [사실]",
  "주도: 10월 5일 1차 투표 뒤 BTG팩추얼 22.5%, 브라데스코 13.6% 등 은행주가 급등을 이끌었습니다 [사실]",
  "자금: EWZ는 연초 이후 달러 기준 37% 올랐고 한 주 순유입이 23억 달러였으며, 브라질이 AI 쏠림 위험의 헤지처로 떠올랐다는 분석입니다 [채널]",
  "결선: 10월 25일 결선 투표를 앞두고 여론조사는 접전이며, 대선 결과가 관세·광물이 걸린 대미 무역을 바꿀 수 있습니다 [제목]"],
 "basis": "partial",
 "check": "Rio Times 검색 결과 요약으로 보베스파 사상 최고·10월 상승률·은행주 급등·결선 일정 확인. EWZ 연초 37%와 주간 순유입 23억 달러, 금융주 25% 상승은 확인 못 함",
 "src": [{"o": "The Rio Times", "d": "2026-10-09", "u": "https://www.riotimesonline.com/brazil-markets-ibovespa-real-friday-october-9-2026/"},
         {"o": "The Rio Times", "d": "2026-10-09", "u": "https://www.riotimesonline.com/brazil-etf-ewz-jumps-14-percent-after-first-round-2026/"}],
 "inds": ["fin"], "nodes": [],
 "added": "이번 로이터·텔레그램 2건으로 {{보베스파 사상 최고}}와 {{금융주 25% 상승}}, 대선이 관세·광물 등 {{대미 무역}}을 바꿀 수 있다는 관측이 추가됐다",
 "items": [
  I("브라질 대선, 관세·광물 걸린 대미 무역 재편할 듯", R, "2026-10-09", "https://www.reuters.com/world/americas/brazil-election-reshape-trade-with-us-with-tariffs-minerals-stake-2026-10-09/",
    "{{브라질 대선}} 결과에 따라 관세와 광물 이해가 걸린 {{대미 무역 관계}}가 다시 짜일 수 있다는 분석이 나왔다 (제목 기준)"),
  I("AI 위험 헤지처로 부상한 브라질 증시, 장기 하락 추세 돌파", HN, "2026-10-13", "https://t.me/HANAchina/70340",
    "{{보베스파}}가 이달 12.2% 올라 사상 최고를 찍고 한 주에 23억 달러가 유입되면서, 브라질이 {{AI 쏠림 위험}}의 헤지처로 떠오르고 있다"),
 ]})

items.append({"cid": "C058", "attachTo": "n-bbg-0236",
 "title": "록히드, 극초음속 대응 {{PAC-3 엣지}} 공개…안두릴 저가 요격미사일과 경쟁",
 "one": "{{록히드마틴}}이 극초음속 위협에 대응하는 PAC-3 엣지를 공개하며 연 2,000발 생산을 내걸고 {{안두릴}}이 PAC-3 절반 이하 비용을 노린 스틸핀을 내놓은 데다 쿠웨이트도 방공체계를 사들이면서, {{요격미사일 시장}} 경쟁이 달아오르고 있다",
 "facts": [
  "무엇이: 록히드마틴이 10월 9일 미 육군 차세대 요격미사일 사업 후보로 PAC-3 엣지를 공개했으며, 새 시커와 노스롭그루먼의 다중 펄스 로켓모터를 씁니다 [사실]",
  "일정·생산: 2027년 시험, 2031년 배치를 목표로 하고, 단가는 기존 PAC-3 MSE 수준에 연 약 2,000발 생산을 계획합니다 [사실]",
  "경쟁: 안두릴은 10월 12일 PAC-3 MSE 능력의 약 80%를 절반 이하 비용으로 노리는 요격미사일 계열 스틸핀을 공개했습니다 [사실]",
  "수요: 영국 정부는 쿠웨이트가 4억 8,900만(통화 단위는 제목에 없음) 규모의 방공체계를 산다고 밝혔습니다 [제목]",
  "구축함: 미 해군 2027회계연도 예산안에는 알레이버크급 구축함이 1척만 담겼습니다 [채널]"],
 "basis": "partial",
 "check": "Defense News·록히드마틴 보도자료 검색 결과 요약으로 PAC-3 엣지 공개일·일정·생산 계획 확인. 쿠웨이트 방공체계 구매는 확인 못 함",
 "src": [{"o": "Defense News", "d": "2026-10-10", "u": "https://www.defensenews.com/industry/techwatch/2026/10/10/lockheed-martin-unveils-pac-3-edge-interceptor-designed-to-counter-hypersonic-threats/"},
         {"o": "Lockheed Martin", "d": "2026-10-09", "u": "https://news.lockheedmartin.com/2026-10-09-Lockheed-Martin-Debuts-PAC-3-Edge-TM-for-the-U-S-Armys-Innovative-Future-Interceptor-Program"}],
 "inds": ["aero"], "nodes": [],
 "added": "이번 로이터 2건으로 록히드의 극초음속 대응 요격미사일 {{PAC-3 엣지}} 공개와 영국이 밝힌 {{쿠웨이트의 방공체계 구매}} 소식이 추가됐다",
 "items": [
  I("영국 '쿠웨이트, 4억 8,900만 규모 방공체계 구매'", R, "2026-10-09", "https://www.reuters.com/business/aerospace-defense/uk-says-kuwait-buys-489-million-air-defence-system-2026-10-09/",
    "영국 정부가 {{쿠웨이트}}가 4억 8,900만 규모의 {{방공체계}}를 사들인다고 밝히면서 영국의 방산 수출 계약이 하나 더해졌다 (제목 기준)"),
  I("록히드마틴, 극초음속 대응 요격미사일 PAC-3 엣지 공개", R, "2026-10-10", "https://www.reuters.com/business/aerospace-defense/lockheed-martin-unveils-pac-3-edge-interceptor-designed-counter-hypersonic-2026-10-09/",
    "{{록히드마틴}}이 극초음속 위협에 맞선 {{PAC-3 엣지}}를 공개하고 2031년 배치를 목표로 하면서, 미 육군 차세대 요격미사일 사업 경쟁에 뛰어들었다"),
 ]})

items.append({"cid": "C067", "attachTo": "",
 "title": "FDA, 테바 {{월 1회 조현병 주사}}·아사히카세이 헤르페스 치료제 승인",
 "one": "{{미 FDA}}가 테바의 월 1회 조현병 주사제 웰트루자와 아사히카세이의 지속성 헤르페스 감염 치료제를 잇달아 승인하면서, {{테바}}는 수주 안에 미국 출시에 나서고 협력사 {{메디셀}}은 최대 1억 1,200만 달러 마일스톤을 받을 수 있다",
 "facts": [
  "무엇이: 테바가 10월 9일 성인 조현병 대상 월 1회 올란자핀 주사제 웰트루자의 FDA 승인을 발표했습니다 [사실]",
  "출시: 테바는 수주 안에 미국 출시를 예상하며, 메디셀과의 협력에서 우제디에 이은 두 번째 제품입니다 [사실]",
  "수익: 메디셀은 최대 1억 1,200만 달러의 마일스톤과 로열티를 받을 수 있습니다 [사실]",
  "아사히카세이: FDA가 아사히카세이의 지속성 헤르페스 감염 치료제를 승인했습니다 [제목]"],
 "basis": "partial",
 "check": "Benzinga·Israel National News 검색 결과 요약으로 웰트루자 승인·출시 시점·메디셀 마일스톤 확인. 아사히카세이 약 이름과 세부 내용은 확인 못 함",
 "src": [{"o": "Benzinga", "d": "2026-10-09", "u": "https://www.benzinga.com/news/fda/26/10/62277846/fda-approves-tevas-new-once-monthly-schizophrenia-injection"},
         {"o": "Israel National News", "d": "2026-10-10", "u": "https://www.israelnationalnews.com/news/434362"}],
 "inds": ["pharma"], "nodes": [],
 "added": "이번 로이터 2건 가운데 나중 글로 {{아사히카세이}}의 {{지속성 헤르페스 감염 치료제}}도 FDA 승인을 받았다는 사실이 추가됐다 (제목 기준)",
 "items": [
  I("테바, 월 1회 조현병 주사제 웰트루자 FDA 승인 획득", R, "2026-10-10", "https://www.reuters.com/legal/litigation/teva-wins-fda-approval-monthly-schizophrenia-injection-weltruza-2026-10-09/",
    "{{테바}}가 한 달에 한 번 맞는 조현병 주사제 {{웰트루자}}의 FDA 승인을 받으면서, 수주 안에 미국 출시에 나설 예정이다"),
  I("미 FDA, 아사히카세이의 지속성 헤르페스 감염 치료제 승인", R, "2026-10-10", "https://www.reuters.com/business/healthcare-pharmaceuticals/us-fda-approves-asahi-kaseis-drug-persistent-herpes-infections-2026-10-09/",
    "{{미 FDA}}가 아사히카세이의 {{지속성 헤르페스 감염}} 치료제를 승인하면서, 아사히카세이가 이 약을 미국에서 팔 수 있게 됐다 (제목 기준)"),
 ]})

items.append({"cid": "C075", "attachTo": "n-tg-0206",
 "title": "TSMC 실적 앞두고 {{2나노 비중 11%}}…BofA 목표가 620달러, 패키징이 새 병목",
 "one": "{{TSMC}}의 3분기 매출이 약 1조 4,900억 대만달러로 가이던스 상단을 넘고 2나노 매출 비중이 3%에서 11%로 뛰면서 {{BofA}}가 15일 실적 발표를 앞두고 목표가를 620달러로 올렸고, AI 칩 병목은 {{첨단 패키징}}으로 옮겨가고 있다",
 "facts": [
  "무엇이: BofA가 10월 12일 TSMC 미국 주식 목표가를 590달러에서 620달러로 올렸습니다 [사실]",
  "실적: 3분기 매출은 약 1조 4,900억 대만달러로 가이던스 상단을 약 2% 웃돌았고, 실적 발표는 10월 15일입니다 [사실]",
  "2나노: BofA는 2나노 매출 비중이 전 분기 3%에서 11%로 뛰었고 선행 PER 16배는 역사적 중간값이라고 봤습니다 [사실]",
  "9월 매출: 9월 매출은 5,118억 6,000만 대만달러로 전년보다 54.6% 늘었습니다 [채널]",
  "패키징: AI 칩 병목이 패키징으로 옮겨가며 TSMC 주도 CoPoS는 2028~2029년 양산이 예상되고, FOPLP·유리 기판이 차세대 기술로 꼽힙니다 [채널]"],
 "basis": "verified",
 "check": "TipRanks·Futu 검색 결과 요약으로 BofA 목표가, 2나노 비중 3%→11%, 3분기 매출, 발표일 확인. 4분기 성장률은 출처마다 11%, 10~15%로 엇갈림. 패키징 내용은 확인 못 함",
 "src": [{"o": "TipRanks", "d": "2026-10-12", "u": "https://www.tipranks.com/news/bofa-raises-tsmc-stock-tsm-price-target-ahead-of-q3-earnings-heres-why"},
         {"o": "Futu News", "d": "2026-10-13", "u": "https://news.futunn.com/en/post/1000942698/ahead-of-the-earnings-report-bank-of-america-raises-taiwan"}],
 "inds": ["macro"], "nodes": ["macro/semis"],
 "added": "이번 텔레그램 2건으로 {{BofA 목표가 620달러}}와 {{2나노 비중 11%}}, 차세대 패키징 {{CoPoS 2028~2029년 양산}} 전망이 추가됐다",
 "items": [
  I("TSMC 실적 임박…CoPoS·FOPLP·유리 기판이 AI 패키징 공급망 재편", HN, "2026-10-10", "https://t.me/HANAchina/70168",
    "AI 칩 생산 병목이 첨단 공정에서 {{패키징}}으로 옮겨가면서, TSMC 주도 {{CoPoS}}와 FOPLP·유리 기판이 차세대 핵심 기술로 떠오르고 있다"),
  I("BofA, TSMC 목표가 620달러로 상향…2나노 확대에 매출·이익률 개선", HN, "2026-10-13", "https://t.me/HANAchina/70339",
    "{{BofA}}가 2나노 매출 비중이 {{3%에서 11%}}로 뛴 점을 들어 목표가를 올리면서, 4분기 매출도 전 분기보다 11% 더 늘 것으로 내다봤다"),
 ]})

items.append({"cid": "C083", "attachTo": "n-rtr-0025",
 "title": "제프리스 '美 AI 대규모 {{자본 파괴}}' 경고…혹 탄 발언에 기술주 매도",
 "one": "{{제프리스}} 크리스 우드가 값싼 중국 오픈소스 모델이 점유율을 가져가 미국 AI에서 막대한 자본 손실이 날 수 있다고 경고한 데 이어 {{혹 탄}}의 자금 병목 발언이 기술주 매도를 부르면서, {{AI 인프라 자금줄}}에 대한 경계가 커지고 있다",
 "facts": [
  "무엇이: 제프리스 크리스 우드는 10월 9일자 GREED & fear에서 미국 AI 사이클의 가장 유력한 결말이 막대한 자본 파괴이며 점유율이 값싼 중국 오픈소스 모델로 넘어갈 것이라고 봤습니다 [사실]",
  "근거: 오픈라우터 기준 중국 상위 모델 처리 토큰은 9월 27일 주간 76조 1,200억 개로 4월 말 4조 3,700억 개에서 급증했고, AI 토큰 평균 가격은 5월 고점보다 52% 떨어졌습니다 [사실]",
  "신용: 우드는 하이퍼스케일러가 적자인 OpenAI·앤트로픽에 사실상 무담보 대출을 몰아줬다며 2008년에 비유했고, 결말은 신용시장이 정할 것이라고 했습니다 [사실]",
  "매도: JP모건 조슈아 마이어스는 혹 탄 브로드컴 CEO의 자금 조달 병목 발언을 13일 기술주 매도의 직접 원인으로 꼽았습니다 [채널]",
  "전력: 한 증권사 보고서는 내년 최대 19GW, 2028년에는 그 이상의 전력 부족을 예상했습니다 [채널]"],
 "basis": "verified",
 "check": "Crypto Briefing·Tiger Brokers 검색 결과 요약으로 우드의 자본 파괴 경고와 토큰 수치 확인(같은 취지 발언은 7월에도 있었음). JP모건의 매도 원인 분석과 19GW 전력 부족 보고서는 확인 못 함",
 "src": [{"o": "Crypto Briefing", "d": "2026-10-10", "u": "https://cryptobriefing.com/jefferies-warns-us-ai-capital-destruction/"},
         {"o": "Tiger Brokers", "d": "2026-10-10", "u": "https://www.itiger.com/news/1179263540"}],
 "inds": ["macro"], "nodes": ["macro/semis"],
 "added": "이번 텔레그램 2건으로 제프리스의 {{중국 오픈소스 모델}}발 자본 손실 경고와 혹 탄 발언에 따른 {{기술주 매도}}, {{19GW 전력 부족}} 전망이 추가됐다",
 "items": [
  I("제프리스 'AI 사이클 결말은 미국 자본 대손실·中 오픈소스로 점유율 이동'", PO, "2026-10-11", "https://t.me/The_MariTimes/63649",
    "{{제프리스}}가 중국 모델 확산에 따른 토큰 가격 하락과 하이퍼스케일러 부채 증가를 지적하면서, {{미국 AI 투자}}가 막대한 자본 손실로 끝날 수 있다고 경고했다"),
  I("JP모건 '혹 탄의 자금 병목 경고가 기술주 매도 직접 원인'", TR, "2026-10-13", "https://t.me/Trillion_labs/10399",
    "{{혹 탄}}의 자금 조달 병목 경고와 {{최대 19GW}} 전력 부족 전망이 겹치면서 13일 기술주 매도세가 커졌다는 분석이 나왔다"),
 ]})

items.append({"cid": "C093", "attachTo": "",
 "title": "佛 시펄·쿼블리, {{프로세서와 양자컴퓨터}} 연결 방안 모색",
 "one": "프랑스 프로세서 업체 {{시펄}}과 양자컴퓨터 업체 {{쿼블리}}가 자사 프로세서와 양자컴퓨터를 잇는 방안을 함께 찾으면서, 기존 프로세서와 양자컴퓨터를 묶어 쓰는 {{하이브리드 컴퓨팅}} 협력이 시작될 수 있다 (제목 기준)",
 "facts": [
  "무엇이: 프랑스 시펄과 쿼블리가 프로세서와 양자컴퓨터를 연결하는 방안을 모색합니다 [제목]",
  "의미: 기존 프로세서와 양자컴퓨터를 함께 쓰는 구성을 겨냥한 협력으로 보입니다 [추론]"],
 "basis": "title",
 "check": "검색하지 않음. 로이터 제목만 근거",
 "src": [], "inds": ["macro"], "nodes": ["macro/semis"],
 "items": [I("프랑스 시펄·쿼블리, 프로세서와 양자컴퓨터 연결 모색", R, "2026-10-09", "https://www.reuters.com/business/frances-sipearl-quobly-explore-linking-processors-with-quantum-computers-2026-10-09/")]})

items.append({"cid": "C101", "attachTo": "",
 "title": "독일 정부, {{독불 전차 공동사업}} 포기설 부인",
 "one": "{{독일 정부}}가 프랑스와 함께하는 전차 공동 개발 사업에서 손을 뗐다는 주장을 부인하면서, {{독불 전차 사업}}이 계속 유지된다는 입장이 확인돼 양국 방산 협력의 불확실성이 다소 줄었다 (제목 기준)",
 "facts": [
  "무엇이: 독일 정부가 독불 전차 사업을 포기했다는 주장을 부인했습니다 [제목]",
  "의미: 사업 지속 여부를 둘러싼 논란이 있었다는 뜻으로, 양국 방산 협력의 마찰이 이어지고 있음을 보여줍니다 [추론]"],
 "basis": "title",
 "check": "검색하지 않음. 로이터 제목만 근거",
 "src": [], "inds": ["aero"], "nodes": [],
 "items": [I("독일, 독불 전차 공동사업 포기했다는 주장 부인", R, "2026-10-09", "https://www.reuters.com/business/aerospace-defense/berlin-rejects-claim-it-dropped-franco-german-tank-project-2026-10-09/")]})

items.append({"cid": "C109", "attachTo": "n-rtr-0043",
 "title": "美 은행주 {{기술적 조정}}…골드만은 약세장 진입 속 실적 시즌",
 "one": "{{미 은행주}}가 국채금리 급등 속에 한 달 반 사이 나란히 10% 넘게 떨어지고 {{골드만삭스}} 등 일부는 20% 이상 밀려 약세장에 들어선 가운데 13일 3분기 실적을 맞으면서, 약 190억 달러로 예상되는 {{트레이딩 수입}}이 분위기를 바꿀지가 관건이 됐다 (채널 전언)",
 "facts": [
  "무엇이: KBW 은행지수가 8월 중순 고점보다 10% 넘게 떨어져 기술적 조정에 들어갔고, 10년물 국채금리는 약 5.27%로 약 24년 만의 최고 수준입니다 [사실]",
  "약세장: 골드만삭스 등 일부 은행주는 20% 넘게 떨어져 기술적 약세장에 들어섰습니다 [채널]",
  "실적: JP모건·골드만삭스·씨티·웰스파고가 10월 13일 개장 전 실적을 내며, 트레이딩 수입은 약 190억 달러로 예상됩니다 [사실]",
  "관전 포인트: 투자자들은 고금리가 신용 건전성과 대출 수요를 해치는지 주시하고 있습니다 [사실]"],
 "basis": "channel",
 "check": "새 텔레그램 글은 검색하지 않음. 골드만삭스 등 일부 은행주의 약세장 진입은 확인 못 함. 지수 조정·실적 일정은 기존 문서 근거",
 "src": [], "inds": ["macro"], "nodes": ["macro/rates"],
 "added": "이번 텔레그램 1건으로 {{골드만삭스}} 등 일부 은행주가 {{20% 넘게 떨어져}} 기술적 약세장에 들어섰다는 내용이 추가됐다",
 "items": [I("미 주요 은행주 나란히 기술적 조정, 골드만 등 일부는 약세장 진입", PO, "2026-10-09", "https://t.me/The_MariTimes/63617",
    "{{국채금리 상승}}이 은행에 악재로 작용하면서 미 주요 은행주가 한 달 반 새 10% 넘게 떨어지고 {{골드만삭스}} 등은 20% 넘게 밀렸다")]})

items.append({"cid": "C117", "attachTo": "",
 "title": "트럼프, 멕시코에 {{양국 에너지 기업 제휴}} 확대 압박",
 "one": "{{트럼프 대통령}}이 멕시코에 양국 에너지 기업 간 제휴를 더 늘리라고 압박했다는 FT 보도가 나오면서, {{멕시코 에너지 시장}}에서 미국 기업의 참여가 넓어질 수 있다 (제목 기준)",
 "facts": [
  "무엇이: 트럼프 대통령이 멕시코에 양국 에너지 기업 간 제휴를 늘리라고 압박하고 있다고 FT가 보도했습니다 [제목]",
  "의미: 미국 에너지 기업의 멕시코 사업 확대로 이어질 수 있습니다 [추론]"],
 "basis": "title",
 "check": "검색하지 않음. 로이터 제목(FT 인용)만 근거",
 "src": [], "inds": ["macro"], "nodes": ["macro/geo"],
 "items": [I("트럼프, 멕시코에 양국 에너지 기업 간 제휴 확대 압박 - FT", R, "2026-10-10", "https://www.reuters.com/business/energy/trump-pushes-mexico-more-cross-nation-tie-ups-between-energy-companies-ft-2026-10-09/")]})

items.append({"cid": "C133", "attachTo": "n-tg-0153",
 "title": "중국 상무부, 미국 주도 {{과잉생산 성명}}에 '필요한 대응' 경고",
 "one": "미국이 14개 경제권과 과잉생산 대응 공동성명을 내자 {{중국 상무부}}가 10월 9일 중국 이익을 해치는 조치에는 필요한 대응을 하겠다고 경고하면서, 희토류·갈륨 등 {{핵심광물 보복}} 가능성이 거론되고 {{공급망 다변화}}에 관심이 쏠리고 있다",
 "facts": [
  "무엇이: 중국 상무부 대변인이 10월 9일 과잉생산을 구실로 한 보호무역에 반대하며, 관련 경제권이 중국 이익을 해치는 조치를 하면 필요한 대응을 하겠다고 밝혔습니다 [사실]",
  "배경: USTR이 10월 7일 14개 경제권 고위 인사와 구조적 과잉생산 대응 공동 각료성명에 서명했다고 발표했습니다 [사실]",
  "대상: 성명은 자동차·전기차, 배터리, 화학, 범용 반도체, 태양광 패널을 우선 분야로 정했습니다 [사실]",
  "보복 수단: 희토류·영구자석·갈륨·게르마늄·안티몬 등 핵심광물을 통한 보복 가능성이 거론됩니다 [채널]",
  "한계: 상무부는 구체적 보복 조치는 밝히지 않았습니다 [사실]"],
 "basis": "verified",
 "check": "신화통신·글로벌타임스 검색 결과 요약으로 상무부 발언과 날짜 확인. 핵심광물 보복 가능성은 채널의 해석",
 "src": [{"o": "신화통신", "d": "2026-10-10", "u": "https://english.news.cn/20261010/2db8c34921c34182a2b4787be889df33/c.html"},
         {"o": "글로벌타임스", "d": "2026-10-09", "u": "https://www.globaltimes.cn/page/202610/1371922.shtml"}],
 "inds": ["macro"], "nodes": ["macro/geo"],
 "added": "이번 텔레그램 1건으로 {{중국 상무부}}의 '필요한 대응' 경고와 희토류·갈륨 등 {{핵심광물 보복}} 가능성이 추가됐다",
 "items": [I("중국 상무부, 미국 등의 과잉생산 대응에 '필요한 대응' 경고", TR, "2026-10-10", "https://t.me/Trillion_labs/10280",
    "{{중국 상무부}}가 중국 이익을 해치는 조치에 대응하겠다고 경고하면서, 희토류·갈륨 등 {{핵심광물}} 보복 가능성이 커졌다는 해석이 나온다")]})

items.append({"cid": "C149", "attachTo": "",
 "title": "美 전기차 판매 부진에도 {{충전망 확충}}…올해 충전소 2,000곳 늘어",
 "one": "미국 전기차 신차 비중이 약 12%에서 6%로 줄었는데도 {{충전 업체}}들이 10월 초까지 충전소 2,000곳과 플러그 1만 2,000개 이상을 새로 깔면서, {{충전 불편}}이 줄어 {{전기차 수요}} 회복을 뒷받침할 수 있다",
 "facts": [
  "무엇이: 10월 초까지 미국에 신규 충전소 약 2,000곳과 충전 포트 1만 2,000개 이상이 추가돼, 기록적이던 2025년과 비슷한 속도입니다 [사실]",
  "판매: 미국 전기차 판매는 올해 1~9월 전년보다 30.7% 줄었습니다 [사실]",
  "비중: 신차 판매 중 전기차 비중은 세액공제 종료 직전인 2025년 3분기 약 12%에서 올해 약 6%로 낮아졌습니다 [채널]",
  "업체: 테슬라는 올해 급속 충전 플러그 3,500개 이상을 더해 약 4만 개를 확보했고, 현대차·도요타 등이 지원하는 아이오나는 급속 충전소 180곳 이상을 운영합니다 [채널]",
  "수익성: 차지포인트는 2분기 매출 1억 1,600만 달러에 순손실 3,560만 달러, EVgo는 순손실 4,630만 달러를 냈습니다 [채널]"],
 "basis": "verified",
 "check": "Tiger Brokers(다우존스 기사 전재)·vietnam.vn 검색 결과 요약으로 충전소·포트 수, 판매 30.7% 감소, 테슬라 3,500개 확인. 신차 비중과 업체별 손익은 확인 못 함",
 "src": [{"o": "Tiger Brokers", "d": "2026-10-11", "u": "https://www.itiger.com/news/2674627815"},
         {"o": "vietnam.vn", "d": "2026-10-12", "u": "https://vietnam.vn/en/thi-truong-sac-xe-dien-my-tang-truong-ky-luc-bat-chap-giam-doanh-so"}],
 "inds": ["auto"], "nodes": [],
 "items": [I("미 전기차 판매 둔화에도 충전 인프라는 조용히 개선", "텔레그램 상상인 김진범", "2026-10-11", "https://t.me/PipeBeom/6656")]})

items.append({"cid": "C157", "attachTo": "n-bbg-0180",
 "title": "우버, 비용 경쟁에 {{아프리카서 후퇴}}…나이지리아 무브도 철수",
 "one": "{{우버}}가 9월 나이지리아에서 철수한 데 이어 편의와 안전보다 비용이 앞서는 아프리카 시장에서 물러나고 차량금융 업체 {{무브}}도 현지 사업을 접으면서, {{현지 차량호출 시장}}에서 이탈이 이어지고 있다 (제목 기준)",
 "facts": [
  "무엇이: 우버가 편의와 안전보다 비용이 앞서는 아프리카에서 후퇴하고 있습니다 [제목]",
  "무브: 무브가 10월 8일 나이지리아 철수를 발표했으며, 우버가 9월 2일 나이지리아 철수를 밝힌 지 약 5주 만입니다 [사실]",
  "이유: 무브 공동 CEO 라디 델라노는 우버 이탈로 사업 경제성이 바뀌어 기존 모델 유지가 어렵다고 설명했습니다 [사실]",
  "정리: 무브는 350억 나이라 이상(약 2,200만~2,600만 달러)어치 차량 소유권을 운전자에게 넘깁니다 [사실]"],
 "basis": "title",
 "check": "새 블룸버그 글은 검색하지 않음, 제목 기준. 무브 관련 사실은 기존 문서 근거",
 "src": [], "inds": ["tech"], "nodes": [],
 "added": "이번 블룸버그 1건으로 우버가 {{비용 경쟁}} 탓에 나이지리아를 넘어 {{아프리카}} 시장에서 물러나고 있다는 분석이 추가됐다 (제목 기준)",
 "items": [I("우버, 편의·안전보다 비용이 앞서는 아프리카에서 후퇴", B, "2026-10-11", "https://www.bloomberg.com/news/articles/2026-10-11/uber-retreats-in-africa-as-cost-comes-before-comfort-and-safety",
    "{{우버}}가 승객들이 편의와 안전보다 {{비용}}을 우선하는 아프리카 시장에서 사업을 줄이며 물러나고 있다 (제목 기준)")]})

items.append({"cid": "C165", "attachTo": "",
 "title": "홍콩 공항청, 뉴월드 사업 넘겨받아…{{정씨 일가}} 구조조정 시간 벌어",
 "one": "{{홍콩 공항청}}이 뉴월드개발의 180억 홍콩달러 규모 11 스카이즈 사업을 넘겨받고 임대료를 탕감하는 구제안이 나오면서, {{정씨 일가}}가 2029년 말까지 {{뉴월드 자본구조}}를 손볼 시간을 벌었다",
 "facts": [
  "무엇이: 홍콩 공항청이 뉴월드의 180억 홍콩달러 규모 11 스카이즈 사업을 완전히 넘겨받고 수십억 홍콩달러의 임대료를 탕감하는 구제안이 나왔습니다 [사실]",
  "옵션: 공항청은 3년 안에 저우다푸기업이 가진 뉴월드 주식 7억 5,000만 주를 22억 5,000만 홍콩달러에 살 수 있는 권리를 받습니다 [사실]",
  "부채: 이르면 내년 약 110억 달러의 부채 만기가 돌아오며, 이번 거래로 정씨 일가는 2029년 말까지 자본구조를 손볼 시간을 얻었습니다 [사실]",
  "한계: 정씨 일가가 아직 추가 사재를 투입하지 않았다는 지적이 나왔습니다 [사실]"],
 "basis": "partial",
 "check": "briefs.co 검색 결과 요약으로 공항청 구제안 내용 확인. 블룸버그 기사와 같은 거래인지와 정확한 발표일은 확인 못 함",
 "src": [{"o": "Briefs", "d": "2026-10-12", "u": "https://www.briefs.co/news/hong-kong-s-airport-authority-moves-to-rescue-new-world-deve/"}],
 "inds": ["realestate"], "nodes": [],
 "items": [I("홍콩의 구명줄, 정씨 일가에 뉴월드 구할 시간 벌어줘", B, "2026-10-13", "https://www.bloomberg.com/news/articles/2026-10-12/hong-kong-lifeline-buys-cheng-family-time-to-save-new-world")]})

items.append({"cid": "C173", "attachTo": "",
 "title": "인도 식품당국, {{800억 달러}} 온라인 식품시장 관리 강화",
 "one": "{{인도 식품안전당국}}이 800억 달러 규모로 커진 {{온라인 식품시장}}에 대한 관리를 조이기로 하면서, 온라인 식품 판매·배달 업체들의 규제 대응 부담이 커질 수 있다 (제목 기준)",
 "facts": [
  "무엇이: 인도 식품당국이 800억 달러 규모 온라인 식품시장에 대한 통제를 강화합니다 [제목]",
  "영향: 온라인 식품 판매·배달 업체의 규제 준수 비용이 늘 수 있습니다 [추론]"],
 "basis": "title",
 "check": "검색하지 않음. 블룸버그 제목만 근거",
 "src": [], "inds": ["consumer"], "nodes": [],
 "items": [I("인도 식품당국, 800억 달러 온라인 식품시장 관리 강화", B, "2026-10-13", "https://www.bloomberg.com/news/articles/2026-10-13/india-food-watchdog-to-tighten-grip-on-80-billion-online-market")]})

items.append({"cid": "C182", "attachTo": "",
 "title": "연기금 PGGM, {{ING 대출 50억 유로}} 연계 SRT 참여",
 "one": "네덜란드 연기금 운용사 {{PGGM}}이 ING 대출 50억 유로와 연계된 {{위험이전거래(SRT)}}를 떠받치기로 하면서, ING가 대출 위험 일부를 덜어 자본 부담을 줄일 수 있다 (제목 기준)",
 "facts": [
  "무엇이: 연기금 PGGM이 ING 대출 50억 유로에 연계된 SRT를 지원하기로 합의했습니다 [제목]",
  "의미: SRT는 은행이 대출 위험 일부를 투자자에게 넘겨 자본 부담을 줄이는 거래입니다 [추론]"],
 "basis": "title",
 "check": "검색하지 않음. 블룸버그 제목만 근거",
 "src": [], "inds": ["fin"], "nodes": [],
 "items": [I("연기금 PGGM, ING 대출 50억 유로 연계 SRT 지원 합의", B, "2026-10-13", "https://www.bloomberg.com/news/articles/2026-10-13/pension-pggm-agrees-to-back-srt-tied-to-5-billion-of-ing-loans")]})

items.append({"cid": "C190", "attachTo": "",
 "title": "레볼루트·빈티드 투자사 스프린츠, {{7억 2,500만 유로}} 펀드 조성",
 "one": "레볼루트와 빈티드에 투자해 온 {{스프린츠}}가 7억 2,500만 유로 규모의 새 펀드를 모으면서, {{스타트업 투자}}에 쓸 수 있는 자금이 그만큼 늘어나 후속 투자 여력이 커지게 됐다 (제목 기준)",
 "facts": [
  "무엇이: 레볼루트·빈티드 투자사 스프린츠가 7억 2,500만 유로 펀드를 조성했습니다 [제목]",
  "의미: 스타트업 후속 투자 여력이 커집니다 [추론]"],
 "basis": "title",
 "check": "검색하지 않음. 블룸버그 제목만 근거",
 "src": [], "inds": ["fin"], "nodes": [],
 "items": [I("레볼루트·빈티드 투자사 스프린츠, 7억 2,500만 유로 펀드 조성", B, "2026-10-13", "https://www.bloomberg.com/news/articles/2026-10-13/revolut-and-vinted-backer-sprints-raises-725-million-fund")]})

items.append({"cid": "C198", "attachTo": "",
 "title": "노키아, 기업 캠퍼스 엣지 사업 {{아우렐리우스}}에 매각",
 "one": "{{노키아}}가 기업 캠퍼스 엣지 사업을 {{아우렐리우스}}에 매각하면서, 해당 사업이 노키아의 사업 구성에서 빠지고 노키아는 남은 사업에 더 집중할 수 있게 됐다 (제목 기준)",
 "facts": [
  "무엇이: 노키아가 기업 캠퍼스 엣지 사업을 아우렐리우스에 팔았습니다 [제목]",
  "의미: 노키아의 사업 포트폴리오 정리로 볼 수 있습니다 [추론]"],
 "basis": "title",
 "check": "검색하지 않음. 로이터 제목만 근거",
 "src": [], "inds": ["tech"], "nodes": [],
 "items": [I("노키아, 기업 캠퍼스 엣지 사업 아우렐리우스에 매각", R, "2026-10-13", "https://www.reuters.com/business/nokia-sells-enterprise-campus-edge-business-aurelius-2026-10-13/")]})

out = {"agent": "W7", "searches_used": 16, "fetches_used": 0, "items": items,
       "skipped": [{"cid": "C125", "reason": "AI 투자 증액"},
                   {"cid": "C141", "reason": "범위 밖"}]}

def strip(x):
    x = re.sub(r' \((제목 기준|채널 전언)\)$', '', x)
    return x.replace('{{', '').replace('}}', '')

errs = []
for it in items:
    c = it['cid']
    multi = len(it['items']) > 1 or it['attachTo']
    tl = len(strip(it['title'])); n = it['title'].count('{{')
    if not (20 <= tl <= 50) or not (1 <= n <= 2): errs.append((c, 'title', tl, n))
    ol = len(strip(it['one'])); n = it['one'].count('{{')
    lo, hi = (90, 160) if multi else (80, 130)
    if not (lo <= ol <= hi) or not (2 <= n <= 4) or not strip(it['one']).endswith('다'): errs.append((c, 'one', ol, n))
    if it['basis'] == 'title' and not it['one'].endswith('(제목 기준)'): errs.append((c, 'tail'))
    if it['basis'] == 'channel' and not it['one'].endswith('(채널 전언)'): errs.append((c, 'tail'))
    if it['basis'] in ('verified', 'partial') and it['one'].endswith(')'): errs.append((c, 'tail?'))
    if not (2 <= len(it['facts']) <= 5) or not it['facts'][0].startswith('무엇이:'): errs.append((c, 'facts'))
    for f in it['facts']:
        if '|' in f or '**' in f or '{{' in f: errs.append((c, 'fact char'))
    if multi:
        a = it.get('added', '')
        al = len(strip(a)); n = a.count('{{')
        if not (60 <= al <= 140) or not (1 <= n <= 3) or not strip(a).endswith('다'): errs.append((c, 'added', al, n))
    else:
        if 'added' in it: errs.append((c, 'added extra'))
    for k in it['items']:
        if not (25 <= len(k['t']) <= 60): errs.append((c, 't', k['t'], len(k['t'])))
        if multi:
            s = k.get('s', '')
            sl = len(strip(s)); n = s.count('{{')
            if not (45 <= sl <= 110) or not (1 <= n <= 2) or not strip(s).endswith('다'): errs.append((c, 's', sl, n, s[:30]))
        elif 's' in k: errs.append((c, 's extra'))
    ds = [k['d'] for k in it['items']]
    if ds != sorted(ds): errs.append((c, 'order'))
print(errs)
json.dump(out, open('/home/user/news-desk/data/mix-2026-10-13b/out2/W7.json', 'w'), ensure_ascii=False, indent=1)
