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
        return str(self.phone_number)


class Profile(models.Model):
    name = models.ForeignKey(User, on_delete=models.CASCADE)
    location = models.CharField(max_length=255, blank=True)
    bio = models.CharField(max_length=255)
    img = models.CharField(max_length=9999)


class Item(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    item_name = models.CharField(max_length=255)
    price = models.FloatField()
    condition = models.CharField(max_length=255)
    description = models.CharField(max_length=255, blank=True)
    location = models.CharField(max_length=255, blank=True)


class ItemImage(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    img = models.CharField(max_length=9999)


class Rating(models.Model):
    User = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField()



