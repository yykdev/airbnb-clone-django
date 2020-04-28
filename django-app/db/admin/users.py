from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from db import models


@admin.register(models.User)
class CustomUserAdmin(UserAdmin):

    fieldsets = UserAdmin.fieldsets + (
        (
            'Profile',
            {
                'fields': (
                    'avatar',
                    'gender',
                    'bio',
                    'birthdate',
                    'language',
                    'currency',
                    'is_superhost',
                )
            }
        ),
    )

    list_filter = UserAdmin.list_filter + (
        "is_superhost",
    )

    list_display = (
        "username",
        "first_name",
        "last_name",
        "email",
        "is_active",
        "language",
        "currency",
        "is_superhost",
        "is_staff",
        "is_superuser",
    )
