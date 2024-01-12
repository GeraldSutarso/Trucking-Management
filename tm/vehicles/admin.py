from django.contrib import admin
from vehicles.models import *

class TruckAdmin(admin.ModelAdmin):
    pass
admin.site.register(Truck,TruckAdmin)
class MaintenanceAdmin(admin.ModelAdmin):
    pass
admin.site.register(Maintenance,MaintenanceAdmin)