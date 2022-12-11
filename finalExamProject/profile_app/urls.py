from django.urls import path, include

from finalExamProject.profile_app.views import ShowProfileView, EditProfileView, DeleteProfileView

urlpatterns = [
    path('', include([
        path('show-profile/<int:pk>/', ShowProfileView.as_view(), name='show profile'),
        path('edit-profile/<int:pk>/', EditProfileView.as_view(), name='edit profile'),
        path('delete-profile/<int:pk>/', DeleteProfileView.as_view(), name='delete profile'),
        ]))

]
