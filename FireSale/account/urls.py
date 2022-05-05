from django.urls import path
from . import views

urlpatterns = [
    path('', views.login, name="login"),
    path('register/', views.register, name="register"),
    path('profile/', views.profile, name='profile'),

    path('editprofile/', views.editprofile, name='editprofile'),
    path('myListings/', views.myListings, name="myListings"),
    path('myBids/', views.myBids, name="myBids"),
]
