from django.contrib import admin

from finalExamProject.common.models import Comment


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['user', 'comment_text', 'picture', 'date' ]
