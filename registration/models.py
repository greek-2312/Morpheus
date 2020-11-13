from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from datetime import date
from django.contrib.auth.models import PermissionsMixin


class MyAccountManager(BaseUserManager):
    def create_user(self, first_name, last_name, email, date, password):
        if not email:
            raise ValueError("User name required")
        user = self.model(
            first_name=first_name,
            last_name=last_name,
            email=self.normalize_email(email),
            password=password,
            date=date,
            # weight=weight,
            # height=height,
            # disease=disease,
            # gender=gender,
            # region=region,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, first_name, last_name, date, password=None):
        user = self.create_user(
            first_name=first_name,
            last_name=last_name,
            date=date,
            email=self.normalize_email(email),
            password=password,
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


# disease = (
#     ('no disease', ' no disease'),
#     ('disease2', 'disease2'),
#     ('disease3', 'disease3'),
#     ('disease4', 'disease4'),)
# gender = (
#     ('M', 'Male'),
#     ('F', 'Female'),)


class user_model(AbstractBaseUser, PermissionsMixin):
    id = models.AutoField(primary_key=True)
    # username = models.CharField(max_length=20, blank=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(verbose_name='email', unique=True)
    date = models.DateField(default=None)
    password = models.CharField(max_length=20)
    is_admin = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    # weight = models.FloatField(default=1)
    # height = models.FloatField(default=1)
    # gender = models.CharField(max_length=20, choices=gender, default='Male')
    # disease = models.CharField(max_length=20, choices=disease, default='no disease')
    # region = models.CharField(max_length=30, default='No place')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['password', 'first_name', 'last_name', 'date']

    objects = MyAccountManager()

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True
