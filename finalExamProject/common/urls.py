from django.urls import path

from finalExamProject.common.views import show_this_page

urlpatterns = [
    path('', show_this_page, name='home')
]