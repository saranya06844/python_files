from django.db import models

# Create your models here.
class Images(models.Model):
    name = models.CharField(max_length=20)
    images = models.ImageField(upload_to='picture')