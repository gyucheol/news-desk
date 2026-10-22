# 음성 보정 원리 조사 (2026-10-22)

질문: "보통 녹음본을 다듬거나 보정하는 프로그램들은 어떻게 목소리를 보정하는지"

1. report.md: 최종 보고서입니다(한국어, 약 4만 5천 자, 인용 195개). 근거를 [문서]·[경험칙]·[업체 주장]·[2차]·[추론]·[비공개]로 구분해 표시했습니다. 제목은 "음성 보정은 소음을 덜어내고, 생성형 AI는 목소리를 다시 그린다"입니다.
2. research_notes/: 서브 에이전트 4개의 조사 노트(영어)입니다. 노트마다 Takeaway, Cited Findings, Inferences, Gaps 형식이고 모든 주장에 링크가 붙어 있습니다.
   - traditional_dsp.md: 전통 신호처리(잡음 제거, 험·저음 컷, EQ, 다이내믹스, 잔향 제거, 라우드니스 표준)
   - ai_speech_enhancement.md: AI 음성 향상(마스크형, 음원 분리, 생성형 복원, 품질 지표, 실시간 처리)
   - products_and_workflows.md: 제품별 기능(iZotope RX 12, Adobe Enhance Speech, Descript, Auphonic, Audacity, 실시간·모바일 도구)
   - singing_pitch_correction.md: 노래 음정·타이밍 보정(Auto-Tune, Melodyne, 피치 검출·이동 알고리즘)
3. PROMPTS.md: 조사, 보고서 작성, 환경 검증, AI 고음 복원 시험에 쓴 서브 에이전트 지시서입니다. 경로는 자리표시자로 바꿨습니다.

사용자 음성 파일과 처리 결과는 공개 저장소라 넣지 않았습니다(압축 파일에 있습니다).
