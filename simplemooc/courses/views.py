from django.shortcuts import render, get_object_or_404

# Create your views here.
from .models import Course
from .forms import ContactCourse

def index(request):
    courses = Course.objects.all()
    context = {
        'courses': courses
    }

    return render(request, 'index.html', context)

# def details(request, pk):
#     course = get_object_or_404(Course, pk=pk)
#     context = {
#         'course': course
#     }
#
#     return render(request, 'details.html', context)

def details(request, slug):
    course = get_object_or_404(Course, slug=slug)

    context = {}    

    if request.method == 'POST':
        form = ContactCourse(request.POST)

        if form.is_valid():
            context['is_valid'] = True
            print(form.cleaned_data['name'])
            print(form.cleaned_data['email'])
            print(form.cleaned_data['message'])
            form = ContactCourse()
    else:
        form = ContactCourse()

    context['form'] = form
    context['course'] = course
    
    return render(request, 'details.html', context)
