
from django.urls import path
from users import views

urlpatterns = [
    path('', views.users_collection, name='users_collection'),  # GET/POST /users/
    path('<str:username>/', views.user_detail, name='user_detail'), # GET/PUT/DELETE /users/<username>/
]





