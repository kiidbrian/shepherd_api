from django.urls import path
from api import views

urlpatterns = [
    path('users/', views.user_list),
    path('users/<int:pk>', views.user_detail)
    path('members/', views.member_list),
    path('members/<int:pk>', views.member_detail)
]