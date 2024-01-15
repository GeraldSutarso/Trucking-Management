from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib import admin

class User(AbstractUser):
    is_customer = models.BooleanField(default=False)
    is_driver = models.BooleanField(default=False)
    phone_number = models.CharField(max_length=20)

class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    address = models.TextField()
    
    @admin.display(ordering='user__username', description='Username')
    def username(self):
        return self.user.username
    
    @admin.display(ordering='user__first_name', description='First Name')
    def first_name(self):
        return self.user.first_name
    
    @admin.display(ordering='user__last_name', description='Last Name')
    def last_name(self):
        return self.user.last_name

    @admin.display(ordering='user__email', description='Email')
    def email(self):
        return self.user.email

    @admin.display(ordering='user__phone_number', description='Phone number')
    def phone_number(self):
        return self.user.phone_number
    
class Driver(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    license_number = models.CharField(max_length=20)
    availability = models.BooleanField(default = False)
    profile_picture = models.ImageField(upload_to='tm/static/img/driver/face', blank=True, null=True)
    id_card = models.ImageField(upload_to='tm/static/img/driver/id', blank= True, null=True)
    license_card = models.ImageField(upload_to='tm/static/img/driver/license', blank= True, null=True)
    profile_picture_confirmed = models.BooleanField(default=False)
    accepted = models.BooleanField(default = False)
    vehicle_available = models.BooleanField(default = False)
    def __str__(self):
        return self.user.first_name + " " + self.user.last_name
    
    @admin.display(ordering='user__username', description='Username')
    def username(self):
        return self.user.username
    
    @admin.display(ordering='user__first_name', description='First Name')
    def first_name(self):
        return self.user.first_name
    
    @admin.display(ordering='user__last_name', description='Last Name')
    def last_name(self):
        return self.user.last_name

    @admin.display(ordering='user__email', description='Email')
    def email(self):
        return self.user.email

    @admin.display(ordering='user__phone_number', description='Phone number')
    def phone_number(self):
        return self.user.phone_number
    
class Admin(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE, primary_key= True)
    
    @admin.display(ordering='user__username', description='Username')
    def username(self):
        return self.user.username

    @admin.display(ordering='user__email', description='Email')
    def email(self):
        return self.user.email

    @admin.display(ordering='user__phone_number', description='Phone number')
    def phone_number(self):
        return self.user.phone_number
