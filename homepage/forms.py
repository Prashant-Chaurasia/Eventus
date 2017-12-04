from django import forms
from .models import Contact


class ContactForm(forms.ModelForm):
    Name = forms.CharField(widget = forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Name', 'id':'name'}))
    Email = forms.EmailField(widget = forms.EmailInput(attrs={'class': 'form-control','placeholder':'Email'}))
    Comment = forms.CharField(widget = forms.Textarea(attrs={'class': 'form-control', 'placeholder':'Comments','rows': '5'}))

    class Meta:
        model = Contact
        fields = {'Name', 'Email', 'Comment'}
