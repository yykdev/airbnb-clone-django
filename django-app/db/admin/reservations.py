from django.contrib import admin
from . import models


@admin.register(models.Reservation)
class ReservationsAdmin(admin.ModelAdmin):

    """ ReservationsAdmin Admin Definition """
