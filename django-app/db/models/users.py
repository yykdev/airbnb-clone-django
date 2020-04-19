from django.contrib.auth.models import AbstractUser
from django.db import models

from utils import Constant

__all__ = (
    'User',
)


class User(AbstractUser):

    """ Custom User Model """

    avatar = models.ImageField(
        blank=True,
    )
    gender = models.CharField(
        choices=Constant.GENDER_CHOICES,
        max_length=10,
        blank=True,
    )
    bio = models.TextField(
        blank=True,
    )
    birthdate = models.DateField(
        blank=True,
    )
    language = models.CharField(
        choices=Constant.LANGUAGE_CHOICES,
        max_length=2,
        blank=True,
    )
    currency = models.CharField(
        choices=Constant.CURRENCY_CHOICES,
        max_length=3,
        blank=True,
    )
    is_superhost = models.BooleanField(
        default=False,
    )
