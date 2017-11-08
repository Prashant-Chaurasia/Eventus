from django import forms
from .models import Events

class EventForm(forms.ModelForm):
    class Meta:
        model = Events
        fields = ('title','cover_image',
                  'short_description','long_description',
                  'categories','start_date', 'last_date',
                  'last_date_to_apply','rulebook','website','venue',
                  'terms_and_conditions','inter_event','city')