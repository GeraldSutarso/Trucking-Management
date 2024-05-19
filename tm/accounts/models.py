from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib import admin

class User(AbstractUser):
    is_customer = models.BooleanField(default=False)
    is_driver = models.BooleanField(default=False)
    phone_number = models.CharField(max_length=20)

def customer_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/customer/<id>/profile/<filename>
    return 'customer/{0}/profile/{1}'.format(instance.user.id, filename)
class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True, related_name="user_customer")
    address = models.TextField()
    profile_picture = models.ImageField(upload_to=customer_directory_path, blank=True, null=True)
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
    
def driver_profile_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/driver/<id>/profile/<filename>
    return 'driver/{0}/profile/{1}'.format(instance.user.id, filename)

def driver_id_card_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/driver/<id>/id_card/<filename>
    return 'driver/{0}/id_card/{1}'.format(instance.user.id, filename)

def driver_license_card_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/driver/<id>/license_card/<filename>
    return 'driver/{0}/license_card/{1}'.format(instance.user.id, filename)
class Driver(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True, related_name="user_driver")
    license_number = models.CharField(max_length=20)
    availability = models.BooleanField(default = False)
    profile_picture = models.ImageField(upload_to=driver_profile_directory_path, blank=True, null=True)
    id_card = models.ImageField(upload_to=driver_id_card_directory_path, blank= True, null=True)
    license_card = models.ImageField(upload_to=driver_license_card_directory_path, blank= True, null=True)
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
    user = models.OneToOneField(User, on_delete = models.CASCADE, primary_key= True, related_name="use_admin")
    
    @admin.display(ordering='user__username', description='Username')
    def username(self):
        return self.user.username

    @admin.display(ordering='user__email', description='Email')
    def email(self):
        return self.user.email

    @admin.display(ordering='user__phone_number', description='Phone number')
    def phone_number(self):
        return self.user.phone_number

# import os
# from django.contrib.auth.models import AbstractUser
# from django.db import models
# from django.contrib import admin

# def driver_directory_path(instance, filename):
#     # Get the driver ID
#     driver_id = instance.user_driver_id

#     # Create the directory path
#     directory_path = f"Driver/{driver_id}/{filename}"

#     # Create the directories if they don't exist
#     os.makedirs(os.path.dirname(directory_path), exist_ok=True)

#     # Return the directory path
#     return directory_path

# def customer_directory_path(instance, filename):
#     # Get the customer ID
#     customer_id = instance.user_customer_id

#     # Create the directory path
#     directory_path = f"Customer/{customer_id}/{filename}"

#     # Create the directories if they don't exist
#     os.makedirs(os.path.dirname(directory_path), exist_ok=True)

#     # Return the directory path
#     return directory_path

# class User(AbstractUser):
#     is_customer = models.BooleanField(default=False)
#     is_driver = models.BooleanField(default=False)
#     phone_number = models.CharField(max_length=20)

# class Customer(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True, related_name="user_customer")
#     address = models.TextField()

#     @admin.display(ordering='user__username', description='Username')
#     def username(self):
#         return self.user.username

#     @admin.display(ordering='user__first_name', description='First Name')
#     def first_name(self):
#         return self.user.first_name

#     @admin.display(ordering='user__last_name', description='Last Name')
#     def last_name(self):
#         return self.user.last_name

#     @admin.display(ordering='user__email', description='Email')
#     def email(self):
#         return self.user.email

#     @admin.display(ordering='user__phone_number', description='Phone number')
#     def phone_number(self):
#         return self.user.phone_number

# class Driver(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True, related_name="user_driver")
#     license_number = models.CharField(max_length=20)
#     availability = models.BooleanField(default=False)
#     profile_picture = models.ImageField(upload_to=driver_directory_path, blank=True, null=True)
#     id_card = models.ImageField(upload_to=driver_directory_path, blank=True, null=True)
#     license_card = models.ImageField(upload_to=driver_directory_path, blank=True, null=True)
#     face_picture = models.ImageField(upload_to=driver_directory_path, blank=True, null=True)
#     profile_picture_confirmed = models.BooleanField(default=False)
#     accepted = models.BooleanField(default=False)
#     vehicle_available = models.BooleanField(default=False)

#     def __str__(self):
#         return self.user.first_name + " " + self.user.last_name

#     @admin.display(ordering='user__username', description='Username')
#     def username(self):
#         return self.user.username

#     @admin.display(ordering='user__first_name', description='First Name')
#     def first_name(self):
#         return self.user.first_name

#     @admin.display(ordering='user__last_name', description='Last Name')
#     def last_name(self):
#         return self.user.last_name

#     @admin.display(ordering='user__email', description='Email')
#     def email(self):
#         return self.user.email

#     @admin.display(ordering='user__phone_number', description='Phone number')
#     def phone_number(self):
#         return self.user.phone_number

# class Admin(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True, related_name="use_admin")

#     @admin.display(ordering='user__username', description='Username')
#     def username(self):
#         return self.user.username

#     @admin.display(ordering='user__email', description='Email')
#     def email(self):
#         return self.user.email

#     @admin.display(ordering='user__phone_number', description='Phone number')
#     def phone_number(self):
#         return self.user.phone_number
