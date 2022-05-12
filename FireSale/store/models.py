from django.db import models
from django.contrib.auth.models import User
from account.models import *
from django_countries.fields import CountryField


# Create your models here.
class Status(models.Model):
    status = models.CharField(max_length=20)

    def __str__(self):
        return self.status


class Bids(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    amount = models.FloatField()
    status = models.ForeignKey(Status, on_delete=models.CASCADE, default=1)


class Payment(models.Model):
    bid = models.ForeignKey(Bids, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=250)
    city = models.CharField(max_length=250)
    location = models.CharField(max_length=250)
    country = CountryField()
    postalCode = models.IntegerField()
    cardNumber = models.IntegerField()
    cardMonth = models.IntegerField()
    cardYear =  models.IntegerField()
    cardCvv = models.IntegerField()
    cardholderName = models.CharField(max_length=250)






