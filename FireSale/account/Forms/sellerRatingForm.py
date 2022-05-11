from django.forms import ModelForm, widgets
from account.models import *
from django import forms

ratingChoices = [
    ('1', '1 Star'),
    ('1', '2 Star'),
    ('1', '3 Star'),
    ('1', '4 Star'),
    ('1', '5 Star'),
]

class SellerReviewForm(ModelForm):
    class Meta:
        model = Rating
        exclude = ['Seller']
        widgets = {
            'rating': forms.CharField(label='How would you rate this seller?', widget=forms.RadioSelect(choices = ratingChoices))
        }
