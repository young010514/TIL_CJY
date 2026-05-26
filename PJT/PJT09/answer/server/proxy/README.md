# Django 중간 서버 (2단 — 프론트와 FastAPI 사이)

3단 구조: **프론트 → 이 서버(8080) → FastAPI(8081)**.  
브라우저는 이 서버만 호출하고, 이 서버가 FastAPI로 HTTP 요청을 보냅니다. **CORS는 이 Django 서버에만 설정**합니다.

## `.env` 세팅

```
MODEL_SERVER_URL="http://localhost:8081/api/v1/openai"
```

(로컬은 HTTP로 통신합니다.)

## 의존성 설치

`server/` 폴더에서 한 번만 설치하면 Django·FastAPI 모두 사용할 수 있습니다.

```bash
cd server
pip install -r requirements.txt
```

## 서버 실행

```bash
python manage.py runserver 0.0.0.0:8080
```

## API 테스트 (curl 복붙)

프로젝트 루트 `2_openai_proxy/README.md` 의 **「API 테스트 (curl)」** 섹션을 참고하세요.

예: 채팅 완성 한 번 호출

```bash
curl -X POST http://localhost:8080/api/v1/chat/completions/ -H "Content-Type: application/json" -d "{\"messages\":[{\"role\":\"user\",\"content\":\"안녕\"}]}"
```

## 정답 구현

이 폴더(`server/proxy/`)는 **정답**입니다. 교육생 작업용 스켈레톤은 `server/skeleton/proxy/` 에 있습니다.
