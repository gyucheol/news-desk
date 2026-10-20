import json, re, sys

TAIL = re.compile(r' \((제목 기준|채널 전언)\)$')
TAGS = ('[사실]', '[채널]', '[제목]', '[추론]', '[미확인]')


def plain(s):
    return s.replace('{{', '').replace('}}', '')


def emph(s):
    """Return (length without braces, emphasized chars, chunk list, problems)."""
    probs = []
    if s.count('{{') != s.count('}}'):
        probs.append('unbalanced braces')
    chunks = re.findall(r'\{\{(.*?)\}\}', s)
    for c in chunks:
        if '{{' in c:
            probs.append('nested: ' + c)
        if len(c) > 30:
            probs.append('chunk>30(%d): %s' % (len(c), c))
        if c != c.strip():
            probs.append('chunk space edge: [%s]' % c)
        if c and c[-1] in ',.\'"':
            probs.append('chunk ends punct: ' + c)
        if c and c[0] in ',.\'"':
            probs.append('chunk starts punct: ' + c)
    total = len(plain(s))
    em = sum(len(c) for c in chunks)
    return total, em, chunks, probs


def rep(label, s, lo, hi, need_emph=True):
    body = TAIL.sub('', s)
    tail = s[len(body):]
    total, em, chunks, probs = emph(body)
    ratio = em / total if total else 0
    flags = []
    if not (lo <= total <= hi):
        flags.append('LEN %d not in %d~%d' % (total, lo, hi))
    if need_emph and not (0.50 <= ratio <= 0.65):
        flags.append('EMPH %.0f%%' % (ratio * 100))
    if '**' in s:
        flags.append('has **')
    flags += probs
    print('  %-6s len=%3d emph=%3.0f%% tail=%r %s' % (label, total, ratio * 100, tail, ' !! ' + '; '.join(flags) if flags else ''))
    return body


def main(path):
    d = json.load(open(path))
    print('agent', d['agent'], 'searches', d['searches_used'], 'fetches', d['fetches_used'])
    for x in d['items']:
        multi = len(x['items']) > 1 or bool(x['attachTo'])
        print(x['cid'], x['basis'], 'attach=%r' % x['attachTo'], 'n_items=%d' % len(x['items']), x['inds'], x['nodes'])
        rep('title', x['title'], 20, 50)
        one = plain(rep('one', x['one'], 90 if multi else 80, 160 if multi else 130))
        if not one.endswith('다'):
            print('  !! one does not end with 다')
        # tail consistency
        if x['basis'] == 'title' and not x['one'].endswith(' (제목 기준)'):
            print('  !! basis title but no (제목 기준) tail')
        if x['basis'] == 'channel' and not x['one'].endswith(' (채널 전언)'):
            print('  !! basis channel but no (채널 전언) tail')
        if x['basis'] in ('verified', 'partial') and TAIL.search(x['one']):
            print('  !! verified/partial but has tail')
        f = x['facts']
        if not (2 <= len(f) <= 5):
            print('  !! facts count', len(f))
        if not f[0].startswith('무엇이:'):
            print('  !! first fact not 무엇이:')
        for line in f:
            if not line.endswith(TAGS):
                print('  !! fact tag missing:', line[-20:])
            if '|' in line or '**' in line or '{{' in line:
                print('  !! fact has forbidden char:', line[:40])
            if ': ' not in line[:20]:
                print('  !! fact label?', line[:30])
        for k in ('check',):
            if '{{' in x[k] or '|' in x[k]:
                print('  !! check has braces or |')
        if multi:
            if 'added' not in x or not x['added']:
                print('  !! added missing')
            else:
                a = plain(rep('added', x['added'], 60, 140))
                if not a.endswith('다'):
                    print('  !! added does not end with 다')
                if not a.startswith('이번 '):
                    print('  !! added does not start with 이번')
        else:
            if x.get('added'):
                print('  !! added present for single item')
        prev = ''
        for it in x['items']:
            tl = len(it['t'])
            fl = []
            if not (25 <= tl <= 60):
                fl.append('t len %d' % tl)
            if '{{' in it['t']:
                fl.append('t has braces')
            if not re.match(r'^\d{4}-\d{2}-\d{2}$', it['d']):
                fl.append('bad d')
            if it['d'] < prev:
                fl.append('order')
            prev = it['d']
            print('   item %s %s t=%d %s' % (it['d'], it['o'], tl, ' !! ' + ','.join(fl) if fl else ''))
            if multi:
                if not it.get('s'):
                    print('   !! s missing')
                else:
                    s = plain(rep('s', it['s'], 45, 110))
                    if not s.endswith('다'):
                        print('   !! s does not end with 다')
            elif it.get('s'):
                print('   !! s present for single item')
        for s in x['src']:
            if 'bloomberg' in s['u'] or 'reuters' in s['u']:
                print('  !! src has bbg/rtr', s['u'])
    print('skipped', d['skipped'])


if __name__ == '__main__':
    main(sys.argv[1])
