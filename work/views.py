from django.http import HttpResponse
from django.shortcuts import redirect, render
from .models import Task
from .forms import CreateTaskForm


def index(request):
    context = {
        'main': 'Главная',
        'about': 'на этой платформе мы помогаем подросткам получить свой первый заработок'
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
            cd = form.cleaned_data
            task = Task.objects.create(
                title=cd['title'],
                description=cd['description'],
                end_date=cd['end_date'],
                cost=cd['cost']
            )
            task.owner = request.user
            task.save()
            return redirect('success')
    return render(request, 'account/create_task.html', context={'form': form})

