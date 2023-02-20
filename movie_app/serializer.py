from rest_framework import serializers
from .models import Director, Movie, Review

class MovieSerializers(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ['title', 'description', 'duration']


class DirectorSerializers(serializers.ModelSerializer):
    class Meta:
        model = Director
        fields = 'id name movies_count'.split()


class ReviewSerializers(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['text', 'movie', "stars"]


class MovieReviewSerializers(serializers.ModelSerializer):
    movie_reviews = ReviewSerializers(many=True)

    class Meta:
        model = Movie
        fields = 'movie_reviews rating'.split()






