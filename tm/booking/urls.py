from django.urls import path
from . import views

urlpatterns = [
    # path('customer/booking/', views.customer_booking, name='customer_booking'),
    path('select-payment/', views.select_payment, name='select_payment'),
    path('create-payment/', views.create_payment, name='create_payment'),
    path('payment-success/<int:booking_id>/', views.payment_success, name='payment_success'),
    path('payment-pending/<int:booking_id>/', views.payment_pending, name='payment_pending'),
    path('payment-declined/<int:booking_id>/', views.payment_declined, name='payment_declined'),
    path('payment_status/<int:booking_id>/', views.payment_status, name='payment_status'),
]