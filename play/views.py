from rest_framework import viewsets
from django.views.generic import ListView, DetailView

from .models import Play, Actor, Genre
from .serializers import (
    PlaySerializer,
    PlayListSerializer,
    ActorSerializer,
    ActorListSerializer,
    GenreSerializer,
    GenreListSerializer
)

#API
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


#HTML
class ActorListView(ListView):
    model = Actor
    template_name = "play/actors_list.html"
    context_object_name = "actors"


class ActorDetailView(DetailView):
    model = Actor
    template_name = "play/actor_detail.html"
    context_object_name = "actor"


class GenreListView(ListView):
    model = Genre
    template_name = "play/genres_list.html"
    context_object_name = "genres"


class PlayListView(ListView):
    model = Play
    template_name = "play/plays_list.html"
    context_object_name = "plays"


class PlayDetailView(DetailView):
    model = Play
    template_name = "play/play_detail.html"
    context_object_name = "play"
