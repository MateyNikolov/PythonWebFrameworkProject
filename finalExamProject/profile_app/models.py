from django.contrib.auth import get_user_model
from django.db import models

UserModel = get_user_model()


class Profile(models.Model):
    MAX_NAME_LENGTH = 20
    MAX_STEAMID_LENGTH = 15

    age = models.PositiveIntegerField()
    steam_ID = models.CharField(
        max_length=15
    )
    picture = models.URLField(
        null=True,
        blank=True,
    )

    email_signed = models.BooleanField(
        default=False,
    )

    user = models.OneToOneField(
        UserModel,
        on_delete=models.CASCADE,
        primary_key=True,
    )
