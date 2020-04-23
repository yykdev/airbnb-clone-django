from django.db import models
from django.conf import settings

from django_countries.fields import CountryField
from core import models as core_models

__all__ = (
    'Room',
    'RoomType',
    'Amenity',
    'Facility',
    'HouseRule',
    'Photo',
)


class AbstractItem(core_models.TimeStampedModel):

    """ Abstract Item """

    name = models.CharField(
        max_length=80,
    )

    class Meta:
        abstract = True

    def __str__(self):
        return self.name


class RoomType(AbstractItem):

    """ RoomType Object Definition """

    class Meta:
        verbose_name_plural = 'Room Types'
        ordering = ['-created']


class Amenity(AbstractItem):

    """ Amenity Object Definition """

    class Meta:
        verbose_name_plural = 'Amenities'


class Facility(AbstractItem):

    """ Facility Object Definition """

    class Meta:
        verbose_name_plural = 'Facilities'


class HouseRule(AbstractItem):

    """ HouseRule Object Definition """

    class Meta:
        verbose_name_plural = 'House Rules'


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

    room_type = models.ForeignKey(
        RoomType,
        on_delete=models.SET_NULL,
        null=True,
    )
    amenities = models.ManyToManyField(
        Amenity,
        blank=True,
    )
    facilities = models.ManyToManyField(
        Facility,
        blank=True,
    )
    house_rules = models.ManyToManyField(
        HouseRule,
        blank=True,
    )

    def __str__(self):
        return self.name


class Photo(core_models.TimeStampedModel):
    """ Photo Model Definition """

    caption = models.CharField(
        max_length=80
    )
    file = models.ImageField()
    room = models.ForeignKey(
        Room,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.caption
