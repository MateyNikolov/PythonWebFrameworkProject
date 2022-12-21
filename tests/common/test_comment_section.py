from django.urls import reverse

from finalExamProject.common.models import Comment
from tests.base.base_file import SkinsTestCase


class CommentTests(SkinsTestCase):

    def test_comment_view_returns_empty_list__when_no_comments_in_DB(self):
        self.client.force_login(self.user)
        response = self.client.get(reverse('share experience'))
        self.assertListEmpty([], response.context['comments'])

    def test_comment_view_returns_comments__when_some_comments_in_DB(self):
        self.client.force_login(self.user)
        Comment.objects.bulk_create([
            Comment(
                comment_text=f'Comment{i}',
                user_id=self.user.pk
            ) for i in range(1, 6)
        ])
        response = self.client.get(reverse('share experience'))
        self.assertEqual(5, len(response.context['comments']))

    def test_comment_section_doesnt_show__when_user_not_logged_in(self):
        response = self.client.get(reverse('share experience'))
        self.assertEqual(None, response.context)