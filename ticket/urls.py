from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import ReservationViewSet, TicketViewSet


router = DefaultRouter()
router.register("reservations", ReservationViewSet, basename="reservation")
router.register("tickets", TicketViewSet, basename="ticket")


urlpatterns = [
    path("", include(router.urls)),
]