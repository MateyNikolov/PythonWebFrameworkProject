from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('finalExamProject.common.urls')),
    path('auth/', include('finalExamProject.accounts.urls')),
    path('profile/', include('finalExamProject.profile_app.urls')),
    path('skins/', include('finalExamProject.skins.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


handler500 = 'finalExamProject.common.handlers.handler500'
handler404 = 'finalExamProject.common.handlers.handler404'
handler403 = 'finalExamProject.common.handlers.handler403'
