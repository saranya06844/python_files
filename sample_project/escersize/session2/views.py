import datetime

from django.shortcuts import render
from django.http import HttpResponse
import time

# Create your views here.
""""here we print functions to say greetings"""
def Good_Morning(request):
    return HttpResponse("<h1>Good Morning</h1>")
def Good_Afternoon(request):
    return HttpResponse("<h1>Good Afternoon</h1>")
def Good_Evenig(request):
    return HttpResponse("<h1>Good Evening</h1>")
def Good_Night(request):
    return HttpResponse("<h1>Good Night</h1>")
"""----------------------------------------------------"""

"""create a functions for print greetings based on current time"""

def Greetings(request):
    time = datetime.datetime.now()
    Current_time = int(time.hour)
    if Current_time < 12:
        return HttpResponse('<h1>Good Morning</h1>'+str(time)+"   "+str(Current_time) )
    else:
        return HttpResponse('<h1>Good Evening</h1>'+str(Current_time)+"   "+str(time))