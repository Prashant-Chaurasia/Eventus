from registration.backends.default.views import RegistrationView
from .forms import FacultyForm, StudentForm
from .models import Faculty, CollegeCode, Students
from django.contrib import messages
from django.shortcuts import render
from django.contrib.auth.models import Group

class StudentRegistrationView(RegistrationView):

    form_class = StudentForm

    def register(self, form_class):

        new_user = super(StudentRegistrationView, self).register(form_class)
        g = Group.objects.get(name='StudentsOnly')
        g.user_set.add(new_user)
        p = form_class.cleaned_data['Name']
        q = form_class.cleaned_data['Code']
        r = form_class.cleaned_data['RollNo']
        college = CollegeCode.objects.get(Name=q)
        new_profile = Students.objects.create(user=new_user, Name=p, Code=college, RollNo=r)
        new_profile.save()
        return new_user
