from rest_framework import serializers
from .models import Director, Movie, Review

class DirectorSerializers(serializers.ModelSerializer):
    class Meta:
        model = Director
        fields = ['name']


class MovieSerializers(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ['title', 'description', 'duration', 'director']

class ReviewSerializers(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['text', 'movie']
