from django.shortcuts import render, redirect
from . import forms
# Create your views here.
from django.http.response import HttpResponse
from .models import Students, Faculty
from django.contrib.auth.models import User
from django.http import Http404
from django.contrib.auth.decorators import login_required


def home(request):
    return redirect('events:events_list')


def is_faculty(user):
    return user.groups.filter(name='FacultyOnly').exists()


def is_faculty_or_secretory(user):

    if user.groups.filter(name='FacultyOnly').exists():
        return True
    else:
        secretory = Students.objects.get(user=user)
        if secretory.is_secratory:
            return False
        else:
            return True

def is_secretory(User):

    if User.groups.filter(name='FacultyOnly').exists():
        return False
    else:
        secretory = Students.objects.get(user=User)
        if secretory.is_secratory:
            return True
        else:
            return False

def ban_user(request):

    sec = False
    if is_secretory(request.user):
        sec = True

    if is_faculty_or_secretory(request.user) :

        if is_faculty(request.user):
            college = Faculty.objects.get(user=request.user)
        else:
            college = Students.objects.get(user=request.user)
        stud = Students.objects.filter(Code=college.Code)


        if request.method == "POST":
            user2 = User.objects.get(email=request.POST['email'])
            user2.is_active = False
            user2.save()
            emid = user2.email
            return render(request, 'account/success.html', {'sec', sec})

        return render(request, 'account/ban.html', {'users': stud, 'sec': sec})
    else:
        raise Http404