from rest_framework import viewsets

from .models import TheatreHall
from .serializers import TheatreHallSerializer, TheatreHallListSerializer


class TheatreHallViewSet(viewsets.ModelViewSet):
    queryset = TheatreHall.objects.all()

    def get_serializer_class(self):
        if self.action == "list":
            return TheatreHallListSerializer
        return TheatreHallSerializer
