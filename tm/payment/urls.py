# urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('payment/', views.payment_page, name='payment_page'),
    # Your other URLs
]

