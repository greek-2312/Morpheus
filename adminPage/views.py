from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from updatePage.models import UpdatePage
# Create your views here.


def index(request):
    user = get_user_model()
    users = user.objects.all()
    # if request.POST:
    #     return redirect('adminPageUser')
    return render(request, 'AdminPanel/adminPage.html', {'users': users})


def useradmin_page(request, id):
    user = get_user_model()
    users = user.objects.all()
    user_data = UpdatePage.objects.all()
    return render(request, 'AdminPanel/adminPageUser.html', {'user_data': user_data[id-1], 'data': users[id]})
