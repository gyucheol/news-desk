import json, sys
P = '/home/user/news-desk/data/industry-2026-10-14/out/aero.json'
d = json.load(open(P, encoding='utf-8'))
N = {n['id']: n for n in d['nodes']}
def rep(obj, key, old, new):
    if old not in obj[key]: sys.exit(f'miss: {old}')
    obj[key] = obj[key].replace(old, new, 1)
it = d['intro']
rep(it, 'money', '{{20년 넘게 이어지는 정비·교체 부품(애프터마켓)}}', '20년 넘게 이어지는 {{정비·교체 부품(애프터마켓)}}')
rep(it, 'money', '{{운영비의 4분의 1~3분의 1 가까이}}', '운영비의 {{4분의 1~3분의 1 가까이}}')
rep(it, 'money', '{{정부와 맺는 다년 계약}}', '정부와 맺는 {{다년 계약}}')
rep(d, 'summary', '{{발사체·위성의 우주 사슬}}', '발사체·위성의 {{우주 사슬}}')
rep(d, 'summary', '{{무기 체계·미사일·탄약 주문}}', '{{무기 체계·미사일·탄약}} 주문')
rep(d, 'summary', '{{항공유 평균 배럴당 152달러}}', '항공유 평균 {{배럴당 152달러}}')
rep(d, 'summary', '{{올해 항공사 순이익 전망}}', '올해 {{항공사 순이익 전망}}')
rep(it['reading'][4], 'means', '{{투자만큼 늘어나는지}}', '투자만큼 {{늘어나는지}}')
rep(N['parts'], 'role', '{{애프터마켓 비중}}', '{{애프터마켓}} 비중')
c = d['cycle']
rep(c['why'][1], 't', '{{1년 새 560억에서 805억 유로}}', '1년 새 {{560억에서 805억 유로}}')
rep(c['why'][1], 't', '{{737 월 47대 증산 요건}}', '{{737 월 47대}} 증산 요건')
rep(c['why'][2], 't', '{{기업가치 180억 달러}}', '기업가치 {{180억 달러}}')
rep(c['why'][3], 't', '{{올해 순이익 전망}}', '올해 {{순이익 전망}}')
for co in N['munitions']['companies']:
    if co['n'] == 'RTX':
        co['note'] = '{{레이시온}}(미사일)·{{프랫앤휘트니}}(엔진)·{{콜린스}}(항공 부품)를 거느립니다. {{SM-3 최대 63억 달러 다년 계약}}을 {{따냈}}습니다'
for co in N['oem']['companies']:
    if co['n'].startswith('롤스로이스'):
        co['note'] = '{{광동체기 엔진(트렌트)}}을 만드는 {{영국 업체}}입니다. 최근 {{실적}}은 {{확인 못 함}}'
json.dump(d, open(P, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('patched')
