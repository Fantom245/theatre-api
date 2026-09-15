from django.contrib import admin

from .models import TheatreHall


@admin.register(TheatreHall)
class TheatreHallAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "rows", "seats_in_row", "total_seats", "created_at", "updated_at")
    readonly_fields = ("total_seats", "created_at", "updated_at")
    list_display_links = ("id", "name")
    search_fields = ("id", "name")
    ordering = ("name",)
    list_per_page = 10

    fieldsets = (
        (None, {
            "fields": ("name", "rows", "seats_in_row"),
            "classes": ("wide",),
            "description": "Enter the details of the theatre hall."
        }),
    )

    add_fieldsets = (
        (None, {
            "fields": ("name", "rows", "seats_in_row"),
            "classes": ("wide",),
            "description": "Enter the details of the new theatre hall."
        }),
    )
