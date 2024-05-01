from django.db import models
from django import forms
from django.contrib import admin
from accounts.models import *

class Booking(models.Model):
  
    driver = models.ForeignKey('accounts.Driver', on_delete=models.SET_NULL, null=True,related_name="booking_driver")
    customer = models.ForeignKey('accounts.Customer', on_delete=models.SET_NULL, null=True,related_name="booking_customer")
    truck = models.ForeignKey('vehicles.Truck', on_delete=models.SET_NULL, null=True,related_name="booking_driver")
    truck_available=models.BooleanField(blank=True, default=False)
    