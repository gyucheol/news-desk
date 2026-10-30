import json
R="https://www.reuters.com/"
def mk(cid,title,one,facts,inds,nodes,items,check="웹 검색 한도 소진으로 독립 출처 확인 못 함, 기사 제목 기준"):
    return {"cid":cid,"attachTo":"","title":title,"one":one+" (제목 기준)","facts":facts,"basis":"title","check":check,"src":[],"inds":inds,"nodes":nodes,"items":items}
out=[
mk("C282","탄자니아 금광 사망 사건, 런던 금 인증기관·정련사 상대 소송 중심에",
"탄자니아 금광에서 발생한 사망 사건이 런던의 금 인증기관과 정련사들을 상대로 한 소송의 핵심 쟁점이 되면서, 금 정련사의 공급망 책임과 원산지 인증 관리에 대한 압박이 커질 수 있다",
["무엇이: 탄자니아 금광 사망 사건이 런던 인증기관·정련사 상대 소송의 중심에 섬 [제목]","의미: 금 공급망 실사·인증 체계의 법적 책임이 쟁점화 [추론]"],
["metals"],[],[{"t":"탄자니아 금광 사망 사건, 런던 인증기관·정련사 상대 소송의 중심에","o":"로이터","d":"2026-10-08","u":R+"world/africa/tanzania-gold-mine-deaths-centre-case-against-london-accreditor-refiners-2026-10-07/"}]),
mk("C292","서클8, 스리 인수 제안 기한 연장 받아",
"서클8이 영국 인력파견업체 스리 인수 제안의 확정 기한을 연장받으면서, 인수 협상이 이어지게 됐고 스리의 매각 여부 결론은 뒤로 미뤄졌다",
["무엇이: 서클8이 스리 인수 제안 관련 기한을 연장받음 [제목]","의미: 확정 제안 여부 결정 시점이 늦춰짐 [추론]"],
["industrial"],[],[{"t":"서클8, 스리 인수 제안 기한 연장 받아","o":"로이터","d":"2026-10-08","u":R+"world/uk/circle8-gets-deadline-extension-sthree-takeover-bid-2026-10-07/"}]),
mk("C302","콜롬비아, 연기금 해외투자 상한 법령 철회",
"콜롬비아 정부가 연기금의 해외투자에 상한을 두는 법령을 철회하면서, 연기금이 해외 자산 비중을 유지하거나 늘릴 길이 열려 페소화와 국내 자산시장 수급에 영향을 줄 수 있다",
["무엇이: 콜롬비아가 연기금 해외투자 상한 법령을 철회 [제목]","영향: 연기금 자금의 국내 송환 압력이 줄어 환율·국내 자산 수급에 영향 가능 [추론]"],
["macro"],["macro/fx","macro/liquidity"],[{"t":"콜롬비아, 연기금 해외투자 상한 법령 철회","o":"로이터","d":"2026-10-07","u":R+"business/colombia-revokes-decree-capping-pension-funds-foreign-investments-2026-10-07/"}]),
mk("C312","라코스테, 파리 패션쇼 앞두고 CEO 해임",
"프랑스 패션 브랜드 라코스테가 파리 런웨이 쇼를 앞두고 최고경영자를 해임했다고 소식통들이 전하면서, 브랜드 경영과 전략 방향에 공백이 생길 수 있다",
["무엇이: 라코스테가 파리 런웨이 쇼를 앞두고 CEO를 해임했다고 소식통들이 전함 [제목]","의미: 새 경영자 선임 전까지 경영 공백 [추론]"],
["consumer"],[],[{"t":"소식통 \"프랑스 브랜드 라코스테, 파리 런웨이 쇼 앞두고 CEO 해임\"","o":"로이터","d":"2026-10-07","u":R+"business/retail-consumer/french-brand-lacoste-fired-ceo-ahead-paris-runway-show-sources-say-2026-10-07/"}]),
mk("C322","BHP, 캄발다 니켈 선광장·광구 골드필즈에 매각",
"BHP가 서호주 캄발다의 니켈 선광 설비와 광구를 골드필즈에 매각하기로 하면서, 니켈값 부진 속 니켈 사업 정리가 이어지고 골드필즈는 금 사업 기반을 넓히게 된다",
["무엇이: BHP가 캄발다 니켈 선광장과 광구를 골드필즈에 매각 [제목]","배경: BHP는 니켈값 하락으로 서호주 니켈 사업을 축소해 왔음 [추론]"],
["metals"],[],[{"t":"BHP, 캄발다 니켈 선광장·광구를 골드필즈에 매각","o":"로이터","d":"2026-10-07","u":R+"legal/transactional/bhp-sell-kambalda-nickel-concentrator-tenements-gold-fields-2026-10-06/"}]),
mk("C332","튀르키예 중앙은행 총재 \"디스인플레이션 다시 속도…신중 기조 유지\"",
"튀르키예 중앙은행 총재가 물가 둔화가 다시 속도를 낼 것이라며 신중한 통화정책 기조를 유지하겠다고 밝히면서, 리라화 자산에 대한 급격한 금리 인하 기대는 제한될 수 있다",
["무엇이: 튀르키예 중앙은행 총재가 디스인플레이션이 다시 속도를 낼 것이라고 언급 [제목]","정책: 신중한 정책 기조 유지 [제목]","영향: 빠른 금리 인하 기대가 제한될 수 있음 [추론]"],
["macro"],["macro/cb","macro/inflation"],[{"t":"튀르키예 중앙은행 총재 \"신중 기조 속 디스인플레이션 다시 속도 낼 것\"","o":"로이터","d":"2026-10-07","u":R+"world/middle-east/turkey-central-bank-governor-says-disinflation-regain-pace-cautious-stance-2026-10-06/"}])]
json.dump(out,open('/home/user/news-desk/data/sm-2026-10-07-09/scratch/W6/b7.json','w'),ensure_ascii=False)
