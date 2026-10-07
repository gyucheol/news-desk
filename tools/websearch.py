"""웹 검색 대체 도구 — WebSearch 세션 한도(200회)에 걸렸을 때 Bash로 쓰는 검색.

사용:
  python3 tools/websearch.py "검색어" [--gnews | --web] [--n 8] [--lang ko|ja|en]
  기본    : 빙 뉴스 RSS — 날짜, 제목, 기사 원래 주소, 요약 160자 (주소를 WebFetch/curl로 바로 열 수 있음)
  --gnews : 구글 뉴스 RSS — 날짜, 매체, 제목 (링크는 구글 뉴스 경유라 열기 어려움, 보도 존재·제목 확인용)
  --web   : 빙 일반 검색 — 제목, 주소, 요약 (1차 자료·기관 페이지 찾기용)
  python3 tools/websearch.py --fetch <주소> [--grep 단어1,단어2] [--n 글자수]
          : 기사 본문 텍스트만 뽑아 출력(기본 앞 3000자). --grep을 주면 그 단어 주변 문장만 출력
"""
import sys, re, html, subprocess, urllib.parse, base64, signal
signal.signal(signal.SIGPIPE, signal.SIG_DFL)  # head 등으로 잘라 볼 때 오류 없이 끝내기

UA = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124 Safari/537.36'

def get(url):
    r = subprocess.run(['curl', '-sSL', '-m', '25', '-A', UA, '-H', 'Accept-Language: en-US,en;q=0.8,ko;q=0.6', url],
                       capture_output=True, text=True)
    return r.stdout

def clean(s):
    return re.sub(r'\s+', ' ', html.unescape(re.sub(r'<[^>]+>', '', html.unescape(s or '')))).strip()

def tag(it, name):
    m = re.search(rf'<{name}[^>]*>(.*?)</{name}>', it, re.S)
    return m.group(1) if m else ''

def bing_news(q, n, lang):
    mkt = {'ko': 'ko-KR', 'ja': 'ja-JP'}.get(lang, 'en-US')
    x = get(f'https://www.bing.com/news/search?q={urllib.parse.quote(q)}&format=rss&setmkt={mkt}&count={n}')
    out = []
    for it in re.findall(r'<item>(.*?)</item>', x, re.S)[:n]:
        link = html.unescape(tag(it, 'link'))
        u = urllib.parse.parse_qs(urllib.parse.urlparse(link).query).get('url', [link])[0]
        d = tag(it, 'pubDate')
        out.append(f"{d[5:16]} | {clean(tag(it, 'title'))} | {u} | {clean(tag(it, 'description'))[:160]}")
    return out

def gnews(q, n, lang):
    hl, gl, ceid = {'ko': ('ko', 'KR', 'KR:ko'), 'ja': ('ja', 'JP', 'JP:ja')}.get(lang, ('en-US', 'US', 'US:en'))
    x = get(f'https://news.google.com/rss/search?q={urllib.parse.quote(q)}&hl={hl}&gl={gl}&ceid={ceid}')
    out = []
    for it in re.findall(r'<item>(.*?)</item>', x, re.S)[:n]:
        out.append(f"{tag(it, 'pubDate')[5:16]} | {clean(tag(it, 'source'))} | {clean(tag(it, 'title'))}")
    return out

def bing_web(q, n, lang):
    mkt = {'ko': 'ko-KR', 'ja': 'ja-JP'}.get(lang, 'en-US')
    x = get(f'https://www.bing.com/search?q={urllib.parse.quote(q)}&setmkt={mkt}&count={n}')
    out = []
    for b in re.findall(r'<li class="b_algo"(.*?)</li>', x, re.S)[:n]:
        a = re.search(r'<h2[^>]*>\s*<a[^>]+href="([^"]+)"[^>]*>(.*?)</a>', b, re.S)
        if not a: continue
        u = html.unescape(a.group(1))
        m = re.search(r'[?&]u=a1([^&]+)', u)
        if m:
            s = m.group(1); s += '=' * (-len(s) % 4)
            try: u = base64.urlsafe_b64decode(s).decode()
            except Exception: pass
        p = re.search(r'<p[^>]*>(.*?)</p>', b, re.S)
        out.append(f"{clean(a.group(2))} | {u} | {clean(p.group(1))[:160] if p else ''}")
    return out

def fetch(url, grep, n):
    x = get(url)
    x = re.sub(r'(?is)<(script|style|noscript|svg|header|footer|nav)[^>]*>.*?</\1>', ' ', x)
    x = re.sub(r'(?i)<br\s*/?>|</p>|</h\d>|</li>', ' \n ', x)
    t = html.unescape(re.sub(r'<[^>]+>', ' ', x))
    t = re.sub(r'[ \t\r\f\v]+', ' ', t)
    t = re.sub(r'\s*\n\s*', '\n', t).strip()
    if not grep:
        return [t[:n]]
    sents = [s_ for s_ in re.split(r'\n|(?<=[.!?다])\s+', t) if len(s_) > 20]
    ws = [w.lower() for w in grep.split(',') if w]
    return [s_[:400] for s_ in sents if any(w in s_.lower() for w in ws)][:30]

if __name__ == '__main__':
    args = sys.argv[1:]
    if args and args[0] == '--fetch':
        g = args[args.index('--grep') + 1] if '--grep' in args else ''
        n = int(args[args.index('--n') + 1]) if '--n' in args else 3000
        for line in fetch(args[1], g, n):
            print('-', line)
        sys.exit()
    q = args[0]
    n = int(args[args.index('--n') + 1]) if '--n' in args else 8
    lang = args[args.index('--lang') + 1] if '--lang' in args else 'en'
    f = gnews if '--gnews' in args else bing_web if '--web' in args else bing_news
    res = f(q, n, lang)
    if not res and f is bing_news:  # 빙 뉴스가 비면(한국어에서 자주) 구글 뉴스로
        res = gnews(q, n, lang)
    for i, r in enumerate(res, 1):
        print(i, r)
    if not res:
        print('(결과 없음 — 검색어를 줄이거나 --gnews / --web / --lang ko 를 시도)')
