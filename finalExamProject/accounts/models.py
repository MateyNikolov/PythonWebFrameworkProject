from django.contrib.auth import base_user
import django.contrib.auth.models as auth_models
from django.db import models
from finalExamProject.accounts.managers import MainUserManager


class MainUser(base_user.AbstractBaseUser, auth_models.PermissionsMixin):
    MAX_USERNAME_LENGTH = 20

    username = models.CharField(
        max_length=MAX_USERNAME_LENGTH,
        unique=True,
        null=False,
        blank=False,
        )
    email = models.EmailField(
        blank=False,
        null=False
    )
    is_staff = models.BooleanField(
        default=False
    )
    is_active = models.BooleanField(
        default=True,
        )
    date_joined = models.DateTimeField(
        auto_now_add=True
    )

    USERNAME_FIELD = "username"
    objects = MainUserManager()
