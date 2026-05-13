# /movies/serializers/movie.py

from rest_framework import serializers
from ..models import Movie, Actor, Review

# 전체 영화 목록
class MovieListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ('title', 'overview',)



# 단일 영화 정보 (출연배우 그리고 리뷰목록 포함)
class MovieSerializer(serializers.ModelSerializer):

    class ActorSerializer(serializers.ModelSerializer):
        class Meta:
            model = Actor
            fields = ('name',)

    class ReviewListSerializer(serializers.ModelSerializer):
        class Meta:
            model = Review
            fields = ('title', 'content')

    actors = ActorSerializer(many=True, read_only=True)
    
    review_set = ReviewListSerializer(many=True, read_only=True)

    class Meta:
        model = Movie
        fields = '__all__'