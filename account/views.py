from django.shortcuts import render, redirect
from . import forms
# Create your views here.
from django.http.response import HttpResponse


def home(request):

    if is_faculty(request.user):
        return HttpResponse('<h1>You are Faculty<h2>')
    else:
        return redirect('events:events_list')


def is_faculty(user):
    return user.groups.filter(name='FacultyOnly').exists()
