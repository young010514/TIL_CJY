import json
import os
from pathlib import Path

import httpx
from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

BASE_DIR = Path(__file__).resolve().parent
ROOT_DIR = BASE_DIR.parent.parent
load_dotenv(ROOT_DIR / ".env")
load_dotenv(BASE_DIR / ".env")

GMS_API = os.getenv("GMS_API") or os.getenv("GMS_KEY")
GMS_URL = "https://gms.ssafy.io/gmsapi/api.openai.com/v1"
MODEL_NAME = "gpt-5-nano"

headers = {
    "Authorization": f"Bearer {GMS_API}",
    "Content-Type": "application/json",
    "Accept": "application/json",
}

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class ChatRequest(BaseModel):
    messages: list[dict]


class ChatResponse(BaseModel):
    content: str


class GuardrailRequest(BaseModel):
    prompt: str


class GuardrailResponse(BaseModel):
    is_appropriate: bool


def post_chat_completions(payload_data):
    if not GMS_API:
        raise HTTPException(status_code=500, detail="GMS_API is not configured")

    try:
        response = httpx.post(
            f"{GMS_URL}/chat/completions",
            headers=headers,
            json=payload_data,
            timeout=60,
        )
        response.raise_for_status()
        return response.json()
    except httpx.HTTPError as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/api/v1/chat/guardrail", response_model=GuardrailResponse)
def get_guardrail_response(guardrail_request: GuardrailRequest):
    messages = [
        {
            "role": "developer",
            "content": (
                "You are a guardrail classifier. Decide whether the user's prompt "
                "is appropriate. Return true only for safe, legal, and non-harmful "
                "requests."
            ),
        },
        {"role": "user", "content": f"prompt: {guardrail_request.prompt}"},
    ]

    response_format = {
        "type": "json_schema",
        "json_schema": {
            "name": "guardrail_response",
            "strict": True,
            "schema": {
                "type": "object",
                "properties": {
                    "is_appropriate": {
                        "type": "boolean",
                        "description": "Whether the prompt is appropriate.",
                    }
                },
                "required": ["is_appropriate"],
                "additionalProperties": False,
            },
        },
    }

    payload_data = {
        "model": MODEL_NAME,
        "messages": messages,
        "response_format": response_format,
    }
    result = post_chat_completions(payload_data)
    content = result["choices"][0]["message"]["content"]
    return json.loads(content)


@app.post("/api/v1/chat/completions", response_model=ChatResponse)
def get_chat_response(chat_request: ChatRequest):
    payload_data = {
        "model": MODEL_NAME,
        "messages": chat_request.messages,
    }
    result = post_chat_completions(payload_data)
    content = result["choices"][0]["message"]["content"]
    return {"content": content}
