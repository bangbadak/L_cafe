from django.urls import path
from . import views
from ledger.views import index

urlpatterns = [
    path('', index),

    path('ledgers/', views.ledgers, name="ledgers"),

    path('item/', views.update_item),
    path('item/add', views.add_item, name="add_item"),


    path('ledgers/<str:pk>/', views.single_ledger),
    path('ledgers/<str:pk>/update', views.single_ledger_update, name="single_ledger"),
    path('ledgers/<str:pk>/order', views.single_ledger_order, name="single_ledger_order"),



    # path('ledgers/item/', ),

    # path('update/', views.update),
    # path('update_item/', views.update_item),
]