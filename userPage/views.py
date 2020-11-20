from django.shortcuts import render
from django.shortcuts import redirect


def userPage_view(request):
    # if request.POST:
    #     return redirect('login')
    return render(request, 'userPage/userPage.html')
