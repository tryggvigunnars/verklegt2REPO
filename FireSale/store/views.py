from django.shortcuts import render


# Create your views here.

items = [
    {'img': '', 'productName': 'Bike', 'seller': 'Kalli', 'location': 'Reykjavík', 'price': 3000},
    {'img': '', 'productName': 'Car', 'seller': 'Páll', 'location': 'Reykjavík', 'price': 5000},
    {'img': '', 'productName': 'Scooter', 'seller': 'Nilli', 'location': 'Reykjavík', 'price': 80000}
]

item_details = [
    {'img': '', 'productName': 'Bike', 'seller': 'Kalli', 'location': 'Reykjavík', 'price': 3000}
]


def browse(request):
    return render(request, 'store/product/browsing.html', context={'items': items})


def item(request):
    return render(request, 'store/product/browsingItem.html', context={'items': items})


def itemDetails(request):
    return render(request, 'store/product/itemDetails.html', context={'item_details': item_details,
                                                                       'items': items})


def sellProduct(request):
    return render(request, 'store/product/sell.html')


def pay(request):
    return render(request, 'store/payment/pay.html')


def reviewPayment(request):
    return render(request, 'store/payment/reviewPayment.html')


def rateSeller(request):
    return render(request, 'store/payment/sellerRating.html')

