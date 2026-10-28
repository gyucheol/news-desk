# 03편 장면 표시 대본 만드는 파일

- plan_data.py: 문장별 자막 조각, 화면, 자막 자리, 가운데 자막 배경
- plan_registry.py: AI 사진(묶음, 요청문), 스톡, 그래픽 설명
- plan_times.py: 녹음 받아 적기(whisper 낱말 시각)로 문장 시작 시각 찾기 → extra.json
- plan_gen.py: 번호 매기기(대본 순서), 25자·쉼표·따옴표 점검, 목록 만들기
- doc_build.py + doc_template.md + fact.md: 03_의지력_장면표시.md 만들기
- extra.json: 구간·문장 시각, 숫자를 소리 내 읽은 말(자막 시각 맞출 때 씀)

다시 만들기: plan_gen.py를 돌린 다음 doc_build.py ../03_의지력_장면표시.md (이 폴더에서, python3 -I). plan_times.py는 녹음 받아 적기 파일 경로가 작업 폴더(스크래치패드) 기준입니다.
