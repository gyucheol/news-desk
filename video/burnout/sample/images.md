# 샘플 이미지 기록 (장면 001~002)

모델: RealVisXL V5.0 Lightning (Hugging Face SG161222/RealVisXL_V5.0_Lightning, 라이선스 openrail++: 상업 이용 가능, 사용 제한 조항 있음)
설정: 1344×768, 5단계, DPM++ SDE Karras, CFG 1.5, CPU 4코어 bf16, 장당 약 2분
공통: 장면 지시문 뒤에 설계표 3-1의 기본 스타일 문구를 붙이고, 금지 문구(글자·로고·실존 인물 등)는 부정 문구로 넣었습니다(scripts/gen.py).

---

## I01 주말 내내 잔 흐트러진 침대 (장면 001)

- 지시문(설계표 I01 그대로): a rumpled bed with a thick duvet in a dim bedroom, soft weekend morning light through curtains, a sleeping silhouette under the blanket
- 후보: 씨앗 101, 102, 103
- 선택: 103. 남색 이불 속에 누운 형태가 보이고, 커튼 사이로 빛이 들어와 지시문에 가장 가깝습니다. 101은 조명이 평평하고, 102는 이불 속 형태가 없습니다.

## I02 어두운 아침, 휴대폰 알람을 끄는 1인칭 손 (장면 002)

1. 설계표 I02 지시문 그대로(씨앗 201~203): 세 장 모두 탈락. 두 사람의 손처럼 보이거나, 휴대폰 대신 다른 기계가 나오거나, 소매가 어색하게 겹쳤습니다.
2. 휴대폰을 앞에 둔 지시문(씨앗 301~302): 탈락. 베이지 소매에 시계 같은 띠, 화면 속 작은 글자, 떠 있는 팔
   - smartphone glowing on a dark nightstand in a pitch dark bedroom at dawn, a hand in a navy knit sleeve with a thin silver ring reaching to tap the screen
3. 1인칭 침대 시점 지시문(씨앗 401~402): 402를 바탕으로 사용. 남색 니트 소매, 은색 반지, 손 모양이 자연스러움. 다만 휴대폰 화면이 꺼져 있었습니다.
   - first-person view from bed in a dark bedroom at dawn, a hand in a navy knit sleeve reaching toward a glowing smartphone on the bedside table
   - 부정 문구 추가: alarm clock, clock, two hands, bright room
4. 화면 켜기(scripts/screen_glow.py, 화면 영역 1089,439,1159,579, 씨앗 503, 강도 0.45): 화면에 푸른 잠금 화면(글자 없이 시계 자리와 버튼 모양만)을 칠하고 이미지 변환으로 다듬은 뒤, 휴대폰 주변만 바꿔 넣었습니다. 손과 나머지 부분은 402 원본 그대로입니다.
   - 흰 화면(씨앗 501·502 첫 시도)은 손전등처럼 보여 버렸고, 씨앗 502(푸른 화면)는 시계 자리가 깨진 글씨처럼 변해 버렸습니다.
- 참고: 협탁 위 랜턴은 모델이 넣은 소품이며 대본과는 관계없습니다.

---

## 제작량 참고 (이 샘플 기준, 추론)

이미지 2장에 후보 10장과 화면 수정 4장이 들었습니다. 손이 나오는 장면은 실패가 잦았습니다. 본편의 사진풍 이미지 69장에 장당 후보 1.5~3장을 가정하면 생성 시간만 약 3.5~7시간입니다(69 × 2분 × 1.5~3). 고르는 시간은 별도입니다.
