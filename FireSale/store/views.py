from django.shortcuts import render, redirect
from account.models import *
from django.shortcuts import get_object_or_404
from store.forms.item_form import ItemCreateForm
from django.http import JsonResponse

# Create your views here.

def browse(request):
    if 'search_filter' in request.GET: #Það verður að bæta við seller og image
        search_filter = request.GET['search_filter']
        filtered_list = Item.objects.filter(item_name__icontains=search_filter)
        things = [ {
            'id': x.id,
            'item_name': x.item_name,
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
