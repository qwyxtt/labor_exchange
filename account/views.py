from django.shortcuts import render


def pf(request):
    return render(request, 'account/account.html', context={'title': 'аккаунт'})
