from django.urls import path
from . import views

urlpatterns = [
    path('itemDetails/', views.itemDetails, name="itemDetails"),
    path('sellProduct/', views.sellProduct, name="sellProduct"),
    path('payment/', views.pay, name="payment"),
    path('', views.browse, name="browseItems"),
    path('payment/review/', views.reviewPayment, name="reviewPayment"),
    path('payment/rateSeller/', views.rateSeller, name="rateSeller")
]
