from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import UpdatePage
#
#
disease = (
    ('disease', 'disease'),
    ('disease', 'disease'),
    ('disease', 'disease'),
    ('disease', 'disease'),)
gender = (
    ('male', 'male'),
    ('female', 'female'),)
#
#
# class FormToMixin(UserCreationForm):
#     weight = forms.FloatField()
#     height = forms.FloatField()
#     gender = forms.ChoiceField(choices=gender)
#     disease = forms.ChoiceField(choices=disease)
#     region = forms.CharField()  # max_length=30, default='No place')
#     # id = forms.ForeignKey(user_model)
#
#     class Meta:
#         model = UserCreationForm
#         fields = ('gender', 'weight', 'height', 'disease', 'disease', 'region')


class UpdateInfoForm(UserChangeForm):
    weight = forms.FloatField()
    height = forms.FloatField()
    gender = forms.ChoiceField(choices=gender)
    disease = forms.ChoiceField(choices=disease)
    region = forms.CharField()  # max_length=30, default='No place')
    # id = forms.ForeignKey()

    class Meta:
        model = UpdatePage
        fields = {
            'gender', 'weight', 'height', 'disease', 'disease', 'region'}
