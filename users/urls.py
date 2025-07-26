from django.urls import path
from users import views

urlpatterns = [
    path('users/', views.add_user, name='add_user'),
    path('users/<str:username>/', views.update_user, name='update_user'),
    path('users/', views.list_users, name='list_users'),
    path('users/<str:username>/', views.get_user, name='get_user'),
   
    ]





