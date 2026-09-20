from rest_framework import serializers

from .models import Actor, Genre, Play


class ActorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = ["id", "first_name", "last_name", "created_at", "updated_at"]
        read_only_fields = ["id", "created_at", "updated_at"]


class ActorListSerializer(serializers.ModelSerializer):
    class Meta:
            model = Actor
            fields = ["id", "first_name", "last_name"]
            read_only_fields = ["id"]


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ["id", "name", "created_at", "updated_at"]
        read_only_fields = ["id", "created_at", "updated_at"]


class GenreListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ["id", "name"]
        read_only_fields = ["id"]


class PlaySerializer(serializers.ModelSerializer):
    actors = ActorSerializer(many=True, read_only=True)
    genres = GenreSerializer(many=True, read_only=True)

    actors_ids = serializers.PrimaryKeyRelatedField(
        source="actors",
        queryset=Actor.objects.all(),
        many=True,
        write_only=True,
        help_text="List of actor IDs associated with the play"
    )

    genres_ids = serializers.PrimaryKeyRelatedField(
        source="genres",
        queryset=Genre.objects.all(),
        many=True,
        write_only=True,
        help_text="List of genre IDs associated with the play"
    )

    class Meta:
        model = Play
        fields = ["id", "title", "description", "actors", "genres", "actors_ids", "genres_ids", "created_at", "updated_at"]
        read_only_fields = ["id", "created_at", "updated_at"]
