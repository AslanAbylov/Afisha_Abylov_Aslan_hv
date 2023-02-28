from rest_framework import serializers
from .models import Director, Movie, Review
from rest_framework.exceptions import ValidationError

class MovieSerializers(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ['title', 'description', 'duration', 'director']


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


class DirectorCreateSerializers(serializers.Serializer):
    name = serializers.CharField(min_length=1)


class MovieCreateSerializers(serializers.Serializer):
    title = serializers.CharField()
    description = serializers.CharField()
    duration = serializers.FloatField()
    director_id = serializers.ListField(child=serializers.IntegerField())

    def validatdirector_id(self, director_id):
        try:
            Director.objects.get(id=director_id)
        except Director.DoesNotExist:
            raise ValidationError('Director does not exists')
        return director_id



class ReviewCreateSerializers(serializers.Serializer):
    text = serializers.CharField()
    stars = serializers.IntegerField()
    movie_id = serializers.ListField(child=serializers.IntegerField())

    def validate_movie_id(self, movie_id):
        try:
            Movie.objects.get(id=movie_id)
        except Movie.DoesNotExist:
            raise ValidationError('Movie does not exists')
        return movie_id





