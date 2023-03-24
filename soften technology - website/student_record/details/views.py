
from .models import Student_entry
from django.views.generic import ListView,DetailView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.urls import reverse_lazy

class Student_entryList(ListView):
    model=Student_entry

class Student_entryDetail(DetailView):
    model=Student_entry

class Student_entryUpdate(UpdateView):
    model=Student_entry
    queryset=Student_entry.objects.all()
    fields=['name','Reg_no','Class','Phone_no','Email_id','Stu_Address']
    success_url=reverse_lazy('home')

class Student_entryCreate(CreateView):
    model=Student_entry
    fields=['name','Reg_no','Class','Phone_no','Email_id','Stu_Address']
    success_url=reverse_lazy('home')

class Student_entryDelete(DeleteView):
    model=Student_entry
    template_name='details/Student_entry_delete.html'
    success_url=reverse_lazy('home')






# Create your views here.
