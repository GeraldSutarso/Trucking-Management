from django.db import models
from django import forms
from django.contrib import admin
from accounts.models import *

class Booking(models.Model):
  
    driver = models.ForeignKey('accounts.Driver', on_delete=models.SET_NULL, null=True,related_name="booking_driver")
    customer = models.ForeignKey('accounts.Customer', on_delete=models.SET_NULL, null=True,related_name="booking_customer")
    truck = models.ForeignKey('vehicles.Truck', on_delete=models.SET_NULL, null=True,related_name="booking_driver")
    pickup = models.CharField(max_length=255, null=True, blank=True)
    destination = models.CharField(max_length=255, null=True, blank=True)
    distance = models.FloatField(null=True, blank=True)
    date = models.DateField(null=True, blank=True)
    details = models.TextField(null=True, blank=True)
    weight = models.FloatField(null=True, blank=True)

    def __str__(self):
        return f"Booking by {self.customer.user.username} on {self.date}"
    
