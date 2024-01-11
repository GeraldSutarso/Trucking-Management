from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    is_customer = models.BooleanField('is a customer',default=False)
    is_driver = models.BooleanField('is a driver',default=False)
    phone_number = models.CharField(max_length=20)

class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    address = models.TextField()
    
class Driver(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    license_number = models.CharField(max_length=20)
    availability = models.BooleanField()
    profile_picture = models.ImageField(upload_to='tm/static/img/driver/', blank=True, null=True)
    profile_picture_confirmed = models.BooleanField(default=False)
    accepted = models.BooleanField(default = False)
    
class Admin(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE, primary_key= True)