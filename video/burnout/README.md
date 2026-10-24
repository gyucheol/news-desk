# 번아웃 편 영상 제작 도구 (채널 「INFJ입니다.」)

작성 2026-10-21, 갱신 2026-10-23. 핸드오프 문서의 9장(영상 제작·편집 지침)과 10장(번아웃 편 장면 설계표)을 따라 영상을 만드는 스크립트입니다.

- sample/: 초반 11.6초, AI 이미지 + 임시 음성 (2026-10-21)
- sample30/: 30초 예시, 스톡 영상 + 아이콘 화면, 빠른 템포, 목소리 자리 비움 (2026-10-22, 사용자 요청 반영: 본인 목소리, 더 빠른 템포, AI만 쓰면 이질감 → 스톡 섞기). 자세한 기록은 sample30/credits.md
- full/: 번아웃 본편. v9(2026-10-23) 8분 15초: 사용자가 표시한 가운데 문장 12곳을 표시한 자리에서 나눠, 부분마다 같은 가운데 자리에서 차례로 바뀜(8차는 아래 줄에 쌓았는데 사용자가 아니라고 함). v8은 v7에서 그 12곳을 줄이 이어서 나타나게 하고, 2:21 큰 글씨 '번아웃'은 그 단어를 말할 때 나타나며, 7:07 "시작합니다" 안에 들어가 있던 쉼을 단어 뒤로 옮김. v7은 v6에서 자막만 바꿈. 가운데 자막(검은 카드·인용 사진)은 한 문장을 통째로 한 화면에, 아래 자막은 사용자가 나눈 예시대로 대본 전체를 뜻 덩어리로 다시 나눔(316줄 → 281줄, full/subtitles_v7.txt). v6은 v5에서 1:42·2:21의 AI 사진을 스톡 사진(Mixkit 무료 영상의 한 장면)으로 바꾸고, 사진 장면은 옆으로 움직이지 않고 아주 천천히 확대만. v5는 v4(8분 13초)에서 사례 구간 두 문장(31살 직장인, 출근하면 일할 의욕이 없고…)을 사용자의 새 대본·녹음으로 교체, 뉴스 장면은 스톡 신문 사진 위 글자, 새 문장 장면 4개, 인용 뒷배경 천천히 확대, 자막 나눔. v4는 재녹음 끝 울림 복원, U156~U162 재녹음 교체, 녹음을 숨소리·입소리 처리 없이 일정한 음량으로 다시 다듬음, 프로이덴버거 사진(사용자 제공)과 WHO 마크. 장면 137개(스톡 영상 78, 사진 8(AI 4, 사용자 제공 1, 스톡 영상 한 장면 3), 그림 화면 27, 카드 24), 배경음악 8곡(흐름이 바뀌는 곳마다 바꿈). v1(2026-10-22)은 8분 18초였습니다. 추상적인 장면을 AI 사진으로 바꾸는 일은 사용자 지시로 미뤘습니다. 영상과 녹음은 운영자 목소리라 커밋하지 않았습니다. 기록과 다시 만드는 순서는 full/credits.md, 유튜브 챕터는 full/chapters.txt
- HANDOFF_VIDEO.md: 확정된 제작 방식 전체 핸드오프(다른 대화창에서 같은 영상을 만들 때 이 문서부터)
- channel/profile/: 채널 프로필 사진. 최종은 profile.png(2026-10-24 사용자 선택: 'INFJ' 글자만, 마침표 없음). 시안 두 가지('INFJ.' 글자와 전구 그림)와 원형으로 줄인 비교 그림도 있습니다. 도구는 scripts/profile_pic.py
- HANDOFF_FEEDBACK.md: 번아웃 편에서 사용자가 준 영상 피드백만 모은 핸드오프(2026-10-24, 「F의 연애2」 등 다음 영상에 적용할 때). 부록에 사용자 원문 39개, 자막 나누기 예시(부록 B), 쇼츠 한 줄 자막 예시(부록 C)가 있습니다. 10장은 쇼츠·릴스 세로판 피드백입니다(2026-10-24 추가). 같은 날 사용자 답(롱폼, 녹음은 사용자가 편집해서 줌, 썸네일은 번아웃 편에서 고른 1번 방식)을 반영했습니다. 만드는 스크립트는 저장소에 없습니다(대화 기록에서 원문을 뽑아 만듦)
- full/shorts_candidates.json: 번아웃 편에서 쇼츠·릴스로 쓸 만한 구간 후보 5개(2026-10-24, 사용자 선택 대기). 자르는 시각, 첫·끝 문장, 고른 이유, 빼 둔 구간이 있습니다. 가로 미리보기는 scripts/shorts_preview.py로 v9에서 자릅니다(영상은 커밋하지 않음). 자세한 내용은 HANDOFF_VIDEO.md 13장 13-8
- full/shorts/: 쇼츠 세로판 명세. S1.json(2026-10-24, 3:24~3:55 「쉬어도 피곤한 이유」 + 끝 화면 3초)은 장면마다 세로로 자르는 자리, 사용자 예시대로 나눈 한 줄 자막(2차), 자막 모양, 끝 화면 글씨(3차), 위쪽 제목 띠(4차), 배경음악(2차: Tapis)과 소리 섞기 값을 담고, S1_lines.json은 한 줄 자막 조각의 시각입니다(scripts/split_subs.py). scripts/build_short.py로 타임라인과 소리를 만들고 scripts/render_short.py로 1080×1920 렌더링합니다(영상은 커밋하지 않음). 자세한 내용은 HANDOFF_VIDEO.md 2-1의 36번과 13장 13-8
- thumbnail/: 번아웃 편 썸네일 시안. 「F의 연애」 썸네일 틀, 가운데 그림은 좌절하거나 지친 사람, 그림은 효과 없이 원본 그대로, 배경 살린 판과 사람만 남긴 판 두 가지(2026-10-22 사용자 지시). 만드는 법은 HANDOFF_VIDEO.md 18장, 도구는 scripts/thumb.py·cutout.py
- 새 도구(2026-10-22): estimate_timing.py(녹음 전 글자 수로 시각 추정), make_bgm.py(배경음악 자르기·음량), mix_audio.py(녹음+배경음악 섞기, -14 LUFS), polish_voice.py(녹음 다듬기: 숨소리·쉼 간격·입소리, -14 LUFS), icons.py(아이콘 화면 모음), bgm_sequence.py(구간마다 곡을 바꾸는 배경음악), fit_clips.py(짧은 스톡의 시작점·속도 맞추기), ocr_scan.py(렌더링 전 스톡 글자·로고 검사, tesseract). 2026-10-23: onsets.py·ctc_align.py(자막을 목소리 시작에 맞춤, refine.py 대신), gen_batch.py(AMX 없는 CPU에서 AI 이미지 여러 장). 4차: polish_voice.py --keep-levels·--cuts-from·끝 울림 보존, prep_audio.py·mix_audio.py는 일정한 음량(loudnorm의 dynamic 전환 문제). 5차: render.py의 사진 위 글자(overlay, icons.py news_card, 말할 때 한 줄씩). 6차: render.py zoom_rate(사진은 같은 속도로 천천히 확대만), mixkit_search.py 새 카드 형식. 7차: build_timeline.py가 자막 줄 시각(lines_align.json)을 따로 받고 장면은 단위 시각을 씀, full/make_lines_v7.py·align_v7.py(자막 줄 나누기와 시각). 8차: 가운데 문장의 steps(차례로 나타나는 줄)와 장면 큰 글씨의 title_at(render.py, build_timeline.py), full/make_lines_v8.py·align_v8.py·edit_narration_v8.py. 9차: full/make_lines_v9.py(표시한 가운데 문장을 부분마다 한 줄로; steps는 쓰지 않음). 쇼츠(2026-10-24): shorts_preview.py(후보 구간 가로 미리보기), build_short.py(본편 타임라인에서 쇼츠 타임라인과 소리), render_short.py(1080×1920, 버튼·제목 자리를 피한 글자, 상자 없는 한 줄 자막), split_subs.py(한 줄 자막 조각의 시각). setup.sh는 기본 설치에서 AI 모델을 빼고 WITH_AI=1일 때만 받습니다.

작업 규칙(2026-10-22 사용자 지시): 임시 음성(합성 음성)은 만들지 않습니다. 녹음 전에 자막 시각이 필요하면 글자 수로 추정합니다(분당 약 527자). 녹음본이 오면 align.py → onsets.py → ctc_align.py로 그 녹음에 맞춥니다(2026-10-23부터, refine.py는 쓰지 않음). 운영자 녹음은 끝을 자르지 않고, 숨소리·입소리 처리 없이(--keep-levels), 일정한 음량으로만 맞춥니다(2026-10-23 사용자 지시).

---

## 1. 샘플 (sample/)

- burnout_hook_sample.mp4: 1920×1080, 30fps, H.264 + AAC 48kHz, 약 11.6초
- 장면: 001 흐트러진 침대(I01) → 002 알람을 끄는 1인칭 손(I02) → 003 검은 화면 속마음 카드(설계표 그대로)
- 목소리: 임시 안내 음성(edge-tts의 ko-KR-SunHiNeural)입니다. 업로드용이 아니며, 실제 영상은 운영자 녹음으로 바꿉니다.
- 배경음악·효과음: 넣지 않았습니다. 지침 10-6에 따라 저작권이 해결된 음원(유튜브 오디오 보관함 등)을 골라 넣어야 하는데, 이 환경에서는 그 음원을 고르거나 들어 볼 수 없습니다.
- 이미지: 이 환경(CPU)에서 RealVisXL V5.0 Lightning(라이선스 openrail++, 상업 이용 가능)으로 생성했습니다. 장당 약 2분입니다. I01은 후보 3장 중 1장, I02는 후보 7장 중 1장을 고른 뒤 휴대폰 화면만 켜는 수정을 했습니다(sample/images.md).
- 재현: sample/의 sentences.json, units.json, spec.json으로 2장의 순서를 그대로 밟으면 같은 영상이 나옵니다(다시 만들어 본 결과 자막 시각 차이 0.02초 이내).

### 1-1. 지침 반영 내용
1. 하단 자막(지침 6-1): Pretendard SemiBold 64(한글 높이 56px, 화면 높이의 5.2%), 흰 글씨, 박스 아래 끝 92.8%, 한 줄 박스 85.0~92.8%, 검정 불투명도 88%, 좌우 여백 28px, 가운데 정렬
2. 검은 화면 카드(지침 6-2): 화면 정가운데, 하단 자막과 같은 크기, 박스 없음, 속마음은 기울임(12도, 한글 글꼴에 기울임체가 없어 기울여 그림)
3. 노란색 강조(#F2C94C)는 '[단어]' 표기로 지원합니다. 설계표에서 첫 강조는 장면 025('번아웃')라 이 샘플에는 없습니다.
4. 이미지 톤(지침 10-4-1): 설계표 3-1의 기본 스타일 문구를 붙여 생성하고, 장면끼리 톤이 맞도록 공통 보정(채도 88%, 중간톤 약간 어둡게, 가장자리 어둡게)을 넣었습니다.
5. 움직임: 사진 장면은 천천히 확대(최대 5%)합니다. 본보기 채널의 움직임 효과는 확인하지 못했고(지침 1-3), 설계표 3-1의 8번 메모(같은 이미지 천천히 확대)를 모든 사진 장면에 넓혀 쓴 제작 선택입니다.
6. 자막 전환: 각 자막은 말소리 시작 0.1초 전에 나타나 다음 자막이 나올 때까지 유지합니다. 장면은 그 장면의 첫 자막과 함께 바뀝니다.
7. 음량: -14 LUFS 근처(지침 10-6), 최종 파일 실측 -14.0 LUFS, 최대 -1.5 dBTP

---

## 2. 녹음본으로 만드는 순서

1. 새 세션에서 한 번: `./setup.sh` (패키지, 글꼴, 모델 약 10GB)
2. 음량 맞추기: `venv/bin/python scripts/prep_audio.py 녹음.m4a work/narration.wav`
3. 자막 단위 목록(units.json): 장면 설계표 자막의 '/' 단위를 순서대로 적습니다(sample/units.json 참고).
4. 말한 시각 찾기
   - `venv/bin/python scripts/align.py work/narration.wav units.json work/align.json`
   - `venv/bin/python scripts/onsets.py work/narration.wav work/align.json work/onsets.json`
   - `venv/bin/python scripts/ctc_align.py work/narration.wav work/onsets.json models/w2v_ko work/align_refined.json`
5. 장면 명세(spec.json): 장면마다 유형과 시작 자막(sample30/spec.json 참고)
   - video: 스톡 영상 src, 시작 지점 in(초), 재생 속도 speed, 자막 안에서 자를 때 offset(초)
   - photo: 이미지 image, 확대 z0→z1, 초점 이동 cx/cy
   - icon: 지침 6-3 아이콘 화면(bulb, battery, scripts/icons.py의 종류)
   - video의 crop(가장자리 글자·로고 잘라 내기), blur(흐림), card의 label(위쪽 작은 회색 글씨)
   - card: 검은 화면 카드
   - 장면별 색 보정 grade(sat, black, gamma, vignette). 밝은 스톡 영상은 gamma를 높여 다른 장면과 맞춥니다.
   - 검은 화면 위 하단 자막은 "box": false(지침 6-1의 7번)
6. `venv/bin/python scripts/build_timeline.py spec.json work/align_refined.json work/narration.wav work/timeline.json` 다음 `venv/bin/python scripts/fit_clips.py work/timeline.json`(짧은 스톡 맞추기). 배경음악을 섞는 경우는 narration.wav 대신 섞은 파일을 넣습니다(HANDOFF_VIDEO.md 7장 7번).
7. 글자 검사 `venv/bin/python scripts/ocr_scan.py work/timeline.json work/ocr` 다음 `venv/bin/python scripts/render.py work/timeline.json out.mp4` (점검용 정지 화면: `--frames-only 1.5,3.0`)
8. 점검: `venv/bin/python scripts/contact.py out.mp4 sheet.png 0.5,2.5,4.0`

이미지 생성: `venv/bin/python scripts/gen.py I02 301,302 "<장면 지시문>"` (장면 지시문 + 기본 스타일 문구가 77토큰을 넘으면 뒤가 잘립니다. 실행 때 토큰 수를 출력합니다.)
화면 부분 수정 예: `venv/bin/python scripts/screen_glow.py work/img/I02B_s402.png work/img/I02D 1089,439,1159,579 503`

(사용하지 않음, 위 작업 규칙) 임시 음성으로 미리 보기: `venv/bin/python scripts/tts.py sample/sentences.json work/narration_raw.wav` 후 2번부터 같습니다.

### 2-1. 스톡 영상 고르기 (Mixkit)
1. 검색: `venv/bin/python scripts/mixkit_search.py work/stock/search alarm sleeping tired` (검색어마다 한 페이지, 2초 간격)
2. 눈으로 고르기: `scripts/thumbsheet.py`(썸네일 모음), 미리보기 영상을 받아 `scripts/filmstrip.py`(영상당 6장면)
3. 라이선스 확인(필수): `venv/bin/python scripts/mixkit_license_check.py work/stock/search/index.json work/stock/items 31411,28899`
   - 결과가 Free인 것만 씁니다. "Mixkit Restricted License"는 수익화 유튜브 영상에 쓸 수 없습니다. 검색 결과에는 표시되지 않습니다.
4. 고른 영상만 1080p로 받습니다(sample30/fetch_stock.sh 참고). 사이트 약관은 라이브러리 전체를 긁어 가는 대량 다운로드를 금지합니다.
5. 사람·상황 장면은 스톡 영상, 상징 장면은 아이콘 화면이나 사물 위주의 AI 이미지를 씁니다(AI의 어색함은 주로 사람·손에서 생깁니다).

참고: 2026-10-22 세션 재시작 뒤 CPU가 AMX(bf16)를 지원하지 않는 기종으로 바뀌어 gen.py가 매우 느려졌습니다(장당 10분 이상). 이미지 생성 전에 `grep -o amx_bf16 /proc/cpuinfo`로 확인하십시오.

---

## 3. 싱크 검증 (임시 음성 기준)

1. 음성 인식(faster-whisper large-v3)의 단어 시각만 쓰면, 쉼 뒤에 오는 자막 단위의 시작이 0.3~0.7초 이르게 잡혔습니다(앞의 쉼을 다음 단어에 붙임).
2. refine.py 보정 후 6개 단위 모두 파형에서 읽은 말소리 시작점과 0.04초 이내였습니다.
3. 대본을 음성 인식 힌트(initial prompt)로 넣으면 첫 문장을 통째로 빠뜨려서, 힌트 없이 인식합니다.
4. 한계: 깨끗한 합성 음성으로 확인한 결과입니다. 실제 녹음(잡음, 숨소리, 문장부호와 다른 쉼)에서는 결과를 다시 확인해야 합니다.
