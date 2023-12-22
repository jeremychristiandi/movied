from django.contrib import admin

from .all_models.movie_model import Movie
from .all_models.actor_model import Actor
from .all_models.starring_model import Starring
from .all_models.genre_model import Genre

class MovieAdmin(admin.ModelAdmin):
    list_display = ("title", "rating")
    prepopulated_fields = {
        "slug": ("title",)
    }

# Register your models here.
admin.site.register(Movie)
admin.site.register(Actor)
admin.site.register(Genre)
admin.site.register(Starring)