from django.conf import settings
from django.db import models
from core import models as core_models

__all__ = (
    'Conversation',
    'Message',
)


class Conversation(core_models.TimeStampedModel):

    participants = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        blank=True,
    )

    def __str__(self):
        return str(self.created)


class Message(core_models.TimeStampedModel):

    message = models.TextField()
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    conversation = models.ForeignKey(
        Conversation,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return "{} says: {}".format(self.user, self.message)
