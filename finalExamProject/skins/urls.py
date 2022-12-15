from django.urls import path, include

from finalExamProject.skins.views import ShowAllSkinsView, ShowAllRiflesView, AddSkinView, AddRifleView, AddAgentView, \
    AddContainerView

urlpatterns = [
    path('all-skins/', ShowAllSkinsView.as_view(), name='all skins'),
    path('all-rifles/', ShowAllRiflesView.as_view(), name='all rifles'),
    path('add-skin/', include([
        path('', AddSkinView.as_view(), name='add skin'),
        path('rifle/', AddRifleView.as_view(), name='add rifle'),
        path('agent/', AddAgentView.as_view(), name='add agent'),
        path('container/', AddContainerView.as_view(), name='add container'),
    ]))]
