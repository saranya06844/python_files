from django import forms
from .models import Student_details

# to create a subclass for forms (forms.Form)
class StudentDetailsInfo(forms.Form):
    Student_Name=forms.CharField()
    Student_Number=forms.IntegerField()

class Student_form(forms.ModelForm):
    class Meta:
        model = Student_details
        fields = '__all__'


