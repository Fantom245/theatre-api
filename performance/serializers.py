from rest_framework import serializers

from .models import Performance
from play.models import Play
from theatrehall.models import TheatreHall


class PlayShortSerializer(serializers.ModelSerializer):
    class Meta:
        model = Play
        fields = ["id", "title"]


class TheatreHallShortSerializer(serializers.ModelSerializer):
    class Meta:
        model = TheatreHall
        fields = ["id", "name", "rows", "seats_in_row", "total_seats"]


class PerformanceSerializer(serializers.ModelSerializer):
    play = PlayShortSerializer(read_only=True)
    theatre_hall = TheatreHallShortSerializer(read_only=True)

    play_id = serializers.PrimaryKeyRelatedField(
        source="play",
        queryset=Play.objects.all(),
        write_only=True
    )

    theatre_hall_id = serializers.PrimaryKeyRelatedField(
        source="theatre_hall",
        queryset=TheatreHall.objects.all(),
        write_only=True
    )

    class Meta:
        model = Performance
        fields = ["id", "play", "theatre_hall", "show_time", "play_id", "theatre_hall_id", "created_at", "updated_at"]
        read_only_fields = ["id", "created_at", "updated_at"]