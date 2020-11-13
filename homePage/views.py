from django.shortcuts import render
from django.http import HttpResponseRedirect


def index(request):
    if request.method == 'POST':
        return HttpResponseRedirect('/registration')
    return render(request, 'homePage/homePage.html')
