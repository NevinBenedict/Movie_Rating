from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator


# Create your models here.

class Movie(models.Model):
    name = models.CharField(max_length=100)
    LANGUAGE_CHOICES = [
        ('english', 'English'),
        ('hindi', 'Hindi'),
        ('tamil', 'Tamil'),
        ('telugu', 'Telugu'),
        ('malayalam', 'Malayalam'),
        ('kannada', 'Kannada'),
    ]
    language =  models.CharField(max_length=20, choices=LANGUAGE_CHOICES)
    GENRE_CHOICES = [
        ('action', 'Action'),
        ('comedy', 'Comedy'),
        ('drama', 'Drama'),
        ('horror', 'Horror'),
        ('romance', 'Romance'),
        ('thriller', 'Thriller'),   
        ('sci-fi', 'Sci-Fi'),
    ]
    genre = models.CharField(max_length=20, choices=GENRE_CHOICES)
    year = models.IntegerField()
    director = models.CharField(max_length=100)
    poster = models.ImageField(upload_to='posters/', null=True, blank=True)

    def __str__(self):
        return self.name
    


class Review(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    review = models.TextField()
    rating = models.FloatField()

   