from django.urls import path
from . import views_home

urlpatterns = [
    path('', views_home.home, name='home'),
    path('register/', views_home.register, name='register'),
]
