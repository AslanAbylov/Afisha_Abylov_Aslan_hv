# Generated by Django 4.1.7 on 2023-02-19 18:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('movie_app', '0012_alter_review_stars'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movie',
            name='director',
        ),
        migrations.AddField(
            model_name='director',
            name='movie',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='movie_app.movie'),
        ),
    ]
