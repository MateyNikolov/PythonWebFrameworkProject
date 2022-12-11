from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('finalExamProject.common.urls')),
    path('', include('finalExamProject.accounts.urls')),
    path('', include('finalExamProject.profile_app.urls')),

]
