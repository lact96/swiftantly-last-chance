from django.urls import path, re_path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('workspace_create/', views.workspace_create, name='workspace_create'),
    re_path(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        views.activate, name='activate'),
]
