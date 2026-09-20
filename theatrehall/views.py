from rest_framework import viewsets

from .models import TheatreHall
from .serializers import TheatreHallSerializer


class TheatreHallViewSet(viewsets.ModelViewSet):
    queryset = TheatreHall.objects.all()
    serializer_class = TheatreHallSerializer
