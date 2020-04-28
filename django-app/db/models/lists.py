from django.conf import settings
from django.db import models
from core import models as core_models
from db.models import Room

__all__ = (
    'List',
)


class List(core_models.TimeStampedModel):

    """ List Model Definition """

    name = models.CharField(
        max_length=80,
    )

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    rooms = models.ManyToManyField(
        Room,
        blank=True,
        related_name="rooms",
    )

    def __str__(self):
        return self.name

    def count_rooms(self):

        return self.rooms.count()

    count_rooms.short_description = "Number of Rooms"
