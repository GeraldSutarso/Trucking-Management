from django.contrib import admin
from vehicles.models import *

class TruckAdmin(admin.ModelAdmin):
    list_display = ("model", "driver")
    
    def get_driver_first_name(self, obj):
        return obj.driver.user.first_name

    def get_driver_last_name(self, obj):
        return obj.driver.user.last_name
    def driver(self,obj):
        return obj.driver.user.first_name + obj.driver.user.last_name
    pass
admin.site.register(Truck,TruckAdmin)
class MaintenanceAdmin(admin.ModelAdmin):
    pass
admin.site.register(Maintenance,MaintenanceAdmin)