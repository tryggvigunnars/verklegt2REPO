from django.db import models
from django.contrib.auth.models import User
from account.models import *


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


class Orders(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)



