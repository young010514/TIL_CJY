from rest_framework import serializers
from .models import Actor, Movie,Review

# 배우의 id, 이름 데이터가 조회
class ActorListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields= (
            'id',
            'name',
        )

# 배우 상세에서 사용할 영화 제목 serializer
class ActorSerializer(serializers.ModelSerializer):
    class MovieTitleSerializer(serializers.ModelSerializer):
        class Meta: 
            model=Movie
            fields=('title',)
        
    movies = MovieTitleSerializer(source='movie_set',many=True, read_only=True)

    class Meta : 
        model = Actor
        fields=('id','name','movies')

# 영화목록
class MovieListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields= (
            'title',
            'overview',
        )

# 영화 디테일 
class MovieSerializer(serializers.ModelSerializer):
    class ActorNameSerializer(serializers.ModelSerializer):
        class Meta :
            model=Actor
            fields=('name',)
        
    class ReviewSerializer(serializers.ModelSerializer):
        class Meta:
            model=Review
            fields=('title','content',)
    actors = ActorNameSerializer(many=True,read_only=True)

    review_set = ReviewSerializer(many=True,read_only=True)

    class Meta :
        model=Movie
        fields=(
            'id',
            'actors',
            'review_set',
            'title',
            'overview',
            'release_date',
            'poster_path',
        )
        
# 리뷰 리스트
class ReviewListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields=('title','content',)

# 리뷰 디테일
class ReviewSerializer(serializers.ModelSerializer):
    class MovieTitleSerializer(serializers.ModelSerializer):
        class Meta:
            model=Movie
            fields=('title',)
    movie = MovieTitleSerializer(read_only=True)

    class Meta:
        model=Review
        fields=(
            'id',
            'movie',
            'title',
            'content',
        )