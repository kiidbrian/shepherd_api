from django.urls import path
from api import views

url_pattern = [
    path('users/', views.user_list),
    path('users/<int:pk>', views.user_detail)
]