import json
c=json.load(open('/home/user/news-desk/work/nightly-2026-10-20/chains/tech.json'))
oc=c['cycle']; ins=c['insight']
def strip(a): return {"t":a["t"].replace('{{','').replace('}}',''),"src":a["src"]}
JIO={"o":"로이터","d":"2026-10-19","u":"https://www.reuters.com/legal/transactional/indias-jio-ipo-anchor-investor-quota-nearly-30-times-oversubscribed-source-says-2026-10-19/"}
ANT={"o":"로이터","d":"2026-10-18","u":"https://www.reuters.com/business/anthropic-commit-5-stake-new-public-benefit-fund-2026-10-18/"}
NS={"o":"블룸버그","d":"2026-10-19","u":"https://www.bloomberg.com/news/newsletters/2026-10-19/ai-s-premium-valuations-are-getting-more-pushback-from-investors"}
NS2={"o":"텔레그램 하나증권 중국전략","d":"2026-10-19","u":"https://t.me/HANAchina/70675"}
SP={"o":"로이터","d":"2026-10-19","u":"https://www.reuters.com/business/top-hyperscalers-likely-have-more-ai-linked-debt-than-now-known-sp-global-warns-2026-10-19/"}
CW={"o":"블룸버그","d":"2026-10-19","u":"https://www.bloomberg.com/news/articles/2026-10-19/coreweave-upgraded-to-buy-at-goldman-on-overblown-debt-worries"}
SX={"o":"로이터","d":"2026-10-09","u":"https://www.reuters.com/business/media-telecom/us-european-telecom-stocks-slide-spacex-spectrum-deal-rattles-sector-2026-10-09/"}
EU4={"o":"텔레그램 미국 주식 인사이더","d":"2026-10-19","u":"https://t.me/insidertracking/66691"}
BOFA={"o":"텔레그램 미국 주식 인사이더","d":"2026-10-13","u":"https://t.me/insidertracking/66100"}
GT={"o":"텔레그램 트릴리온","d":"2026-10-15","u":"https://t.me/Trillion_labs/10537"}
DS={"o":"로이터","d":"2026-10-19","u":"https://www.reuters.com/technology/us-banning-chinese-ai-deepseek-government-agency-it-systems-2026-10-19/"}
MM={"o":"텔레그램 미국 주식 인사이더","d":"2026-10-20","u":"https://t.me/insidertracking/66719"}
SM={"o":"로이터","d":"2026-10-13","u":"https://www.reuters.com/business/retail-consumer/global-smartphone-shipments-record-worst-third-quarter-14-years-amid-memory-2026-10-12/"}
DXC={"o":"로이터","d":"2026-10-19","u":"https://www.reuters.com/legal/transactional/dxc-advanced-talks-sell-insurance-software-unit-24-billion-sources-say-2026-10-19/"}
VK={"o":"텔레그램 상상인 김진범","d":"2026-10-19","u":"https://t.me/PipeBeom/6742"}
GS={"o":"텔레그램 하나증권 중국전략","d":"2026-10-13","u":"https://t.me/HANAchina/70365"}
def st(src,nid,t): return {"d":src["d"],"o":src["o"],"u":src["u"],"nid":nid,"t":t}
cycle={"stage":2,"conf":"중간",
"why":[
 {"t":"국면은 ② 자본 유입·증설로 두되 근거를 새 뉴스로 바꿨습니다. 상장 자금은 아직 몰립니다. 지오 플랫폼스 앵커 물량에 GIC·블랙록 등 약 250억 달러가 몰려 배정분의 약 30배였고, 앤트로픽은 11월 상장을 앞두고 지분 5% 공익기금 출연을 밝혔습니다 [사실]","src":[JIO,ANT]},
 strip(oc['why'][1]),
 {"t":"반대 신호는 더 쌓였습니다. 엔스케일 IPO에서 일부 투자자는 목표 기업가치 약 300억 달러 대신 160억~190억 달러를 제시했고, S&P는 상위 하이퍼스케일러가 드러난 것보다 많은 AI 부채를 지고 있을 것이라고 경고했습니다 [사실]","src":[NS,SP]},
 {"t":"통신은 ⑥ 공급 파괴·통합입니다. 텔리아 감원·AT&T 멕시코 매각에 이어, 스페이스X가 800MHz 주파수를 사들이자 STOXX 600 통신지수가 3.3% 내려 기존 통신사는 정리와 위성 신규 진입자를 동시에 맞게 됐습니다 [귀납]","src":[oc['why'][3]['src'][0],oc['why'][3]['src'][1],SX]}],
"next":oc['next'].replace('{{','').replace('}}',''),
"watch":["AI 기업 상장·공모가 대비 주가(앤트로픽·지오·엔스케일)","GPU 임대료 지수","코어위브·오라클 CDS와 데이터센터 채권 가격","스마트폰·PC 출하","통신사 감원·설비 정리와 위성 직접통신 주파수"],
"split":oc['split']}
x={"id":"tech","summary":"",
"state":{
 "cloud":[st(NS,"n-bbg-0453","엔스케일 IPO에서 일부 투자자가 목표 기업가치 약 300억 달러 대신 160억~190억 달러를 제시했고, 계약 1,030억 달러의 약 85%가 마이크로소프트·앤트로픽에 몰려 있습니다 [사실]"),
          st(VK,"n-tg-0492","우크라이나 드론이 상트페테르부르크 일대를 공격해 VK 데이터센터 등 데이터센터 2곳에 대형 화재가 났고, 데이터센터가 전쟁 표적으로 넓어지고 있습니다 [채널]")],
 "ai":[st(DS,"n-tg-0323","미 국토안보부가 연방 민간기관에 딥시크 제품과 딥시크 기반 제3자 제품을 지우고 구매·계약하지 말라고 명령했고, 민간 기업·소비자에는 적용되지 않습니다 [사실]"),
       st(MM,"n-tg-0323","미니맥스 M3.1 플래시는 추론 속도를 약 3배 높이고 사용 비용을 70% 낮췄으며, API 가격은 입력 100만 토큰당 1위안, 출력 4위안입니다 [채널]")],
 "telecom":[st(EU4,"n-bbg-0103","도이치텔레콤·오렌지·텔레포니카·보다폰이 스타링크에 맞서 유럽 위성 이동통신 주파수 공동 입찰을 검토하는 구속력 없는 의향서를 맺었고, AST 스페이스모바일도 함께했습니다 [사실]")],
 "devices":[st(SM,"n-rtr-0474","메모리 부족 속에 세계 3분기 스마트폰 출하가 1년 전보다 약 20% 줄어 14년 만의 최악이었고, 샤오미 출하는 30% 넘게 줄었습니다 [사실]")],
 "software":[st(DXC,"n-rtr-0360","액센츄어의 중국 사업 매각 검토에 이어 DXC가 보험 소프트웨어 부문을 24억 달러에 파는 막바지 협상을 하고 있습니다 [제목]")]},
"industryState":[
 {"d":"2026-10-19","kind":"price","o":"로이터","u":JIO["u"],"nid":"n-bbg-0122","t":"지오 플랫폼스는 기업가치를 6월 기대보다 약 19% 낮춘 약 1,060억 달러로 잡았고, 앵커 물량에는 약 250억 달러가 몰려 배정분의 약 30배였습니다 [사실]"},
 {"d":"2026-10-19","kind":"price","o":"블룸버그","u":NS["u"],"nid":"n-bbg-0453","t":"엔스케일 IPO에 일부 투자자가 제시한 기업가치는 160억~190억 달러로 목표 약 300억 달러보다 40% 안팎 낮고, 회사는 최대 30억 달러 조달을 노립니다 [사실]"},
 {"d":"2026-10-19","kind":"price","o":"블룸버그","u":CW["u"],"nid":"n-bbg-0322","t":"오라클 5년 CDS는 260bp를 넘었고, 코어위브 2032년물은 1달러당 80센트 밑에 머물렀으며 골드만은 코어위브 목표가 106달러를 제시했습니다 [채널]"},
 {"d":"2026-10-20","kind":"price","o":"텔레그램 미국 주식 인사이더","u":MM["u"],"nid":"n-tg-0323","t":"미니맥스 M3.1 플래시 API는 입력 100만 토큰당 1위안, 출력 4위안으로 사용 비용을 70% 낮췄습니다 [채널]"}],
"flags":[
 {"nid":"n-bbg-0428","t":"재검토 필요: 스페이스X의 800MHz 주파수 인수와 유럽 4대 통신사·AST 공동 입찰 검토는 통신 노드에 새 자본이 들어오는 ② 자본 유입·증설 국면을 가리키며, 위성 직접통신이 정리 중인 지상망과 반대 방향이기 때문입니다 [유추]"},
 {"nid":"n-tg-0559","t":"재검토 필요: 골드만이 클라우드 자본지출 증가율 정점을 2026년 3분기로 보고 위험 신호 3개 중 2개가 켜졌다고 한 것은 ③ 공급 과잉 국면을 가리키며, 증설 속도가 꺾이면 이미 지은 설비가 수요를 앞지를 수 있기 때문입니다 [유추]"}],
"insight":{
 "a":[strip(ins['a'][0]),strip(ins['a'][1]),
  {"t":"통신에는 위성 직접통신이라는 새 경쟁자가 들어옵니다. 스페이스X의 800MHz 인수 뒤 도이치텔레콤이 7~8% 떨어졌고 유럽 4대 통신사는 AST와 공동 입찰을 검토하며, BofA는 미 후불 가입자 10%가 옮기면 아이폰 판매가 약 500만 대 줄 수 있다고 봤습니다 [사실]","src":[SX,EU4,BOFA]}],
 "a1":[{"t":"차입 비용이 오르면 신용이 약한 네오클라우드·데이터센터 개발사부터 상장과 가동이 늦어질 가능성이 높습니다. 엔스케일은 마이크로소프트의 영국 계약 철수에 이어 IPO 기업가치를 40% 안팎 깎으라는 요구를 받았고, 가트너는 네오클라우드 80% 이상이 2030년까지 독립 운영을 멈출 것으로 봤습니다 [유추]","src":ins['a1'][0]['src']+[NS,GT]}],
 "c":[strip(ins['c'][0]),
  {"t":"상장 시장의 문도 아직 열려 있습니다. 지오 플랫폼스 앵커 물량은 배정분의 약 30배가 몰렸고, 골드만은 시장이 조달 비용을 과대평가한다며 코어위브를 매수로 올렸습니다 [사실]","src":[JIO,CW]}]},
"cycle":cycle,"nodeStage":{},"gaps":"",
"note":"뉴스 46건 반영: 엔스케일 IPO 몸값 160억~190억 달러 요구, 지오 앵커 30배 청약, 스페이스X 800MHz 인수와 유럽 통신사 공동 대응, 미 정부 딥시크 퇴출. 국면 ② 그대로(통신 ⑥, why 3줄 교체), 근거 7줄, 수치 4줄, 인사이트 a·a1·c 고침, 재검토 신호 2건, 검색 0회",
"applied":[json.loads(l)['id'] for l in open('news/tech.jsonl')],"searches":0,"fetches":0}
json.dump(x,open('out/tech.json','w'),ensure_ascii=False,indent=1)
print(len(x['applied']))
