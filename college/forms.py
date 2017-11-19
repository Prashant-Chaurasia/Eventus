from django import forms
from .models import College

class CollegeForm(forms.ModelForm):
    class Meta:
        model = College
        fields = ('name','logo',
                  'scc_mail_id','description',
                  'website','address',
                  'city')