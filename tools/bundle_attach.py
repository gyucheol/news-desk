"""비슷한 뉴스 묶기 공용 함수. 기존 문서에 새 기사(items)를 더하거나, 따로 저장된 문서들을 한 문서로 흡수한다.
mk_one_tg.py(텔레그램 attachTo)와 merge_docs.py(소급 묶기)가 쓴다. 문서 형식은 mk_bundle.py와 같다:
items[{t, o, d, u}], updatedAt(KST ISO) — 데스크는 updatedAt이 읽은 시각보다 늦으면 다시 '안 읽음'으로 보인다."""
from datetime import datetime, timezone, timedelta

KST = timezone(timedelta(hours=9))


def now_kst():
    return datetime.now(KST).strftime('%Y-%m-%dT%H:%M:%S+09:00')


def src_label(d):
    s = d.get('source', '')
    return s + (' ' + d['channel'] if s == '텔레그램' and d.get('channel') else '')


def as_items(d):
    """문서의 기사 목록. 묶음이 아니던 문서는 자기 자신을 기사 1건으로 만든다."""
    if d.get('items'):
        return [dict(it) for it in d['items']]
    return [{'t': d.get('title', ''), 'o': src_label(d), 'd': (d.get('published') or d.get('processed') or '')[:10],
             'u': d.get('url') or (d.get('src') or [{}])[0].get('u', '')}]


def _ind_key(i):
    return (i != 'macro', i)


def attach(d, new_items, fields, today, now=None, extra_src=(), inds=(), nodes=(), published=''):
    """기존 문서 d(사본을 돌려줌)에 new_items를 더한다. fields(title·one·facts·basis·check)는 묶음 전체로 새로 쓴 값."""
    d = dict(d)
    its = as_items(d)
    have = {it['u'] for it in its}
    its += [it for it in new_items if it['u'] not in have and not have.add(it['u'])]
    d['items'] = sorted(its, key=lambda it: it.get('d', ''))
    d.update({k: v for k, v in fields.items() if v not in (None, '')})
    d['headline'] = d['title']
    d['inds'] = sorted(set(d.get('inds', [])) | set(inds), key=_ind_key)
    d['nodes'] = sorted(set(d.get('nodes', [])) | set(nodes))
    hs = {s.get('u') for s in d.get('src', [])}
    d['src'] = d.get('src', []) + [s for s in extra_src if s.get('u') not in hs and not hs.add(s.get('u'))]
    if published > (d.get('published') or ''):
        d['published'] = published
    d['updatedAt'] = now or now_kst()
    d['processed'] = today
    return d


def absorb(keep, others, fields, today, now=None):
    """keep 문서에 others(따로 저장된 비슷한 문서들)의 기사·출처·분야를 모두 옮긴다. others는 지울 대상."""
    new_items, src, inds, nodes, pub = [], [], set(), set(), ''
    for o in others:
        new_items += as_items(o)
        src += o.get('src', [])
        inds |= set(o.get('inds', []))
        nodes |= set(o.get('nodes', []))
        pub = max(pub, o.get('published') or '')
    d = attach(keep, new_items, fields, today, now, src, inds, nodes, pub)
    d.pop('dupOf', None) if d.get('dupOf') in {o['id'] for o in others} else None
    return d


def rotate_seen(seen, old, today, limit=240000):
    """newsSeen 문서가 한도(256KB)에 가까우면 오래된 줄을 newsSeenOld로 옮긴다. 옮겼으면 True."""
    import json
    size = lambda d: len(json.dumps(d, ensure_ascii=False).encode())
    moved = 0
    while size(seen) > limit and len(seen['lines']) > 1:
        k = max(1, len(seen['lines']) // 10)
        old['lines'] = old.get('lines', []) + seen['lines'][:k]
        seen['lines'] = seen['lines'][k:]; moved += k
    if moved:
        seen['count'] = len(seen['lines']); old['count'] = len(old['lines']); old['updated'] = today
    return bool(moved)
