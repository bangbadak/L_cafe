from django.shortcuts import get_object_or_404, redirect, render
from .models import Ledger, Order, Item
from datetime import datetime
from django.utils.dateformat import DateFormat

def index(request):

    return render(
        request,
        'ledger/index.html',
    )


def ledgers(request):


    ledgers = Ledger.objects.all()
    check = False
    date = DateFormat(datetime.now()).format('Y년m월d일')

    for date in ledgers:
        check = True
    
    if(check == False):
        Ledger.objects.create()    

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


    

    if request.method == "POST":
        num = request.POST['order_num']
        orderer = request.POST['orderer']
        item = request.POST['order_item']
        cnt = request.POST['count']

        Order.objects.create(number=num, orderer=orderer, item=item, count=cnt)

        order_list = Order.objects.all()


        return redirect(
            '/l_cafe_ledger/ledgers/'+str(pk)
        )

    else:
        order_list = Order.objects.all()
        print(order_list)
        return render(
            request,
            'ledger/single_ledger_order.html',
            {
                'order_list': order_list,
                'pk': pk,
            },
        )



def single_ledger_update(request, pk):


    id = Ledger.objects.get(pk=pk)
    iden = Ledger.objects.get(pk=pk).identification
    order_list = Order.objects.all()

    if request.method == "POST":
        
        order = Order.objects.filter(identification=iden)


        print(order)
        print("실행됨")
        
        
        # get_object_or_404(Order, pk=pk).order_by('create_at')
        # Order().objects.get(pk=pk)

        
        order.orderer = request.POST['orderer']
        order.item = request.POST['order_item']
        order.count = request.POST['order_count']

        order.save()

        return redirect(
            '/l_cafe_ledger/ledgers/'+str(pk)+'/update/'
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



def update_item(request):

    items = Item.objects.all()
    
    return render(
        request,
        'ledger/item.html',
        {
            'items': items
        },
    )

def add_item(request):

    if request.method=="POST":
        name = request.POST['item_name']
        cost = request.POST['item_cost']

        Item.objects.create(name=name, cost=cost)
            
        return redirect(
            '/l_cafe_ledger/item/'
        )

    else:
        return render(
            request,
            'ledger/add_item.html',
        )