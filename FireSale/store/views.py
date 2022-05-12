from django.shortcuts import render, redirect
from account.models import *
from django.shortcuts import get_object_or_404
from account.models import Item
from store.forms import bidsForm
from store.forms.item_form import ItemCreateForm
from store.forms.bidsForm import sendOfferForm
from store.forms.paymentForm import PaymentForm
from django.http import JsonResponse
from django.db.models import Avg, Max, Min
from django.contrib.auth.decorators import login_required
from store.models import *
# Create your views here.

def browse(request):
    if 'order_by' in request.GET:
        order_by_value = request.GET['order_by']
        ordered_items = Item.objects.all().exclude(accepted=True).order_by(str(order_by_value))
        things = [{
            'id': x.id,
            'name': x.item_name,
            'image': x.itemimage_set.first().img if x.itemimage_set.first() is not None else '',
            'user': x.user.username,
            'location': x.location,
            'price': x.price
        } for x in ordered_items]
        return JsonResponse({'data': things})
    if 'search_filter' in request.GET:
        search_filter = request.GET['search_filter']
        filtered_list = Item.objects.filter(item_name__icontains=search_filter).exclude(accepted=True)
        things = [ {
            'id': x.id,
            'name': x.item_name,
            'image': x.itemimage_set.first().img if x.itemimage_set.first() is not None else '',
            'user': x.user.username,
            'location': x.location,
            'price': x.price
        } for x in filtered_list]
        if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
            return JsonResponse({ 'data': things })
        else:
            return render(request, 'store/product/browsing.html', {
                'items': filtered_list
            })
    items = {'items': Item.objects.all().exclude(accepted=True)} #þurfum að breyta í html
    return render(request, 'store/product/browsing.html', items)


def item(request):
    return render(request, 'store/product/browsingItem.html', context={'items': items})


def itemDetails(request, id):
    item = get_object_or_404(Item, pk=id)
    itemName = item.item_name[:3].lower()
    form = sendOfferForm(initial={
        'item': item
    })
    bids = Bids.objects.filter(item_id=id)
    highest_offer = bids.aggregate(Max('amount'))
    context = { 'item': item, 'items': Item.objects.filter(item_name__contains=itemName).exclude(pk=id), 'form': form, 'highest_offer': highest_offer}
    return render(request, 'store/product/itemDetails.html', context)


@login_required
def sellProduct(request):
    return render(request, 'store/product/sell2.html')


@login_required
def pay(request):
    return render(request, 'store/payment/pay.html')


def insertPaymentInfo(request, id):
    bid = get_object_or_404(Bids, pk=id)
    pay = Payment.objects.filter(user=request.user).first()
    if pay:
        if request.method == 'POST':
                form = PaymentForm(instance=pay, data=request.POST)
                if form.is_valid():
                    pay = form.save(commit=False)
                    pay.user = request.user
                    pay.save()
                    return redirect('reviewPayment', pay.id)
        else:
            return render(request, 'store/payment/pay.html', {'form': PaymentForm(instance=pay), 'bid': bid})
    else:
        if request.method == 'POST':
            form = PaymentForm(request.POST)
            if form.is_valid():
                pay = form.save(commit=False)
                pay.user = request.user
                pay.bid = bid
                pay.save()
                return redirect('reviewPayment', pay.id)
        else:
            form = PaymentForm()
            return render(request, 'store/payment/pay.html', {'form': form, 'bid': bid})




def reviewPayment(request, id):
    payment = get_object_or_404(Payment, pk=id)
    return render(request, "store/payment/reviewPayment.html", {'payment': payment})


@login_required
def rateSeller(request):
    return render(request, 'store/payment/sellerRating.html')



@login_required
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


@login_required
def sendOffer(request):
    if request.method == 'POST':
        form = sendOfferForm(data=request.POST)
        if form.is_valid():
            bid = form.save(commit=False)
            bid.user = request.user
            bid.save()
            return redirect('browseItems')


def deletePaidListing(request, id):
    listing = get_object_or_404(Item, pk=id)
    listing.delete()
    return redirect('rateSeller')


def acceptBid(request, id):
    bid = get_object_or_404(Bids, pk=id)
    item = get_object_or_404(Item, pk=bid.item_id)
    bids = Bids.objects.filter(item_id=item.id)
    for b in bids:
        b.status = get_object_or_404(Status, pk=2)
        b.save()
    bid.status = get_object_or_404(Status, pk=3)
    item.accepted = True
    bid.save()
    item.save()
    return redirect('myListingDetails', bid.item_id)


def declineOffer(request, id):
    bid = get_object_or_404(Bids, pk=id)
    bid.status = get_object_or_404(Status, pk=2)
    bid.save()
    return redirect('myListingDetails', bid.item_id)




