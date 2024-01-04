from django.contrib import admin
from .models import Customer, Truck, Driver, Booking, Payment, Delivery, Notification, Maintenance

admin.site.register(Customer)
admin.site.register(Truck)
admin.site.register(Driver)
admin.site.register(Booking)
admin.site.register(Payment)
admin.site.register(Delivery)
admin.site.register(Notification)
admin.site.register(Maintenance)
