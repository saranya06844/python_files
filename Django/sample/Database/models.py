from django.db import models

# Create your models here.
class Employee(models.Model):    
    Employee_no = models.IntegerField()
    Employee_name = models.CharField(max_length=30)
    Employee_Salary = models.IntegerField()
    Employee_Address = models.CharField(max_length=100)