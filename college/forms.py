from django import forms
from .models import College,CITY_CHOICES

class CollegeForm(forms.ModelForm):

    class Meta:
        model = College
        fields = ('name','logo',
                  'scc_mail_id','description',
                  'website','address',
                  )