
from django.shortcuts import render
from django.http import HttpResponse

def setsession(request):
    request.session['sname']='sara'
    request.session['semail']='saranya@gmail.com'
    return HttpResponse('section is set')
def getsession(request):
    student_name = request.session['sname']
    student_email = request.session['semail']
    return HttpResponse(student_name+" "+student_email)
# Create your views here.
