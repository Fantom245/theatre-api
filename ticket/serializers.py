from rest_framework import serializers
from django.contrib.auth import get_user_model

from .models import Reservation, Ticket
from performance.models import Performance
from performance.serializers import PlayShortSerializer
from theatrehall.serializers import TheatreHallListSerializer


class UserShortSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ["id", "email", "username", "first_name", "last_name"]


class PerformanceShortSerializer(serializers.ModelSerializer):
    play = PlayShortSerializer(read_only=True)
    theatre_hall = TheatreHallListSerializer(read_only=True)

    class Meta:
        model = Performance
        fields = ["id", "play", "theatre_hall", "show_time"]


class ReservationSerializer(serializers.ModelSerializer):
    user = UserShortSerializer(read_only=True)

    user_id = serializers.PrimaryKeyRelatedField(
            source="user",
            queryset=get_user_model().objects.all(),
            write_only=True
        )

    class Meta:
        model = Reservation
        fields = ["id", "created_at", "user", "user_id"]
        read_only_fields = ["id", "created_at"]


class TicketSerializer(serializers.ModelSerializer):
    performance = PerformanceShortSerializer(read_only=True)
    reservation = ReservationSerializer(read_only=True)

    performance_id = serializers.PrimaryKeyRelatedField(
        source="performance",
        queryset=Performance.objects.all(),
        write_only=True
    )

    reservation_id = serializers.PrimaryKeyRelatedField(
            source="reservation",
            queryset=Reservation.objects.all(),
            write_only=True
        )

    class Meta:
        model = Ticket
        fields = ["id", "row", "seat", "performance", "reservation", "performance_id", "reservation_id", "created_at", "updated_at"]
        read_only_fields = ["id", "created_at", "updated_at"]


class TicketListSerializer(TicketSerializer):
    class Meta(TicketSerializer.Meta):
        fields = ["id", "row", "seat", "performance", "reservation"]
        read_only_fields = ["id"]