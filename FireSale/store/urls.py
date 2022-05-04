from django.urls import path
from . import views

urlpatterns = [
    path('itemDetails/', views.itemDetails, name="itemDetails"),
    path('sellProduct/', views.sellProduct, name="sellProduct"),
    path('payment/', views.pay, name="payment"),
    path('browse/', views.browse, name="browseItems")
]
