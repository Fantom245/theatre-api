from django.urls import path

from .views import ActorListView, ActorDetailView, GenreListView, PlayListView, PlayDetailView


urlpatterns = [
    path("actors/", ActorListView.as_view(), name="actors-list"),
    path("actors/<int:pk>/", ActorDetailView.as_view(), name="actor-detail"),
    path("genres/", GenreListView.as_view(), name="genres-list"),
    path("plays/", PlayListView.as_view(), name="plays-list"),
    path("plays/<int:pk>/", PlayDetailView.as_view(), name="play-detail")
]
