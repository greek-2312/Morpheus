from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from .forms import UpdateInfoForm
from django.contrib.auth.forms import UserCreationForm, UserChangeForm


def updatePage(request):
    if request.method == 'POST':
        form = UpdateInfoForm(request.POST)
        print(form.errors)
        if form.is_valid():
            form.save()
            # weight = form.cleaned_data('weight')
            # id = form.cleaned_data('id')
            return HttpResponseRedirect('/homePage')
    else:
        form = UpdateInfoForm()
    return render(request, 'updatePage/updatePage.html', {'form': form})

