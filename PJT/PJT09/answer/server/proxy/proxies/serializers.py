from rest_framework import serializers

# ======================= 부모 ==========================


class MessageSerializer(serializers.Serializer):
    """채팅 메시지 정보를 담는 Serializer"""

    role = serializers.CharField()
    content = serializers.JSONField()


class PromptRequestSerializer(serializers.Serializer):
    """텍스트 프롬프트 요청을 위한 기본 Serializer"""

    prompt = serializers.CharField()


class ScoreResponseSerializer(serializers.Serializer):
    """점수 기반 응답을 위한 공통 Serializer"""

    score = serializers.IntegerField()
    reason = serializers.CharField()


# ==================================================


class ChatRequestSerializer(serializers.Serializer):
    """채팅 히스토리를 포함한 대화 요청 Serializer"""

    messages = MessageSerializer(many=True)


class ChatResponseSerializer(serializers.Serializer):
    """채팅 요청에 대한 응답 Serializer"""

    content = serializers.CharField()


class ChatGuardrailRequestSerializer(PromptRequestSerializer):
    """채팅 가드레일 검사를 위한 요청 Serializer"""

    pass


class ChatGuardrailResponseSerializer(serializers.Serializer):
    """채팅 내용의 적절성 여부를 반환하는 응답 Serializer"""

    is_appropriate = serializers.BooleanField()


class ChatScoreRequestSerializer(serializers.Serializer):
    """채팅 응답의 품질 점수를 요청하는 Serializer"""

    messages = MessageSerializer(many=True)
    answer = serializers.CharField()


class ChatScoreResponseSerializer(ScoreResponseSerializer):
    """채팅 품질 평가 결과 점수 응답 Serializer"""

    pass


class ImageGenerationRequestSerializer(PromptRequestSerializer):
    """이미지 생성을 위한 요청 Serializer"""

    pass


class ImageGenerationResponseSerializer(serializers.Serializer):
    """생성된 이미지 정보를 담는 응답 Serializer"""

    url = serializers.CharField()


class ImageScoreRequestForImageURLSerializer(serializers.Serializer):
    """이미지 URL을 이용한 점수 평가 요청 Serializer"""

    question = serializers.CharField()
    image_url = serializers.CharField()


class ImageScoreResponseForImageURLSerializer(ScoreResponseSerializer):
    """이미지 URL 분석에 대한 점수 응답 Serializer"""

    pass


class DecideRouteRequestSerializer(PromptRequestSerializer):
    """라우팅 경로 결정을 위한 요청 Serializer"""

    pass


class DecideRouteResponseSerializer(serializers.Serializer):
    """결정된 라우팅 경로 정보를 담는 응답 Serializer"""

    route = serializers.CharField()


class GenerateSpeechRequestSerializer(serializers.Serializer):
    """TTS 요청 Serializer"""

    text = serializers.CharField()


class GenerateSpeechResponseSerializer(serializers.Serializer):
    """TTS 응답 Serializer"""

    audio_data = serializers.CharField()
