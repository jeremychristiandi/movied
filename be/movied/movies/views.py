from django.shortcuts import render
from django.http import Http404
from django.db.models import Q

from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Movies
from .serializers import MoviesSerializer


class AllMovies(APIView):
    def get(self, request, format=None):
        movies = Movies.objects.all()
        serializer = MoviesSerializer(movies, many=True)

        return Response(serializer.data)

class MovieDetail(APIView):
    def get_movie(self, movie_slug):
        try:
            return Movies.objects.get(slug=movie_slug)
        except Movies.DoesNotExist:
            raise Http404

    def get(self, request, movie_slug, format=None):
        movie = self.get_movie(movie_slug)
        serializer = MoviesSerializer(movie)
        return Response(serializer.data)