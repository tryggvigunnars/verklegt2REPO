from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def login(request):
    return render(request, 'Account/login.html')

def register(request):
    return render(request, 'Account/register.html')

def profile(request):
    return render(request, 'Account/profile.html')
