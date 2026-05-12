from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view

from rest_framework import status

from .models import Article
from .serializers import ArticleListSerializer,ArticleSerializer

# Create your views he
# 4. 모든 DRF의 뷰함수는 반드시 api_view 데코레이터가 필수
@api_view(['GET','POST'])
def article_list(request):
    if request.method =='GET':
        # 1. 전체 게시글 조회 (DB)
        articles =Article.objects.all()
        # 그런데 articles는 쿼리셋 형식이여서 다른 서비스들은 이 타입을 활용할 수 없음
        # 직렬화를 진행해서 유연한 데이터 형식으로 전환하는 과정이 필요
        # 2. 직렬화
        # 원물데이터가 단일데이터가 아닌형식이면 many 옵션을 True로 변경 피룡
        serializer = ArticleListSerializer(articles,many=True)
        # 3. 직렬화된 데이터 덩어리에서 게시글 데이터만 추출해서 응답
        return Response(serializer.data)
    
    elif request.method=='POST':
        # 1. 사용자가 보낸 데이터를 직렬화
        # 과거에는 request.POST에서 추출했지만 DRF에서는 request.data를 사용
        serializer = ArticleSerializer(data=request.data)
        # 2. 유효성 검사
        if serializer.is_valid():
            # 3. 저장
            serializer.save()
            # 4. 저장 후 201 상태 코드 응답
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        # 5. 유효성 검사 실패했다면 40 상태 코드 응답
        return Response(serializer.errors , status=status.HTTP_400_BAD_REQUEST)
    


@api_view(['GET','DELETE','PATCH'])
def article_detail(request,article_id):
    article = Article.objects.get(pk=article_id)
    if request.method=='GET':
        # 1. 단일 게시글 조회
        # 2. 직렬화
        serializer = ArticleSerializer(article)
        # 3. 직렬화된 데이터에서 필요한 데이터만 추출하여 응답
        return Response(serializer.data)
    elif request.method=='DELETE':
        # 조회된 게시글 데이터를 삭제
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    elif request.method=='PATCH': # PUT은 전체 수정 PATCH 는 partial=True 옵션으로 부분 수정 가능
        # 1. 사용자가 보낸 수정 데이터를 직렬화
        # 수정이기 때문에 기존 객체를 함께 넣어서 직렬화를 진행
        serializer=ArticleSerializer(article,data=request.data,partial=True)
        # serializer=ArticleSerializer(instance=article,data=request.data)
        if serializer.is_valid():
            serializer.save()
            # 2. 갱신 후 201 상태 코드 응답
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        # 3. 유효성 검사 실패했다면 40 상태 코드 응답
        return Response(serializer.errors , status=status.HTTP_400_BAD_REQUEST)