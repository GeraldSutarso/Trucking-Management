from django.urls import path
from . import views

urlpatterns = [
    path('gps/', views.gps, name='gps'),
]