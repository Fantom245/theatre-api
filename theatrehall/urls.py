from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import TheatreHallViewSet


router = DefaultRouter()
router.register("theatrehall", TheatreHallViewSet, basename="theatrehall")


urlpatterns = [
    path("", include(router.urls)),
]
