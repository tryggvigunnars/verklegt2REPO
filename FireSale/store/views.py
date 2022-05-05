from django.shortcuts import render


# Create your views here.

item_details = [
    {'img': '', 'productName': 'Rocketlauncher', 'seller': 'jon', 'condition': 'bad', 'highestOffer': 12345, 'location': 'Tannes', 'price': 4000000,
     'description': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Ut semper at mauris id sodales. Aenean quis gravida libero. Suspendisse eu mauris a mauris pharetra blandit eget nec magna. Maecenas eleifend sapien risus. Suspendisse venenatis mi ac ipsum vehicula viverra. Nullam a luctus sem, sed faucibus sem. Cras faucibus odio ac commodo condimentum. Nulla lobortis odio eu eros egestas, ut condimentum est ornare.'}
]

item_info = [
    {'img': '', 'productName': 'Bike', 'seller': 'Kalli', 'location': 'Reykjavík', 'price': 3000},
    {'img': '', 'productName': 'Car', 'seller': 'Páll', 'location': 'Reykjavík', 'price': 5000},
    {'img': '', 'productName': 'Scooter', 'seller': 'Nilli', 'location': 'Reykjavík', 'price': 80000}
]


def browse(request):
        return render(request,'store/product/item.html', context={'item_info': item_info, 'extension': 'store/product/browsing.html'})


def itemDetails(request):
    return render(request, 'store/product/item.html', context={'item_info': item_info, 'item_details': item_details,'extension': 'store/product/itemDetails.html'})


def sellProduct(request):
    return render(request, 'store/product/sell.html')


def pay(request):
    return render(request, 'store/payment/pay.html')


def reviewPayment(request):
    return render(request, 'store/payment/reviewPayment.html')

