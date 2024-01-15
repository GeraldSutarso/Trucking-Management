from django.db import models
from django.contrib import admin
from accounts.models import *

class Truck(models.Model):
    model = models.CharField(max_length=255)
    license_plate = models.CharField(max_length=20)
    driver = models.OneToOneField('accounts.Driver', on_delete=models.SET_NULL, null=True)
    capacity = models.IntegerField(blank=True, null=True)
    location = models.CharField(max_length=255, blank=True, null=True)

    def get_driver_first_name(self, obj):
        return obj.driver.user.first_name

    def get_driver_last_name(self, obj):
        return obj.driver.user.last_name

class Maintenance(models.Model):
    truck = models.ForeignKey(Truck, on_delete=models.CASCADE)
    sensor_type = models.CharField(max_length=50)
    notification_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20)