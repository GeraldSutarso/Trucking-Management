from django.db import models
from django import forms
from django.contrib import admin
from accounts.models import *


def truck_image_directory_path(instance, view, filename):
    # file will be uploaded to MEDIA_ROOT/truck/<id>/<view>/<filename>
    return 'truck/{0}/{1}/{2}'.format(instance.id, view, filename)
def get_front_view_path(instance, filename):
    return truck_image_directory_path(instance, 'frontview', filename)

def get_side_view_path(instance, filename):
    return truck_image_directory_path(instance, 'sideview', filename)

def get_back_view_path(instance, filename):
    return truck_image_directory_path(instance, 'backview', filename)

def get_top_view_path(instance, filename):
    return truck_image_directory_path(instance, 'topview', filename)

def get_overall_view_path(instance, filename):
    return truck_image_directory_path(instance, 'overall', filename)
class Truck(models.Model):
    status_choices= (
        ("OK", "OK"),
        ("WARNING","WARNING"),
        ("DANGER","DANGER")
    )
    truck_model = models.CharField(max_length=255)
    license_plate = models.CharField(max_length=20)
    driver = models.ForeignKey('accounts.Driver', on_delete=models.SET_NULL, null=True,related_name="truck_driver")
    capacity = models.IntegerField(blank=True, null=True)
    location = models.CharField(max_length=255, blank=True, null=True)
    status = models.CharField(choices=status_choices, max_length = 10, default="OK")
    last_maintained = models.DateField(blank = True, null = True)
    front_view = models.ImageField(upload_to=get_front_view_path, blank=True, null=True)
    side_view = models.ImageField(upload_to=get_side_view_path, blank=True, null=True)
    back_view = models.ImageField(upload_to=get_back_view_path, blank=True, null=True)
    top_view = models.ImageField(upload_to=get_top_view_path, blank=True, null=True)
    overall_view=models.ImageField(upload_to=get_overall_view_path, blank=True, null=True)
    truck_accepted = models.BooleanField(blank=True, default=False)
    truck_available=models.BooleanField(blank=True, default=False)
    
    def __str__(self):
        return self.truck_model
class TruckForm(forms.ModelForm):
    class Meta:
        model = Truck
        fields = ['truck_model', 'license_plate', 'driver', 'capacity', 'location', 'status', 'last_maintained', 'front_view', 'side_view', 'back_view', 'top_view', 'overall_view', 'truck_accepted', 'truck_available']
    
class Maintenance(models.Model):
    truck = models.ForeignKey(Truck, on_delete=models.CASCADE, related_name="truck_maintenance")
    sensor_type = models.CharField(max_length=50)
    notification_date = models.DateTimeField(auto_now_add=True)
    schedule = models.DateTimeField(blank = True, null = True)