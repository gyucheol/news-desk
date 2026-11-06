# 살걸·팔걸 편 v1 기록(README.md) 만들기 (2026-11-06). 스톡 목록과 완성 파일 정보는 파일에서 읽어 채움.
# usage: make_readme.py OUT.md [VIDEO.mp4]   (salgeol/v1에서)
import glob, json, os, subprocess, sys

out = sys.argv[1]
video = sys.argv[2] if len(sys.argv) > 2 else None
L = json.load(open('lines.json', encoding='utf-8'))
SEG = json.load(open('segments.json', encoding='utf-8'))
PICKS = {}
for p in sorted(glob.glob('stock/picks/group_*.json')):
    for x in json.load(open(p, encoding='utf-8')):
        PICKS[x['seg']] = x
OVR = json.load(open('stock_overrides.json', encoding='utf-8')) if os.path.exists('stock_overrides.json') else {}
TL = json.load(open('timeline.json', encoding='utf-8')) if os.path.exists('timeline.json') else None
tl_by_from = {}
if TL:
    for sc in TL.get('scenes', []):
        tl_by_from[sc.get('from')] = sc
used_n = len(open('stock/used_before.txt').read().split())

# 바꾼 까닭(사람이 쓴 짧은 말). 고른 기록의 영상과 다른 영상을 쓴 장면만.
WHY = {
    'st24': '바꿈: 고른 144(창가에서 휴대폰을 치는 손)는 번아웃 편에서 쓴 영상이라, 카페에서 노트에 적는 남자의 손(1744)으로',
    'st32': '바꿈: 고른 1013(해변을 걷는 맨발)은 번아웃 편에서 쓴 영상이라, 고른 사람의 예비 영상인 달과 구름(3147)으로',
    'st32b': '48번 사진 자리. 바꿈: 고른 4511(창가의 여성 뒷모습)은 주인공(남성)의 속마음 문장과 맞지 않고 번아웃 편에서도 쓴 영상이라, '
             '남자의 손이 옛 앨범을 여는 영상(4644)으로(지난 일을 돌아봄)',
}


def fmt_t(t):
    m, s = divmod(t, 60)
    return f'{int(m)}:{s:04.1f}'


def stock_lines():
    rows = []
    for d in SEG['segs']:
        if d['kind'] == 'P':
            continue
        st = d['value']
        pk = dict(PICKS.get(st, {}))
        pk.update({k: v for k, v in OVR.get(st, {}).items()})
        pk = {k: v for k, v in pk.items() if v is not None}
        texts = [L[i]['text'] for i in range(d['i0'], d['i1'])]
        t = ' / '.join(texts)
        if len(t) > 70:
            t = t[:68] + '…'
        if not pk.get('id'):
            rows.append(f"- {st} {d['t0']:.1f}초부터 {d['t1'] - d['t0']:.1f}초: (스톡 없음) {t}")
            continue
        sc = tl_by_from.get(L[d['i0']]['id'], {})
        tin = sc.get('in', pk.get('in', 0.0))
        spd = sc.get('speed', pk.get('speed', 1.0))
        extra = []
        if st in WHY:
            extra.append(WHY[st])
        if pk.get('blur_box'):
            extra.append('상표·글자 자리 흐림')
        if spd and abs(float(spd) - 1.0) > 1e-6:
            extra.append(f'{float(spd):g}배 속도(영상이 장면보다 짧음)')
        tail = (' | ' + '; '.join(extra)) if extra else ''
        rows.append(f"- {st} {d['t0']:.1f}초부터 {d['t1'] - d['t0']:.1f}초, Mixkit {pk['id']} \"{pk.get('title', '')}\" "
                    f"({float(tin):g}초부터): {t}{tail}")
    return rows


def video_info(p):
    if not p or not os.path.exists(p):
        return '- 완성: (렌더링 뒤에 채움)'
    q = lambda *a: subprocess.run(['ffprobe', '-v', 'error', *a, p], capture_output=True, text=True).stdout.strip()
    w, h, fr, nb = q('-select_streams', 'v:0', '-count_packets', '-show_entries', 'stream=width,height,r_frame_rate,nb_read_packets',
                     '-of', 'csv=p=0').split(',')
    dur = float(q('-show_entries', 'format=duration', '-of', 'csv=p=0'))
    a = q('-select_streams', 'a:0', '-show_entries', 'stream=codec_name,sample_rate,channels,bit_rate', '-of', 'csv=p=0').split(',')
    num, den = fr.split('/')
    lufs = subprocess.run(['ffmpeg', '-hide_banner', '-nostats', '-i', p, '-map', '0:a', '-af', 'ebur128=peak=true', '-f', 'null', '-'],
                          capture_output=True, text=True).stderr
    I = [l for l in lufs.splitlines() if l.strip().startswith('I:')]
    P = [l for l in lufs.splitlines() if l.strip().startswith('Peak:')]
    li = I[-1].split()[1] if I else '?'
    pk = P[-1].split()[1] if P else '?'
    m, s = divmod(dur, 60)
    return (f'- 완성: {os.path.basename(p)}(올리지 않음), {w}x{h}, {round(int(num) / int(den))}fps, {int(nb):,}프레임({dur:.2f}초, '
            f'{int(m)}분 {s:.0f}초), 소리 {a[0].upper()} {round(int(a[3]) / 1000)}kbps {int(a[1]) // 1000} kHz '
            f"{'스테레오' if a[2] == '2' else a[2] + '채널'}, {li} LUFS, true peak {pk} dBFS.")


TEXT = f"""# 살걸·팔걸 편 영상 v1 기록 (2026-11-06)

사용자께서 보내 주신 최종 대본(../대본_최종_사용자.txt, 사진 번호는 ../대본_사진표시.md), AI 사진 47장, 녹음 3개로 만든 첫 영상의 기록입니다.
영상, 녹음, 사진, 스톡 원본, 음악 원본은 올리지 않았습니다.

요청(2026-11-06)
- "대본, 녹음본, 사진 줄테니 영상제작 바로 돌입. 대본은 너가 가지고 있고, 사진은 내가 여기에 넣는 순서대로 번호 매겨서 쓰면됨."
- 사진은 메시지 세 개(17 + 20 + 10장)로 받아 받은 순서대로 1~47번. 녹음은 세 개(1_1, 2_1, 3_1).
- "47,48번은 동일한 사진을 쓰던, 아니면 스톡 영상을 활용하던 해줘": 48번 사진은 만들지 않음. 47번 사진은 '셋째. 오답노트를
  작성하세요'와 첫 혼잣말까지 쓰고, 48번 자리('그때 내가 너무 좋은 쪽으로만 / 생각했었던 것 같아.')는 스톡 영상(st32b).

파일과 순서(작업 폴더 scratchpad/salgeol/v1, 전체 순서는 run_v1.sh)
1. 사진: 받은 순서 = 대본 번호(photos_in/P01~P47.png, 모두 1024x572).
2. 별 표시 지우기: 03·04편, 수면 편과 같은 도구(wm_remove_v3.py, wm_post.py, wm_choose.py). 03편 2000 크기의 깨끗한 별 모양을
   1024 크기로 줄여 씀(별 중심 934.5, 482.5). 사진마다 고른 방법(메움 또는 되살림)은 wm_choose_1024.txt(1~37번),
   wm_choose_1024_b.txt(38~47번). 별 자리를 크게 본 점검 시트에서 자국이 보이지 않음.
3. make_photos.py: photos_final/PNN.png. 흐림: 37번 상자 옆면의 쇼핑몰 로고와 글자, 29번 간판의 전화번호처럼 보이는 숫자 두 곳.
4. 녹음: 48 kHz 모노로만 바꿈(자르거나 속도를 바꾸지 않음). join_narration.py로 세 파일을 이어 rec/rec.wav(468.90초).
   세 파일 모두 말이 0.05초 안에 시작하고 끝에서 약 0.2초 안에 끝나서, 이음매에 무음을 넣어 쉼을 맞춤(1→2 0.70초, 2→3 0.50초;
   녹음 안 문장 사이 쉼은 0.25~0.59초). 목소리 끝 468.72초(rec/voice_end.json), 영상 끝 = 목소리 끝 + 3초 = 471.72초.
5. 받아쓰기(faster-whisper large-v3, rec/partN_words_seg.json)와 대본 대조. 숫자와 알파벳은 ko_words.py로 읽는 말(30% -> 삼십
   퍼센트, A -> 에이)로 바꿔 맞춤(rec/partN_words_ko.json).
   - 받아쓰기가 지어낸 말 두 곳은 음절 모델(w2v_ko)로 소리가 없음을 확인하고 맞춤에서 뺌: 1번 파일 170.8초 뒤(파일 끝),
     2번 파일 87.2~87.67초('상처를 겪었습니다'; '상철은'은 한 번만 읽힘).
   - 녹음과 대본이 다른 곳(ctc_check_batch.py, rec/checks1~3.json):
     '답한 람이 76%였습니다'(대본의 '람이'를 그대로 읽은 것으로 보임, 두 모델 모두 '사' 없음) -> 자막은 '답한 사람이 76%였습니다.',
     맞춤은 녹음대로. '것 같애' -> 녹음이 '같아'에 가까워 자막 '같아'. 대본 '* 016년' -> 녹음 '이천십육 년' -> 자막 '2016년'.
     '팔지말껄' -> 자막 '팔지 말걸'.
6. plan_salgeol.py(문장, 자막 조각, 자리 b 아래 / c 가운데 / i 가운데 기울임, 화면 P 사진 / st 스톡) -> make_lines.py ->
   lines.json(자막 {len(L)}줄), units.json. 03·04편, 수면 편과 같은 규칙: 숫자는 아라비아 숫자, 쉼표 없음, 질문·해석·제목·마무리는
   가운데, 따옴표 속 속마음은 가운데 기울임. 같은 번호가 바로 이어지면(40 -> 40, 41 -> 41, 47 -> 47) 앞 화면을 그대로 씀.
7. run_align.sh(04편과 같은 도구: align_words.py, onsets.py, ctc_align.py, onsets_v2.py) -> onsets_v2.json. ctc_recheck.py로
   모든 줄을 앞 줄과 함께 다시 맞춰 봄(recheck_all.json): V105('2016년 프리드먼과…')만 1.06초 늦게 잡혀(첫 낱말 뒤 쉼을 시작으로
   봄) fix_onsets.py로 189.58초로 고침 -> onsets_v3.json. 나머지 줄은 0.15초 안에서 같음.
8. build_segments.py -> segments.json(장면 {len(SEG['segs'])}개: 사진 {sum(1 for d in SEG['segs'] if d['kind'] == 'P')}, 스톡 {sum(1 for d in SEG['segs'] if d['kind'] != 'P')}),
   build_spec.py -> spec.json(수면 편과 같은 방식: 사진은 아주 천천히 확대만, 가운데 자막 동안 그림을 흐리고 어둡게).
9. 소리: prep_audio.py(목소리 -14 LUFS, 이 녹음은 +3.2 dB), bgm_sequence.py(배경음악 6곡, -36 LUFS, 곡마다 고정 크기, 3초 겹쳐
   바꿈, 끝 4초 줄임), mix_audio.py(-14 LUFS, 끝 단계 제한기).
   - 제한기 메모: 목소리를 +3.2 dB 올리면 가장 큰 곳이 +1.2 dBTP가 되어, 끝 단계 제한기가 10 ms 구간의 약 17%에서 최대 2.7 dB
     줄임. 결과 -14.0 LUFS, true peak -1.5 dBFS.
10. build_timeline.py, fit_clips.py, render_parallel.py(3조각, 영상만) + ffmpeg로 소리 합침(AAC 320kbps).

배경음악(Mixkit Stock Music Free License, audio/bgm_segments.json)
- 0:00~1:12.5 Fallen (Asper) / Eugenio Mininni (565): ① 도입(03편 v2에서 사용자가 고른 도입 곡, 04편·수면 편 도입과 같음)
- 1:12.5~2:47.6 Staring at the Night Sky / Alejandro Magaña (168): ② 원인 1(오딘, 바버와 오딘)
- 2:47.6~4:02.9 Tapis / Eugenio Mininni (615): ③ 원인 2(판 뒤의 밤, 프리드먼과 캐머러 실험)
- 4:02.9~5:28.7 Classical 2 / Jonny S. (709): ④ 원인 3(폴과 조지 문항, 길로비치와 메드벡)
- 5:28.7~7:21.3 Miss You / Eugenio Mininni (592): ⑤⑥ 해결책 1·2
- 7:21.3~끝 Rebecca on the Shore / Eugenio Mininni (545): ⑦ 해결책 3과 마무리(곡의 끝이 영상 끝과 맞게 58초부터)

스톡(Mixkit, 모두 라이선스 Free, 2026-11-06 확인. 고른 기록은 stock/picks/group_A·B·C.json, 바꾼 것은 stock_overrides.json.
앞 편에서 쓴 영상은 stock/used_before.txt({used_n}개)로 거름)
"""

TAIL = """
점검
- 렌더링 전: 스톡마다 쓰는 구간의 처음·가운데·끝 프레임을 한 줄에 놓은 시트(pick_sheet.py)로 얼굴, 글자, 상표, 컷 전환을 봄.
- 앞 편 영상 목록 보완: used_before.txt(190개)에 번아웃 편(첫 편) 영상 39개가 빠져 있던 것을 찾아 넣음(229개). 그래서 st24(144),
  st32(1013)를 바꿈. 고른 사람들의 예비 영상 가운데 번아웃 편 영상(4397, 28893, 144)은 쓰지 않음.
- 주인공은 남성(사진 1, 3, 20, 46 등)이라, 주인공의 속마음 자리(st32b)에 다른 사람(여성)이 나오지 않게 바꿈.
- 장면마다 가운데 시각의 프레임을 뽑아 봄(scene_sheet.py): 사진 번호, 자막 자리와 글자, 가운데 자막 밑 흐림, 상표.
{video}
- 남은 것: '답한 람이 76%였습니다' 문장을 다시 녹음할지(사용자 답 기다림, 다시 녹음하지 않으면 지금 녹음 그대로).
  24번 사진은 머리에 뇌파 측정 모자(EEG)를 쓴 모습이지만 실제 연구(프리드먼과 캐머러 2016)는 MRI 장치 안에서 함(사진 목록도 MRI).
"""

body = TEXT + '\n'.join(stock_lines()) + '\n' + TAIL.format(video=video_info(video))
open(out, 'w', encoding='utf-8').write(body)
print(out, len(body.splitlines()), 'lines')
