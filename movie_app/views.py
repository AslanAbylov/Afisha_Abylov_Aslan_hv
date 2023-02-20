from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Director, Movie, Review
from .serializer import DirectorSerializers, MovieSerializers, ReviewSerializers, MovieReviewSerializers


@api_view(['GET'])
def get_movie_review_list_api_view(request):
    movie = Movie.objects.all()
    serializers = MovieReviewSerializers(movie, many=True)
    return Response(data=serializers.data)


@api_view(['GET'])
def directors_list_api_view(request):
    directors = Director.objects.all()
    serializers = DirectorSerializers(directors, many=True)
    return Response(data=serializers.data)


@api_view(['GET'])
def director_detail_list_api_view(request, id):
    try:
        director = Director.objects.get(id=id)
    except Director.DoesNotExist:
        return Response(data={'directors': 'director not found'}, status=status.HTTP_404_NOT_FOUND)
    serializer = DirectorSerializers(director)
    return Response(data=serializer.data)


@api_view(['GET'])
def movies_list_api_view(request):
    movies = Movie.objects.all()
    serializers = MovieSerializers(movies, many=True)
    return Response(data=serializers.data)


@api_view(['GET'])
def movie_detail_list_api_view(request, id):
    try:
        movie = Movie.objects.get(id=id)
    except Movie.DoesNotExist:
        return Response(data={'movie': 'movie not found'}, status=status.HTTP_404_NOT_FOUND)
    serializer = MovieSerializers(movie)
    return Response(data=serializer.data)


@api_view(['GET'])
def review_list_api_view(request):
    reviews = Review.objects.all()
    serializers = ReviewSerializers(reviews, many=True)
    return Response(data=serializers.data)


@api_view(['GET'])
def review_detail_list_api_view(request, id):
    try:
        review = Review.objects.get(id=id)
    except Review.DoesNotExist:
        return Response(data={'review': 'review not found'}, status=status.HTTP_404_NOT_FOUND)
    serializers = ReviewSerializers(review)
    return Response(data=serializers.data)




