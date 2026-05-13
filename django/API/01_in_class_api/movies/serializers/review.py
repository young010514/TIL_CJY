from rest_framework import serializers
from ..models import Review, Movie

# 전체 리뷰 목록
class ReviewListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ('title', 'content',)


# 단일 리뷰 정보 (해당되는 영화의 제목 포함)
class ReviewSerializer(serializers.ModelSerializer):
    class MovieSerializer(serializers.ModelSerializer):
        class Meta:
            model = Movie
            fields = ('title',)


    movie = MovieSerializer(read_only=True)

    class Meta:
        model = Review
        fields = '__all__'