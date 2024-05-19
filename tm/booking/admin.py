from django.contrib import admin
from .models import Booking

class BookingAdmin(admin.ModelAdmin):
    list_filter = ("customer", "driver", "truck", "date", "payment_method", "payment_status")
    search_fields = ["customer", "driver", "truck", "date", "payment_method", "payment_status"]
    list_display = ("id", "customer", "driver", "truck", "date", "payment_status", "payment_method")


admin.site.register(Booking, BookingAdmin)
