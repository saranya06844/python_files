from django.shortcuts import render, redirect
from .forms import UserForm
from .models import UserDetails

# Create your views here.

def home(request):
    return render(request, 'home.html')


def register_request(request):
    form = UserForm()
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    return render(request,'register.html', {'form': form})

    

def display(request):
    data = UserDetails.objects.all().values()
    context ={'form': data}
    return render(request, 'display.html', context)


def example(req):
    return render(req, 'example.html')

def add(request):
    num1 = int(request.POST["num1"])
    num2 = int(request.POST["num2"])
    addition = num1+num2
    return render(request, 'example2.html' ,{'add':addition})
