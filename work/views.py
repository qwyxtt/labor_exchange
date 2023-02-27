from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    context = {
        main: 'Главная'
    }
    return render(request,'authentications/index.html', context)
