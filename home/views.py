from django.contrib import messages
from django.shortcuts import redirect, render

from .models import Category, Contact, Project


def home(request):
    projects = Project.objects.order_by('-date_added')[:6]
    categories = Category.objects.all()
    return render(request, 'home.html', {'projects': projects, 'categories': categories})


def projects(request):
    all_projects = Project.objects.order_by('-date_added')
    categories = Category.objects.all()
    return render(
        request,
        'project.html',
        {'projects': all_projects, 'categories': categories},
    )


def contact(request):
    if request.method != 'POST':
        return redirect('home')

    fields = {
        'name': request.POST.get('name', '').strip(),
        'email': request.POST.get('email', '').strip(),
        'subject': request.POST.get('subject', '').strip(),
        'message': request.POST.get('message', '').strip(),
    }
    if not all(fields.values()):
        messages.error(request, 'Please complete every contact field.')
    else:
        Contact.objects.create(**fields)
        messages.success(request, 'Thanks—your message has been received.')
    return redirect('/#contact')
