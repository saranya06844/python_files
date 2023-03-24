from django.db import models

# Create your models here.
class Teacher(models.Model):
    Teacher_name = models.CharField(max_length=30)
    Teacher_salary = models.FloatField()
    Teacher_Address = models.CharField(max_length=100)
