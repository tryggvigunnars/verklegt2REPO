from django.forms import ModelForm, widgets
from store.models import Bids
from django import forms


class sendOfferForm(ModelForm):
    class Meta:
        model = Bids
        exclude = ['status', 'user']
        widgets = {
            'amount': widgets.NumberInput(attrs={'class': 'form-control'}),
            'item': widgets.HiddenInput()
        }
