from django.shortcuts import render

# Create your views here.
" the below code is for rendering html file in templates folder"
def welcome(request):
    return render(request, 'session3/sample.html')

def add_static(request):
    return render(request, 'session3/static_check.html')