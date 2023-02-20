from django.db import models

class Director(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    def movies_count(self):
        try:
            return self.movie.all().count()
        except:
            return ''



class Movie(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    duration = models.FloatField()
    director = models.ManyToManyField(Director, null=True, blank=True, related_name='movie')


    def __str__(self):
        return self.title


    def rating(self):
        try:
            count = self.movie_reviews.all().count()
            stars = sum([i.stars for i in self.movie_reviews.all()])
            return stars // count
        except:
            return ''


class Review(models.Model):
    text = models.TextField()
    stars = models.IntegerField(choices=(
        (1, '*'),
        (2, '**'),
        (3, '***'),
        (4, '****'),
        (5, '*****'),
    ), default=5)
    movie = models.ForeignKey(Movie, models.CASCADE, null=True, blank=True, related_name='movie_reviews')

    def __str__(self):
        return self.text



