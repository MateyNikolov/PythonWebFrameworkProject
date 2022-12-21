from django.core.exceptions import ValidationError
from django.urls import reverse, reverse_lazy

from finalExamProject.profile_app.models import Profile
from tests.base.base_file import BaseTestCase


class ProfileTests(BaseTestCase):

    def test_profile_has_the_right_age(self):

        Profile.objects.create(
            steam_ID='123456',
            picture=None,
            user_id=self.user.pk,
            age=21,
            email_signed=False
        )
        user = Profile.objects.get(pk=self.user.pk)
        self.assertEqual(21, user.age)

    def test_profile_has_the_right_steam_ID(self):

        Profile.objects.create(
            steam_ID='123456',
            picture=None,
            user_id=self.user.pk,
            age=21,
            email_signed=False
        )
        user = Profile.objects.get(pk=self.user.pk)
        self.assertEqual('123456', user.steam_ID)

    def test_profile_is_not_signed_in_for_notifications(self):

        Profile.objects.create(
            steam_ID='123456',
            picture=None,
            user_id=self.user.pk,
            age=21,
            email_signed=False
        )
        user = Profile.objects.get(pk=self.user.pk)
        self.assertEqual(False, user.email_signed)

    def test_show_profile_page(self):
        self.client.force_login(self.user)
        user = Profile.objects.create(
            steam_ID='123456',
            picture=None,
            user_id=self.user.pk,
            age=21,
            email_signed=False
        )
        response = self.client.get(reverse('show profile', kwargs={'pk': self.user.pk}))
        self.assertEqual(response.context['object'], user)

