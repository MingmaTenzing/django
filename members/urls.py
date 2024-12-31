from django.urls import path
from . import views
urlpatterns = [
    path('', views.main_page, name='main'),
    path('testing/', views.testing, name='testing'),
    path('members/', views.members, name="members"),
    path('users/', views.users, name='users'),
    path('members/details/<int:id>', views.member_details, name="details")
]