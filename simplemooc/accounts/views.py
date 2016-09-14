from django.shortcuts import render, redirect

# Create your views here.

from django.contrib.auth.forms import UserCreationForm
from django.conf import settings


from .forms import RegisterForm

def register(request):
    template_name = 'register.html'

    if request.method == 'POST':
        form = RegisterForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect(settings.LOGIN_URL)    
    else:
        form = RegisterForm()

    context = {
        'form':form
    }

    return render(request, template_name, context)    
