from django.db import models


class Truck(models.Model):
    model = models.CharField(max_length=255)
    license_plate = models.CharField(max_length=20)
    driver = models.OneToOneField('accounts.Driver', on_delete=models.SET_NULL, null=True)
    capacity = models.IntegerField()

class Maintenance(models.Model):
    truck = models.ForeignKey(Truck, on_delete=models.CASCADE)
    sensor_type = models.CharField(max_length=50)
    notification_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20)