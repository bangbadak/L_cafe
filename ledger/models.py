from django.db import models
from datetime import datetime
from django.utils.dateformat import DateFormat

# Create your models here.
class Ledger(models.Model):
    identification = models.CharField(default=DateFormat(datetime.now()).format('Ymd'), max_length=8)
    personInCharge = models.CharField(max_length=5)
    date = models.DateTimeField(auto_now_add=True, blank=True)


    def __str__(self):
        return DateFormat(datetime.now()).format('Y년m월d일')
    
    def get_absolute_url(read):
        return f'/edit_ledger/read/{read}/'



class Order(models.Model):
    identification = models.IntegerField()
    number = models.IntegerField()
    orderer = models.CharField(max_length=5)
    item = models.CharField(max_length=20)
    count = models.IntegerField()