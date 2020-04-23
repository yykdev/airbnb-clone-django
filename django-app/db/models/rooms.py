from django.db import models
from django.conf import settings

from django_countries.fields import CountryField
from core import models as core_models

__all__ = (
    'Room',
)


class Room(core_models.TimeStampedModel):

    host = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )
    name = models.CharField(
        max_length=40,
        blank=True,
    )
    description = models.TextField(
        blank=True,
    )
    country = CountryField(
        default='KR'
    )
    city = models.CharField(
        max_length=80,
        blank=True,
    )
    price = models.IntegerField(
        default=0,
    )
    address = models.CharField(
        max_length=140,
        blank=True,
    )
    guests = models.IntegerField(
        default=0,
    )
    beds = models.IntegerField(
        default=0,
    )
    bedrooms = models.IntegerField(
        default=0,
    )
    baths = models.IntegerField(
        default=0,
    )
    check_in = models.TimeField(
        null=True,
    )
    check_out = models.TimeField(
        null=True,
    )
    instant_book = models.BooleanField(
        default=False,
    )

    def __str__(self):
        return self.name
