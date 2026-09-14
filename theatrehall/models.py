from django.db import models

from play.models import TimeStampedModel


class TheatreHall(TimeStampedModel):
    name = models.CharField(
        max_length=100,
        unique=True,
        help_text="Theatre hall name"
    )
    rows = models.PositiveIntegerField(
        help_text="Number of rows in the theatre hall"
    )
    seats_in_row = models.PositiveIntegerField(
        help_text="Number of seats in each row"
    )

    @property
    def total_seats(self):
        return self.rows * self.seats_in_row

    class Meta:
        ordering = ["name"]
        verbose_name = "Theatre Hall"
        verbose_name_plural = "Theatre Halls"

    def __str__(self):
        return self.name
