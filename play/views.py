from rest_framework import viewsets

from .models import Play, Actor, Genre
from .serializers import (
    PlaySerializer,
    PlayListSerializer,
    ActorSerializer,
    ActorListSerializer,
    GenreSerializer,
    GenreListSerializer
)


class ActorViewSet(viewsets.ModelViewSet):
    queryset = Actor.objects.all()

    def get_serializer_class(self):
        if self.action == "list":
            return ActorListSerializer
        return ActorSerializer


class GenreViewSet(viewsets.ModelViewSet):
    queryset = Genre.objects.all()

    def get_serializer_class(self):
        if self.action == "list":
            return GenreListSerializer
        return GenreSerializer


class PlayViewSet(viewsets.ModelViewSet):
    queryset = Play.objects.prefetch_related(
        "actors",
        "genres"
    )

    def get_serializer_class(self):
        if self.action == "list":
            return PlayListSerializer
        return PlaySerializer
