from django.db import models
from datetime import datetime
from django.utils.dateformat import DateFormat

# Create your models here.
class Ledger(models.Model):
    identification = models.CharField(default=DateFormat(datetime.now()).format('Y년m월d일'), max_length=16)
    personInCharge = models.CharField(max_length=5)
    date = models.DateTimeField(auto_now_add=True, blank=True)


    def __str__(self):
        return DateFormat(datetime.now()).format('Y년m월d일')
    
    def get_absolute_url_read(self):
        return f'/edit_ledger/read/{self.pk}/'
    
    def get_absolute_url_update(self):
        return f'/edit_ledger/update/{self.pk}/'



class Order(models.Model):
    identification = models.CharField(default=DateFormat(datetime.now()).format('Y년m월d일'), max_length=16)

    number = models.IntegerField(default=1)
    orderer = models.CharField(max_length=5)
    item = models.CharField(max_length=20)
    count = models.IntegerField(default=1)