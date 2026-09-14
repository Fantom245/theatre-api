from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from django.contrib.auth import get_user_model


User = get_user_model()


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    list_display = ("id", "email", "username", "first_name", "last_name", "is_staff", "is_active")
    list_display_links = ("id", "email")
    search_fields = ("id", "email", "username", "first_name", "last_name")
    list_filter = ("is_staff", "is_active", "is_superuser")
    ordering = ("email",)
    list_per_page = 10
    filter_horizontal = ("groups", "user_permissions")

    fieldsets = (
        (None, {
            "fields": ("email", "password"),
            "classes": ("wide",),
            "description": "Use a strong password for security."
        }),
        ("Personal Info", {
            "fields": ("username", "first_name", "last_name"),
            "classes": ("wide",),
            "description": "Enter the user's personal information."
        }),
        ("Permissions", {
            "fields": (
                "is_staff",
                "is_active",
                "is_superuser",
                "groups",
                "user_permissions"
            ),
            "classes": ("collapse",),
            "description": "Manage the user's permissions and access levels."
        })
    )

    add_fieldsets = (
        (None, {
            "fields": ("email", "password1", "password2"),
            "classes": ("wide",)
        }),
        ("Personal Info", {
            "fields": ("username", "first_name", "last_name"),
            "classes": ("wide",)
        }),
        ("Permissions", {
            "fields": (
                "is_staff",
                "is_active",
                "is_superuser",
            ),
            "classes": ("collapse",)
        })
    )