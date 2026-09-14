from django.db import models
from django.contrib.auth.models import BaseUserManager

from django.contrib.auth.models import AbstractUser


class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("Email is required")

        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)

        return self.create_user(email, password, **extra_fields)


class User(AbstractUser):
    email = models.EmailField(unique=True, help_text="User email address")
    first_name = models.CharField(max_length=150, help_text="User first name")
    last_name = models.CharField(max_length=150, help_text="User last name")

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    objects = CustomUserManager()

    class Meta:
        verbose_name = "user"
        verbose_name_plural = "users"
        ordering = ["username", "email"]

    def __str__(self):
        return f"Email: {self.email}, Username: {self.username}, Full Name: {self.get_full_name()}"
