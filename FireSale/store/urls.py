from django.urls import path
from . import views

urlpatterns = [
    path('<int:id>', views.itemDetails, name="itemDetails"),
    path('sellProduct/', views.createItem, name="sellProduct"),
    path('payment/', views.pay, name="payment"),
    path('', views.browse, name="browseItems"),
    path('payment/review/<int:id>', views.reviewPayment, name="reviewPayment"),
    path('payment/rateSeller/', views.rateSeller, name="rateSeller"),
    path('create_item', views.createItem, name='create_item'),
    path('sendOffer', views.sendOffer, name='sendOffer'),
    path('insertPaymentInfo', views.insertPaymentInfo, name='insertPaymentInfo'),
    path('acceptOffer/<int:id>', views.acceptBid, name='acceptOffer'),
    path('declineOffer/<int:id>', views.declineOffer, name='declineOffer'),
]
