from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import user_model
from datetime import date


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')
    date = forms.DateField()
    password1 = forms.CharField(max_length=20, required=False, help_text='Optional.')
    password2 = password1

    class Meta:
        abstract = True
        model = user_model
        fields = ('first_name', 'last_name', 'email', 'date', 'password1', 'password2')
