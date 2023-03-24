from django.shortcuts import render
from .models import wedding

# Create your views here.
def index(req):
    service = wedding.objects.all()
    return render(req,'index.html',{'services':service})