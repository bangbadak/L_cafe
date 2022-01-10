from django.shortcuts import get_object_or_404, render
from .models import Ledger, Order

def index(request):

    return render(
        request,
        'ledger/index.html',
    )


def ledgers(request):

    ledgers = Ledger.objects.all()

    return render(
        request,
        'ledger/ledgers.html',
        {
            'ledger': ledgers,
        }
    )

def single_ledger(request, pk):

    id = Ledger.objects.get(pk=pk)
    order_list = Order.objects.all()
    return render(
        request,
        'ledger/single_ledger.html',
        {
            'order_list': order_list,
            'id': id,
            'pk': pk,
        },
    )

def single_ledger_order(request, pk):

    return render(
        request,
        'ledger/single_ledger_order.html',
        {
            
        }
    )

def single_ledger_update(request, pk):


    id = Ledger.objects.get(pk=pk)
    order_list = Order.objects.all()

    if request.method == "POST":

        order = Order.objects.get(pk=pk)
        print("실행됨")
        
        
        # get_object_or_404(Order, pk=pk).order_by('create_at')
        # Order().objects.get(pk=pk)

        
        order.number = request.POST['']
        order.orderer = request.POST['orderer']
        order.item = request.POST['order_item']
        order.count = request.POST['order_count']

        order.save()

        return render(
            request,
            'ledger/single_ledger.html',
            {
            'order_list': order_list,
            'id': id,
            'pk': pk,
            },
        )

    
    else:
        print("실행 안 됨")
        return render(
        request,
        'ledger/single_ledger_update.html',
        {
            'order_list': order_list,
            'id': id,
            'pk': pk,
        },
    )

# def update_item(request)