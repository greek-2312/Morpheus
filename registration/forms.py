from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import user_model
from datetime import date
from django.contrib.auth import authenticate


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
        fields = ('first_name', 'last_name', 'email', 'date', 'password1', 'password2',)


class AccountAuthenticationForm(forms.ModelForm):

    password = forms.CharField()

    class Meta:
        model = user_model
        fields = ('email', 'password')

    def clean(self):
        if self.is_valid():
            email = self.cleaned_data['email']
            password = self.cleaned_data['password']
            if not authenticate(email=email, password=password):
                raise forms.ValidationError("Invalid Login")
