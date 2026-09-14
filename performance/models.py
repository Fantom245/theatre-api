from django.db import models

from play.models import Play, TimeStampedModel
from theatrehall.models import TheatreHall


class Performance(TimeStampedModel):
    play = models.ForeignKey(
        Play,
        on_delete=models.CASCADE,
        related_name="performances",
        help_text="Play being performed"
    )
    theatre_hall = models.ForeignKey(
        TheatreHall,
        on_delete=models.CASCADE,
        related_name="performances",
        help_text="Theatre hall where the performance takes place"
    )
    show_time = models.DateTimeField(help_text="Date and time of the performance")

    class Meta:
        verbose_name = "performance"
        verbose_name_plural = "performances"
        ordering = ["show_time"]

    def __str__(self):
        return f"Performance of '{self.play.title}' at {self.show_time} in {self.theatre_hall.name}"
