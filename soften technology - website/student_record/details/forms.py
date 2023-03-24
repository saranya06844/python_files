from pyexpat import model
from django import forms
from .models import Student_entry

class MyForm(forms.ModelForm):
    class Meta:
        model=Student_entry
        fields='__all__'

