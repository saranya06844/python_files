from django.db import models

# Create your models here.
class UserDetails(models.Model):
    Phone_no = models.IntegerField()
    Address = models.CharField(max_length=100)
    Age = models.IntegerField()
    date = models.DateField()
    username = models.CharField(max_length=100)
