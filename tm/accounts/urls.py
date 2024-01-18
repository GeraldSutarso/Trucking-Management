from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login, name='login'),
    path('register_customer/', views.register_customer, name='register_customer'),
    path('register_driver/', views.register_driver, name='register_driver'),
    path('logout/', views.logout, name='logout'),
    path('driver/home/', views.go_driver_home, name='go_driver_home'),
    path('customer/home/', views.go_customer_home, name='go_customer_home'),
]