"""덤프(work/dump/*.jsonl)를 산업별 후보 파일(work/split/<산업>.txt)로 나눈다.

- 이미 카드로 쓴 글(seen)과 본문 30자 미만 글은 뺀다.
- 채널 사이에 같은 글이 퍼진 경우(앞 60자 동일)는 처음 것만 남긴다.
- 각 줄: 표시(N=한 번도 검토 안 한 구간, R=예전에 훑고 넘긴 구간)  채널/id  KST날짜  본문 앞 280자
사용: python3 tools/tg_split.py [시작날짜 KST, 기본 2026-07-01]
"""
import json, glob, os, re, sys, collections
from datetime import datetime

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'work')
START = sys.argv[1] if len(sys.argv) > 1 else '2026-07-01'

# 예전에 훑은 구간(진행 기록 progressPf·progressV4 기준): (시작 KST, 끝 KST 또는 끝 id)
#  - 8월 1일~소급 위치(backfill): 8개 채널, 9월 16일~10월 2일 21시: 새 글 읽기
BACKFILL_END = {'Badonions': 6390, 'HANAchina': 67521, 'Onionfarmer': 17799, 'PipeBeom': 6365,
                'TNBfolio': 71199, 'The_MariTimes': 62406, 'Trillion_labs': 7697, 'insidertracking': 60038}
NEW_END = {'Badonions': 7629, 'HANAchina': 69766, 'Onionfarmer': 17988, 'PipeBeom': 6592, 'TNBfolio': 71429,
           'The_MariTimes': 63459, 'Trillion_labs': 9927, 'cahier_de_market': 10912, 'insidertracking': 65217,
           'kkkontemp': 2726}
NEW_FROM = {'cahier_de_market': '2026-10-01', 'kkkontemp': '2026-10-01'}

def reviewed(ch, pid, day):
    if ch in BACKFILL_END and '2026-08-01' <= day and pid < BACKFILL_END[ch]:
        return True
    if ch in NEW_END and NEW_FROM.get(ch, '2026-09-16') <= day and pid < NEW_END[ch]:
        return True
    return False

KW = {
 'power': '전력,전력망,송전,배전,변압기,발전기,가스터빈,터빈,ESS,배터리,저장장치,태양광,폴리실리콘,풍력,데이터센터,PJM,ERCOT,계통,전기요금,전력수요,유틸리티,grid,power,transformer,turbine,solar,battery,BESS',
 'uranium': '우라늄,원전,원자력,원자로,SMR,농축,카메코,센트러스,웨스팅하우스,핵연료,uranium,nuclear,reactor,enrich',
 'gas': 'LNG,천연가스,가스,헨리허브,TTF,JKM,카타르,액화,재기화,파이프라인,가스관,natural gas',
 'coal': '석탄,유연탄,원료탄,점결탄,발전용 석탄,제철,철강,철광석,coal,coking,steel',
 'drilling': '시추,리그,해양플랜트,FPSO,유정관,OCTG,셰일,업스트림,오일서비스,시추선,rig count,drilling,offshore,subsea,shale',
 'petchem': '석유화학,화학,에틸렌,나프타,크래커,폴리머,정유,정제마진,크랙,경유,디젤,휘발유,refin,crack,diesel,chemical,ethylene',
 'jpins': '일본,BOJ,일본은행,엔화,엔/달러,JGB,일본 국채,보험,생보,손보,재보험,Japan,yen,insur',
 'beauty': '화장품,뷰티,K-뷰티,스킨케어,아모레,코스맥스,한국콜마,ODM,cosmetic,beauty',
 'macro': '연준,Fed,FOMC,금리,국채,기준금리,인플레,물가,CPI,PCE,고용,실업,관세,재정,부채,환율,달러,유가,원유,브렌트,WTI,OPEC,호르무즈,이란,제재,경기침체,PMI,GDP,신용,스프레드,유동성,yield,inflation,tariff,treasury',
 'semis': '반도체,메모리,HBM,D램,DRAM,낸드,NAND,HDD,TSMC,엔비디아,NVIDIA,마이크론,하이닉스,삼성전자,AI 투자,capex,CAPEX,설비투자,데이터센터 투자,GPU,ASML,파운드리,AI 서버',
}
KW = {k: v.split(',') for k, v in KW.items()}

def tags(x):
    """대문자가 섞인 키워드(ESS, Fed, LNG 등)는 대소문자를 구분해 찾는다 — 'ess'가 'business'에 걸리지 않게."""
    xl = x.lower()
    hit = lambda w: (w in x) if any(c.isupper() for c in w) else (w in xl)
    return [k for k, ws in KW.items() if any(hit(w) for w in ws)]

out = collections.defaultdict(list); cnt = collections.Counter(); dup = set()
stat = collections.defaultdict(collections.Counter)
for f in sorted(glob.glob(os.path.join(ROOT, 'dump', '*.jsonl'))):
    ch = os.path.basename(f)[:-6]
    for line in open(f):
        r = json.loads(line); day = r['t'][:10]
        if day < START: continue
        x = re.sub(r'\s+', ' ', r['x']).strip()
        st = stat[ch]; st['all'] += 1
        if r.get('seen'): st['carded'] += 1; continue
        if len(x) < 30: st['short'] += 1; continue
        key = x[:60]
        if key in dup: st['dup'] += 1; continue
        dup.add(key)
        rv = reviewed(ch, r['id'], day); st['R' if rv else 'N'] += 1
        tg = tags(x)
        if not tg: st['notag'] += 1; continue
        for t in tg:
            out[t].append((r['t'], f"{'R' if rv else 'N'}\t{ch}/{r['id']}\t{r['t'][5:16].replace('T', ' ')}\t{x[:280]}"))
os.makedirs(os.path.join(ROOT, 'split'), exist_ok=True)
for t, rows in out.items():
    rows.sort()
    open(os.path.join(ROOT, 'split', f'{t}.txt'), 'w').write('\n'.join(r for _, r in rows) + '\n')
    print(t, len(rows), 'N', sum(1 for _, r in rows if r[0] == 'N'))
print('채널별:')
for ch, st in sorted(stat.items()):
    print(' ', ch, dict(st))
