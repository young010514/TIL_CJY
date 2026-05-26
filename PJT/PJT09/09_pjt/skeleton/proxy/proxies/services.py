import json

import requests
from django.conf import settings

REQUEST_TIMEOUT = 60
GMS_URL = settings.GMS_URL
MODEL_NAME = settings.MODEL_NAME
IMAGE_MODEL_NAME = settings.IMAGE_MODEL_NAME


def get_gms_headers():
    if not settings.GMS_API:
        raise ValueError("GMS_API is not configured")

    return {
        "Authorization": f"Bearer {settings.GMS_API}",
        "Content-Type": "application/json",
        "Accept": "application/json",
    }


def post_gms_chat_completions(payload_data):
    response = requests.post(
        f"{GMS_URL}/chat/completions",
        headers=get_gms_headers(),
        json=payload_data,
        timeout=REQUEST_TIMEOUT,
    )
    if not response.ok:
        print(f"[gms error] status={response.status_code}, body={response.text[:1000]}")
        response.raise_for_status()
    return response.json()


def post_gms_image_generation(payload_data):
    response = requests.post(
        f"{GMS_URL}/images/generations",
        headers=get_gms_headers(),
        json=payload_data,
        timeout=REQUEST_TIMEOUT,
    )
    response.raise_for_status()
    return response.json()


def score_response_format(name):
    return {
        "type": "json_schema",
        "json_schema": {
            "name": name,
            "strict": True,
            "schema": {
                "type": "object",
                "properties": {
                    "score": {"type": "integer"},
                    "reason": {"type": "string"},
                },
                "required": ["score", "reason"],
                "additionalProperties": False,
            },
        },
    }


def get_chat_response(chat_request):
    payload_data = {
        "model": MODEL_NAME,
        "messages": chat_request["messages"],
    }
    try:
        data = post_gms_chat_completions(payload_data)
        content = data["choices"][0]["message"]["content"]
        return {"content": content}
    except Exception as e:
        print(f"[service error] {e}")
        return None


def get_chat_guardrail_response(guardrail_request):
    messages = [
        {
            "role": "developer",
            "content": (
                "You are a guardrail classifier. Decide whether the user's prompt "
                "is appropriate. Return true only for safe, legal, and non-harmful "
                "requests."
            ),
        },
        {"role": "user", "content": f"prompt: {guardrail_request['prompt']}"},
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
    try:
        response_data = post_gms_chat_completions(payload_data)
        content = response_data["choices"][0]["message"]["content"]
        data = json.loads(content)
        if isinstance(data.get("is_appropriate"), bool):
            return {"is_appropriate": data["is_appropriate"]}
        return None
    except Exception as e:
        print(f"[service error] {e}")
        return None


def get_chat_score_response(score_request):
    messages = [
        {
            "role": "developer",
            "content": (
                "You score whether an assistant answer fits the user's question. "
                "Return a score from 0 to 100 and a short Korean reason."
            ),
        },
        {
            "role": "user",
            "content": json.dumps(
                {
                    "question_messages": score_request["messages"],
                    "answer": score_request["answer"],
                },
                ensure_ascii=False,
            ),
        },
    ]
    payload_data = {
        "model": MODEL_NAME,
        "messages": messages,
        "response_format": score_response_format("chat_score_response"),
    }
    try:
        response_data = post_gms_chat_completions(payload_data)
        content = response_data["choices"][0]["message"]["content"]
        result = json.loads(content)
        return {"score": int(result["score"]), "reason": result["reason"]}
    except Exception as e:
        print(f"[service error] {e}")
        return None


def get_image_generation_response(gen_request):
    payload_data = {
        "model": IMAGE_MODEL_NAME,
        "prompt": gen_request["prompt"],
        "size": "1024x1024",
    }
    try:
        response_data = post_gms_image_generation(payload_data)
        image_data = response_data["data"][0]

        if image_data.get("url"):
            return {"url": image_data["url"]}

        if image_data.get("b64_json"):
            return {"url": f"data:image/png;base64,{image_data['b64_json']}"}

        return None
    except Exception as e:
        print(f"[service error] {e}")
        return None


def get_image_score_response_for_url(score_request):
    result = get_image_score_response_with_vision(score_request)
    if result is not None:
        return result

    return get_image_score_response_from_prompt(score_request)


def get_image_score_response_with_vision(score_request):
    messages = [
        {
            "role": "developer",
            "content": (
                "You score whether the generated image fits the user's request. "
                "Return a score from 0 to 100 and a short Korean reason."
            ),
        },
        {
            "role": "user",
            "content": [
                {"type": "text", "text": f"question: {score_request['question']}"},
                {
                    "type": "image_url",
                    "image_url": {"url": score_request["image_url"]},
                },
            ],
        },
    ]
    payload_data = {
        "model": MODEL_NAME,
        "messages": messages,
        "response_format": score_response_format("image_score_response"),
    }
    try:
        response_data = post_gms_chat_completions(payload_data)
        content = response_data["choices"][0]["message"]["content"]
        result = json.loads(content)
        return {"score": int(result["score"]), "reason": result["reason"]}
    except Exception as e:
        print(f"[service error] {e}")
        return None


def get_image_score_response_from_prompt(score_request):
    messages = [
        {
            "role": "developer",
            "content": (
                "You score whether an image generation result is likely to fit the "
                "user's image request. The actual image could not be inspected, so "
                "judge based on the original request and the fact that the image was "
                "generated from that prompt. Return a score from 0 to 100 and a short "
                "Korean reason."
            ),
        },
        {
            "role": "user",
            "content": f"image generation request: {score_request['question']}",
        },
    ]
    payload_data = {
        "model": MODEL_NAME,
        "messages": messages,
        "response_format": score_response_format("image_score_fallback_response"),
    }
    try:
        response_data = post_gms_chat_completions(payload_data)
        content = response_data["choices"][0]["message"]["content"]
        result = json.loads(content)
        return {"score": int(result["score"]), "reason": result["reason"]}
    except Exception as e:
        print(f"[service error] {e}")
        return None


def get_decide_route_response(route_request):
    return None


def get_tts_response(tts_request):
    return None
