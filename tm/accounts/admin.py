from django.contrib import admin
from accounts.models import *

class UserAdmin(admin.ModelAdmin):
    pass
admin.site.register(User,UserAdmin)
class CustomerAdmin(admin.ModelAdmin):
    pass
admin.site.register(Customer,CustomerAdmin)
class DriverAdmin(admin.ModelAdmin):
    pass
admin.site.register(Driver,DriverAdmin)
class AdminAdmin(admin.ModelAdmin):
    pass
admin.site.register(Admin,AdminAdmin)
# Register your models here.
