from rest_framework import serializers

from .models import Performance
from play.models import Play
from theatrehall.models import TheatreHall
from theatrehall.serializers import TheatreHallListSerializer


class PlayShortSerializer(serializers.ModelSerializer):
    class Meta:
        model = Play
        fields = ["id", "title"]


class PerformanceSerializer(serializers.ModelSerializer):
    play = PlayShortSerializer(read_only=True)
    theatre_hall = TheatreHallListSerializer(read_only=True)

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


class PerformanceListSerializer(PerformanceSerializer):
    class Meta(PerformanceSerializer.Meta):
        fields = ["id", "play", "theatre_hall", "show_time"]
        read_only_fields = ["id"]