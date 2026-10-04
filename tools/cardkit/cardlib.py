import json, os
def s(o, d, u): return {"o": o, "d": d, "u": u}
def card(**k):
    k.setdefault('source', '텔레그램'); k.setdefault('channel', ''); k.setdefault('dupOf', ''); k.setdefault('insight', {})
    return k
def save(cards, d='cards'):
    os.makedirs(d, exist_ok=True)
    for c in cards:
        json.dump(c, open(os.path.join(d, c['key'] + '.json'), 'w'), ensure_ascii=False, indent=1)
    print('saved', len(cards))
