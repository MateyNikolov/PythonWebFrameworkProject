from enum import Enum

from django.contrib.auth import get_user_model
from django.db import models
from finalExamProject.core.mixins.mixins import ChoicesEnumMixin

UserModel = get_user_model()


class GunsTypes(ChoicesEnumMixin, Enum):
    rifle = 'Rifle'
    pistol = 'Pistol'
    knife = 'Knife'


class ContainerTypes(ChoicesEnumMixin, Enum):
    recoil_case = 'Recoil Case'
    dreams_and_nightmares = 'Dreams and Nightmares'
    clutch_case = 'Clutch Case'
    glove_case = 'Glove Case'
    gamma_2_case = 'Gamma 2 Case'
    fracture_case = 'Fracture Case'
    revolver_case = 'Revolver Case'
    snakebite_case = 'Snakebite Case'


class AgentSides(ChoicesEnumMixin, Enum):
    t_side = 'T Side'
    ct_side = 'CT Side'


class Guns(models.Model):
    MAX_NAME_LENGTH_GUN = 20

    name = models.CharField(
        max_length=MAX_NAME_LENGTH_GUN,
    )

    description = models.TextField()
    type = models.CharField(
        choices=GunsTypes.choices(),
        max_length=GunsTypes.max_len(),
    )
    price = models.PositiveIntegerField()
    picture = models.ImageField(
        upload_to='guns/',
        null=True,
        blank=True,
    )
    user = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
    )


class Container(models.Model):
    MAX_NAME_LENGTH_CONTAINER = 20

    name = models.CharField(
        max_length=MAX_NAME_LENGTH_CONTAINER,
    )

    type = models.CharField(
        choices=ContainerTypes.choices(),
        max_length=ContainerTypes.max_len(),
    )
    description = models.TextField()

    price = models.PositiveIntegerField()
    picture = models.ImageField(
        upload_to='containers/',
        null=True,
        blank=True
    )

    user = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
    )


class Agent(models.Model):
    MAX_NAME_LENGTH_AGENT = 30

    name = models.CharField(
        max_length=MAX_NAME_LENGTH_AGENT,
    )
    description = models.TextField()

    price = models.PositiveIntegerField()
    side = models.CharField(
        choices=AgentSides.choices(),
        max_length=AgentSides.max_len(),
    )
    picture = models.ImageField(
        upload_to='agents/',
        null=True,
        blank=True,
    )

    user = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE
    )
