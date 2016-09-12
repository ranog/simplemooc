from django.shortcuts import render, redirect

# Create your views here.

from django.contrib.auth.forms import UserCreationForm
from django.conf import settings


def register(request):
    template_name = 'register.html'

    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect(settings.LOGIN_URL)    
    else:
        form = UserCreationForm()

    context = {
        'form':form
    }

    return render(request, template_name, context)    
