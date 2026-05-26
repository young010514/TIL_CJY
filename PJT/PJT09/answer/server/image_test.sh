BASE_URL="http://localhost:8080"
API_BASE="$BASE_URL/api/v1"

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