from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('help/', views.request_help, name='request_help'),
    path('success/', views.success, name='success'),
]