from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import PlayViewSet, ActorViewSet, GenreViewSet


router = DefaultRouter()
router.register("plays", PlayViewSet, basename="play")
router.register("actors", ActorViewSet, basename="actor")
router.register("genres", GenreViewSet, basename="genre")

urlpatterns = [
    path("", include(router.urls)),
]