from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import PerformanceViewSet


router = DefaultRouter()
router.register("performances", PerformanceViewSet, basename="performance")


urlpatterns = [
    path("", include(router.urls)),
]