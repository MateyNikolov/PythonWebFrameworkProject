from django.core import exceptions


def validate_age_is_above_16(value):
    if not isinstance(value, int):
        raise exceptions.ValidationError('Value must be number!')
    if value < 16:
        raise exceptions.ValidationError('You must be at least 16 Years old!')