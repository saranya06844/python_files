from django.db import models

# Create your models here.
class wedding(models.Model):
    name= models.CharField(max_length=30)
    img = models.ImageField(upload_to='picture')
