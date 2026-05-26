from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from proxies.serializers import (
    ChatGuardrailRequestSerializer,
    ChatGuardrailResponseSerializer,
    ChatRequestSerializer,
    ChatResponseSerializer,
    ChatScoreRequestSerializer,
    ChatScoreResponseSerializer,
    ImageGenerationRequestSerializer,
    ImageGenerationResponseSerializer,
    ImageScoreRequestForImageURLSerializer,
    ImageScoreResponseForImageURLSerializer,
)
from proxies.services import (
    get_chat_guardrail_response,
    get_chat_response,
    get_chat_score_response,
    get_image_generation_response,
    get_image_score_response_for_url,
)


def chatbot_page(request):
    return render(request, "proxies/chatbot.html")


def get_last_user_prompt(messages):
    for message in reversed(messages):
        if message.get("role") == "user":
            content = message.get("content")
            return content if isinstance(content, str) else str(content)
    return ""


@api_view(["POST"])
def chat_response(request):
    serializer = ChatRequestSerializer(data=request.data)

    if not serializer.is_valid():
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    prompt = get_last_user_prompt(serializer.validated_data["messages"])
    guardrail_result = get_chat_guardrail_response({"prompt": prompt})

    if guardrail_result is None:
        return Response(
            {"detail": "Guardrail check failed"},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR,
        )

    if not guardrail_result["is_appropriate"]:
        return Response(
            {
                "detail": "Inappropriate request blocked by guardrail",
                "is_appropriate": False,
            },
            status=status.HTTP_403_FORBIDDEN,
        )

    result = get_chat_response(serializer.validated_data)

    if result is None:
        return Response(
            {"detail": "Chat response failed"},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR,
        )

    return Response(ChatResponseSerializer(result).data, status=status.HTTP_201_CREATED)


@api_view(["POST"])
def chat_guardrail_response(request):
    serializer = ChatGuardrailRequestSerializer(data=request.data)

    if not serializer.is_valid():
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    result = get_chat_guardrail_response(serializer.validated_data)

    if result is None:
        return Response(
            {"detail": "Chat guardrail response failed"},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR,
        )

    response_data = ChatGuardrailResponseSerializer(result).data
    if result["is_appropriate"]:
        return Response(response_data, status=status.HTTP_201_CREATED)

    return Response(response_data, status=status.HTTP_403_FORBIDDEN)


@api_view(["POST"])
def chat_score_response(request):
    serializer = ChatScoreRequestSerializer(data=request.data)

    if not serializer.is_valid():
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    result = get_chat_score_response(serializer.validated_data)

    if result is None:
        return Response(
            {"detail": "Chat score response failed"},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR,
        )

    return Response(ChatScoreResponseSerializer(result).data, status=status.HTTP_201_CREATED)


@api_view(["POST"])
def image_generation_response(request):
    serializer = ImageGenerationRequestSerializer(data=request.data)

    if not serializer.is_valid():
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    guardrail_result = get_chat_guardrail_response(serializer.validated_data)

    if guardrail_result is None:
        return Response(
            {"detail": "Guardrail check failed"},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR,
        )

    if not guardrail_result["is_appropriate"]:
        return Response(
            {
                "detail": "Inappropriate request blocked by guardrail",
                "is_appropriate": False,
            },
            status=status.HTTP_403_FORBIDDEN,
        )

    result = get_image_generation_response(serializer.validated_data)

    if result is None:
        return Response(
            {"detail": "Image generation response failed"},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR,
        )

    return Response(ImageGenerationResponseSerializer(result).data, status=status.HTTP_201_CREATED)


@api_view(["POST"])
def image_score_response_for_url(request):
    serializer = ImageScoreRequestForImageURLSerializer(data=request.data)

    if not serializer.is_valid():
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    result = get_image_score_response_for_url(serializer.validated_data)

    if result is None:
        return Response(
            {"detail": "Image score response failed"},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR,
        )

    return Response(
        ImageScoreResponseForImageURLSerializer(result).data,
        status=status.HTTP_201_CREATED,
    )


@api_view(["POST"])
def decide_route_response(request):
    return Response({"detail": "Not implemented"}, status=status.HTTP_501_NOT_IMPLEMENTED)


@api_view(["POST"])
def tts_response(request):
    return Response({"detail": "Not implemented"}, status=status.HTTP_501_NOT_IMPLEMENTED)
