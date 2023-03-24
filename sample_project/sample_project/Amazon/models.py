from django.db import models

# Create your models here.
class Student_details(models.Model):
    Student_RollNo = models.IntegerField()
    Student_Name = models.CharField(max_length=30)
    Student_Mark = models.FloatField()