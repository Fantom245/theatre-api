from django.urls import path

from .views import TheatreHallListView


urlpatterns = [
    path("theatrehalls/", TheatreHallListView.as_view(), name="theatrehalls-list"),
]
