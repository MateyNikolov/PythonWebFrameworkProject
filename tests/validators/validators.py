from unittest import TestCase

from django.core.exceptions import ValidationError

from finalExamProject.core.validators.validators import validate_age_is_above_16


class AgeValidationTest(TestCase):

    def test_age_happy_path_above_16(self):
        validate_age_is_above_16(17)

    def test_age_is_under_16(self):
        with self.assertRaises(ValidationError) as context:
            validate_age_is_above_16(15)

        self.assertIsNotNone(context.exception)

    def test_age_is_16(self):
        validate_age_is_above_16(16)

    def test_age_is_string(self):
        with self.assertRaises(ValidationError) as context:
            validate_age_is_above_16('dasasd')

        self.assertIsNotNone(context.exception)

    def test_age_is_float(self):
        with self.assertRaises(ValidationError) as context:
            validate_age_is_above_16(12.2)

        self.assertIsNotNone(context.exception)