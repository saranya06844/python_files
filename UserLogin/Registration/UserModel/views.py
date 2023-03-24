from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import UserAdminCreationForm


def register(req):
    form = UserAdminCreationForm()
    if req.method == 'POST':
        form = UserAdminCreationForm(req.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    return render(req, 'register.html', {'form': form})

@login_required
def home(request):
    return render(request, 'base.html')