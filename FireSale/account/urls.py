from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from . import views

urlpatterns = [
    path('login', LoginView.as_view(template_name='Account/login.html'), name='login'),
    path('', LoginView.as_view(template_name='Account/login.html'), name='login'),
    path('logout', LogoutView.as_view(next_page='login'), name='logout'),
    path('register/', views.register, name="register"),
    path('profile/', views.profile, name='profile'),
    path('editprofile/', views.editprofile, name='editprofile'),
    path('myListings/', views.myListings, name="myListings"),
    path('myListings/<int:id>', views.myListingDetails, name="myListingDetails"),
    path('myBids/', views.myBids, name="myBids"),
    path('deleteListing/<int:id>', views.deleteListing, name="deleteListing"),
    path('notifications/', views.getNotifications, name="notifications"),

    path('payment/rateSeller/<int:id>', views.rateSeller, name="rateSeller"),
    path('payment/rateseller/deleteFunc/<int:id>', views.deleteAfterPayment, name="deleteAfterPayment"),

]
