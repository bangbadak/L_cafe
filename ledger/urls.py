from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('create/', views.create),
    path('read/', views.read),
    path('update/', views.update),
    path('update_item/', views.update_item),
]