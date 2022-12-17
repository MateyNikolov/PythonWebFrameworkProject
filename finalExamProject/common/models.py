from django.contrib.auth import get_user_model
from django.db import models

from finalExamProject.profile_app.models import Profile

UserModel = get_user_model()


class Comment(models.Model):
    MAX_COMMENT_LENGTH = 400

    comment_text = models.TextField(
        max_length=MAX_COMMENT_LENGTH,
        blank=False,
        null=False,
    )

    date = models.DateTimeField(auto_now_add=True, blank=True)

    user = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE
    )

    picture = models.URLField(
        null=True
    )

