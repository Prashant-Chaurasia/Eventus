from django import forms
from.models import Suggest


class SuggestForm(forms.ModelForm):
    class Meta:
        model = Suggest
        fields = ('Name', 'Details')
