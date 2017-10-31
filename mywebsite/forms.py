from django.contrib.auth.forms import AuthenticationForm
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Event, Comment

# If you don't do this you cannot use Bootstrap CSS

class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2',)

    def clean_email(self):
        if User.objects.filter(email=self.cleaned_data.get('email', None)).count() > 0:
            raise forms.ValidationError("User with this email already exists")

        return self.cleaned_data.get('email')

    def clean_username(self):
        if User.objects.filter(username=self.cleaned_data.get('username', None)).count() > 0:
            raise forms.ValidationError("User with this username already exists")

        return self.cleaned_data.get('username')

class SignUpFormForOrganizer(UserCreationForm):
    Official_phone_num = forms.CharField(max_length=15)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', 'Official_phone_num')

    def clean_email(self):
        if User.objects.filter(email=self.cleaned_data.get('email', None)).count() > 0:
            raise forms.ValidationError("User with this email already exists")

        return self.cleaned_data.get('email')

    def clean_username(self):
        if User.objects.filter(username=self.cleaned_data.get('username', None)).count() > 0:
            raise forms.ValidationError("User with this username already exists")

        return self.cleaned_data.get('username')

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ('Event_Name', 'Organized_By', 'Event_Image',
                  'Short_Description_Of_Event','Long_Description_Of_Event',
                  'Categories','Event_Start_Date', 'Event_Last_Date',
                  'Last_Date_For_Apply','Rulebook_Of_Event','Apply_Link_Of_Event',
                  'Venue_Of_Event','Terms_and_Condtions_Of_Event')



class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('author','text')