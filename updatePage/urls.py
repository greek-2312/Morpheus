from django.urls import path, include
from . import views


urlpatterns = [
    path("", views.updatePage_view, name="updatePage"),
]
