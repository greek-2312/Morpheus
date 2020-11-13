from django.db import models
from PBLProject import settings
from django.contrib.auth.models import AbstractUser


disease = (
    ('no disease', ' no disease'),
    ('disease', 'disease'),
    ('disease', 'disease'),
    ('disease', 'disease'),)
gender = (
    ('male', 'male'),
    ('female', 'female'),)


class UpdatePage(models.Model):
    id = models.ForeignKey(settings.AUTH_USER_MODEL, unique=True, primary_key=True, on_delete=models.CASCADE,
                           db_column='id')
    weight = models.FloatField(default=1)
    height = models.FloatField(default=1)
    gender = models.CharField(max_length=20, choices=gender, default='Male')
    disease = models.CharField(max_length=20, choices=disease, default='no disease')
    region = models.CharField(max_length=30, default='No place')
