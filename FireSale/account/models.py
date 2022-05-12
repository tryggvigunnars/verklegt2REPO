from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserInfo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    phone_number = models.IntegerField()
    address = models.CharField(max_length=255)
    zip = models.IntegerField()
    dob = models.DateField()

    def __str__(self):
        return str(self.user)



class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE) #change to user possibly
    location = models.CharField(max_length=255, blank=True)
    bio = models.CharField(max_length=255, blank=True)
    img = models.CharField(max_length=9999, blank=True)


class Condition(models.Model):
    condition = models.CharField(max_length=255)

    def __str__(self):
        return str(self.condition)


class Item(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    item_name = models.CharField(max_length=255)
    price = models.FloatField()
    condition = models.ForeignKey(Condition, on_delete=models.CASCADE)
    description = models.CharField(max_length=255, blank=True)
    location = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return str(self.item_name)


class ItemImage(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    img = models.CharField(max_length=9999)


class SellerRating(models.Model):
    seller = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField()