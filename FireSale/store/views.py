from django.shortcuts import render


# Create your views here.

def item(request):
        return render(request,'store/product/item.html')


def itemDetails(request):
    return render(request, 'store/product/itemDetails.html')

def sellProduct(request):
    return render(request, 'store/product/sell.html')

def pay(request):
    return render(request, 'store/payment/pay.html')
