from django.contrib import admin
from . import models


@admin.register(models.Review)
class PhotoAdmin(admin.ModelAdmin):

    list_display = (
        "__str__",
        "rating_average",
    )
