#!/usr/bin/env python3
"""공시 감시: 한국(DART)·미국(SEC EDGAR) 관심 종목의 새 공시를 텔레그램으로 보낸다.

GitHub Actions(.github/workflows/disclosure-watch.yml)가 5분마다 실행한다.
본 공시 번호는 상태 파일(기본 .disclosure-state/seen.json)에 남겨 같은 공시를 두 번 보내지 않는다.
처음 보는 종목은 그때 있던 공시를 '본 것'으로만 기록하고 보내지 않는다(옛 공시가 한꺼번에 오는 것을 막음).

환경 변수
  TELEGRAM_BOT_TOKEN, TELEGRAM_CHAT_ID  필수(보내기)
  DART_API_KEY       선택. 있으면 DART 오픈API로 목록을 받고, 없으면 DART 사이트 검색 결과를 읽는다.
  SEC_USER_AGENT     선택. SEC는 연락처(이메일)가 든 User-Agent를 요구한다.
  ANTHROPIC_API_KEY  선택. 있으면 Claude가 한국어로 요약하고, 없으면 원문 앞부분을 보낸다.
  CLAUDE_MODEL       선택. 요약 모델(기본 claude-opus-5-5).

사용법
  python3 tools/disclosure/watch.py                 # 한 번 확인하고 새 공시를 보냄
  python3 tools/disclosure/watch.py --dry-run       # 보내지 않고 화면에만 출력, 상태 저장 안 함
  python3 tools/disclosure/watch.py --preview 1     # 종목마다 최근 공시 1건으로 메시지 미리보기(보내지 않음)
  python3 tools/disclosure/watch.py --preview 1 --send   # 위 미리보기를 실제로 텔레그램에 보냄(시험용)
  python3 tools/disclosure/watch.py --test-message  # 텔레그램 연결 시험 메시지
  python3 tools/disclosure/watch.py --find-chat-id  # 봇에게 말을 건 대화방의 chat_id 출력
"""
import argparse
import datetime as dt
import html
import json
import os
import re
import sys
import time
import urllib.error
import urllib.parse
import urllib.request

HERE = os.path.dirname(os.path.abspath(__file__))
WATCHLIST = os.path.join(HERE, "watchlist.json")
DEFAULT_STATE = ".disclosure-state/seen.json"
KST = dt.timezone(dt.timedelta(hours=9))

# SEC는 연락처가 든 User-Agent를 요구한다. 실제 이메일을 SEC_USER_AGENT로 넣는 것을 권장(아래는 임시 값)
SEC_UA = os.environ.get("SEC_USER_AGENT") or "news-desk disclosure-watch admin@example.com"
BROWSER_UA = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120 Safari/537.36"

MAX_SEND_PER_RUN = 10      # 한 번 실행에 보내는 최대 건수(나머지는 다음 실행)
KEEP_SEEN = 400            # 종목별로 기억하는 공시 번호 수
DOC_CHARS = 40000          # 요약에 넘기는 원문 최대 글자 수
LOOKBACK_DAYS = int(os.environ.get("LOOKBACK_DAYS") or 7)  # 목록 조회 기간(일)

CLAUDE_MODEL = os.environ.get("CLAUDE_MODEL") or "claude-opus-5-5"
# 서버 측 대체 모델(fallbacks)을 받는 모델. Haiku는 받지 않는다.
FALLBACK_MODELS = {"claude-opus-5-5", "claude-opus-5", "claude-fable-5-1", "claude-sonnet-5-5"}

SEC_8K_ITEMS = {
    "1.01": "중요 계약 체결", "1.02": "중요 계약 해지", "1.03": "파산·회생",
    "1.05": "사이버보안 사고", "2.01": "자산 인수·처분 완료", "2.02": "실적 발표",
    "2.03": "직접 금융채무 발생", "2.04": "채무 조기상환 사유 발생", "2.05": "구조조정 비용",
    "2.06": "자산 손상", "3.01": "상장 유지 기준 미달·상장 이전", "3.02": "미등록 증권 발행",
    "3.03": "주주 권리 변경", "4.01": "감사인 교체", "4.02": "과거 재무제표 신뢰 불가",
    "5.01": "지배권 변경", "5.02": "임원·이사 변동, 보수", "5.03": "정관·회계연도 변경",
    "5.05": "윤리강령 변경", "5.07": "주주총회 표결 결과", "5.08": "주주 추천 이사 후보",
    "7.01": "Reg FD 공개(IR 자료 등)", "8.01": "기타 중요 사항", "9.01": "재무제표·첨부 서류",
}
SEC_FORMS = {
    "8-K": "수시 공시", "8-K/A": "수시 공시 정정", "6-K": "외국 기업 수시 공시",
    "10-Q": "분기 보고서", "10-K": "연간 보고서", "20-F": "외국 기업 연간 보고서",
    "40-F": "캐나다 기업 연간 보고서", "4": "내부자 거래 보고", "4/A": "내부자 거래 보고 정정",
    "3": "내부자 최초 보유 보고", "144": "내부자 주식 매도 예정 신고",
    "SCHEDULE 13G": "5% 이상 지분 보유(단순 투자)", "SCHEDULE 13G/A": "5% 이상 지분 보유 변동(단순 투자)",
    "SCHEDULE 13D": "5% 이상 지분 보유(경영 참여 가능)", "SCHEDULE 13D/A": "5% 이상 지분 보유 변동(경영 참여 가능)",
    "424B5": "증권 발행 설명서", "424B2": "증권 발행 설명서", "FWP": "발행 관련 자유서식 설명서",
    "S-3": "증권 발행 등록", "S-3ASR": "증권 발행 일괄 등록", "S-8": "임직원 주식 보상 등록",
    "DEF 14A": "주주총회 위임장 설명서", "SD": "분쟁 광물 보고",
}


def log(*a):
    print(*a, file=sys.stderr, flush=True)


# ---------------------------------------------------------------- HTTP

def http(url, data=None, headers=None, timeout=30, tries=3):
    """(본문 bytes, 응답 헤더)를 돌려준다. 실패하면 마지막 예외를 그대로 올린다."""
    body = urllib.parse.urlencode(data).encode() if isinstance(data, dict) else data
    last = None
    for i in range(tries):
        req = urllib.request.Request(url, data=body, headers=headers or {})
        try:
            with urllib.request.urlopen(req, timeout=timeout) as r:
                return r.read(), r.headers
        except urllib.error.HTTPError as e:
            last = e
            if e.code not in (429, 500, 502, 503, 504):
                raise
        except (urllib.error.URLError, TimeoutError, ConnectionError) as e:
            last = e
        time.sleep(2 * (i + 1))
    raise last


def decode(raw, headers):
    m = re.search(r"charset=([\w-]+)", headers.get("Content-Type", "") or "", re.I)
    for enc in ([m.group(1)] if m else []) + ["utf-8"]:
        try:
            return raw.decode(enc)
        except (UnicodeDecodeError, LookupError):
            pass
    return raw.decode("cp949", errors="replace")


def html_to_text(s):
    s = re.sub(r"(?is)<(script|style|head|ix:header)\b.*?</\1>", " ", s)
    s = re.sub(r"(?i)<br\s*/?>|</(p|div|tr|li|h\d|table)>", "\n", s)
    s = re.sub(r"(?s)<[^>]+>", " ", s)
    s = html.unescape(s).replace("\xa0", " ")
    s = re.sub(r"[ \t\r\f\v]+", " ", s)
    s = re.sub(r"\n\s*\n+", "\n", s)
    return s.strip()


# ---------------------------------------------------------------- DART (한국)

def dart_list(corp):
    today = dt.datetime.now(KST).date()
    start = today - dt.timedelta(days=LOOKBACK_DAYS)
    key = os.environ.get("DART_API_KEY")
    if key:
        q = urllib.parse.urlencode({
            "crtfc_key": key, "corp_code": corp["corp_code"], "page_count": 100,
            "bgn_de": start.strftime("%Y%m%d"), "end_de": today.strftime("%Y%m%d"),
        })
        raw, _ = http("https://opendart.fss.or.kr/api/list.json?" + q)
        j = json.loads(raw)
        if j.get("status") == "013":  # 조회된 데이터 없음
            return []
        if j.get("status") != "000":
            raise RuntimeError(f"DART API {j.get('status')} {j.get('message')}")
        return [{"id": x["rcept_no"], "title": re.sub(r"\s+", " ", x["report_nm"]).strip(),
                 "filer": x.get("flr_nm", ""), "date": x["rcept_dt"]} for x in j.get("list", [])]

    raw, hd = http("https://dart.fss.or.kr/dsab007/detailSearch.ax", data={
        "currentPage": 1, "maxResults": 100, "maxLinks": 10, "sort": "date", "series": "desc",
        "textCrpCik": corp["corp_code"],
        "startDate": start.strftime("%Y%m%d"), "endDate": today.strftime("%Y%m%d"),
    }, headers={"User-Agent": BROWSER_UA})
    page = decode(raw, hd)
    out = []
    for row in re.findall(r"(?s)<tr>(.*?)</tr>", page):
        m = re.search(r'(?s)rcpNo=(\d{14})"[^>]*>(.*?)</a>', row)
        if not m:
            continue
        tds = re.findall(r"(?s)<td[^>]*>(.*?)</td>", row)
        date = next((re.sub(r"\D", "", html_to_text(t)) for t in tds
                     if re.fullmatch(r"\s*\d{4}\.\d{2}\.\d{2}\s*", html_to_text(t))), "")
        filer = re.search(r'(?s)<td class="tL ellipsis" title="([^"]*)"', row)
        out.append({"id": m.group(1), "title": re.sub(r"\s+", " ", html_to_text(m.group(2))).strip(),
                    "filer": html.unescape(filer.group(1)) if filer else "", "date": date})
    if not out and "rcpNo=" not in page and "검색결과가 없습니다" not in page and "조회 결과가 없습니다" not in page:
        log(f"  [경고] DART 검색 결과를 해석하지 못함({corp['name']}). 사이트 구조가 바뀌었을 수 있음")
    return out


def dart_url(item):
    return f"https://dart.fss.or.kr/dsaf001/main.do?rcpNo={item['id']}"


def dart_text(item):
    raw, hd = http(dart_url(item), headers={"User-Agent": BROWSER_UA})
    page = decode(raw, hd)
    m = re.search(r'viewDoc\("(\d+)",\s*"(\d+)",\s*"([^"]*)",\s*"([^"]*)",\s*"([^"]*)",\s*"([^"]*)"', page)
    if not m:
        return ""
    q = urllib.parse.urlencode({"rcpNo": m.group(1), "dcmNo": m.group(2), "eleId": m.group(3),
                                "offset": m.group(4), "length": m.group(5), "dtd": m.group(6)})
    raw, hd = http("https://dart.fss.or.kr/report/viewer.do?" + q, headers={"User-Agent": BROWSER_UA})
    return html_to_text(decode(raw, hd))


# ---------------------------------------------------------------- SEC (미국)

def sec_list(corp):
    raw, _ = http(f"https://data.sec.gov/submissions/CIK{corp['cik']}.json", headers={"User-Agent": SEC_UA})
    r = json.loads(raw)["filings"]["recent"]
    since = (dt.date.today() - dt.timedelta(days=LOOKBACK_DAYS)).isoformat()
    out = []
    for i, acc in enumerate(r["accessionNumber"]):
        if r["filingDate"][i] < since:
            continue
        out.append({"id": acc, "form": r["form"][i], "items": r.get("items", [""] * (i + 1))[i] or "",
                    "doc": r["primaryDocument"][i], "desc": r.get("primaryDocDescription", [""] * (i + 1))[i] or "",
                    "date": r["filingDate"][i], "accepted": r.get("acceptanceDateTime", [""] * (i + 1))[i] or ""})
    return out


def sec_base(corp, item):
    return f"https://www.sec.gov/Archives/edgar/data/{int(corp['cik'])}/{item['id'].replace('-', '')}"


def sec_url(corp, item):
    return f"{sec_base(corp, item)}/{item['doc']}" if item["doc"] else sec_base(corp, item) + "/"


def sec_text(corp, item):
    """(본문, 첨부 보도자료 목록)을 돌려준다."""
    main, exhibits = "", []
    urls = [sec_url(corp, item)] if item["doc"] else []
    try:  # 8-K·6-K는 보도자료가 첨부(EX-99)에 있는 경우가 많다
        raw, _ = http(sec_base(corp, item) + "/index.json", headers={"User-Agent": SEC_UA})
        names = [f["name"] for f in json.loads(raw)["directory"]["item"]]
        ex = [n for n in names if re.search(r"ex-?99", n, re.I) and n.lower().endswith((".htm", ".html", ".txt"))]
        urls += [f"{sec_base(corp, item)}/{n}" for n in ex[:2]]
    except Exception as e:  # noqa: BLE001 - 첨부 목록은 없어도 본문만으로 진행
        log(f"  [참고] SEC 첨부 목록을 읽지 못함: {e}")
    for i, u in enumerate(urls):
        try:
            raw, hd = http(u, headers={"User-Agent": SEC_UA})
            t = html_to_text(decode(raw, hd))
            if i == 0 and item["doc"]:
                main = t
            elif t:
                exhibits.append(t)
        except Exception as e:  # noqa: BLE001
            log(f"  [참고] SEC 문서를 읽지 못함 {u}: {e}")
        time.sleep(0.2)  # SEC 요청 한도(초당 10회) 아래로
    return main, exhibits


def sec_excerpt_source(main, exhibits):
    """요약 키가 없을 때 보여 줄 부분: 보도자료 첨부가 있으면 그것, 없으면 표지 뒤 첫 'Item' 부터."""
    if exhibits:
        t = exhibits[0]
        m = re.search(r"(?i)(for immediate release|news release|press release)", t)
        return t[m.end():] if m else t
    m = re.search(r"Item\s+\d+\.\d{2}", main)
    return main[m.start():] if m else main


def sec_title(item):
    form = item["form"]
    t = form + (f" ({SEC_FORMS[form]})" if form in SEC_FORMS else "")
    if item["items"]:
        names = [f"{x} {SEC_8K_ITEMS.get(x, '')}".strip() for x in item["items"].split(",") if x]
        t += " — " + ", ".join(names)
    return t


# ---------------------------------------------------------------- 요약

def summarize(company, title, text):
    """Claude로 한국어 요약. 키가 없거나 실패하면 None."""
    if not os.environ.get("ANTHROPIC_API_KEY") or not text:
        return None
    try:
        import anthropic
    except ImportError:
        log("  [참고] anthropic 패키지가 없어 요약을 건너뜀(pip install anthropic)")
        return None
    cut = len(text) > DOC_CHARS
    doc = text[:DOC_CHARS]
    prompt = (
        "아래 기업 공시 원문을 한국어로 요약해 주세요.\n"
        "- 3~5개 항목, 항목마다 한 줄, 각 줄은 '• '로 시작합니다.\n"
        "- 금액·수량·비율·날짜·계약 상대방·인물 이름은 원문 그대로 적습니다.\n"
        "- 원문에 없는 내용, 전망, 투자 의견은 쓰지 않습니다.\n"
        "- 정정 공시면 무엇이 바뀌었는지를 먼저 적습니다.\n"
        "- 굵게, 제목, 머리말 없이 항목만 출력합니다.\n\n"
        f"회사: {company}\n공시: {title}\n"
        + ("(원문이 길어 앞부분만 제공합니다. 제공된 부분만 근거로 쓰세요.)\n" if cut else "")
        + f"\n<document>\n{doc}\n</document>"
    )
    kwargs = dict(model=CLAUDE_MODEL, max_tokens=8000, output_config={"effort": "low"},
                  messages=[{"role": "user", "content": prompt}])
    try:
        client = anthropic.Anthropic()
        if CLAUDE_MODEL in FALLBACK_MODELS:
            resp = client.beta.messages.create(**kwargs, betas=["server-side-fallback-2026-07-01"],
                                               fallbacks="default")
        else:
            resp = client.messages.create(**kwargs)
    except anthropic.RateLimitError as e:
        log(f"  [참고] Claude 요청 한도 초과, 요약 없이 보냄: {e}")
        return None
    except anthropic.APIStatusError as e:
        log(f"  [참고] Claude 오류 {e.status_code}, 요약 없이 보냄: {e.message}")
        return None
    except anthropic.APIConnectionError as e:
        log(f"  [참고] Claude 연결 실패, 요약 없이 보냄: {e}")
        return None
    if resp.stop_reason == "refusal":
        log("  [참고] Claude가 요약을 거절함, 원문 앞부분으로 대신함")
        return None
    out = "".join(b.text for b in resp.content if b.type == "text").strip()
    return out or None


def excerpt(text, n=450):
    t = re.sub(r"\s+", " ", text or "").strip()
    return (t[:n] + "…") if len(t) > n else t


# ---------------------------------------------------------------- 텔레그램

def tg(method, payload=None):
    token = os.environ.get("TELEGRAM_BOT_TOKEN")
    if not token:
        raise RuntimeError("TELEGRAM_BOT_TOKEN이 없습니다")
    raw, _ = http(f"https://api.telegram.org/bot{token}/{method}",
                  data=json.dumps(payload or {}).encode(), headers={"Content-Type": "application/json"})
    j = json.loads(raw)
    if not j.get("ok"):
        raise RuntimeError(f"텔레그램 {method} 실패: {j}")
    return j["result"]


def tg_send(text):
    chat = os.environ.get("TELEGRAM_CHAT_ID")
    if not chat:
        raise RuntimeError("TELEGRAM_CHAT_ID가 없습니다")
    if len(text) > 4000:
        text = text[:3990] + "…"
    tg("sendMessage", {"chat_id": chat, "text": text, "parse_mode": "HTML",
                       "disable_web_page_preview": True})


def build_message(flag, company, title, meta_line, summary, text, url):
    def e(s, quote=False):
        return html.escape(s, quote=quote)
    lines = [f"{flag} <b>[{e(company)}]</b> {e(title)}", e(meta_line), ""]
    if summary:
        lines += [e(summary), ""]
    elif text:
        lines += ["원문 앞부분:", e(excerpt(text)), ""]
    lines.append(f'<a href="{e(url, quote=True)}">공시 원문 보기</a>')
    return "\n".join(lines)


def kr_message(corp, item):
    try:
        text = dart_text(item)
    except Exception as e:  # noqa: BLE001
        log(f"  [참고] DART 본문을 읽지 못함: {e}")
        text = ""
    d = item["date"]
    date = f"{d[:4]}-{d[4:6]}-{d[6:]}" if len(d) == 8 else d
    summary = summarize(corp["name"], item["title"], text)
    return build_message("🇰🇷", corp["name"], item["title"], f"제출인: {item['filer']} · 접수일: {date}",
                         summary, text, dart_url(item))


def us_message(corp, item):
    try:
        main, exhibits = sec_text(corp, item)
    except Exception as e:  # noqa: BLE001
        log(f"  [참고] SEC 본문을 읽지 못함: {e}")
        main, exhibits = "", []
    title = sec_title(item)
    full = "\n\n".join([main] + [f"[첨부 {i + 1}]\n{x}" for i, x in enumerate(exhibits)]).strip()
    summary = summarize(f"{corp['name']} ({corp['ticker']})", title, full)
    text = sec_excerpt_source(main, exhibits)
    meta = f"제출일(미국 기준): {item['date']}" + (f" · {item['desc']}" if item["desc"] and item["desc"].upper() not in (item["form"], f"FORM {item['form']}", "PRIMARY DOCUMENT") else "")
    return build_message("🇺🇸", f"{corp['name']} {corp['ticker']}", title, meta, summary, text, sec_url(corp, item))


# ---------------------------------------------------------------- 상태

def load_state(path):
    try:
        with open(path, encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return {}


def save_state(path, state):
    os.makedirs(os.path.dirname(path) or ".", exist_ok=True)
    tmp = path + ".tmp"
    with open(tmp, "w", encoding="utf-8") as f:
        json.dump(state, f, ensure_ascii=False, indent=1)
    os.replace(tmp, path)


def sources(watch):
    for c in watch.get("kr", []):
        yield f"kr:{c['corp_code']}", c, dart_list, kr_message
    for c in watch.get("us", []):
        yield f"us:{c['cik']}", c, sec_list, us_message


# ---------------------------------------------------------------- 실행

def run(args):
    with open(WATCHLIST, encoding="utf-8") as f:
        watch = json.load(f)
    state = load_state(args.state)
    changed = False
    pending = []   # (key, corp, item, maker)
    failures = 0
    n_sources = 0
    tg_failed = False

    for key, corp, lister, maker in sources(watch):
        n_sources += 1
        try:
            items = lister(corp)
        except Exception as e:  # noqa: BLE001 - 한 종목 실패가 나머지를 막지 않게
            failures += 1
            log(f"[오류] {corp['name']} 목록 조회 실패: {e}")
            continue
        log(f"{corp['name']}: 최근 {LOOKBACK_DAYS}일 공시 {len(items)}건")
        if args.preview:
            pending += [(key, corp, it, maker) for it in items[: args.preview]]
            continue
        seen = state.get(key)
        if seen is None:  # 처음 보는 종목: 기록만 하고 보내지 않음
            state[key] = [it["id"] for it in items]
            changed = True
            log(f"  처음 등록 → 기존 {len(items)}건은 보내지 않고 기록만 함")
            continue
        new = [it for it in items if it["id"] not in set(seen)]
        pending += [(key, corp, it, maker) for it in reversed(new)]  # 오래된 것부터

    if len(pending) > MAX_SEND_PER_RUN and not args.preview:
        log(f"새 공시 {len(pending)}건 중 {MAX_SEND_PER_RUN}건만 이번에 보내고 나머지는 다음 실행에 보냄")
        pending = pending[:MAX_SEND_PER_RUN]

    sent = 0
    for key, corp, item, maker in pending:
        msg = maker(corp, item)
        if args.dry_run or (args.preview and not args.send):
            print("-" * 60)
            print(msg)
            continue
        try:
            tg_send(msg)
        except Exception as e:  # noqa: BLE001 - 못 보낸 건은 기록하지 않아 다음 실행에 다시 시도
            log(f"[오류] 텔레그램 전송 실패({corp['name']} {item['id']}): {e}")
            tg_failed = True
            break
        sent += 1
        if not args.preview:
            state.setdefault(key, []).insert(0, item["id"])
            state[key] = state[key][:KEEP_SEEN]
            changed = True
        time.sleep(1)

    log(f"보냄 {sent}건, 대기 {len(pending) - sent}건, 목록 조회 실패 {failures}곳")
    if changed and not args.dry_run and not args.preview:
        save_state(args.state, state)
    out = os.environ.get("GITHUB_OUTPUT")
    if out:
        with open(out, "a") as f:
            f.write(f"changed={'true' if changed and not args.dry_run and not args.preview else 'false'}\n")
    # 텔레그램 전송 실패나 전 종목 조회 실패면 Actions에 실패로 표시해 알아챌 수 있게 한다
    return 1 if tg_failed or (n_sources and failures == n_sources) else 0


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--state", default=DEFAULT_STATE)
    ap.add_argument("--dry-run", action="store_true", help="보내지 않고 출력만, 상태 저장 안 함")
    ap.add_argument("--preview", type=int, default=0, help="종목마다 최근 N건으로 메시지 미리보기")
    ap.add_argument("--send", action="store_true", help="--preview 결과를 실제로 보냄")
    ap.add_argument("--test-message", action="store_true")
    ap.add_argument("--find-chat-id", action="store_true")
    args = ap.parse_args()

    if args.find_chat_id:
        ups = tg("getUpdates")
        if not ups:
            print("받은 메시지가 없습니다. 텔레그램에서 봇에게 /start 를 보낸 뒤 다시 실행하세요.")
        chats = {}
        for u in ups:
            m = u.get("message") or u.get("channel_post") or u.get("my_chat_member") or {}
            c = m.get("chat")
            if c:
                chats[c["id"]] = c.get("title") or c.get("username") or c.get("first_name")
        for cid, name in chats.items():
            print(f"chat_id={cid}  ({name})")
        return 0
    if args.test_message:
        tg_send("✅ 공시 알림 봇 연결 시험 메시지입니다.")
        print("보냄")
        return 0
    return run(args)


if __name__ == "__main__":
    sys.exit(main())
