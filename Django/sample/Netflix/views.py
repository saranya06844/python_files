from django.shortcuts import render
from django.http import HttpResponse
import datetime


def first(request):
    
    return render(request,'base.html',{'first_name':'I\'am','last_name':'not sure'})

rooms =[
    {'id':1,'name':'saranya'},
    {'id':2, 'name':'charru'},
    {'id':3, 'name':'sara'}
]

def room(request):
    return render(request, 'room.html',{'rooms':rooms})

def nav(request, m):
   
    return render(request, 'navigation.html',{'ram':range(8)})

def mine(request):
    time = datetime.datetime.now
    date_dic = {'display_time':time}
    return render(request, 'mine.html',date_dic)


# Create your views here.
