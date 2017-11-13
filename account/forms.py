from django import forms
from django.contrib.auth.models import User
from registration.forms import RegistrationFormUniqueEmail, RegistrationForm
from .models import Faculty, CollegeCode, Students

class FacultyForm(RegistrationFormUniqueEmail):

    Name = forms.CharField()
    #Code = forms.CharField(label='', widget=forms.Select(choices=CollegeCode.objects.all()))
    Code = forms.ModelChoiceField(queryset=CollegeCode.objects.all(), widget=forms.Select(attrs={'class':'selectpicker show-tick'}))


class StudentForm(RegistrationFormUniqueEmail):

    Name = forms.CharField()
    RollNo = forms.CharField()
    Code = forms.ModelChoiceField(queryset=CollegeCode.objects.all(), widget=forms.Select(attrs={'class':'selectpicker show-tick', 'data-width':'469px'}), empty_label='Please Select a College' )
