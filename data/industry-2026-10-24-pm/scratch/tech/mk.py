import json,re
B='/home/user/news-desk/'
c=json.load(open(B+'work/nightly-2026-10-24/chains/tech.json'))
ids=[json.loads(l)['id'] for l in open(B+'data/industry-2026-10-24-pm/news/tech.jsonl')]
U=lambda s: re.sub(r'\{\{|\}\}','',s)
old=c['cycle']; R='https://www.reuters.com/'
ORNN='https://data.ornn.com/markets/h100-sxm'
OAI='https://t.me/TNBfolio/71677'
ANT=R+'legal/transactional/anthropic-ipo-stands-alone-ai-market-jitters-sideline-others-2026-10-22/'
META=R+'business/steep-bill-ai-buildout-punishes-meta-other-tech-favorites-2026-10-22/'
SPX=R+'business/media-telecom/spacex-seeks-access-80000-us-cell-sites-wireless-network-bloomberg-news-reports-2026-10-22/'
def st(d,o,u,nid,t): return {"d":d,"o":o,"u":u,"nid":nid,"t":t}
state={
"cloud":[st("2026-10-23","텔레그램 하나증권 중국전략","https://t.me/HANAchina/70899","n-rtr-0714","ORTEX 집계로 네오클라우드·데이터센터 공매도는 10월 60억 달러 평가이익을 냈고, 코어위브 무담보채 수익률은 약 15%, 자금 부족분 추정은 230억~760억 달러로 엇갈렸습니다 [채널]"),
         st("2026-10-22","블룸버그","https://www.bloomberg.com/news/articles/2026-10-22/ai-data-center-backlash-threatens-australia-s-70-billion-dream","n-rtr-0715","시드니·멜버른에 계획·건설 중인 대형 데이터센터 40여 곳(약 700억 달러) 가운데 전력 연결을 공개 확인한 곳은 23%뿐이고, 한 개발사는 12억 호주달러 사업을 접었습니다 [사실]")],
"ai":[st("2026-10-23","텔레그램 TNBfolio",OAI,"n-tg-0743","오픈AI는 투자자 저항에 이번 조달의 투자 전 기업가치 목표를 1조 4,000억 달러에서 1조 2,500억 달러로 낮췄고, 10월 30일 확약 마감 뒤 조달액이 300억 달러를 밑돌 수 있다고 채널이 전했습니다 [채널]"),
      st("2026-10-22","로이터",ANT,"n-bbg-0671","다른 AI 상장이 미뤄지는 가운데 앤트로픽은 10월 말 증권신고서 공개와 11월 중순 상장을 추진하며, IFR은 11월 9일 로드쇼 시작과 목표 기업가치 2조 달러를 전했습니다 [사실]")],
"software":[st("2026-10-23","로이터",R+"world/india/indias-coforge-posts-strong-quarterly-growth-encora-integration-deal-momentum-2026-10-23/","n-bbg-0676","인포시스는 기업 IT 지출 억제로 연간 매출 전망을 낮췄고, 코포지 2분기 매출은 6억 5,220만 달러(+40.1%)였지만 대부분 인수 효과로 유기적 성장은 전 분기 대비 3.8%였습니다 [사실]"),
            st("2026-10-23","로이터",R+"business/media-telecom/japan-simulate-cyberattacks-php-flaws-roil-global-internet-2026-10-23/","n-rtr-0713","AI 도구가 찾아낸 PHP 결함 php2shell 공개 뒤 클라우드플레어는 2시간 만에 수십만 건의 공격 시도를, 팔로알토는 잠재 취약 인스턴스 2,260만 개를 집계했습니다 [사실]")],
"devices":[st("2026-10-23","로이터",R+"business/retail-consumer/apple-bets-iphone-duo-can-remake-foldable-market-sales-begin-2026-10-22/","n-tg-0234","아이폰 듀오가 10월 23일 1,999달러에 매장 판매를 시작했고 애플은 12개월 출하 목표를 970만 대에서 1,400만 대로 44% 올렸다고 전해졌지만, 9월 조립 수율은 60%를 조금 넘었습니다 [사실]"),
           st("2026-10-22","로이터",R+"world/us-blocks-two-devices-with-chinese-made-surveillance-chips-2026-10-22/","n-rtr-0672","FCC는 10월 13일 발효된 규정에 따라 하이실리콘 감시칩이 든 대시보드 카메라·무선 영상 송신기 2종의 미국 시장 진입을 처음 막았습니다 [사실]")],
"telecom":[st("2026-10-22","로이터",SPX,"n-bbg-0428","FCC가 스페이스X의 1695~1710MHz 15MHz 면허 인수를 승인하고 구축 의무를 면제했으며, 미국 기지국 8만 곳 접근 협상 보도에 T모바일·AT&T는 5% 가까이 내렸습니다 [사실]"),
           st("2026-10-23","블룸버그","https://www.bloomberg.com/news/articles/2026-10-23/rogers-beats-on-sports-revenue-as-wireless-remains-sluggish","n-bbg-0696","캐나다 로저스는 스포츠 매출 덕에 예상을 웃돌았지만 본업인 무선 부문 부진이 이어졌습니다 [제목]")],
"platforms":[st("2026-10-22","로이터",META,"n-bbg-0448","메타 5년물 CDS는 실적 뒤 약 119.3bp로 거래 시작 이래 최고였고, 메타가 공개한 리스·계약 지출 약정은 약 8,250억 달러로 7월 약 7,000억 달러에서 늘었습니다 [사실]"),
             st("2026-10-23","로이터",R+"world/india/indias-swiggy-falls-after-quick-commerce-losses-widen-during-second-quarter-2026-10-23/","n-bbg-0682","스위기 인스타마트 조정 EBITDA 손실이 89억 5천만 루피로 1분기 77억 8천만 루피에서 커져 주가가 장중 최대 17% 내렸고, 경쟁사 블링킷은 18억 4천만 루피 흑자였습니다 [사실]")],
"media":[st("2026-10-23","텔레그램 미국 주식 인사이더","https://t.me/insidertracking/67062","n-tg-0750","스포티파이 3분기 매출은 50억 유로(고정환율 +14%), 유료 구독자는 3억 600만 명이었고 매출총이익률 33%, 잉여현금흐름 7억 3,500만 유로였다고 채널이 전했습니다 [채널]"),
         st("2026-10-21","로이터",R+"legal/litigation/getty-images-says-investor-litigation-helped-push-it-bankruptcy-2026-10-22/","n-rtr-0203","게티이미지는 10월 21일 사전조정형 챕터11을 신청했고, 워런트 소송 판결·이자 2억 달러 넘는 부담과 약 21억 달러 부채가 원인으로 꼽혔으며 무담보채 2억 7천만 달러가 소각됩니다 [사실]")]}
ind=[
 {"d":"2026-10-22","kind":"price","o":"Ornn(검색 요약)","u":ORNN,"t":"Ornn H100 SXM 지수는 10월 22일 GPU당 시간당 3.15달러로 10월 2일 2.79달러, 10월 19일 2.98달러보다 높아 연산력 임대료는 아직 꺾이지 않았습니다 [사실]"},
 {"d":"2026-10-23","kind":"capex","o":"텔레그램 TNBfolio","u":OAI,"nid":"n-tg-0743","t":"오픈AI의 이번 조달 기업가치 목표는 1조 4,000억 달러에서 1조 2,500억 달러로 내려갔고 조달액은 300억 달러를 밑돌 수 있으며, 앤트로픽도 2조 달러 대신 약 1조 5,000억 달러가 거론됩니다 [채널]"},
 {"d":"2026-10-22","kind":"capex","o":"로이터","u":META,"nid":"n-bbg-0448","t":"메타의 리스·계약 지출 약정은 약 8,250억 달러로 7월 약 7,000억 달러에서 늘었고, 주요 하이퍼스케일러 합산 잉여현금흐름은 약 16억 달러 적자로 돌아섰다는 추정입니다 [채널]"},
 {"d":"2026-10-22","kind":"supply","o":"블룸버그","u":"https://www.bloomberg.com/news/articles/2026-10-22/ai-data-center-backlash-threatens-australia-s-70-billion-dream","nid":"n-rtr-0715","t":"호주 대형 데이터센터 40여 곳(약 1,000억 호주달러) 중 전력 연결을 공개 확인한 곳은 23%였습니다 [사실]"}]
flags=[
 {"nid":"n-tg-0741","t":"재검토 필요: 세미애널리시스의 GPU 일정 수준 공급 과잉·2028년 데이터센터 과잉 진단과 화타이의 1조 3,000억 달러 자금 부족 추정은 ③ 공급 과잉을 가리키지만, 채널 전언이고 H100 임대료가 아직 올라 판정은 그대로 둡니다 [유추]"},
 {"nid":"n-tg-0743","t":"재검토 필요: 오픈AI 기업가치 목표 1조 4,000억→1조 2,500억 달러 하향과 조달 미달 가능성은 AI 모델 노드의 ② 자본 유입이 정점을 지나 ③ 공급 과잉으로 가는 신호이며, 투자자 저항이 몸값을 깎기 시작했기 때문입니다 [유추]"}]
ow=[dict(t=U(w['t']),src=w['src']) for w in old['why']]
why=[
 {"t":"국면은 ② 자본 유입·증설로 두되 근거를 새 뉴스로 바꿨습니다. 다른 AI 상장이 미뤄지는 중에도 앤트로픽은 11월 중순 상장을 추진하고, 지오 플랫폼스 IPO는 인도 증시 급락 속에도 22.19배 청약돼 대형 상장 자금은 아직 몰립니다 [사실]",
  "src":[{"o":"로이터","d":"2026-10-22","u":ANT},{"o":"HDFC Sky(NSE 집계 인용)","d":"2026-10-23","u":"https://hdfcsky.com/news/jio-ipo-subscribed-22-19x-on-final-day"}]},
 {"t":"연산력은 아직 빠듯합니다. Ornn H100 지수는 10월 22일 GPU당 시간당 3.15달러로 10월 2일 2.79달러보다 높고, 앤트로픽 3분기 매출은 전분기보다 약 45% 늘었습니다 [사실]",
  "src":[{"o":"Ornn(검색 요약)","d":"2026-10-22","u":ORNN},{"o":"로이터","d":"2026-10-14","u":R+"business/finance/anthropics-q3-revenue-surges-45-nearly-17-billion-2026-10-14/"}]},
 {"t":"반대 신호는 더 쌓였습니다. 오픈AI가 기업가치 목표를 1조 2,500억 달러로 낮췄다는 전언이 나왔고, 메타 CDS가 약 119.3bp로 사상 최고였으며, 나스닥 3분기 신규 상장은 167건으로 1년 전 205건보다 줄었습니다 [사실]",
  "src":[{"o":"텔레그램 TNBfolio","d":"2026-10-23","u":OAI},{"o":"로이터","d":"2026-10-22","u":META},{"o":"로이터","d":"2026-10-22","u":R+"legal/transactional/nasdaq-ceo-flags-modest-softening-ipo-market-macro-uncertainty-hits-debuts-2026-10-22/"}]},
 {"t":"통신은 ⑥ 공급 파괴·통합입니다. 텔리아 감원·AT&T 멕시코 매각에 이어, FCC가 스페이스X 15MHz 인수를 승인하고 스페이스X가 기지국 8만 곳 접근을 협상한다는 보도에 T모바일·AT&T가 5% 가까이 내려 기존 통신사는 정리와 위성 진입자를 함께 맞습니다 [귀납]",
  "src":ow[3]['src'][:2]+[{"o":"로이터","d":"2026-10-22","u":SPX}]}]
cy={"stage":2,"conf":"중간","why":why,
 "next":U(old['next']).replace("앤트로픽 같은 대형 AI 상장이","앤트로픽(11월 중순) 같은 대형 AI 상장이"),
 "watch":["앤트로픽 상장(11월 중순)·오픈AI 조달 마감(10월 30일)의 기업가치","GPU 임대료 지수(Ornn H100)","코어위브·오라클·메타 CDS와 데이터센터 채권 가격","스마트폰·PC 출하와 아이폰 듀오 공급","통신사 감원·설비 정리와 위성 직접통신 주파수"],
 "split":old['split']}
ins={
"a2":[{"t":"정반대로 흐른다면 연산력 수요가 실제로 강해서입니다. Ornn H100 지수는 10월 22일 GPU당 시간당 3.15달러로 10월 2일 2.79달러보다 높고, 채권·상장 시장이 흔들리는 중에도 임대료가 오른 것은 이번 흔들림이 금리 충격에 따른 일시 조정에 그칠 수 있음을 뜻합니다 [유추]",
       "src":[{"o":"Ornn(검색 요약)","d":"2026-10-22","u":ORNN}]}],
"b":[old_b:=dict(t=U(c['insight']['b'][0]['t']),src=c['insight']['b'][0]['src']),
     {"t":"애플 안에서도 갈립니다. 아이폰 듀오는 10월 23일 1,999달러에 출시돼 12개월 출하 목표가 970만 대에서 1,400만 대로 44% 올랐다고 전해졌지만, 라간정밀은 주요 고객사의 11월 주문이 더 약해질 것으로 봐 1,355달러로 오른 프로 모델 수요가 부담으로 꼽혔습니다 [채널]",
      "src":[{"o":"로이터","d":"2026-10-22","u":R+"business/retail-consumer/apple-bets-iphone-duo-can-remake-foldable-market-sales-begin-2026-10-22/"},{"o":"블룸버그","d":"2026-10-23","u":"https://www.bloomberg.com/news/newsletters/2026-10-23/apple-s-iphone-duo-ushers-in-new-era-for-smartphones"}]}],
"c":[dict(t=U(c['insight']['c'][0]['t']),src=c['insight']['c'][0]['src']),
     {"t":"연산력 값도 아직 버팁니다. Ornn H100 지수는 10월 22일 GPU당 시간당 3.15달러로 10월 2일 2.79달러보다 높았고, 스포티파이처럼 AI 밖 구독 사업은 매출 14% 증가와 잉여현금흐름 7억 3,500만 유로를 냈습니다 [사실]",
      "src":[{"o":"Ornn(검색 요약)","d":"2026-10-22","u":ORNN},{"o":"텔레그램 미국 주식 인사이더","d":"2026-10-23","u":"https://t.me/insidertracking/67062"}]}],
"c1":[dict(t=U(c['insight']['c1'][0]['t']),src=c['insight']['c1'][0]['src']),
      {"t":"빚과 몸값 쪽 경계는 오히려 넓어졌습니다. 메타 CDS가 약 119.3bp로 사상 최고였고 지출 약정은 약 8,250억 달러로 늘었으며, 오픈AI는 기업가치 목표를 1조 2,500억 달러로 낮췄다는 전언이 나와 매출 증가만으로 업계의 자금 부담을 덮기는 어렵습니다 [귀납]",
       "src":[{"o":"로이터","d":"2026-10-22","u":META},{"o":"텔레그램 TNBfolio","d":"2026-10-23","u":OAI}]}]}
summary="기술·통신은 반도체를 산 클라우드가 연산력을 빌려주고, 그 위에서 AI 모델·기업용 소프트웨어·인터넷 플랫폼·미디어·게임이 기업과 소비자에게 서비스를 팔며, 기기와 통신망이 사용자와 서비스를 잇는 사슬입니다. 2026년 10월 하순에도 가장 빠듯한 곳은 연산력으로, Ornn H100 지수는 10월 22일 GPU당 시간당 3.15달러로 10월 초보다 높고 앤트로픽은 11월 중순 상장을 추진합니다. 다만 몸값과 빚 쪽은 더 흔들려, 오픈AI가 기업가치 목표를 1조 4,000억 달러에서 1조 2,500억 달러로 낮췄다는 전언이 나왔고 메타 CDS는 약 119.3bp로 사상 최고, 코어위브 무담보채 수익률은 약 15%이며 호주 대형 데이터센터는 23%만 전력 연결을 확인했습니다. 기기는 아이폰 듀오 출하 목표가 1,400만 대로 오른 반면 프로 모델 주문은 약해지고, 통신은 스페이스X가 주파수와 기지국 8만 곳 접근을 넓히는 사이 기존 사업자의 정리가 이어집니다."
gaps=U(c['gaps']).replace("WebSearch 18회(첫 작성 14회, 10월 17일 2회, 10월 19일 1회, 10월 21일 1회)","WebSearch 19회(첫 작성 14회, 10월 17일 2회, 10월 19일 1회, 10월 21일 1회, 10월 24일 1회)")
gaps+=" (8) 10월 24일 검색 1회로 Ornn H100 지수 10월 22일 3.15달러를 검색 요약으로 확인했고 지오 22.19배 청약은 금융 페이지 점검의 검색 결과를 옮겼습니다. 오픈AI 기업가치 하향(FT 인용)·세미애널리시스의 GPU 과잉 진단·하이퍼스케일러 FCF 16억 달러 적자는 채널 전언뿐이고, 인포시스의 새 연간 전망 수치는 기사 제목 수준이라 확인하지 못했습니다."
x={"id":"tech","summary":summary,"state":state,"industryState":ind,"flags":flags,"insight":ins,"cycle":cy,"nodeStage":{},"gaps":gaps,
"note":f"뉴스 {len(ids)}건 반영: 오픈AI 기업가치 목표 하향, 메타 CDS 사상 최고·지출 약정 8,250억 달러, 아이폰 듀오 출하 목표 1,400만 대. 국면 그대로(②, why 근거 교체), 근거 14줄, 수치 4줄, 재검토 신호 2건, 검색 1회",
"applied":ids,"searches":1,"fetches":0}
print(len(ids), sum(len(v) for v in state.values()))
json.dump(x,open(B+'data/industry-2026-10-24-pm/out/tech.json','w'),ensure_ascii=False,indent=1)
