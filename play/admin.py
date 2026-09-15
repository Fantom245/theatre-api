from django.contrib import admin

from .models import Actor, Genre, Play


@admin.register(Actor)
class ActorAdmin(admin.ModelAdmin):
    list_display = ("id", "first_name", "last_name", "created_at", "updated_at")
    list_display_links = ("id", "first_name", "last_name")
    search_fields = ("first_name", "last_name")
    readonly_fields = ("created_at", "updated_at")
    ordering = ("last_name", "first_name")
    list_per_page = 10

    fieldsets = (
        (None, {
            "fields": ("first_name", "last_name"),
            "classes": ("wide",),
            "description": "Enter the details of the actor."
        }),
    )

    add_fieldsets = (
        (None, {
            "fields": ("first_name", "last_name"),
            "classes": ("wide",),
            "description": "Enter the details of the new actor."
        }),
    )


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "created_at", "updated_at")
    list_display_links = ("id", "name")
    search_fields = ("name",)
    readonly_fields = ("created_at", "updated_at")
    ordering = ("name",)
    list_per_page = 10

    fieldsets = (
        (None, {
            "fields": ("name",),
            "classes": ("wide",),
            "description": "Enter the details of the genre."
        }),
    )

    add_fieldsets = (
        (None, {
            "fields": ("name",),
            "classes": ("wide",),
            "description": "Enter the details of the new genre."
        }),
    )


@admin.register(Play)
class PlayAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "description", "display_actors", "display_genres", "created_at", "updated_at")
    list_display_links = ("id", "title")
    search_fields = ("title", "actors__first_name", "actors__last_name", "genres__name")
    readonly_fields = ("created_at", "updated_at")
    ordering = ("title",)
    list_per_page = 10

    fieldsets = (
        (None, {
            "fields": ("title", "description"),
            "classes": ("wide",),
            "description": "Enter the details of the play."
        }),
        ("Actors and Genres", {
            "fields": ("actors", "genres"),
            "classes": ("wide",),
            "description": "Select actors and genres associated with the play."
        }),
    )

    add_fieldsets = (
        (None, {
            "fields": ("title", "description"),
            "classes": ("wide",),
            "description": "Enter the details of the new play."
        }),
        ("Actors and Genres", {
            "fields": ("actors", "genres"),
            "classes": ("wide",),
            "description": "Select actors and genres associated with the new play."
        }),
    )

    @admin.display(description="Actors")
    def display_actors(self, obj):
        return ", ".join(
            [f"{actor.first_name} {actor.last_name}" for actor in obj.actors.all()]
        )

    @admin.display(description="Genres")
    def display_genres(self, obj):
        return ", ".join(
            [genre.name for genre in obj.genres.all()]
        )