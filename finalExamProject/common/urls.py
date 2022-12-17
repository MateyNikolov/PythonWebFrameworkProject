from django.urls import path

from finalExamProject.common.views import ShowHomePageView, ShareExperienceView

urlpatterns = [
    path('', ShowHomePageView.as_view(), name='home'),
    path('share-experience', ShareExperienceView.as_view(), name='share experience'),
]
