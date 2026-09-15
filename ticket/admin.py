from django.contrib import admin

from .models import Reservation, Ticket


@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "created_at")
    list_display_links = ("id", "user")
    search_fields = ("id", "user__email", "user__username")
    ordering = ("-created_at",)
    readonly_fields = ("created_at",)
    list_per_page = 10

    fieldsets = (
        (None, {
            "fields": ("user",),
            "classes": ("wide",),
            "description": "Select the user who made the reservation."
        }),
    )

    add_fieldsets = (
        (None, {
            "fields": ("user",),
            "classes": ("wide",),
            "description": "Select the user for the new reservation."
        }),
    )


@admin.register(Ticket)
class TicketAdmin(admin.ModelAdmin):
    list_display = ("id", "row", "seat", "performance", "reservation", "created_at", "updated_at")
    list_display_links = ("id",)
    search_fields = ("id", "performance__id", "reservation__id")
    ordering = ("-created_at",)
    readonly_fields = ("created_at", "updated_at")
    list_per_page = 10

    fieldsets = (
        (None, {
            "fields": ("row", "seat", "performance", "reservation"),
            "classes": ("wide",),
            "description": "Enter the seat details and associate it with a performance and reservation."
        }),
    )

    add_fieldsets = (
        (None, {
            "fields": ("row", "seat", "performance", "reservation"),
            "classes": ("wide",),
            "description": "Enter the seat details and associate it with a performance and reservation."
        }),
    )