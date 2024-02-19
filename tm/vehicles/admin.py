from django.contrib import admin
from vehicles.models import *

class TruckAdmin(admin.ModelAdmin):
    search_fields = ("truck_model", "driver","status")
    list_display = ("truck_model", "driver","status")
    list_filter = ("status",)
    
    def get_driver_first_name(self, obj):
        return obj.driver.user.first_name

    def get_driver_last_name(self, obj):
        return obj.driver.user.last_name
    def driver(self,obj):
        return obj.driver.user.first_name + obj.driver.user.last_name
    pass
admin.site.register(Truck,TruckAdmin)
class MaintenanceAdmin(admin.ModelAdmin):
    list_display = ("truck_model", "driver", "notification_date")
    search_fields = ("truck_model", "driver","notification_date","schedule")
    list_filter = ("notification_date","schedule")
    
    def truck_model(self,obj):
        return obj.truck.truck_model
    
    def get_driver_first_name(self, obj):
        return obj.truck.driver.user.first_name

    def get_driver_last_name(self, obj):
        return obj.truck.driver.user.last_name
    def driver(self,obj):
        return f"{obj.truck.driver.user.first_name} {obj.truck.driver.user.last_name}"
    pass
admin.site.register(Maintenance,MaintenanceAdmin)