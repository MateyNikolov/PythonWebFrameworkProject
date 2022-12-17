from django.contrib import admin

from finalExamProject.profile_app.models import Profile


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'age', 'steam_ID', 'picture']
