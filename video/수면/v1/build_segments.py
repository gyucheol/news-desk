# 화면이 바뀌는 곳(plan_data의 화면 칸)마다 장면 하나. 시작은 그 장면 첫 자막의 목소리 시작(onsets_v2), 끝은 다음 장면 시작.
# 마지막 장면은 영상 끝(목소리 끝 + 3초)까지. 수면 편(2026-11-04): lines.json, rec/voice_end.json. 인자: [onsets 파일] [출력 파일]
import json, sys
L = json.load(open('lines.json', encoding='utf-8'))
O = {o['id']: o for o in json.load(open(sys.argv[1] if len(sys.argv) > 1 else 'onsets_v2.json', encoding='utf-8'))}
J = json.load(open('rec/voice_end.json'))
END = round(J['voice_end'] + 3.0, 3)
segs = []
for i, l in enumerate(L):
    if l['vis'] or i == 0:
        segs.append({'vis': l['vis'], 'i0': i})
for k, s in enumerate(segs):
    s['i1'] = segs[k + 1]['i0'] if k + 1 < len(segs) else len(L)
    s['t0'] = round(O[L[s['i0']]['id']]['start'], 3) if k else 0.0
    s['t1'] = round(O[L[s['i1']]['id']]['start'], 3) if s['i1'] < len(L) else END
    s['dur'] = round(s['t1'] - s['t0'], 2)
    s['n'] = k + 1
    s['kind'] = 'P' if s['vis'].startswith('P') else 'S'
    s['value'] = s['vis']
    s['text'] = ' / '.join(L[i]['text'] for i in range(s['i0'], s['i1']))
    s['pos'] = ''.join(L[i]['pos'] for i in range(s['i0'], s['i1']))
json.dump({'end': END, 'segs': segs}, open(sys.argv[2] if len(sys.argv) > 2 else 'segments.json', 'w'), ensure_ascii=False, indent=1)
st = [s for s in segs if s['kind'] == 'S']
print(len(segs), 'scenes |', sum(1 for s in segs if s['kind'] == 'P'), 'photo scenes,', len(st), 'stock | end', END)
print('photo time', round(sum(s['dur'] for s in segs if s['kind'] == 'P'), 1), 'stock time', round(sum(s['dur'] for s in st), 1))
for s in st:
    print(f"{s['value']} {s['t0']:7.2f} {s['dur']:5.2f}s [{s['pos']}] {s['text']}")
print('shortest', sorted((s['dur'], s['vis']) for s in segs)[:6])
