import uuid

from django.conf import settings
from django.core.mail import send_mail
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.template.loader import render_to_string
from django.utils.html import strip_tags

from utils import Constant

__all__ = (
    'User',
)


class User(AbstractUser):

    """ Custom User Model """

    avatar = models.ImageField(
        max_length=255,
        upload_to="avatar/%Y/%m/%d",
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
        null=True,
    )
    language = models.CharField(
        choices=Constant.LANGUAGE_CHOICES,
        default=Constant.LANGUAGE_KOREAN,
        max_length=2,
        blank=True,
    )
    currency = models.CharField(
        choices=Constant.CURRENCY_CHOICES,
        default=Constant.CURRENCY_KRW,
        max_length=3,
        blank=True,
    )
    is_superhost = models.BooleanField(
        default=False,
    )
    email_verified = models.BooleanField(
        default=False,
    )
    email_secret = models.CharField(
        max_length=120,
        default="",
    )

    def verify_email(self):
        if self.email_verified is False:
            secret = uuid.uuid4().hex[:20]
            self.email_secret = secret
            html_message = render_to_string('emails/verify_email.html', context={"secret": secret})
            send_mail(
                "Verify Airbnb Account",
                strip_tags(html_message),
                settings.EMAIL_FROM,
                [self.email],
                fail_silently=False,
                html_message=html_message,
            )
            self.save()
        return
