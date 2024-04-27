from django.urls import path
from . import views

urlpatterns = [
    path('customer/booking/', views.customer_booking, name='customer_booking'),
]