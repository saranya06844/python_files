from django.shortcuts import render
import os
from django.http import HttpResponse

# Create your views here.
def Home(request):
    return render(request,'index.html')
def category(request):
    return render(request,'category.html')
def contact(request):
    return render(request,'contact.html')
def listing(request):
    return render(request,'listing.html')

def image(request):
    image1 = os.path.abspath('assets\images\listing-01.jpg')

    return render(request ,{'img':image1})




