from django.shortcuts import render
from .models import Student

# Create your views here.
def home(req):
    student=Student.objects.all()
    return render(req, 'home.html',{'students':student})