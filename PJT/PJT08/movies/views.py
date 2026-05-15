from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from .models import Actor, Movie, Review
from .serializers import *



# Create your views here.
@api_view(['GET'])
def actor_list(request):
    if request.method =='GET':
        actors = Actor.objects.all()
        serializer = ActorListSerializer(actors,many=True)
        return Response(serializer.data)




@api_view(['GET'])
def actor_detail(request,actor_id):
    actor = Actor.objects.get(pk=actor_id)
    if request.method=='GET':
        serializer=ActorSerializer(actor)
        return Response(serializer.data)
    



@api_view(['GET'])
def movie_list(request):
    if request.method =='GET':
        movies = Movie.objects.all()
        serializer = MovieListSerializer(movies,many=True)
        return Response(serializer.data)


@api_view(['GET'])
def movie_detail(request,movie_id):
    movie=Movie.objects.get(pk=movie_id)
    if request.method =='GET':
        serializer = MovieSerializer(movie)
        return Response(serializer.data)



@api_view(['GET'])
def review_list(request):
    if request.method =='GET':
        reviews = Review.objects.all()
        serializer = ReviewListSerializer(reviews,many=True)
        return Response(serializer.data)






@api_view(['GET','PUT','DELETE'])
def review_detail(request,review_id):
    review=Review.objects.get(pk=review_id)
    if request.method=='GET':
        serializer=ReviewSerializer(review)
        return Response(serializer.data)

    elif request.method=='PUT':
        # 수정
        serializer=ReviewSerializer(review,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.data,status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method =='DELETE':
        # 삭제
        review.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



@api_view(['POST'])
def create_review(request,movie_id):
    if request.method=='POST':
        movie=Movie.objects.get(pk=movie_id)
        serializer=ReviewSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(movie=movie)
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_405_METHOD_NOT_ALLOWED)
