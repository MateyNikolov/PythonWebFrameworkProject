from django.urls import path, include

from finalExamProject.skins.views import ShowAllSkinsView, ShowAllRiflesView, AddSkinView, AddRifleView, AddAgentView, \
    AddContainerView, ShowAllAgentsView, ShowAllContainersView, MySkinsView, ShowGunDetailsView, ShowAgentDetailsView, \
    ShowContainerDetailsView

urlpatterns = [
    path('all-skins/', ShowAllSkinsView.as_view(), name='all skins'),
    path('all-rifles/', ShowAllRiflesView.as_view(), name='all rifles'),
    path('all-agents/', ShowAllAgentsView.as_view(), name='all agents'),
    path('all-containers/', ShowAllContainersView.as_view(), name='all containers'),
    path('my-skins/', MySkinsView.as_view(), name='my skins'),
    path('add-skin/', include([
        path('', AddSkinView.as_view(), name='add skin'),
        path('rifle/', AddRifleView.as_view(), name='add rifle'),
        path('agent/', AddAgentView.as_view(), name='add agent'),
        path('container/', AddContainerView.as_view(), name='add container'),
    ])),
    path('details/', include([
        path('gun/<int:pk>/', ShowGunDetailsView.as_view(), name='gun details'),
        path('agent/<int:pk>/', ShowAgentDetailsView.as_view(), name='agent details'),
        path('container/<int:pk>/', ShowContainerDetailsView.as_view(), name='container details'),
    ]))
    ]
