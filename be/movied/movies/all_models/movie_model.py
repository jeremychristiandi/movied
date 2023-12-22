from django.db import models
from django.core import serializers
from django.core.validators import MaxValueValidator, MinValueValidator
from .genre_model import Genre
from .actor_model import Actor
from movies.all_models.starring_model import Starring

BASE_URL = 'http://127.0.0.1:8020'

class Movie(models.Model):
    title = models.CharField(max_length=250)
    # actor = models.ManyToManyField(Actor)
    # actor = models.ForeignKey(Actor, related_name="actors", on_delete=models.CASCADE, blank=True, null=True)
    genre = models.ForeignKey(Genre, related_name="movies", on_delete=models.CASCADE, default=None, blank=True, null=True)
    release_year = models.IntegerField(blank=True, null=True, default=None)
    slug = models.SlugField(blank=True, null=True)
    rating = models.FloatField(validators=[MinValueValidator(1.0), MaxValueValidator(10.0)])
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to="uploads/", blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def image_url(self):
        if self.image:
            return BASE_URL + self.image.url
        return ''

    def get_absolute_url(self):
        return f"/movies/{self.slug}/"

    @property
    def starrings(self):
        starring = Starring.objects.filter(movie__id=self.id)
        # actor_ids = starring.values_list("actor", flat=True)
        # return Actor.objects.filter(id__in=actor_ids)
        return starring

    # @property
    # def starring(self):
    #     return list(Starring.objects.filter(movie__id=self.id)[0].actor.all())

    # def all_actors(self):
    #     actors_data = []
    #     for actor in self.actor.all():
    #         actors_data.append(actor.name)
    #     return actors_data