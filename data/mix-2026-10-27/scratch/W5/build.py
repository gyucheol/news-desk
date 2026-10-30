import json
D = '2026-10-27'
def V(ind, node, f, d, k, t): return {"ind": ind, "node": node, "f": f, "dir": d, "k": k, "t": t}
def I(t, o, u, s=None, d=D):
    x = {"t": t, "o": o, "d": d, "u": u}
    if s: x["s"] = s
    return x
def S(o, u, d=D): return {"o": o, "d": d, "u": u}
TG = '텔레그램 '
R = []

R.append(dict(cid="G1-007", attachTo="",
 title="정제유 공급난 심화…골드만 '중동·러 정유 가동중단 하루 580만 배럴'·중국 경유 수출 감소·인도 수출 급증",
 one="\n".join([
  "중동·러시아 정유 차질로 경유 등 석유제품 공급난이 깊어지는 가운데 인도 수출이 숨통을 틀 수 있다는 전망이 나왔다",
  "· 골드만삭스는 중동·러시아 정유 가동중단이 하루 580만 배럴로 최악 시나리오 500만 배럴을 넘었다고 밝혔다",
  "· 골드만은 가을 정기보수가 27% 줄어 2027년 2분기 인도·한국 정유 가동중단이 계절 평균을 140% 웃돌 것으로 봤다",
  "· 중국은 국내 재고 감소로 경유 수출을 계속 줄이며 두 차례 전쟁으로 흔들린 세계 시장을 더 압박했다",
  "· 블룸버그는 인도 경유 수출 급증이 내년 세계 공급난을 덜 수 있다고 전했다",
  "· 프랑스 정유사들은 경유 전략비축유를 다시 채울 의무 없이 방출해 사실상 매각하고 있다"]),
 facts=[
  "무엇이: 골드만삭스는 10월 25일 보고서에서 중동·러시아 정유공장 초과 가동중단을 하루 580만 배럴(중동 160만, 러시아 420만)로 추산해 9월 최악 시나리오 500만 배럴을 넘었다고 밝혔다 [사실]",
  "정비 이연: 가을 정기보수가 전년보다 27% 줄어 2027년 2분기 인도·한국 정유 가동중단이 계절 평균을 140% 웃돌고 공급 부족이 2027년까지 이어질 수 있다고 봤다 [채널]",
  "중국: 국내 재고 감소로 경유 수출 감소세가 이어지며 세계 시장 압박을 키웠다 [채널]",
  "인도: 인도 경유 수출 급증이 내년 세계 경유 공급난을 덜 것으로 보인다 [제목]",
  "프랑스: 정유사들이 경유 전략비축유 방출 뒤 리필할 필요가 없다고 정부로부터 확인받아 미국식 대여가 아닌 매각 형태로 방출하고 있다 [채널]"],
 basis="partial",
 check="골드만 580만 배럴(중동 160만·러시아 420만)과 9월 최악 시나리오 500만 배럴 초과는 검색 결과 요약(Futu 등)으로 확인. 중국 경유 수출 감소·인도 수출 급증·프랑스 비축유 매각 방출은 확인 못 함",
 src=[S("Futu News", "https://news.futunn.com/en/post/1002378523/goldman-sachs-warns-that-the-scale-of-refinery-outages-has"),
      S("IndexBox", "https://www.indexbox.io/blog/goldman-sachs-diesel-at-the-core-of-global-oil-supply-squeeze/")],
 inds=["oil"], nodes=[],
 vc=[V("oil", "refining", "공급", "down", "실제", "중동·러 정유 가동중단 하루 580만 배럴"),
     V("oil", "products", "공급", "up", "예상", "인도 경유 수출 급증에 내년 공급난 완화 전망")],
 items=[
  I("골드만, 중동·러 정유 가동중단 하루 580만 배럴로 최악 시나리오 초과", TG+"하나증권 중국전략", "https://t.me/HANAchina/71084",
    "골드만삭스가 중동·러시아 정유 가동중단을 하루 580만 배럴로 추산하면서 석유제품 공급 부족이 2027년까지 이어질 수 있다고 경고했다"),
  I("프랑스, 경유 전략비축유 리필 없이 매각 형태로 방출", TG+"Polaristimes", "https://t.me/The_MariTimes/64027",
    "프랑스 정유사들이 경유 전략비축유를 리필 의무 없이 방출하면서 미국식 대여가 아닌 매각 형태로 시장에 물량을 풀고 있다"),
  I("중국, 국내 재고 감소로 경유 수출 감소세 지속", TG+"트릴리온", "https://t.me/Trillion_labs/11267",
    "중국이 국내 경유 재고 감소로 수출을 계속 줄이면서 두 차례 전쟁으로 흔들린 세계 경유 시장에 압박을 더했다"),
  I("인도 경유 수출 급증, 내년 세계 공급난 완화 전망", "블룸버그", "https://www.bloomberg.com/news/articles/2026-10-27/india-diesel-export-boom-set-to-ease-global-crunch-next-year",
    "인도의 경유 수출이 급증하면서 내년 세계 경유 공급난이 완화될 것이라는 전망이 나왔다 (제목 기준)")]))

R.append(dict(cid="G1-018", attachTo="",
 title="UPS 3분기 매출 228.5억 달러·조정 EPS 1.69달러로 예상 상회…연간 전망 상향",
 one="\n".join([
  "UPS의 3분기 매출과 조정 주당순이익이 시장 예상을 웃돌았고 연간 실적 전망도 높아졌다",
  "· 매출은 228억 5,000만 달러로 전년보다 6.7% 늘어 예상치 222억 8,000만 달러를 넘었다",
  "· 조정 EPS는 1.69달러로 예상 1.62달러를 웃돌았지만 1년 전 1.74달러보다는 낮았다",
  "· 연간 매출 전망은 약 926억 달러, 조정 EPS 전망은 약 7.28달러로 높여 제시됐다"]),
 facts=[
  "무엇이: UPS의 3분기 매출은 229억 달러(채널 228억 5,000만 달러)로 전년 대비 6.7% 늘었고 조정 EPS는 1.69달러였다 [사실]",
  "예상 대비: 시장 예상은 매출 222억 8,000만 달러, 조정 EPS 1.62달러였다 [채널]",
  "수익성: 조정 영업이익은 20억 5,400만 달러로 1년 전 21억 3,200만 달러보다 줄었고 조정 영업이익률은 10.0%에서 9.0%로 낮아졌다 [사실]",
  "전망: 2026년 연간 매출 약 926억 달러, 조정 EPS 약 7.28달러, 조정 잉여현금흐름 약 61억 달러로 전망을 높였고 4분기 매출은 약 257억 달러로 제시했다 [사실]"],
 basis="verified",
 check="UPS 실적 발표문(investors.ups.com)을 열어 매출 6.7% 증가·조정 EPS 1.69달러·연간 전망 상향 확인. 시장 예상치는 확인 못 함",
 src=[S("UPS 투자자 관계 실적 발표", "https://investors.ups.com/news-events/press-releases/detail/2172/ups-releases-3q-2026-earnings")],
 inds=["shipping"], nodes=[],
 vc=[V("shipping", "ports", "수요", "up", "실제", "UPS 3분기 매출 6.7% 증가·연간 전망 상향")],
 items=[
  I("UPS 3분기 매출·조정 EPS 예상 상회, 연간 가이던스 상향", TG+"미국 주식 인사이더", "https://t.me/insidertracking/67491",
    "UPS가 3분기 매출 228억 5,000만 달러, 조정 EPS 1.69달러로 예상을 웃돌면서 연간 실적 가이던스도 올렸다"),
  I("UPS, 연말 성수기 강세 신호 속 매출 전망 상향", "블룸버그", "https://www.bloomberg.com/news/articles/2026-10-27/ups-raises-sales-outlook-in-sign-of-strength-for-holiday-season",
    "UPS가 연간 매출 전망을 높이면서 연말 성수기 택배 물동량이 견조하다는 신호를 시장에 보냈다")]))

R.append(dict(cid="G1-024", attachTo="",
 title="인도네시아, 싱가포르행 가스 수출 하루 3,100만 입방피트 축소…양국 화재 TF로 긴장 완화",
 one="\n".join([
  "인도네시아가 10월 24일부터 싱가포르행 파이프라인 가스 수출을 줄이면서 양국 갈등이 불거졌다",
  "· 감축량은 하루 3,100만 표준입방피트로 나투나 1,500만, 수마트라 1,600만이다",
  "· 인도네시아는 바탐·빈탄·수마트라 발전용 국내 수요를 먼저 채우려는 조치라고 밝혔다",
  "· 싱가포르는 감축이 18일간 일일 가스 수요의 2% 미만이라며 계약 위반 여부를 따지겠다고 했다",
  "· 양국은 산불 연무 갈등을 다룰 화재 태스크포스로 긴장 완화에 나섰다"]),
 facts=[
  "무엇이: 인도네시아가 10월 24일부터 싱가포르행 파이프라인 가스 수출을 하루 약 3,100만 표준입방피트(나투나 1,500만, 수마트라 1,600만) 줄였다 [사실]",
  "이유: 규제기관 SKK Migas는 바탐·빈탄·수마트라 발전용 국내 공급을 위한 것이라 했고, 에너지장관은 인도네시아를 존중하지 않는 나라에 수출 중단도 검토할 수 있다고 말했다 [사실]",
  "싱가포르: 에너지시장청은 감축이 18일간이며 일일 가스 수요의 2% 미만이라고 밝혔고, 정부는 계약 위반 여부를 확인하겠다고 했다 [사실]",
  "긴장 완화: 양국은 산불 연무 문제를 다룰 화재 태스크포스로 긴장을 누그러뜨리려 하고 있다 [제목]"],
 basis="verified",
 check="감축 시작일(10월 24일)·하루 3,100만 표준입방피트·싱가포르 반응은 검색 결과 요약으로 확인. 화재 태스크포스 내용은 제목 기준",
 src=[S("The Star", "https://www.thestar.com.my/business/business-news/2026/10/26/indonesia-begins-trimming-pipeline-gas-exports-to-singapore"),
      S("The Diplomat", "https://thediplomat.com/2026/10/indonesia-reduces-gas-supply-to-singapore-citing-domestic-energy-needs/"),
      S("Mothership", "https://mothership.sg/2026/10/indonesia-cut-gas-exports-sg/")],
 inds=["gas"], nodes=["gas/midstream"],
 vc=[V("gas", "midstream", "공급", "down", "실제", "인도네시아 싱가포르행 파이프라인 가스 수출 축소")],
 items=[
  I("싱가포르·인도네시아, 화재 태스크포스로 긴장 완화 모색", "블룸버그", "https://www.bloomberg.com/news/articles/2026-10-27/singapore-s-top-envoy-visits-indonesia-after-natural-gas-cuts",
    "싱가포르와 인도네시아가 화재 태스크포스를 꾸리면서 가스 수출 축소로 불거진 양국 긴장을 누그러뜨리려 하고 있다"),
  I("인도네시아가 싱가포르행 가스 수출을 줄이는 이유", "블룸버그", "https://www.bloomberg.com/news/articles/2026-10-27/why-indonesia-is-reducing-gas-exports-to-singapore",
    "인도네시아가 국내 발전 수요를 이유로 싱가포르행 가스 수출을 하루 3,100만 표준입방피트 줄이면서 공급 계약 이행 문제가 불거졌다")]))

R.append(dict(cid="G1-030", attachTo="n-rtr-0675",
 title="밀 흑해 프리미엄 소멸…러 해운 협상 시사에 7월 이후 최저·8주 연속 하락 1997년 이후 최장",
 one="\n".join([
  "밀 선물이 8주 연속 내린 데 이어 러시아의 흑해 해운 협상 시사로 흑해 위험 프리미엄까지 지웠다",
  "· 시카고 밀 선물은 8주 연속 하락해 1997년 이후 최장 약세를 이어갔고 23일까지 한 주에 4.7% 내렸다",
  "· 러시아가 흑해 곡물 해운 안전 제안을 검토한다고 밝히자 시카고 밀은 2% 내린 부셸당 6.125달러가 됐다",
  "· 이는 7월 9일 이후 최저이고 유로넥스트 12월물 제분용 밀도 2.7% 내린 톤당 227.75유로였다",
  "· 중국 구매자들은 호주산 카놀라 약 100만 톤을 톤당 약 695~705달러에 사들였다",
  "· 인도는 원당 무관세 수입 기한을 12월 31일까지 늘렸다"]),
 facts=[
  "무엇이: 러시아가 흑해 곡물 해운 안전 제안을 검토한다고 밝히자 밀값의 흑해 위험 프리미엄이 사라졌다 [사실]",
  "가격: 시카고 밀 최근월물은 23일까지 주간 4.7% 내리며 8주 연속 하락해 1997년 이후 최장을 기록했고, 26일에는 2% 내린 부셸당 6.125달러로 7월 9일 이후 최저였으며 유로넥스트 12월물은 2.7% 내린 227.75유로였다 [사실]",
  "배경·러시아 입장: 미국 수출 판매 부진과 호주·아르헨티나 수확도 하락 요인으로 꼽혔고, 알리모프 러시아 외무차관은 튀르키예 등과 접촉 중이지만 곡물협정 부활 전망은 아직 없다고 말했다 [사실]",
  "카놀라: 중국 국영·민간 구매자들이 관계 개선·관세 인하·가공 마진 개선 속에 2027년 초 도착분 호주산 카놀라 약 100만 톤을 톤당 약 695~705달러(C&F)에 샀다 [채널]",
  "설탕: 인도가 원당 무관세 수입 기한을 12월 31일로 연장했다 [제목]"],
 basis="verified",
 check="러시아 외무차관의 흑해 곡물 해운 안전 제안 검토 발언과 시카고 밀 2% 하락(부셸당 6.125달러, 7월 9일 이후 최저)·유로넥스트 2.7% 하락은 검색 결과 요약으로 확인",
 src=[S("UkrAgroConsult", "https://ukragroconsult.com/en/news/wheat-market-effectively-loses-black-sea-shipping-risk-premium/"),
      S("Daily Sabah", "https://www.dailysabah.com/world/europe/russia-reviewing-proposals-to-ensure-black-sea-grain-shipping-official")],
 inds=["agri"], nodes=[],
 vc=[V("agri", "grains", "가격", "down", "실제", "러 흑해 해운 협상 시사에 밀 7월 이후 최저")],
 added="블룸버그 1건 — 러시아의 흑해 곡물 해운 협상 시사로 밀 흑해 위험 프리미엄 소멸, 시카고 밀 6.125달러로 7월 9일 이후 최저 내용이 추가됨",
 items=[
  I("밀, 러시아 해운 협상 시사에 흑해 프리미엄 소멸", "블룸버그", "https://www.bloomberg.com/news/articles/2026-10-26/wheat-erases-black-sea-premium-as-russia-signals-shipping-talks",
    "러시아가 흑해 곡물 해운 협상 의사를 내비치면서 밀 선물이 흑해 위험 프리미엄을 모두 반납하고 7월 이후 최저로 내렸다")]))

R.append(dict(cid="G1-034", attachTo="",
 title="독일 정부 '재산 몰수 계획 저지 어려워'…베를린 주택 공유화에 연방 투자보호법으로 제동 추진",
 one="\n".join([
  "독일 연방정부가 베를린의 대형 임대주택 몰수(공유화) 계획을 막기 어렵다고 경고했다",
  "· 도브린트 내무장관은 시가 현금 보상 등 요건을 담은 연방 투자보호법으로 계획에 제동을 걸려 한다",
  "· 최대 임대업체 보노비아는 최대 80억 유로 타격 우려 속에 베를린 신규 주택사업을 멈췄다"]),
 facts=[
  "무엇이: 독일 정부가 재산 몰수 계획을 막기 어렵다고 경고했다 [제목]",
  "배경: 베를린은 기본법 15조를 근거로 대형 임대업체 주택 공유화를 추진하고 있고, 도브린트 내무장관은 다른 수단 소진 입증과 시가 현금 보상을 요구하는 연방 투자보호법으로 제동을 추진했다 [사실]",
  "비용: 베를린 계획은 약 160억 유로를 상정했지만 시가 매입 시 500억~600억 유로가 든다는 추정이 있다 [사실]",
  "업계: 보노비아는 최대 80억 유로 타격 가능성 속에 베를린 신규 주택사업을 멈췄고 계획이 위헌이라고 본다 [사실]"],
 basis="partial",
 check="베를린 주택 공유화 계획, 연방정부의 투자보호법 제동안, 보노비아 영향은 검색 결과 요약으로 확인. 블룸버그 기사의 '저지 어렵다' 경고 내용 자체는 확인 못 함",
 src=[S("The Local", "https://www.thelocal.de/20261026/germanys-interior-ministry-puts-forward-plan-to-block-housing-socialisation-in-berlin"),
      S("European Business Magazine", "https://europeanbusinessmagazine.com/germanys-landlord-faces-8bn-hit/")],
 inds=["realestate"], nodes=[],
 vc=[V("realestate", "develop", "공급", "down", "실제", "베를린 공유화 추진에 보노비아 신규 주택사업 중단")],
 items=[
  I("독일, 재산 몰수 계획 저지에 어려움 있다고 경고", "블룸버그", "https://www.bloomberg.com/news/articles/2026-10-26/germany-warns-of-difficulty-in-blocking-property-seizure-plans")]))

R.append(dict(cid="G1-040", attachTo="",
 title="엘리멘틀 파워, 최대 7.5억 달러 원전 개발 파트너십 예비합의…GE버노바 히타치 BWRX-300 활용",
 one="\n".join([
  "미국 원전 개발사 엘리멘틀 파워가 최대 7억 5,000만 달러 규모 원전 개발 파트너십 예비합의를 맺었다",
  "· 한국 DS투자파트너스 주도 컨소시엄과 맺은 합의로 삼성물산 건설부문이 전략 투자자 후보로 참여한다",
  "· 자금은 GE버노바 히타치 BWRX-300을 쓰는 오하이오 1.5GW 사업 등 최대 3개 사업의 투자결정 전 단계에 쓰인다"]),
 facts=[
  "무엇이: 엘리멘틀 파워가 DS투자파트너스 주도 컨소시엄과 최대 7억 5,000만 달러(7.5억 달러) 규모 원전 개발 파트너십 예비합의(의향서·조건 합의서)를 맺었다 [사실]",
  "기술: 계획된 사업에는 GE버노바 히타치 원자력의 BWRX-300 소형모듈원자로가 쓰이며 오하이오 1.5GW 사업이 포함된다 [사실]",
  "용도: 최대 3개 사업의 인허가·계통 연결·장납기 기자재 조달 등 최종투자결정 전 비용 일부를 댄다 [사실]",
  "단계: 최종 계약·규제 승인 전의 예비 단계로 최종투자결정이 아니며 구체 일정은 공개되지 않았다 [사실]"],
 basis="verified",
 check="7억 5,000만 달러 예비합의, DS투자파트너스·삼성물산 컨소시엄, 오하이오 BWRX-300 사업은 검색 결과 요약으로 확인",
 src=[S("OilPrice", "https://oilprice.com/Company-News/Elementl-Power-Eyes-750-Million-Deal-for-US-Nuclear-Projects.html"),
      S("POWER Magazine", "https://www.powermag.com/elementl-power-developing-ohio-smr-project-with-ge-vernova-hitachi-nuclear-energy/")],
 inds=["uranium"], nodes=["uranium/build"],
 vc=[V("uranium", "build", "수요", "up", "예상", "BWRX-300 SMR 사업에 최대 7.5억 달러 개발자금 예비합의")],
 items=[
  I("엘리멘틀 파워, BWRX-300 활용 7.5억 달러 원전 개발 예비합의", TG+"미국 주식 인사이더", "https://t.me/insidertracking/67430")]))

R.append(dict(cid="G1-046", attachTo="",
 title="웨빌드·오데브레시트, 아프리카 구리 철도 건설 유력…앙골라 로비토 회랑 830km 구간",
 one="\n".join([
  "이탈리아 웨빌드와 브라질 오데브레시트가 아프리카 핵심 구리 철도 건설을 맡을 유력 후보로 떠올랐다",
  "· 두 회사가 속한 우선협상 컨소시엄은 앙골라 로비토 회랑 철도 830km 구간을 짓게 된다",
  "· 이 구간은 중앙아프리카 구리·코발트 광산 지대와 앙골라 대서양 연안을 잇는다"]),
 facts=[
  "무엇이: 웨빌드와 오데브레시트가 아프리카 핵심 구리 철도 건설의 유력 후보가 됐다 [제목]",
  "사업: 두 회사가 포함된 우선협상 컨소시엄이 로비토 회랑 철도 830km 구간을 맡아 중앙아프리카 구리·코발트 광산 지대와 앙골라 대서양 연안을 잇는다 [사실]",
  "단계: 계약 확정 보도는 아직 없고 우선협상 대상 단계다 [사실]",
  "시장: 웨빌드 주가는 0.41% 오른 1.95유로였다 [사실]"],
 basis="verified",
 check="로비토 회랑 830km 구간 우선협상 컨소시엄 참여와 웨빌드 주가는 검색 결과 요약으로 확인. 최종 계약은 확인 못 함",
 src=[S("Mining Weekly", "https://www.miningweekly.com/?al_id=3371681"),
      S("Newsquawk", "https://newsquawk.com/headlines/newsquawk-daily-european-equity-opening-news---27th-october-2026")],
 inds=["industrial"], nodes=[],
 vc=[V("industrial", "construction", "수요", "up", "예상", "로비토 회랑 구리 철도 830km 구간 우선협상 선정")],
 items=[
  I("웨빌드·오데브레시트, 아프리카 핵심 구리 철도 건설 유력", "블룸버그", "https://www.bloomberg.com/news/articles/2026-10-27/webuild-odebrecht-in-line-to-build-key-african-copper-rail-line")]))

R.append(dict(cid="G1-052", attachTo="",
 title="마루티 스즈키 분기 순이익 27% 감소…원자재·부품비 48%↑에 판매 최대에도 마진 압박",
 one="\n".join([
  "인도 최대 완성차업체 마루티 스즈키의 7~9월 분기 순이익이 원가 부담에 27% 줄었다",
  "· 단독 순이익은 241억 4,900만 루피로 원자재·부품 비용이 48% 늘어난 탓이 컸다",
  "· 판매량은 69만 6,654대로 26.5% 늘어 분기 최대였고 매출도 약 26% 늘었다"]),
 facts=[
  "무엇이: 마루티 스즈키의 2027회계연도 2분기(7~9월) 단독 순이익이 241억 4,900만 루피로 전년보다 27% 줄었다 [사실]",
  "원인: 원자재·부품 비용이 3,748억 8,400만 루피로 48% 늘었고 투자자산 평가손실도 부담이 됐으며, 서아시아 긴장에 따른 공급망 문제가 원가 압박 배경으로 꼽혔다 [사실]",
  "판매: 판매량은 69만 6,654대로 26.5% 늘었고 매출은 5,335억 5,500만 루피로 약 26% 늘었다 [사실]",
  "연결: 연결 순이익은 26.4% 줄어든 246억 6,100만 루피였고 영업이익(EBIT)은 17.1% 줄었다 [사실]"],
 basis="verified",
 check="단독 순이익 27% 감소(2,414.9크로르 루피)·원자재비 48% 증가·판매 69만 6,654대는 검색 결과 요약으로 확인",
 src=[S("Autocar Professional", "https://www.autocarpro.in/news/maruti-suzuki-q2-net-profit-drops-27-percent-to-rs-2415-crore-amid-input-cost-inflation-135496"),
      S("Business Today", "https://www.businesstoday.in/markets/stocks/story/maruti-suzuki-q2-profit-falls-26-to-rs-2466-crore-revenue-rises-26-563972-2026-10-27")],
 inds=["auto"], nodes=[],
 vc=[V("auto", "oem", "가격", "down", "실제", "원가 48% 상승에 마루티 순이익 27% 감소")],
 items=[
  I("마루티 스즈키, 원가 부담에 이익 27% 감소", "블룸버그", "https://www.bloomberg.com/news/articles/2026-10-27/maruti-suzuki-profit-misses-estimate-as-costs-squeeze-margins")]))

R.append(dict(cid="G2-003", attachTo="",
 title="AI 거래 흔들…앤트로픽 상장 신청에 반등 뒤 탄력 둔화·골드만 'TMT 200억 달러 이탈은 디레버리징'",
 one="\n".join([
  "기술주 급락 뒤 AI 관련주가 앤트로픽의 상장 신청(S-1)에 반등했지만 곧 탄력이 꺾였다",
  "· 시타델증권 샤는 경제와 증시가 AI 거래에 묶여 실수할 여지가 없다고 경고했다",
  "· 골드만삭스 파스콰렐로는 기술주 급락이 AI 거래에 의문을 던졌다고 짚었다",
  "· 앤트로픽 상장 서류 제출로 AI주가 반등해 나스닥이 약 0.9% 올랐지만 이후 랠리가 힘을 잃었다",
  "· 골드만 트레이딩 데스크는 TMT에서 200억 달러가 빠진 급락을 헤지펀드 디레버리징으로 분석했다",
  "· 오픈라우터 기준 토큰 수요는 20개월 새 250배 늘었지만 지출 비중은 27%에 그쳐 약세론 근거가 됐다"]),
 facts=[
  "무엇이: 앤트로픽이 상장 서류를 내자 AI 관련주가 반등해 나스닥이 약 0.9% 올랐다 [사실]",
  "신중론: 시타델증권 샤는 AI 수익성 의문·데이터센터 정치적 반발·금융비용 상승이 겹쳐 AI 거래에 실수할 여지가 없다고 봤다 [사실]",
  "탄력 둔화: 골드만 파스콰렐로는 기술주 급락이 AI 거래에 의문을 던졌다고 했고, 앤트로픽 상장 신청 뒤 AI 거래가 동력을 잃기 시작했다 [제목]",
  "골드만 데스크: TMT 200억 달러 이탈을 디레버리징으로 보고 모멘텀 바스켓이 7.8% 내릴 때 나스닥은 0.8% 내렸다며, 선별 매수 순서로 전력·하이퍼스케일 클라우드·추론과 보안을 들고 11월 6일 전 MS·구글·아마존 설비투자 가이던스 하향 여부를 변수로 꼽았다 [채널]",
  "약세론 근거: 오픈라우터 기준 토큰 수요는 20개월 새 250배 늘었지만 트래픽 72%가 싼 오픈소스 모델로 몰려 지출 비중은 27%에 그쳤고, 토큰 가격은 분기마다 47% 내린 반면 GPU 임대료는 160% 올랐다 [채널]"],
 basis="partial",
 check="시타델 샤의 경고와 앤트로픽 상장 신청 뒤 AI주 반등(나스닥 약 0.9% 상승)은 검색 결과 요약으로 확인. 골드만 파스콰렐로 발언 내용·데스크 분석·오픈라우터 수치는 확인 못 함",
 src=[S("investingLive", "https://investinglive.com/stock-market-update/citadel-securities-warns-ai-trade-has-little-margin-for-error-as-three-risks-converge/"),
      S("NPR", "https://www.npr.org/2026/10/26/nx-s1-6014772/anthropic-ai-ipo-could-break-records")],
 inds=["macro", "tech"], nodes=["macro/semis"],
 vc=[V("macro", "semis", "가격", "mixed", "실제", "앤트로픽 상장 신청에 AI주 반등 뒤 탄력 둔화"),
     V("tech", "ai", "가격", "down", "실제", "토큰 가격 분기마다 47% 하락")],
 items=[
  I("시타델증권 샤 'AI 거래에 실수할 여지 없다'", "블룸버그", "https://www.bloomberg.com/news/articles/2026-10-26/citadel-securities-shah-says-ai-trade-has-no-margin-for-error",
    "시타델증권 샤가 경제와 증시가 AI 거래에 깊이 얽혀 있다고 짚으면서 AI 수익성·금융비용 위험이 겹친 시장에 여유가 없다고 경고했다"),
  I("골드만 파스콰렐로 '기술주 급락이 AI 거래에 의문 던져'", "블룸버그", "https://www.bloomberg.com/news/articles/2026-10-26/goldman-s-pasquariello-says-tech-rout-casts-doubt-on-ai-trade",
    "골드만삭스 파스콰렐로가 기술주 급락을 근거로 AI 거래의 지속성에 의문을 제기하면서 투자자 신중론을 키웠다 (제목 기준)"),
  I("앤트로픽 상장 신청에 자금 우려 완화…AI 거래 반등", "블룸버그", "https://www.bloomberg.com/news/articles/2026-10-27/asian-chip-stocks-rise-as-anthropic-ipo-filing-rekindles-ai-bets",
    "앤트로픽의 상장 신청이 AI 기업 자금 조달 불안을 덜면서 아시아 반도체주 등 AI 관련주가 이틀간의 매도를 딛고 반등했다"),
  I("토큰 소비 72%가 지출 비중 27%…AI 강세론·약세론 쟁점", TG+"하나증권 중국전략", "https://t.me/HANAchina/71077",
    "오픈라우터 데이터에서 토큰 수요가 250배 늘었지만 지출 비중은 27%에 그치면서 골드만이 AI 자본 순환 구조의 취약성을 짚었다"),
  I("앤트로픽 상장 신청으로 기술주 랠리 하루 더 연장", "블룸버그", "https://www.bloomberg.com/news/newsletters/2026-10-27/anthropic-s-ipo-filing-extends-tech-rally",
    "앤트로픽의 상장 서류 제출이 기술주 랠리를 하루 더 이어가게 하면서 AI 관련주 매수세가 다시 살아났다 (제목 기준)"),
  I("골드만 데스크 'TMT 200억 달러 이탈은 디레버리징'", TG+"하나증권 중국전략", "https://t.me/HANAchina/71092",
    "골드만삭스 트레이딩 데스크가 TMT 200억 달러 이탈을 수요 둔화가 아닌 헤지펀드 디레버리징으로 분석하면서 AI 혼잡 포지션이 크게 정리됐다고 봤다"),
  I("앤트로픽 상장 신청 뒤 AI 거래 탄력 둔화하기 시작", "블룸버그", "https://www.bloomberg.com/news/newsletters/2026-10-27/ai-trade-starts-to-lose-momentum-after-anthropic-filing",
    "앤트로픽 상장 신청으로 살아났던 AI 거래가 동력을 잃기 시작하면서 반등의 지속성에 다시 의문이 생겼다 (제목 기준)")]))

R.append(dict(cid="G2-005", attachTo="",
 title="룰라 재선 충격…보베스파 장중 17.3% 폭락·헤알 하루 8% 급락·60억 달러 주식 발행 무산",
 one="\n".join([
  "룰라 대통령이 결선에서 51.8%로 예상 밖 재선에 성공하자 브라질 주식·통화·채권이 동반 급락했다",
  "· 보베스파지수는 장중 최대 17.3% 떨어졌고 B3 거래소는 2020년 3월 이후 처음 30분간 거래를 멈췄다",
  "· 채널은 브라질 국내 요인에 따른 하락으로는 36년 만의 최대 낙폭이라고 전했다",
  "· 헤알은 하루 약 8% 떨어져 1999년 이후 최대 일일 낙폭을 기록했다",
  "· 재무부는 예정된 국채 입찰을 취소했고 은행들이 준비하던 60억 달러 규모 주식 발행이 무산됐다",
  "· 시장은 재정 확대 공약 부담과 재무장관 인선, 2027년 예산 방향을 주시하고 있다"]),
 facts=[
  "무엇이: 룰라가 10월 결선에서 51.8%(51.79%)를 얻어 플라비우 보우소나루(48.2%)를 꺾고 재선했다 [사실]",
  "주식: 보베스파는 장중 17.34% 급락한 뒤 13.88% 내린 17만 6,608로 마감했고 B3는 30분 서킷브레이커를 발동했으며, 채널은 국내 요인 기준 1990년 이후 36년 만 최대 낙폭이라고 전했다 [사실]",
  "헤알·국채: 헤알은 달러 대비 약 8% 내려 1999년 이후 최대 일일 낙폭을 기록했고(장중 약 12% 하락 전언), 국채 가격도 떨어져 재무부가 국채 입찰을 취소했다 [채널]",
  "자본시장: 룰라 승리로 은행들이 준비하던 60억 달러 규모 주식 발행이 무산됐다 [제목]",
  "종목·전망: 페트로브라스 8%, XP 48%, 누홀딩스 17%가 내렸고, 시장은 재무장관 인선과 2027년 예산 조정, 보우소나루의 불복을 주시한다 [채널]"],
 basis="verified",
 check="결선 득표율(51.79% 대 48.21%), 보베스파 장중 17.34%·종가 13.88% 하락, 30분 서킷브레이커, 달러·헤알 8.79% 상승은 검색 결과 요약으로 확인. 36년 만 최대·1999년 이후 최대·60억 달러 주식 발행 무산은 확인 못 함",
 src=[S("Rio Times", "https://www.riotimesonline.com/brazil-markets-ibovespa-real-monday-october-26-2026/"),
      S("Al Jazeera", "https://www.aljazeera.com/economy/2026/10/26/brazils-real-sinks-after-lulas-re-election-victory")],
 inds=["macro", "fin"], nodes=["macro/fx", "macro/fiscal"],
 vc=[V("macro", "fx", "가격", "down", "실제", "룰라 재선에 헤알 하루 약 8% 급락"),
     V("fin", "ib", "수요", "down", "실제", "룰라 승리에 브라질 60억 달러 주식 발행 무산")],
 items=[
  I("룰라 승리에 60억 달러 주식 발행 무산…은행들 휘청", "블룸버그", "https://www.bloomberg.com/news/articles/2026-10-26/shock-lula-win-derails-6-billion-in-equity-sales-as-banks-reel",
    "룰라의 예상 밖 승리로 브라질 증시가 흔들리면서 은행들이 주관하던 60억 달러 규모 주식 발행이 무산됐다 (제목 기준)"),
  I("룰라 재선에 보베스파 장중 17.34% 폭락, 거래 중단 발동", TG+"미국 주식 인사이더", "https://t.me/insidertracking/67414",
    "룰라 재선 직후 보베스파가 장중 17.34% 급락하고 시총 8,900억 헤알 이상이 사라지면서 B3가 2020년 이후 첫 거래 중단을 발동했다"),
  I("룰라의 보우소나루 상대 승리, 브라질 금융 앞날에 우려", "블룸버그", "https://www.bloomberg.com/news/articles/2026-10-26/lula-s-win-over-bolsonaro-in-brazil-election-stokes-fears-over-financial-future",
    "룰라가 보우소나루를 꺾고 재선하면서 재정 확대 우려로 브라질 금융시장의 앞날에 대한 불안이 커졌다 (제목 기준)"),
  I("룰라 51.8% 재선, 헤알 1999년 이후 최대 낙폭·국채 동반 하락", TG+"상상인 김진범", "https://t.me/PipeBeom/6872",
    "룰라가 결선에서 51.8%로 재선하면서 헤알이 약 8% 떨어져 1999년 이후 최대 일일 낙폭을 기록했고 국채 조달 비용도 올랐다"),
  I("보베스파 하락, 국내 요인 기준 36년 만에 최대", TG+"미국 주식 인사이더", "https://t.me/insidertracking/67442",
    "브라질 국내 요인에 따른 주가 하락으로는 1990년 3월 이후 36년 만에 가장 큰 낙폭이 나오면서 충격의 크기가 부각됐다")]))

R.append(dict(cid="G2-008", attachTo="",
 title="중국 기술주 급락…STAR50 4개월 새 40%↓·시총 4,800억 달러 증발·국가대표 자금 의존 드러나",
 one="\n".join([
  "중국 AI·반도체주가 무너지면서 STAR50지수가 4개월이 채 안 돼 40% 떨어졌다",
  "· STAR50 하락으로 시가총액 약 4,800억 달러가 증발했다",
  "· 마감 직전 급락은 국가대표 자금의 떠받치기에 기댄 시장 구조를 드러냈다",
  "· 중국 주식형 펀드 포지션은 2년 만에 가장 낮아졌다",
  "· CICC는 중국 클라우드 기업 ROIC를 11.9%로 추산해 미국 19.9%를 크게 밑돈다고 봤다"]),
 facts=[
  "무엇이: 중국 AI·반도체 대표 기업으로 구성된 STAR50지수가 4개월이 채 안 돼 40% 떨어져 시총 약 4,800억 달러가 사라졌다 [사실]",
  "수급: 상하이종합지수가 1.33% 내리고 4,900개 넘는 종목이 하락한 날 마감 직전 급락이 국가대표 자금 의존을 드러냈고, 국가대표 자금은 한 주에 ETF 9개로 1,287억 위안을 넣었다 [사실]",
  "포지션: 중국 주식형 펀드 포지션은 2년래 최저로 수급 조정은 마무리 국면이지만 투자심리는 신중하다 [채널]",
  "클라우드 수익성: CICC는 중국 주요 클라우드 기업 가중평균 ROIC를 11.9%로 추산해 미국 19.9%를 밑돌았고 2분기 잉여현금흐름이 모두 마이너스로 돌아섰다고 봤다 [채널]",
  "원인: 높은 밸류에이션, 세금 부담, 데이터센터의 중국산 장비 사용 금지 가능성이 꼽혔고 STAR50은 여전히 과거 이익의 약 100배에 거래된다 [사실]"],
 basis="verified",
 check="STAR50 40% 하락·시총 4,800억 달러 증발, 마감 직전 급락과 국가대표 자금 의존은 검색 결과 요약으로 확인. 주식형 펀드 포지션·CICC ROIC는 확인 못 함",
 src=[S("Geo News", "https://www.geo.tv/latest/688414-ai-bubble-bursts-in-china-as-star50-index-plunges-40-erasing-480-billion"),
      S("IBTimes Australia", "https://www.ibtimes.com.au/china-stocks-tech-selloff-asian-markets-rally-1877459")],
 inds=["fin", "macro"], nodes=["macro/semis"],
 vc=[V("fin", "markets", "가격", "down", "실제", "STAR50 4개월 새 40% 하락·시총 4,800억 달러 증발")],
 items=[
  I("중국 AI 버블 이미 붕괴, STAR50 4개월 새 40% 하락", TG+"카이에 de market", "https://t.me/cahier_de_market/11126",
    "중국 AI·반도체주가 고평가와 수출 제한 우려로 무너지면서 STAR50이 40% 떨어지고 시총 약 4,800억 달러가 사라졌다"),
  I("CICC, 중국 클라우드 ROIC 11.9%로 미국 19.9% 하회", TG+"하나증권 중국전략", "https://t.me/HANAchina/71078",
    "CICC가 중국 클라우드 기업 ROIC를 11.9%로 추산하면서 AI 투자가 미국보다 빨리 중국 내수를 위축시킬 수 있다고 분석했다"),
  I("중국 주식형 펀드 포지션 2년래 최저…투심은 신중", TG+"하나증권 중국전략", "https://t.me/HANAchina/71083",
    "중국 주식형 펀드 포지션이 2년래 최저로 내려가면서 수급 조정은 마무리 국면이지만 투자심리는 여전히 신중한 상태다"),
  I("중국 증시 마감 직전 급락, 국가대표 자금 의존 드러내", "블룸버그", "https://www.bloomberg.com/news/articles/2026-10-27/chinese-stocks-final-hour-slide-shows-reliance-on-national-team",
    "중국 증시가 마감 한 시간 동안 급락하면서 시장이 국가대표 자금의 지지에 기대고 있다는 점이 드러났다")]))

R.append(dict(cid="G2-014", attachTo="",
 title="암호화폐 업계 제도권 진입…리플 美 국가신탁은행 최종 인가·갤럭시 실적 호조·네덜란드 이탈 조짐",
 one="\n".join([
  "리플이 미국 국가신탁은행 최종 인가를 받는 등 암호화폐 기업의 제도권 진입과 상장 준비가 이어졌다",
  "· 리플은 통화감독청 최종 승인으로 RLUSD 준비금 관리와 디지털자산 수탁을 맡는 신탁은행을 연다",
  "· 갤럭시디지털은 3분기 매출이 예상을 웃돌아 주가가 올랐고 순이익은 3억 2,300만 달러였다",
  "· 결제 핀테크 레드닷페이는 연내 비공개 상장 신청을 준비하는 것으로 알려졌다",
  "· 네덜란드 투자자들은 부유세 예외에서 빠진 암호화폐를 떠날 조짐을 보이고 있다"]),
 facts=[
  "무엇이: 리플이 10월 26일 미 통화감독청(OCC)에서 리플 국가신탁은행 최종 인가를 받았고, 이 은행은 예금·대출 없이 RLUSD 준비금 관리와 디지털자산 수탁을 맡는다 [사실]",
  "갤럭시: 3분기 운영 수익·손익 합계는 87억 달러, 순이익은 3억 2,300만 달러, 조정 EBITDA는 4억 5,500만 달러였다 [사실]",
  "상장: 레드닷페이가 연내 비공개 IPO 신청을 준비하는 것으로 알려졌다 [제목]",
  "네덜란드: 부유세 개편에서 암호화폐가 예외 대상에서 빠지자 투자자 이탈 조짐이 보인다 [제목]"],
 basis="partial",
 check="리플 OCC 최종 인가는 검색 결과 요약, 갤럭시 3분기 실적은 SEC 제출 실적 발표문을 열어 확인. 갤럭시 매출의 예상치 상회 여부와 레드닷페이·네덜란드 건은 확인 못 함",
 src=[S("Cointelegraph", "https://cointelegraph.com/news/ripple-wins-final-us-approval-for-national-trust-bank"),
      S("SEC 갤럭시디지털 실적 발표문", "https://www.sec.gov/Archives/edgar/data/0001859392/000185939226000108/glxy-20260930xpressrelease.htm")],
 inds=["fin"], nodes=[],
 vc=[V("fin", "payments", "공급", "up", "실제", "리플 미 국가신탁은행 최종 인가")],
 items=[
  I("결제 핀테크 레드닷페이, 연내 비공개 IPO 신청 준비", "블룸버그", "https://www.bloomberg.com/news/articles/2026-10-26/redotpay-said-to-prepare-confidential-ipo-filing-by-year-end",
    "결제 핀테크 레드닷페이가 연내 비공개 상장 신청을 준비하면서 암호화폐 결제 기업의 상장 행렬에 합류하려 하고 있다 (제목 기준)"),
  I("네덜란드 투자자, 부유세 예외 제외에 암호화폐 이탈 조짐", "블룸버그", "https://www.bloomberg.com/news/articles/2026-10-26/dutch-investors-poised-to-flee-crypto-over-wealth-tax-carveout",
    "네덜란드가 부유세 개편에서 암호화폐를 예외 대상에서 빼면서 현지 투자자들이 암호화폐 자산을 떠날 채비를 하고 있다 (제목 기준)"),
  I("리플, 미 통화감독청서 국가신탁은행 최종 인가 획득", "블룸버그", "https://www.bloomberg.com/news/articles/2026-10-27/ripple-gets-final-us-approval-for-national-trust-bank",
    "리플이 미 통화감독청 최종 인가를 받으면서 RLUSD 준비금 관리와 디지털자산 수탁을 맡는 국가신탁은행을 열 수 있게 됐다"),
  I("노보그라츠의 갤럭시, 매출 예상 상회에 주가 상승", "블룸버그", "https://www.bloomberg.com/news/articles/2026-10-27/novogratz-s-galaxy-tops-revenue-estimates-shares-rise",
    "갤럭시디지털이 3분기 순이익 3억 2,300만 달러를 내고 매출이 예상을 웃돌면서 주가가 올랐다")]))

R.append(dict(cid="G2-017", attachTo="",
 title="TSMC, CoWoS 가격 최대 20% 인상 추진·장비 납기 8개월…엔비디아 광학 인터포저 공개",
 one="\n".join([
  "AI 칩 첨단 패키징 공급이 부족해지면서 TSMC가 CoWoS 가격을 최대 20% 올리는 방안을 추진하고 있다",
  "· 인상 폭은 10~20%로 전해졌고 AI GPU·서버 CPU·맞춤형 ASIC 패키징 수요가 함께 늘었다",
  "· 반도체 장비 납기는 3~6개월에서 6~8개월로 늘어났다",
  "· 리소그래피·다이 본딩 등 병목 공정과 부품 제약으로 공급 확대 속도에는 한계가 있다",
  "· 엔비디아는 연산 칩과 광학 엔진을 한 인터포저에 올린 광학 인터포저(OOI) 시제품을 공개했다",
  "· 인터포저 사용량이 크게 늘 수 있다는 분석에 UMC와 PSMC가 주목받고 있다"]),
 facts=[
  "무엇이: TSMC가 CoWoS 패키징 가격을 10~20% 올리는 방안을 추진한다고 대만 공상시보가 보도했고 TSMC는 확인하지 않았다 [사실]",
  "납기: AI 반도체 패키징 수요가 공급을 넘어서며 장비 납기가 3~6개월에서 6~8개월로 늘었고, TSMC는 올해 장비 가격 재협상을 요구하지 않았다 [사실]",
  "영향: 한 분석은 가격 인상이 AI 가속기 부품원가를 약 2~4.5% 높일 것으로 추정했다 [사실]",
  "광학 인터포저: 엔비디아가 광학 인터포저(OOI) 시제품을 공개해 인터포저 면적·사용량이 크게 늘 수 있다는 분석 속에 UMC·PSMC가 주목받았다 [채널]"],
 basis="verified",
 check="CoWoS 10~20% 인상 추진 보도와 장비 납기 6~8개월은 검색 결과 요약으로 확인. 엔비디아 OOI·UMC·PSMC 관련 내용은 확인 못 함",
 src=[S("Wccftech", "https://wccftech.com/tsmc-cowos-price-hike-20-percent-ai-gpu-asic-demand/"),
      S("TipRanks", "https://www.tipranks.com/news/tsmcs-ai-chip-packaging-prices-could-jump-20")],
 inds=["macro", "semis"], nodes=["macro/semis"],
 vc=[V("semis", "packaging", "가격", "up", "예상", "TSMC CoWoS 가격 최대 20% 인상 추진"),
     V("semis", "equipment", "공급", "down", "실제", "반도체 장비 납기 6~8개월로 늘어")],
 items=[
  I("엔비디아 광학 인터포저(OOI) 공개…UMC·PSMC 주목", TG+"하나증권 중국전략", "https://t.me/HANAchina/71053",
    "엔비디아가 연산 칩과 광학 엔진을 한 인터포저에 올린 OOI 시제품을 공개하면서 인터포저 수요 기대에 UMC·PSMC가 주목받았다"),
  I("TSMC, CoWoS 가격 최대 20% 인상 추진…공급 부족 심화", TG+"하나증권 중국전략", "https://t.me/HANAchina/71056",
    "TSMC가 AI GPU·ASIC 패키징 수요 급증에 CoWoS 가격을 10~20% 올릴 전망이면서 장비 납기도 6~8개월로 늘어났다"),
  I("TSMC, CoWoS 추가 20% 인상 계획…장비 납기 최대 8개월", TG+"미국 주식 인사이더", "https://t.me/insidertracking/67472",
    "TSMC가 CoWoS 가격을 20% 더 올릴 계획으로 알려지면서 가격 결정력은 강해지고 AI 반도체 생산 확대 속도는 제약받을 수 있다")]))

R.append(dict(cid="G2-020", attachTo="n-rtr-0653",
 title="연준 10월 동결 확률 FedWatch 90%·칼시 93%…이코노미스트 100명 전원 12월 인상 전망·워시 소통 시험대",
 one="\n".join([
  "연준이 10월 27~28일 회의에서 금리를 동결하고 12월에 다시 올릴 것이라는 전망이 굳어졌다",
  "· 로이터 조사에서 100명 중 94명이 10월 3.75~4.00% 동결을, 100명 전원이 12월 인상을 예상했다",
  "· 약 60%는 금리 정점을 4.00~4.25%로 봤고 물가는 2028년 전에 목표로 돌아오기 어렵다고 봤다",
  "· CME FedWatch는 이번 주 동결 확률을 90%, 예측시장 칼시는 93%로 집계했다",
  "· 선제 지침을 거부해 온 워시 의장이 동결 논리를 설명하며 12월 인상 여지를 남길지가 시험대에 올랐다",
  "· 9월 FOMC 점도표와 10월 9일 기준 OIS 금리 선도곡선 사이의 괴리도 지적됐다 (채널 전언)"]),
 facts=[
  "무엇이: 10월 16~20일 로이터 조사에서 이코노미스트 100명 중 94명이 10월 27~28일 회의의 3.75~4.00% 동결을, 100명 전원이 12월 인상을 예상했다 [사실]",
  "정점·물가: 약 60%는 금리 정점을 4.00~4.25%로 봤고 92명 중 38명은 최소 두 차례 추가 인상을 예상했으며, 연준 선호 물가지표는 2028년 이전 목표 복귀가 어렵다고 봤다 [사실]",
  "시장 확률: CME FedWatch는 이번 주 동결 확률을 90%, 예측시장 칼시는 93%로 집계했다 [채널]",
  "워시 시험대: 인플레이션이 악화하는 가운데 선제 지침을 거부해 온 워시 의장이 동결 논리를 설명하면서 인플레 대응 신뢰를 지키고 12월 인상 여지를 남길지가 관건으로 꼽혔다 [채널]",
  "변수·괴리: 블룸버그는 10월 결정이 AI·인플레이션·전쟁 변수에 직면했다고 보도했고, 9월 FOMC 점도표와 10월 9일 기준 OIS 금리 선도곡선 가격이 어긋나 있다는 지적도 나왔다 [채널]"],
 basis="channel",
 check="이번 회차 글(FedWatch 90%·칼시 93%·워시 소통 시험대)은 검색으로 확인하지 않음. 기존 문서의 로이터 조사 수치는 기존 근거 유지",
 src=[],
 inds=["macro"], nodes=["macro/cb"],
 vc=[V("macro", "cb", "가격", "up", "예상", "10월 동결 확률 90% 넘고 12월 인상 전망 우세")],
 fed=[
  {"k": "Warsh", "who": "케빈 워시", "role": "의장", "kind": "관련 뉴스", "stance": "",
   "t": "FedWatch 동결 확률 90% 속에 워시 의장의 동결 논리 설명이 시험대에 올랐다", "d": D, "u": "https://t.me/HANAchina/71046"},
  {"k": "", "who": "FOMC", "role": "연방공개시장위원회", "kind": "관련 뉴스", "stance": "",
   "t": "예측시장 칼시에서 10월 금리 동결 확률이 93%로 집계됐다", "d": D, "u": "https://t.me/insidertracking/67457"}],
 added="텔레그램 2건 — FedWatch 이번 주 동결 확률 90%·칼시 93%, 워시 의장의 동결 논리 설명과 12월 인상 여지 시험대 내용이 추가됨",
 items=[
  I("연준 10월 회의 전망: 동결 유력, 워시 소통 능력 시험대", TG+"하나증권 중국전략", "https://t.me/HANAchina/71046",
    "FedWatch가 이번 주 동결 확률을 90%로 보면서 선제 지침을 거부해 온 워시 의장이 12월 인상 여지를 어떻게 남길지가 관심사로 떠올랐다"),
  I("예측시장 칼시, 연준 10월 금리 동결 확률 93% 집계", TG+"미국 주식 인사이더", "https://t.me/insidertracking/67457",
    "예측시장 칼시에서 연준의 10월 기준금리 동결 확률이 93%로 집계되면서 이번 주 동결 전망이 한층 굳어졌다")]))

R.append(dict(cid="G2-026", attachTo="n-bbg-0687",
 title="인도네시아 MSCI 충격 확산…10년물 국채금리 4년 최고·회사채 발행 보류·회사채 위험지표 6년 최고",
 one="\n".join([
  "MSCI 지위 하향 우려가 인도네시아 주식에서 국채·회사채 시장으로 번지고 있다",
  "· 회사채 위험 프리미엄은 6년 만에 최고로 올랐고 MSCI 여파로 회사채 발행이 보류됐다",
  "· 10년물 국채 금리는 MSCI 위험과 유가 부담에 4년 만에 최고로 올랐다",
  "· 10년물 금리는 10월 19일 7.16%에서 26일 7.45%로 뛰었다",
  "· 인도네시아중앙은행은 금리 동결·인상·인하를 섞은 정책 조합에 논리가 있다고 밝혔다"]),
 facts=[
  "무엇이: MSCI 위험과 유가 부담에 인도네시아 10년물 국채 금리가 4년 최고로 올랐고 MSCI 여파로 회사채 발행이 보류됐다 [제목]",
  "금리 수준: 10년물 금리는 10월 19일 7.16%에서 23일 7.44%, 26일 7.45%로 올랐고 미국채와의 스프레드는 219.4bp에서 228.6bp로 벌어졌다 [사실]",
  "회사채·배경: MSCI가 인도네시아를 신흥시장에서 단독 시장으로 재분류하는 안을 내놓은 뒤 회사채 위험 지표가 6년 최고로 올랐다 [사실]",
  "중앙은행: 인도네시아중앙은행은 동결·인상·인하가 뒤섞인 정책 조합에 논리가 있다고 밝혔다 [제목]",
  "전망: MUFG는 연말까지 기준금리 6.25% 인상을, 골드만삭스는 2026년 4분기와 2027년 1분기 25bp씩 두 차례 인상을 예상했다 [사실]"],
 basis="partial",
 check="10년물 금리 7.16%→7.45% 상승은 검색 결과 요약(Trading Economics)으로 확인. '4년 최고' 여부와 회사채 발행 보류는 확인 못 함",
 src=[S("Trading Economics", "https://tradingeconomics.com/indonesia/government-bond-yield")],
 inds=["macro", "fin"], nodes=["macro/rates"],
 vc=[V("macro", "rates", "가격", "up", "실제", "MSCI 위험·유가에 인니 10년물 금리 4년 최고"),
     V("fin", "markets", "공급", "down", "실제", "MSCI 여파로 인니 회사채 발행 보류")],
 added="블룸버그 2건 — 10년물 국채 금리 4년 최고(MSCI 위험·유가), MSCI 여파로 회사채 발행 보류 내용이 추가됨",
 items=[
  I("MSCI 여파 확산, 인도네시아 회사채 발행 보류", "블룸버그", "https://www.bloomberg.com/news/articles/2026-10-27/msci-indonesian-corporate-bond-sale-kb-bank-moodys-ratings-fitch-prabowo",
    "MSCI 지위 하향 우려가 회사채 시장까지 번지면서 인도네시아 기업의 회사채 발행 계획이 보류됐다 (제목 기준)"),
  I("인도네시아 국채 금리 4년 최고…MSCI 위험·유가 부담", "블룸버그", "https://www.bloomberg.com/news/articles/2026-10-27/indonesia-10-year-yield-at-four-year-high-on-msci-risk-oil",
    "MSCI 위험과 유가 부담이 겹치면서 인도네시아 10년물 국채 금리가 4년 만에 최고로 올라 정부 조달 비용이 커졌다")]))

R.append(dict(cid="G2-034", attachTo="n-bbg-0680",
 title="캄브리콘 회장 '2027년 100만 개 출하설 소통한 적 없다'…1~3분기 매출 95억 위안·3분기 104.5%↑",
 one="\n".join([
  "중국 AI 칩업체 캄브리콘의 매출이 두 배로 늘었지만 예상에 못 미친 가운데 회장이 출하 소문을 부인했다",
  "· 3분기 매출은 35억 3,100만 위안으로 104.5%, 순이익은 14억 400만 위안으로 147.7% 늘었다",
  "· 1~3분기 매출은 95억 2,600만 위안으로 106.76% 늘었다",
  "· 블룸버그는 매출 부진이 HBM 부족 등 생산 제약을 드러낸 신호라고 봤다",
  "· 천톈스 회장은 2027년 칩 출하 100만 개 초과설에 대해 회사가 소통한 적이 없다고 밝혔다",
  "· 재고는 116억 6,500만 위안으로 늘었고 회장은 주로 전략 비축 때문이라고 설명했다"]),
 facts=[
  "무엇이: 캄브리콘의 3분기 매출은 35억 3,100만 위안으로 전년 대비 104.47%, 지배주주 순이익은 14억 400만 위안으로 147.74% 늘었지만 시장 예상에 못 미쳐 생산 제약 신호로 읽혔다 [사실]",
  "누적: 1~3분기 매출은 95억 2,600만 위안으로 106.76%, 순이익은 37억 1,500만 위안으로 131.49% 늘었다 [사실]",
  "출하설 부인: 천톈스 회장은 10월 26일 실적 설명회에서 2027년 칩 출하 100만 개 초과설에 대해 회사가 소통한 적이 없다고 밝혔고, DeepSeek·Kimi 등 중국 대형 모델과의 호환 작업을 마쳤다고 했다 [사실]",
  "재고: 재고는 116억 6,500만 위안(2025년 말 49억 4,400만 위안)으로 늘었고 회장은 주로 전략 비축 때문이라고 했으며, 1~3분기 재고평가충당금 5억 200만 위안을 쌓았고 선급금·지급어음도 크게 늘었다 [사실]",
  "공급 제약: 분석가들은 고대역폭 메모리(HBM) 부족 등 공급망 압박을 지목했고 모건스탠리는 HBM 비용 상승으로 MLU580 출하가 제약됐다고 봤다 [사실]"],
 basis="verified",
 check="회장의 출하설 부인, 1~3분기 매출 95억 2,600만 위안(106.76%), 재고 116억 6,500만 위안·재고평가충당금 5억 200만 위안은 검색 결과 요약(21세기경제보도 등)으로 확인",
 src=[S("21세기경제보도", "https://www.21jingji.com/article/20261026/herald/0cf099bda033ba3efa0ba578c3a7216e.html"),
      S("24TopNews", "https://24topnews.com/news/company/cambricon-chairman-denies-2027-chip-shipment-rumors-q1-q3-revenue-up-4069e8fd")],
 inds=["macro", "semis"], nodes=["macro/semis"],
 vc=[V("semis", "design", "공급", "down", "실제", "HBM 부족 등으로 캄브리콘 생산 제약")],
 added="텔레그램 1건 — 회장의 2027년 칩 100만 개 출하설 부인, 100억 위안 넘는 재고는 전략 비축이라는 설명, DeepSeek·Kimi 호환 완료 내용이 추가됨",
 items=[
  I("캄브리콘 회장, 2027년 칩 100만 개 출하설 부인", TG+"하나증권 중국전략", "https://t.me/HANAchina/71060",
    "캄브리콘 회장이 2027년 칩 출하 100만 개 초과설을 부인하면서 100억 위안 넘는 재고는 전략 비축 때문이라고 설명했다")]))

R.append(dict(cid="G2-040", attachTo="",
 title="마이크로소프트, 직원 약 6만 명에 희망퇴직 제안…전체 인력 4분의 1 대상 비용 절감",
 one="\n".join([
  "마이크로소프트가 비용 절감을 위해 직원 약 6만 명에게 자발적 희망퇴직을 제안했다",
  "· 대상은 전체 인력의 약 4분의 1로 미국·캐나다·인도·영국 일부 팀의 부사장급 이하 직원이다",
  "· 직원들은 12월 초까지 결정하며 수락하면 12월 31일 퇴사하고 통상 퇴직금 수준의 혜택을 받는다"]),
 facts=[
  "무엇이: 마이크로소프트가 10월 26일 직원 약 6만 명(전체 인력의 약 4분의 1)에게 자발적 희망퇴직을 제안했다 [사실]",
  "대상: 미국·캐나다·인도·영국 참여 팀의 부사장급 이하 직원으로 엑스박스·윈도·코파일럿·재무가 전면 참여하고 데이터센터·영업·마케팅·보안·양자컴퓨팅 일부는 빠졌다 [사실]",
  "일정: 12월 초까지 결정하고 수락하면 12월 31일 퇴사하며 통상 퇴직금과 비슷한 혜택을 받는다 [사실]",
  "앞선 감원: 올해 초 미국 인력 약 7%에 희망퇴직을 제안해 대상자 약 8,750명 중 30% 이상이 수락했고, 7월에는 4,800명(약 2.1%) 감원을 발표했다 [사실]"],
 basis="verified",
 check="약 6만 명 대상 희망퇴직 제안, 대상·일정, 앞선 감원은 검색 결과 요약(CNBC·TechCrunch 등)으로 확인",
 src=[S("CNBC", "https://www.cnbc.com/2026/10/26/microsoft-msft-voluntary-buyouts.html"),
      S("TechCrunch", "https://techcrunch.com/2026/10/26/microsoft-offers-buyouts-to-around-60000-employees-reports-say/")],
 inds=["tech"], nodes=[],
 vc=[V("tech", "software", "공급", "down", "예상", "마이크로소프트 직원 약 6만 명에 희망퇴직 제안")],
 items=[
  I("마이크로소프트, 직원 6만 명에 희망퇴직 제안…추가 비용 절감", "블룸버그", "https://www.bloomberg.com/news/articles/2026-10-26/microsoft-to-offer-buyouts-to-60-000-workers-in-latest-cost-cut")]))

R.append(dict(cid="G2-046", attachTo="",
 title="노바티스, 신약 성장에 연간 핵심 영업이익 전망 상향…3분기 핵심 EPS 2.46달러",
 one="\n".join([
  "스위스 제약사 노바티스가 신약 성장에 힘입어 3분기 실적과 함께 올해 핵심 영업이익 전망을 높였다",
  "· 연간 핵심 영업이익 전망은 한 자릿수 초반 감소에서 보합~한 자릿수 초반 증가로 바뀌었다",
  "· 3분기 핵심 EPS는 2.46달러로 예상을 웃돌았지만 19억 달러 손상 반영으로 순이익은 약 70% 줄었다"]),
 facts=[
  "무엇이: 노바티스가 10월 27일 3분기 실적과 함께 2026년 핵심 영업이익 전망을 한 자릿수 초반 감소에서 보합~한 자릿수 초반 증가로 높였고 매출 전망은 유지했다 [사실]",
  "3분기: 핵심 영업이익은 고정환율 기준 약 10% 늘어 약 60억 달러, 핵심 EPS는 8% 늘어 2.46달러로 예상을 웃돌았다 [사실]",
  "손상: 후기 임상 실패로 델데시란 자산에 19억 달러 부분 손상을 반영해 영업이익은 약 61%, 순이익은 약 70% 줄었다 [사실]",
  "매출: 매출은 시장 예상을 소폭 밑돌았다 [사실]"],
 basis="verified",
 check="연간 핵심 영업이익 전망 상향, 핵심 EPS 2.46달러, 19억 달러 손상은 노바티스 발표·검색 결과 요약으로 확인",
 src=[S("노바티스 보도자료", "https://www.novartis.com/news/media-releases/novartis-delivered-sales-growth-and-core-margin-expansion-q3-raised-fy-core-operating-income-guidance"),
      S("Quartz", "https://qz.com/novartis-raises-profit-outlook-trial-failure-charge-102726")],
 inds=["pharma"], nodes=[],
 vc=[V("pharma", "bigpharma", "수요", "up", "실제", "신약 성장에 연간 핵심 영업이익 전망 상향")],
 items=[
  I("노바티스, 신약 성장에 힘입어 연간 이익 전망 상향", "블룸버그", "https://www.bloomberg.com/news/articles/2026-10-27/novartis-raises-profit-outlook-on-growth-of-new-medicines")]))

R.append(dict(cid="G2-052", attachTo="",
 title="CIMB 필리핀 법인 매각에 BPI·메트로뱅크 관심…최대 2억 달러 거래 거론",
 one="\n".join([
  "말레이시아 CIMB그룹의 필리핀 법인 매각에 현지 대형은행 BPI와 메트로뱅크가 관심을 보였다",
  "· 구속력 있는 입찰은 10월 말 전에 마감되며 거래 가치는 최대 2억 달러로 거론된다",
  "· CIMB는 지역 포트폴리오와 자본 배분을 재검토하는 중이며 거래 성사는 확실하지 않다"]),
 facts=[
  "무엇이: CIMB그룹의 필리핀 사업 매각에 필리핀아일랜드은행(BPI)과 메트로뱅크가 관심을 보였고 다른 후보들도 관심을 나타냈다 [사실]",
  "일정·규모: 구속력 있는 입찰은 이달 말 전 마감이며 거래 가치는 최대 2억 달러(8억 1,700만 링깃)로 거론된다 [사실]",
  "배경: CIMB는 2018년 12월 필리핀에 진출해 2025년 9월까지 고객 1,000만 명을 모았고 지역 포트폴리오를 재검토 중이다 [사실]",
  "불확실성: 검토가 진행 중이라 거래 성사는 확실하지 않고 BPI는 논평을 거부했다 [사실]"],
 basis="verified",
 check="BPI·메트로뱅크 관심, 이달 말 구속력 있는 입찰, 최대 2억 달러 가치는 검색 결과 요약(BusinessWorld 등)으로 확인",
 src=[S("BusinessWorld", "https://bworldonline.com/banking-finance/2026/10/27/789532/cimb-said-to-attract-bpi-metrobank-for-philippine-unit-sale/"),
      S("The Edge Malaysia", "https://theedgemalaysia.com/node/823378")],
 inds=["fin"], nodes=[],
 vc=[V("fin", "banks", "공급", "down", "예상", "CIMB 필리핀 법인 매각에 BPI·메트로뱅크 관심")],
 items=[
  I("CIMB 필리핀 법인 매각에 BPI·메트로뱅크 관심", "블룸버그", "https://www.bloomberg.com/news/articles/2026-10-27/cimb-bpi-metrobank-philippine-unit-sale")]))

R.append(dict(cid="G2-058", attachTo="",
 title="피치, 남아공 부채 전망서 재무부와 엇갈려…부채비율 2028/29년 79%로 상승 전망",
 one="\n".join([
  "신용평가사 피치가 남아공 정부부채 전망에서 재무부와 다른 시각을 내놓으며 부채비율 상승을 예상했다",
  "· 피치는 부채비율이 GDP 대비 약 78%를 유지하다 2028/29회계연도에 79%로 오를 것으로 봤다",
  "· 재무부는 부채비율이 2025/26년 78.4%로 정점을 찍고 2029/30년 76.6%로 내려간다고 밝혔다"]),
 facts=[
  "무엇이: 피치는 남아공 부채비율이 향후 2개 회계연도 GDP 대비 약 78%에 머문 뒤 2028/29년 79%로 오를 것으로 봐 재무부·무디스 전망과 엇갈렸다 [사실]",
  "재무부: 고동와나 재무장관은 부채비율이 2025/26년 78.4%로 정점을 찍고 2029/30년 76.6%로 내려간다고 밝혔다 [사실]",
  "이유: 피치는 주로 약한 성장 탓으로 봤지만 중기예산정책보고서(MTBPS)의 재정건전화 노력은 순항 중이라고 평가했다 [사실]",
  "등급 일정: 피치는 6월 BB(안정적)로 올렸고, 무디스·S&P는 11월 27일, 피치는 12월 11일 평가를 내놓는다 [사실]"],
 basis="verified",
 check="피치의 부채비율 78%→2028/29년 79% 전망과 재무부의 78.4% 정점·76.6% 하락 전망은 검색 결과 요약으로 확인",
 src=[S("Ghanamma", "https://www.ghanamma.com/2026/10/27/fitch-diverges-from-national-treasury-on-debt-outlook/"),
      S("EWN", "https://www.ewn.co.za/fitch-says-mtbps-supports-sas-debt-stability-while-flagging-growth-risks")],
 inds=["macro"], nodes=["macro/fiscal"],
 vc=[V("macro", "fiscal", "공급", "up", "예상", "피치, 남아공 부채비율 2028/29년 79% 상승 전망")],
 items=[
  I("피치, 남아공 부채 전망에서 재무부와 엇갈린 시각", "블룸버그", "https://www.bloomberg.com/news/articles/2026-10-26/fitch-diverges-from-south-africa-s-treasury-on-debt-outlook")]))

KEYS = ["cid", "attachTo", "title", "one", "facts", "basis", "check", "src", "inds", "nodes", "vc", "fed", "added", "items"]
out = {"agent": "W5", "searches_used": 18, "fetches_used": 3,
       "items": [{k: r[k] for k in KEYS if k in r} for r in R], "skipped": []}
json.dump(out, open('/home/user/news-desk/data/mix-2026-10-27/out2/W5.json', 'w'), ensure_ascii=False, indent=1)

# length report
import re
for r in R:
    w = r['cid']; P = []
    if not 20 <= len(r['title']) <= 70: P.append(f"title {len(r['title'])}")
    L = r['one'].replace(' (채널 전언)', '').replace(' (제목 기준)', '').split('\n')
    if not 40 <= len(L[0]) <= 90: P.append(f"L1 {len(L[0])}")
    for i, l in enumerate(L[1:], 2):
        if not 25 <= len(l) <= 90: P.append(f"L{i} {len(l)}")
    for it in r['items']:
        if not 25 <= len(it['t']) <= 60: P.append(f"t {len(it['t'])} {it['t']}")
        if 's' in it:
            s = it['s'].replace(' (제목 기준)', '')
            if not 45 <= len(s) <= 110: P.append(f"s {len(s)}")
    for v in r['vc']:
        if not 12 <= len(v['t']) <= 45: P.append(f"vc {len(v['t'])}")
    if 'added' in r and not 40 <= len(r['added']) <= 140: P.append(f"added {len(r['added'])}")
    for f in r.get('fed', []):
        if not 20 <= len(f['t']) <= 70: P.append(f"fed {len(f['t'])}")
    for f in r['facts']:
        if '|' in f or '**' in f: P.append('bad char')
    if P: print(w, P)
