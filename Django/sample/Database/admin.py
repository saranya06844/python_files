from django.contrib import admin
from .models import Employee


class EmployeeAdmin(admin.ModelAdmin):
    emp_details =['Employee_no','Employee_name','Employee_Salary','Employee_Address']

# Register your models here.
admin.site.register(Employee, EmployeeAdmin)
