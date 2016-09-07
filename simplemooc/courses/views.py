from django.shortcuts import render

# Create your views here.
from .models import Course

def index(request):
    courses = Course.objects.all()
    context = {
        'courses': courses
    }

    return render(request, 'index.html', context)
