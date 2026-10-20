"""매크로 산업 페이지 '연준 인사 발언' 칸의 처음 목록(chains/macro.fed). 사용자 지시 2026-10-15.
지난 뉴스(이미 저장된 문서의 원문·원문별 한 줄)와 연준 이사회 공식 연설 목록(10월)에서 옮김. 뉴스 문서는 고치지 않음.
사용: python3 -I mk_fed.py <DB 사본 macro.json> <출력 json>"""
import json, sys
R = json.load(open('/home/user/news-desk/tools/industry/fed_roster.json'))
W = {p['k']: p for p in R['people']}
B = 'https://www.bloomberg.com/news/articles/'; RT = 'https://www.reuters.com/'
FB = 'https://www.federalreserve.gov/newsevents/speech/'
def e(d, k, kind, stance, t, u, o, nid='', who='', role=''):
    p = W.get(k, {})
    return {'d': d, 'k': k, 'who': who or p.get('n', ''), 'role': role or p.get('role', ''), 'kind': kind, 'stance': stance, 't': t, 'u': u, 'o': o, **({'nid': nid} if nid else {})}
X = [
 e('2026-10-01', 'Warsh', '관련 뉴스', '', "트럼프가 '내가 워시였다면 인상에 반대표'라며 인상 책임을 연준 이사회로 돌렸다", B + '2026-10-01/trump-says-warsh-should-have-voted-against-fed-s-rate-hike', '블룸버그', 'n-bbg-0052'),
 e('2026-10-01', 'Waller', '연설', '', "연설 제목은 '데이터판 고질라 대 콩: FRED가 AI에 맞서다'다", FB + 'waller20261001a.htm', '연준 공식 이사회'),
 e('2026-10-02', 'Jefferson', '연설', '중립', '물가 위험은 위로 기울었지만 다음 조정은 데이터를 보고 판단하며 시간이 더 걸릴 수 있다고 했다', FB + 'jefferson20261001a.htm', '연준 공식 이사회', 'n-bbg-0052'),
 e('2026-10-02', 'Bowman', '연설', '', "연설 제목은 '금융규제 현대화: eSLR에 대한 첫 관찰'이다", FB + 'bowman20261001a.htm', '연준 공식 이사회'),
 e('2026-10-03', 'Powell', '인사·독립성', '', '트럼프가 연준 본부 공사비 초과를 들어 파월 전 의장의 사임을 압박했다', 'https://t.me/insidertracking/65257', '텔레그램 미국 주식 인사이더', 'n-tg-0165'),
 e('2026-10-06', 'Bowman', '연설', '', "연설 제목은 '규제·감독 환경의 현대화'다", FB + 'bowman20261006a.htm', '연준 공식 이사회'),
 e('2026-10-06', 'Warsh', '관련 뉴스', '', '하원 중국특위 위원장이 워시 의장에게 홍콩의 연준 달러 창구 이용 재검토를 요구했다', B + '2026-10-06/us-lawmaker-seeks-review-of-hong-kong-s-access-to-fed-facility', '블룸버그', 'n-bbg-0074'),
 e('2026-10-07', 'Daly', '발언', '중립', '추가 인상이 필요한지는 충격이 어떻게 전개되느냐에 달려 있다고 했다', RT + 'business/feds-daly-need-more-hikes-hinges-what-happens-with-shocks-2026-10-06/', '로이터', 'n-bbg-0052'),
 e('2026-10-07', 'Bowman', '감독·규제', '', '지역 연은 총재 대신 5개 권역 책임자가 은행 감독을 총괄하도록 체계를 바꾸겠다고 밝혔다', RT + 'business/finance/fed-plans-overhaul-bank-supervision-responsibilities-bowman-says-2026-10-06/', '로이터', 'n-rtr-0171'),
 e('2026-10-07', '', '조사·보고서', '', '9월 소비자 기대 조사에서 1년 뒤 물가 예상이 3.9%로 2023년 5월 이후 최고였다', B + '2026-10-07/one-year-inflation-expectations-reach-three-year-high-ny-fed', '블룸버그', 'n-bbg-0097', '뉴욕연은', '소비자 기대 조사'),
 e('2026-10-07', '', '관련 뉴스', '', '법원이 라디언트 월드 사건과 관련해 뉴욕연은 결제 기록 소환을 허가했다', RT + 'legal/government/us-judge-authorizes-fund-subpoena-new-york-fed-documents-related-radiant-world-2026-10-06/', '로이터', 'n-rtr-0165', '뉴욕연은', '법원 소환'),
 e('2026-10-08', '', '성명·의사록', '매파', '9월 인상은 12대 0이었고 대부분이 연내 한 번 더 인상이 적절하다고 본 것으로 나타났다', B + '2026-10-07/fed-minutes-show-hawkish-unity-behind-september-rate-hike', '블룸버그', 'n-bbg-0090', 'FOMC', '9월 회의 의사록'),
 e('2026-10-08', '', '성명·의사록', '', '위원들이 인상 논리를 두고 의견이 갈렸고 일부는 시장 스트레스 대비를 원한 것으로 나타났다', RT + 'business/fed-policymakers-divided-over-rate-hike-logic-september-minutes-show-2026-10-07/', '로이터', 'n-bbg-0052', 'FOMC', '9월 회의 의사록'),
 e('2026-10-08', 'Waller', '연설', '매파', '데이터가 예상대로면 추가 인상을 예상하지만 연속 회의 인상일 필요는 없다고 했다', FB + 'waller20261008a.htm', '연준 공식 이사회', 'n-bbg-0052'),
 e('2026-10-09', 'Musalem', '발언', '매파', '물가를 낮추려면 추가 금리 인상이 필요하다고 했다', RT + 'markets/us/feds-musalem-says-lowering-inflation-will-require-more-rate-hikes-2026-10-08/', '로이터', 'n-bbg-0052'),
 e('2026-10-09', '', '조사·보고서', '', '관세가 없었다면 2월 물가가 하락해 디플레이션 영역이었을 것이라는 분석이 전해졌다', 'https://t.me/The_MariTimes/63607', '텔레그램 Polaristimes', 'n-bbg-0052', '뉴욕연은', '연구(채널 전언)'),
 e('2026-10-09', '', '인사·독립성', '', '트럼프의 연준 이사 후보였던 주디 셸턴이 베선트 재무장관 자문을 맡았다', RT + 'world/china/trumps-fed-ex-nominee-shelton-advise-bessent-treasury-says-2026-10-09/', '로이터', 'n-rtr-0232', '주디 셸턴', '전 연준 이사 후보'),
 e('2026-10-10', 'Cook', '인사·독립성', '', '트럼프가 쿡 이사를 조사할 백악관 위원회를 출범시켜 해임을 다시 추진했다', RT + 'world/us/trump-launches-committee-probe-feds-lisa-cook-white-house-statement-2026-10-09/', '로이터', 'n-rtr-0232'),
 e('2026-10-10', 'Cook', '인사·독립성', '', '쿡 이사 변호인단이 청문에서 주택담보대출 사기가 아님을 보이겠다고 했다', RT + 'legal/government/feds-cook-lawyers-say-hearing-will-show-no-mortgage-fraud-case-2026-10-09/', '로이터', 'n-rtr-0232'),
 e('2026-10-12', 'Warsh', '관련 뉴스', '', '채권 트레이더들이 금리 경로의 단서로 CPI와 워시 의장 발언을 주목했다', B + '2026-10-11/us-bond-traders-await-cpi-warsh-for-insight-on-fed-s-rate-path', '블룸버그', 'n-bbg-0052'),
 e('2026-10-13', 'Hammack', '발언', '매파', '작고 잦은 금리 조정이 낫다며 긴축을 지지했고 비교적 빨리 하는 게 낫다고 했다', B + '2026-10-12/fed-s-hammack-says-smaller-frequent-rate-adjustments-preferable', '블룸버그', 'n-bbg-0052'),
 e('2026-10-13', 'Goolsbee', '발언', '매파', '물가가 오를 때 금리 동결은 실질적 인하이고 기업 투자는 놀랍도록 강하다고 했다', 'https://t.me/The_MariTimes/63686', '텔레그램 Polaristimes', 'n-bbg-0052'),
 e('2026-10-13', 'Goolsbee', '인터뷰', '매파', 'AI발 인플레이션이 데이터센터 공급망 밖으로 번지고 있다고 경고했다', RT + 'business/goolsbee-says-ai-induced-inflation-is-jumping-out-its-lane-semafor-reports-2026-10-13/', '로이터', 'n-bbg-0052'),
 e('2026-10-13', 'Waller', '발언', '중립', '장기 국채금리 상승이 주택·자동차 수요를 눌러 연준 긴축을 일부 대신할 수 있다고 했다', B + '2026-10-13/fed-s-waller-says-higher-yields-could-help-fed-cool-demand', '블룸버그', 'n-bbg-0242'),
 e('2026-10-13', 'Waller', '발언', '중립', '기대인플레이션은 잘 고정돼 있어 금리 상승이 물가 불안 신호는 아니라고 했다', RT + 'markets/asia/us-inflation-expectations-are-well-anchored-feds-waller-says-2026-10-13/', '로이터', 'n-bbg-0242'),
 e('2026-10-13', 'Waller', '발언', '', '국채 안전자산 프리미엄이 사라져 금리에 50~70bp 상승 압력이 생겼을 수 있다고 했다', 'https://t.me/insidertracking/66122', '텔레그램 미국 주식 인사이더', 'n-bbg-0242'),
 e('2026-10-13', 'Waller', '발언', '', '프랑스 재정 압박을 경고로 보면서도 미국은 성장과 해외 자금 유입으로 버틸 수 있다고 했다', B + '2026-10-13/blackstone-s-gray-fed-s-waller-see-warning-from-france-s-stress', '블룸버그', 'n-bbg-0111'),
 e('2026-10-14', 'Williams', '인터뷰', '중립', '연내 1회 추가 인상은 적절하지만 현재로선 2027년 인상은 필요 없다고 봤다', B + '2026-10-13/fed-s-williams-currently-sees-no-need-for-rate-hike-in-2027', '블룸버그', 'n-bbg-0052'),
 e('2026-10-14', 'Williams', '발언', '중립', '실질 중립금리를 1% 안팎으로 보며 현 금리가 중립에서 멀지 않다고 했다', 'https://t.me/TNBfolio/71530', '텔레그램 TNBfolio', 'n-bbg-0052'),
 e('2026-10-14', 'Williams', '발언', '', 'AI 인프라 투자가 반도체값·건설비를 올리지만 경제 전반의 과열은 아니라고 했다', 'https://t.me/insidertracking/66135', '텔레그램 미국 주식 인사이더', 'n-bbg-0052'),
 e('2026-10-14', 'Collins', '발언', '매파', '물가를 잡으려면 올해 금리가 더 오를 가능성이 크다며 연말 전 추가 인상을 열어 뒀다', B + '2026-10-13/fed-s-collins-sees-higher-rates-likely-this-year-to-tame-prices', '블룸버그', 'n-bbg-0052'),
 e('2026-10-14', 'Barkin', '발언', '매파', '콜린스와 함께 물가 압력이 이어진다며 통화정책 대응을 강조한 것으로 전해졌다', 'https://t.me/insidertracking/66135#barkin', '텔레그램 미국 주식 인사이더', 'n-bbg-0052'),
 e('2026-10-14', 'Cook', '인사·독립성', '', '쿡 이사 변호인이 조사위원회의 공정성을 문제 삼고 11월 5일 청문 연기를 요구했다', RT + 'world/us/lawyer-feds-cook-denounces-trumps-latest-attempt-remove-her-2026-10-13/', '로이터', 'n-rtr-0232'),
 e('2026-10-15', 'Bowman', '연설', '', "연설 제목은 '실리콘밸리은행 이후의 감독 현대화'다", FB + 'bowman20261014a.htm', '연준 공식 이사회'),
]
for x in X:
    assert x['who'] and x['role'] and x['t'].endswith('다') and 15 <= len(x['t']) <= 80, x['t']
assert len({x['u'] for x in X}) == len(X)
fed = {'asOf': '2026-10-15', 'note': R['note'] + ' 처음 목록은 10월 1~15일 저장된 뉴스의 원문·원문별 한 줄과 연준 이사회 공식 연설 목록에서 옮김(연설은 제목만 옮긴 것과 원문을 읽고 요약한 것이 섞여 있음).',
       'src': R['src'], 'roster': R['people'], 'items': sorted(X, key=lambda x: x['d'])}
c = json.load(open(sys.argv[1])); c['fed'] = fed
c['history'] = c.get('history', []) + [{'rev': '2026-10-15', 'note': "사용자 요청으로 '연준 인사 발언' 칸 추가: 의장·부의장·이사·지역 연은 총재 발언과 FOMC·연준 인사 관련 뉴스 " + str(len(X)) + '건(10월 1~15일), FOMC 명단은 연준 이사회 FOMC 페이지 기준'}]
json.dump(c, open(sys.argv[2], 'w'), ensure_ascii=False, indent=1)
print(len(X), 'items', len(json.dumps(c, ensure_ascii=False).encode()), 'bytes')
