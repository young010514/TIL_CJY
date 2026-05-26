from fastapi import APIRouter, HTTPException, Response, status
from ..services.openai import (
    get_chat_response,
    get_image_generation_response,
    get_decide_route_response,
    get_image_score_response_for_image_url,
    get_chat_guardrail_response,
    get_chat_score_response,
    get_generate_speech_response,
)
from ..schemas.openai import (
    ChatRequest,
    ChatResponse,
    ChatGuardrailRequest,
    ChatGuardrailResponse,
    ImageGenerationRequest,
    ImageGenerationResponse,
    DecideRouteRequest,
    DecideRouteResponse,
    ImageScoreRequestForImageURL,
    ImageScoreResponseForImageURL,
    ChatScoreRequest,
    ChatScoreResponse,
    GenerateSpeechRequest,
    GenerateSpeechResponse,
)


router = APIRouter()


@router.post(
    "/chat/completions",
    response_model=ChatResponse,
    status_code=status.HTTP_201_CREATED,
)
def chat_response(chat_request: ChatRequest) -> ChatResponse:
    result = get_chat_response(chat_request)

    if result is None:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Chat response failed",
        )

    return result


@router.post(
    "/chat/guardrail",
    response_model=ChatGuardrailResponse,
    status_code=status.HTTP_201_CREATED,
)
def chat_guardrail_response(
    chat_guardrail_request: ChatGuardrailRequest, response: Response
) -> ChatGuardrailResponse:
    result = get_chat_guardrail_response(chat_guardrail_request)

    if result is None:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Chat Guardrail Failed",
        )

    if result["is_appropriate"]:
        response.status_code = status.HTTP_201_CREATED
    else:
        # 정책 위반(부적절한 콘텐츠)으로 판단될 경우 403 Forbidden 사용
        response.status_code = status.HTTP_403_FORBIDDEN

    return result


@router.post(
    "/chat/score", response_model=ChatScoreResponse, status_code=status.HTTP_201_CREATED
)
def chat_score_response(chat_score_request: ChatScoreRequest) -> ChatScoreResponse:
    result = get_chat_score_response(chat_score_request)

    if result is None:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Chat score request failed",
        )

    return result


@router.post(
    "/images/generations",
    response_model=ImageGenerationResponse,
    status_code=status.HTTP_201_CREATED,
)
def image_generation_response(
    image_generation_request: ImageGenerationRequest,
) -> ImageGenerationResponse:
    result = get_image_generation_response(image_generation_request)

    if result is None:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Image generation failed",
        )

    return result


@router.post(
    "/images/score/url",
    response_model=ImageScoreResponseForImageURL,
    status_code=status.HTTP_201_CREATED,
)
def image_score_resposne_for_url(
    image_score_request_for_image_url: ImageScoreRequestForImageURL,
) -> ImageScoreResponseForImageURL:
    result = get_image_score_response_for_image_url(image_score_request_for_image_url)

    if result is None:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Image score request failed",
        )

    return result


@router.post(
    "/decide-route",
    response_model=DecideRouteResponse,
    status_code=status.HTTP_201_CREATED,
)
def decide_route_response(
    decide_route_request: DecideRouteRequest,
) -> DecideRouteResponse:
    result = get_decide_route_response(decide_route_request)

    if result is None:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Route decision failed",
        )

    return result


@router.post(
    "/generate-speech",
    response_model=GenerateSpeechResponse,
    status_code=status.HTTP_201_CREATED,
)
def tts_response(
    generate_speech_request: GenerateSpeechRequest,
) -> GenerateSpeechResponse:
    result = get_generate_speech_response(generate_speech_request)
    
    if result is None:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="speech generation failed",
        )

    return result