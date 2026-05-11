from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import Article
from .serializers import *

# Create your views he
# 4. 모든 DRF의 뷰함수는 반드시 api_view 데코레이터가 필수
@api_view(['GET'])
def article_list(request):
    # 1. 전체 게시글 조회 (DB)
    articles = Article.objects.all()
    # 그런데 articles는 쿼리셋 형식이여서 다른 서비스들은 이 타입을 활용할 수 없음
    # 직렬화를 진행해서 유연한 데이터 형식으로 전환하는 과정이 필요
    # 2. 직렬화
    # 원물데이터가 단일데이터가 아닌형식이면 many 옵션을 True로 변경 피룡
    serializer = ArticleListSerializer(articles, many =True)
    # 3. 직렬화된 데이터 덩어리에서 게시글 데이터만 추출해서 응답
    return Response(serializer.data)

@api_view(['GET'])
def article_detail(request,article_id):
    # 1. 단일 게시글 조회
    article = Article.objects.get(pk=article_id)
    # 2. 직렬화
    serializer = ArticleSerializer(article)
    # 3. 직렬화된 데이터에서 필요한 데이터만 추출하여 응답
    return Response(serializer.data)
