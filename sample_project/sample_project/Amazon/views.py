from django.shortcuts import render, redirect
from .models import Student_details
from .forms import Student_form , StudentDetailsInfo

# Create your views here.
def sample(request):
    data =Student_details.objects.all()
    data_dic ={'Student_list':data}
    return render(request, 'Student_details.html',context= data_dic)

def StudentForm(request):
    form=StudentDetailsInfo()
    form_dic ={'form':form}
    return render(request,'input.html',form_dic)

def Cookies_count_view(request):
    count = request.COOKIES.get('count',0)
    total_count = int(count)+1
    response = render(request, 'cookie.html',{'count':total_count})
    response.set_cookie('count',total_count)
    return response

def Session_count_view(request):
    count = request.session.get('count',0)
    total_count = int(count) + 1
    request.session['count'] = total_count
    print(request.session.get_expiry_date)
    return render(request, 'cookie.html', {'count':total_count})

def Student_info(request):
    student = Student_details.objects.all()
    return render(request, 'index.html', {'student':student})

def Add_student(request):
    form =Student_form()
    if request.method == 'POST':
        form = Student_form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('display')
    return render(request, 'create.html',{'form':form})


def delete_view(request, id):
    student = Student_details.objects.get(id =id)
    student.delete()
    return redirect('display')

def update_view(request, id):
    student = Student_details.objects.get(id = id)
    if request.method == 'POST':
        student = Student_form(request.POST,instance = student)
        if student.is_valid():
            student.save()
            return redirect('display')
    return render(request, 'update.html', {'student':student})

