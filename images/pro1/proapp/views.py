from django.shortcuts import render
from .models import Images

# Create your views here.
def home(request):
    Image= Images.objects.all()
    return render(request, 'home.html', {'images':Image})