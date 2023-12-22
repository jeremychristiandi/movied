from django.db import models
from movies.all_models.actor_model import Actor

class Starring(models.Model):
    # Movie = movie_model.Movie
    movie = models.ForeignKey('Movie', related_name="movies", on_delete=models.CASCADE, blank=True, null=True)
    # actor = models.ManyToManyField(Actor)
    actor = models.ForeignKey('Actor', related_name="actors", on_delete=models.CASCADE, blank=True, null=True)
    role = models.CharField(max_length=250, blank=True, null=True)

    def __str__(self):
        return str(self.movie)

    @property
    def cast(self):
        return Actor.objects.filter(id=self.actor.id)