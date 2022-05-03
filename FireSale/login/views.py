from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def loginIndex(request):
    return render(request, 'Login/loginIndex.html')

def registerIndex(request):
    return render(request, 'Login/registerIndex.html')