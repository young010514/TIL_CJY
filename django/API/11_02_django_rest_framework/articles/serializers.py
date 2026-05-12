from rest_framework import serializers
from .models import Article, Comment


# 단일 게시글 데이터(단일 인스턴스)를 직렬화 하는 도구
# 그러면 ArticleListSerializer를 단일 게시글에서는 못쓰나요? ==> NO
class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = '__all__'


# 전체 게시글 데이터(쿼리셋)를 직렬화 하는 도구
class ArticleListSerializer(serializers.ModelSerializer):
    class CommentDetailSerializer(serializers.ModelSerializer):
        class Meta:
            model = Comment
            fields =('id','content',)

    # 기존에 article이 가지고 있는 역참조 매니저인 comment_set에 값을 CommentDetailSerializer로 변경
    comment_set= CommentDetailSerializer(read_only=True,many=True)

    class Meta:
        model = Article
        fields = ('id', 'title', 'content',)

class CommentSerializer(serializers.ModelSerializer):

    # [댓글 데이터 제공할 때 댓글이 작성된 게시글의 번호와 제목도 함께 제공하기 위한 추가 데이터 설정]
    # 게시글의 제목을 직렬화할 수 있는 도구를 생성
    class ArticleTitleSerializer(serializers.ModelSerializer):
        class Meta:
            model = Article
            fields=('id','title',)

    # 기존 읽기전용 필드인 article 필드를 위해 도구(ArticleTitleSerializer)의 결과 값으로 재정의
    # 기존 필드를 재정의 할때는 Meta클래스에서 작성했던 read_only_fields 가 먹히지 않게 됨
    # 다른 방법으로 읽기 전용 필드로 설정 (read_only 속성)
    article = ArticleTitleSerializer(read_only=True)
        
    class Meta:
        model = Comment
        fields="__all__"
        # read_only_fields=('article',)