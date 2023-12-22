from rest_framework import serializers
from .all_models.movie_model import Movie
from .all_models.actor_model import Actor
from .all_models.starring_model import Starring
from .all_models.genre_model import Genre

class ActorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = (
            'id',
            'name',
            'birth_date',
            'age',
            'image_url',
        )

class StarringSerializer(serializers.ModelSerializer):
    # cast = serializers.SerializerMethodField()

    # def get_cast(self, instance):
    #     cast = instance.cast
    #     serializer = ActorSerializer(data=cast, many=True)
    #     serializer.is_valid()
    #     return serializer.data

    actor = ActorSerializer()

    class Meta:
        model = Starring
        fields = (
            'actor',
            'role'
        )

class MovieSerializer(serializers.ModelSerializer):
    # actors = serializers.SerializerMethodField()

    # def get_actors(self, instance):
    #     actors = instance.actors
    #     serializer = ActorSerializer(data=actors, many=True)
    #     serializer.is_valid()
    #     return serializer.data

    starrings = serializers.SerializerMethodField()

    def get_starrings(self, instance):
        starrings = instance.starrings
        serializer = StarringSerializer(data=starrings, many=True)
        serializer.is_valid()
        return serializer.data

    class Meta:
        model = Movie
        fields = (
            'id',
            'title',
            'genre',
            'release_year',
            'rating',
            'starrings',
            'description',
            'image_url',
            'get_absolute_url'
        )

class GenreSerializer(serializers.ModelSerializer):
    # movies = MovieSerializer(many=True)

    class Meta:
        model = Genre
        fields = (
            'name',
            # 'movies',
        )