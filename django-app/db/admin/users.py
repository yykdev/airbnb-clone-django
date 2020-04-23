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
