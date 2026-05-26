import requests
from django.conf import settings

MODEL_SERVER_URL = settings.MODEL_SERVER_URL


def get_chat_response(chat_request):
    """채팅 요청을 FastAPI 모델 서버(8081)에 HTTP로 전달하고 응답을 반환합니다."""
    messages = chat_request["messages"]
    payload_data = {"messages": messages}
    try:
        response = requests.post(
            f"{MODEL_SERVER_URL}/chat/completions", json=payload_data
        )
        response.raise_for_status()
        content = response.json()["content"]
        return {"content": content}
    except Exception as e:
        print(f"[서비스 에러 발생] {e}")
        return None


def get_chat_guardrail_response(guardrail_request):
    """prompt를 모델 서버 /chat/guardrail로 보내고 is_appropriate를 반환합니다."""
    payload_data = {"prompt": guardrail_request["prompt"]}
    try:
        response = requests.post(
            f"{MODEL_SERVER_URL}/chat/guardrail", json=payload_data
        )
        response.raise_for_status()
        return {"is_appropriate": response.json()["is_appropriate"]}
    except Exception as e:
        print(f"[서비스 에러 발생] {e}")
        return None


def get_chat_score_response(score_request):
    """messages, answer를 모델 서버 /chat/score로 보내고 score, reason을 반환합니다."""
    payload_data = {
        "messages": score_request["messages"],
        "answer": score_request["answer"],
    }
    try:
        response = requests.post(
            f"{MODEL_SERVER_URL}/chat/score", json=payload_data
        )
        response.raise_for_status()
        data = response.json()
        return {"score": data["score"], "reason": data["reason"]}
    except Exception as e:
        print(f"[서비스 에러 발생] {e}")
        return None


def get_image_generation_response(gen_request):
    """prompt를 모델 서버 /images/generations로 보내고 url을 반환합니다."""
    payload_data = {"prompt": gen_request["prompt"]}
    try:
        response = requests.post(
            f"{MODEL_SERVER_URL}/images/generations", json=payload_data
        )
        response.raise_for_status()
        return {"url": response.json()["url"]}
    except Exception as e:
        print(f"[서비스 에러 발생] {e}")
        return None


def get_image_score_response_for_url(score_request):
    """question, image_url을 모델 서버 /images/score/url로 보내고 score, reason을 반환합니다."""
    payload_data = {
        "question": score_request["question"],
        "image_url": score_request["image_url"],
    }
    try:
        response = requests.post(
            f"{MODEL_SERVER_URL}/images/score/url", json=payload_data
        )
        response.raise_for_status()
        data = response.json()
        return {"score": data["score"], "reason": data["reason"]}
    except Exception as e:
        print(f"[서비스 에러 발생] {e}")
        return None


def get_decide_route_response(route_request):
    """prompt를 모델 서버 /decide-route로 보내고 route를 반환합니다."""
    payload_data = {"prompt": route_request["prompt"]}
    try:
        response = requests.post(
            f"{MODEL_SERVER_URL}/decide-route", json=payload_data
        )
        response.raise_for_status()
        return {"route": response.json()["route"]}
    except Exception as e:
        print(f"[서비스 에러 발생] {e}")
        return None


def get_tts_response(tts_request):
    """text를 모델 서버 /generate-speech로 보내고 audio_data를 반환합니다."""
    payload_data = {"text": tts_request["text"]}
    try:
        response = requests.post(
            f"{MODEL_SERVER_URL}/generate-speech", json=payload_data
        )
        response.raise_for_status()
        return {"audio_data": response.json()["audio_data"]}
    except Exception as e:
        print(f"[서비스 에러 발생] {e}")
        return None
