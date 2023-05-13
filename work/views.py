from django.http import HttpResponse
from django.shortcuts import redirect, render
from .models import Task, Employer, Employee
from django.shortcuts import get_object_or_404
from django.contrib import messages
from django.db import transaction
from .forms import CreateTaskForm


def index(request):
    context = {
        'main': 'Главная',
        'about': 'наш сайта предлогает следущий перечень услуг',
        'k': 'k',
        'l': 'l',
        'p': 'p',
    }
    return render(request, 'work/index.html', context)


def task_history(request):
    context = {
        'tasks': Task.objects.filter(owner__user=request.user, is_active=True)
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
                city=cd['city']
            )
            task.owner = obj
            task.save()
            return redirect('success')
    return render(request, 'account/create_task.html', context={'form': form})


def task_history_employee(request):
    context = {
        'task': Task.objects.filter(executor__user=request.user)
    }
    return render(request, 'account/history_of_task.html', context)


def work(request):
    context = {
        'info': 'Здесь вы можете выбрать работу на свой вкус',
        'tasks': Task.objects.filter(is_active=True)
    }
    my_data = Task.objects.all()
    my_filter = request.GET.get('filter')
    my_sort = request.GET.get('sort')
    if my_filter:
        my_data = my_data.filter(my_field=my_filter)
    if my_sort:
        my_data = my_data.order_by(my_sort)

    context = {
        'my_data': my_data,
        'my_filter': my_filter,
        'my_sort': my_sort,
    }
    return render(request, 'account/work.html', context)


def accept_task(request, task_id):
    task = Task.objects.get(pk=task_id)
    return render(request, 'account/accept_task.html', context={'task': task})


def go_to_task(request, task_id):
    try:
        employee = Employee.objects.get(user=request.user)
        if Task.objects.filter(executor=employee, is_active=True).exists():
            msg = 'У вас уже есть активное задание - {}'.format(
                Task.objects.get(executor=employee, is_active=True).title
            )
            messages.add_message(request, messages.ERROR, msg)
        else:
            task = Task.objects.get(pk=task_id)
            task.executor = employee
            task.save()
    except Employee.DoesNotExist:
        msg = 'Вы не являетесь работником'
        messages.add_message(request, messages.ERROR, msg)

    return redirect('get_work')


@transaction.atomic
def end_task(request, task_id):
    try:
        task = Task.objects.get(pk=task_id)
        if request.user == task.owner.user:
            task.is_active = False
            task.owner.balance -= task.cost
            task.executor.balance += task.cost
            task.owner.full_clean()
            task.save()
            task.owner.save()
            task.executor.save()
        else:
            msg = 'Вы не является владельцем задания'
            messages.add_message(request, messages.ERROR, msg)
    except Task.DoesNotExist:
        msg = 'Такого задания нету'
        messages.add_message(request, messages.ERROR, msg)
    return render(request, 'work/end_task.html', context={'task_id': task_id})
