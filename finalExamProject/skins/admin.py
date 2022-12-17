from django.contrib import admin

from finalExamProject.skins.models import Guns, Agent, Container


@admin.register(Guns)
class RifleAdmin(admin.ModelAdmin):
    list_display = ['user', 'name', 'type', 'price', 'picture']


@admin.register(Agent)
class AgentAdmin(admin.ModelAdmin):
    list_display = ['user', 'name', 'side', 'price', 'picture']


@admin.register(Container)
class RifleAdmin(admin.ModelAdmin):
    list_display = ['user', 'name', 'type', 'price', 'picture']