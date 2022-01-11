from django.contrib import admin
from .models import Ledger, Order, Item

# Register your models here.
admin.site.register(Ledger)
admin.site.register(Order)
admin.site.register(Item)