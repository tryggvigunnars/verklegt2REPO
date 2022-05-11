from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.db.models import Max
from django. shortcuts import render, redirect
from account.Forms.profileForm import ProfileForm
from account.models import Profile, Item
from store.models import Bids
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
# Create your views here.

user_info = [
    {'name': 'Kalli', }
]

def login(request):
    return render(request, 'Account/login.html')


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    return render(request, 'Account/register.html', {
        'form': UserCreationForm()
    })

@login_required
def editprofile(request):
    profile = Profile.objects.filter(user=request.user).first()
    if request.method == 'POST':
        form = ProfileForm(instance=profile, data=request.POST)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()
            return redirect('profile')
    return render(request, 'Account/editprofile.html', {
        'form': ProfileForm(instance=profile)
    })

@login_required
def profile(request):
    context = {'profile': Profile.objects.filter(user=request.user).first()}
    return render(request, 'Account/profile.html', context)


@login_required
def myListings(request):
    context = {'items': Item.objects.filter(user=request.user)}
    return render(request, 'account/myListings.html', context)


@login_required
def myBids(request):
    context = {'bids': Bids.objects.filter(user=request.user)}
    return render(request, 'account/myBids.html', context)


@login_required
def deleteListing(request, id):
    listing = get_object_or_404(Item, pk=id)
    listing.delete()
    return redirect('myListings')



def myListingDetails(request, id):
    item = get_object_or_404(Item, pk=id)
    bids = Bids.objects.filter(item_id=id).exclude(status_id=2).order_by('-amount')
    highest_offer = bids.aggregate(Max('amount'))
    context = { 'item': item, 'bids': bids, 'highest_offer': highest_offer}
    return render(request, 'Account/myListingDetails.html', context)



