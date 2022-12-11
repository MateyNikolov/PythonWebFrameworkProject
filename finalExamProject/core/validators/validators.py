from django.core import exceptions


def validate_age_is_above_16(value):
    if value < 16:
        raise exceptions.ValidationError('You must be at least 16 Years old!')