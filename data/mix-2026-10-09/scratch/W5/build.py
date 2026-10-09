import json,re
OUT='/home/user/news-desk/data/mix-2026-10-09/out2/W5.json'
T=lambda t,o,d,u:{"t":t,"o":o,"d":d,"u":u}
items=[]
def add(cid,att,title,one,facts,basis,check,src,inds,nodes,its):
    items.append({"cid":cid,"attachTo":att,"title":title,"one":one,"facts":facts,"basis":basis,"check":check,"src":src,"inds":inds,"nodes":nodes,"items":its})

add("C005","n-tg-0149",
"오픈AI 매출 500억 달러 보도에 AI주 급락…필라델피아 반도체지수 3.66%↓",
"FT가 오픈AI의 9월 말 연환산 매출이 약 500억 달러로 앞서 알려진 700억 달러보다 200억 달러 적다고 보도하면서, 필라델피아 반도체지수가 3.66% 급락하고 오라클·코어위브 등 AI 관련주가 줄줄이 떨어져 AI 투자 회수 능력에 대한 의문이 커졌다",
["무엇이: FT는 오픈AI가 투자자들에게 9월 말 연환산 매출이 약 500억 달러라고 설명했다고 보도했고, 이는 앞서 알려진 약 700억 달러보다 약 200억 달러 적습니다 [사실]",
 "주가: 10월 8일 엔비디아 3%, 오라클 약 6%, 코어위브 약 8%, AMD·브로드컴 4%, 인텔 5% 하락했습니다 [사실]",
 "지수: 필라델피아 반도체지수는 478.0포인트(3.66%) 내린 12,588.2에 마감했고 나스닥100은 1.6% 하락했습니다 [채널]",
 "차이 원인: 앤트로픽은 클라우드 파트너 경유 매출을 넣은 총매출, 오픈AI는 순매출 기준이며, CNBC는 앞선 680억 달러가 파트너 총매출을 포함한 수치라고 전했습니다 [사실]",
 "배경: 오픈AI는 투자자들에게 2026년 말 연환산 매출 700억 달러 이상을 내세운 바 있습니다 [사실]"],
"verified","FT 보도(500억 달러, 200억 달러 차이)와 AI주 하락은 CNBC 등 검색 결과 요약으로 확인. 반도체지수 3.66%·12,588.2는 채널 수치(다른 보도는 3.4%로 차이). 앤트로픽 매출 정체 주장은 확인 못 함",
[{"o":"CNBC","d":"2026-10-08","u":"https://www.cnbc.com/2026/10/08/open-ai-revenue-nvidia-oracle-coreweave.html"},
 {"o":"Investing.com(FT 인용)","d":"2026-10-08","u":"https://www.investing.com/news/stock-market-news/openai-annualized-revenue-at-50bn-far-below-reports--ft-4939530"}],
["macro"],["macro/semis"],
[T("앤트로픽 연환산 매출 성장 정체 주장…중국산 저가 AI 잠식 지목","텔레그램 Polaristimes","2026-10-09","https://t.me/The_MariTimes/63604"),
 T("오픈AI 매출 200억 달러 적다는 보도에 필라델피아 반도체지수 3.66% 급락","텔레그램 TNBfolio","2026-10-09","https://t.me/TNBfolio/71482"),
 T("CNN, 오픈AI 매출 예상보다 낮다는 보도에 기술주 하락…회계 기준 차이 지목","텔레그램 카이에 de market","2026-10-09","https://t.me/cahier_de_market/10950"),
 T("TickerTrends, 오픈AI 연간 매출 추적치 약 504억 달러로 FT 보도와 부합","텔레그램 카이에 de market","2026-10-09","https://t.me/cahier_de_market/10951")])

add("C007","n-tg-0121",
"우크라 드론, 얀덱스 데이터센터 이틀 새 두 곳 타격…트럼프 '러 정유 공격 멈춰야'",
"우크라이나 드론이 루코일 볼고그라드 정유소를 멈춰 세운 데 이어 이틀 새 얀덱스 데이터센터 두 곳까지 타격하자, 트럼프 대통령이 경유 공급 부족을 이유로 러시아 정유시설 공격 중단을 요구하면서 러시아 석유제품 차질이 외교 쟁점으로 번지고 있다",
["무엇이: 얀덱스는 10월 9일 칼루가주 데이터센터의 여러 모듈이 드론 공격으로 완전히 멈췄다고 밝혔고, 하루 전 랴잔주 데이터센터에 이은 이틀 새 두 번째 피해입니다 [사실]",
 "정유소: 루코일 볼고그라드 정유소(하루 약 28만 배럴)가 10월 2일 원유 처리를 완전히 멈췄고, 10월 9일에는 코미공화국의 루코일 정유소도 공격받았다는 보도가 나왔습니다 [사실]",
 "트럼프: 트럼프 대통령은 우크라이나가 러시아 정유시설 공격을 멈춰야 하며 경유 공급 부족은 중동이 아니라 러우전쟁 때문이라고 말했습니다 [채널]",
 "공습: 우크라이나군은 10월 9일 새벽 이틀 연속 대규모 드론 공습을 벌였습니다 [채널]",
 "우크라이나: 러시아의 공격에 맞서 우크라이나가 주유소 방호를 강화하고 있습니다 [제목]"],
"verified","얀덱스 두 번째 데이터센터(칼루가) 피해와 코미 정유소 공격은 모스크바타임스 등 검색 결과 요약으로 확인. 트럼프의 10월 9일 발언은 찾지 못했고 9월 중순 같은 취지 발언만 확인",
[{"o":"The Moscow Times","d":"2026-10-09","u":"https://www.themoscowtimes.com/2026/10/09/ukraine-drones-hit-second-yandex-data-center-in-two-days-a93927"},
 {"o":"NBC News","d":"2026-09","u":"https://www.nbcnews.com/world/ukraine/trump-calls-ukraine-halt-strikes-russian-diesel-fuel-citing-global-sho-rcna597637"}],
["macro"],["macro/geo","macro/commodity"],
[T("우크라이나군, 이틀 연속 러시아에 대규모 드론 공습","텔레그램 미국 주식 인사이더","2026-10-09","https://t.me/insidertracking/65802"),
 T("트럼프 '우크라, 러시아 정유시설 공격 멈춰야…경유 부족은 러우전쟁 탓'","텔레그램 Polaristimes","2026-10-09","https://t.me/The_MariTimes/63606"),
 T("우크라이나, 러시아 공격에 대비해 주유소 방호 강화","로이터","2026-10-09","https://www.reuters.com/business/energy/ukraine-fortifies-its-filling-stations-against-russian-attacks-2026-10-09/"),
 T("러시아 얀덱스 '두 번째 데이터센터도 드론 공격 받아'","로이터","2026-10-09","https://www.reuters.com/world/europe/russias-yandex-says-second-data-centre-hit-by-drone-attack-2026-10-09/")])

add("C012","",
"中, 지방에 820억 달러 추가 부양…인민은행 '경쟁적 절하 안 한다'",
"중국 재정부가 쓰지 않은 정부 차입 한도 5,500억 위안(820억 달러)을 지방 예산에 다시 배정해 성장 목표 달성을 위한 재정 지출을 늘리는 가운데, 인민은행은 경쟁적 위안화 절하를 하지 않겠다고 밝혀 환율 안정 의지를 내비쳤다",
["무엇이: 중국이 지방정부가 820억 달러를 끌어 쓸 수 있게 하는 추가 부양책을 내놓았습니다 [제목]",
 "내용: 재정부가 쓰지 않은 차입 한도 5,500억 위안을 지방 예산에 재배정했고, 이 중 3,000억 위안은 현·구 단위 운영비, 나머지는 공사 중인 사업 위주 인프라에 쓰입니다 [사실]",
 "목표: 중국은 성장 목표 달성을 위해 재정 지원을 늘리고 있습니다 [제목]",
 "환율: 인민은행은 관리변동환율제 아래 시장이 환율 결정에 결정적 역할을 하게 하고, 무역 경쟁력을 위한 절하는 필요도 의도도 없으며 경쟁적 절하를 하지 않는다고 밝혔습니다 [채널]"],
"partial","820억 달러=5,500억 위안 재배정은 Finimize 검색 결과 요약으로 확인했으나 재정부 원문은 못 봄. 인민은행 환율 입장은 채널 원문만 근거",
[{"o":"Finimize","d":"2026-10-09","u":"https://finimize.com/content/china-unlocked-82-billion-in-debt-quotas-for-local-budgets"}],
["macro"],["macro/fiscal","macro/fx"],
[T("인민은행 '환율 결정은 시장이 결정적 역할…경쟁적 절하 안 해'","텔레그램 하나증권 중국전략","2026-10-08","https://t.me/HANAchina/70077"),
 T("중국, 지방 정부에 820억 달러 규모 추가 부양책 내놓아","블룸버그","2026-10-09","https://www.bloomberg.com/news/articles/2026-10-09/china-allows-provinces-to-draw-on-82-billion-to-shore-up-growth"),
 T("중국, 성장 목표 달성 위해 재정 지원 강화","로이터","2026-10-09","https://www.reuters.com/world/china-ramps-up-fiscal-push-meet-growth-target-2026-10-09/")])

add("C017","n-bbg-0077",
"후티 아브카이크 공격 전언…트럼프 발언 약발 다한 유가, 실물 공급이 좌우",
"아람코가 완충재고 고갈을 경고한 가운데 예멘 후티 반군이 사우디 아브카이크 석유시설을 공격했다는 전언이 나왔고, 트럼프의 이란 경고는 유가를 거의 움직이지 못하면서 원유 시장이 정치 발언 대신 물동량 같은 실물 공급 지표에 반응하고 있다 (채널 전언)",
["무엇이: 예멘 후티 반군이 사우디 아브카이크 석유시설을 공격한 것으로 보이며 큰 화염과 연기가 목격됐다고 전해졌습니다 [채널]",
 "엇갈림: 사우디 정부·아람코의 공식 확인은 찾지 못했고, 위성에 잡힌 연기가 아브카이크 본시설이 아니라 아인다르 유전 남쪽에서 나왔다는 반론도 있습니다 [미확인]",
 "트럼프: 4월 트럼프의 위협 발언은 유가를 하루 만에 7% 올렸지만 10월 이란 경고는 거의 영향이 없었고, 트레이더들은 해운 물동량 등 객관적 데이터에 주목하고 있습니다 [채널]",
 "재고: 아람코 CEO는 중동 위기 이후 10억 배럴 넘는 상업재고가 풀렸고 남은 재고도 대부분 쓸 수 없다고 경고했습니다 [사실]",
 "2019년: 당시 아브카이크·쿠라이스 공격으로 사우디 원유 생산이 절반가량 멈췄습니다 [사실]"],
"channel","아브카이크 10월 공격은 소셜미디어·소규모 매체에만 있고 공식 확인 없음. 트럼프 발언의 유가 영향 약화는 검색하지 않음. 재고 경고는 기존 문서 근거",
[{"o":"Wikipedia(2019 아브카이크 공격)","d":"2019-09-14","u":"https://en.wikipedia.org/wiki/Abqaiq%E2%80%93Khurais_attack"}],
["macro"],["macro/commodity","macro/geo"],
[T("후티 반군, 사우디 아브카이크 석유시설 공격한 듯…대형 화염 목격","텔레그램 트릴리온","2026-10-09","https://t.me/Trillion_labs/10218"),
 T("트럼프 발언, 더는 유가 못 움직여…실물 공급 데이터가 새 기준(중국언론)","텔레그램 하나증권 중국전략","2026-10-09","https://t.me/HANAchina/70104")])

add("C021","n-tg-0204",
"中 국경절 국내여행 8억 2,600만 회·지출 1,101억 달러…씀씀이는 주춤",
"중국 국경절 연휴 출입국자가 6.7% 늘어난 데 이어 국내 여행이 8억 2,600만 회, 지출이 7,384억 위안(1,101억 달러)으로 집계됐지만, 일평균 지출 증가율(4.3%)이 여행 횟수 증가율(6.3%)에 못 미쳐 1회당 씀씀이는 약해졌다",
["무엇이: 문화관광부 집계로 국경절 연휴(10월 1~7일) 국내 여행은 8억 2,600만 회, 국내 여행 지출은 7,384억 3,800만 위안(1,101억 달러)입니다 [사실]",
 "증가율: 작년 연휴와 길이가 달라 일평균으로 비교하면 여행 횟수는 6.3%, 지출은 4.3% 늘었습니다 [사실]",
 "1회당: 1회당 지출은 약 894위안으로 작년 연휴 약 911위안보다 낮습니다 [추론]",
 "출입국: 출입국자는 1,546만 2,000명으로 6.7% 늘었고 본토 주민 출국은 9.3% 늘었습니다 [채널]"],
"verified","2026년 국내 여행 수치는 anews 등 검색 결과 요약으로 확인. 하나증권 텔레그램 글(8.88억 명·8,090억 위안·1인당 911위안)은 2025년 연휴 통계의 재탕이라 기사 목록에서 뺌",
[{"o":"A News","d":"2026-10-09","u":"https://www.anews.com.tr/world/2026/10/09/chinas-national-day-holiday-tourism-spending-reaches-1101b"}],
["consumer"],[],
[T("중국 국경절 연휴 국내 여행 지출 1,100억 달러 기록","로이터","2026-10-09","https://www.reuters.com/business/retail-consumer/chinas-domestic-travel-spend-during-golden-week-hits-110-billion-2026-10-09/")])

add("C026","n-rtr-0114",
"美 세븐일레븐, 인플레에 공급망 내재화 추진…IPO 시점은 회복·시장에 달려",
"세븐&아이의 2분기 영업이익이 일본 편의점 부진으로 11% 줄어든 가운데, 미국 7-일레븐이 인플레이션 부담 속에 공급망을 직접 운영하는 방안을 추진하고 CEO가 IPO 시점은 사업 회복과 시장 상황에 달렸다고 밝히면서 북미 상장 일정이 불확실해졌다",
["무엇이: 미국 7-일레븐이 인플레이션 부담 속에 공급망을 내재화하는 방안을 추진하고 있습니다 [제목]",
 "IPO: 미국 7-일레븐 CEO는 IPO 시점이 사업 회복과 시장 상황에 달렸다고 말했습니다 [제목]",
 "연기: 세븐&아이는 4월 북미 법인 상장을 빨라야 2027 회계연도로 미뤘고, 경제 전망이 불확실하다고 했습니다 [사실]",
 "실적: 세븐&아이 2분기(6~8월) 영업이익은 1,273억 엔으로 11% 줄었고 해외 편의점 영업이익은 약 두 배로 늘었습니다 [사실]"],
"partial","상장 연기 배경은 CSP Daily News 검색 결과 요약으로 확인. 공급망 내재화 세부 내용과 CEO의 IPO 발언은 로이터·블룸버그 제목 외 독립 출처로 확인 못 함",
[{"o":"CSP Daily News","d":"2026-04","u":"https://www.cspdailynews.com/company-news/seven-i-holdings-delays-north-american-ipo-fiscal-year-2027"}],
["consumer"],[],
[T("미국 7-일레븐, 인플레이션 압박에 공급망 내재화 추진","로이터","2026-10-09","https://www.reuters.com/business/7-elevens-us-arm-looks-move-supply-chain-in-house-inflation-bites-2026-10-09/"),
 T("미국 7-일레븐 CEO 'IPO 시점은 사업 회복과 시장에 달려'","블룸버그","2026-10-09","https://www.bloomberg.com/news/articles/2026-10-09/us-7-eleven-ipo-timing-depends-on-turnaround-market-ceo-says")])

add("C032","n-bbg-0162",
"에어텔 머니, 런던 데뷔 첫날 공모가 언저리 맴돌아…53억 파운드 IPO",
"아프리카 모바일 결제업체 에어텔 머니가 기업가치 53억 파운드로 5억 2,900만 파운드어치 구주를 팔아 런던 5년 만의 최대급 IPO를 마쳤지만, 거래 첫날 주가가 공모가 1.96파운드 언저리에서 맴돌면서 런던 IPO 시장 회복 기대에 힘이 실리지 못했다",
["무엇이: 에어텔 머니는 10월 9일 런던증권거래소에서 거래를 시작했고, 첫 한 시간 1.94파운드로 공모가 1.96파운드를 밑돌았다는 보도가 나왔습니다 [사실]",
 "규모: 카타르투자청·TPG 등 기존 주주가 2억 7천만 주를 팔아 약 5억 2,900만 파운드를 조달했고, 초과배정 옵션으로 2,700만 주를 더 팔 수 있습니다 [사실]",
 "가격: 투자 수요를 끌어내려 기업가치 기대치를 두 번 낮추고 고정 가격으로 공모했습니다 [사실]",
 "일정: 조건 없는 정식 거래는 10월 14일 시작될 예정입니다 [사실]"],
"verified","첫날 주가 흐름과 공모 조건은 Yahoo UK·DirectorsTalk 등 검색 결과 요약으로 확인(시점별로 보합~1% 하락으로 엇갈림)",
[{"o":"Yahoo Finance UK","d":"2026-10-09","u":"https://uk.finance.yahoo.com/news/airtel-money-shares-muted-london-083848971.html"},
 {"o":"DirectorsTalk","d":"2026-10-09","u":"https://www.directorstalkinterviews.com/airtel-money-set-to-begin-trading-on-london-stock-exchange/4121265701"}],
["fin"],[],
[T("에어텔 머니, 런던 증시 데뷔 첫날 잠잠한 출발","로이터","2026-10-09","https://www.reuters.com/business/airtel-money-makes-muted-london-trading-debut-2026-10-09/")])

add("C037","n-tg-0136",
"코스피, 반도체지수와 이례적 디커플링…자사주 매입 약화·옵션 청산 겹쳐",
"삼성전자·TSMC의 사상 최대 실적에도 AI 호황 지속성 의문에 코스피가 밀린 가운데, 자사주 매입 자금이 먼저 빠지고 고유가와 옵션 포지션 청산이 겹치면서 코스피가 주요 이동평균선을 밑돌며 필라델피아 반도체지수와 따로 움직이고 있다",
["무엇이: 코스피가 100일 이동평균선 등 주요 이동평균선을 밑돌며 강세를 이어가는 필라델피아 반도체지수와 엇갈린 흐름을 보였습니다 [사실]",
 "수급: 삼성전자·SK하이닉스 자사주 매입이 사실상 마무리되면서 수급 공백 우려가 커졌고, 옵션 포지션 청산과 고유가도 부담입니다 [사실]",
 "골드만삭스: 이번 조정은 사이클 정점보다는 포지션 조정에 가깝고 반도체 펀더멘털은 견조하다고 봤습니다 [사실]",
 "실적: 삼성전자 3분기 잠정 영업이익 107조 4,000억 원에도 10월 8일 삼성 주가는 2.4%, 코스피는 2.6% 떨어졌습니다 [사실]"],
"partial","디커플링·자사주 매입 소진·골드만 시각은 AllWeather Finance·BigGo 등 2차 매체 검색 결과 요약으로 확인. 골드만 원문 보고서는 못 봄",
[{"o":"AllWeather Finance","d":"2026-10-08","u":"https://allweatherfinance.com/south-korean-stocks-have-broken-below-a-key-moving-average-a-rare-divergence-has-occurred-with-the-philadelphia-semiconductor-index-and-buyback-support-is-also-waning/"},
 {"o":"BigGo Finance","d":"2026-10","u":"https://finance.biggo.com/news/6007996e-e840-48b0-82be-5c2988eaa7a8"}],
["macro"],["macro/semis"],
[T("코스피, 이동평균선 하회하며 반도체지수와 이례적 디커플링…자사주 매입 지지 약화","텔레그램 하나증권 중국전략","2026-10-08","https://t.me/HANAchina/70080")])

add("C042","",
"中 고무값 9년 만의 최고…타이어 업체 60여 곳 2~5% 일제 인상",
"상하이 고무 선물값이 연초보다 28% 넘게 올라 톤당 2만 145위안으로 9년 만의 최고를 찍으면서, 중국 타이어 업체 60여 곳이 9월 이후 70건 넘는 공문을 내고 전 품목 값을 2~5% 올리고 있다",
["무엇이: 10월 8일 상하이선물거래소 고무 주력 계약은 톤당 20,145위안으로 연초 대비 28% 넘게 올라 9년 만의 고점입니다 [사실]",
 "가격 인상: 9월 이후 60여 개 타이어 업체가 70건 넘는 인상 공문을 냈고, 전강·반강·공정용 타이어 전 품목에 2~5% 인상률을 적용했습니다 [사실]",
 "원가: 타이어 원가의 70% 이상이 원료이고, 산둥 업체 기준 연초 이후 천연고무는 약 15%, 카본블랙은 75% 넘게 올랐습니다 [사실]",
 "원인: 고무나무 채취 면적 증가 둔화, 동남아 강우, 원자재 자금 유입이 겹쳤고 칭다오 고무 재고는 평년 약 15만 톤에서 약 9만 톤으로 줄었습니다 [사실]"],
"verified","고무 가격·인상 공문 건수·인상률은 21세기경제보도·CCTV 재전송(시나) 검색 결과 요약으로 확인",
[{"o":"21세기경제보도","d":"2026-10-09","u":"https://m.21jingji.com/article/20261009/herald/401ebff89bd61d5912167416ea7fa0d1.html"},
 {"o":"시나(CCTV 재전송)","d":"2026-10-09","u":"https://www.sina.cn/weibo/detail/5352031725814475.html"}],
["agri"],[],
[T("중국 고무값 9년 만의 최고, 타이어 업체 60여 곳 일제 가격 인상","텔레그램 하나증권 중국전략","2026-10-09","https://t.me/HANAchina/70093")])

add("C047","",
"라간, 내년 중반 CPO용 FAU 모듈 양산…3분기 총이익률 13년 만의 최저",
"대만 렌즈업체 라간이 CPO 사업을 넓히려 새 공장에서 내년 중반 FAU 모듈 양산에 들어가는 가운데, 3분기 매출총이익률이 42.21%로 7.2%포인트 떨어지고 스마트폰 주문은 11월부터 둔화할 전망이다",
["무엇이: 라간은 새 공장에서 내년 중반 FAU 모듈 양산을 시작할 계획이며, 시험 라인은 9월 고객 인증을 통과했습니다 [사실]",
 "실적: 3분기 매출은 156억 5,100만 대만달러로 전분기보다 14.54% 늘고 전년보다 11.46% 줄었으며, 매출총이익률 42.21%는 13년여 만의 최저입니다 [사실]",
 "원인: 신제품 수율과 재생에너지 전력 구매 비용이 이익률을 끌어내렸고, 가격 전가는 2028년에나 가능할 전망입니다 [사실]",
 "주문: 10월 주문은 9월과 비슷하지만 11월부터 둔화하고, 고객사의 수요 전망 하향으로 2027년 주문 가시성은 낮습니다 [사실]",
 "장기: 새로 산 부지 공장은 광통신·FAU용으로 2030년 완공이 목표입니다 [사실]"],
"verified","10월 8일 실적설명회 내용은 자유시보·테크뉴스 등 검색 결과 요약으로 확인. FAU 양산 시점은 내년 중반(자유시보)과 2027년 하반기(중앙사)로 보도가 엇갈림",
[{"o":"자유시보","d":"2026-10-08","u":"https://ec.ltn.com.tw/article/breakingnews/5600023"},
 {"o":"TechNews","d":"2026-10-08","u":"https://technews.tw/2026/10/08/largan-2026-q3-financial-report/"}],
["macro"],["macro/semis"],
[T("라간, 내년 중반 새 공장서 FAU 모듈 양산…3분기 총이익률 7.2%p 하락","텔레그램 하나증권 중국전략","2026-10-09","https://t.me/HANAchina/70099")])

add("C052","",
"아디티아 비를라 재생에너지, 셸 인도 법인 인수에 15억 달러 루피 대출 추진",
"인도 아디티아 비를라 리뉴어블스가 셸의 인도 재생에너지 자회사 솔에너지를 18억 달러에 사들이려 15억 달러 규모 루피 대출을 추진하면서, MUFG 브리지론을 프로젝트 단위 장기 대출로 바꾸려 하고 있다",
["무엇이: 아디티아 비를라 리뉴어블스가 15억 달러 규모 루피 표시 대출을 추진하며 인도국영은행·HDFC은행 등에 타진했습니다 [사실]",
 "인수: 스프링 에너지 계열을 포함한 솔에너지 파워 인수가는 18억 달러이며 약 5GWp 설비가 더해집니다 [사실]",
 "구조: 앞서 받은 MUFG의 16억 달러 브리지론 약정을 대신해 운영·건설 중 사업을 담은 17~20개 특수목적법인 단위로 대출을 나눌 계획입니다 [사실]",
 "엇갈림: 7월 보도는 MUFG 15억 달러를 5년 만기 해외 상업차입으로 확보했다고 해 자금 구조 설명이 다릅니다 [미확인]"],
"verified","대출 규모·인수가·대출 구조는 Scoopearth·Whalesbook 검색 결과 요약으로 확인",
[{"o":"Scoopearth","d":"2026-10-09","u":"https://scoopearth.com/aditya-birla-renewables-is-seeking-1-5-billion-in-rupee-denominated-loans-for-shell-india-unit-deal/"},
 {"o":"Whalesbook","d":"2026-10-09","u":"https://www.whalesbook.com/news/English/bankingfinance/Aditya-Birla-Renewables-Seeks-dollar15B-Loan-for-Shell-Deal/6ac88e8a79a16deaeaeba113"}],
["power"],["power/developers"],
[T("인도 아디티아 비를라 자회사, 셸 자회사 솔에너지 인수 위해 15억 달러 루피 대출 추진","로이터","2026-10-09","https://www.reuters.com/world/indias-aditya-birla-unit-seeks-15-billion-rupee-loans-buy-shell-arm-solenergi-2026-10-09/")])

add("C057","",
"노르세 애틀랜틱, 파키스탄항공에 787-9 두 대 임대…ACMI 계약 확보",
"노르웨이 항공사 노르세 애틀랜틱이 파키스탄국제항공에 보잉 787-9 두 대를 승무원·정비·보험 포함 조건으로 빌려주기로 하면서, 인디고 계약 종료로 빈 기재를 11월부터 파키스탄-영국 노선에 다시 투입하게 됐다",
["무엇이: 노르세 애틀랜틱이 파키스탄국제항공에 보잉 787-9 두 대를 ACMI(기재·승무원·정비·보험 포함) 방식으로 빌려주며 운항은 2026년 11월 시작합니다 [사실]",
 "노선: 파키스탄국제항공은 이 기재로 파키스탄-영국 노선 운항을 늘립니다 [사실]",
 "배경: 인디고가 7월 웻리스 계약을 끝냈고, 노르세는 항공유 급등에 대서양 저가 노선을 줄이고 ACMI 비중을 늘리며 7월부터 매각·합병 절차를 밟고 있습니다 [사실]",
 "엇갈림: 9월 파키스탄국제항공 이사회는 노르세의 보잉 777 두 대 6개월 임대를 승인했다고 보도돼 기종이 다릅니다 [미확인]"],
"verified","임대 기종·운항 시점·배경은 FlightGlobal·Paddle Your Own Kanoo 검색 결과 요약으로 확인",
[{"o":"FlightGlobal","d":"2026-10","u":"https://www.flightglobal.com/airlines/2026/10/pakistan-international-airlines-to-lease-norse-787s-after-termination-of-indigo-partnership/"},
 {"o":"Paddle Your Own Kanoo","d":"2026-10-09","u":"https://www.paddleyourownkanoo.com/2026/10/09/norse-atlantic-secures-wet-lease-deal-with-pakistan-international-airlines-more-deals-could-be-on-the-way/"}],
["aero"],[],
[T("노르세 애틀랜틱, 파키스탄국제항공과 항공기 임대 계약","로이터","2026-10-09","https://www.reuters.com/business/aerospace-defense/norse-atlantic-lands-lease-deal-with-pakistans-pia-2026-10-09/")])

add("C062","",
"英 뷰티테크, CEO·CTO 지분 일부 할인 매각에 주가 하락",
"영국 뷰티기기 업체 뷰티테크 그룹의 CEO와 CTO가 상장 후 처음으로 주식 150만 주를 주당 400펜스, 직전 종가보다 약 15% 싸게 팔면서 주가가 장중 470펜스에서 422펜스까지 밀렸다",
["무엇이: 로런스 뉴먼 CEO와 앤드루 쇼먼 CTO가 각각 75만 주, 모두 150만 주(지분 약 1.4%)를 주당 400펜스에 팔았고 2025년 10월 상장 후 첫 매도입니다 [사실]",
 "조건: 매각가는 직전 종가보다 약 15% 낮고 10월 1일 발표한 역 가속 북빌딩 방식 자사주 매입과 연계됐으며, 90일간 추가 매도를 하지 않기로 했습니다 [사실]",
 "지분: 매각 뒤 뉴먼은 약 3.9%, 쇼먼은 약 4.1%를 보유합니다 [사실]",
 "주가: 470펜스에 시작해 장중 422펜스까지 떨어졌습니다 [사실]"],
"verified","매각 규모·가격·지분·주가는 TipRanks·Proactive Investors·ADVFN 검색 결과 요약으로 확인(하락률은 시점별로 1.8~6.6%로 엇갈림)",
[{"o":"TipRanks","d":"2026-10-09","u":"https://www.tipranks.com/news/company-announcements/beauty-tech-group-executives-trim-stakes-in-coordinated-share-sale"},
 {"o":"ADVFN","d":"2026-10-09","u":"https://uk.advfn.com/market-news/article/24361/the-beauty-tech-group-shares-fall-1-8-following-6-million-executive-share-sale"}],
["beauty"],["beauty/brands"],
[T("영국 뷰티테크, CEO·CTO 지분 축소 소식에 주가 하락","로이터","2026-10-09","https://www.reuters.com/world/uk/uks-beauty-tech-slips-ceo-cto-trim-stake-2026-10-09/")])

add("C067","",
"폴란드 의회 위원회, 글라핀스키 중앙은행 총재 국사재판소 회부 표결 권고",
"폴란드 하원 헌법책임위원회가 글라핀스키 중앙은행 총재를 국사재판소에 세우자는 보고서를 채택해 하원 표결을 권고하면서, 현직 중앙은행 총재 기소 절차가 본회의로 넘어가고 가결 요건을 둘러싼 다툼이 이어질 전망이다",
["무엇이: 하원 헌법책임위원회가 10월 9일 글라핀스키 총재를 국사재판소에 회부하자는 보고서를 채택했고, 혐의는 8가지입니다 [사실]",
 "혐의: 중앙은행을 통한 최소 1,440억 즐로티 재정적자 간접 지원, 이사회 승인 없는 외환 개입, 선거운동 기간 금리 인하 등이 포함됐습니다 [사실]",
 "일정: 의원들에게 최소 21일 검토 기간을 줘야 해 하원 표결은 빨라야 10월 말입니다 [사실]",
 "가결 요건: 연정은 과반을 갖고 있지만 2024년 1월 헌법재판소는 5분의 3(276표)이 필요하다고 봤고 연정은 30표 넘게 모자랍니다 [사실]",
 "반응: 글라핀스키 총재는 절차가 근거 없다는 입장입니다 [사실]"],
"verified","위원회 보고서 채택·혐의·표결 요건은 RMF24·Super Biznes 등 폴란드 매체 검색 결과 요약으로 확인",
[{"o":"RMF24","d":"2026-10-09","u":"https://rmf24.pl/fakty/polska/news-adam-glapinski-przed-trybunal-stanu-komisja-przeglosowala-wn,nIdn,1021168"},
 {"o":"Super Biznes","d":"2026-10-09","u":"https://superbiz.se.pl/wiadomosci/koniec-prac-komisji-glapinski-blizej-trybunalu-stanu-aa-gGYK-mz2a-jCi3.html"}],
["macro"],["macro/cb"],
[T("폴란드, 중앙은행 총재 국사재판소 회부 표결 추진","블룸버그","2026-10-09","https://www.bloomberg.com/news/articles/2026-10-09/polish-commission-recommends-vote-on-putting-glapinski-on-trial")])

add("C072","",
"EU, 핵심광물 전략사업 46곳 추가 선정…211억 유로 투자 필요",
"EU 집행위원회가 16개 회원국의 핵심광물 전략사업 46곳을 새로 골라 인허가를 앞당기고 자금 조달을 돕기로 하면서, 약 211억 유로가 드는 리튬·희토류 등 역내 공급망 구축에 속도가 붙을 수 있다",
["무엇이: EU 집행위가 2차 공모 신청 102건 가운데 16개 회원국의 전략사업 46곳을 골랐습니다 [사실]",
 "구성: 전략 원자재 17종 중 구리·리튬·니켈·희토류 등 15종을 다루며 채굴 8건, 가공 11건, 재활용 19건 등입니다 [사실]",
 "투자: 46개 사업에 공공·민간 합쳐 약 211억 유로(237억 달러)의 투자가 필요합니다 [사실]",
 "목표: 2030년까지 연간 수요의 10% 채굴, 40% 가공, 25% 재활용이 목표이고, 기존 선정분과 합치면 리튬·희토류 기준은 맞출 수 있다고 집행위는 봤습니다 [사실]",
 "한계: 선정이 곧 자금 지원은 아니며, 개발사들은 8월 긴급 자금이 없으면 더 많은 사업이 무산될 수 있다고 경고했습니다 [사실]"],
"verified","선정 수·국가·투자액·구성은 Bruxelles2·MLex 등 검색 결과 요약으로 확인",
[{"o":"Bruxelles2","d":"2026-10-09","u":"https://www.bruxelles2.eu/en/article/321145"},
 {"o":"MLex","d":"2026-10-09","u":"https://www.mlex.com/mlex/trade/articles/2536072"}],
["metals"],[],
[T("EU 집행위, 핵심광물 전략사업 46곳 새로 선정","로이터","2026-10-09","https://www.reuters.com/business/aerospace-defense/european-commission-picks-46-new-strategic-critical-mineral-projects-2026-10-09/")])

add("C077","",
"이탈리아 8월 산업생산 1.3% 급감…보합 예상 크게 밑돌아",
"이탈리아 통계청이 발표한 8월 산업생산이 전월보다 1.3% 줄어 보합을 점친 시장 예상을 크게 밑돌았고, 최근 3개월 평균도 직전 3개월보다 1.1% 줄어 제조업 생산이 뒷걸음질하고 있다",
["무엇이: 이탈리아 통계청에 따르면 8월 계절조정 산업생산은 전월보다 1.3% 줄었습니다 [사실]",
 "예상: 분석가 11명 조사에서는 보합이 예상됐습니다 [사실]",
 "추세: 7월 증가율은 0.7%에서 0.6%로 하향됐고, 최근 3개월 평균은 직전 3개월보다 1.1% 줄었습니다 [사실]",
 "전년 대비: 달력 조정 지수는 2025년 8월과 같았습니다 [사실]"],
"verified","이탈리아 통계청 보도자료와 검색 결과 요약으로 확인",
[{"o":"이탈리아 통계청(ISTAT)","d":"2026-10-09","u":"https://www.istat.it/en/press-release/industrial-production-august-2026/"}],
["macro"],["macro/growth"],
[T("이탈리아 8월 산업생산, 예상과 달리 큰 폭으로 감소","로이터","2026-10-09","https://www.reuters.com/business/italy-industrial-output-dives-unexpectedly-august-2026-10-09/")])

add("C082","",
"가나, 광업법 초안 대신 수정안 낸다…특별지분 논란 속 소식통 전언",
"가나 정부가 국가 특별지분 조항 등으로 논란이 된 광업법 초안을 수정안으로 바꿔 낼 것으로 전해지면서, 금 광산 등 외국 광업사가 받을 투자 조건이 다시 바뀔 수 있다 (제목 기준)",
["무엇이: 가나가 광업법 초안을 수정안으로 바꿔 낼 것이라고 소식통들이 전했습니다 [제목]",
 "초안: 2026년 광물·광업 법안 초안은 국가의 10% 무상 지분을 유지하면서 장관 재량으로 주요 거래 동의권을 가진 특별지분을 요구할 수 있게 했습니다 [사실]",
 "논란: 가나 광업회의소는 10월 7일 초안의 광구 임대 기간 보도를 바로잡아 달라고 로이터에 요청했습니다 [사실]",
 "로열티: 가격에 따라 약 5~12%로 움직이는 광업 로열티 규정이 3월 10일부터 시행 중입니다 [사실]"],
"title","수정안 교체 자체는 독립 출처로 확인 못 함. 초안 내용·광업회의소 반발·로열티 규정은 검색 결과 요약으로 확인",
[{"o":"Citi Newsroom","d":"2026-10-07","u":"https://www.citinewsroom.com/2026/10/chamber-of-mines-asks-reuters-to-clarify-ghana-mining-bill-report/"},
 {"o":"WTS Global","d":"2026","u":"https://wts-global.com/publishing-article/ghana-new-royalty-regime-for-mining-industry~publishing-article"}],
["metals"],[],
[T("가나, 광업법 초안을 수정안으로 교체할 예정…소식통","로이터","2026-10-09","https://www.reuters.com/world/africa/ghana-replace-draft-mining-bill-with-revised-version-sources-say-2026-10-09/")])

d={"agent":"W5","searches_used":17,"fetches_used":0,"items":items,"skipped":[]}
json.dump(d,open(OUT,'w'),ensure_ascii=False,indent=1)
for x in items:
    n=len(re.sub(r' \((제목 기준|채널 전언)\)$','',x['one']))
    multi = len(x['items'])>1 or x['attachTo']
    lo,hi=(90,160) if multi else (80,130)
    tl=len(x['title'])
    bad=[f for f in x['facts'] if '|' in f or '**' in f]
    print(x['cid'],n,'OK' if lo<=n<=hi else f'BAD({lo}-{hi})','title',tl,'OK' if 20<=tl<=50 else 'BADT',[len(i['t']) for i in x['items'] if not 25<=len(i['t'])<=60],bad)
