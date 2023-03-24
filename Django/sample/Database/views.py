from django.shortcuts import render
from .models import Employee

def Employee_list(request):
    data=Employee.objects.all()
    dat_dic={'employee_list':data}
    return render(request, 'EmployeeDetails.html',dat_dic)

# Create your views here.
