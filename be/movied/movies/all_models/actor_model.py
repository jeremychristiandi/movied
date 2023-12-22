from django.db import models
from django.core import serializers
from django.core.validators import MaxValueValidator, MinValueValidator
import datetime
# from .movie_model import Movie

BASE_URL = 'http://127.0.0.1:8020'

class Actor(models.Model):
    name = models.CharField(max_length=250)
    birth_date = models.DateField()
    height = models.IntegerField(blank=True, null=True)
    # movie = models.ManyToManyField(Movie)
    image = models.ImageField(upload_to="uploads/", blank=True, null=True)
    
    def __str__(self):
        return self.name

    def age(self):
        return datetime.date.today() - self.birth_date

    def image_url(self):
        if self.image:
            return BASE_URL + self.image.url
        return ''

    # def all_movies(self):
    #     return self.movie.all()