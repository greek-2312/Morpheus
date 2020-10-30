from django.shortcuts import render


def updatePage(request):
    return render(request, 'updatePage/update-page.html')

