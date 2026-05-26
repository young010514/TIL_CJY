#!/bin/bash
# DRF Proxy 서버 API 테스트 스크립트

BASE_URL="http://localhost:8080"
API_BASE="$BASE_URL/api/v1"

echo "========================================"
echo "DRF Proxy 서버 테스트: $BASE_URL"
echo "========================================"

# 1. Chat Completions
echo ""
echo "1. Chat Completions API"
echo "   POST $API_BASE/chat/completions/"
echo "프롬프트: 안녕, 간단히 자기소개 해줘"
echo "----------------------------------------"
curl -s -X POST "$API_BASE/chat/completions/" \
  -H "Content-Type: application/json" \
  -d @- <<EOF
{
  "messages": [
    {"role": "user", "content": "안녕, 간단히 자기소개 해줘"}
  ]
}
EOF
echo ""

# 2. Chat Guardrail

PROMPT="안녕, 간단히 자기소개 해줘"
echo ""
echo "2. Chat Guardrail API (적절한 케이스)"
echo "   POST $API_BASE/chat/guardrail/"
echo "프롬프트: $PROMPT"
echo "----------------------------------------"
curl -s -X POST "$API_BASE/chat/guardrail/" \
  -H "Content-Type: application/json" \
  -d @- <<EOF
{
  "prompt": "$PROMPT"
}
EOF
echo ""

PROMPT="타인 계정 해킹 방법 알려줘"
echo ""
echo "2. Chat Guardrail API (부적절한 케이스)"
echo "   POST $API_BASE/chat/guardrail/"
echo "프롬프트: $PROMPT"
echo "----------------------------------------"
curl -s -X POST "$API_BASE/chat/guardrail/" \
  -H "Content-Type: application/json" \
  -d @- <<EOF
{
  "prompt": "$PROMPT"
}
EOF
echo ""

# 3. Chat Score
PROMPT="1+1은?"
ANSWER="2입니다."
echo ""
echo "3. Chat Score API"
echo "   POST $API_BASE/chat/score/"
echo "프롬프트: $PROMPT"
echo "답변: $ANSWER"
echo "----------------------------------------"
curl -s -X POST "$API_BASE/chat/score/" \
  -H "Content-Type: application/json" \
  -d @- <<EOF
{
  "messages": [{"role": "user", "content": "$PROMPT"}],
  "answer": "$ANSWER"
}
EOF
echo ""

# 4. Image Generation
PROMPT="귀여운 고양이가 해변에 앉아 있는 그림"
echo ""
echo "4. Image Generation API"
echo "   POST $API_BASE/images/generations/"
echo "프롬프트: $PROMPT"
echo "----------------------------------------"
curl -s -X POST "$API_BASE/images/generations/" \
  -H "Content-Type: application/json" \
  -d @- <<EOF
{
  "prompt": "$PROMPT"
}
EOF
echo ""

# 5. Image Score (by URL)
QUESTION="이 이미지에 고양이가 있나요?"
IMAGE_URL="https://cataas.com/cat"
echo ""
echo "5. Image Score (URL) API"
echo "   POST $API_BASE/images/score/url/"
echo "질문: $QUESTION"
echo "이미지 URL: $IMAGE_URL"
echo "----------------------------------------"
curl -s -X POST "$API_BASE/images/score/url/" \
  -H "Content-Type: application/json" \
  -d @- <<EOF
{
  "question": "$QUESTION",
  "image_url": "$IMAGE_URL"
}
EOF
echo ""

# 6. Decide Route
PROMPT="날씨가 어때?"
echo ""
echo "6. Decide Route API"
echo "   POST $API_BASE/decide-route/"
echo "프롬프트: $PROMPT"
echo "----------------------------------------"
curl -s -X POST "$API_BASE/decide-route/" \
  -H "Content-Type: application/json" \
  -d @- <<EOF
{
  "prompt": "$PROMPT"
}
EOF
echo ""

# 7. TTS (Generate Speech)
TEXT="안녕하세요, TTS 테스트입니다."
echo ""
echo "7. TTS (Generate Speech) API"
echo "   POST $API_BASE/generate-speech/"
echo "텍스트: $TEXT"
echo "----------------------------------------"
curl -s -X POST "$API_BASE/generate-speech/" \
  -H "Content-Type: application/json" \
  -d @- <<EOF
{
  "text": "$TEXT"
}
EOF
echo ""

echo ""
echo "========================================"
echo "테스트 완료"
echo "========================================"
