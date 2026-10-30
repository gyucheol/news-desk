"""2026-10-30 사용자 지시에 따른 안 읽은 뉴스 판정(사람이 제목·한줄을 읽고 정한 목록) -> decisions.json
사용: python3 -I decide.py <DB 사본 폴더>   (reads·news를 읽어 지금 안 읽은 문서인지 확인)"""
import json, sys, glob, datetime
DB = sys.argv[1]
# 매크로: 미국·일본도 지정학도 아님 -> 읽음 (다른 섹터에 해당하는 것은 아래 KEEP)
MACRO_READ = {
 'n-bbg-0530': '캐나다 금리', 'n-bbg-0542': '뉴질랜드 금리', 'n-bbg-0548': '브라질 물가', 'n-bbg-0621': '중국 기업 채무',
 'n-bbg-0630': '영국 국채 발행', 'n-bbg-0635': '세네갈 예산', 'n-bbg-0636': '인도 루피', 'n-bbg-0668': '유로존 PMI·ECB',
 'n-bbg-0669': '영국 소매판매', 'n-bbg-0677': '인도 PMI', 'n-bbg-0684': '캐나다 소매판매', 'n-bbg-0686': '싱가포르 물가',
 'n-bbg-0688': '페루 재정', 'n-bbg-0691': '러시아 중앙은행 금리', 'n-bbg-0692': '카자흐스탄 금리', 'n-bbg-0693': '호주 성장·고용',
 'n-bbg-0694': '영국 비상물자 권고(국내 대비책)', 'n-bbg-0727': '브라질 선거 뒤 증시(금융 겹침)', 'n-bbg-0754': '남아공 GDP',
 'n-bbg-0766': '영국 예산', 'n-bbg-0798': '베트남 국가 지분', 'n-bbg-0803': '폴란드 야당 발언(국내 정치)', 'n-bbg-0813': 'ECB 금리',
 'n-bbg-0822': '영국 예산', 'n-bbg-0823': '볼리비아 개혁', 'n-bbg-0826': '인도 중앙은행', 'n-bbg-0833': '홍콩달러 페그',
 'n-bbg-0834': '말레이시아 예산', 'n-bbg-0835': '캐나다 온타리오 재정', 'n-bbg-0674': '홍콩 증시(금융 겹침)',
 'n-rtr-0723': '토큰화 주식·스웨덴 중앙은행(금융 겹침)', 'n-rtr-0024': '브라질 헤알(금융 겹침)', 'n-rtr-0654': '이스라엘 금리',
 'n-rtr-0655': '콜롬비아 예산', 'n-rtr-0681': '영국 규제·관세 유예(국내 정책)', 'n-rtr-0711': '프랑스 국채', 'n-rtr-0725': '튀르키예 신용등급',
 'n-rtr-0726': '독일 세수', 'n-rtr-0727': '베네수엘라 IDB 연체', 'n-rtr-0728': '리비아 중앙은행 총재', 'n-rtr-0730': 'UAE·그리스 투자 협정',
 'n-tg-0742': '코스피(금융 겹침)', 'n-tg-0745': '중국 재정수입', 'n-tg-0825': '코스피 목표·원화(금융 겹침)', 'n-tg-0827': '위안화',
 'n-bbg-0673': '중국 AI 해외 확장(AI 긍정, 매크로는 중국)',
}
PHARMA_READ = ['n-bbg-0299', 'n-bbg-0327', 'n-bbg-0689', 'n-bbg-0690', 'n-bbg-0726', 'n-bbg-0739', 'n-bbg-0743', 'n-bbg-0814', 'n-bbg-0842',
 'n-bbg-0843', 'n-rtr-0052', 'n-rtr-0359', 'n-rtr-0627', 'n-rtr-0647', 'n-rtr-0658', 'n-rtr-0659', 'n-rtr-0660', 'n-rtr-0661', 'n-rtr-0718',
 'n-rtr-0722', 'n-rtr-0724', 'n-tg-0748', 'n-tg-0778', 'n-tg-0830', 'n-tg-0831', 'n-tg-0836']
# AI: 부정적이지 않은 AI 뉴스(모델 출시·매출 성장·도구) -> 읽음
AI_READ = {'n-tg-0214': '구글 제미나이 신모델 출시', 'n-tg-0312': '딥시크·문샷 신모델', 'n-tg-0713': 'AI 매출 추정 증가',
 'n-tg-0752': '대만 AI 공급망 긍정 평가', 'n-rtr-0732': '마이크로소프트 AI 진단 도구', 'n-tg-0780': '오픈AI 난제 증명·신모델'}
# 조건에 안 맞는 섹터가 있어도 다른 섹터에 해당해 안 읽음으로 둔 것
KEEP = {'n-bbg-0760': '매크로는 영국이지만 부동산(주택 지원·주택건설주)', 'n-bbg-0764': '매크로는 캐나다지만 부동산(주택시장)',
 'n-rtr-0430': '매크로는 독일이지만 원유·전력(전기세·정유소)', 'n-tg-0775': '매크로는 중국이지만 AI·반도체주 급락(AI 부정)',
 'n-rtr-0670': '제약이 겹치지만 소비재(비만약에 식음료 대응)', 'n-bbg-0832': '제약이 겹치지만 AI 부정(의료 AI 반대 여론)'}
reads = json.load(open(f'{DB}/data/users/me/reads.json'))['ids']
def upd(n):
    u = n.get('updatedAt')
    return int(datetime.datetime.fromisoformat(u.replace('Z', '+00:00')).timestamp() * 1000) if u else 0
docs = {json.load(open(p))['id']: json.load(open(p)) for p in glob.glob(f'{DB}/news/*.json')}
out = {'rule': '2026-10-30 사용자 지시: 매크로는 지정학이 아니면 미국·일본만, 제약·바이오 섹터 삭제(지금까지 내용 읽음), AI는 부정적인 내용만. '
               '안 읽은 문서 중 해당 없는 것은 읽음.', 'macro_read': [], 'pharma_read': [], 'ai_read': [], 'keep': []}
bad = []
for key, src in (('macro_read', MACRO_READ), ('pharma_read', {i: '제약·바이오' for i in PHARMA_READ}), ('ai_read', AI_READ), ('keep', KEEP)):
    for i, why in src.items():
        n = docs.get(i)
        if not n: bad.append(('missing', i)); continue
        unread = not (i in reads and reads[i] >= upd(n))
        if not unread: bad.append(('already read', i))
        out[key].append({'id': i, 'why': why, 'title': n.get('title', ''), 'processed': n.get('processed')})
ids = [x['id'] for k in ('macro_read', 'pharma_read', 'ai_read') for x in out[k]]
assert len(ids) == len(set(ids)), 'duplicate'
json.dump(out, open('decisions.json', 'w'), ensure_ascii=False, indent=1)
print({k: len(v) for k, v in out.items() if isinstance(v, list)}, 'to read', len(ids), 'problems', bad)
