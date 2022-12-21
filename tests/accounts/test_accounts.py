from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from finalExamProject.accounts.forms import UserForm
from tests.base.base_file import BaseTestCase

UserModel = get_user_model()


class RegisterFunctionality(TestCase):

    def test_happy_path_register_user(self):
        reg_form = UserForm(
            {'username': 'Makolov',
             'email': 'email1@abv.bg',
             'password1': '123123123d',
             'password2': '123123123d',
             'steam_ID': '123456',
             'age': 22,
             }
        )
        self.assertTrue(reg_form.is_valid())

    def test_not_same_password_register_user(self):
        reg_form = UserForm(
            {'username': 'Makolov',
             'email': 'email1@abv.bg',
             'password1': '123123123d',
             'password2': '123123123',
             'steam_ID': '123456',
             'age': 22,
             }
        )
        self.assertFalse(reg_form.is_valid())

    def test_email_is_not_valid(self):
        reg_form = UserForm(
            {'username': 'Makolov',
             'email': 'email1@abv',
             'password1': '123123123d',
             'password2': '123123123d',
             'steam_ID': '123456',
             'age': 22,
             }
        )
        self.assertFalse(reg_form.is_valid())

    def test_age_is_under_16(self):
        reg_form = UserForm(
            {'username': 'Makolov',
             'email': 'email1@abv.bg',
             'password1': '123123123d',
             'password2': '123123123d',
             'steam_ID': '123456',
             'age': 15,
             }
        )
        self.assertFalse(reg_form.is_valid())

    def test_steam_id_is_empty_field(self):
        reg_form = UserForm(
            {'username': 'Makolov',
             'email': 'email1@abv.bg',
             'password1': '123123123d',
             'password2': '123123123d',
             'steam_ID': '',
             'age': 22,
             }
        )
        self.assertFalse(reg_form.is_valid())


class LogOutViewTest(BaseTestCase):
    def tearDown(self):
        self.user.delete()

    def test_redirect_to_home_after_logout(self):
        is_logged = self.client.login(username=self.USERNAME, email=self.EMAIL, password=self.PASSWORD)
        self.assertTrue(is_logged)
        response = self.client.get(reverse('logout'), follow=False)
        self.assertEqual(302, response.status_code)
        self.assertEqual(reverse('home'), response.headers['location'])
