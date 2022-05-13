from django.forms import ModelForm, widgets
from account.models import Item
from django import forms


class ItemCreateForm(ModelForm):
    first_image = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    second_image = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = Item
        exclude = ['id', 'user', 'accepted']
        widgets = {
            'item_name': widgets.TextInput(attrs={'class': 'form-control'}),
            'price': widgets.NumberInput(attrs={'class': 'form-control'}),
            'condition': widgets.Select(attrs={'class': 'form-control'}),
            'description': widgets.TextInput(attrs={'class': 'form-control'}),
            'location': widgets.TextInput(attrs={'class': 'form-control'})
        }


