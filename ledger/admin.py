from django.contrib import admin
from .models import Ledger, Order

# Register your models here.
admin.site.register(Ledger)
admin.site.register(Order)