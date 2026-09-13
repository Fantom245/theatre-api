from django.db import models


class Actor(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    class Meta:
        ordering = ["last_name", "first_name"]
        verbose_name = "Actor"
        verbose_name_plural = "Actors"

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Genre(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        ordering = ["name"]
        verbose_name = "Genre"
        verbose_name_plural = "Genres"

    def __str__(self):
        return self.name


class Play(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()

    actors = models.ManyToManyField(Actor, related_name="plays", blank=True)
    genres = models.ManyToManyField(Genre, related_name="plays", blank=True)

    class Meta:
        ordering = ["title"]
        verbose_name = "Play"
        verbose_name_plural = "Plays"

    def __str__(self):
        return self.title
