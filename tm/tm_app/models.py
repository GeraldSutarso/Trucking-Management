from django.db import models

class Customer(models.Model):
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    full_name = models.CharField(max_length=255)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)
    address = models.TextField()

class Truck(models.Model):
    model = models.CharField(max_length=255)
    license_plate = models.CharField(max_length=20)
    capacity = models.IntegerField()
    driver = models.ForeignKey('Driver', on_delete=models.CASCADE, related_name='driver')

class Driver(models.Model):
    full_name = models.CharField(max_length=255)
    license_number = models.CharField(max_length=20)
    availability = models.BooleanField()
    vehicle_used = models.OneToOneField('Truck', on_delete=models.SET_NULL, null=True, related_name='truck')
    profile_picture = models.ImageField(upload_to='driver_profile_pics/', blank=True, null=True)
    profile_picture_confirmed = models.BooleanField(default=False)

class Booking(models.Model):
    customer = models.ForeignKey('Customer', on_delete=models.CASCADE)
    truck = models.ForeignKey('Truck', on_delete=models.CASCADE)
    reason_for_booking = models.TextField()
    delivery_content = models.TextField()
    booking_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20)

class Payment(models.Model):
    booking = models.ForeignKey('Booking', on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_method = models.CharField(max_length=50)
    payment_date = models.DateTimeField(auto_now_add=True)

class Delivery(models.Model):
    booking = models.OneToOneField('Booking', on_delete=models.CASCADE)
    driver = models.ForeignKey('Driver', on_delete=models.CASCADE)
    delivery_date = models.DateTimeField()
    delivery_status = models.CharField(max_length=20)
    

class Notification(models.Model):
    booking = models.ForeignKey('Booking', on_delete=models.CASCADE)
    driver = models.ForeignKey('Driver', on_delete=models.CASCADE)
    notification_type = models.CharField(max_length=50)
    timestamp = models.DateTimeField(auto_now_add=True)

class Maintenance(models.Model):
    truck = models.ForeignKey('Truck', on_delete=models.CASCADE)
    sensor_type = models.CharField(max_length=50)
    notification_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20)
