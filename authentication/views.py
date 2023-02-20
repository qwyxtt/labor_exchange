from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from .models import CustomUser
from .forms import SignUpForm, LoginForm
from django.contrib.auth.decorators import login_required


def signup(request):
    form = SignUpForm(request.POST or None)
    error = ''
    if request.method == 'POST':
        if form.is_valid():
            cd = form.cleaned_data
            user = CustomUser.objects.create_user(
                full_name=cd['full_name'],
                email=cd['email'],
                password1=cd['password1'],
                birthdate=cd['birthdate'],
                activity=cd['activity']
            )
            user.is_active = True
            user.set_password(cd['password1'])
            user.save()

            return redirect('main')
        error += 'User with such email already exists'

    return render(request, template_name='authentications/signup.html', context={
        'form': form,
        'title': 'Signup',
        'error': error
    })


def login_view(request):
    form = LoginForm(request.POST or None)
    error = ''
    if request.method == 'POST':
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(email=cd['email'], password=cd['password'])
            if user is not None:
                login(request, user)
                return redirect('main')
            error += 'Username or password are incorrect'
    return render(request, 'authentications/login.html', context={
        'form': form,
        'error': error
    })


@login_required
def logout_view(request):
    logout(request)
    return redirect('success')
