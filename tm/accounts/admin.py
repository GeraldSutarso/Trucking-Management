from django.contrib import admin
from accounts.models import *

class UserAdmin(admin.ModelAdmin):
    pass
admin.site.register(User,UserAdmin)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ("username","first_name","last_name", "email", "phone_number")
    search_fields = ["username","first_name","last_name", "email", "phone_number"]
    pass
admin.site.register(Customer,CustomerAdmin)
class DriverAdmin(admin.ModelAdmin):
    list_display = ("username","first_name","last_name", "email", "phone_number")
    search_fields = ["username","first_name","last_name", "email", "phone_number"]
    pass
admin.site.register(Driver,DriverAdmin)
class AdminAdmin(admin.ModelAdmin):
    list_display = ("username", "email", "phone_number")
    search_fields = ["username", "email", "phone_number"]
    pass
admin.site.register(Admin,AdminAdmin)
# Register your models here.
