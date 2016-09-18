from django.shortcuts import render, redirect

# Create your views here.

from django.contrib.auth.forms import UserCreationForm
from django.conf import settings
<<<<<<< HEAD
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
=======

>>>>>>> parent of de19e8f... Usuario faz o cadastro já loga no sistema

from .forms import RegisterForm, EditAccountForm

@login_required
def dashboard(request):
    template_name = 'dashboard.html'
    return render(request, template_name)

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

@login_required
def edit(request):
    template_name = 'edit.html'
    context = {}
    if request.method == 'POST':
        form = EditAccountForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            form = EditAccountForm(instance=request.user)
            context['success'] = True

        else:
            form = EditAccountForm(instance=request.user)
        context['form'] = form

    return render(request, template_name, context)

@login_required
def edit_password(request):
    template_name = 'edit_password.html'
    return render(request, template_name)
