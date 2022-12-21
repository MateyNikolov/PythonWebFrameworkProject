from django.contrib.auth import get_user_model
from django.test import TestCase, Client


UserModel = get_user_model()


class BaseTestCase(TestCase):
    USERNAME = 'matey9234'
    EMAIL = 'matey@abv.bg'
    PASSWORD = '123123123d'

    def setUp(self):
        self.user = UserModel.objects.create_user(
            username=BaseTestCase.USERNAME,
            email=BaseTestCase.EMAIL,
            password=BaseTestCase.PASSWORD,
        )
        self.user_is_active = True
        self.user.save()

    def tearDown(self):
        self.user.delete()


class SkinsTestCase(TestCase):
    username = 'matey923'
    email = 'matey123@abv.bg'
    password = '123123123d'

    def assertListEmpty(self, ll, message=None):
        return self.assertEqual([], ll, 'This list is not empty.')

    def setUp(self):
        self.client = Client()
        self.user = UserModel.objects.create_user(
            username=self.username,
            email=self.email,
            password=self.password,
        )
        self.super_user = UserModel.objects.create_superuser(
            username='matey_super1',
            email='mateysuper@abv.bg',
            password='123123123d',
        )
