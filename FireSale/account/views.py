
from django.contrib. auth. forms import UserCreationForm
from django. shortcuts import render, redirect
from django.http import HttpResponse
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
    return render(request, 'Account/register2.html', {
        'form': UserCreationForm()
    })

def profile(request):
    return render(request, 'Account/profile.html')

def editprofile(request):
    return render(request, 'Account/editprofile.html')

def myListings(request):
    return render(request, 'account/myListings.html')

def myBids(request):
    return render(request, 'account/myBids.html')



