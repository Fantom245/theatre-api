from django.db import models
from django.contrib.auth import get_user_model

from play.models import TimeStampedModel
from performance.models import Performance


User = get_user_model()


class Reservation(models.Model):
    created_at = models.DateTimeField(
        auto_now_add=True,
        help_text="Creation timestamp"
    )
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="reservations",
        help_text="User who made the reservation"
    )

    class Meta:
        verbose_name = "reservation"
        verbose_name_plural = "reservations"
        ordering = ["-created_at"]

    def __str__(self):
        return f"Reservation ID: {self.id}, User: {self.user.email}, Created At: {self.created_at}"


class Ticket(TimeStampedModel):
    row = models.PositiveIntegerField(help_text="Row number of the seat")
    seat = models.PositiveIntegerField(help_text="Seat number within the row")
    performance = models.ForeignKey(
        Performance,
        on_delete=models.CASCADE,
        related_name="tickets",
        help_text="Performance for which the ticket is issued"
    )
    reservation = models.ForeignKey(
        Reservation,
        on_delete=models.CASCADE,
        related_name="tickets",
        help_text="Reservation associated with the ticket"
    )

    class Meta:
        verbose_name = "ticket"
        verbose_name_plural = "tickets"
        ordering = ["performance", "row", "seat"]

    def __str__(self):
        return f"Ticket ID: {self.id}, Performance: {self.performance}, Row: {self.row}, Seat: {self.seat}"
