from django.db import models
class GFG(models.Model):
    name = models.CharField(max_length=100)
    contact = models.CharField(max_length=100)
    address = models.CharField(max_length=500)
 
class File(models.Model):
    file = models.FileField(upload_to="excel") 

class ExcelData(models.Model):
    data = models.FileField(upload_to='uploads/')

class UploadedFile(models.Model):
    file = models.FileField(upload_to='uploads/')
class ColumnAverages(models.Model):
    # Fields for each column average
    altitude_avg = models.FloatField()
    engine_load_avg = models.FloatField()
    barometric_pressure_avg = models.FloatField()
    engine_coolant_temp_avg = models.FloatField()
    ambient_air_temp_avg = models.FloatField()
    engine_rpm_avg = models.FloatField()
    intake_manifold_pressure_avg = models.FloatField()
    maf_avg = models.FloatField()
    air_intake_temp_avg = models.FloatField()
    speed_avg = models.FloatField()
    throttle_pos_avg = models.FloatField()
    engine_runtime_avg = models.FloatField()
    
    # Field for maintenance status
    maintenance_status = models.CharField(max_length=255)
    
    # Timestamp for the record
    created_at = models.DateTimeField(auto_now_add=True)
    driver_id = models.ForeignKey('accounts.Driver', on_delete=models.SET_NULL, null=True,related_name="maintenance_driver")

    def __str__(self):
        return f"Averages and Status as of {self.created_at}"
