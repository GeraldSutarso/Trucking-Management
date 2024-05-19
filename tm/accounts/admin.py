from django.contrib import admin
from .models import User, Customer, Driver, Admin

class UserAdmin(admin.ModelAdmin):
    list_filter = ("is_superuser", "is_driver", "is_customer")
    search_fields = ["username", "first_name", "last_name", "email", "phone_number"]

class CustomerAdmin(admin.ModelAdmin):
    list_display = ("username", "first_name", "last_name", "email", "phone_number")
    search_fields = ["user__username", "user__first_name", "user__last_name", "user__email", "user__phone_number"]

class DriverAdmin(admin.ModelAdmin):
    list_display = ("username", "first_name", "last_name", "email", "phone_number")
    search_fields = ["user__username", "user__first_name", "user__last_name", "user__email", "user__phone_number"]

class AdminAdmin(admin.ModelAdmin):
    list_display = ("username", "email", "phone_number")
    search_fields = ["user__username", "user__email", "user__phone_number"]

admin.site.register(User, UserAdmin)
admin.site.register(Customer, CustomerAdmin)
admin.site.register(Driver, DriverAdmin)
admin.site.register(Admin, AdminAdmin)
