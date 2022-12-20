from django.urls import path, include

from finalExamProject.profile_app.views import ShowProfileView, EditProfileView, DeleteProfileView, ChangePassword, \
    SignUpEmailNotificationPage

urlpatterns = [
    path('', include([
        path('show-profile/<int:pk>/', ShowProfileView.as_view(), name='show profile'),
        path('edit-profile/<int:pk>/', EditProfileView.as_view(), name='edit profile'),
        path('change-password/', ChangePassword.as_view(), name='change password'),
        path('delete-profile/<int:pk>/', DeleteProfileView.as_view(), name='delete profile'),
        path('email-sign-up/', SignUpEmailNotificationPage.as_view(), name='email sign up'),
    ]))

]
