"""연준(이사회·FOMC·12개 지역 연은) 인사의 최근 연설·발언·의회 증언 목록을 공식 사이트에서 모은다 (본문은 받지 않음).

사용:
  python3 tools/fedspeech.py <since ISO UTC> [--out <file>]
  예) python3 tools/fedspeech.py 2026-10-01T00:00:00Z --out work/fed.tsv
출력(탭 구분, 시각 오름차순): KST시각(YYYY-MM-DD HH:MM)  출처키  연사 성(영문, 모르면 '')  제목  주소
  - 날짜만 있는 출처는 그 날짜 00:00으로 적고, since 비교는 날짜 단위로 한다.
  - 같은 주소는 한 번만, seen_urls.txt(이미 처리한 주소)에 있는 주소는 뺀다.
  - 출처별 건수/오류는 stderr. 한 출처가 실패해도 나머지는 계속한다(curl 25초, 2회 재시도).
SOURCES (출처키: 가져오는 곳)
  board: 이사회 speeches.xml + testimony.xml RSS ('Bowman, 제목' → 연사/제목 분리)
  fomc: press_monetary.xml RSS (연사 '')
  ny: 연설 목록 HTML (RSS는 봇 차단 페이지)      boston: 연설 목록 HTML (rss_speeches.xml은 2024년에 멈춤)
  cleveland: 목록 HTML 안의 data-initialize JSON   chicago: 총재실 Speaking Engagements HTML
  philadelphia: speeches-anna-paulson HTML (총재 교체 시 주소 바뀜)   richmond: ?cc_view=rss
  atlanta: 목록 HTML 안의 feed_ JSON   stlouis: SXA 검색 API(/sxa/search/results, 총재 Musalem 고정)
  minneapolis: /api/sitesearch (ess_pagetype:Speech)   kansascity: 목록 HTML 카드
  dallas: /rss/speeches.xml   sf: WP REST sffed_speeches (eern-speeches는 타 연준 인사 재게시라 제외)
  stlouis·kansascity는 브라우저 UA를 쓰면 접속이 끊겨 curl 기본 UA로 받는다.
"""
import sys, re, os, html, json, subprocess
from datetime import datetime, timedelta, timezone

KST = timezone(timedelta(hours=9))
ROOT = os.path.dirname(os.path.abspath(__file__))
SEEN = os.path.join(ROOT, '..', 'work', 'seen_urls.txt')
seen = set(open(SEEN).read().split()) if os.path.exists(SEEN) else set()
UA = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0 Safari/537.36'
MON = {m: i + 1 for i, m in enumerate('jan feb mar apr may jun jul aug sep oct nov dec'.split())}

try:
    from zoneinfo import ZoneInfo
    ZONES = {k: ZoneInfo(v) for k, v in {'E': 'America/New_York', 'C': 'America/Chicago',
                                          'M': 'America/Denver', 'P': 'America/Los_Angeles'}.items()}
except Exception:  # tzdata 없으면 표준시 고정
    ZONES = {k: timezone(timedelta(hours=h)) for k, h in {'E': -5, 'C': -6, 'M': -7, 'P': -8}.items()}

def get(url, ua=UA):
    err = ''
    for i in range(3):
        cmd = ['curl', '-sS', '-L', '--compressed', '-m', '25', '-w', '\n%{http_code}', url]
        if ua: cmd[1:1] = ['-A', ua]
        if i: cmd.insert(1, '--http1.1')  # 재시도는 HTTP/1.1 (HTTP/2 스트림 오류 대비)
        r = subprocess.run(cmd, capture_output=True, text=True, errors='replace')
        body, _, code = r.stdout.rpartition('\n')
        if code == '200': return body
        err = f'HTTP {code or "000"} {r.stderr.strip()[:100]}'
    raise RuntimeError(f'{err} {url}')

def clean(s):
    s = re.sub(r'<!\[CDATA\[|\]\]>', '', s or '')
    s = re.sub(r'</?(a|span|strong|em|b|i|cite|sup|sub)\b[^>]*>', '', s)  # 인라인 태그는 공백 없이
    s = html.unescape(re.sub(r'<[^>]+>', ' ', s))
    return re.sub(r'\s+', ' ', html.unescape(s)).strip()

def surname(name):
    """'Susan M. Collins, President' → 'Collins'"""
    ws = [w for w in re.split(r'\s+', clean(name).split(',')[0]) if w.rstrip('.').lower() not in ('jr', 'sr', 'ii', 'iii', 'iv')]
    return ws[-1].strip('.') if ws else ''

def day(y, m, d):  # 날짜만 있는 항목
    return datetime(int(y), int(m), int(d), tzinfo=KST), True

def mdy(s):
    """'Oct 7, 2026' / 'Sept. 29, 2026' / 'October 13, 2026'"""
    m = re.search(r'([A-Za-z]{3})[a-z]*\.? (\d{1,2})(?:\s*[-–]\s*\d{1,2})?,? (\d{4})', s)
    if not m or m.group(1).lower() not in MON: return None, True  # 못 읽는 날짜는 건너뜀
    return day(m.group(3), MON[m.group(1).lower()], m.group(2))

def local(s, z='E'):
    """'2026-02-20T09:30:00' (현지 시각) → aware; 00:00:00이면 날짜만으로 본다"""
    d = datetime.fromisoformat(s[:19])
    if d.hour == d.minute == 0: return day(d.year, d.month, d.day)
    return d.replace(tzinfo=ZONES[z]), False

def rfc822(s):
    m = re.search(r'(\d{1,2}) (\w{3}) (\d{4}) (\d\d):(\d\d)(?::(\d\d))?\s*(\S*)', clean(s))
    d = datetime(int(m.group(3)), MON[m.group(2).lower()], int(m.group(1)), int(m.group(4)), int(m.group(5)), int(m.group(6) or 0))
    tz = m.group(7).upper()
    if re.fullmatch(r'[+-]\d{4}', tz):
        off = timedelta(hours=int(tz[1:3]), minutes=int(tz[3:]))
        return d.replace(tzinfo=timezone(off if tz[0] == '+' else -off)), False
    if tz[:1] in ZONES and tz[1:] in ('ST', 'DT', 'T'):  # EST/CDT 등은 현지 벽시계로 해석(서머타임 표기 오류 대비)
        return d.replace(tzinfo=ZONES[tz[0]]), False
    return d.replace(tzinfo=timezone.utc), False

def rss(xml):
    for it in re.findall(r'<item\b.*?>(.*?)</item>', xml, re.S):
        f = lambda t: (re.search(rf'<{t}\b[^>]*>(.*?)</{t}>', it, re.S) or [None, ''])[1]
        yield clean(f('title')), clean(f('link')), f('pubDate'), clean(f('description'))

# ---- 출처별: (dt, dateonly, 연사, 제목, 주소) 목록을 돌려준다 ----

def board():
    out = []
    for u in ('https://www.federalreserve.gov/feeds/speeches.xml', 'https://www.federalreserve.gov/feeds/testimony.xml'):
        for t, link, pd, _ in rss(get(u)):
            m = re.match(r'([^,]{2,40}), (.+)', t)
            out.append((*rfc822(pd), surname(m.group(1)) if m else '', m.group(2) if m else t, link))
    return out

def fomc():
    return [(*rfc822(pd), '', t, link) for t, link, pd, _ in rss(get('https://www.federalreserve.gov/feeds/press_monetary.xml'))]

def ny():
    s, out = get('https://www.newyorkfed.org/newsevents/speeches'), []
    for d, href, t in re.findall(r'<div>\s*([A-Z][a-z]{2} \d{1,2}, \d{4})\s*</div>.*?<a href="([^"]+)"[^>]*>(.*?)</a>', s, re.S):
        t = clean(t)
        m = re.match(r'([A-Z][\w\'’.-]+(?: [A-Z][\w\'’.-]+){0,2}):\s+(.+)', t)
        out.append((*mdy(d), surname(m.group(1)) if m else '', m.group(2) if m else t, 'https://www.newyorkfed.org' + href if href.startswith('/') else href))
    return out

def boston():
    s, out = get('https://www.bostonfed.org/news-and-events/speeches.aspx'), []
    for b in s.split('<h1 class="card-title">')[1:]:
        a = re.search(r'<a href="([^"]+)"[^>]*>(.*?)</a>', b, re.S)
        d = re.search(r'class="date-and-location">(.*?)</p>', b, re.S)
        sp = re.search(r'class="list-inline speaker">.*?<a[^>]*>(.*?)</a>', b, re.S)
        if not (a and d): continue
        out.append((*mdy(clean(d.group(1))), surname(sp.group(1)) if sp else '', clean(a.group(2)), 'https://www.bostonfed.org' + a.group(1)))
    return out

def cleveland():
    s = get('https://www.clevelandfed.org/collections/speeches')
    d = json.loads(html.unescape(re.search(r"<search-results[^>]*data-initialize='([^']*)'", s).group(1)))
    out = []
    for r in d['results']:
        when = (datetime.fromisoformat(r['speechTime']), False) if r.get('speechTime') else day(*r['releaseDate'][:10].split('-'))
        u = r['url']
        if re.match(r'/collections/speeches/sp-', u):  # 목록 화면과 같은 연도 경로로
            u = u.replace('/speeches/', f'/speeches/{r["sortDate"][:4]}/', 1)
        out.append((*when, surname(r['authors'][0]['label']) if r.get('authors') else '', clean(r['title']), 'https://www.clevelandfed.org' + u))
    return out

def chicago():
    s = get('https://www.chicagofed.org/utilities/about-us/office-of-the-president/office-of-the-president-speaking')
    p = re.search(r'office-of-the-president-home">\s*(?:President )?([A-Z][\w.]+(?: [A-Z][\w.]*)+)\s*</a>', s)
    who, out = surname(p.group(1)) if p else 'Goolsbee', []
    for href, t, d in re.findall(r'<div class="cyan-publication"><a href="([^"]+)">(.*?)</a>\s*<p class="cyan-publication-date">([^<]+)</p>', s, re.S):
        out.append((*mdy(d), who, clean(t), 'https://www.chicagofed.org' + href if href.startswith('/') else href))
    return out

def philadelphia():
    s, out = get('https://www.philadelphiafed.org/the-economy/speeches-anna-paulson'), []
    p = re.search(r'<title>[^<]*President ([^<|]+)', s)
    who = surname(p.group(1)) if p else 'Paulson'
    body = s[s.find('article-body'):]
    for y, ul in re.findall(r'<h2>\s*(\d{4})\s*</h2>\s*<ul>(.*?)</ul>', body, re.S):
        for href, t, rest in re.findall(r'<li>\s*<a href="([^"]+)">(.*?)</a>(.*?)</li>', ul, re.S):
            m = re.search(r'\|\s*([A-Za-z]{3})[a-z]*\.? (\d{1,2})', clean(rest))
            if not m: continue
            out.append((*day(y, MON[m.group(1).lower()], m.group(2)), who, clean(t), 'https://www.philadelphiafed.org' + href if href.startswith('/') else href))
    return out

def richmond():
    out = []
    for t, link, pd, _ in rss(get('https://www.richmondfed.org/press_room/speeches?cc_view=rss')):
        m = re.search(r'/speeches/([a-z_]+)/\d{4}/', link)
        out.append((*rfc822(pd), m.group(1).split('_')[-1].capitalize() if m else '', t, link))
    return out

def atlanta():
    s = get('https://www.atlantafed.org/news/speeches')
    i = re.search(r'var feed_[0-9a-f]+ = ', s).end()
    out = []
    for x in json.JSONDecoder().raw_decode(s[i:])[0]:
        t = clean(x['Title'])
        if x.get('Authors'): who = surname(x['Authors'][0]['FullName'])
        else: m = re.search(r'President (\w+)', t); who = m.group(1) if m else ''
        out.append((*local(x['Date']), who, t, x.get('UrlNoLang') or x['Url']))
    return out

def stlouis():
    q = ('https://www.stlouisfed.org/sxa/search/results/?s=%7BDA5A2E95-2DA8-48EF-8A05-C6C4DEE314B1%7D'
         '&itemid=%7B171B272E-9D98-430F-9F07-825319267544%7D&sig=srremarks&autoFireSearch=true'
         '&v=%7B073ED7F6-4F06-4C6D-9FF4-09BD85939FDC%7D&p=30&o=Manually%20Updated%2CDescending')
    out = []
    for r in json.loads(get(q, ua=None))['Results']:
        t = clean(r['Html'])
        m = re.search(r'\(([A-Za-z]{3})[a-z]*\.? (\d{1,2}), (\d{4})\)\.?$', t)
        if not m: continue
        t = re.sub(r'\s*\([^()]*\)\.?$', '', t).replace(' ,', ',')
        out.append((*day(m.group(3), MON[m.group(1).lower()], m.group(2)), 'Musalem', t, 'https://www.stlouisfed.org' + r['Url']))
    return out

def minneapolis():
    q = ('https://www.minneapolisfed.org/api/sitesearch?searchTerm=&appliedFacets=ess_pagetype%3ASpeech'
         '&sortBy=date&startingResult=0&resultsPerPage=30')
    out = []
    for r in json.loads(get(q))['results']:
        f = {x['name']: x['values'] for x in r['fields']}
        ts = (f.get('ess_publishdatetime') or [''])[0]
        if not ts[:4].isdigit(): continue
        if ts[11:19] == '00:00:00': when = day(*ts[:10].split('-'))
        else: when = (datetime.fromisoformat(ts.replace('Z', '+00:00')), False)
        t = re.sub(r'\s*\|\s*Federal Reserve Bank of Minneapolis\s*$', '', clean(r['title']))
        out.append((*when, 'Kashkari' if 'Kashkari' in t else '', t, r['reference']))
    return out

def kansascity():
    s, out = get('https://www.kansascityfed.org/speeches/', ua=None), []
    for b in s.split('class="card-outer"')[1:]:
        d = re.search(r'<time datetime="(\d{4})-(\d\d)-(\d\d)', b)
        a = re.search(r'<h3>\s*<a href="([^"]+)"[^>]*>(.*?)</a>', b, re.S)
        sp = re.search(r'<footer>.*?<a[^>]*>(.*?)</a>', b, re.S)
        if not (d and a): continue
        href = html.unescape(a.group(1))
        out.append((*day(*d.groups()), surname(sp.group(1)) if sp else '', clean(a.group(2)), 'https://www.kansascityfed.org' + href if href.startswith('/') else href))
    return out

def dallas():
    out = []
    for t, link, pd, desc in rss(get('https://www.dallasfed.org/rss/speeches.xml')):
        m = re.search(r'/speeches/([a-z]+)/\d{4}/', link)
        if m and m.group(1) != 'speeches': who = m.group(1).capitalize()
        else:
            m = re.search(r'(?:President|Officer|Director|Economist|Adviser|Advisor)\s+((?:[A-Z][\w.\'’-]*\s+){1,3}[A-Z][\w\'’-]+)', desc)
            who = surname(m.group(1)) if m else ''
        out.append((*rfc822(pd), who, t, link))
    return out

def sf():
    q = 'https://www.frbsf.org/wp-json/wp/v2/sffed_speeches?per_page=40&_fields=date,date_gmt,link,title,parsely'
    out = []
    for x in json.loads(get(q)):
        if '/eern-speeches/' in x['link']: continue
        when = day(*x['date'][:10].split('-')) if x['date'].endswith('T00:00:00') else \
            (datetime.fromisoformat(x['date_gmt']).replace(tzinfo=timezone.utc), False)
        cr = ((x.get('parsely') or {}).get('meta') or {}).get('creator') or ['']
        out.append((*when, surname(cr[0]), clean(x['title']['rendered']), x['link']))
    return out

SOURCES = [board, fomc, ny, boston, cleveland, chicago, philadelphia, richmond, atlanta,
           stlouis, minneapolis, kansascity, dallas, sf]

if __name__ == '__main__':
    since = datetime.fromisoformat(sys.argv[1].replace('Z', '+00:00'))
    out_path = sys.argv[sys.argv.index('--out') + 1] if '--out' in sys.argv else None
    rows, urls = [], set()
    for fn in SOURCES:
        try:
            n = 0
            for dt, dateonly, who, title, url in fn():
                if dt is None: continue
                ok = dt.date() >= since.astimezone(timezone.utc).date() if dateonly else dt >= since
                if not ok or url in urls or url in seen: continue
                urls.add(url); n += 1
                rows.append((dt, fn.__name__, who.replace('\t', ' '), title.replace('\t', ' '), url))
            print(f'{fn.__name__}\t{n}', file=sys.stderr)
        except Exception as e:
            print(f'{fn.__name__}\tERROR {type(e).__name__}: {str(e)[:160]}', file=sys.stderr)
    rows.sort(key=lambda r: (r[0].astimezone(timezone.utc), r[1]))
    lines = [f'{dt.astimezone(KST):%Y-%m-%d %H:%M}\t{src}\t{who}\t{t}\t{u}' for dt, src, who, t, u in rows]
    text = '\n'.join(lines) + ('\n' if lines else '')
    if out_path: open(out_path, 'w').write(text)
    else: sys.stdout.write(text)
