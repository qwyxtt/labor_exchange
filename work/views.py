from django.http import HttpResponse
from django.shortcuts import render
from .models import Task
from .forms import CreateTaskForm


def index(request):
    about = 'на этой платформе мы помогаем подросткам получить свой первый заработок'
    context = {
        'main': 'Главная',
        'about': about
    }
    return render(request, 'work/index.html', context)


def task_history(request):
    context = {
        'task': Task.objects.filter(owner__user=request.user)
    }
    return render(request, 'account/task.html', context)


def create_task(request):
    form = CreateTaskForm(request.POST or None)
    error = ''
    if request.method == 'POST':
        if form.is_valid():
            cd = form.clean_data
            task = Task.objects.create(
                title=cd['title'],
                descriptions_task=cd['descriptions_task'],
                end_date=cd['end_date'],
                cost=cd['cost']
            )
        return render(request, 'account/create_task.html', context={'form': form})

