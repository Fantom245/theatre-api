from django.db import models


class TimeStampedModel(models.Model):
    created_at = models.DateTimeField(
        auto_now_add=True,
        help_text="Creation timestamp"
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        help_text="Last update timestamp"
    )

    class Meta:
        abstract = True


class Actor(TimeStampedModel):
    first_name = models.CharField(
        max_length=100,
        db_index=True,
        help_text="Actor first name"
    )
    last_name = models.CharField(
        max_length=100,
        db_index=True,
        help_text="Actor last name"
    )

    class Meta:
        ordering = ["last_name", "first_name"]
        verbose_name = "Actor"
        verbose_name_plural = "Actors"
        constraints = [
            models.UniqueConstraint(
                fields=[
                    "first_name",
                    "last_name"
                ], name="unique_actor_name"
            )
        ]

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Genre(TimeStampedModel):
    name = models.CharField(
        max_length=100,
        unique=True,
        help_text="Genre name"
    )

    class Meta:
        ordering = ["name"]
        verbose_name = "Genre"
        verbose_name_plural = "Genres"

    def __str__(self):
        return self.name


class Play(TimeStampedModel):
    title = models.CharField(
        max_length=200,
        unique=True,
        help_text="Play title"
    )
    description = models.TextField(
        blank=True,
        help_text="Play description"
    )

    actors = models.ManyToManyField(
        Actor,
        related_name="plays",
        blank=True
    )
    genres = models.ManyToManyField(
        Genre,
        related_name="plays",
        blank=True
    )

    class Meta:
        ordering = ["title"]
        verbose_name = "Play"
        verbose_name_plural = "Plays"

    def __str__(self):
        return self.title
