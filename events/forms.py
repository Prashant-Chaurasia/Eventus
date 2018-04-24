from django import forms
from .models import Events
from material import *

class EventForm(forms.ModelForm):
    class Meta:
        model = Events

        widgets = {
            'start_date': forms.DateTimeInput(attrs={'class': 'datetime-input'})
        }

        fields = ('title','cover_image',
                  'description','categories','start_date', 'last_date',
                  'last_date_to_apply','rulebook','website','facebook_link','venue','college',
                    'inter_event','register','no_of_tickets')