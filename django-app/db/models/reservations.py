from django.conf import settings
from django.db import models
from core import models as core_models
from db.models import Room
from utils import Constant

__all__ = (
    'Reservation',
)


class Reservation(core_models.TimeStampedModel):

    """ Reservation Model Definition """

    status = models.CharField(
        max_length=12,
        choices=Constant.STATUS_CHOICES,
        default=Constant.STATUS_PENDING,
    )
    check_in = models.DateField()
    check_out = models.DateField()

    guest = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    room = models.ForeignKey(
        Room,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return "{} - {}".format(self.room, self.check_in)
