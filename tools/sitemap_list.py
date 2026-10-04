"""블룸버그·로이터 뉴스 사이트맵에서 제목 목록만 받아 관심 산업 키워드로 거른다 (본문은 받지 않음).

사용:
  python3 tools/sitemap_list.py bbg <since ISO UTC> [--all]
  python3 tools/sitemap_list.py rtr <since ISO UTC> [--all]
  예) python3 tools/sitemap_list.py rtr 2026-10-01T10:00:00Z
출력: 번호  KST시각  [추정 산업]  제목  주소   (--all이면 키워드에 안 걸린 것도 출력)
seen_urls.txt(이미 처리한 주소, meta/newsSeen에서 생성)에 있는 기사는 뺀다.
"""
import sys, re, os, html, subprocess
from datetime import datetime, timedelta, timezone

KST = timezone(timedelta(hours=9))
ROOT = os.path.dirname(os.path.abspath(__file__))
SEEN = os.path.join(ROOT, '..', 'work', 'seen_urls.txt')
seen = set(open(SEEN).read().split()) if os.path.exists(SEEN) else set()

# 산업 id → 제목 키워드(소문자, 단어 앞부분 일치)
KW = {
 'uranium': 'uranium,nuclear,reactor,enrich*,centrus,cameco,kazatom,urenco,smr,westinghouse',
 'drilling': 'rig,rigs,drilling,offshore,fpso,subsea,oilfield,halliburton,slb,baker hughes,transocean,valaris,shale,octg',
 'gas': 'lng,natural gas,gas price,gas prices,qatar,liquefaction,henry hub,ttf,jkm,pipeline',
 'coal': 'coal,coking,steel,iron ore',
 'power': 'power,grid,electricity,utility,utilities,data center,data centre,solar,wind farm,wind power,battery,batteries,storage,transformer,turbine*,polysilicon,pjm,ercot',
 'petchem': 'chemical*,petrochemical*,ethylene,cracker,polymer,plastic*,refiner*,refinery,refining,naphtha,basf,dow inc,lyondell,sabic',
 'jpins': 'japan,japanese,insur*,jgb,boj,bank of japan,yen,reinsur*',
 'beauty': "cosmetic*,beauty,skincare,amorepacific,l'oreal,estee",
 'macro': 'fed,treasury,treasuries,yield,yields,inflation,cpi,rate hike,rate cut,central bank,ecb,tariff*,recession,gdp,payroll,bond,bonds,dollar,oil,opec,crude,brent,wti,hormuz,iran,sanction*,semiconductor,chip,chips,chipmaker*,nvidia,memory,hbm,tsmc',
}
KW = {k: v.split(',') for k, v in KW.items()}

def get(url):
    r = subprocess.run(['curl', '-sS', '-m', '30', '-A', 'Mozilla/5.0', '-w', '\n%{http_code}', url],
                       capture_output=True, text=True)
    body, _, code = r.stdout.rpartition('\n')
    if code != '200':
        raise SystemExit(f'HTTP {code or "000"} {url} {r.stderr.strip()[:120]}')
    return body

def items(xml):
    for u in re.findall(r'<url>(.*?)</url>', xml, re.S):
        loc = re.search(r'<loc>(.*?)</loc>', u).group(1)
        t = re.search(r'<news:title>(.*?)</news:title>', u, re.S)
        d = re.search(r'<news:publication_date>(.*?)<', u) or re.search(r'<lastmod>(.*?)<', u)
        title = html.unescape(re.sub(r'<!\[CDATA\[|\]\]>', '', t.group(1))).strip() if t else ''
        yield html.unescape(loc), datetime.fromisoformat(d.group(1).replace('Z', '+00:00')), title

def tag(title):
    """단어 단위로 일치(끝에 *가 붙은 키워드만 앞부분 일치) — 'rig'가 'Religion'에, 'power'가 'powers'에 걸리지 않게."""
    s = title.lower()
    def hit(w):
        pat = re.escape(w[:-1]) if w.endswith('*') else re.escape(w) + r'(?![a-z])'
        return re.search(r'(?<![a-z])' + pat, s)
    return [k for k, ws in KW.items() if any(hit(w) for w in ws)]

def fetch(src, since):
    out = []
    if src == 'bbg':
        out = list(items(get('https://www.bloomberg.com/sitemaps/news/latest.xml')))
    else:
        base = 'https://www.reuters.com/arc/outboundfeeds/sitemap/?outputType=xml'
        for off in range(0, 10000, 100):
            xs = list(items(get(base + (f'&from={off}' if off else ''))))
            if not xs: break
            out += xs
            if min(x[1] for x in xs) < since: break
    langs = re.compile(r'reuters\.com/(de|es|fr|it|pt|ja|ar|zh)/')
    return [x for x in out if x[1] >= since and not langs.search(x[0]) and x[0] not in seen]

if __name__ == '__main__':
    src, since = sys.argv[1], datetime.fromisoformat(sys.argv[2].replace('Z', '+00:00'))
    show_all = '--all' in sys.argv
    xs = sorted(fetch(src, since), key=lambda x: x[1], reverse=True)
    n = 0
    for loc, d, title in xs:
        h = tag(title)
        if not h and not show_all: continue
        n += 1
        print(f'{n}\t{d.astimezone(KST):%m-%d %H:%M}\t[{",".join(h) or "-"}]\t{title}\t{loc}')
    print(f'# {src}: {since:%m-%d %H:%M}Z 이후 {len(xs)}건 중 {n}건 표시')
