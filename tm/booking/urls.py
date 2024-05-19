from django.urls import path
from . import views

urlpatterns = [
    # path('customer/booking/', views.customer_booking, name='customer_booking'),
    path('select-payment/', views.select_payment, name='select_payment'),
    path('create-payment/', views.create_payment, name='create_payment'),
    path('payment-success/', views.payment_success, name='payment_success'),
]