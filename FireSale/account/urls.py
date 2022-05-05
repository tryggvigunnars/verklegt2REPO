from django.urls import path
from . import views

urlpatterns = [
    path('', views.login, name="login"),
    path('register/', views.register, name="register"),
    path('profile/', views.profile, name='profile'),
    path('editprofile/', views.editprofile, name='editProfile'),
]
