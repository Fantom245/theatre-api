from django.contrib import admin

from .models import Performance


@admin.register(Performance)
class PerformanceAdmin(admin.ModelAdmin):
    list_display = ("id", "play", "theatre_hall", "show_time", "created_at", "updated_at")
    list_display_links = ("id", "play")
    search_fields = ("play__title", "theatre_hall__name")
    readonly_fields = ("created_at", "updated_at")
    ordering = ("show_time",)
    list_per_page = 10

    fieldsets = (
        (None, {
            "fields": ("play", "theatre_hall", "show_time"),
            "classes": ("wide",),
            "description": "Enter the details of the performance."
        }),
    )

    add_fieldsets = (
        (None, {
            "fields": ("play", "theatre_hall", "show_time"),
            "classes": ("wide",),
            "description": "Enter the details of the new performance."
        }),
    )