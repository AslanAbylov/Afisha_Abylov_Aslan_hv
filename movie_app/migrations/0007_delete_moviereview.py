# Generated by Django 4.1.7 on 2023-02-19 17:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movie_app', '0006_moviereview_remove_review_movie_movie_review'),
    ]

    operations = [
        migrations.DeleteModel(
            name='MovieReview',
        ),
    ]