from django.shortcuts import render


# Create your views here.

item_info = [
    {'img': '', 'productName': 'Bike', 'seller': 'Kalli', 'location': 'Reykjavík', 'price': 3000},
    {'img': '', 'productName': 'Car', 'seller': 'Páll', 'location': 'Reykjavík', 'price': 5000},
    {'img': '', 'productName': 'Scooter', 'seller': 'Nilli', 'location': 'Reykjavík', 'price': 80000}
]

def browse(request):
        return render(request,'store/product/item.html', context={'item_info': item_info, 'extension': 'store/product/browsing.html'})

def itemDetails(request):
    return render(request, 'store/product/item.html', context={'item_info': item_info, 'extension': 'store/product/itemDetails.html'})


def sellProduct(request):
    return render(request, 'store/product/sell.html')

def pay(request):
    return render(request, 'store/payment/pay.html')

