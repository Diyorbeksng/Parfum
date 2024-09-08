from django.http import HttpResponse
from django.shortcuts import render



def index(request):
    context = {
        'title':'Главная страница',
    }

    return render(request, 'main/index.html',context)


def about(request):
    context = {
        'title':'Страница о нас',
    }

    return render(request, 'main/about.html',context)
# Create your views here.
