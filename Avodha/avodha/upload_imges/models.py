from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=29)
    image = models.ImageField(upload_to='picture')