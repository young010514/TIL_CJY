from typing import Any
from pydantic import BaseModel, Field

# ======================= 부모 ==========================


class Message(BaseModel):
    """
    채팅 메시지 정보를 담는 모델입니다.

    Attributes:
        role (str): 메시지 발신자의 역할 (예: 'user', 'assistant')
        content (str|list[dict[str, Any]]): 메시지 내용
    """

    role: str
    content: str | list[dict[str, Any]]


class PromptRequest(BaseModel):
    """
    텍스트 프롬프트 요청을 위한 기본 모델입니다.

    Attributes:
        prompt (str): 모델에 전달할 프롬프트 문자열
    """

    prompt: str


class ScoreResponse(BaseModel):
    """
    점수 기반 응답을 위한 공통 모델입니다.

    Attributes:
        score (int): 계산된 점수 결과
        reason (str): 해당 점수가 나온 간단한 이유
    """

    score: int
    reason: str


# ==================================================


class ChatRequest(BaseModel):
    """
    채팅 히스토리를 포함한 대화 요청 모델입니다.

    Attributes:
        messages (list[Message]): 대화 흐름을 구성하는 메세지 객체 리스트
    """

    messages: list[Message]


class ChatResponse(BaseModel):
    """
    채팅 요청에 대한 응답 모델입니다.

    Attributes:
        content (str): 생성된 채팅 응답 내용
    """

    content: str


class ChatGuardrailRequest(PromptRequest):
    """
    채팅 가드레일 검사를 위한 요청 모델입니다.

    Attributes:
        prompt (str): 검사 대상이 되는 입력 프롬프트 # 상속: PromptRequest
    """

    pass


class ChatGuardrailResponse(BaseModel):
    """
    채팅 내용의 적절성 여부를 반환하는 응답 모델입니다.

    Attributes:
        is_appropriate (bool): 콘텐츠의 적절성 여부 (True: 적절함, False: 부적절함)
    """

    is_appropriate: bool


class ChatScoreRequest(BaseModel):
    """
    채팅 응답의 품질 점수를 요청하는 모델입니다.

    Attributes:
        messages (list[Message]): 대화 흐름을 구성하는 메세지 객체 리스트
        answer (str): 모델이 생성한 답변
    """

    messages: list[Message]
    answer: str


class ChatScoreResponse(ScoreResponse):
    """
    채팅 품질 평가 결과 점수 응답 모델입니다.

    Attributes:
        score (int): 답변의 품질 점수 # 상속: ScoreResponse
        reason (str): 해당 점수를 반영한 간단한 이유 # 상속: ScoreResponse
    """

    pass


class ImageGenerationRequest(PromptRequest):
    """
    이미지 생성을 위한 요청 모델입니다.

    Attributes:
        prompt (str): 생성할 이미지에 대한 묘사 # 상속: PromptRequest
    """

    pass


class ImageGenerationResponse(BaseModel):
    """
    생성된 이미지 정보를 담는 응답 모델입니다.

    Attributes:
        url (str): 생성된 이미지의 접근 URL
    """

    url: str


class ImageScoreRequestForImageURL(BaseModel):
    """
    이미지 URL을 이용한 점수 평가 요청 모델입니다.

    Attributes:
        question (str): 이미지와 함께 전달할 질문 또는 평가 기준
        image_url (str): 분석할 이미지의 URL 주소
    """

    question: str
    image_url: str


class ImageScoreResponseForImageURL(ScoreResponse):
    """
    이미지 URL 분석에 대한 점수 응답 모델입니다.

    Attributes:
        score (int): 이미지 분석 결과 점수 # 상속: ScoreResponse
        reason (str): 해당 점수를 반영한 간단한 이유 # 상속: ScoreResponse
    """

    pass


class DecideRouteRequest(PromptRequest):
    """
    라우팅 경로 결정을 위한 요청 모델입니다.

    Attributes:
        prompt (str): 경로 결정을 위한 입력 텍스트 # 상속: PromptRequest
    """

    pass


class DecideRouteResponse(BaseModel):
    """
    결정된 라우팅 경로 정보를 담는 응답 모델입니다.

    Attributes:
        route (str): 결정된 대상 경로 이름
    """

    route: str
    

class GenerateSpeechRequest(BaseModel):
    """
    TTS 요청 모델입니다.
    
    Attributes:
        text (str) : 음성 변환 대상 문자열
    """
    text: str 


class GenerateSpeechResponse(BaseModel):
    """
    TTS 응답 모델입니다.
    
    Attributes:
        audio_data (str) : base64 음성 파일
    """
    
    audio_data: str

# ===================
# OPENAI response_format


# ======================= 부모 ==========================
class ScoreResponseFormat(BaseModel):
    """
    점수 기반 응답 결과의 공통 응답 포맷을 정의하는 모델입니다.

    Attributes:
        score (int): 답변의 점수
        reason (str): 해당 점수를 받은 이유
    """

    score: int = Field(
        description="다른 딕셔너리로 감싸지 않은, 직접적인 정수(int) 값이어야 합니다."
    )
    reason: str = Field(
        description="다른 딕셔너리로 감싸지 않은, 직접적인 문자열(str) 값이어야 합니다."
    )


# =======================================================


class ChatGuardrailResponseFormat(BaseModel):
    """
    채팅 가드레일 검사 결과의 응답 포맷을 정의하는 모델입니다.

    Attributes:
        is_appropriate (bool): 사용자의 질문이 적절하다면 True, 아니라면 False
    """

    is_appropriate: bool = Field(
        description="다른 딕셔너리로 감싸지 않은, 직접적인 불리언(bool) 값이어야 합니다."
    )


class ChatScoreResponseFormat(ScoreResponseFormat):
    """
    채팅 품질 평가 결과의 응답 포맷을 정의하는 모델입니다.

    Attributes:
        score (int): 답변의 점수 # 상속: ScoreResponseFormat
        reason (str): 해당 점수를 받은 이유 # 상속: ScoreResponseFormat
    """

    pass


class ImageScoreResponseFormatForImageURL(ScoreResponseFormat):
    """
    이미지 URL 분석 점수 결과의 응답 포맷을 정의하는 모델입니다.

    Attributes:
        score (int): 답변의 점수 # 상속: ScoreResponseFormat
        reason (str): 해당 점수를 받은 이유 # 상속: ScoreResponseFormat
    """

    pass


class ImageScoreResponseFormatForBase64Image(ScoreResponseFormat):
    """
    base64 이미지 분석 점수 결과의 응답 포맷을 정의하는 모델입니다.

    Attributes:
        score (int): 답변의 점수 # 상속: ScoreResponseFormat
        reason (str): 해당 점수를 받은 이유 # 상속: ScoreResponseFormat
    """

    pass


class JsonGenerationsResponseFormat(BaseModel):
    """
    JSON 데이터 생성 결과의 응답 포맷을 정의하는 모델입니다.

    Attributes:
        data (list[dict]): 증강된 데이터 리스트
    """

    data: list[dict] = Field(
        description="다른 딕셔너리로 감싸지 않은, 객체들의 직접적인 리스트 형태여야 합니다."
    )


class DecideRouteResponseFormat(BaseModel):
    """
    라우팅 경로 결정 결과의 응답 포맷을 정의하는 모델입니다.

    Attributes:
        route (str): 질문에 대한 적절한 API 경로
    """

    route: str = Field(
        description="""
            반드시 두 개 문자열 중 하나를 리턴한다.
            '/images/generations' 또는 '/chat/completions'
        """
    )
