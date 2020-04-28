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
        related_name='conversation',
    )

    def __str__(self):

        usernames = []

        for user in self.participants.all():

            usernames.append(user.username)

        return ", ".join(usernames)

    def count_messages(self):

        return self.messages.count()

    count_messages.short_description = "Number of Message"

    def count_participants(self):

        return self.participants.count()

        count_participants.short_description = "Number of participants"


class Message(core_models.TimeStampedModel):

    message = models.TextField()
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='messages',
    )
    conversation = models.ForeignKey(
        Conversation,
        on_delete=models.CASCADE,
        related_name='messages',
    )

    def __str__(self):
        return "{} says: {}".format(self.user, self.message)
