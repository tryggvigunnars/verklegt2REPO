from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Orders)
admin.site.register(Status)
admin.site.register(Payment)
admin.site.register(Bids)

