from django.db import models

class Gps(models.Model):
    id = models.AutoField(primary_key=True)
    lat = models.FloatField()
    lng = models.FloatField()
    created_date = models.DateTimeField()

    class Meta:
        db_table = 'tbl_gps'
