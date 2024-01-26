from django.db import models
from django.contrib import admin
from accounts.models import *

class Truck(models.Model):
    status_choices= (
        ("OK", "OK"),
        ("WARNING","WARNING"),
        ("DANGER","DANGER")
    )
    truck_model = models.CharField(max_length=255)
    license_plate = models.CharField(max_length=20)
    driver = models.OneToOneField('accounts.Driver', on_delete=models.SET_NULL, null=True,related_name="truck_driver")
    capacity = models.IntegerField(blank=True, null=True)
    location = models.CharField(max_length=255, blank=True, null=True)
    status = models.CharField(choices=status_choices, max_length = 10)
    last_maintained = models.DateField(blank = True, null = True)
    
    def __str__(self):
        return self.truck_model
    
class Maintenance(models.Model):
    truck = models.ForeignKey(Truck, on_delete=models.CASCADE, related_name="truck_maintenance")
    sensor_type = models.CharField(max_length=50)
    notification_date = models.DateTimeField(auto_now_add=True)
    schedule = models.DateTimeField(blank = True, null = True)