from django.urls import path
from . import views

urlpatterns = [
    path('', views.loginIndex, name="loginIndex"),
    path('registers/', views.registerIndex, name="loginIndex"),
]
