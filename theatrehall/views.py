from rest_framework import viewsets
from django.views.generic import ListView, DetailView

from .models import TheatreHall
from .serializers import TheatreHallSerializer, TheatreHallListSerializer


class TheatreHallViewSet(viewsets.ModelViewSet):
    queryset = TheatreHall.objects.all()

    def get_serializer_class(self):
        if self.action == "list":
            return TheatreHallListSerializer
        return TheatreHallSerializer


class TheatreHallListView(ListView):
    model = TheatreHall
    template_name = "theatrehall/theatrehall_list.html"
    context_object_name = "theatrehalls"