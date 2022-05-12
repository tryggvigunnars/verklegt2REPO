from django.forms import ModelForm, widgets
from store.models import *
from django import forms

class PaymentForm(ModelForm):
    class Meta:
        model = Payment
        exclude = ['id', 'bid', 'user']
        widgets = {
            'address': widgets.TextInput(attrs={'class': 'form-control'}),
            'city': widgets.TextInput(attrs={'class': 'form-control'}),
            'location': widgets.TextInput(attrs={'class': 'form-control'}),
            'country': widgets.Select(attrs={'class': 'form-control'}),
            'postalCode': widgets.NumberInput(attrs={'class': 'form-control'}),
            'cardNumber': widgets.NumberInput(attrs={'class': 'form-control'}),
            'cardMonth': widgets.NumberInput(attrs={'class': 'form-control'}),
            'cardYear': widgets.NumberInput(attrs={'class': 'form-control'}),
            'cardCvv': widgets.NumberInput(attrs={'class': 'form-control'}),
            'cardHolderName': widgets.TextInput(attrs={'class': 'form-control'}),
        }
