from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    about = 'на этой платформе мы помогаем подросткам получить свой первый заработок'
    context = {
        'main': 'Главная',
        'about': about
    }
    return render(request, 'work/index.html', context)


