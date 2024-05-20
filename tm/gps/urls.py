from django.urls import path
from . import views

urlpatterns = [
    path('customer/trucks/gps', views.gps, name='gps'),
]