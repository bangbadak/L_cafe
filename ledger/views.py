from django.shortcuts import render
from .models import Ledger, Order

# Create your views here.
def index(request):

    return render(
        request,
        'index.html',
    )

def create(request):
    return render(
        request,
        'ledger/create.html',
    )


def read(request):

    ledgers = Ledger.objects.all()
    # orders = Order.objects.all()
    
    return render(
        request,
        'read.html',
        {
            'ledger': ledgers,
            # 'order': orders,

        },
    )

def read_single_ledger(request, read):
    page_num = {
        'page_num': read,
    }
    return render(
        request, 
        'read_single_ledger.html',
        page_num,
    )

# def update(request):


# def update_item(request)