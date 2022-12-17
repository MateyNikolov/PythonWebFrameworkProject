from django.urls import path, include

from finalExamProject.skins.views import ShowAllSkinsView, ShowAllRiflesView, AddSkinView, AddRifleView, AddAgentView, \
    AddContainerView, ShowAllAgentsView, ShowAllContainersView, MySkinsView, ShowRifleDetailsView, ShowAgentDetailsView, \
    ShowContainerDetailsView, RifleEditView, RifleDeleteView, AgentEditView, AgentDeleteView, ContainerEditView, \
    ContainerDeleteView

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
        path('rifle/', include([
            path('details/<int:pk>/', ShowRifleDetailsView.as_view(), name='rifle details'),
            path('edit/<int:pk>/', RifleEditView.as_view(), name='rifle edit'),
            path('delete/<int:pk>/', RifleDeleteView.as_view(), name='rifle delete'),
        ])),
        path('agent/', include([
            path('details/<int:pk>/', ShowAgentDetailsView.as_view(), name='agent details'),
            path('edit/<int:pk>/', AgentEditView.as_view(), name='agent edit'),
            path('delete/<int:pk>/', AgentDeleteView.as_view(), name='agent delete'),
        ])),
        path('container/<int:pk>/', ShowContainerDetailsView.as_view(), name='container details'),
        path('', include([
            path('edit/<int:pk>/', ContainerEditView.as_view(), name='container edit'),
            path('delete/<int:pk>/', ContainerDeleteView.as_view(), name='container delete'),
        ])),
    ]))
]
