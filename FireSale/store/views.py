from django.shortcuts import render, redirect
from account.models import *
from django.shortcuts import get_object_or_404


# Create your views here.
from store.forms.item_form import ItemCreateForm

"""
items = [
    {'img': '', 'productName': 'Bike', 'seller': 'Kalli', 'location': 'Reykjavík', 'price': 3000},
    {'img': '', 'productName': 'Car', 'seller': 'Páll', 'location': 'Reykjavík', 'price': 5000},
    {'img': '', 'productName': 'Scooter', 'seller': 'Nilli', 'location': 'Reykjavík', 'price': 80000}
]

item_details = [
    {'img': '', 'productName': 'Bike', 'seller': 'Kalli', 'location': 'Reykjavík', 'price': 3000}
]
"""

def browse(request):
    items = {'items': Item.objects.all()}
    return render(request, 'store/product/browsing.html', items)


def item(request):
    return render(request, 'store/product/browsingItem.html', context={'items': items})


def itemDetails(request, id):
    context = { 'item': get_object_or_404(Item, pk=id), 'items': Item.objects.all()}
    return render(request, 'store/product/itemDetails.html', context)


def sellProduct(request):
    return render(request, 'store/product/sell2.html')


def pay(request):
    return render(request, 'store/payment/pay.html')


def reviewPayment(request):
    return render(request, 'store/payment/reviewPayment.html')


def rateSeller(request):
    return render(request, 'store/payment/sellerRating.html')


def createItem(request):
    if request.method == 'POST':
        form = ItemCreateForm(data=request.POST)
        if form.is_valid():
            item = form.save(commit=False)
            item.user = request.user
            item.save()
            item_image = ItemImage(img=request.POST['image'], item=item)
            item_image.save()
            return redirect('browseItems')
    else:
        form = ItemCreateForm()
        return render(request, 'Store/product/sell2.html', {
            'form': form
        })

