from django.db import models
from django.contrib.auth.models import User
from account.models import *


# Create your models here.
#status tafla
class Bids(models.Model): # skoða
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    amount = models.FloatField()# bæta við foreign key á status


class Orders(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)



