from rest_framework import viewsets

from .models import Play
from .serializers import PlaySerializer


class PlayViewSet(viewsets.ModelViewSet):
    queryset = Play.objects.prefetch_related(
        "actors",
        "genres"
    )
    serializer_class = PlaySerializer
