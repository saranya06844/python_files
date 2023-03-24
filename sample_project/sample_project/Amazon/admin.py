from django.contrib import admin
from .models import Student_details

class StudentAdmin(admin.ModelAdmin):
    #Student_dict = ['Student_RollNo' , 'Student_Name' , 'Student_Mark']
    Student_dict ='__all__'
# Register your models here.
admin.site.register(Student_details,StudentAdmin)
