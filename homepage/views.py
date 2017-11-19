from django.shortcuts import render
from django.contrib.auth.models import Group

# Create your views here.


def home(request):

    my_group, created = Group.objects.get_or_create(name='FacultyOnly')
    my_group, created = Group.objects.get_or_create(name='StudentsOnly')

    return render(request,'account/home.html',{})