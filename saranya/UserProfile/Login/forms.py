from django.forms import ModelForm
from .models import UserDetails

class UserForm(ModelForm):
    
    #resume = forms.FileField(upload_to='static/pdfs/', null=True, blank=True)
    class Meta:
        model = UserDetails
        fields = '__all__'

    



        