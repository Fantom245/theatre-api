from rest_framework import serializers

from .models import TheatreHall


class TheatreHallSerializer(serializers.ModelSerializer):
    class Meta:
        model = TheatreHall
        fields = ["id", "name", "rows", "seats_in_row", "total_seats", "created_at", "updated_at"]
        read_only_fields = ["id", "total_seats", "created_at", "updated_at"]
