from django.shortcuts import render
from work.models import Task, Employer


def account_of_employer(request):
    context = {
        'title': 'Мой аккаунт'
    }
    try:
        emp = Employer.objects.get(user=request.user)
        context.update({'emp': emp})
    except Employer.DoesNotExist:
        emp = Employee.objects.get(user=request.user)
        context.update({'emp': emp})
    return render(request, 'account/account.html', context)
