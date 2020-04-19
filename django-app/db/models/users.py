from django.contrib.auth.models import AbstractUser
from django.db import models

from utils import Constant

__all__ = (
    'User',
)


class User(AbstractUser):

    """ Custom User Model """

    avatar = models.ImageField(
        null=True,
        blank=True,
    )
    gender = models.CharField(
        choices=Constant.GENDER_CHOICES,
        max_length=10,
        null=True,
        blank=True,
    )
    bio = models.TextField(
        default='',
        blank=True,
    )
    birthdate = models.DateField(
        null=True,
    )
    language = models.CharField(
        choices=Constant.LANGUAGE_CHOICES,
        max_length=2,
        null=True,
        blank=True,
    )
    currency = models.CharField(
        choices=Constant.CURRENCY_CHOICES,
        max_length=2,
        null=True,
        blank=True,
    )
    is_superhost = models.BooleanField(
        default=False,
    )
