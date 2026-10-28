# 03편 장면 표시 대본 만드는 파일 (2판)

- plan_data.py: 문장별 자막 조각과 자리(아래, 가운데, 가운데 기울임)
- plan_scenes.py: 장면 나누기. 장면마다 화면 하나(첫 문장 번호, 화면, 화면 반 나누기의 오른쪽이 나오는 자막, 큰 글씨)
- plan_registry.py: AI 사진(묶음, 요청문), 스톡, 그래픽 설명
- plan_gen.py: 번호 매기기(처음 나오는 순서), 25자·쉼표·따옴표·같은 화면 이어짐 점검, 장면 길이와 흐림 구간 계산, 목록 만들기
- doc_build.py + doc_template.md + fact.md: 03_의지력_장면표시.md 만들기
- extra.json: 자막 조각마다 녹음에서 시작하는 시각(음절 맞춤 결과), 영상 끝 시각, 숫자를 소리 내 읽은 말

다시 만들기: 이 폴더에서 python3 -I plan_gen.py, 그다음 python3 -I doc_build.py ../03_의지력_장면표시.md
(plan_gen.py가 만드는 scene_list.md, ai_list.md, stock_list.md, graphics_list.md, summary.json, shots_v2.json은 저장소에 올리지 않습니다.)
