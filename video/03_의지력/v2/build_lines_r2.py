# 03편 v2: build_lines_v3.py와 같고 음절 정렬만 새 녹음(10월 30일 다시 녹음한 구간을 이어 붙인 것)으로 한 것을 읽는다.
# usage: build_lines_r2.py align_ctc.json lines_out.json units_out.json
# 2판 자막 줄 448개에서 [69]만 사진 4장에 맞춰 다시 나눈 450줄 + 음절 정렬 단위를 만든다.
import json, sys
sys.path.insert(0, '../plan')
import plan_data as d
L = json.load(open('../align/lines.json', encoding='utf-8'))
A = json.load(open(sys.argv[1], encoding='utf-8'))
pos = []
for sec in d.SECTIONS:
    for sn, s in enumerate(sec['sents']):
        pass
k = 0; sn = 0; meta = []
for sec in d.SECTIONS:
    for s in sec['sents']:
        sn += 1
        for pi, (t, p) in enumerate(s):
            meta.append((sn, pi, t, p)); k += 1
assert len(meta) == len(L) == len(A) == 448
lines, units = [], []
def add(sn, pi, text, p, syl, src):
    i = len(lines) + 1
    lid = f"V{i:03d}"
    lines.append({'id': lid, 'sent': sn, 'pi': pi, 'text': text, 'pos': p, 'say': src['say'] if 'say' in src else text,
                  'lead': src.get('lead', ''), 'src': src['id']})
    u = {'id': lid, 'text': text, 'shown': text, 'syl': syl, 'start': syl[0][1] if syl else None,
         'start_ctc': syl[0][1] if syl else None}
    units.append(u)
for k in range(448):
    sn, pi, t, p = meta[k]
    if k == 205:   # 준비하고 이동하고 운동하고
        s = A[205]['syl']; s2 = A[206]['syl']
        assert ''.join(x[0] for x in s) == '준비하고이동하고운동하고' and ''.join(x[0] for x in s2) == '씻고돌아와야합니다'
        add(69, 0, '준비하고', p, s[0:4], dict(L[205], say='준비하고', lead=''))
        add(69, 1, '이동하고', p, s[4:8], dict(L[205], say='이동하고', lead=''))
        add(69, 2, '운동하고 씻고', p, s[8:12] + s2[0:2], dict(L[205], say='운동하고 씻고', lead=''))
        continue
    if k == 206:
        s2 = A[206]['syl']
        add(69, 3, '돌아와야 합니다.', p, s2[2:], dict(L[206], say='돌아와야 합니다.', lead=''))
        continue
    if (sn, pi) == (74, 0):   # 사용자 대본(2026-10-29)이 "자 그렇다면"이라 녹음의 '자'를 자막에도 씀(2판은 말하지만 쓰지 않는 말로 둠)
        add(sn, pi, '자 그렇다면', p, A[k]['syl'], dict(L[k], lead=''))
        units[-1].update({kk: A[k][kk] for kk in ('start', 'start_ctc') if kk in A[k]})
        continue
    add(sn, pi, t, p, A[k]['syl'], L[k])
    units[-1].update({kk: A[k][kk] for kk in ('start', 'start_ctc') if kk in A[k]})
json.dump(lines, open(sys.argv[2], 'w'), ensure_ascii=False, indent=1)
json.dump(units, open(sys.argv[3], 'w'), ensure_ascii=False, indent=1)
print(len(lines), 'lines')
