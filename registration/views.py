from django.contrib.auth import login, authenticate
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect


from .forms import SignUpForm


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        print(form.errors)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            raw_password = form.cleaned_data.get('password')
            user = authenticate(username=email, password=raw_password)
            # login(request, user)
            return HttpResponseRedirect('/updatePage')
    else:
        form = SignUpForm()
    return render(request, 'registration/registration.html', {'form': form})
