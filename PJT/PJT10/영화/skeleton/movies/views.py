from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.http import require_safe
from community.models import Review
from .models import Movie, Genre


# Create your views here.
@require_safe
def index(request):
    movies = Movie.objects.prefetch_related('genres').all()
    genres = Genre.objects.all()
    context = {
        'movies': movies,
        'genres': genres,
    }
    return render(request, 'movies/index.html', context)


@require_safe
def filter_genre(request):
    genre_id = request.GET.get('genre_id')

    movies = Movie.objects.prefetch_related('genres').all()
    if genre_id and genre_id != 'all':
        movies = movies.filter(genres__pk=genre_id).distinct()

    data = {
        'movies': [
            {
                'id': movie.pk,
                'title': movie.title,
                'genres': [genre.name for genre in movie.genres.all()],
            }
            for movie in movies
        ]
    }
    return JsonResponse(data)


@require_safe
def recommended(request):
    recommendation_reason = '인기와 평점이 높은 영화를 추천합니다.'
    recommended_movies = Movie.objects.prefetch_related('genres').order_by(
        '-popularity', '-vote_average'
    )[:10]

    if request.user.is_authenticated:
        liked_reviews = request.user.like_reviews.all()
        liked_titles = liked_reviews.values_list('movie_title', flat=True)
        base_movies = Movie.objects.filter(title__in=liked_titles).prefetch_related('genres')
        genre_ids = Genre.objects.filter(movie__in=base_movies).values_list('pk', flat=True).distinct()

        if genre_ids.exists():
            recommended_movies = Movie.objects.filter(genres__pk__in=genre_ids).distinct().order_by(
                '-popularity', '-vote_average'
            )[:10]
            recommendation_reason = '좋아요한 리뷰의 영화 장르를 기반으로 추천합니다.'

    context = {
        'movies': recommended_movies,
        'recommendation_reason': recommendation_reason,
    }
    return render(request, 'movies/recommended.html', context)
