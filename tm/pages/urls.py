from django.urls import path
from . import views

urlpatterns = [
    #Correct the path of the missing lambs
    
    #home
    path('driver/home', views.driver_home, name = 'driver_home'),
    path('customer/home', views.customer_home, name = 'customer_home'),
    path('driver/', views.driver_home, name = 'driver_home'),
    path('customer/', views.customer_home, name = 'customer_home'),
    path('', views.go_home, name='go_home'),
    path('home', views.go_home, name='go_home'),
    path('homel', views.go_home),
    
    #authentication
    path('login', views.go_login, name='go_login'),
    path('register', views.go_register_c, name='go_register_c'),
    path('register/customer', views.go_register_c, name='go_register_c'),
    path('register/driver', views.go_register_d, name='go_register_d'),
    path('register/customer', views.go_register_c, name='go_register_c'),
    path('register/driver', views.go_register_d, name='go_register_d'),
    path('logout', views.go_logout, name='OUTT'),

    #profile
    path('profile' , views.profile, name ='profile'),
    path('customer/profile', views.customer_profile, name= 'customer_profile'),
    path('driver/profile', views.driver_profile, name='driver_profile'),
    
    #trucks
    path('trucks' , views.trucks, name ='trucks'),
    path('customer/trucks', views.customer_trucks, name= 'customer_trucks'),
    path('driver/trucks', views.driver_trucks, name='driver_trucks'),
    path('delete_truck/', views.delete_truck, name='delete_truck'),
    path('add_truck/', views.add_truck, name='add_truck'),
    path('edit_truck/<int:truck_id>/', views.edit_truck, name='edit_truck'),
    path('save_truck/', views.save_truck, name='save_truck'),
    
    #booking
    path('book_truck/', views.book_truck, name='book_truck'),
    path('booking/<int:truck_id>/', views.booking, name='booking'),
    
    path('book_summary/<int:booking_id>/', views.booking_result, name='booking_result'),
    
    #notification
    path('customer-notification', views.notification_customer, name='notification_customer'),
    
    

    
]
