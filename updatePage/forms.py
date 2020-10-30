from django import forms
from ..registration.forms import SignUpForm


class FormToMixin(forms.ModelForm):
    gender = forms.ChoiceField([('M', 'Male'),
                                ('F', 'Female')])
    weight = forms.FloatField(blank=False)
    height = forms.FloatField(blank=False)
    disease = forms.ChoiceField([('Disease1', 'Disease'),
                                 ('Disease2', 'Disease'),
                                 ('Disease3', 'Disease'),
                                 ('Disease4', 'Disease'),
                                 ])