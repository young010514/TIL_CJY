# 프론트엔드 (1단 — 브라우저)

3단 구조에서 **첫 번째 단**입니다. 사용자 입력을 받아 **Django 중간 서버(8080)** 로만 HTTP 요청합니다.  
프론트에는 CORS 설정이 없습니다. CORS는 Django(8080)에서만 설정합니다.

## API 목록 (Django 기준 경로)

- `/api/v1/chat/completions/`
- `/api/v1/chat/guardrail/`
- `/api/v1/chat/score/`
- `/api/v1/images/generations/`
- `/api/v1/images/score/url/`
- `/api/v1/decide-route/`
- `/api/v1/generate-speech/`

## 시나리오

1. 사용자가 텍스트 질문을 할 경우
   - `/chat/guardrail` 로 질문이 적절한지 판단: 적절하지 못하면 답변 중지
   - 적절하다면 `/decide-route` 로 `/chat/completions` 와 `/images/generations` 중 어디로 갈지 판단
     - `/chat/completions`: 답변 출력 후 `/chat/score` 로 점수·이유 출력
     - `/images/generations`: 이미지 출력 후 `/images/score/url` 로 점수·이유 출력
2. 채팅 화면에서 파일 드래그 시: json / png, jpeg 지원. json은 문자열로, 이미지는 base64로 붙여 1번과 동일하게 진행.
3. TTS 화면: `/generate-speech` 로 텍스트 전송 후 base64 mp3 `audio_data` 수신.

테스트용 curl 예제는 프로젝트 루트 `2_openai_proxy/README.md` 를 참고하세요.
