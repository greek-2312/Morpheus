from django.urls import path, include
from . import views


urlpatterns = [
    # path('', views.adminPageUser_views, name='adminPageUser'),
    path('', views.index, name='index'),
    path('<int:id>', views.useradmin_page, name='userAdminPage')
]
