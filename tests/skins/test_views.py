from django.test import TestCase

from django.contrib.auth import get_user_model
from django.urls import reverse

from finalExamProject.skins.models import Guns
from tests.base.base_file import SkinsTestCase

UserModel = get_user_model()


class ViewsTests(SkinsTestCase):

    def test_if_home_page_opens_with_200_code(self):
        response = self.client.get('')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateNotUsed(response, 'testing/home_page.html')

    def test_rifles_list_view__when_no_rifles__expect_empty_list(self):
        response = self.client.get(reverse('all rifles'))
        self.assertListEmpty([], response.context['object_list'])

    def test_agents_list_view__when_no_agents__expect_empty_list(self):
        response = self.client.get(reverse('all agents'))
        self.assertListEmpty([], response.context['object_list'])

    def test_containers_list_view__when_no_containers__expect_empty_list(self):
        response = self.client.get(reverse('all containers'))
        self.assertListEmpty([], response.context['object_list'])

    def test_rifles_list_view__when_query_is_not_empty__expect_query_count(self):
        guns_count = 3
        Guns.objects.bulk_create([
            Guns(
                name=f'Gun {i}',
                description=f'Desc {i}',
                type='pistol',
                price=f'{i + 1}',
                picture=f'123{i}.jpg',
                user_id=self.user.pk
            ) for i in range(1, guns_count + 1)
        ])
        response = self.client.get(reverse('all rifles'))
        self.assertEqual(3, len(response.context['object_list']))
