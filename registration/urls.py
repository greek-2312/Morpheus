from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path("", views.registration_view, name="registration"),
    path("", views.login_view, name="login"),
    path("", views.logout_view, name="logout"),
]
