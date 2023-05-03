from django.shortcuts import render
from work.models import Task, Employer


def account_of_employer(request):
    context = {
        'title': 'Мой аккаунт',
        'tasks': 'tasks'
    }
    emp = Employer.objects.get(user=request.user)
    tasks = Task.objects.filter(owner=emp)
    #if tasks.exists():
    return render(request, 'account/account.html', context)
