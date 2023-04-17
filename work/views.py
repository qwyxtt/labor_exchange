from django.http import HttpResponse
from django.shortcuts import redirect, render
from .models import Task, Employer, Employee
from django.shortcuts import get_object_or_404

from .forms import CreateTaskForm


def index(request):
    context = {
        'main': 'Главная',
        'about': 'на этой платформе мы помогаем подросткам получить свой первый заработок'
    }
    return render(request, 'work/index.html', context)


def task_history(request):
    context = {
        'tasks': Task.objects.filter(owner__user=request.user)
    }
    return render(request, 'account/task.html', context)


def create_task(request):
    form = CreateTaskForm(request.POST or None)
    error = ''
    if request.method == 'POST':
        if form.is_valid():
            cd = form.cleaned_data
            obj = get_object_or_404(Employer, user=request.user)
            task = Task.objects.create(
                title=cd['title'],
                description=cd['description'],
                end_date=cd['end_date'],
                cost=cd['cost'],
                is_active=cd['is_active']
            )
            task.owner = obj
            task.save()
            return redirect('success')
    return render(request, 'account/create_task.html', context={'form': form})


def task_history_employee(request):
    context = {
        'task': Task.objects.filter(executor__user=request.user)
    }
    return render(request, 'account/task.html', context)


def work(request):
    context = {
        'info': 'здесь вы можете выбрать работу на свой вкус',
        'tasks': Task.objects.filter(is_active=True)
    }
    return render(request, 'account/work.html', context)


def accept_task(request, task_id):
    task = Task.objects.get(pk=task_id)
    return render(request, 'account/accept_task.html', context={'task': task})


def go_to_task(request, task_id):
    if request.user.activity == 'Employee':
        task = Task.objects.get(pk=task_id)
        task.executor = CustomUser
    return redirect('get_work')
