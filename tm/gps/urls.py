from django.urls import path
from . import views

urlpatterns = [
    path('delivery/gps', views.gps, name='gps'),
]