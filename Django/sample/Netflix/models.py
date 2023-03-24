from django.db import models

# Create your models here.
class Teacher(models.Model):
    Teacher_name=models.CharField(max_length=14)
    Teacher_salary=models.IntegerField()

class Student(models.Model):
    Student_name=models.CharField(max_length=10)
