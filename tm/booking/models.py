from django.db import models
from django import forms
from django.contrib import admin
from accounts.models import *


def receipt_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/payment_receipt/<id>/<filename>
    return 'payment_receipts/{0}/{1}'.format(instance.id, filename)
class Booking(models.Model):
    PAYMENT_METHOD_CHOICES = [
        ('cash', 'Cash'),
        ('bank_transfer', 'Bank Transfer'),
    ]
    
    PAYMENT_STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('completed', 'Completed'),
        ('failed', 'Failed'),
    ]
  
    driver = models.ForeignKey('accounts.Driver', on_delete=models.SET_NULL, null=True, related_name="booking_driver")
    customer = models.ForeignKey('accounts.Customer', on_delete=models.SET_NULL, null=True, related_name="booking_customer")
    truck = models.ForeignKey('vehicles.Truck', on_delete=models.SET_NULL, null=True, related_name="booking_driver")
    pickup = models.CharField(max_length=255, null=True, blank=True)
    destination = models.CharField(max_length=255, null=True, blank=True)
    distance = models.FloatField(null=True, blank=True)
    date = models.DateField(null=True, blank=True)
    details = models.TextField(null=True, blank=True)
    weight = models.FloatField(null=True, blank=True)
    price = models.FloatField(null=True, blank=True)
    payment_method = models.CharField(max_length=20, choices=PAYMENT_METHOD_CHOICES, null=True, blank=True)
    payment_status = models.CharField(max_length=20, choices=PAYMENT_STATUS_CHOICES, default='pending')
    transfer_receipt = models.ImageField(upload_to=receipt_path, null=True, blank=True)

    def __str__(self):
        return f"Booking by {self.customer.user.username} on {self.date}"


