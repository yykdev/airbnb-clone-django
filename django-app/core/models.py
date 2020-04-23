from django.db import models


class TimeStampedModel(models.Model):

    """ Abstract Time Stamped Mdel """

    created = models.DateTimeField()
    updated = models.DateTimeField()

    class Meta:
        abstract = True
