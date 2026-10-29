# 03편 v1 제작 기록(credits_v1.md) 만들기: 장면 목록, 사진 번호, 스톡(라이선스), 배경음악, 점검 결과.
# usage: make_credits_v1.py <result.json>   (result.json: 영상 파일 정보와 점검 결과, 렌더링 뒤에 씀)
import glob, json, os, re, sys
R = json.load(open(sys.argv[1], encoding='utf-8')) if len(sys.argv) > 1 and os.path.exists(sys.argv[1]) else {}
SEG = json.load(open('segments.json', encoding='utf-8'))
L = json.load(open('lines_v3.json', encoding='utf-8'))
BGM = json.load(open('audio/bgm_segments.json', encoding='utf-8'))
PICKS = {}
for p in sorted(glob.glob('stock/picks/group_*.json')):
    for x in json.load(open(p, encoding='utf-8')):
        PICKS[x['seg']] = x
OVR = json.load(open('stock_overrides.json', encoding='utf-8')) if os.path.exists('stock_overrides.json') else {}
for k, v in OVR.items():
    PICKS.setdefault(k, {}).update(v)


def mmss(t):
    return f"{int(t // 60)}:{t % 60:04.1f}"


out = []
w = out.append
w("# 03편 「퇴근 후 의지력」 v1 영상 제작 기록")
w("")
w(f"작성 {R.get('date', '2026-10-29')}. 결과 파일: {R.get('file', '03_의지력_v1.mp4')} ({R.get('spec', '1920×1080, 30fps, H.264 + AAC 320kbps 48kHz 스테레오')}, "
  f"{R.get('duration', '')}, {R.get('size', '')}, 소리 크기 {R.get('lufs', '')}). 운영자 목소리와 사용자가 만든 사진이 들어 있어 영상, 녹음, 사진은 "
  "저장소에 올리지 않았습니다(SendUserFile로 전달).")
w("")
w("## 1. 사용자 요청 (2026-10-29)")
w("")
w("- \"대본 및 녹음본, 그리고 ai 사진 전달드림. ai 사진을 사용한 부분은 \"<\"자막\">숫자\" 이렇게 표시해놨음. 예를 들면 \"사진 1\"은 \"<자막>1\"에 사용해주면 됨.\"")
w("- \"[대본] * \"/\"이 표시는 스톡 영상을 앞 뒤로 다르게 써달라는 의미임.\"")
w("- 표시한 대본 전체는 user_script_marked.txt, 사진은 메시지 15개(각 5장)로 75장이 왔습니다.")
w("")
w("## 2. 정한 것과 이유")
w("")
for line in R.get('decisions', []):
    w(f"- {line}")
w("")
w("## 3. 사용자 사진")
w("")
for line in R.get('photo_notes', []):
    w(f"- {line}")
w("")
w("## 4. 장면 목록")
w("")
w("시각은 영상 안에서 장면이 시작하는 때, 괄호는 길이(초)입니다. ' / '는 자막 하나의 끝, (가)는 가운데 자막입니다.")
w("")
for d in SEG:
    if d['kind'] == 'P':
        what = f"사용자 사진 {d['value']}"
    elif d['kind'] == 'K':
        what = "검은 화면"
    else:
        pk = PICKS.get(d['value'], {})
        what = f"스톡 {d['value']} Mixkit {pk.get('id', '?')} ({pk.get('title', '')[:60]})"
    lines = L[d['i0']:d['i1']]
    txt = ' / '.join(('(가)' if l['pos'] in 'ci' else '') + l['text'] for l in lines)
    w(f"{d['n']}. {mmss(d['t0'])} ({d['dur']:.1f}) {what}: {txt}")
w("")
w("## 5. 스톡 영상 (Mixkit, 모두 무료 라이선스)")
w("")
w("영상 페이지의 구조화 데이터(JSON-LD) copyrightNotice가 \"Free\"인 것만 썼습니다(stock/tools/mk.py lic, 확인 기록은 stock/items/lic_*.json). "
  "같은 영상을 두 곳에 쓴 것은 한 줄에 적었습니다. '대신함'은 원하던 장면의 무료 영상이 없어 비슷한 장면을 쓴 곳입니다.")
w("")
COMP = {
    'st09': '쓰러지는 순간은 없고, 쓰러진 뒤 소파에 누워 팔로 눈을 가린 모습',
    'st14': '책을 펴는 장면이 아니라 모눈 공책을 펴고 쓰기 시작하는 손',
    'st21': '화면이 있는 연구실 영상은 모두 제한 라이선스라 현미경을 보는 연구자',
    'st23': 'TV 화면은 보이지 않고, 밤 거실에서 TV 쪽을 보며 먹는 사람',
    'st32': '운동화나 운동 가방 앞에서 망설이는 영상이 없어 길가에 앉아 발만 움직이는 사람',
    'st37': '운동화를 들고 있지 않음. 헬스장에서 지쳐 앉아 있는 사람',
    'st38': '헬스장 입구 영상이 없어 러닝머신에 올라서는 사람',
    'st40': '운동 가방을 싸는 영상이 없어 권투 전에 손에 붕대를 감는 손',
    'st41': '치지 않고 안고만 있는 장면이 아니라 어두운 방에서 기타를 치는 손(흑백, 가운데 자막 뒤라 흐림)',
    'st49': '문을 열고 열쇠를 내려놓는 영상은 모두 제한 라이선스라 집에 들어와 소파에 앉는 사람',
    'st64': '현관에 운동화를 꺼내 두는 영상이 없어 운동화 끈을 묶는 손(가운데 자막 뒤라 흐림)',
    'st76': '77번 사진이 오지 않아 넣은 임시 장면',
    'st81': '퇴근길이 아니라 실내 소파에서 스마트워치를 보는 손목',
    'st82': '7시를 가리키는 무료 영상이 없어 시계 윗부분(11~1)만 보이는 장면',
    'st86': '밤길 영상이 없어 맑은 낮 거리를 걷는 뒷모습을 어둡게(가운데 자막 뒤라 흐림)',
    'st87': '빈 플래너 영상이 없어 달력의 25에 동그라미를 치는 장면(HOLIDAY 글씨는 흐림)',
    'st89': '운동 가방 대신 덤벨을 바닥에 내려놓고 지쳐 앉는 사람',
    'st92': '소파 장면은 없고, 낮 공원에서 운동화 끈을 묶는 사람(마스크를 씀, 가운데 자막 뒤라 흐림)',
}
BW = {'st22', 'st24', 'st25', 'st26', 'st41'}
by_id = {}
for d in SEG:
    if d['kind'] == 'S':
        pk = PICKS.get(d['value'], {})
        if pk.get('id'):
            by_id.setdefault(pk['id'], []).append((d, pk))
for vid, uses in sorted(by_id.items(), key=lambda kv: kv[1][0][0]['t0']):
    pk = uses[0][1]
    parts = []
    for d, u in uses:
        st = d['value']
        x = f"{st} {mmss(d['t0'])}부터({d['dur']:.1f}초, 원본 {float(u.get('in', 0)):.1f}초부터), 원하던 장면: {d.get('desc', '')}"
        if st in COMP:
            x += f", 대신함: {COMP[st]}"
        if st in BW and st != 'st41':
            x += ", 흑백 영상"
        if OVR.get(st, {}).get('why'):
            x += f", 손본 것: {OVR[st]['why']}"
        parts.append(x)
    w(f"- {vid} {pk.get('title', '')}: {pk.get('url', '')} | 라이선스 {pk.get('license_notice', 'Free')} (확인 {pk.get('checked', '')}) | "
      + " / ".join(parts))
w("")
w("## 6. 배경음악 (Mixkit Stock Music Free License)")
w("")
w("AI는 소리를 들을 수 없어서, 곡의 태그와 소리 크기 변화(3초 창 RMS)로 골랐습니다. 곡마다 한 가지 크기로 맞추고(-36 LUFS, 곡 사이 3초 겹침), 목소리와 섞은 전체는 -14 LUFS입니다.")
w("")
for b in BGM:
    w(f"- {mmss(b['start'])}~{mmss(b['end'])} {b['name']} (곡 {b['id']}, {b['offset']}초부터): {b['why']}")
w("")
w("## 7. 점검")
w("")
for line in R.get('checks', []):
    w(f"- {line}")
w("")
w("## 8. 다시 만드는 순서")
w("")
w("run_v1.sh 순서대로입니다. 커밋하지 않은 준비물(녹음, 사진, 스톡 원본, 음악 원본, 모델, 글꼴)은 그 파일 첫머리에 적었습니다.")
w("")
w("## 9. 사용자 확인이 필요한 것")
w("")
for line in R.get('questions', []):
    w(line)
open('credits_v1.md', 'w', encoding='utf-8').write('\n'.join(out) + '\n')
print('credits_v1.md', len(out), 'lines')
