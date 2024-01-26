from django.urls import path
from . import views

urlpatterns = [
    #Correct the path of the missing lambs
    path('', views.go_home, name='go_home'),
    path('home', views.go_home, name='go_home'),
    path('login', views.go_login, name='go_login'),
    path('homel', views.go_home),
    path('register', views.go_register_c, name='go_register_c'),
    path('register/customer', views.go_register_c, name='go_register_c'),
    path('register/driver', views.go_register_d, name='go_register_d'),
    path('register/customer', views.go_register_c, name='go_register_c'),
    path('register/driver', views.go_register_d, name='go_register_d'),
    
    path('driver/home', views.driver_home, name = 'driver_home'),
    path('customer/home', views.customer_home, name = 'customer_home')

]
