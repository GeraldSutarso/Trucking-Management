from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login, name='login'),
    path('register_customer/', views.register_customer, name='register_customer'),
    path('register_driver/', views.register_driver, name='register_driver'),
    path('logout/', views.logout, name='logout'),
    path('driver/home/', views.driver_home, name='driver_home'),
    path('customer/home/', views.customer_home, name='customer_home'),
]