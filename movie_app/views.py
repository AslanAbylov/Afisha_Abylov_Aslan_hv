from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Director, Movie, Review
from .serializer import DirectorSerializers, MovieSerializers, ReviewSerializers, MovieReviewSerializers, DirectorCreateSerializers, MovieCreateSerializers, ReviewCreateSerializers


@api_view(['GET'])
def get_movie_review_list_api_view(request):
    movie = Movie.objects.all()
    serializers = MovieReviewSerializers(movie, many=True)
    return Response(data=serializers.data)


@api_view(['GET', 'POST'])
def directors_list_api_view(request):
    if request.method == 'GET':
        directors = Director.objects.all()
        serializers = DirectorSerializers(directors, many=True)
        return Response(data=serializers.data)
    elif request.method == 'POST':
        serializers = DirectorCreateSerializers(data=request.data)
        if not serializers.is_valid():
            return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
        name = request.data.get('name')
        director = Director.objects.create(name=name)
        return Response(data={'message': 'data received!', 'director': DirectorSerializers(director).data}, status=status.HTTP_201_CREATED)


@api_view(['GET', 'PUT', 'DELETE'])
def director_detail_list_api_view(request, id):
    try:
        director = Director.objects.get(id=id)
    except Director.DoesNotExist:
        return Response(data={'directors': 'director not found'}, status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = DirectorSerializers(director)
        return Response(data=serializer.data)
    elif request.method == 'PUT':
        serializers = DirectorCreateSerializers(data=request.data)
        if not serializers.is_valid():
            return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
        director.name = request.data.get('name')
        director.save()
        return Response(data={'message': 'data received', 'director': DirectorSerializers(director).data})
    elif request.method == 'DELETE':
        director.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
def movies_list_api_view(request):
    if request.method == 'GET':
        movies = Movie.objects.all()
        serializers = MovieSerializers(movies, many=True)
        return Response(data=serializers.data)
    elif request.method == 'POST':
        serializers = MovieCreateSerializers(data=request.data)
        if not serializers.is_valid():
            return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
        title = request.data.get('title')
        description = request.data.get('description')
        duration = request.data.get('duration')
        director_id = request.data.get('director_id')
        movie = Movie.objects.create(title=title, duration=duration, description=description, director_id=director_id)
        return Response(data={'data': 'received', 'movie': MovieSerializers(movie).data}, status=status.HTTP_201_CREATED)


@api_view(['GET', 'PUT', 'DELETE'])
def movie_detail_list_api_view(request, id):
    try:
        movie = Movie.objects.get(id=id)
    except Movie.DoesNotExist:
        return Response(data={'movie': 'movie not found'}, status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = MovieSerializers(movie)
        return Response(data=serializer.data)
    elif request.method == 'PUT':
        serializers = MovieCreateSerializers(data=request.data)
        if not serializers.is_valid():
            return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
        movie.title = request.data.get('title')
        movie.description = request.data.get('description')
        movie.duration = request.data.get('duration')
        movie.director_id = request.data.get('director_id')
        return Response(data={'data': 'received!', 'movie': MovieSerializers(movie).data})
    elif request.method == 'DELETE':
        movie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
def review_list_api_view(request):
    if request.method == 'GET':
        reviews = Review.objects.all()
        serializers = ReviewSerializers(reviews, many=True)
        return Response(data=serializers.data)
    elif request.method == 'POST':
        serializers = ReviewCreateSerializers(data=request.data)
        if not serializers.is_valid():
            return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
        text = request.data.get('text')
        stars = request.data.get('stars')
        movie_id = request.data.get('movie_id')
        reviews = Review.objects.create(text=text, stars=stars, movie_id=movie_id)
        return Response(data={'data': 'received!', 'reviews' : ReviewSerializers(reviews).data}, status=status.HTTP_201_CREATED)


@api_view(['GET', 'DELETE', 'PUT'])
def review_detail_list_api_view(request, id):
    try:
        review = Review.objects.get(id=id)
    except Review.DoesNotExist:
        return Response(data={'review': 'review not found'}, status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializers = ReviewSerializers(review)
        return Response(data=serializers.data)
    elif request.method == 'DELETE':
        review.delete()
        return Response(data={'data': 'received!', 'review' : ReviewSerializers(review).data}, status=status.HTTP_204_NO_CONTENT)
    elif request.method == 'PUT':
        serializers = ReviewCreateSerializers(data=request.data)
        if not serializers.is_valid():
            return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
        review.text = request.data.get('text')
        review.stars = request.data.get('stars')
        review.movie_id = request.data.get('movie_id')
        review.save()
        return Response(data={'message': 'data received!', 'review': ReviewSerializers(review).data})



