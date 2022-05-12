from django.forms import ModelForm, widgets
from account.models import *
from django import forms

ratingChoices = [
    ('1', '1 Star'),
    ('2', '2 Star'),
    ('3', '3 Star'),
    ('4', '4 Star'),
    ('5', '5 Star'),
]


class SellerReviewForm(ModelForm):
    class Meta:
        model = SellerRating
        exclude = ['seller']
        widgets = {
            'rating': forms.widgets.RadioSelect(choices=ratingChoices)
        }
