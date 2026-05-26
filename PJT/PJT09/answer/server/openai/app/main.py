from fastapi import FastAPI
from .routers import openai

app = FastAPI()

app.include_router(
    openai.router,
    prefix="/api/v1/openai",
    tags=["openai"],
)

# 브라우저는 Django(8080)만 호출하고, Django가 이 서버(8081)로 HTTP 요청하므로 CORS 불필요.
