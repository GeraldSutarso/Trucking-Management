from django.db import models

class FacePhoto(models.Model):
    image = models.ImageField(upload_to='photos/')
    result = models.CharField(max_length=50)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    driver = models.ForeignKey('accounts.Driver', on_delete=models.SET_NULL, null=True, related_name="driver_face")