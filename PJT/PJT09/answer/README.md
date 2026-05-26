# OpenAI 연동 — 3단 구조 프로젝트

## 3단 구조 (프론트 → Django → FastAPI)

```
[프론트엔드]  ──HTTP──►  [Django 중간 서버 :8080]  ──HTTP──►  [FastAPI 모델 서버 :8081]
  (브라우저)              (CORS 처리, 로직)                    (LLM/이미지/TTS)
```

- **1단: 프론트** — 사용자 입력을 받아 `http://localhost:8080` 으로만 요청합니다.
- **2단: Django (중간 서버)** — 8080에서 요청을 받고, CORS를 처리한 뒤 비즈니스 로직(가드레일·라우팅 등)을 수행하고, 필요 시 3단으로 전달합니다.
- **3단: FastAPI** — 8081에서 실제 LLM/이미지/TTS API를 제공합니다. 브라우저는 직접 호출하지 않고, Django만 호출합니다.


---
## 실행 순서 (HTTP 기준, 로컬)

**의존성**: `server/` 폴더에서 `pip install -r requirements.txt` 한 번 실행.

1. **FastAPI (모델 서버)**  
   `server/openai` 에서:  
   `uvicorn app.main:app --host 0.0.0.0 --port 8081 --reload`
2. **Django (중간 서버)**  
   교육생 작업 시: `server/skeleton/proxy` 에서 `python manage.py runserver 0.0.0.0:8080`  
   정답 실행 시: `server/proxy` 에서 동일 명령.
3. **프론트**  
   `client/` 의 `index.html` 을 브라우저에서 열거나, 로컬 웹 서버로 제공.

프론트는 **항상 Django(8080)** 만 호출하고, Django가 **FastAPI(8081)** 로 HTTP로 요청합니다.

---

## API 테스트 (curl — 복붙용)

아래는 **Django 중간 서버(8080)** 로 보내는 예제입니다. 서버 실행 후 그대로 복사해 터미널에서 실행하면 됩니다.

**Base URL**: `http://localhost:8080/api/v1`

### 채팅 완성

```bash
curl -X POST http://localhost:8080/api/v1/chat/completions/ -H "Content-Type: application/json" -d "{\"messages\":[{\"role\":\"user\",\"content\":\"안녕하세요\"}]}"
```

### 채팅 가드레일 (적절성 판단)

```bash
curl -X POST http://localhost:8080/api/v1/chat/guardrail/ -H "Content-Type: application/json" -d "{\"prompt\":\"안녕하세요\"}"
```

### 채팅 점수

```bash
curl -X POST http://localhost:8080/api/v1/chat/score/ -H "Content-Type: application/json" -d "{\"messages\":[{\"role\":\"user\",\"content\":\"안녕\"},{\"role\":\"assistant\",\"content\":\"안녕하세요\"}],\"answer\":\"안녕하세요\"}"
```

### 라우트 결정

```bash
curl -X POST http://localhost:8080/api/v1/decide-route/ -H "Content-Type: application/json" -d "{\"prompt\":\"고양이 그려줘\"}"
```

### 이미지 생성

```bash
curl -X POST http://localhost:8080/api/v1/images/generations/ -H "Content-Type: application/json" -d "{\"prompt\":\"귀여운 고양이\"}"
```

### 이미지 점수 (URL)

```bash
curl -X POST http://localhost:8080/api/v1/images/score/url/ -H "Content-Type: application/json" -d "{\"question\":\"귀여운 고양이\",\"image_url\":\"https://example.com/cat.png\"}"
```

### TTS (음성 생성)

```bash
curl -X POST http://localhost:8080/api/v1/generate-speech/ -H "Content-Type: application/json" -d "{\"text\":\"안녕하세요\"}"
```

---

## 디렉터리 역할

| 경로 | 역할 |
|------|------|
| `client/` | 프론트. Django(8080)로만 요청. |
| `server/skeleton/` | **교육생 작업용 스켈레톤.** `skeleton/proxy` 에서 뷰·서비스 로직을 채워 구현. |
| `server/proxy/` | **Django 중간 서버 정답.** 전체 뷰·서비스 구현본. |
| `server/openai/` | **FastAPI 모델 서버 정답.** LLM/이미지/TTS API 전체 구현. |

- **교육 진행**: 교육생은 `server/skeleton/proxy/` 를 작업 폴더로 사용하고, `proxies/views.py`, `proxies/services.py` 를 채우면 됩니다. 정답은 `server/proxy/`, `server/openai/` 에 있습니다.
- **CORS**: 브라우저가 8080으로 요청하므로 **Django만** CORS를 설정합니다.
- **구현 초점**: Django 쪽에서 "어떤 JSON을 어떤 URL로 보낼지" 같은 HTTP·로직에 집중하면 됩니다.
