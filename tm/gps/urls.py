from django.urls import path
from . import views

urlpatterns = [
    path('customer/delivery/gps', views.gps, name='gps'),
]