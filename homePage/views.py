from django.shortcuts import render
from django.http import HttpResponseRedirect


def index(request):
    if request.POST:
        return HttpResponseRedirect('/login')
    return render(request, 'homePage/homePage.html')
