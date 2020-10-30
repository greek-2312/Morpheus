from django.db import models
from ..registration.forms import SignUpForm


class UserUpdateInfo(SignUpForm):
    gender = models.ChoiceField([('M', 'Male'),
                                ('F', 'Female')])
    weight = models.FloatField(blank=False)
    height = models.FloatField(blank=False)
    disease = models.ChoiceField([('Disease1', 'Disease'),
                                 ('Disease2', 'Disease'),
                                 ('Disease3', 'Disease'),
                                 ('Disease4', 'Disease'),
                                 ])
# Create your models here.
