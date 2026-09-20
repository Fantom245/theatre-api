from rest_framework import viewsets

from .models import Performance
from .serializers import PerformanceSerializer, PerformanceListSerializer


class PerformanceViewSet(viewsets.ModelViewSet):
    queryset = Performance.objects.select_related(
        "play",
        "theatre_hall"
    )

    def get_serializer_class(self):
        if self.action == "list":
            return PerformanceListSerializer
        return PerformanceSerializer

