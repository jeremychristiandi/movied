from django.shortcuts import render
from django.http import Http404
from django.db.models import Q

from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .all_models.movie_model import Movie
from .all_models.actor_model import Actor
from .all_models.genre_model import Genre
from .serializers import MovieSerializer, GenreSerializer, ActorSerializer

class AllMovies(APIView):
    def get(self, request, format=None):
        movies = Movie.objects.all()
        serializer = MovieSerializer(movies, many=True)

        return Response(serializer.data)

class MovieDetail(APIView):
    def get_movie(self, movie_slug):
        try:
            return Movie.objects.get(slug=movie_slug)
        except Movie.DoesNotExist:
            raise Http404

    def get(self, request, movie_slug, format=None):
        movie = self.get_movie(movie_slug)
        serializer = MovieSerializer(movie)
        return Response(serializer.data)

class AllGenres(APIView):
    def get(self, request, format=None):
        genres = Genre.objects.all()
        serializer = GenreSerializer(genres, many=True)

        return Response(serializer.data)

class AllActors(APIView):
    def get(self, request, format=None):
        actors = Actor.objects.all()
        serializer = ActorSerializer(actors, many=True)

        return Response(serializer.data)