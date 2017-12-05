from django.shortcuts import render, redirect
from django.contrib.auth.models import Group
from .forms import ContactForm
from django.contrib import messages
# Create your views here.


def home(request):

    my_group, created = Group.objects.get_or_create(name='FacultyOnly')
    my_group, created = Group.objects.get_or_create(name='StudentsOnly')
    form = ContactForm
    return render(request, 'account/home.html', {'form':form})


def contact_new(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        print(form)
        if form.is_valid():
            form.save()
            messages.success(request, 'lol')
            return redirect('home:homepage')
    else:
        form = ContactForm()
        return render(request, 'account/home.html', {'form':form})


