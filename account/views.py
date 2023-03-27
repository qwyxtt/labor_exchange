from django.shortcuts import render


def account_of_employer(request):
    return render(request, 'account/account.html', context={'title': ' мой аккаунт'})
