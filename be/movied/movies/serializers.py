from rest_framework import serializers
from .models import Movies, Actor

class ActorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = (
            'name',
            'birth_date',
            'image_url'
        )

class MoviesSerializer(serializers.ModelSerializer):
    actor = ActorSerializer(many=True)

    class Meta:
        model = Movies
        fields = (
            'id',
            'title',
            'genre',
            'release_year',
            'actor',
            'rating',
            'description',
            'image_url'
        )