from django.shortcuts import render
from django.http import HttpResponse
import datetime

date_dic = {}
# Create your views here.
def display(request):
    date = datetime.datetime.now()
    hour = int(date.strftime('%H'))
    message ='Hi '
    if hour <12:
        message += 'good morning'
    else:
        message += 'godd evening'
    da_dic = {'greetings': message }
    return render(request,'hello.html',da_dic)
    

    #return HttpResponse( message)