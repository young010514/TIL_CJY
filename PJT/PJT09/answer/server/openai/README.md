# FastAPI 모델 서버 (3단 — LLM/이미지/TTS 제공)

3단 구조에서 **마지막 단**입니다. Django 중간 서버(8080)가 HTTP로 이 서버(8081)를 호출합니다. 브라우저는 직접 호출하지 않으므로 **CORS 설정 없음**.

## 실행

- 가상환경 생성 후, `server/` 에서: `pip install -r requirements.txt`
- 실행: `server/openai` 로 이동 후 `uvicorn app.main:app --host 0.0.0.0 --port 8081 --reload`

(로컬에서는 HTTP로 `http://localhost:8081` 에서 동작합니다.)

## `.env`

```
MODE="GMS"
GMS_KEY="MY_GMS_KEY"
GMS_URL="https://gms.ssafy.io/gmsapi/api.openai.com/v1"
```

이 폴더(`server/openai/`)는 **정답** 구현입니다. 교육생은 `server/skeleton/proxy/` 의 Django 쪽 로직을 구현하면 됩니다.
