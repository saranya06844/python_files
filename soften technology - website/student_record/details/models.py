from operator import mod
from unicodedata import name
from django.db import models

classes=(
    ('sslc','SSLC'),
    ('plusone','PlusOne'),
    ('plustwo','PlusTwo'),
)

class Student_entry(models.Model):
    name=models.CharField(max_length=100)
    Reg_no= models.IntegerField(blank=True, null=True)
    Class=models.CharField(max_length=100, choices=classes, default='SSLC')
    Stu_Address=models.TextField(max_length=100)
    Phone_no=models.IntegerField(blank=True, null=True)
    Email_id=models.EmailField(max_length=100)

    def __str__(self):
        return self.name

# Create your models here.
