from django.urls import path, re_path, include
from . import views
from django.contrib.auth import views as auth_views
from rest_framework.routers import DefaultRouter

app_name = 'workspace'

urlpatterns = [
    path('register/', views.register, name='register'),
    re_path(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        views.activate, name='activate'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('email_dashboard/', views.email_dashboard, name='email_dashboard'),

]


