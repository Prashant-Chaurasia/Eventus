from django import forms
from .models import Events

class EventForm(forms.ModelForm):
    class Meta:
        model = Events
        fields = ('title','cover_image',
                  'description','categories','start_date', 'last_date',
                  'last_date_to_apply','rulebook','website','venue','college',
                    'inter_event')