from rest_framework import viewsets

from .models import Play, Actor, Genre
from .serializers import PlaySerializer, ActorSerializer, GenreSerializer


class ActorViewSet(viewsets.ModelViewSet):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer


class GenreViewSet(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer


class PlayViewSet(viewsets.ModelViewSet):
    queryset = Play.objects.prefetch_related(
        "actors",
        "genres"
    )
    serializer_class = PlaySerializer
