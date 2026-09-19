from rest_framework import viewsets

from .models import Performance
from .serializers import PerformanceSerializer


class PerformanceViewSet(viewsets.ModelViewSet):
    queryset = Performance.objects.select_related(
        "play",
        "theatre_hall"
    )
    serializer_class = PerformanceSerializer

