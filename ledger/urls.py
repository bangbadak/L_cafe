from django.urls import path
from . import views
from ledger.views import index

urlpatterns = [
    path('', index),
    path('create/', views.create),
    path('read/', views.read),
    path('read/<str:read>/', views.read_single_ledger),
    # path('update/', views.update),
    # path('update_item/', views.update_item),
]